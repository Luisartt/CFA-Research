"""Build the report body (Word) in the layout of the La Comer template, with Bimbo's palette.

Reads report/header.yaml, report/sections/NN-*.md (included tables from report/tables/*.md) and report/charts/**.png.
Parsing and the uncited-number check come from the research-challenge skill (tools/build_docx.py).

Run:  .venv/bin/python report/build/build_report_docx.py [--check] [--out report/BIMBOA_report_v2.docx]
The official CFA cover page is put in front by the team.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Mm, Pt, RGBColor

SKILL_TOOLS = Path.home() / ".claude/skills/CFA-report/tools"
sys.path.insert(0, str(SKILL_TOOLS))
import build_docx as B  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = ROOT / "report/sections"
TABLES = ROOT / "report/tables"
BLUE, NAVY, RED = "0033A0", "001268", "EC1C2D"
PALE, BAND = "C9D6F2", "F2F2F2"
BODY, HEAD = "Times New Roman", "Gill Sans MT"
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")
TEXT_W = Mm(210 - 28)
HALF_W = Inches(3.45)
IMG_FULL_W = Inches(7.0)


def preprocess(text: str) -> str:
    def inc(m: re.Match) -> str:
        return (TABLES / f"{m.group(1)}.md").read_text()
    text = re.sub(r"^\{\{table:\s*([\w]+)\s*\}\}\s*$", inc, text, flags=re.M)
    return re.sub(r"\s*\(\{fig:[\w]+\}\)", "", text)


def load():
    out = []
    for p in sorted(SECTIONS.glob("[0-9]*.md")):
        out.append((p, B.parse_markdown(preprocess(p.read_text()), p.name)))
    return out


def runs(par, text, size=9.0, font=BODY, bold=False, italic=False, color=None):
    for part in INLINE.split(text):
        if not part:
            continue
        strong = part.startswith("**") and part.endswith("**")
        emph = not strong and part.startswith("*") and part.endswith("*") and len(part) > 2
        r = par.add_run(part.strip("*") if (strong or emph) else part)
        r.font.name, r.font.size = font, Pt(size)
        r._element.rPr.rFonts.set(qn("w:eastAsia"), font)
        r.bold = True if (strong or bold) else None
        r.italic = True if (emph or italic) else None
        if color:
            r.font.color.rgb = RGBColor.from_string(color)


def fmt(par, after=4, before=0, align=WD_ALIGN_PARAGRAPH.JUSTIFY, keep_next=False):
    pf = par.paragraph_format
    pf.space_after, pf.space_before, pf.line_spacing = Pt(after), Pt(before), 1.0
    par.alignment = align
    pf.keep_with_next = keep_next


def shade(cell, hex_):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hex_)
    tcPr.append(shd)


def cell_margins(table, top=20, bottom=20, left=50, right=50):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for k, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); mar.append(e)
    tblPr.append(mar)


def borders(table, color="BFBFBF", sz=4):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for k in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{k}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), "0"); e.set(qn("w:color"), color)
        b.append(e)
    tblPr.append(b)


class Builder:
    def __init__(self, header, sections):
        self.h, self.sections = header, sections
        self.doc = Document()
        self.fig_n = self.tab_n = 0
        s = self.doc.sections[0]
        s.page_width, s.page_height = Mm(210), Mm(297)
        s.left_margin = s.right_margin = Mm(14)
        s.top_margin, s.bottom_margin = Mm(12), Mm(13); s.footer_distance = Mm(5.5)
        st = self.doc.styles["Normal"]
        st.font.name, st.font.size = BODY, Pt(9.0)
        self._footer(s)

    def _footer(self, s):
        p = s.footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Grupo Bimbo (BIMBO A) - CFA Institute Research Challenge - page ")
        r.font.size, r.font.name = Pt(7.5), BODY
        for t in ("begin", None, "end"):
            run = p.add_run(); run.font.size = Pt(7.5)
            if t:
                f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), t); run._r.append(f)
            else:
                it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = "PAGE"; run._r.append(it)

    # ---- blocks ----
    def title(self, text, first=False, new_page=False):
        p = self.doc.add_paragraph()
        p.paragraph_format.page_break_before = new_page
        fmt(p, after=3, before=0 if first else 8, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=True)
        runs(p, text.upper(), size=12, font=HEAD, color=BLUE)
        pPr = p._p.get_or_add_pPr()
        bd = OxmlElement("w:pBdr"); e = OxmlElement("w:bottom")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "6"); e.set(qn("w:space"), "1"); e.set(qn("w:color"), BLUE)
        bd.append(e); pPr.append(bd)

    def sub(self, text, level):
        p = self.doc.add_paragraph()
        fmt(p, after=2, before=4, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=True)
        runs(p, text, size=10.5 if level == 2 else 10, bold=True, color="000000")

    def para(self, text):
        p = self.doc.add_paragraph()
        fmt(p, after=4)
        runs(p, text)
        return p

    def bullet(self, text):
        p = self.doc.add_paragraph()
        fmt(p, after=2.5)
        p.paragraph_format.left_indent = Mm(4.5)
        p.paragraph_format.first_line_indent = Mm(-4.5)
        r = p.add_run("●\t"); r.font.size, r.font.name = Pt(6.5), "Arial"
        r.font.color.rgb = RGBColor.from_string(BLUE)
        runs(p, text)

    def caption(self, kind, text, size=8):
        if kind == "Chart":
            self.fig_n += 1; n = self.fig_n
        else:
            self.tab_n += 1; n = self.tab_n
        p = self.doc.add_paragraph()
        fmt(p, after=1, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        runs(p, f"{kind} {n}: ", size=size, bold=True)
        runs(p, text, size=size)

    def source(self, text, size=7.5):
        p = self.doc.add_paragraph()
        fmt(p, after=5, align=WD_ALIGN_PARAGRAPH.CENTER)
        runs(p, text, size=size, italic=True)

    def table(self, rows, colw=None):
        n = len(rows[0])
        total = TEXT_W
        t = self.doc.add_table(rows=len(rows), cols=n)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        borders(t); cell_margins(t)
        t.autofit = False
        if colw:
            total = sum(colw)
            first, rest = colw[0], int((total - colw[0]) / (n - 1))
        else:
            first = max(Mm(40), Mm(180 * 0.34)) if n > 4 else Mm(60)
            rest = int((TEXT_W - first) / (n - 1)) if n > 1 else 0
        if rows[0][0].startswith("Risk") or rows[0][0] == "Component":
            widths = None
        for ri, row in enumerate(rows):
            bold_row = row[0].startswith("**")
            for ci, txt in enumerate(row):
                c = t.cell(ri, ci)
                c.width = first if ci == 0 else rest
                p = c.paragraphs[0]
                fmt(p, after=0, align=WD_ALIGN_PARAGRAPH.LEFT if ci == 0 or (len(txt) > 14 and not B.looks_numeric(txt.strip("*"))) else WD_ALIGN_PARAGRAPH.CENTER)
                runs(p, txt, size=7.5, bold=(ri == 0) or None, color=NAVY if ri == 0 else None)
                if ri == 0:
                    shade(c, PALE)
                elif bold_row:
                    shade(c, BAND)
        return t

    def image(self, path: Path, width):
        p = self.doc.add_paragraph()
        fmt(p, after=1, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        p.add_run().add_picture(str(path), width=width)

    def figure(self, blk):
        title, _, src = blk.text.partition(" | ")
        path = (SECTIONS / blk.path).resolve()
        self.caption("Chart", title)
        self.image(path, self._w(path))
        self.source(src)

    def _w(self, path):
        from docx.image.image import Image
        im = Image.from_file(str(path))
        return IMG_FULL_W if im.px_width / im.horz_dpi > 5 else HALF_W

    def pair(self, a, b):
        t = self.doc.add_table(rows=1, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        cell_margins(t, 0, 0, 30, 30)
        for c, blk in zip(t.rows[0].cells, (a, b)):
            c.width = int(TEXT_W / 2)
            title, _, src = blk.text.partition(" | ")
            self.fig_n += 1
            p = c.paragraphs[0]; fmt(p, after=1, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
            runs(p, f"Chart {self.fig_n}: ", size=8, bold=True); runs(p, title, size=8)
            q = c.add_paragraph(); fmt(q, after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
            q.add_run().add_picture(str((SECTIONS / blk.path).resolve()), width=Inches(2.85))
            s = c.add_paragraph(); fmt(s, after=3, align=WD_ALIGN_PARAGRAPH.CENTER)
            runs(s, src, size=7.2, italic=True)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)

    # ---- cover ----
    def cover(self):
        h = self.h
        t = self.doc.add_table(rows=1, cols=2)
        t.autofit = False
        c0, c1 = t.rows[0].cells
        c0.width, c1.width = Mm(60), Mm(120)
        logo = ROOT / "report/assets/bimbo-logo.png"
        if logo.exists():
            c0.paragraphs[0].add_run().add_picture(str(logo), height=Mm(15))
        p = c1.paragraphs[0]; fmt(p, after=0, align=WD_ALIGN_PARAGRAPH.RIGHT)
        runs(p, "Grupo Bimbo", size=24, font=HEAD, color=BLUE)
        q = c1.add_paragraph(); fmt(q, after=0, align=WD_ALIGN_PARAGRAPH.RIGHT)
        runs(q, "Equity research report - CFA Institute Research Challenge 2026-2027", size=8.5, italic=True)
        up = h["target_price"] / h["price"] - 1
        info = [
            [f"**Valuation date:** {h['price_date']}", f"**Recommendation:** {h['recommendation']}", f"**Stock exchange:** {h['exchange']}"],
            [f"**Current price ({h['price_date']}):** {h['currency']} {h['price']:.2f}", f"**12-month target price:** {h['currency']} {h['target_price']:.2f}", f"**Sector:** {h['sector']}"],
            [f"**Ticker:** {h['ticker']}.MX", f"**Upside:** {up*100:.1f}% (total return 11.4%)", f"**Industry:** {h['industry']}"],
        ]
        it = self.doc.add_table(rows=3, cols=3)
        it.autofit = False
        borders(it, color="FFFFFF", sz=2); cell_margins(it, 30, 30, 80, 80)
        for ri, row in enumerate(info):
            for ci, txt in enumerate(row):
                c = it.cell(ri, ci); c.width = Mm(60); shade(c, PALE if ci == 1 else BAND)
                p = c.paragraphs[0]; fmt(p, after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
                runs(p, txt, size=9, font=HEAD, color=RED if "Recommendation" in txt else None)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)
        n = json.load(open(ROOT / "report/data/tp12m_numbers.json"))
        mc = h["price"] * n["shares"] / 1000
        md = [["Market data", "Value"],
              ["Market capitalisation", f"MXN {mc:,.1f} bn"],
              ["Enterprise value (model bridge)", f"MXN {(h['price'] * n['shares'] + n['eq_claims_dec26'])/1000:,.1f} bn"],
              ["Shares outstanding", f"{n['shares']:,.1f} million"],
              ["52-week range", "MXN 53.03 - 68.67"],
              ["Dividend yield (2027E)", f"{n['dividend_2027']/h['price']*100:.1f}%"],
              ["Net debt incl. leases / EBITDA (FY2025A)", f"{n['leverage'][4]:.2f}x"]]
        self.table(md, colw=[Mm(75), Mm(45)])
        self.source("Source: S&P Capital IQ (2026); Grupo Bimbo (2026f); team model.")


def build(project_out: Path, check_only=False):
    header = yaml.safe_load((ROOT / "report/header.yaml").read_text())
    sections = load()
    if check_only:
        un = B.uncited(sections)
        words = sum(B._words(b) for _, b in sections if not B._slug(_).startswith("appendix"))
        print("body words (excl. appendix):", words)
        print("uncited:", len(un))
        for s, t in un:
            print("  ", s, "|", t)
        return
    b = Builder(header, sections)
    b.cover()
    prev_h1 = None
    for path, blocks in sections:
        slug = B._slug(path)
        appendix = slug.startswith("appendix")
        i = 0
        while i < len(blocks):
            blk = blocks[i]
            if blk.kind == "heading":
                if blk.level == 1:
                    b.title(blk.text, new_page=appendix)
                else:
                    b.sub(blk.text, blk.level)
            elif blk.kind == "paragraph":
                if blk.text.startswith("Table:"):
                    b.caption("Table", blk.text[6:].strip())
                elif B.SOURCE_LINE.match(blk.text):
                    b.source(blk.text)
                else:
                    b.para(blk.text)
            elif blk.kind in ("bullet", "number"):
                b.bullet(blk.text)
            elif blk.kind == "table":
                b.table(blk.rows)
            elif blk.kind == "image":
                nxt = blocks[i + 1] if i + 1 < len(blocks) else None
                a_w = b._w((SECTIONS / blk.path).resolve())
                if nxt is not None and nxt.kind == "image" and a_w == HALF_W and b._w((SECTIONS / nxt.path).resolve()) == HALF_W:
                    b.pair(blk, nxt); i += 1
                else:
                    b.figure(blk)
            i += 1
        if slug == "summary":
            p = b.doc.add_paragraph(); fmt(p, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
            runs(p, "Analysts: ", size=9, font=HEAD, bold=True)
            prof = yaml.safe_load((ROOT / "company-profile.yaml").read_text()) if (ROOT / "company-profile.yaml").exists() else {}
            names = [m.get("name") for m in prof.get("team", [])] if isinstance(prof.get("team"), list) else []
            runs(p, ", ".join(n for n in names if n) or "Luis Arturo Romo Alba, Diego Benavides Pro, Alexa Garcia Saldivar, Jorge Alejandro Gaytan, Carolina del Rosario Benites", size=9, font=HEAD)
    project_out.parent.mkdir(parents=True, exist_ok=True)
    b.doc.save(project_out)
    print("wrote", project_out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "report/BIMBOA_report_v2.docx"))
    a = ap.parse_args()
    build(Path(a.out), a.check)
