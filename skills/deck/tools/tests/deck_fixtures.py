"""Fixtures for the deck tools (a plain module, not conftest.py: two conftest modules collide).

Import this module FIRST in test files: it puts skills/deck/tools on sys.path.
"""

from __future__ import annotations

import io
import json
import sys
import zipfile
from collections.abc import Mapping, Sequence
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
from pptx.oxml.ns import qn  # noqa: E402
from pptx.oxml.shapes.picture import CT_Picture  # noqa: E402
from pptx.util import Inches  # noqa: E402

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


# --- synthetic templates reproducing real-template failure modes -------------------------------

ES_NAMES = {"Title Slide": "Diapositiva de título", "Title and Content": "Título y objetos",
            "Section Header": "Encabezado de sección", "Two Content": "Dos objetos", "Comparison": "Comparación",
            "Title Only": "Solo el título", "Blank": "En blanco", "Content with Caption": "Contenido con título",
            "Picture with Caption": "Imagen con título", "Title and Vertical Text": "Título y texto vertical",
            "Vertical Title and Text": "Título vertical y texto"}


def default_layouts(keep: Sequence[str], strip_types: bool = True) -> Any:
    """The plain default template reduced to `keep` layouts, in that order (layout types removed)."""
    prs = Presentation()
    layouts = prs.slide_master.slide_layouts
    for layout in list(layouts):
        if layout.name not in keep:
            layouts.remove(layout)
    id_list = prs.slide_master._element.find(qn("p:sldLayoutIdLst"))
    by_name = dict(zip((layout.name for layout in layouts), list(id_list)))
    for element in list(id_list):
        id_list.remove(element)
    for name in keep:
        id_list.append(by_name[name])
    if strip_types:
        for layout in layouts:
            layout._element.attrib.pop("type", None)
    return prs


def layout(prs: Any, name: str) -> Any:
    return next(item for item in prs.slide_layouts if item.name == name)


def placeholder(layout_: Any, idx: int) -> Any:
    return next(ph for ph in layout_.placeholders if ph.placeholder_format.idx == idx)


def set_box(shape: Any, left: float, top: float, width: float, height: float) -> None:
    shape.left, shape.top, shape.width, shape.height = Inches(left), Inches(top), Inches(width), Inches(height)


def thin_bar_template(path: Path) -> Path:
    """Pitchbook-like: a 'Heading Only' layout (title + thin heading-bar body) listed before '1-Up'
    (title + thin bar + the real body)."""
    prs = default_layouts(["Title Slide", "Title and Content", "Two Content", "Title Only"])
    heading = layout(prs, "Title and Content")
    heading.name = "Heading Only"
    set_box(placeholder(heading, 1), 0.5, 1.6, 9.0, 0.3)
    one_up = layout(prs, "Two Content")
    one_up.name = "1-Up"
    set_box(placeholder(one_up, 1), 0.5, 1.6, 9.0, 0.3)
    set_box(placeholder(one_up, 2), 0.5, 2.0, 9.0, 4.6)
    prs.save(str(path))
    return path


def section_mid_title_template(path: Path) -> Path:
    """Training-like: 'Section Header' (title mid-slide, no body, no layout type) listed before 'Title Only'."""
    prs = default_layouts(["Title Slide", "Section Header", "Title and Content", "Title Only"])
    section = layout(prs, "Section Header")
    body = placeholder(section, 1)
    body._element.getparent().remove(body._element)
    prs.save(str(path))
    return path


def vertical_title_template(path: Path, only_vertical: bool = False) -> Path:
    """A 'Vertical Title and Text' layout listed before the normal content layouts.

    only_vertical: Pitchbook-like, the only content layout has a side title and a normal (horizontal) body.
    """
    keep = ["Title Slide", "Vertical Title and Text"] if only_vertical else \
        ["Title Slide", "Vertical Title and Text", "Title and Content", "Title Only"]
    prs = default_layouts(keep)
    if only_vertical:
        body_pr = placeholder(layout(prs, "Vertical Title and Text"), 1)._element.find(
            f"{qn('p:txBody')}/{qn('a:bodyPr')}")
        body_pr.attrib.pop("vert", None)
    prs.save(str(path))
    return path


def spanish_template(path: Path) -> Path:
    prs = default_layouts(list(ES_NAMES))
    for item in prs.slide_layouts:
        item.name = ES_NAMES[item.name]
    prs.save(str(path))
    return path


def no_subtitle_template(path: Path, with_body: bool = True) -> Path:
    """with_body: the title layout has a plain body placeholder instead of a subtitle;
    otherwise only 'Title Only' and 'Blank' exist."""
    if with_body:
        prs = default_layouts(["Title Slide", "Title and Content", "Section Header", "Title Only"], strip_types=False)
        placeholder(layout(prs, "Title Slide"), 1)._element.ph.set("type", "body")
    else:
        prs = default_layouts(["Title Only", "Blank"])
    prs.save(str(path))
    return path


def title_and_blank_template(path: Path) -> Path:
    """Only 'Title Slide' (title mid-slide) and 'Blank': every slide needs fallbacks."""
    default_layouts(["Title Slide", "Blank"]).save(str(path))
    return path


def logo_template(path: Path, logo: Path) -> Path:
    """Default template with a logo picture on the master in the footer band (bottom left)."""
    prs = Presentation()
    master = prs.slide_master
    _, rel_id = master.part.get_or_add_image_part(str(logo))
    tree = master.shapes._spTree
    shape_id = max(int(e.get("id")) for e in tree.iter(qn("p:cNvPr"))) + 1
    tree.append(CT_Picture.new_pic(  # type: ignore[no-untyped-call]  # pptx oxml factory is unannotated
        shape_id, "Logo", "", rel_id, Inches(0.3), Inches(6.85), Inches(1.2), Inches(0.55)))
    prs.save(str(path))
    return path


def potx_from(pptx_path: Path, potx_path: Path) -> Path:
    """Re-label a .pptx as a PowerPoint template (.potx), as PowerPoint saves it."""
    main = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
    template = "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
    buffer = io.BytesIO()
    with zipfile.ZipFile(pptx_path) as zin, zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = data.replace(main.encode(), template.encode())
            zout.writestr(item, data)
    potx_path.write_bytes(buffer.getvalue())
    return potx_path


def set_outline(project: Path, outline: Mapping[str, Any]) -> None:
    (project / "pitch" / "outline.yaml").write_text(yaml.safe_dump(dict(outline), sort_keys=False), encoding="utf-8")
