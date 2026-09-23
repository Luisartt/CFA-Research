from __future__ import annotations

import copy
from pathlib import Path

import pytest
from docx import Document
from docx.shared import Mm

from report_fixtures import HEADER, SECTIONS, report_project, write_report_project  # noqa: F401
from build_docx import BUDGET_PAGES, main, parse_markdown
from charts import main as draw_charts


def _build(project: Path) -> Path:
    draw_charts(["--project", str(project)])
    assert main(["--project", str(project)]) == 0
    return project / "report" / "ACME_report_v1.docx"


def test_builds_a4_body_with_header_sections_and_figures(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    section = doc.sections[0]
    assert abs(section.page_width - Mm(210)) < Mm(1) and abs(section.page_height - Mm(297)) < Mm(1)  # type: ignore[operator]
    text = "\n".join(p.text for p in doc.paragraphs)
    for heading in ("Investment summary", "Business description", "Valuation", "Appendix"):
        assert heading in text
    assert "Figure 1: Revenue and EBITDA margin" in text
    assert len(doc.inline_shapes) == 1
    usable = section.page_width - section.left_margin - section.right_margin  # type: ignore[operator]
    assert all(shape.width <= usable for shape in doc.inline_shapes)


def test_header_block_has_the_required_fields(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    header_text = " ".join(cell.text for row in doc.tables[0].rows for cell in row.cells)
    for expected in ("Acme Alimentos", "BMV: ACME", "Consumer Staples / Packaged Foods", "BUY",
                     "MXN 25.00 (2026-10-14)", "MXN 31.00 (+24.0%)"):
        assert expected in header_text, expected


def test_markdown_tables_and_inline_formatting(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    assert len(doc.tables) == 2  # header block + the valuation table
    assert doc.tables[1].rows[0].cells[0].text == "Method"
    bold_runs = [r.text for p in doc.paragraphs for r in p.runs if r.bold]
    assert "BUY" in bold_runs


def test_appendix_starts_on_a_new_page(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    xml = doc.element.body.xml
    assert xml.index('w:type="page"') < xml.index(">Appendix<")


def test_versions_are_never_overwritten(report_project: Path) -> None:
    _build(report_project)
    assert main(["--project", str(report_project)]) == 0
    assert (report_project / "report" / "ACME_report_v1.docx").is_file()
    assert (report_project / "report" / "ACME_report_v2.docx").is_file()


def test_check_mode_reports_budget_and_uncited(report_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(report_project), "--check"]) == 0
    out = capsys.readouterr().out
    assert out.isascii()
    assert "investment-summary" in out and "pages" in out
    assert "uncited" in out and "Our DCF gives 31 per share" in out
    assert not list((report_project / "report").glob("*.docx"))


def test_check_mode_flags_over_budget(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    sections = copy.deepcopy(SECTIONS)
    sections["02-business-description.md"] = "# Business description\n\n" + ("word " * 600) + "\n"
    project = write_report_project(tmp_path, sections=sections)
    main(["--project", str(project), "--check"])
    assert "[over] business-description" in capsys.readouterr().out


def test_missing_header_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_report_project(tmp_path, header=None)
    assert main(["--project", str(project)]) == 2
    assert "header.yaml" in capsys.readouterr().out


def test_bad_recommendation_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    header = dict(HEADER)
    header["recommendation"] = "STRONG BUY"
    project = write_report_project(tmp_path, header=header)
    assert main(["--project", str(project)]) == 2
    assert "recommendation" in capsys.readouterr().out


def test_parser_blocks() -> None:
    blocks = parse_markdown("# Title\n\nPara one\nstill one.\n\n- a\n- b\n\n1. x\n\n![Cap](c.png)\n\n| A | B |\n|---|---|\n| 1 | 2 |\n")
    assert [b.kind for b in blocks] == ["heading", "paragraph", "bullet", "bullet", "number", "image", "table"]
    assert blocks[1].text == "Para one still one."
    assert blocks[6].rows == [["A", "B"], ["1", "2"]]


def test_budget_covers_the_seven_graded_sections() -> None:
    assert set(BUDGET_PAGES) == {"investment-summary", "business-description", "industry", "financial-analysis",
                                 "valuation", "risks", "esg"}
    assert sum(BUDGET_PAGES.values()) == 10
