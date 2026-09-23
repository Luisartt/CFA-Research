"""Assemble the written report body as an A4 .docx.

Inputs (team project folder):
  report/header.yaml            first-page header fields
  report/sections/NN-slug.md    one file per section, sorted by NN; 99-appendix* starts the appendix
  report/charts/*.png           images referenced from the sections with ![caption](../charts/x.png)

The official CFA Institute cover page is NOT generated; the team puts it in front.
--check prints the page budget per section and paragraphs with numbers but no citation,
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
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_IO_ERROR = 4
PAGE_LIMIT = 10
WORDS_PER_PAGE = 500
PAGES_PER_FIGURE = 0.3
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
MARGIN = Mm(20)
CITATION = re.compile(r"\([^()]*\b(19|20)\d{2}\b[^()]*\)|Source:", re.IGNORECASE)
HAS_NUMBER = re.compile(r"\d")
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


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


def parse_markdown(source: str) -> list[Block]:
    """A small Markdown subset: #/##/### headings, paragraphs, - and 1. lists, images, pipe tables."""
    blocks: list[Block] = []
    paragraph: list[str] = []
    table: list[list[str]] = []

    def flush() -> None:
        if paragraph:
            blocks.append(Block("paragraph", " ".join(paragraph)))
            paragraph.clear()
        if table:
            blocks.append(Block("table", rows=[row[:] for row in table]))
            table.clear()

    for raw in source.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("|") and line.endswith("|"):
            if paragraph:
                flush()
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                table.append(cells)
            continue
        if table:
            flush()
        heading = re.match(r"^(#{1,3})\s+(.*)$", line)
        image = re.match(r"^!\[(.*)\]\((.+)\)$", line)
        bullet = re.match(r"^[-*]\s+(.*)$", line)
        number = re.match(r"^\d+\.\s+(.*)$", line)
        if heading:
            flush()
            blocks.append(Block("heading", heading.group(2), level=len(heading.group(1))))
        elif image:
            flush()
            blocks.append(Block("image", image.group(1), path=image.group(2)))
        elif bullet:
            flush()
            blocks.append(Block("bullet", bullet.group(1)))
        elif number:
            flush()
            blocks.append(Block("number", number.group(1)))
        else:
            paragraph.append(line)
    flush()
    return blocks


def _slug(path: Path) -> str:
    return re.sub(r"^\d+-", "", path.stem)


def load_header(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ReportInputError(["report/header.yaml not found: the report skill writes it (company, rating, price, target)"])
    doc = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    if not isinstance(doc, dict):
        raise ReportInputError(["report/header.yaml must be a mapping (key: value)"])
    problems = [f"report/header.yaml: {name} is missing" for name in HEADER_FIELDS if doc.get(name) in (None, "")]
    rating = str(doc.get("recommendation", "")).upper()
    if rating and rating not in RATINGS:
        problems.append("report/header.yaml: recommendation must be BUY, HOLD or SELL")
    for name in ("price", "target_price"):
        value = doc.get(name)
        if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0):
            problems.append(f"report/header.yaml: {name} must be a positive number")
    if problems:
        raise ReportInputError(problems)
    doc["recommendation"] = rating
    return doc


def load_sections(folder: Path) -> list[tuple[Path, list[Block]]]:
    files = sorted(folder.glob("*.md")) if folder.is_dir() else []
    if not files:
        raise ReportInputError(["report/sections/ has no .md files: write the sections first"])
    return [(path, parse_markdown(path.read_text(encoding="utf-8-sig"))) for path in files]


def _words(blocks: Sequence[Block]) -> int:
    count = 0
    for block in blocks:
        if block.kind == "table":
            count += sum(len(cell.split()) for row in block.rows for cell in row)
        elif block.kind != "image":
            count += len(block.text.split())
    return count


def budget_rows(sections: Sequence[tuple[Path, list[Block]]]) -> list[tuple[str, int, int, float, float | None]]:
    rows: list[tuple[str, int, int, float, float | None]] = []
    for path, blocks in sections:
        slug = _slug(path)
        if slug.startswith("appendix"):
            continue
        figures = sum(1 for b in blocks if b.kind == "image")
        pages = _words(blocks) / WORDS_PER_PAGE + figures * PAGES_PER_FIGURE
        rows.append((slug, _words(blocks), figures, round(pages, 2), BUDGET_PAGES.get(slug)))
    return rows


def uncited(sections: Sequence[tuple[Path, list[Block]]]) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for path, blocks in sections:
        for block in blocks:
            if block.kind in ("paragraph", "bullet", "number") and HAS_NUMBER.search(block.text) \
                    and not CITATION.search(block.text):
                found.append((_slug(path), block.text[:70]))
    return found


def _add_runs(paragraph: Any, text: str, size: float = 10) -> None:
    for part in INLINE.split(text):
        if not part:
            continue
        bold = part.startswith("**") and part.endswith("**")
        italic = not bold and part.startswith("*") and part.endswith("*")
        run = paragraph.add_run(part.strip("*") if (bold or italic) else part)
        run.bold, run.italic = bold, italic
        run.font.name, run.font.size = FONT, Pt(size)


def _shade(cell: Any, hex_color: str) -> None:
    shading = OxmlElement("w:shd")
    shading.set(qn("w:val"), "clear")
    shading.set(qn("w:color"), "auto")
    shading.set(qn("w:fill"), hex_color)
    cell._tc.get_or_add_tcPr().append(shading)


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
    for (label, value), row in zip(rows, table.rows):
        _shade(row.cells[0], "DDEBF7")
        _add_runs(row.cells[0].paragraphs[0], f"**{label}**", 9)
        _add_runs(row.cells[1].paragraphs[0], f"**{value}**" if label == "Recommendation" else value, 9)
        if label == "Recommendation":
            row.cells[1].paragraphs[0].runs[0].font.color.rgb = RGBColor.from_string(RATINGS[value])
    doc.add_paragraph()


def _table(doc: Any, rows: list[list[str]]) -> None:
    width = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    for i, cells in enumerate(rows):
        for j in range(width):
            text = cells[j] if j < len(cells) else ""
            paragraph = table.rows[i].cells[j].paragraphs[0]
            _add_runs(paragraph, f"**{text}**" if i == 0 and text else text, 8)
            if i == 0:
                _shade(table.rows[i].cells[j], "DDEBF7")
    doc.add_paragraph()


def build(project: Path, header: dict[str, Any], sections: Sequence[tuple[Path, list[Block]]]) -> Path:
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Mm(210), Mm(297)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(section, side, MARGIN)
    usable = section.page_width - section.left_margin - section.right_margin  # type: ignore[operator]
    doc.styles["Normal"].font.name = FONT
    doc.styles["Normal"].font.size = Pt(10)
    _header_block(doc, header)
    figure = 0
    for path, blocks in sections:
        if _slug(path).startswith("appendix"):
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        for block in blocks:
            if block.kind == "heading":
                heading = doc.add_heading(level=min(block.level, 3))
                _add_runs(heading, block.text, 14 if block.level == 1 else 11)
                for run in heading.runs:
                    run.font.color.rgb = NAVY
            elif block.kind == "paragraph":
                _add_runs(doc.add_paragraph(), block.text)
            elif block.kind in ("bullet", "number"):
                style = "List Bullet" if block.kind == "bullet" else "List Number"
                _add_runs(doc.add_paragraph(style=style), block.text)
            elif block.kind == "table":
                _table(doc, block.rows)
            elif block.kind == "image":
                image = (path.parent / block.path).resolve()
                if not image.is_file():
                    raise ReportInputError([f"{path.name}: image not found: {block.path} (run charts.py first)"])
                shape = doc.add_picture(str(image))
                if shape.width > usable:
                    shape.height = int(shape.height * usable / shape.width)
                    shape.width = usable
                figure += 1
                caption = doc.add_paragraph()
                _add_runs(caption, f"*Figure {figure}: {block.text}*", 8)
    out_dir = project / "report"
    ticker = re.sub(r"[^A-Za-z0-9]+", "-", str(header["ticker"])).strip("-") or "REPORT"
    pattern = re.compile(rf"^{re.escape(ticker)}_report_v(\d+)\.docx$")
    versions = [int(m.group(1)) for p in out_dir.glob("*.docx") if (m := pattern.match(p.name))]
    target = out_dir / f"{ticker}_report_v{max(versions, default=0) + 1}.docx"
    doc.save(str(target))
    return target


def _print_check(sections: Sequence[tuple[Path, list[Block]]]) -> None:
    rows = budget_rows(sections)
    print("section                 words  figures  pages  budget")
    for slug, words, figures, pages, budget in rows:
        flag = "[over]" if budget is not None and pages > budget * 1.1 else "      "
        budget_text = "-" if budget is None else f"{budget:.1f}"
        print(f"{flag} {ascii_safe(slug):<18} {words:>5}  {figures:>7}  {pages:>5.1f}  {budget_text:>6}")
    total = sum(r[3] for r in rows)
    print(f"total estimated pages: {total:.1f} of {PAGE_LIMIT} (appendix not counted)")
    if total > PAGE_LIMIT:
        print("[x] over the 10-page limit: cut before building")
    missing = [s for s in BUDGET_PAGES if s not in {r[0] for r in rows}]
    if missing:
        print("[warn] sections not written yet: " + ", ".join(missing))
    flagged = uncited(sections)
    print(f"uncited paragraphs with numbers: {len(flagged)}")
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
