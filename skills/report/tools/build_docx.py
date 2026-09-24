"""Assemble the written report body as an A4 .docx.

Inputs (team project folder):
  report/header.yaml            first-page header fields
  report/sections/NN-slug.md    one file per section, sorted by NN; 98-appendix.md and then
                                99-appendix-ai-use.md each start on a new page
  report/charts/*.png           images referenced from the sections with ![caption](../charts/x.png)

The official CFA Institute cover page is NOT generated; the team puts it in front.
--check prints the page budget per section and paragraphs or tables with numbers but no citation,
without writing a file. Console output is ASCII only.

Usage: python build_docx.py --project <team folder> [--check]
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.image.image import Image as DocxImage
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Length, Mm, Pt, RGBColor
from docx.text.paragraph import Paragraph

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_IO_ERROR = 4
PAGE_LIMIT = 10
WORDS_PER_PAGE = 500
PAGES_PER_FIGURE = 0.3  # a narrow figure on its own line, or any figure whose file is not on disk yet
PAGES_PER_PAIR = 0.3  # two narrow figures side by side (0.15 each)
PAGES_PER_FULL_FIGURE = 0.45  # a figure wider than PAIR_MAX_SHARE of the text width
HEADER_PAGES = 0.25  # the first-page header block
BUDGET_PAGES: dict[str, float] = {
    "investment-summary": 1.5,
    "business-description": 0.5,
    "industry": 1.0,
    "financial-analysis": 2.0,
    "valuation": 2.0,
    "risks": 1.5,
    "esg": 1.5,
}
RATINGS = {"BUY": "00B050", "HOLD": "BF8F00", "SELL": "C00000"}
HEADER_FIELDS = ("company", "exchange", "ticker", "sector", "industry", "recommendation", "price",
                 "price_date", "currency", "target_price", "report_date")
FONT = "Arial"
NAVY = RGBColor(0x1F, 0x4E, 0x79)
GREY = RGBColor(0x59, 0x59, 0x59)
RULE_COLOR = "1F4E79"
HEADER_FILL = "DDEBF7"
PAGE_WIDTH, PAGE_HEIGHT = Mm(210), Mm(297)  # A4
MARGIN = Mm(20)
USABLE_WIDTH = Length(int(PAGE_WIDTH) - 2 * int(MARGIN))
LABEL_WIDTH, VALUE_WIDTH = Mm(45), Mm(125)
CELL_PADDING = Mm(4)  # left + right cell margins Word adds around a picture in a table cell
PAIR_MAX_SHARE = 0.55  # images at most this share of the text width may sit side by side
HEADING_SIZES = {1: 11.0, 2: 10.5, 3: 10.0}

# Author-date "(Acme, 2025a, p. 4)", "(Acme, 2025, pp. 4-6)", "(Acme, 3Q25 earnings call)", "(INEGI, n.d.)",
# "(team estimate)" / "(team model)", and mixed ones such as "(team model; Acme, 2025)".
_OTHER_SOURCES = r"(?:[^()]*;\s*)?"  # earlier sources in a mixed citation, separated by ";"
CITATION = re.compile(
    rf"\({_OTHER_SOURCES}[A-Z][^()]*?,?\s(19|20)\d{{2}}[a-z]?([,;][^()]*)?\)"
    rf"|\({_OTHER_SOURCES}[A-Z][^()]*,\s*\d[QH]\d{{2}}[^()]*\)"
    r"|\([^()]*n\.d\.\)"
    r"|\(team (estimate|model)\)"
)
# Numbers that are labels, not data: removed before looking for digits.
NOT_DATA = re.compile(r"\bFigure \d+|\bTable \d+|\bPillar \d+|\b\d[QH]\d{2}\b|\bFY\d+|\b\d{4}[AE]\b", re.IGNORECASE)
HAS_NUMBER = re.compile(r"\d")
SOURCE_LINE = re.compile(r"^source:", re.IGNORECASE)
NUMERIC = re.compile(r"^[-+(]?[$]?\s?\d[\d.,]*\s?(%|x|bps?|pp)?\)?$|^(n\.?m\.?|n\.?a\.?|-+)$", re.IGNORECASE)
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")

TABLE_SEPARATOR = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?$")
UNESCAPED_PIPE = re.compile(r"(?<!\\)\|")
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\([^)]*\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
IMAGE = re.compile(r"^!\[(.*)\]\((.+)\)$")
BULLET = re.compile(r"^[-*]\s+(.*)$")
NUMBER = re.compile(r"^\d+\.\s+(.*)$")
RULE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
CONTINUATION = re.compile(r"^( {2,}|\t)\S")

# Child order inside <w:tcPr> (ECMA-376); Word rejects cells whose properties are out of order.
TCPR_ORDER = ("cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap", "tcMar",
              "textDirection", "tcFitText", "vAlign", "hideMark")


class ReportInputError(Exception):
    def __init__(self, messages: list[str]) -> None:
        super().__init__("; ".join(messages))
        self.messages = messages


@dataclass
class Block:
    kind: str  # heading, paragraph, bullet, number, image, table
    text: str = ""
    level: int = 1
    path: str = ""
    rows: list[list[str]] = field(default_factory=list)


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


# --- Markdown ------------------------------------------------------------------------------------------

def _inline(text: str) -> str:
    """[text](url) -> text; runs of spaces collapse to one."""
    return " ".join(LINK.sub(r"\1", text).split())


def _cells(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|") and not text.endswith("\\|"):
        text = text[:-1]
    return [_inline(cell.replace("\\|", "|")) for cell in UNESCAPED_PIPE.split(text)]


def _strip_comments(source: str, where: str, errors: list[str]) -> str:
    """Drop <!-- ... --> comments, keeping their line breaks so line numbers stay right."""
    text = COMMENT.sub(lambda m: "\n" * m.group().count("\n"), source)
    start = text.find("<!--")
    if start >= 0:
        line = text.count("\n", 0, start) + 1
        errors.append(f"{where}line {line}: a '<!--' comment that is never closed is not supported; "
                      "use '-->' to close it")
        text = text[:start]
    return text


def _unsupported(line: str) -> str:
    """What is wrong with a line the report cannot render, or '' if it is fine."""
    heading = HEADING.match(line)
    if heading and len(heading.group(1)) > 3:
        return "a #### heading is not supported; use #, ## or ### (three levels at most)"
    if RULE.match(line):
        return "a horizontal rule (---) is not supported; use a heading or a blank line"
    if line.startswith(">"):
        return "a blockquote (>) is not supported; use a normal paragraph with its citation"
    return ""


def parse_markdown(source: str, name: str = "") -> list[Block]:
    """A small Markdown subset: #/##/### headings, paragraphs, - and 1. lists, images, pipe tables.

    Raises ReportInputError with every unsupported construct, as "<name>: line <n>: ...".
    """
    where = f"{name}: " if name else ""
    errors: list[str] = []
    lines = _strip_comments(source, where, errors).splitlines()
    blocks: list[Block] = []
    paragraph: list[str] = []
    item_open = False  # the last block is a list item that an indented line may continue

    def flush() -> None:
        if paragraph:
            blocks.append(Block("paragraph", _inline(" ".join(paragraph))))
            paragraph.clear()

    i = 0
    while i < len(lines):
        raw, number = lines[i], i + 1
        line = raw.strip()
        i += 1
        if not line:
            flush()
            item_open = False
            continue
        if item_open and CONTINUATION.match(raw):
            blocks[-1].text = _inline(f"{blocks[-1].text} {line}")
            continue
        item_open = False
        if "|" in line and i < len(lines) and TABLE_SEPARATOR.match(lines[i].strip()):
            flush()
            rows = [_cells(line)]
            i += 1  # the separator
            while i < len(lines) and "|" in lines[i]:
                if not TABLE_SEPARATOR.match(lines[i].strip()):
                    rows.append(_cells(lines[i]))
                i += 1
            blocks.append(Block("table", rows=rows))
            continue
        problem = _unsupported(line)
        if problem:
            errors.append(f"{where}line {number}: {problem}")
            continue
        heading, image = HEADING.match(line), IMAGE.match(line)
        bullet, numbered = BULLET.match(line), NUMBER.match(line)
        if heading:
            flush()
            blocks.append(Block("heading", _inline(heading.group(2)), level=len(heading.group(1))))
        elif image:
            flush()
            blocks.append(Block("image", _inline(image.group(1)), path=image.group(2)))
        elif bullet or numbered:
            flush()
            match = bullet or numbered
            assert match is not None
            blocks.append(Block("bullet" if bullet else "number", _inline(match.group(1))))
            item_open = True
        else:
            paragraph.append(line)
    flush()
    if errors:
        raise ReportInputError(errors)
    return blocks


# --- inputs --------------------------------------------------------------------------------------------

def _slug(path: Path) -> str:
    return re.sub(r"^\d+-", "", path.stem)


def _read_text(path: Path, shown: str) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        raise ReportInputError([f"{shown} is not UTF-8 text: save it as UTF-8 "
                                "(in VS Code: 'Save with Encoding' -> UTF-8)"]) from None


def load_header(path: Path) -> dict[str, Any]:
    shown = "report/header.yaml"
    if not path.is_file():
        raise ReportInputError([f"{shown} not found: the report skill writes it (company, rating, price, target)"])
    try:
        doc = yaml.safe_load(_read_text(path, shown))
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        line = f" at line {mark.line + 1}" if mark is not None else ""
        problem = getattr(exc, "problem", None) or "syntax error"
        raise ReportInputError([f"{shown} is not valid YAML{line}: {problem} (check quotes, colons and brackets)"]) \
            from None
    if not isinstance(doc, dict):
        raise ReportInputError([f"{shown} must be a mapping (key: value)"])
    problems = [f"{shown}: {name} is missing" for name in HEADER_FIELDS if doc.get(name) in (None, "")]
    ticker = doc.get("ticker")
    if ticker not in (None, "") and not isinstance(ticker, str):
        problems.append(f'{shown}: ticker must be text; put the ticker in quotes (ticker: "0700")')
    rating = str(doc.get("recommendation", "")).upper()
    if rating and rating not in RATINGS:
        problems.append(f"{shown}: recommendation must be BUY, HOLD or SELL")
    for name in ("price", "target_price"):
        value = doc.get(name)
        if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0):
            problems.append(f"{shown}: {name} must be a positive number")
    if problems:
        raise ReportInputError(problems)
    doc["recommendation"] = rating
    return doc


def load_sections(folder: Path) -> list[tuple[Path, list[Block]]]:
    files = sorted(folder.glob("*.md")) if folder.is_dir() else []
    if not files:
        raise ReportInputError(["report/sections/ has no .md files: write the sections first"])
    sections: list[tuple[Path, list[Block]]] = []
    errors: list[str] = []
    for path in files:
        try:
            sections.append((path, parse_markdown(_read_text(path, path.name), name=path.name)))
        except ReportInputError as exc:
            errors.extend(exc.messages)
    if errors:
        raise ReportInputError(errors)
    return sections


# --- checks --------------------------------------------------------------------------------------------

def _words(blocks: Sequence[Block]) -> int:
    count = 0
    for block in blocks:
        if block.kind == "table":
            count += sum(len(cell.split()) for row in block.rows for cell in row)
        elif block.kind != "image":
            count += len(block.text.split())
    return count


def _narrow(section: Path, block: Block, usable: Length) -> bool | None:
    """Like _fits_half, but None instead of an error when the image is not on disk or unreadable."""
    image = (section.parent / block.path).resolve()
    if not image.is_file():
        return None
    try:
        width = int(DocxImage.from_file(str(image)).width)
    except Exception:  # python-docx raises several types for files it cannot read as an image
        return None
    return width <= int(usable) * PAIR_MAX_SHARE


def _figure_pages(section: Path, blocks: Sequence[Block]) -> float:
    """Pages the figures take, pairing consecutive narrow images the way build() does."""
    pages = 0.0
    k = 0
    while k < len(blocks):
        block = blocks[k]
        k += 1
        if block.kind != "image":
            continue
        narrow = _narrow(section, block, USABLE_WIDTH)
        following = blocks[k] if k < len(blocks) else None
        if narrow and following is not None and following.kind == "image" \
                and _narrow(section, following, USABLE_WIDTH):
            pages += PAGES_PER_PAIR
            k += 1
        elif narrow is False:
            pages += PAGES_PER_FULL_FIGURE
        else:
            pages += PAGES_PER_FIGURE
    return pages


def budget_rows(sections: Sequence[tuple[Path, list[Block]]]) -> list[tuple[str, int, int, float, float | None]]:
    rows: list[tuple[str, int, int, float, float | None]] = []
    for path, blocks in sections:
        slug = _slug(path)
        if slug.startswith("appendix"):
            continue
        figures = sum(1 for b in blocks if b.kind == "image")
        pages = _words(blocks) / WORDS_PER_PAGE + _figure_pages(path, blocks)
        rows.append((slug, _words(blocks), figures, round(pages, 2), BUDGET_PAGES.get(slug)))
    return rows


def _has_data(text: str) -> bool:
    return bool(HAS_NUMBER.search(NOT_DATA.sub("", text)))


def _is_source(block: Block | None) -> bool:
    return block is not None and block.kind == "paragraph" and bool(SOURCE_LINE.match(block.text))


def uncited(sections: Sequence[tuple[Path, list[Block]]]) -> list[tuple[str, str]]:
    """Paragraphs and list items with data but no citation; tables with data and no 'Source:' line under them.

    Paragraphs and list items in the appendix are skipped: the reference list lives there.
    """
    found: list[tuple[str, str]] = []
    for path, blocks in sections:
        appendix = _slug(path).startswith("appendix")
        for k, block in enumerate(blocks):
            if block.kind in ("paragraph", "bullet", "number"):
                if appendix:
                    continue
                if _has_data(block.text) and not CITATION.search(block.text) and not _is_source(block):
                    found.append((_slug(path), block.text[:70]))
            elif block.kind == "table":
                following = blocks[k + 1] if k + 1 < len(blocks) else None
                if any(_has_data(cell) for row in block.rows for cell in row) and not _is_source(following):
                    header = " | ".join(block.rows[0])[:40]
                    found.append((_slug(path), f"table '{header}' has no 'Source:' line under it"))
    return found


def looks_numeric(text: str) -> bool:
    """True for cells such as 31.0, (1,234.5), +24.0%, 8.5x, 150bp, $12, n.m. or -."""
    return bool(NUMERIC.match(text.strip().strip("*").strip()))


# --- docx helpers --------------------------------------------------------------------------------------

def _add_runs(paragraph: Any, text: str, size: float = 10, bold: bool = False) -> None:
    """Add **bold** / *italic* runs. Unmarked runs inherit (None) so a bold heading style stays bold."""
    for part in INLINE.split(text):
        if not part:
            continue
        strong = part.startswith("**") and part.endswith("**")
        italic = not strong and part.startswith("*") and part.endswith("*")
        run = paragraph.add_run(part.strip("*") if (strong or italic) else part)
        run.bold = True if (strong or bold) else None
        run.italic = True if italic else None
        run.font.name, run.font.size = FONT, Pt(size)


def _tight(paragraph: Any) -> None:
    paragraph.paragraph_format.space_after = Pt(0)
    paragraph.paragraph_format.line_spacing = 1.0


def _set_tcpr(cell: Any, element: Any) -> None:
    """Put a cell property in its schema position, replacing an existing one of the same kind."""
    tc_pr = cell._tc.get_or_add_tcPr()
    local = element.tag.split("}")[1]
    for old in tc_pr.findall(element.tag):
        tc_pr.remove(old)
    rank = TCPR_ORDER.index(local)
    for child in tc_pr:
        name = child.tag.split("}")[1]
        if name in TCPR_ORDER and TCPR_ORDER.index(name) > rank:
            child.addprevious(element)
            return
    tc_pr.append(element)


def _shade(cell: Any, hex_color: str) -> None:
    shading = OxmlElement("w:shd")
    shading.set(qn("w:val"), "clear")
    shading.set(qn("w:color"), "auto")
    shading.set(qn("w:fill"), hex_color)
    _set_tcpr(cell, shading)


def _rule(cell: Any, *edges: str) -> None:
    """Horizontal rules on the given edges ("top", "bottom") of a cell."""
    borders = OxmlElement("w:tcBorders")
    for edge in edges:
        line = OxmlElement(f"w:{edge}")
        line.set(qn("w:val"), "single")
        line.set(qn("w:sz"), "6")
        line.set(qn("w:space"), "0")
        line.set(qn("w:color"), RULE_COLOR)
        borders.append(line)
    _set_tcpr(cell, borders)


def _column_widths(table: Any, widths: Sequence[Length]) -> None:
    table.autofit = False
    for column, width in zip(table.columns, widths):
        column.width = width
    for row in table.rows:
        for cell, width in zip(row.cells, widths):
            cell.width = width


def _header_block(doc: Any, header: dict[str, Any]) -> None:
    upside = header["target_price"] / header["price"] - 1
    rows = (
        ("Company", str(header["company"])),
        ("Exchange: ticker", f"{header['exchange']}: {header['ticker']}"),
        ("Sector / industry", f"{header['sector']} / {header['industry']}"),
        ("Recommendation", header["recommendation"]),
        ("Price (date)", f"{header['currency']} {header['price']:,.2f} ({header['price_date']})"),
        ("Target price (upside)", f"{header['currency']} {header['target_price']:,.2f} ({upside:+.1%})"),
        ("Report date", str(header["report_date"])),
    )
    table = doc.add_table(rows=len(rows), cols=2)
    _column_widths(table, (LABEL_WIDTH, VALUE_WIDTH))
    for (label, value), row in zip(rows, table.rows):
        _shade(row.cells[0], HEADER_FILL)
        label_paragraph, value_paragraph = row.cells[0].paragraphs[0], row.cells[1].paragraphs[0]
        _add_runs(label_paragraph, label, 9, bold=True)
        _add_runs(value_paragraph, value, 9, bold=label == "Recommendation")
        _tight(label_paragraph)
        _tight(value_paragraph)
        if label == "Recommendation":
            value_paragraph.runs[0].font.color.rgb = RGBColor.from_string(RATINGS[value])
    doc.add_paragraph()


def _table(doc: Any, rows: list[list[str]], spacer: bool = True) -> None:
    """A data table; spacer=False when a 'Source:' line follows, so it sits right under the table."""
    width = max(len(r) for r in rows)
    grid = [[cells[j] if j < len(cells) else "" for j in range(width)] for cells in rows]
    body = grid[1:]
    numeric_columns = {j for j in range(width)
                       if any(r[j] for r in body) and all(looks_numeric(r[j]) for r in body if r[j])}
    table = doc.add_table(rows=len(grid), cols=width)
    last = len(grid) - 1
    for i, cells in enumerate(grid):
        for j, text in enumerate(cells):
            cell = table.rows[i].cells[j]
            paragraph = cell.paragraphs[0]
            _add_runs(paragraph, text, 8, bold=i == 0)
            _tight(paragraph)
            if (i == 0 and j in numeric_columns) or (i > 0 and looks_numeric(text)):
                paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            if i == 0:
                _shade(cell, HEADER_FILL)
                _rule(cell, "top", "bottom")
            elif i == last:
                _rule(cell, "bottom")
    if spacer:
        doc.add_paragraph()


def _source_line(doc: Any, text: str) -> None:
    """The 'Source:' line under a table: 8 pt grey, with the gap the table spacer would have left after it."""
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_after = Pt(12)
    _add_runs(paragraph, text, 8)
    for run in paragraph.runs:
        run.font.color.rgb = GREY


def _image_path(section: Path, block: Block) -> Path:
    image = (section.parent / block.path).resolve()
    if not image.is_file():
        raise ReportInputError([f"{section.name}: image not found: {block.path} (run charts.py first)"])
    return image


def _not_an_image(section: Path, block: Block) -> ReportInputError:
    return ReportInputError([f"{section.name}: {block.path} is not an image Word can place: "
                             "use PNG or JPEG (SVG is not supported)"])


def _fits_half(section: Path, block: Block, usable: Length) -> bool:
    """True if the image at its own size is narrow enough to share the line with another one."""
    _image_path(section, block)  # raises when the file is missing
    narrow = _narrow(section, block, usable)
    if narrow is None:
        raise _not_an_image(section, block)
    return narrow


def _picture(paragraph: Any, section: Path, block: Block, max_width: Length) -> None:
    """Centered picture, scaled down to max_width, kept on the page of its caption."""
    image = _image_path(section, block)
    try:
        shape = paragraph.add_run().add_picture(str(image))
    except Exception:  # python-docx raises several types for files it cannot read as an image
        raise _not_an_image(section, block) from None
    if shape.width > max_width:
        shape.height = int(shape.height * max_width / shape.width)
        shape.width = max_width
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.keep_with_next = True


def _caption(paragraph: Any, number: int, text: str) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_runs(paragraph, f"*Figure {number}: {text}*", 8)


def _image_pair(doc: Any, section: Path, pair: tuple[Block, Block], first: int, usable: Length) -> None:
    half = Length(int(usable) // 2)
    table = doc.add_table(rows=1, cols=2)
    _column_widths(table, (half, half))
    for offset, (cell, block) in enumerate(zip(table.rows[0].cells, pair)):
        picture = cell.paragraphs[0]
        _picture(picture, section, block, Length(int(half) - int(CELL_PADDING)))
        _tight(picture)
        caption = cell.add_paragraph()
        _caption(caption, first + offset, block.text)
        _tight(caption)
    doc.add_paragraph()


def _numbered_list(doc: Any) -> int:
    """A new w:num on the "List Number" definition that starts again at 1; returns its numId."""
    numbering = doc.part.numbering_part.element
    style_num = doc.styles["List Number"].element.pPr.numPr.numId.val
    abstract = numbering.num_having_numId(style_num).abstractNumId.val
    num = numbering.add_num(abstract)
    num.add_lvlOverride(ilvl=0).add_startOverride(1)
    return int(num.numId)


def _set_numbering(paragraph: Any, num_id: int) -> None:
    num_pr = paragraph._p.get_or_add_pPr().get_or_add_numPr()
    num_pr.get_or_add_ilvl().val = 0
    num_pr.get_or_add_numId().val = num_id


def _break_before(doc: Any, element: Any) -> None:
    """Start a page at element: on the paragraph itself, or on an empty paragraph put before a table."""
    if element.tag != qn("w:p"):
        spacer = OxmlElement("w:p")
        element.addprevious(spacer)
        element = spacer
    Paragraph(element, doc._body).paragraph_format.page_break_before = True


# --- build ---------------------------------------------------------------------------------------------

def build(project: Path, header: dict[str, Any], sections: Sequence[tuple[Path, list[Block]]]) -> Path:
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = PAGE_WIDTH, PAGE_HEIGHT
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(section, side, MARGIN)
    usable = USABLE_WIDTH
    doc.styles["Normal"].font.name = FONT
    doc.styles["Normal"].font.size = Pt(10)
    _header_block(doc, header)
    body = doc.element.body
    figure = 0
    num_id: int | None = None
    for path, blocks in sections:
        new_page = _slug(path).startswith("appendix")
        k = 0
        while k < len(blocks):
            block = blocks[k]
            k += 1
            start = len(body) - 1  # new content goes before the closing w:sectPr
            if block.kind != "number":
                num_id = None
            if block.kind == "heading":
                level = min(block.level, 3)
                heading = doc.add_heading(level=level)
                _add_runs(heading, block.text, HEADING_SIZES[level])
                for run in heading.runs:
                    run.font.color.rgb = NAVY
            elif block.kind == "paragraph":
                if k >= 2 and blocks[k - 2].kind == "table" and _is_source(block):
                    _source_line(doc, block.text)
                else:
                    _add_runs(doc.add_paragraph(), block.text)
            elif block.kind == "bullet":
                _add_runs(doc.add_paragraph(style="List Bullet"), block.text)
            elif block.kind == "number":
                if num_id is None:
                    num_id = _numbered_list(doc)
                item = doc.add_paragraph(style="List Number")
                _set_numbering(item, num_id)
                _add_runs(item, block.text)
            elif block.kind == "table":
                _table(doc, block.rows, spacer=not _is_source(blocks[k] if k < len(blocks) else None))
            elif block.kind == "image":
                following = blocks[k] if k < len(blocks) else None
                if following is not None and following.kind == "image" \
                        and _fits_half(path, block, usable) and _fits_half(path, following, usable):
                    _image_pair(doc, path, (block, following), figure + 1, usable)
                    figure += 2
                    k += 1
                else:
                    _picture(doc.add_paragraph(), path, block, usable)
                    figure += 1
                    _caption(doc.add_paragraph(), figure, block.text)
            if new_page and len(body) - 1 > start:
                _break_before(doc, body[start])
                new_page = False
    out_dir = project / "report"
    ticker = re.sub(r"[^A-Za-z0-9]+", "-", str(header["ticker"])).strip("-") or "REPORT"
    pattern = re.compile(rf"^{re.escape(ticker)}_report_v(\d+)\.docx$")
    versions = [int(m.group(1)) for p in out_dir.glob("*.docx") if (m := pattern.match(p.name))]
    target = out_dir / f"{ticker}_report_v{max(versions, default=0) + 1}.docx"
    doc.save(str(target))
    return target


def _print_check(sections: Sequence[tuple[Path, list[Block]]]) -> None:
    rows = budget_rows(sections)
    width = max([len("header block")] + [len(ascii_safe(r[0])) for r in rows])
    print(f"       {'section':<{width}}  words  figures  pages  budget")
    print(f"       {'header block':<{width}}  {'-':>5}  {'-':>7}  {HEADER_PAGES:>5.2f}  {'-':>6}")
    for slug, words, figures, pages, budget in rows:
        flag = "[over]" if budget is not None and pages > budget * 1.1 else "      "
        budget_text = "-" if budget is None else f"{budget:.1f}"
        print(f"{flag} {ascii_safe(slug):<{width}}  {words:>5}  {figures:>7}  {pages:>5.2f}  {budget_text:>6}")
    total = sum(r[3] for r in rows) + HEADER_PAGES
    print(f"total estimated pages: {total:.1f} of {PAGE_LIMIT} (conservative estimate: {WORDS_PER_PAGE} words per page, "
          f"{PAGES_PER_FULL_FIGURE} page per full-width figure, {PAGES_PER_PAIR} per side-by-side pair, "
          f"{PAGES_PER_FIGURE} per other figure or chart not drawn yet; appendix not counted)")
    if total > PAGE_LIMIT:
        print("[x] over the 10-page limit: cut before building")
    missing = [s for s in BUDGET_PAGES if s not in {r[0] for r in rows}]
    if missing:
        print("[warn] sections not written yet: " + ", ".join(missing))
    flagged = uncited(sections)
    print(f"uncited paragraphs or tables with numbers: {len(flagged)}")
    for slug, text in flagged:
        print(f"  - [{ascii_safe(slug)}] {ascii_safe(text)}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the report body (A4 .docx) or check the page budget.")
    parser.add_argument("--project", default=".", help="Team project folder")
    parser.add_argument("--check", action="store_true", help="Print the page budget and uncited paragraphs only")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    try:
        sections = load_sections(project / "report" / "sections")
        if args.check:
            _print_check(sections)
            return EXIT_OK
        header = load_header(project / "report" / "header.yaml")
        target = build(project, header, sections)
    except ReportInputError as exc:
        print("[x] Cannot build the report. Fix these first:")
        for message in exc.messages:
            print("  - " + ascii_safe(message))
        return EXIT_INPUT_ERROR
    except OSError as exc:
        print(f"[x] Could not write the report: {ascii_safe(exc.strerror or str(exc))}. Close it in Word and run again.")
        return EXIT_IO_ERROR
    print(f"[ok] report -> report/{ascii_safe(target.name)}")
    print("Next: put the official CFA Institute cover page in front, then check the layout in Word.")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
