from __future__ import annotations

from pathlib import Path

import pytest
from deck_fixtures import deck_project, write_template  # noqa: F401  (import first: sets sys.path)
from pptx import Presentation
from pptx.util import Inches, Pt

from audit_pptx import Finding, audit, main
from build_pptx import main as build


def _built(project: Path) -> Path:
    assert build(["--project", str(project)]) == 0
    return project / "pitch" / "ACME_deck_v1.pptx"


def _codes(findings: list[Finding]) -> set[str]:
    return {f.code for f in findings}


def test_built_deck_has_no_errors(deck_project: Path) -> None:
    findings = audit(_built(deck_project), deck_project)
    assert not [f for f in findings if f.severity == "ERROR"], findings


def test_planted_problems_are_found(deck_project: Path) -> None:
    path = _built(deck_project)
    prs = Presentation(str(path))
    extra = prs.slides.add_slide(prs.slide_layouts[5])  # Title Only, no sources, no notes
    extra.shapes.title.text = "Our target price is MXN 40.0 with a WACC of 9.0%"
    box = extra.shapes.add_textbox(Inches(9), Inches(1), Inches(3), Inches(1))  # runs off a 10in slide
    box.text_frame.text = "Click to add text"
    box.text_frame.paragraphs[0].font.size = Pt(7)
    box.text_frame.paragraphs[0].font.name = "Comic Sans MS"
    prs.save(str(path))
    codes = _codes(audit(path, deck_project))
    for code in ("no-sources", "no-notes", "leftover", "off-slide", "small-font", "stale-target", "stale-wacc"):
        assert code in codes, code


def test_too_many_slides(deck_project: Path) -> None:
    path = _built(deck_project)
    prs = Presentation(str(path))
    for _ in range(12):
        prs.slides.add_slide(prs.slide_layouts[6])
    prs.save(str(path))
    assert "slide-count" in _codes(audit(path, deck_project))


def test_report_file_and_ascii_output(deck_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    _built(deck_project)
    assert main(["--project", str(deck_project)]) == 0
    assert (deck_project / "pitch" / "deck-audit.md").is_file()
    out = capsys.readouterr().out
    assert out.isascii() and "ACME_deck_v1.pptx" in out


def test_fix_removes_empty_placeholders_and_off_palette_fonts(deck_project: Path) -> None:
    path = _built(deck_project)
    prs = Presentation(str(path))
    slide = prs.slides.add_slide(prs.slide_layouts[1])  # title + empty body placeholder
    slide.shapes.title.text = "Extra"
    slide.shapes.title.text_frame.paragraphs[0].runs[0].font.name = "Comic Sans MS"
    prs.save(str(path))
    assert main(["--project", str(deck_project), "--fix"]) == 0
    fixed = Presentation(str(deck_project / "pitch" / "ACME_deck_v2.pptx"))
    last = fixed.slides[len(fixed.slides) - 1]
    assert all(ph.text_frame.text.strip() for ph in last.placeholders if ph.has_text_frame)
    fonts = {r.font.name for p in last.shapes.title.text_frame.paragraphs for r in p.runs}
    assert "Comic Sans MS" not in fonts
    assert (deck_project / "pitch" / "ACME_deck_v1.pptx").is_file()  # original kept


def test_no_deck_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "pitch").mkdir()
    assert main(["--project", str(tmp_path)]) == 2
    assert "no deck" in capsys.readouterr().out
