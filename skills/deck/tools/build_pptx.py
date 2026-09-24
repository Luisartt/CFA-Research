"""Build the pitch deck (.pptx) from pitch/outline.yaml on the team's own template.

Template: --template <file>, else pitch/template.pptx, else python-pptx's plain default.
A .potx template is read as a presentation (converted in memory). Example slides already
in the template are removed; its layouts, theme, fonts and colors are kept. Layouts are
chosen by geometry (where the title and body placeholders actually sit), preferring the
layout type when the template sets one, so any team template works in any language.
Every slide except the title gets a "Source:" footer ("Fuente:"/"Fonte:" for es/pt decks)
in the template's footer band (Challenge rule: slides show their sources); speaker notes
go in the notes field. Output (never overwritten): pitch/<TICKER>_deck_v<N>.pptx.

Usage: python build_pptx.py --project <team folder> [--template <file>] [--list-layouts]
Console output is ASCII only.
"""

from __future__ import annotations

import argparse
import io
import re
import zipfile
from collections.abc import Iterator, Sequence
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

import yaml
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
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
MIN_FOOTER_HEIGHT = Inches(0.3)
GAP = Inches(0.15)
MIN_AREA_HEIGHT = Inches(1)
BULLET_PT = 16
SOURCES_NAME = "Sources"
SOURCE_LABELS = {"en": "Source:", "es": "Fuente:", "pt": "Fonte:"}
SOURCE_GREY = RGBColor(0x59, 0x59, 0x59)  # type: ignore[no-untyped-call]  # RGBColor.__new__ has no annotations
TITLE_TYPES = {PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE}
BODY_TYPES = {PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT}
FOOTER_TYPES = {PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.DATE, PP_PLACEHOLDER.SLIDE_NUMBER}
# Geometry rules for choosing layouts (shares of the slide size).
TITLE_TOP_SHARE = 0.25  # a usable title starts in the top quarter...
TITLE_HEIGHT_SHARE = 0.30  # ...and is not taller than this (vertical titles are)
MIN_BODY_HEIGHT = Inches(1.5)
BODY_WIDTH_SHARE = 0.40  # a content body is at least this wide
PAIR_WIDTH_SHARE = 0.25  # each body of a two-content pair
PAIR_TOP_SHARE = 0.10  # the two bodies start at about the same height
FREE_HEIGHT_SHARE = 0.50  # a chart / title-only layout leaves this much free below the title
FOOTER_BAND_SHARE = 0.75  # footer placeholders and logos below this line form the footer band
DECOR_WIDTH_SHARE = 0.80  # wider template shapes are backgrounds/bands, not obstacles
DECOR_AREA_SHARE = 0.50
VERTICAL_TEXT = {"vert", "vert270", "eaVert", "wordArtVert", "mongolianVert", "wordArtVertRtl"}
SECTION_NAME = re.compile(r"section|secci|se[cç][aã]o", re.IGNORECASE)
TEMPLATE_MAIN = b"application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
PRESENTATION_MAIN = b"application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
# Child order of a:pPr (CT_TextParagraphProperties); a:buChar must go before a:tabLst/a:defRPr.
PPR_ORDER = ("lnSpc", "spcBef", "spcAft", "buClrTx", "buClr", "buSzTx", "buSzPct", "buSzPts", "buFontTx", "buFont",
             "buNone", "buAutoNum", "buChar", "buBlip", "tabLst", "defRPr", "extLst")
BULLET_TAGS = {"buNone", "buAutoNum", "buChar", "buBlip"}


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


@dataclass(frozen=True)
class Box:
    left: int
    top: int
    width: int
    height: int

    @property
    def right(self) -> int:
        return self.left + self.width

    @property
    def bottom(self) -> int:
        return self.top + self.height

    @property
    def area(self) -> int:
        return self.width * self.height

    def overlap(self, other: Box) -> tuple[int, int]:
        """Overlap width and height (0 when apart)."""
        return (max(0, min(self.right, other.right) - max(self.left, other.left)),
                max(0, min(self.bottom, other.bottom) - max(self.top, other.top)))


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


# --- outline --------------------------------------------------------------------------------

def _read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except UnicodeDecodeError:
        raise DeckInputError([f"{path.name} is not saved as UTF-8; re-save it as UTF-8"]) from None
    except yaml.YAMLError as exc:
        raise DeckInputError([f"{path.name} is not valid YAML: {exc}"]) from None


def _chart_problem(path: Path) -> str | None:
    if not path.is_file():
        return "not found in report/charts (run the report skill's charts.py)"
    try:
        with Image.open(path) as image:
            image.verify()
    except (OSError, SyntaxError, ValueError):  # PIL.UnidentifiedImageError is an OSError
        return "is not a readable PNG image (re-create it with the report skill's charts.py)"
    return None


def load_outline(path: Path, charts_dir: Path) -> tuple[dict[str, Any], list[SlideSpec], list[str]]:
    if not path.is_file():
        raise DeckInputError(["pitch/outline.yaml not found: run the pitch skill first"])
    doc = _read_yaml(path)
    if not isinstance(doc, dict) or not isinstance(doc.get("slides"), list) or not doc["slides"]:
        raise DeckInputError(["pitch/outline.yaml needs a non-empty 'slides:' list"])
    deck_raw = doc.get("deck")
    deck: dict[str, Any] = deck_raw if isinstance(deck_raw, dict) else {}
    problems: list[str] = []
    warnings: list[str] = []
    slides: list[SlideSpec] = []
    for n, raw in enumerate(doc["slides"], start=1):
        if not isinstance(raw, dict):
            problems.append(f"slide {n}: must be a mapping")
            continue
        kind, title = str(raw.get("kind", "content")), str(raw.get("title") or "").strip()
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
        chart = re.sub(r"\.png$", "", str(raw.get("chart") or "").strip(), flags=re.IGNORECASE)
        if kind == "chart" and not chart:
            problems.append(f"{where}: a chart slide needs 'chart:' (a PNG name in report/charts)")
        if chart and (problem := _chart_problem(charts_dir / f"{chart}.png")):
            problems.append(f"{where}: chart '{chart}' {problem}")
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


# --- template geometry ----------------------------------------------------------------------

def shape_box(shape: Any) -> Box | None:
    """The shape's bounding box (inherited from layout/master for placeholders; turned for 90-degree rotation)."""
    values = (shape.left, shape.top, shape.width, shape.height)
    if any(v is None for v in values):
        return None
    left, top, width, height = (int(v) for v in values)
    rotation = getattr(shape, "rotation", 0.0) or 0.0
    if 45 < rotation % 180 < 135:
        cx, cy = left + width // 2, top + height // 2
        left, top, width, height = cx - height // 2, cy - width // 2, height, width
    return Box(left, top, width, height)


def _vertical_text(placeholder: Any) -> bool:
    element: Any = placeholder._element
    while element is not None:
        body_pr = element.find(f"{qn('p:txBody')}/{qn('a:bodyPr')}")
        vert = body_pr.get("vert") if body_pr is not None else None
        if vert:
            return vert in VERTICAL_TEXT
        base = getattr(placeholder, "_base_placeholder", None)
        placeholder, element = base, (base._element if base is not None else None)
    return False


def decor_boxes(layout: Any, width: int, height: int) -> list[Box]:
    """Non-placeholder shapes (logos, side bars) the layout and its master draw on every slide.

    Full-slide backgrounds and full-width bands are left out: text may sit on them.
    """
    shapes = list(layout.shapes)
    if layout._element.get("showMasterSp") != "0":
        shapes += list(layout.slide_master.shapes)
    boxes = []
    for shape in shapes:
        if shape.is_placeholder or (box := shape_box(shape)) is None:
            continue
        if box.width < DECOR_WIDTH_SHARE * width and box.area < DECOR_AREA_SHARE * width * height:
            boxes.append(box)
    return boxes


def _master_box(master: Any, types: set[Any]) -> Box | None:
    for ph in master.placeholders:
        if ph.placeholder_format.type in types and (box := shape_box(ph)) is not None:
            return box
    return None


@dataclass(frozen=True)
class Frame:
    """Where content may go on slides of one template: horizontal extent and the footer band."""
    width: int
    height: int
    left: int
    right: int
    body_top: int  # where the master's body starts (bands often sit between title and body)
    footer: Box  # vertical band (and horizontal extent) for the Sources line

    @property
    def band_top(self) -> int:
        return self.footer.top


def _frame(prs: Any) -> Frame:
    width, height = int(prs.slide_width), int(prs.slide_height)
    master = prs.slide_master
    body = _master_box(master, {PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT})
    left, right = (body.left, body.right) if body is not None else (int(MARGIN), width - int(MARGIN))
    left, right = max(0, left), min(width, right)
    band = [box for ph in master.placeholders if ph.placeholder_format.type in FOOTER_TYPES
            and (box := shape_box(ph)) is not None and box.top >= FOOTER_BAND_SHARE * height]
    footer = next((box for ph in master.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.FOOTER
                   and (box := shape_box(ph)) is not None and box.top >= FOOTER_BAND_SHARE * height), None)
    if footer is None and band:
        footer = min(band, key=lambda b: b.top)
    if footer is not None:
        top = footer.top
        box_height = min(max(footer.height, int(MIN_FOOTER_HEIGHT)), height - top)
    else:
        top, box_height = height - int(FOOTER_HEIGHT), int(FOOTER_HEIGHT - Inches(0.05))
    body_top = body.top if body is not None else 0
    return Frame(width, height, left, right, body_top, Box(left, top, right - left, box_height))


@dataclass(frozen=True)
class LayoutInfo:
    layout: Any
    order: int
    kind: str  # the layout's own type attribute ("" when the template does not set one)
    title_idx: int | None
    title: Box | None
    title_usable: bool  # horizontal, in the top quarter, not too tall
    title_vertical: bool  # tall and narrow, or vertical text: a side title
    subtitle_idx: int | None
    bodies: tuple[tuple[int, Box], ...]  # horizontal-text BODY/OBJECT placeholders
    others: int  # other content placeholders (pictures, charts, tables, vertical text...)


def _analyse(layout: Any, order: int, frame: Frame) -> LayoutInfo:
    title_idx: int | None = None
    title: Box | None = None
    subtitle_idx: int | None = None
    vertical = False
    bodies: list[tuple[int, Box]] = []
    others = 0
    for ph in layout.placeholders:
        ph_type, idx, box = ph.placeholder_format.type, ph.placeholder_format.idx, shape_box(ph)
        if ph_type in FOOTER_TYPES:
            continue
        if ph_type in TITLE_TYPES and title_idx is None and box is not None:
            title_idx, title = idx, box
            vertical = box.height > box.width or _vertical_text(ph)
        elif ph_type == PP_PLACEHOLDER.SUBTITLE and subtitle_idx is None:
            subtitle_idx = idx
        elif ph_type in BODY_TYPES and box is not None and not _vertical_text(ph):
            bodies.append((idx, box))
        else:
            others += 1
    usable = bool(title is not None and not vertical and title.top < TITLE_TOP_SHARE * frame.height
                  and title.height <= TITLE_HEIGHT_SHARE * frame.height)
    return LayoutInfo(layout, order, layout._element.get("type") or "", title_idx, title, usable, vertical,
                      subtitle_idx, tuple(bodies), others)


def _big(box: Box, frame: Frame, width_share: float = BODY_WIDTH_SHARE) -> bool:
    return box.height >= MIN_BODY_HEIGHT and box.width >= width_share * frame.width


def _title_target(info: LayoutInfo, frame: Frame, need: str) -> Box | None:
    """Where the title goes: a horizontal title far down a layout is moved to the top for content slides."""
    title = info.title
    if title is None or need in ("title", "section") or info.title_usable or info.title_vertical:
        return title
    return Box(title.left, min(int(MARGIN), int(0.05 * frame.height)), title.width,
               min(title.height, int(0.18 * frame.height)))


def _bottom_limit(layout: Any, frame: Frame) -> int:
    """Content ends above the footer band and above logos in it."""
    tops = [frame.band_top] + [box.top for box in decor_boxes(layout, frame.width, frame.height)
                               if box.top >= FOOTER_BAND_SHARE * frame.height
                               and box.left < frame.right and box.right > frame.left]
    return min(tops) - int(GAP)


def free_area(layout: Any, frame: Frame, title: Box | None) -> Box:
    """The area left for content: below a horizontal title (beside a vertical one), above the footer band."""
    left, top, right = frame.left, int(MARGIN), frame.right
    if title is not None:
        if title.height > title.width:
            if title.left + title.width // 2 > frame.width // 2:
                right = min(right, title.left - int(GAP))
            else:
                left = max(left, title.right + int(GAP))
        else:
            top = max(top, title.bottom + int(GAP))
            if frame.body_top >= title.bottom:
                top = max(top, frame.body_top)
    bottom = _bottom_limit(layout, frame)
    if bottom - top < MIN_AREA_HEIGHT:
        top = max(0, bottom - int(MIN_AREA_HEIGHT))
    return Box(left, top, max(int(Inches(1)), right - left), max(0, bottom - top))


@dataclass(frozen=True)
class Choice:
    info: LayoutInfo
    title: Box | None  # where the title goes on the slide
    text_idx: int | None = None  # placeholder for the bullets (or the title slide's subtitle)
    chart_idx: int | None = None  # body placeholder whose area takes the chart
    split: bool = False  # bullets left, chart right, in one area


def _need(kind: str, bullets: bool, chart: bool) -> str:
    if kind in ("title", "section"):
        return kind
    if bullets and chart:
        return "two"
    return "chart" if chart else "content"


def _fit(info: LayoutInfo, need: str, strict: bool, frame: Frame) -> tuple[tuple[float, ...], Choice] | None:
    """How well a layout fits a need; None when it does not. Higher keys are better."""
    title = _title_target(info, frame, need)
    if title is None or (strict and not info.title_usable and need not in ("title", "section")):
        return None
    moved = 0.0 if title == info.title else -1.0
    choice = Choice(info, title)
    extras = len(info.bodies) + info.others + (info.subtitle_idx is not None)
    area = free_area(info.layout, frame, title)
    open_area = area.height >= FREE_HEIGHT_SHARE * frame.height and area.width >= BODY_WIDTH_SHARE * frame.width
    bigs = sorted((b for b in info.bodies if _big(b[1], frame)), key=lambda b: b[1].area, reverse=True)

    def key(tier: int, bonus: bool, extra: int, metric: float) -> tuple[float, ...]:
        return (tier, moved, float(bonus), -extra, metric, -info.order)

    if need == "title":
        if info.title_vertical:
            return None
        if info.subtitle_idx is not None:
            return key(3, info.kind == "title", extras - 1, 0), replace(choice, text_idx=info.subtitle_idx)
        if info.bodies and strict:
            below = sorted(info.bodies, key=lambda b: (b[1].top < title.top, b[1].top))
            return key(2, info.kind in ("title", "secHead"), extras - 1, info.kind == "title"), \
                replace(choice, text_idx=below[0][0])
        return (key(1, False, extras, 0), choice) if not strict else None
    if need == "section":
        if strict and info.kind == "secHead":
            return key(3, True, extras, 0), choice
        if strict and SECTION_NAME.search(info.layout.name):
            return key(2, False, extras, 0), choice
        if strict and not (info.title_usable and open_area and not bigs):
            return None
        return key(1 if strict else 0, info.kind == "titleOnly", extras, 0), choice
    if need == "two":
        pairs = [(a, b) for a in info.bodies for b in info.bodies
                 if a[1].right <= b[1].left + GAP and _big(a[1], frame, PAIR_WIDTH_SHARE)
                 and _big(b[1], frame, PAIR_WIDTH_SHARE) and abs(a[1].top - b[1].top) <= PAIR_TOP_SHARE * frame.height]
        if pairs:
            left, right = max(pairs, key=lambda p: min(p[0][1].area, p[1][1].area))
            return key(3, info.kind == "twoObj", extras - 2, min(left[1].area, right[1].area)), \
                replace(choice, text_idx=left[0], chart_idx=right[0])
        if bigs:
            return key(2, info.kind == "obj", extras - 1, bigs[0][1].area), \
                replace(choice, text_idx=bigs[0][0], split=True)
        if open_area:
            return key(1, info.kind == "titleOnly", extras, area.area), replace(choice, split=True)
        return None
    if need == "chart":
        if open_area and not bigs:
            return key(2, info.kind == "titleOnly", extras, area.area), choice
        if bigs:
            return key(1, info.kind == "obj", extras - 1, bigs[0][1].area), replace(choice, chart_idx=bigs[0][0])
        return None
    if bigs:  # content
        return key(2, info.kind == "obj", extras - 1, bigs[0][1].area), replace(choice, text_idx=bigs[0][0])
    if open_area:
        return key(1, info.kind == "titleOnly", extras, area.area), choice
    return None


def _plan(prs: Any, need: str) -> Choice:
    """Best layout for a need: strict geometry first, then relaxed (side titles, titles moved up)."""
    frame = _frame(prs)
    infos = [_analyse(layout, order, frame) for order, layout in enumerate(prs.slide_layouts)]
    for strict in (True, False):
        fits = [fit for info in infos if (fit := _fit(info, need, strict, frame)) is not None]
        if fits:
            return max(fits, key=lambda fit: fit[0])[1]
    info = next((i for i in infos if i.title is not None), infos[0])
    return Choice(info, _title_target(info, frame, need))


def pick_layout(prs: Any, kind: str, with_chart: bool, with_bullets: bool | None = None) -> Any:
    """Choose a template layout by placeholder geometry (works with any team template)."""
    bullets = kind != "chart" if with_bullets is None else with_bullets
    return _plan(prs, _need(kind, bullets, with_chart)).info.layout


# --- slide assembly ---------------------------------------------------------------------------

def _clear_slides(prs: Any) -> None:
    ids = prs.slides._sldIdLst
    for sld_id in list(ids):
        prs.part.drop_rel(sld_id.rId)
        ids.remove(sld_id)


def _remove(shape: Any) -> None:
    element = shape._element
    element.getparent().remove(element)


def _set_box(shape: Any, box: Box) -> None:
    shape.left, shape.top, shape.width, shape.height = Emu(box.left), Emu(box.top), Emu(box.width), Emu(box.height)


def _fill(text_frame: Any, lines: Sequence[str]) -> None:
    text_frame.paragraphs[0].text = lines[0] if lines else ""
    for line in lines[1:]:
        text_frame.add_paragraph().text = line


def _local(element: Any) -> str:
    return str(element.tag).rsplit("}", 1)[-1]


def _insert_in_order(parent: Any, child: Any) -> None:
    rank = PPR_ORDER.index(_local(child))
    for existing in parent:
        name = _local(existing)
        if name in PPR_ORDER and PPR_ORDER.index(name) > rank:
            existing.addprevious(child)
            return
    parent.append(child)


def _bullet(paragraph: Any) -> None:
    props = paragraph._p.get_or_add_pPr()
    for child in list(props):
        if _local(child) in BULLET_TAGS:
            props.remove(child)
    props.set("marL", str(int(Inches(0.3))))
    props.set("indent", str(-int(Inches(0.3))))
    _insert_in_order(props, props.makeelement(qn("a:buChar"), {"char": "•"}))


def _textbox(slide: Any, box: Box, lines: Sequence[str], size: int, bullets: bool) -> Any:
    shape = slide.shapes.add_textbox(Emu(box.left), Emu(box.top), Emu(box.width), Emu(box.height))
    frame = shape.text_frame
    frame.word_wrap = True
    _fill(frame, lines)
    for paragraph in frame.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(size)
        if bullets:
            _bullet(paragraph)
    return shape


def _picture(slide: Any, path: Path, box: Box) -> None:
    with Image.open(path) as image:
        w_px, h_px = image.size
    scale = min(box.width / w_px, box.height / h_px)
    w, h = int(w_px * scale), int(h_px * scale)
    slide.shapes.add_picture(str(path), Emu(box.left + (box.width - w) // 2), Emu(box.top + (box.height - h) // 2),
                             Emu(w), Emu(h))


def _halves(box: Box) -> tuple[Box, Box]:
    half = box.width // 2
    return (Box(box.left, box.top, half - int(GAP) // 2, box.height),
            Box(box.left + half + int(GAP) // 2, box.top, box.width - half - int(GAP) // 2, box.height))


def _clip(box: Box, bottom: int) -> Box:
    return replace(box, height=max(int(MIN_AREA_HEIGHT), min(box.bottom, bottom) - box.top))


def footer_box(layout: Any, frame: Frame) -> Box:
    """The footer band, narrowed to its widest stretch free of logos and side bars."""
    band = frame.footer
    cuts = sorted((box.left - int(GAP) // 2, box.right + int(GAP) // 2)
                  for box in decor_boxes(layout, frame.width, frame.height)
                  if box.top < band.bottom and box.bottom > band.top)
    stretches, start = [], band.left
    for cut_left, cut_right in cuts:
        if cut_left > start:
            stretches.append((start, min(cut_left, band.right)))
        start = max(start, cut_right)
    if start < band.right:
        stretches.append((start, band.right))
    left, right = max(stretches, key=lambda s: s[1] - s[0], default=(band.left, band.right))
    return Box(left, band.top, max(int(Inches(1)), right - left), band.height)


def _sources(slide: Any, box: Box, label: str, text: str) -> None:
    shape = _textbox(slide, box, [f"{label} {text}"], 9, bullets=False)
    shape.name = SOURCES_NAME
    for run in shape.text_frame.paragraphs[0].runs:
        run.font.color.rgb = SOURCE_GREY


def _placeholder(slide: Any, idx: int | None) -> Any:
    return next((ph for ph in slide.placeholders if ph.placeholder_format.idx == idx), None)


def _fill_title_slide(slide: Any, spec: SlideSpec, choice: Choice, title: Box, used: set[int]) -> list[str]:
    if not spec.subtitle:
        return []
    target = _placeholder(slide, choice.text_idx)
    where = f"slide '{spec.title}'"
    if target is not None:
        target.text = spec.subtitle
        used.add(target.placeholder_format.idx)
        if target.placeholder_format.type == PP_PLACEHOLDER.SUBTITLE:
            return []
        return [f"{where}: the template's title layout has no subtitle placeholder; subtitle put in its text box"]
    box = Box(title.left, title.bottom + int(GAP), title.width, int(Inches(0.8)))
    _textbox(slide, box, [spec.subtitle], 20, bullets=False)
    return [f"{where}: the template has no subtitle placeholder; subtitle added as a text box under the title"]


def _fill_content(prs: Any, slide: Any, spec: SlideSpec, choice: Choice, title: Box | None, frame: Frame,
                  chart_path: Path | None, used: set[int]) -> None:
    layout = choice.info.layout
    bottom = _bottom_limit(layout, frame)
    area = free_area(layout, frame, title)
    text_ph = _placeholder(slide, choice.text_idx) if spec.bullets else None
    chart_ph = _placeholder(slide, choice.chart_idx) if chart_path is not None else None
    chart_box = area
    if text_ph is not None:
        _fill(text_ph.text_frame, spec.bullets)
        used.add(text_ph.placeholder_format.idx)
        if choice.split and chart_path is not None and (body := shape_box(text_ph)) is not None:
            text_box, chart_box = _halves(_clip(body, bottom))
            _set_box(text_ph, text_box)
    elif spec.bullets:
        text_box = area
        if chart_path is not None:
            text_box, chart_box = _halves(area)
        _textbox(slide, text_box, spec.bullets, BULLET_PT, bullets=True)
    if chart_path is None:
        return
    if chart_ph is not None and (body := shape_box(chart_ph)) is not None:
        chart_box = _clip(body, bottom)
    _picture(slide, chart_path, chart_box)


def _add_slide(prs: Any, spec: SlideSpec, charts_dir: Path, choice: Choice, frame: Frame, label: str) -> list[str]:
    slide = prs.slides.add_slide(choice.info.layout)
    used: set[int] = set()
    warnings: list[str] = []
    title_ph = _placeholder(slide, choice.info.title_idx)
    title = choice.title
    if title_ph is not None and title is not None:
        title_ph.text = spec.title
        used.add(title_ph.placeholder_format.idx)
        if title != choice.info.title:
            _set_box(title_ph, title)
    else:
        title = Box(frame.left, int(MARGIN), frame.right - frame.left, int(Inches(1)))
        _textbox(slide, title, [spec.title], 32, bullets=False).name = "Title"
    chart_path = charts_dir / f"{spec.chart}.png" if spec.chart else None
    if spec.kind == "title":
        warnings += _fill_title_slide(slide, spec, choice, title, used)
    elif spec.kind in ("content", "chart"):
        _fill_content(prs, slide, spec, choice, title, frame, chart_path, used)
    for ph in list(slide.placeholders):
        if ph.placeholder_format.idx not in used:
            _remove(ph)
    if spec.sources:
        _sources(slide, footer_box(choice.info.layout, frame), label, spec.sources)
    header = f"[{spec.speaker} - {spec.minutes:g} min] " if spec.speaker else ""
    slide.notes_slide.notes_text_frame.text = (header + spec.notes).strip()
    return warnings


def _ticker(project: Path) -> str:
    profile = project / "company-profile.yaml"
    try:
        doc = _read_yaml(profile) if profile.is_file() else None
    except DeckInputError:
        doc = None
    ticker = doc.get("company", {}).get("ticker") if isinstance(doc, dict) else None
    return re.sub(r"[^A-Za-z0-9]+", "-", str(ticker or "DECK")).strip("-") or "DECK"


def open_presentation(template: Path | None) -> Any:
    """Open a .pptx (or a .potx, converted in memory); DeckInputError when it is not a presentation."""
    if template is None:
        return Presentation()
    bad = DeckInputError([f"{template.name} is not a valid .pptx file (open it in PowerPoint and save as .pptx)"])
    try:
        data = template.read_bytes()
        with zipfile.ZipFile(io.BytesIO(data)) as package:
            types = package.read("[Content_Types].xml")
            if TEMPLATE_MAIN in types:
                buffer = io.BytesIO()
                with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as out:
                    for item in package.infolist():
                        content = package.read(item.filename)
                        if item.filename == "[Content_Types].xml":
                            content = content.replace(TEMPLATE_MAIN, PRESENTATION_MAIN)
                        out.writestr(item, content)
                data = buffer.getvalue()
        return Presentation(io.BytesIO(data))
    except (PackageNotFoundError, zipfile.BadZipFile, KeyError, ValueError):
        raise bad from None
    except OSError as exc:
        raise DeckInputError([f"cannot read {template.name}: {exc.strerror or exc}"]) from None


def _label(deck: dict[str, Any]) -> str:
    language = str(deck.get("language") or "en").strip().lower()[:2]
    return SOURCE_LABELS.get(language, SOURCE_LABELS["en"])


def build(project: Path, template: Path | None) -> tuple[Path, list[str]]:
    deck, slides, warnings = load_outline(project / "pitch" / "outline.yaml", project / "report" / "charts")
    prs = open_presentation(template)
    _clear_slides(prs)
    frame = _frame(prs)
    plans: dict[str, Choice] = {}
    for spec in slides:
        need = _need(spec.kind, bool(spec.bullets), bool(spec.chart))
        choice = plans.get(need) or plans.setdefault(need, _plan(prs, need))
        warnings += _add_slide(prs, spec, project / "report" / "charts", choice, frame, _label(deck))
    out_dir = project / "pitch"
    ticker = _ticker(project)
    pattern = re.compile(rf"^{re.escape(ticker)}_deck_v(\d+)\.pptx$")
    versions = [int(m.group(1)) for p in out_dir.glob("*.pptx") if (m := pattern.match(p.name))]
    target = out_dir / f"{ticker}_deck_v{max(versions, default=0) + 1}.pptx"
    prs.save(str(target))
    return target, warnings


def _layout_lines(prs: Any) -> Iterator[str]:
    for i, layout in enumerate(prs.slide_layouts):
        kinds = ", ".join(sorted(str(ph.placeholder_format.type).split(" ")[0] for ph in layout.placeholders))
        yield f"{i}: {ascii_safe(layout.name)} | placeholders: {ascii_safe(kinds)}"


def list_layouts(template: Path | None) -> None:
    prs = open_presentation(template)
    for line in _layout_lines(prs):
        print(line)
    for kind, need in (("title", "title"), ("section", "section"), ("content", "content"),
                       ("content + chart", "two"), ("chart", "chart")):
        print(f"  {kind} slides -> {ascii_safe(_plan(prs, need).info.layout.name)}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the pitch deck from pitch/outline.yaml.")
    parser.add_argument("--project", default=".", help="Team project folder")
    parser.add_argument("--template", help="Team .pptx/.potx template (default: pitch/template.pptx)")
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
