# Phase 3b — Pitch and Deck Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the presentation half: a `pitch` skill (10-minute outline, speaker notes, timing, scored judge Q&A drill) and a `deck` skill that builds a .pptx from that outline on the team's own template and audits any deck against the Challenge rules.

**Architecture:** `pitch` writes `pitch/outline.yaml` (machine-readable source of truth) and `pitch/qa-drill.md`. Two pure-Python tools in `skills/deck/tools/` (python-pptx): `build_pptx.py` (inspect template layouts, clear example slides, one slide per outline entry, charts from `report/charts/`, a named "Sources" footer on every slide, speaker notes in the notes field, versioned output) and `audit_pptx.py` (structural checks: slide count for 10 minutes, sources, notes, leftovers, fonts, sizes, overflow estimate, bounds, stale numbers vs `model-summary.json` / `report/header.yaml`; `--fix` only for mechanical issues). Workflow ideas (inspect the template first, structural edits before text, notes in the notes field, leftover-placeholder check) are inspired by Anthropic's pptx skill; no text or code is copied from it.

**Tech Stack:** Python 3.10+, python-pptx (bundles Pillow), PyYAML; pytest + mypy strict; Markdown skills.

**Spec:** `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` §8. Refinement recorded in Task 7: the outline is `pitch/outline.yaml`, not `outline.md`.

**Rules (2026-2027 Official Rules):** presentation 10 minutes; Q&A 10 minutes at the local final (15 at regional/global finals, none at the recorded sub-regional round); every slide shows its sources; no handouts or props; English from sub-regional up. Presentation scoring /100: Financial analysis 20, Valuation 20, ESG 10, Presentation 20, Q&A 20, Team involvement 5, Materials 5. Judges likely ask about AI use.

**Branch:** `feat/phase3b-deck` (exists).

---

## File map

| File | Responsibility |
|---|---|
| `pyproject.toml` | python-pptx dependency, test path, mypy |
| `skills/deck/tools/build_pptx.py` | outline + template -> versioned deck; `--list-layouts` |
| `skills/deck/tools/audit_pptx.py` | structural audit, `deck-audit.md`, `--fix` |
| `skills/deck/tools/tests/deck_fixtures.py` | fixture writer (template, outline, charts, summary, header) — NOT a conftest.py |
| `skills/deck/tools/tests/test_build_pptx.py`, `test_audit_pptx.py` | tests |
| `skills/pitch/SKILL.md` + `references/pitch-structure.md`, `outline-template.yaml`, `qa-bank.md` | outline, notes, timing, Q&A drill |
| `skills/deck/SKILL.md` + `references/deck-design.md` | build, audit, visual check |
| integration | structural tests, AGENTS template, README, manifests 0.4.0, evals, spec |

---

### Task 1: Tooling and fixtures

**Files:**
- Modify: `pyproject.toml`
- Create: `skills/deck/tools/tests/deck_fixtures.py`

- [ ] **Step 1: `pyproject.toml`**

  - `dependencies`: add `"python-pptx>=1.0"`.
  - `testpaths`: add `"skills/deck/tools/tests"`.
  - `[tool.mypy]` `mypy_path`: `"skills/model/engine,skills/report/tools,skills/deck/tools"`.
  - `[[tool.mypy.overrides]]` `module`: add `"pptx"` and `"pptx.*"`.

- [ ] **Step 2: Install** — `python -m pip install "python-pptx>=1.0"` (already present on the dev machine is fine).

- [ ] **Step 3: Create `skills/deck/tools/tests/deck_fixtures.py`**

```python
"""Fixtures for the deck tools (a plain module, not conftest.py: two conftest modules collide).

Import this module FIRST in test files: it puts skills/deck/tools on sys.path.
"""

from __future__ import annotations

import json
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest
import yaml

TOOLS_DIR = Path(__file__).resolve().parent.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from pptx import Presentation  # noqa: E402

OUTLINE: dict[str, Any] = {
    "deck": {"title": "Acme Alimentos (BMV: ACME) - BUY, target MXN 31.0", "language": "en", "minutes": 10},
    "slides": [
        {"kind": "title", "title": "Acme Alimentos (BMV: ACME)", "subtitle": "BUY - target MXN 31.0 (+24%)",
         "notes": "Open with the recommendation.", "speaker": "Ana", "minutes": 0.5},
        {"kind": "content", "title": "Investment thesis", "bullets": ["Volume recovery", "Margin expansion"],
         "sources": "Company filings; team model", "notes": "Three pillars.", "speaker": "Ana", "minutes": 1.5},
        {"kind": "content", "title": "Revenue and margins", "bullets": ["Revenue grows 6% a year", "EBITDA margin 19-20%"],
         "chart": "revenue-margin", "sources": "Team model", "notes": "Walk the chart.", "speaker": "Luis",
         "minutes": 1.5},
        {"kind": "chart", "title": "Valuation summary", "chart": "football-field",
         "sources": "Team model; market data (2026-10-14)", "notes": "DCF vs comps.", "speaker": "Luis",
         "minutes": 1.5},
        {"kind": "section", "title": "Risks and ESG", "sources": "Team analysis", "notes": "", "speaker": "Eva",
         "minutes": 0.2},
    ],
}

SUMMARY: dict[str, Any] = {"valuation": {"wacc": 0.1245, "price_gordon": 13.43, "upside_gordon": 0.24}}
HEADER: dict[str, Any] = {"ticker": "ACME", "target_price": 31.0, "price": 25.0, "currency": "MXN"}


def _chart(path: Path, wide: bool) -> None:
    fig, ax = plt.subplots(figsize=(6.3, 3.0) if wide else (3.2, 2.3))
    ax.plot([1, 2, 3], [1, 4, 9])
    fig.savefig(path, dpi=100)
    plt.close(fig)


def write_template(path: Path, example_slides: int = 1) -> Path:
    prs = Presentation()
    for _ in range(example_slides):
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = "Example slide from the template"
    path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(path))
    return path


def write_deck_project(root: Path, outline: Mapping[str, Any] | None = OUTLINE, template: bool = True,
                       charts: bool = True) -> Path:
    for folder in ("pitch", "report/charts", "model", "report"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    (root / "company-profile.yaml").write_text(
        yaml.safe_dump({"company": {"name": "Acme Alimentos", "ticker": "ACME"}}), encoding="utf-8")
    if outline is not None:
        (root / "pitch" / "outline.yaml").write_text(yaml.safe_dump(dict(outline), sort_keys=False), encoding="utf-8")
    if template:
        write_template(root / "pitch" / "template.pptx")
    if charts:
        _chart(root / "report" / "charts" / "revenue-margin.png", wide=False)
        _chart(root / "report" / "charts" / "football-field.png", wide=True)
    (root / "model" / "model-summary.json").write_text(json.dumps(SUMMARY), encoding="utf-8")
    (root / "report" / "header.yaml").write_text(yaml.safe_dump(HEADER), encoding="utf-8")
    return root


@pytest.fixture
def deck_project(tmp_path: Path) -> Path:
    return write_deck_project(tmp_path)
```

- [ ] **Step 4: Verify collection** — `python -m pytest -q skills/deck/tools/tests` -> `no tests ran` (exit 5 fine); bare `python -m pytest -q` still passes (365).

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml skills/deck/tools/tests/deck_fixtures.py
git commit -m "test(deck): tooling and deck project fixtures"
```

---

### Task 2: Deck builder (`build_pptx.py`)

**Files:**
- Create: `skills/deck/tools/build_pptx.py`
- Test: `skills/deck/tools/tests/test_build_pptx.py`

- [ ] **Step 1: Write the failing tests** — `skills/deck/tools/tests/test_build_pptx.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

import pytest
from deck_fixtures import OUTLINE, deck_project, write_deck_project  # noqa: F401  (import first: sets sys.path)
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

from build_pptx import SOURCES_NAME, main, pick_layout


def _build(project: Path) -> object:
    assert main(["--project", str(project)]) == 0
    return Presentation(str(project / "pitch" / "ACME_deck_v1.pptx"))


def test_one_slide_per_outline_entry_and_template_examples_removed(deck_project: Path) -> None:
    prs = _build(deck_project)
    assert len(prs.slides) == len(OUTLINE["slides"])
    titles = [s.shapes.title.text if s.shapes.title is not None else "" for s in prs.slides]
    assert "Example slide from the template" not in titles
    assert titles[1] == "Investment thesis"


def test_sources_footer_on_every_slide_but_the_title(deck_project: Path) -> None:
    prs = _build(deck_project)
    for i, slide in enumerate(prs.slides):
        if i == 0:
            continue
        footers = [sh for sh in slide.shapes if sh.name == SOURCES_NAME]
        assert len(footers) == 1, i
        assert footers[0].text_frame.text.startswith("Source: ")


def test_speaker_notes_in_the_notes_field(deck_project: Path) -> None:
    prs = _build(deck_project)
    notes = prs.slides[1].notes_slide.notes_text_frame.text
    assert "Ana" in notes and "Three pillars." in notes


def test_charts_placed_inside_the_slide(deck_project: Path) -> None:
    prs = _build(deck_project)
    pictures = [sh for s in prs.slides for sh in s.shapes if sh.shape_type == MSO_SHAPE_TYPE.PICTURE]
    assert len(pictures) == 2
    for slide in prs.slides:
        for sh in slide.shapes:
            if sh.left is None or sh.width is None:
                continue
            assert sh.left >= 0 and sh.top >= 0
            assert sh.left + sh.width <= prs.slide_width and sh.top + sh.height <= prs.slide_height


def test_bullets_land_on_the_slide(deck_project: Path) -> None:
    prs = _build(deck_project)
    text = " ".join(sh.text_frame.text for sh in prs.slides[1].shapes if sh.has_text_frame)
    assert "Volume recovery" in text and "Margin expansion" in text


def test_no_empty_placeholders_left(deck_project: Path) -> None:
    prs = _build(deck_project)
    for slide in prs.slides:
        for ph in slide.placeholders:
            assert not ph.has_text_frame or ph.text_frame.text.strip(), ph.name


def test_versions_are_never_overwritten(deck_project: Path) -> None:
    _build(deck_project)
    assert main(["--project", str(deck_project)]) == 0
    assert (deck_project / "pitch" / "ACME_deck_v2.pptx").is_file()


def test_plain_default_when_no_template(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_deck_project(tmp_path, template=False)
    assert main(["--project", str(project)]) == 0
    out = capsys.readouterr().out
    assert out.isascii() and "no template" in out


def test_missing_sources_is_an_error(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["slides"][1]["sources"] = ""
    project = write_deck_project(tmp_path, outline=outline)
    assert main(["--project", str(project)]) == 2
    assert "sources" in capsys.readouterr().out


def test_missing_chart_is_an_error(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_deck_project(tmp_path, charts=False)
    assert main(["--project", str(project)]) == 2
    assert "revenue-margin" in capsys.readouterr().out


def test_long_outline_warns_about_time(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    outline = copy.deepcopy(OUTLINE)
    outline["slides"][1]["minutes"] = 9
    project = write_deck_project(tmp_path, outline=outline)
    assert main(["--project", str(project)]) == 0
    assert "minutes" in capsys.readouterr().out


def test_list_layouts(deck_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(deck_project), "--list-layouts"]) == 0
    out = capsys.readouterr().out
    assert out.isascii() and "Title Slide" in out and "Two Content" in out


def test_layout_choice_on_the_default_template() -> None:
    prs = Presentation()
    assert pick_layout(prs, "title", False).name == "Title Slide"
    assert pick_layout(prs, "section", False).name == "Section Header"
    assert pick_layout(prs, "content", False).name == "Title and Content"
    assert pick_layout(prs, "content", True).name == "Two Content"
    assert pick_layout(prs, "chart", True).name == "Title Only"
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest -q skills/deck/tools/tests/test_build_pptx.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'build_pptx'`.

- [ ] **Step 3: Implement `skills/deck/tools/build_pptx.py`**

```python
"""Build the pitch deck (.pptx) from pitch/outline.yaml on the team's own template.

Template: --template <file>, else pitch/template.pptx, else python-pptx's plain default.
Example slides already in the template are removed; its layouts, theme, fonts and colors
are kept. Every slide except the title gets a "Sources" footer (Challenge rule: slides
show their sources); speaker notes go in the notes field. Output (never overwritten):
pitch/<TICKER>_deck_v<N>.pptx.

Usage: python build_pptx.py --project <team folder> [--template <file>] [--list-layouts]
Console output is ASCII only.
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import PP_PLACEHOLDER
from pptx.exc import PackageNotFoundError
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_IO_ERROR = 4
KINDS = ("title", "section", "content", "chart")
DEFAULT_MINUTES = 10.0
MAX_BULLETS = 6
MAX_BULLET_WORDS = 20
MARGIN = Inches(0.5)
FOOTER_HEIGHT = Inches(0.4)
GAP = Inches(0.15)
SOURCES_NAME = "Sources"
SOURCE_GREY = RGBColor(0x59, 0x59, 0x59)
TITLE_TYPES = {PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE}
BODY_TYPES = {PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT}


class DeckInputError(Exception):
    def __init__(self, messages: list[str]) -> None:
        super().__init__("; ".join(messages))
        self.messages = messages


@dataclass(frozen=True)
class SlideSpec:
    kind: str
    title: str
    subtitle: str = ""
    bullets: tuple[str, ...] = ()
    chart: str = ""
    notes: str = ""
    sources: str = ""
    speaker: str = ""
    minutes: float = 0.0


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except UnicodeDecodeError:
        raise DeckInputError([f"{path.name} is not saved as UTF-8; re-save it as UTF-8"]) from None
    except yaml.YAMLError as exc:
        raise DeckInputError([f"{path.name} is not valid YAML: {exc}"]) from None


def load_outline(path: Path, charts_dir: Path) -> tuple[dict[str, Any], list[SlideSpec], list[str]]:
    if not path.is_file():
        raise DeckInputError(["pitch/outline.yaml not found: run the pitch skill first"])
    doc = _read_yaml(path)
    if not isinstance(doc, dict) or not isinstance(doc.get("slides"), list) or not doc["slides"]:
        raise DeckInputError(["pitch/outline.yaml needs a non-empty 'slides:' list"])
    deck = doc.get("deck") if isinstance(doc.get("deck"), dict) else {}
    problems: list[str] = []
    warnings: list[str] = []
    slides: list[SlideSpec] = []
    for n, raw in enumerate(doc["slides"], start=1):
        if not isinstance(raw, dict):
            problems.append(f"slide {n}: must be a mapping")
            continue
        kind, title = str(raw.get("kind", "content")), str(raw.get("title", "")).strip()
        where = f"slide {n} ({title or 'untitled'})"
        if kind not in KINDS:
            problems.append(f"{where}: kind must be one of {', '.join(KINDS)}")
        if not title:
            problems.append(f"slide {n}: title is missing")
        bullets = raw.get("bullets") or []
        if not isinstance(bullets, list) or not all(isinstance(b, str) for b in bullets):
            problems.append(f"{where}: bullets must be a list of text lines")
            bullets = []
        if len(bullets) > MAX_BULLETS:
            warnings.append(f"{where}: {len(bullets)} bullets; judges read slides fast - keep to {MAX_BULLETS} or fewer")
        if any(len(b.split()) > MAX_BULLET_WORDS for b in bullets):
            warnings.append(f"{where}: a bullet has more than {MAX_BULLET_WORDS} words; shorten it")
        chart = str(raw.get("chart") or "").strip()
        if kind == "chart" and not chart:
            problems.append(f"{where}: a chart slide needs 'chart:' (a PNG name in report/charts)")
        if chart and not (charts_dir / f"{chart}.png").is_file():
            problems.append(f"{where}: chart '{chart}' not found in report/charts (run the report skill's charts.py)")
        sources = str(raw.get("sources") or "").strip()
        if kind != "title" and not sources:
            problems.append(f"{where}: every slide except the title needs sources (Challenge rule)")
        minutes = raw.get("minutes", 0)
        if isinstance(minutes, bool) or not isinstance(minutes, (int, float)) or minutes < 0:
            problems.append(f"{where}: minutes must be a number >= 0")
            minutes = 0
        slides.append(SlideSpec(kind, title, str(raw.get("subtitle") or ""), tuple(bullets), chart,
                                str(raw.get("notes") or ""), sources, str(raw.get("speaker") or ""), float(minutes)))
    if problems:
        raise DeckInputError(problems)
    limit = deck.get("minutes", DEFAULT_MINUTES)
    total = sum(s.minutes for s in slides)
    if isinstance(limit, (int, float)) and total > limit:
        warnings.append(f"planned time is {total:g} minutes, over the {limit:g}-minute limit")
    return deck, slides, warnings


def _types(layout: Any) -> set[Any]:
    return {ph.placeholder_format.type for ph in layout.placeholders}


def _bodies(layout: Any) -> int:
    return sum(1 for ph in layout.placeholders if ph.placeholder_format.type in BODY_TYPES)


def pick_layout(prs: Any, kind: str, with_chart: bool) -> Any:
    """Choose a template layout by its placeholders (works with any team template)."""
    layouts = list(prs.slide_layouts)

    def has_title(layout: Any) -> bool:
        return bool(_types(layout) & TITLE_TYPES)

    def title_only(layout: Any) -> bool:
        return has_title(layout) and _bodies(layout) == 0 and PP_PLACEHOLDER.SUBTITLE not in _types(layout)

    preferences: list[Callable[[Any], bool]]
    if kind == "title":
        preferences = [lambda l: has_title(l) and PP_PLACEHOLDER.SUBTITLE in _types(l)]
    elif kind == "section":
        preferences = [lambda l: "section" in l.name.lower(), title_only]
    elif kind == "chart":
        preferences = [title_only]
    elif with_chart:
        preferences = [lambda l: has_title(l) and _bodies(l) == 2 and "comparison" not in l.name.lower(), title_only]
    else:
        preferences = [lambda l: has_title(l) and _bodies(l) == 1]
    for predicate in [*preferences, has_title]:
        for layout in layouts:
            if predicate(layout):
                return layout
    return layouts[0]


def _clear_slides(prs: Any) -> None:
    ids = prs.slides._sldIdLst
    for sld_id in list(ids):
        prs.part.drop_rel(sld_id.rId)
        ids.remove(sld_id)


def _remove(shape: Any) -> None:
    element = shape._element
    element.getparent().remove(element)


def _fill(text_frame: Any, lines: Sequence[str]) -> None:
    text_frame.paragraphs[0].text = lines[0] if lines else ""
    for line in lines[1:]:
        text_frame.add_paragraph().text = line


def _content_box(prs: Any, slide: Any) -> tuple[int, int, int, int]:
    title = slide.shapes.title
    top = int(title.top + title.height + GAP) if title is not None and title.top is not None else int(Inches(1.4))
    height = int(prs.slide_height - top - FOOTER_HEIGHT - GAP)
    return int(MARGIN), top, int(prs.slide_width - 2 * MARGIN), height


def _picture(slide: Any, path: Path, box: tuple[int, int, int, int]) -> None:
    left, top, width, height = box
    with Image.open(path) as image:
        w_px, h_px = image.size
    scale = min(width / w_px, height / h_px)
    w, h = int(w_px * scale), int(h_px * scale)
    slide.shapes.add_picture(str(path), Emu(left + (width - w) // 2), Emu(top + (height - h) // 2), Emu(w), Emu(h))


def _textbox_bullets(slide: Any, bullets: Sequence[str], box: tuple[int, int, int, int]) -> None:
    left, top, width, height = box
    frame = slide.shapes.add_textbox(Emu(left), Emu(top), Emu(width), Emu(height)).text_frame
    frame.word_wrap = True
    _fill(frame, bullets)
    for paragraph in frame.paragraphs:
        paragraph.font.size = Pt(16)
        props = paragraph._p.get_or_add_pPr()
        props.set("marL", str(int(Inches(0.3))))
        props.set("indent", str(-int(Inches(0.3))))
        props.append(props.makeelement(qn("a:buChar"), {"char": "•"}))


def _sources(prs: Any, slide: Any, text: str) -> None:
    box = slide.shapes.add_textbox(MARGIN, Emu(prs.slide_height - FOOTER_HEIGHT),
                                   Emu(prs.slide_width - 2 * MARGIN), Emu(FOOTER_HEIGHT - Inches(0.05)))
    box.name = SOURCES_NAME
    box.text_frame.word_wrap = True
    paragraph = box.text_frame.paragraphs[0]
    paragraph.text = f"Source: {text}"
    paragraph.font.size = Pt(9)
    paragraph.font.color.rgb = SOURCE_GREY


def _add_slide(prs: Any, spec: SlideSpec, charts_dir: Path) -> None:
    layout = pick_layout(prs, spec.kind, bool(spec.chart))
    slide = prs.slides.add_slide(layout)
    used: set[int] = set()
    if slide.shapes.title is not None:
        slide.shapes.title.text = spec.title
        used.add(slide.shapes.title.placeholder_format.idx)
    placeholders = sorted((ph for ph in slide.placeholders if ph.placeholder_format.idx not in used),
                          key=lambda ph: (ph.left or 0))
    subtitles = [ph for ph in placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.SUBTITLE]
    bodies = [ph for ph in placeholders if ph.placeholder_format.type in BODY_TYPES]
    if spec.kind == "title" and subtitles and spec.subtitle:
        subtitles[0].text = spec.subtitle
        used.add(subtitles[0].placeholder_format.idx)
    chart_path = charts_dir / f"{spec.chart}.png" if spec.chart else None
    if spec.kind in ("content", "chart"):
        if spec.bullets and bodies:
            _fill(bodies[0].text_frame, spec.bullets)
            used.add(bodies[0].placeholder_format.idx)
        if chart_path is not None:
            if spec.bullets and len(bodies) >= 2:
                right = bodies[1]
                box = (int(right.left), int(right.top), int(right.width), int(right.height))
                _picture(slide, chart_path, box)
            elif spec.bullets and not bodies:
                left, top, width, height = _content_box(prs, slide)
                half = width // 2
                _textbox_bullets(slide, spec.bullets, (left, top, half - int(GAP), height))
                _picture(slide, chart_path, (left + half, top, half, height))
            else:
                _picture(slide, chart_path, _content_box(prs, slide))
        elif spec.bullets and not bodies:
            _textbox_bullets(slide, spec.bullets, _content_box(prs, slide))
    for ph in list(slide.placeholders):
        if ph.placeholder_format.idx not in used:
            _remove(ph)
    if spec.sources:
        _sources(prs, slide, spec.sources)
    header = f"[{spec.speaker} - {spec.minutes:g} min] " if spec.speaker else ""
    slide.notes_slide.notes_text_frame.text = (header + spec.notes).strip()


def _ticker(project: Path) -> str:
    profile = project / "company-profile.yaml"
    try:
        doc = _read_yaml(profile) if profile.is_file() else None
    except DeckInputError:
        doc = None
    ticker = doc.get("company", {}).get("ticker") if isinstance(doc, dict) else None
    return re.sub(r"[^A-Za-z0-9]+", "-", str(ticker or "DECK")).strip("-") or "DECK"


def build(project: Path, template: Path | None) -> tuple[Path, list[str]]:
    _, slides, warnings = load_outline(project / "pitch" / "outline.yaml", project / "report" / "charts")
    try:
        prs = Presentation(str(template)) if template is not None else Presentation()
    except PackageNotFoundError:
        raise DeckInputError([f"{template} is not a valid .pptx file"]) from None
    _clear_slides(prs)
    for spec in slides:
        _add_slide(prs, spec, project / "report" / "charts")
    out_dir = project / "pitch"
    ticker = _ticker(project)
    pattern = re.compile(rf"^{re.escape(ticker)}_deck_v(\d+)\.pptx$")
    versions = [int(m.group(1)) for p in out_dir.glob("*.pptx") if (m := pattern.match(p.name))]
    target = out_dir / f"{ticker}_deck_v{max(versions, default=0) + 1}.pptx"
    prs.save(str(target))
    return target, warnings


def list_layouts(template: Path | None) -> None:
    prs = Presentation(str(template)) if template is not None else Presentation()
    for i, layout in enumerate(prs.slide_layouts):
        kinds = ", ".join(sorted(str(ph.placeholder_format.type).split(" ")[0] for ph in layout.placeholders))
        print(f"{i}: {ascii_safe(layout.name)} | placeholders: {ascii_safe(kinds)}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the pitch deck from pitch/outline.yaml.")
    parser.add_argument("--project", default=".", help="Team project folder")
    parser.add_argument("--template", help="Team .pptx template (default: pitch/template.pptx)")
    parser.add_argument("--list-layouts", action="store_true", help="List the template's layouts and exit")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    template: Path | None = Path(args.template).resolve() if args.template else project / "pitch" / "template.pptx"
    if template is not None and not template.is_file():
        if args.template:
            print(f"[x] Template not found: {ascii_safe(args.template)}")
            return EXIT_INPUT_ERROR
        print("[warn] no template found at pitch/template.pptx: using a plain default (put your team template there)")
        template = None
    try:
        if args.list_layouts:
            list_layouts(template)
            return EXIT_OK
        target, warnings = build(project, template)
    except DeckInputError as exc:
        print("[x] Cannot build the deck. Fix these first:")
        for message in exc.messages:
            print("  - " + ascii_safe(message))
        return EXIT_INPUT_ERROR
    except OSError as exc:
        print(f"[x] Could not write the deck: {ascii_safe(exc.strerror or str(exc))}. Close it in PowerPoint and run again.")
        return EXIT_IO_ERROR
    for warning in warnings:
        print("[warn] " + ascii_safe(warning))
    print(f"[ok] deck -> pitch/{ascii_safe(target.name)}")
    print("Next: run audit_pptx.py, then open the deck in PowerPoint and check every slide.")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest -q skills/deck/tools/tests/test_build_pptx.py`
Expected: `13 passed`. python-pptx API details (e.g. `placeholder_format.type` string form in `list_layouts`, inherited `left`/`top` on placeholders) may need small adjustments — keep behavior, report changes.

- [ ] **Step 5: mypy and commit**

Run: `python -m mypy skills/deck/tools`
Expected: `Success` (typing-only fixes allowed).

```bash
git add skills/deck/tools/build_pptx.py skills/deck/tools/tests/test_build_pptx.py
git commit -m "feat(deck): build the pitch deck from the outline on the team template"
```

---

### Task 3: Deck audit (`audit_pptx.py`)

**Files:**
- Create: `skills/deck/tools/audit_pptx.py`
- Test: `skills/deck/tools/tests/test_audit_pptx.py`

- [ ] **Step 1: Write the failing tests** — `skills/deck/tools/tests/test_audit_pptx.py`

```python
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
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest -q skills/deck/tools/tests/test_audit_pptx.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'audit_pptx'`.

- [ ] **Step 3: Implement `skills/deck/tools/audit_pptx.py`**

```python
"""Audit a pitch deck against the Challenge rules and basic presentation hygiene.

Structural checks only (no rendering): slide count for a 10-minute talk, a source on
every slide but the title, speaker notes, leftover placeholder text, shapes off the
slide, small fonts, too many font families, likely text overflow, dense slides, and
numbers that disagree with model/model-summary.json and report/header.yaml.
--fix saves a NEW version with mechanical fixes only (empty placeholders removed,
off-palette fonts set to the deck's main font); everything else is reported.
Writes pitch/deck-audit.md. Console output is ASCII only.

Usage: python audit_pptx.py --project <team folder> [--deck <file>] [--fix]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from pptx import Presentation
from pptx.exc import PackageNotFoundError

EXIT_OK = 0
EXIT_NO_DECK = 2
EXIT_IO_ERROR = 4
MIN_SLIDES, MAX_SLIDES = 6, 14
MIN_FONT_PT, MIN_FOOTER_PT = 10, 8
MAX_WORDS = 60
MAX_FONT_FAMILIES = 2
DEFAULT_FONT_PT = 18
EMU_PER_PT = 12700
LEFTOVERS = ("click to add", "lorem ipsum", "todo", "[insert", "xx.x", "tbd")
TARGET_RE = re.compile(r"target(?:\s+price)?\D{0,15}?(\d[\d,]*\.?\d*)", re.IGNORECASE)
WACC_RE = re.compile(r"WACC\D{0,15}?(\d+(?:\.\d+)?)\s*%", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    slide: int  # 0 = whole deck
    severity: str  # ERROR or WARN
    code: str
    message: str


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _texts(slide: Any) -> Iterator[tuple[Any, str]]:
    for shape in slide.shapes:
        if shape.has_text_frame:
            yield shape, shape.text_frame.text


def _load_reference(project: Path) -> dict[str, float]:
    ref: dict[str, float] = {}
    header = project / "report" / "header.yaml"
    if header.is_file():
        doc = yaml.safe_load(header.read_text(encoding="utf-8-sig"))
        if isinstance(doc, dict) and isinstance(doc.get("target_price"), (int, float)):
            ref["target"] = float(doc["target_price"])
    summary = project / "model" / "model-summary.json"
    if summary.is_file():
        data = json.loads(summary.read_text(encoding="utf-8"))
        wacc = data.get("valuation", {}).get("wacc")
        if isinstance(wacc, (int, float)):
            ref["wacc_pct"] = float(wacc) * 100
    return ref


def _overflow(shape: Any, text: str) -> bool:
    if shape.width is None or shape.height is None or not text.strip():
        return False
    sizes = [r.font.size.pt for p in shape.text_frame.paragraphs for r in p.runs if r.font.size is not None]
    size = min(sizes) if sizes else DEFAULT_FONT_PT
    chars_per_line = max(1.0, (shape.width / EMU_PER_PT) / (size * 0.5))
    lines = sum(max(1, -(-len(p.text) // int(chars_per_line))) for p in shape.text_frame.paragraphs)
    capacity = (shape.height / EMU_PER_PT) / (size * 1.2)
    return lines > capacity + 0.5


def audit(path: Path, project: Path) -> list[Finding]:
    prs = Presentation(str(path))
    reference = _load_reference(project)
    findings: list[Finding] = []
    count = len(prs.slides)
    if not MIN_SLIDES <= count <= MAX_SLIDES:
        findings.append(Finding(0, "WARN", "slide-count",
                                f"{count} slides; a 10-minute talk usually needs {MIN_SLIDES}-{MAX_SLIDES}"))
    families: Counter[str] = Counter()
    for n, slide in enumerate(prs.slides, start=1):
        texts = list(_texts(slide))
        all_text = " ".join(t for _, t in texts)
        if n > 1 and not any(t.strip().lower().startswith("source") for _, t in texts):
            findings.append(Finding(n, "ERROR", "no-sources", "no 'Source:' line (Challenge rule: slides show sources)"))
        notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
        if not notes.strip():
            findings.append(Finding(n, "WARN", "no-notes", "no speaker notes"))
        lowered = all_text.lower()
        for marker in LEFTOVERS:
            if marker in lowered:
                findings.append(Finding(n, "ERROR", "leftover", f"placeholder text left: '{marker}'"))
        if len(all_text.split()) > MAX_WORDS:
            findings.append(Finding(n, "WARN", "dense", f"{len(all_text.split())} words; aim for under {MAX_WORDS}"))
        for shape in slide.shapes:
            if None not in (shape.left, shape.top, shape.width, shape.height) and (
                    shape.left < 0 or shape.top < 0 or shape.left + shape.width > prs.slide_width
                    or shape.top + shape.height > prs.slide_height):
                findings.append(Finding(n, "ERROR", "off-slide", f"'{shape.name}' extends beyond the slide"))
        for shape, text in texts:
            is_footer = text.strip().lower().startswith("source")
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.font.name:
                        families[run.font.name] += len(run.text)
                    size = run.font.size or paragraph.font.size
                    if size is not None and size.pt < (MIN_FOOTER_PT if is_footer else MIN_FONT_PT):
                        findings.append(Finding(n, "WARN", "small-font", f"{size.pt:g} pt text in '{shape.name}'"))
            if _overflow(shape, text):
                findings.append(Finding(n, "WARN", "overflow", f"text may not fit in '{shape.name}'"))
        if "target" in reference:
            for match in TARGET_RE.finditer(all_text):
                value = float(match.group(1).replace(",", ""))
                if abs(value - reference["target"]) > 0.01 * reference["target"]:
                    findings.append(Finding(n, "WARN", "stale-target",
                                            f"target {value:g} differs from report/header.yaml ({reference['target']:g})"))
        if "wacc_pct" in reference:
            for match in WACC_RE.finditer(all_text):
                if abs(float(match.group(1)) - reference["wacc_pct"]) > 0.1:
                    findings.append(Finding(n, "WARN", "stale-wacc",
                                            f"WACC {match.group(1)}% differs from the model ({reference['wacc_pct']:.1f}%)"))
    if len(families) > MAX_FONT_FAMILIES:
        findings.append(Finding(0, "WARN", "fonts", "fonts used: " + ", ".join(sorted(families))))
    return findings


RARE_FONT_SHARE = 0.2


def fix(path: Path, target: Path) -> int:
    """Mechanical fixes only; returns the number of changes. Saves to `target`.

    - removes empty placeholders;
    - a font used for less than 20% of the deck's text is reset to the template's
      theme font (explicit font removed), so stray pasted fonts disappear while
      the team's main font is never touched.
    """
    prs = Presentation(str(path))
    families: Counter[str] = Counter()
    total = 0
    for slide in prs.slides:
        for shape, _ in _texts(slide):
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    total += len(run.text)
                    if run.font.name:
                        families[run.font.name] += len(run.text)
    rare = {name for name, chars in families.items() if chars < RARE_FONT_SHARE * total}
    changes = 0
    for slide in prs.slides:
        for ph in list(slide.placeholders):
            if ph.has_text_frame and not ph.text_frame.text.strip():
                ph._element.getparent().remove(ph._element)
                changes += 1
        for shape, _ in _texts(slide):
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.font.name in rare:
                        run.font.name = None
                        changes += 1
    prs.save(str(target))
    return changes


def _latest_deck(pitch: Path) -> Path | None:
    decks = sorted(pitch.glob("*_deck_v*.pptx"),
                   key=lambda p: int(m.group(1)) if (m := re.search(r"_v(\d+)\.pptx$", p.name)) else 0)
    return decks[-1] if decks else None


def _next_version(path: Path) -> Path:
    match = re.match(r"^(.*_deck_v)(\d+)\.pptx$", path.name)
    if not match:
        return path.with_name(path.stem + "_fixed.pptx")
    stem = match.group(1)
    versions = [int(m.group(1)) for p in path.parent.glob(f"{stem}*.pptx")
                if (m := re.search(r"_v(\d+)\.pptx$", p.name))]
    return path.with_name(f"{stem}{max(versions) + 1}.pptx")


def write_report(project: Path, deck: Path, findings: Sequence[Finding]) -> Path:
    lines = [f"# Deck audit - {deck.name}", "",
             f"{sum(f.severity == 'ERROR' for f in findings)} errors, {sum(f.severity == 'WARN' for f in findings)} warnings.",
             "", "| Slide | Severity | Check | Finding |", "|---|---|---|---|"]
    lines += [f"| {f.slide or 'deck'} | {f.severity} | {f.code} | {f.message} |" for f in findings]
    lines += ["", "Structural checks only: open the deck in PowerPoint and look at every slide before presenting."]
    report = project / "pitch" / "deck-audit.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the pitch deck (and optionally apply mechanical fixes).")
    parser.add_argument("--project", default=".", help="Team project folder")
    parser.add_argument("--deck", help="Deck to audit (default: newest pitch/<TICKER>_deck_v<N>.pptx)")
    parser.add_argument("--fix", action="store_true", help="Save a new version with mechanical fixes")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    deck = Path(args.deck).resolve() if args.deck else _latest_deck(project / "pitch")
    if deck is None or not deck.is_file():
        print("[x] no deck found: build it with build_pptx.py or pass --deck <file>")
        return EXIT_NO_DECK
    try:
        if args.fix:
            fixed = _next_version(deck)
            changes = fix(deck, fixed)
            print(f"[ok] {changes} mechanical fixes -> pitch/{ascii_safe(fixed.name)}")
            deck = fixed
        findings = audit(deck, project)
        report = write_report(project, deck, findings)
    except PackageNotFoundError:
        print(f"[x] {ascii_safe(deck.name)} is not a valid .pptx file")
        return EXIT_NO_DECK
    except OSError as exc:
        print(f"[x] Could not write: {ascii_safe(exc.strerror or str(exc))}. Close the file and run again.")
        return EXIT_IO_ERROR
    errors = sum(f.severity == "ERROR" for f in findings)
    print(f"audited {ascii_safe(deck.name)}: {errors} errors, {len(findings) - errors} warnings")
    for f in findings:
        where = "deck" if f.slide == 0 else f"slide {f.slide}"
        print(f"[{'x' if f.severity == 'ERROR' else 'warn'}] {where}: {ascii_safe(f.message)}")
    print(f"[ok] report -> pitch/{report.name}")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest -q skills/deck/tools/tests/test_audit_pptx.py`
Expected: `6 passed`. If the fix test's font rule is too strict/lenient for the planted case, adjust the RULE (keep "never change the main font; replace rare off-palette fonts") and report.

- [ ] **Step 5: mypy and commit**

Run: `python -m mypy skills/deck/tools`
Expected: `Success`.

```bash
git add skills/deck/tools/audit_pptx.py skills/deck/tools/tests/test_audit_pptx.py
git commit -m "feat(deck): structural deck audit with stale-number checks and mechanical fixes"
```

---

### Task 4: `pitch` skill

**Files:**
- Create: `skills/pitch/references/pitch-structure.md`
- Create: `skills/pitch/references/outline-template.yaml`
- Create: `skills/pitch/references/qa-bank.md`
- Create: `skills/pitch/SKILL.md`

- [ ] **Step 1: Create `skills/pitch/references/pitch-structure.md`**

```markdown
# Pitch structure (CFA Institute Research Challenge, 2026-2027 Official Rules)

## Format by round

| Round | Talk | Q&A | Language |
|---|---|---|---|
| Local final | 10 min | 10 min | Local host decides (English, Spanish or Portuguese) |
| Sub-regional | 10 min, recorded | none | English |
| Regional semifinal | 10 min | 10 min | English |
| Regional and global finals | 10 min | 15 min | English |

Every slide shows its sources. No handouts or props (cue cards are fine). Only
students present.

## How it is scored (out of 100)

Financial analysis 20, Valuation 20, ESG 10, Presentation 20, Q&A 20, Team
involvement 5, Materials (slides) 5. At the local final the presentation is
50% of the total (the report is the other 50%).

## Suggested flow (10-12 slides, about 9.5 minutes, 30 seconds of buffer)

| # | Slide | Minutes | Rubric it feeds |
|---|---|---|---|
| 1 | Title: company, rating, target, upside | 0.5 | Presentation |
| 2 | Investment summary: the 2-3 pillars and what the market misses | 1.0 | Presentation |
| 3 | Business and industry positioning | 1.0 | Financial analysis |
| 4-5 | Financial analysis: history, forecast drivers tied to pillars | 2.0 | Financial analysis |
| 6-7 | Valuation: DCF and comps, sensitivity, football field | 2.0 | Valuation |
| 8 | Investment risks: matrix, the 2-3 that matter, downside value | 1.0 | Presentation |
| 9 | ESG: material issues, governance, link to value | 1.0 | ESG |
| 10 | Recommendation, catalysts, what would change our mind | 1.0 | Presentation |

Every member presents at least one part (team involvement). Plan handoffs:
the last sentence of each part names the next speaker's topic.

## Slide rules

- The title is the message ("Margins expand 150 bp as wheat costs ease"), not a label ("Margins").
- At most 6 bullets of at most 20 words; a chart beats a table.
- Numbers on slides must match the report and the model; change them in the
  model or outline, never by hand in the deck.
```

- [ ] **Step 2: Create `skills/pitch/references/outline-template.yaml`**

```yaml
# pitch/outline.yaml - written by the pitch skill, read by deck/tools/build_pptx.py.
# kind: title | section | content | chart. Every slide except the title needs sources.
# chart: a PNG name from report/charts without .png (revenue-margin, free-cash-flow,
#        football-field, sensitivity, risk-matrix).
deck:
  title: ""                 # e.g. "Company (BMV: TICKER) - BUY, target MXN 00.0"
  language: en              # the presentation language for this round
  minutes: 10
slides:
  - kind: title
    title: ""
    subtitle: ""            # rating, target, upside
    notes: ""
    speaker: ""
    minutes: 0.5
  - kind: content
    title: ""               # the slide's message, as a sentence
    bullets: []             # at most 6, each at most 20 words
    chart: ""               # optional
    sources: ""             # required
    notes: ""               # what the speaker says
    speaker: ""
    minutes: 1.0
```

- [ ] **Step 3: Create `skills/pitch/references/qa-bank.md`**

```markdown
# Judge Q&A bank

Generate questions from the team's own files — the judges read the report.
Pick 30: at least 4 from each category, weighted to the team's weakest spots
(largest assumption vs history, terminal value share, biggest risk, governance).

## Categories and seed questions

**Valuation** — Why this WACC; where does beta come from? What share of value is
the terminal value, and why is that acceptable? Why does the DCF differ from comps?
What price does the market imply (reverse DCF), and why is it wrong?

**Forecast and financial analysis** — Which assumption moves the target most?
Why will margins beat their historical range? What happens to cash flow if
growth halves? Why these working-capital days?

**Industry and competition** — Who loses share if you are right? What stops a
competitor from copying the advantage?

**Accounting** — Why does your EBITDA differ from the company's? How did you
treat leases (IFRS 16)? Any one-offs you removed?

**Risks** — Which risk worries you most and what is it worth per share? What
would make you change the rating?

**ESG and governance** — Which ESG issue is material for this company and how is
it in your numbers? Does the controlling shareholder deserve a discount?

**AI use** (judges are likely to ask) — Which AI tools did you use, for what, and
how did you check the output? What did you decide yourselves? What would you do
differently?

**Recommendation** — Why now? What is the catalyst and when?

## Scoring a practice answer (1-5 each)

| Criterion | 5 means |
|---|---|
| Direct | Answers the question in the first sentence |
| Evidence | Cites a number or a source |
| Linked | Connects back to a pillar or the valuation |
| Concise | Under about 60 seconds |
| Honest | Owns uncertainty; no bluffing |
```

- [ ] **Step 4: Create `skills/pitch/SKILL.md`**

````markdown
---
name: pitch
description: Prepare the CFA Research Challenge presentation - a 10-minute slide-by-slide outline (pitch/outline.yaml) with speaker notes, timing and speaker assignments built from the team's report and model, and a judge Q&A drill of about 30 questions generated from the team's own files, run as scored mock rounds (including questions about how the team used AI). The team decides the lead message, who presents what, and answers in their own words. Use whenever a student asks about the presentation, pitch, slides outline, speaker notes, timing, rehearsal, mock Q&A or likely judge questions - even if they don't say pitch.
---

# pitch

## Purpose

Turn the report into a 10-minute talk the judges remember and prepare every
member for Q&A. Structure, notes, timing and questions are the assistant's job;
the lead message, the speakers and the answers belong to the team.

## Reads

- `report/sections/*.md` and `report/header.yaml` (preferred source); if missing,
  `research/thesis.md`, `valuation/valuation.md`, `model/model-summary.json`,
  `research/risks.md`, `research/esg.md`, `data/adjustments.md` — say which
  inputs are missing and continue with placeholders tagged `[assumption]`.
- `report/charts/*.png` — the charts slides can use.
- `company-profile.yaml` — `presentation_language`; `docs/context/ai-use-log.md`
  for the AI-use questions; `docs/context/memory.md` for team decisions.
- `pitch/outline.yaml`, `pitch/qa-drill.md` — if present, revise them.
- `references/pitch-structure.md`, `references/outline-template.yaml`,
  `references/qa-bank.md`.

## Steps

1. **Round and language**: ask which round this is for (local final, recorded
   sub-regional, regional, global) unless `todo.md` or `memory.md` says; take
   the language from the table in `pitch-structure.md` (local: the profile's
   `presentation_language`).
2. **Lead message** (Coach moments) before any slide.
3. **Draft `pitch/outline.yaml`** from the template and the suggested flow: each
   slide's title is its message; at most 6 bullets of at most 20 words; a chart
   from `report/charts/` where one exists; `sources` on every slide but the title
   (Challenge rule); notes written as spoken sentences in the presentation
   language; speaker and minutes per slide, total about 9.5.
4. **Speakers and cuts** (Coach moments), then update the outline.
5. **Q&A drill**: write `pitch/qa-drill.md` with about 30 questions from
   `references/qa-bank.md`, each with a pointer to the file and number that
   answers it (not a scripted answer).
6. **Mock rounds** when asked: one question at a time, the student answers,
   score with the bank's five criteria, give one improvement, re-ask weak ones
   later. Include AI-use questions every round.
7. **Close**: slide count, planned minutes, weakest Q&A area, next step
   ("next: the deck skill builds the slides from this outline").

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Lead message**: the one sentence the judges should remember.
- **Who presents what**: every member speaks (team involvement is scored).
- **What to cut** to fit 10 minutes.

## Writes

- `pitch/outline.yaml`, `pitch/qa-drill.md`
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — pitch — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | pitch | pitch/outline.yaml, pitch/qa-drill.md | drafted outline, notes and Q&A drill; team chose message and speakers`
- `docs/context/todo.md`: rehearsal dates, weak Q&A areas.
````

- [ ] **Step 5: Commit** (structural tests are added in Task 6)

```bash
git add skills/pitch/
git commit -m "feat(pitch): presentation outline, speaker notes, timing and scored Q&A drill"
```

---

### Task 5: `deck` skill

**Files:**
- Create: `skills/deck/references/deck-design.md`
- Create: `skills/deck/SKILL.md`

- [ ] **Step 1: Create `skills/deck/references/deck-design.md`**

```markdown
# Deck design and checks

## The team's template is the design

Put the team's template at `pitch/template.pptx`. The builder keeps its theme,
fonts, colors and layouts, removes its example slides, and picks layouts by
their placeholders: a title layout with a subtitle, a title-and-content layout,
a two-content layout (bullets left, chart right), a title-only layout (full
chart), a section layout. Run `--list-layouts` first to see what the template
offers; a template without a title-and-content layout still works (text boxes
are used), but tell the team.

## Rules for every slide

- Title = the message, as a sentence.
- At most 6 bullets, at most 20 words each; charts over tables.
- A "Source: ..." line at the bottom (Challenge rule) — the builder adds it as a
  shape named `Sources`.
- Speaker notes in the notes field, never on the slide.
- Numbers come from the model and the report through the outline; never type a
  number into the deck by hand.
- The template's fonts only; body text at least 10 pt (source lines 8 pt minimum).

## What the audit checks (structural, no rendering)

Slide count for 10 minutes (6-14), sources, notes, leftover placeholder text,
shapes off the slide, small fonts, more than two font families, likely text
overflow, dense slides (over 60 words), and target price or WACC that differ
from `report/header.yaml` / `model/model-summary.json`.

`--fix` saves a new version with mechanical fixes only: empty placeholders
removed, rarely used stray fonts reset to the template's theme font. Everything
else is a finding to fix in the outline (then rebuild) or by the team.

## Visual check

The audit cannot see the slides. If LibreOffice is installed,
`soffice --headless --convert-to pdf <deck>` renders it; look at every page for
overflow, overlaps, the source line colliding with content, and contrast.
Otherwise the team opens the deck in PowerPoint and checks the slides the audit
listed.
```

- [ ] **Step 2: Create `skills/deck/SKILL.md`**

````markdown
---
name: deck
description: Build the CFA Research Challenge pitch deck as a PowerPoint file from pitch/outline.yaml on the team's own template - layouts chosen from the template, charts from the report, a Sources line on every slide (Challenge rule) and speaker notes in the notes field - and audit any deck (slide count for 10 minutes, sources, notes, leftover placeholders, fonts, overflow, numbers that no longer match the model), fixing mechanical problems and flagging the rest. The team owns the design and final polish. Use whenever a student asks to make, build, generate, format, clean up, check or audit the slides, the deck or the PowerPoint - even if they don't say deck.
---

# deck

## Purpose

Save the team hours of slide formatting and catch rule breaks before judges
do. Building and checking are the assistant's job; the design (their template)
and the final visual polish belong to the team.

## Reads

- `pitch/outline.yaml` — required to build. Missing: suggest the pitch skill (an
  audit of an existing deck still works without it).
- `pitch/template.pptx` — the team's template. Missing: build on a plain default
  and recommend adding their template, then rebuild.
- `report/charts/*.png` — missing charts: run the report skill's `charts.py`.
- `model/model-summary.json`, `report/header.yaml` — for the stale-number check.
- `references/deck-design.md`.

## Steps

Find Python as in init-skills (3.10 or newer; python-pptx missing -> the
init-skills install command). Tools live in `${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/`
(if `${CLAUDE_PLUGIN_ROOT}` does not resolve, use the installed plugin's absolute
path, in quotes).

1. **Inspect the template**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py" --project . --list-layouts`
   Tell the team which layouts will be used and anything missing.
2. **Build**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py" --project .`
   Exit 2: fix the outline (sources, charts) and rerun. Exit 4: close the file in
   PowerPoint.
3. **Audit**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/audit_pptx.py" --project .`
   Add `--fix` for mechanical fixes (new version). Fix content findings (dense
   slides, stale numbers, missing sources) in `pitch/outline.yaml` and rebuild —
   never edit numbers inside the deck.
4. **Existing deck**: to check a deck the team made by hand, run the audit with
   `--deck "<file>"` (and `--fix` if they agree).
5. **Visual check** per `references/deck-design.md` (LibreOffice render if
   available; otherwise list the slides for the team to check in PowerPoint).
6. **Close**: file name, slide count, errors and warnings left, and the checkpoint.

## Coach moments

No story decisions. One review checkpoint: the team opens the deck in
PowerPoint and confirms the layout and design are theirs to present; their
changes to wording go back into `pitch/outline.yaml` so the next build keeps them.

## Writes

- `pitch/<TICKER>_deck_v<N>.pptx` (never overwritten), `pitch/deck-audit.md`

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | deck | pitch/<file> | built deck from outline on team template; audit <n> errors, <m> warnings`
- `docs/context/todo.md`: remaining audit findings and slides to check visually.
````

- [ ] **Step 3: Commit**

```bash
git add skills/deck/SKILL.md skills/deck/references/
git commit -m "feat(deck): deck skill (build on team template, audit, visual check)"
```

---

### Task 6: Integration — structural tests, AGENTS template, README, manifests, evals, spec

**Files:**
- Modify: `tests/test_plugin_structure.py`
- Modify: `skills/init-skills/templates/AGENTS.md`, `README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- Create: `evals/phase3b.md`
- Modify: spec (status, §8 outline file name)

- [ ] **Step 1: Structural tests** — in `tests/test_plugin_structure.py`: add `"pitch", "deck"` to the end of `SKILLS`; add to `TOOL_CALLS`:

```python
    "deck": ("${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py",
             "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/audit_pptx.py"),
```

and append:

```python
def test_outline_template_names_real_charts_and_fields() -> None:
    import sys

    if str(REPORT_TOOLS) not in sys.path:
        sys.path.insert(0, str(REPORT_TOOLS))
    from charts import CHARTS

    text = read_text(SKILLS_DIR / "pitch" / "references" / "outline-template.yaml")
    for chart in CHARTS:
        assert chart.name in text, chart.name
    for field in ("kind:", "title:", "subtitle:", "bullets:", "chart:", "sources:", "notes:", "speaker:", "minutes:"):
        assert field in text, field
```

- [ ] **Step 2: AGENTS.md template** — add after the `report` row:

```markdown
| `pitch` | 10-minute outline, speaker notes, timing, judge Q&A drill | `pitch/outline.yaml`, `pitch/qa-drill.md` |
| `deck` | Build the PowerPoint on your template; audit any deck | `pitch/<TICKER>_deck_v<N>.pptx`, `pitch/deck-audit.md` |
```

- [ ] **Step 3: README** — `## Skills (v0.3)` -> `## Skills (v0.4)`; add after the `report` row:

```markdown
| `pitch` | 10-minute outline with speaker notes and timing; scored mock Q&A (incl. AI-use questions) | The lead message, who presents what, your answers |
| `deck` | Builds the PowerPoint on your team template (sources on every slide, notes, charts) and audits any deck | The design and the final polish |
```

Replace the "Coming next" line with nothing (delete it); typical order line ends `... -> \`report\` -> \`pitch\` -> \`deck\``. In Requirements, change "python-pptx comes with the presentation skills" (or equivalent) so the list is: openpyxl, pyyaml, matplotlib, python-docx, python-pptx. Development install line: add `"python-pptx>=1.0"`; add a third mypy command `python -m mypy skills/deck/tools`.

- [ ] **Step 4: Manifests** — `plugin.json` `"version": "0.4.0"`; in both descriptions (plugin.json and the marketplace entry) replace `, and the written report` with `, the written report, the pitch and the PowerPoint deck`.

- [ ] **Step 5: Create `evals/phase3b.md`**

```markdown
# Phase 3b manual evals

Project with the report drafted (phase 3a evals done). Put a real team
template at `pitch/template.pptx` (e.g. a university template) for eval 2.

## pitch

1. Prompt: "prepare our presentation"
   - [ ] Asks the round (or reads it) and uses the right language.
   - [ ] Asks for the lead message before drafting slides.
   - [ ] Writes `pitch/outline.yaml`: message titles, <= 6 bullets, sources on every slide but the title, speakers, ~9.5 minutes.
2. Prompt: "run a mock Q&A"
   - [ ] Asks one question at a time, scores with the five criteria, gives one improvement.
   - [ ] Includes at least one AI-use question.

## deck

1. Prompt: "build our slides" (no template)
   - [ ] Warns that no template was found, builds on the default.
2. Prompt: "build our slides" (with the team template)
   - [ ] Runs `--list-layouts` first and says which layouts it will use.
   - [ ] Deck opens in PowerPoint; every slide but the title has a Source line; notes are in the notes pane.
   - [ ] Runs the audit and reports errors/warnings; fixes content in the outline and rebuilds.
3. Prompt: "check this deck" with a hand-made .pptx
   - [ ] Audits it with `--deck`, lists findings, offers `--fix`, never overwrites the original.
```

- [ ] **Step 6: Spec** — header status -> `approved; phases 1, 2a, 2b, 3a and 3b implemented`; in §8 replace `pitch/outline.md` with `pitch/outline.yaml` (both in the table and elsewhere).

- [ ] **Step 7: Run everything**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine; python -m mypy skills/report/tools; python -m mypy skills/deck/tools; claude plugin validate .`
Expected: all pass.

- [ ] **Step 8: Commit**

```bash
git add tests/test_plugin_structure.py skills/init-skills/templates/AGENTS.md README.md .claude-plugin/ evals/phase3b.md docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md
git commit -m "docs: integrate pitch and deck into tests, AGENTS template, README, manifests and evals"
```
