"""Build the CFA Research Challenge report on Grupo Bimbo as a PDF in the layout of last year's La Comer report.

Layout: placeholder cover page; body of up to 10 A4 pages in two columns (text on the left, figures on the right), a grey
header band on page 1; appendix in one column. Text comes from report/sections/*.md, numbers from report_data.py,
charts from report/charts/en/*.png (report_charts.py), tables from report_tables.py.

Usage: python report_charts.py && python build_report_pdf.py [output.pdf]
"""

from __future__ import annotations

import html as htmllib
import io
import re
import sys
from pathlib import Path

import pymupdf
from PIL import Image

import i18n
import report_data as D
import report_tables as T
from report_style import (AMBER, ASSETS, BLUE, CHARTS, FULL_W, GRAY, INK, LC_W, LC_X0, MARGIN_B, MARGIN_L, MARGIN_R, MARGIN_T,
                          NAVY, PAGE_H, PAGE_W, RC_W, RC_X0, RED, REPORT, ROOT, SECTIONS)

OUT_DEFAULT = (ROOT / "output" / "BIMBOA_reporte_v1_borrador_ES.pdf") if i18n.ES_ON else (REPORT / "BIMBOA_report_v1_draft.pdf")
BODY_ORDER = ["00-executive-summary", "02-business-description", "03-industry", "01-investment-summary", "05-valuation",
              "04-financial-analysis", "06-risks", "07-esg"]
APPX_FILES = ["98-appendix", "99-appendix-ai-use"]
TXT = {
    "en": dict(
        foot="Grupo Bimbo, S.A.B. de C.V. (BMV: BIMBO A)  |  CFA Institute Research Challenge  |  Draft v1, 19 October 2026  |  HOLD (provisional)",
        fig="Figure", page="Page", appendix="Appendix",
        c1="INSERT THE OFFICIAL<br/>CFA INSTITUTE RESEARCH CHALLENGE<br/>COVER PAGE HERE",
        c2=("The official cover carries the required disclosures. It is downloaded from the Research Challenge student page, goes in front "
            "unaltered except its highlighted fields, and does not count towards the 10-page limit."),
        c3="Equity research report, draft v1 for team review, 19 October 2026<br/>Rating: HOLD (provisional). Target price: to be set by the team.",
        sector="Consumer Staples, Packaged Food &amp; Bakery", rec_pre="", rec_post=" Recommendation ", prov="(provisional)",
        target="Target Price:", tbd=" TBD ", tbd_note="(team to set)", price="Price:", title="Grupo Bimbo (BMV: BIMBO A) - CFA Institute Research Challenge - draft v1"),
    "es": dict(
        foot="Grupo Bimbo (BMV: BIMBO A)  |  CFA Institute Research Challenge  |  Borrador v1, 19-oct-2026  |  HOLD (provisional)  |  Traducción; la oficial es la inglesa",
        fig="Figura", page="Página", appendix="Anexo",
        c1="INSERTE AQUÍ LA PORTADA OFICIAL<br/>DEL CFA INSTITUTE RESEARCH CHALLENGE",
        c2=("La portada oficial lleva las divulgaciones requeridas. Se descarga de la página del Research Challenge para estudiantes, va al frente "
            "sin alteraciones salvo sus campos resaltados y no cuenta para el límite de 10 páginas. Esta es una traducción al español para uso "
            "interno del equipo; la versión oficial que se entrega es la inglesa."),
        c3=("Reporte de análisis de renta variable, borrador v1 para revisión del equipo, 19 de octubre de 2026<br/>"
            "Recomendación: HOLD (provisional). Precio objetivo: lo define el equipo."),
        sector="Consumo básico, alimentos y panificación", rec_pre="Recomendación: ", rec_post=" ", prov="(provisional)",
        target="Precio objetivo:", tbd=" Por definir ", tbd_note="(lo define el equipo)", price="Precio:", title="Grupo Bimbo (BMV: BIMBO A) - CFA Institute Research Challenge - borrador v1 (español)"),
}["es" if i18n.ES_ON else "en"]
FOOT = TXT["foot"]
ARCH = pymupdf.Archive("C:/Windows/Fonts")
TOP0, TOP, BOT = 80.0, MARGIN_T, PAGE_H - MARGIN_B
GAP_FIG = 11.0

FIGS = {
    "football": ("fig_football", "Value per share by method vs. price", "Source: Team model; S&amp;P Capital IQ (2026)."),
    "ev_bridge": ("fig_ev_bridge", "DCF: from enterprise value to equity value", "Source: Team model. Equity value / 4,294.9m shares = MXN 44.76 at 30-Jun; x 1.0369 roll to 16-Oct = MXN 46.42."),
    "roic_wacc": ("fig_roic_wacc", "Returns on capital vs. cost of capital", "Source: Grupo Bimbo (2026f); team model."),
    "sales_region": ("fig_sales_region", "FY2025 net sales by region", "Source: Grupo Bimbo (2026b, p. 4)."),
    "sales_vs_ebitda": ("fig_sales_vs_ebitda", "Share of net sales vs. Adj. EBITDA, FY2025", "Source: Grupo Bimbo (2026b, p. 4; 2026e, p. 17)."),
    "ownership": ("fig_ownership", "Shareholder structure", "Source: Grupo Bimbo (2026a, pp. 181-182)."),
    "market_growth": ("fig_market_growth", "Bakery market value growth", "Source: Global Data, in Grupo Bimbo (2026a, pp. 107-111)."),
    "market_type": ("fig_market_type", "Global bakery market by type, 2024", "Source: Global Data, in Grupo Bimbo (2026a, p. 107); team model."),
    "peers": ("fig_peers", "EV/EBITDA, Bimbo and peers", "Source: S&amp;P Capital IQ (2026); team model."),
    "five_forces": ("fig_five_forces", "Porter's five forces (team estimate)", "Source: Team estimate; 1 = weak force, 5 = strong."),
    "thesis_map": ("fig_thesis_map", "What each thesis is worth", "Source: Team model (DCF)."),
    "na_margin": ("fig_na_margin", "North America: margin and sales growth", "Source: Grupo Bimbo (2026b, 2026c, 2026d); quarterly releases."),
    "capex_cfo": ("fig_capex_cfo", "Cash flow from operations and capex", "Source: Grupo Bimbo (2026f, pp. 85-86)."),
    "cost_lines": ("fig_cost_lines", "Cost of sales by nature: growth in FY2025", "Source: Grupo Bimbo (2026f, p. 82); team model."),
    "growth_gap": ("fig_growth_gap", "Net sales growth ex-FX: history vs. model", "Source: Grupo Bimbo (2026a, 2026c, 2026d); team estimate. *1H26 is the simple average of the 1Q26 and 2Q26 rates; model bars are annual rates."),
    "multiple_curve": ("fig_multiple_curve", "Exit multiple and 12-month expected return", "Source: Team model."),
    "tornado": ("fig_tornado", "Value per share: sensitivity to drivers", "Source: Team model."),
    "rev_margin": ("fig_rev_margin", "Net sales and Adj. EBITDA margin", "Source: Grupo Bimbo (2026f); team model."),
    "leverage": ("fig_leverage", "Net debt / EBITDA including leases", "Source: Grupo Bimbo (2026f, 2026d, p. 6); S&amp;P Capital IQ (2026); team model."),
    "risk_matrix": ("fig_risk_matrix", "Risk matrix", "Source: Team estimate (see Appendix A8)."),
    "esg_sp": ("fig_esg_sp", "S&amp;P Global ESG score, 2013-2026", "Source: S&amp;P Capital IQ (2026)."),
    "esg_lseg": ("fig_esg_lseg", "LSEG ESG score vs. food peers", "Source: LSEG (2026)."),
    "emissions": ("fig_emissions", "Greenhouse gas emissions and 2030 targets", "Source: LSEG (2026); Grupo Bimbo (2026e, p. 169)."),
    "governance": ("fig_governance", "Governance scorecard", "Source: Team estimate (31 of 64 points)."),
}

CSS = f"""
@font-face {{ font-family: ArialW; src: url(arial.ttf); }}
@font-face {{ font-family: ArialW; src: url(arialbd.ttf); font-weight: bold; }}
@font-face {{ font-family: ArialW; src: url(ariali.ttf); font-style: italic; }}
@font-face {{ font-family: ArialW; src: url(arialbi.ttf); font-weight: bold; font-style: italic; }}
body {{ font-family: ArialW; font-size: 8.7pt; line-height: 1.22; color: {INK}; }}
p {{ margin: 0 0 3.4pt 0; text-align: justify; }}
h1 {{ font-size: 17pt; color: {BLUE}; margin: 8pt 0 5pt 0; padding: 0 0 2pt 4pt; border-bottom: 1.1pt solid {INK}; }}
h1.first {{ margin-top: 0pt; }}
h2 {{ font-size: 9.6pt; color: {BLUE}; margin: 4.5pt 0 2pt 0; }}
h3 {{ font-size: 9.3pt; color: {BLUE}; margin: 6pt 0 2.4pt 0; line-height: 1.18; }}
p.li {{ margin: 0 0 2.4pt 0; padding-left: 9pt; text-indent: -9pt; }}
div.note {{ border-left: 2.8pt solid {AMBER}; padding: 1pt 0 1pt 6pt; margin: 1pt 0 5pt 0; }}
.pb {{ page-break-before: always; }}
div.note p {{ margin: 0; }}
p.ft {{ font-size: 8.6pt; font-weight: bold; text-align: center; margin: 0 0 2pt 0; line-height: 1.15; color: {INK}; }}
p.fs {{ font-size: 7.3pt; font-style: italic; text-align: left; margin: 1pt 0 0 2pt; color: #333333; line-height: 1.12; }}
"""

CSS_APPX = CSS.replace("font-size: 8.7pt; line-height: 1.22", "font-size: 8.3pt; line-height: 1.2") + f"""
h2 {{ font-size: 9.6pt; text-align: center; color: {BLUE}; margin: 7pt 0 3pt 0; }}
"""


# ============================================================================================ markdown to HTML
def read(name: str) -> str:
    return (SECTIONS / f"{name}.md").read_text(encoding="utf-8")


def fig_numbers() -> dict:
    nums, n = {}, 0
    for name in BODY_ORDER:
        for m in re.finditer(r"^\[\[figs:\s*(.+?)\]\]\s*$", read(name), flags=re.M):
            for key in [k.strip() for k in m.group(1).split(",")]:
                n += 1
                nums[key] = n
    return nums


NUMS = fig_numbers()


def inline(text: str) -> str:
    t = htmllib.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\{fig:([a-z_]+)\}", lambda m: f"{TXT['fig']} {NUMS[m.group(1)]}", t)
    t = re.sub(r"(?<![\w.)\-])-(?=\d|MXN|US\$)", "\u2212", t)
    return t


def md_to_html(md: str, *, first: bool = False, appendix: bool = False, appendix_part: int = 0, prefix: str = "x", breaks=frozenset()):
    out, figs, boxes = [], [], []
    para: list[str] = []
    counter = [0]
    pending: list = []          # a heading waiting for its next element (so a heading never strands above a moved table)

    def uid(kind: str) -> str:
        counter[0] += 1
        return f"{kind}{prefix}_{counter[0]}"

    def cls(i: str, extra: str = "") -> str:
        c = (extra + " " + ("pb" if i in breaks else "")).strip()
        return f' class="{c}"' if c else ""

    kinds: list = []            # parallel to out: "h" heading, "p" paragraph, "x" anything else

    def add(kind: str, html: str):
        out.append(html)
        kinds.append(kind)

    def release():
        if pending:
            hid, tag, text = pending.pop()
            add("h", f'<{tag} id="{hid}"{cls(hid)}>{text}</{tag}>')

    def flush():
        if para:
            release()
            text = " ".join(para)
            if text.startswith(("**PROVISIONAL", "**Theses validated", "**Tesis validadas")):
                add("x", f'<div class="note"><p>{inline(text)}</p></div>')
            else:
                add("p", f"<p>{inline(text)}</p>")
            para.clear()

    seen_h1 = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        m = re.match(r"^\[\[(figs|box|table):\s*(.+?)\]\]$", line.strip())
        if m:
            flush()
            kind, arg = m.group(1), m.group(2)
            if kind == "figs":
                figs += [k.strip() for k in arg.split(",")]
            elif kind == "box":
                boxes.append(arg.strip())
            else:
                tid = uid("t")
                head_html = ""
                if pending:
                    _, tag, text = pending.pop()
                    head_html = f"<{tag}>{text}</{tag}>"
                elif len(kinds) >= 2 and kinds[-1] == "p" and kinds[-2] == "h":       # heading + intro paragraph + table
                    intro = out.pop()
                    kinds.pop()
                    heading = out.pop()
                    kinds.pop()
                    head_html = re.sub(r'^<(h[23]) id="[^"]*"( class="[^"]*")?>', r"<\1>", heading) + intro
                tbl_html = T.REGISTRY[arg.strip()]()
                k_ = tbl_html.rfind('<p style="margin:1.5pt')                 # the source note: give it an id so a note stranded on the next page is detected
                if k_ >= 0:
                    tbl_html = tbl_html[:k_] + f'<p id="n{tid}" style="margin:1.5pt' + tbl_html[k_ + len('<p style="margin:1.5pt'):]
                add("x", f'<div id="{tid}"{cls(tid)}>{head_html}{tbl_html}</div>')
            continue
        if line.strip() == "[[refs]]":
            flush()
            release()
            add("x", f"<div>{T.refs()}</div>")
            continue
        if line.startswith("# "):
            flush()
            release()
            title = line[2:].strip()
            if appendix:
                if appendix_part > 0:
                    pending.append((uid("h"), "h2", f"A12. {inline(title)}"))
                seen_h1 = True
                continue
            sid = "sec-" + re.sub("[^a-z]", "", title.lower())
            add("x", f'<h1 id="{sid}"{cls(sid, "first" if (first and not seen_h1) else "")}>{inline(title)}</h1>')
            seen_h1 = True
        elif line.startswith("### "):
            flush()
            release()
            pending.append((uid("h"), "h3", inline(line[4:])))
        elif line.startswith("## "):
            flush()
            release()
            pending.append((uid("h"), "h2", inline(line[3:])))
        elif line.startswith("- "):
            flush()
            release()
            add("x", f'<p class="li">• {inline(line[2:])}</p>')
        elif line.startswith("> "):
            flush()
            release()
            add("x", f'<div class="note"><p>{inline(line[2:])}</p></div>')
        else:
            para.append(line.strip())
    flush()
    release()
    return "".join(out), figs, boxes


# ============================================================================================ layout helpers
def measure(html: str, width: float, css: str = CSS) -> float:
    st = pymupdf.Story(html=html, user_css=css, archive=ARCH)
    _, filled = st.place(pymupdf.Rect(0, 0, width, 4000))
    return filled[3] - filled[1]


def put_text(page, rect, text, font, size, align, color):
    """insert_textbox with built-in Helvetica; grows the box a little if the text does not fit (it draws nothing otherwise)."""
    for grow in range(0, 40, 4):
        r = pymupdf.Rect(rect.x0, rect.y0, rect.x1, rect.y1 + grow)
        if page.insert_textbox(r, text, fontname=font, fontsize=size, align=align, color=color) >= 0:
            return
    print("WARNING: text did not fit:", text[:60])


class Item:
    def __init__(self, kind: str, key: str):
        self.kind, self.key = kind, key
        if kind == "fig":
            fname, title, source = FIGS[key]
            self.num = NUMS[key]
            self.title_txt = i18n.tr(htmllib.unescape(title))
            self.src_txt = i18n.tr(htmllib.unescape(source))
            self.title_html = f'<p class="ft">{TXT["fig"]} {self.num}: {htmllib.escape(self.title_txt, quote=False)}</p>'
            self.src_html = f'<p class="fs">{htmllib.escape(self.src_txt, quote=False)}</p>'
            self.path = CHARTS / f"{fname}.png"
            with Image.open(self.path) as im:
                self.img_h = RC_W * im.height / im.width
            self.th = measure(self.title_html, RC_W) + 1.5
            self.sh = measure(self.src_html, RC_W) + 1.0
            self.h = self.th + self.img_h + self.sh + GAP_FIG
        else:
            self.html = T.REGISTRY[key]()
            self.h = measure(self.html, RC_W) + 8.0 + GAP_FIG

    def draw(self, page: pymupdf.Page, y: float):
        x0 = RC_X0
        if self.kind == "fig":
            put_text(page, pymupdf.Rect(x0, y, x0 + RC_W, y + self.th + 3), f"{TXT['fig']} {self.num}: {self.title_txt}", "hebo", 8.6,
                     pymupdf.TEXT_ALIGN_CENTER, (0.10, 0.10, 0.10))
            page.insert_image(pymupdf.Rect(x0, y + self.th, x0 + RC_W, y + self.th + self.img_h), filename=str(self.path))
            yy = y + self.th + self.img_h
            put_text(page, pymupdf.Rect(x0 + 2, yy + 1, x0 + RC_W, yy + self.sh + 3), self.src_txt, "heit", 7.3,
                     pymupdf.TEXT_ALIGN_LEFT, (0.2, 0.2, 0.2))
        else:
            page.insert_htmlbox(pymupdf.Rect(x0, y, x0 + RC_W, y + self.h - GAP_FIG + 2), self.html, css=CSS, archive=ARCH)


def run_story(html: str, css: str, rect_for_page, n_max: int = 40):
    """Flow html over pages; returns (pdf bytes, element positions, filled rects)."""
    story = pymupdf.Story(html=html, user_css=css, archive=ARCH)
    buf = io.BytesIO()
    writer = pymupdf.DocumentWriter(buf)
    media = pymupdf.paper_rect("a4")
    recs, filled_rects = [], []
    more, pg = True, 0

    def make(p):
        def cb(pos):
            recs.append({"page": p, "id": pos.id, "open_close": pos.open_close, "y0": pos.rect[1], "y1": pos.rect[3],
                         "heading": pos.heading, "text": pos.text})
        return cb

    while more and pg < n_max:
        dev = writer.begin_page(media)
        more, filled = story.place(rect_for_page(pg))
        story.element_positions(make(pg))
        story.draw(dev)
        writer.end_page()
        filled_rects.append(filled)
        pg += 1
    writer.close()
    return buf.getvalue(), recs, filled_rects


def find_break(recs, existing, top_first: float, top_rest: float = TOP, bot: float = BOT):
    """Topmost element that must start a new page: a table split across pages, or a heading stranded near the page bottom.

    Only the topmost one is returned: adding a break changes the layout below it, so later problems are re-measured."""
    by_id: dict = {}
    for r in recs:
        if r["id"]:
            by_id.setdefault(r["id"], {})[r["open_close"] & 3] = r
    cand = []
    for id_, d in by_id.items():
        if id_ in existing:
            continue
        o, c = d.get(1), d.get(2)
        if not o or not c:
            continue
        if o["y0"] < (top_first if o["page"] == 0 else top_rest) + 12:
            continue
        bad = False
        if id_.startswith("t"):
            note = by_id.get("n" + id_, {}).get(1)
            bad = o["page"] != c["page"] or c["y1"] > bot + 0.5 or (note is not None and note["page"] != o["page"])
        elif id_.startswith(("h", "sec-")):
            bad = c["page"] != o["page"] or c["y1"] > bot - 26
        if bad:
            cand.append((o["page"], o["y0"], id_))
    return min(cand)[2] if cand else None


def flow(files, css, rect, *, appendix=False, n_max=40, top_first=TOP0, top_rest=TOP):
    """Run the story with a keep-together fixer: tables that split and headings stranded at a page bottom move to the next page."""
    breaks: set = set()
    for _ in range(120):
        htmls, metas = [], []
        for i, name in enumerate(files):
            h, figs, boxes = md_to_html(read(name), first=(i == 0 and not appendix), appendix=appendix, appendix_part=i,
                                        prefix=f"{'a' if appendix else 'b'}{i}", breaks=breaks)
            htmls.append(h)
            metas.append((name, figs, boxes))
        data, recs, filled = run_story("".join(htmls), css, rect, n_max=n_max)
        nxt = find_break(recs, breaks, top_first, top_rest)
        if nxt is None:
            return data, recs, filled, metas, breaks
        breaks.add(nxt)
    return data, recs, filled, metas, breaks


# ============================================================================================ build
def build_body():
    def rect(pg: int):
        return pymupdf.Rect(LC_X0, TOP0 if pg == 0 else TOP, LC_X0 + LC_W, BOT)

    data, recs, filled, metas, breaks = flow(BODY_ORDER, CSS, rect)
    sec_figs = {n: f for n, f, _ in metas}
    sec_boxes = {n: b for n, _, b in metas}
    doc = pymupdf.open("pdf", data)

    # section spans from the h1 ids
    starts = [(r["id"], r["page"], r["y0"]) for r in recs if r["id"] and r["id"].startswith("sec-") and r["open_close"] & 1]
    spans = []
    for k, (sid, pg, y0) in enumerate(starts):
        if k + 1 < len(starts):
            spans.append((sid, pg, y0, starts[k + 1][1], starts[k + 1][2]))
        else:
            spans.append((sid, pg, y0, doc.page_count - 1, filled[-1][3]))
    assert len(spans) == len(BODY_ORDER), (len(spans), len(BODY_ORDER))

    # right column: global pointer
    ptr_page, ptr_y = 0, TOP0
    warnings = []
    placed = []
    for name, (sid, sp, sy, ep, ey) in zip(BODY_ORDER, spans):
        items = [Item("box", k) for k in sec_boxes[name]] + [Item("fig", k) for k in sec_figs[name]]
        if (sp, sy) > (ptr_page, ptr_y):
            ptr_page, ptr_y = sp, max(sy - 1.0, TOP if sp else TOP0)
        for it in items:
            while ptr_y + it.h - GAP_FIG > BOT:
                ptr_page += 1
                ptr_y = TOP
            if ptr_page >= doc.page_count:
                warnings.append(f"{it.kind} {it.key} would need page {ptr_page + 1} (body has {doc.page_count} pages)")
                break
            if ptr_page > ep:
                warnings.append(f"{it.kind} {it.key} of {name} lands on page {ptr_page + 1}, after its section ends on page {ep + 1}")
            placed.append((it, ptr_page, ptr_y))
            it.draw(doc[ptr_page], ptr_y)
            ptr_y += it.h
    return doc, spans, warnings, placed


def build_appendix():
    rect = lambda pg: pymupdf.Rect(MARGIN_L, 60, PAGE_W - MARGIN_R, BOT)
    data, recs, filled, metas, breaks = flow(APPX_FILES, CSS_APPX, rect, appendix=True, n_max=14, top_first=60, top_rest=60)
    return pymupdf.open("pdf", data)


def cover() -> pymupdf.Document:
    doc = pymupdf.open()
    p = doc.new_page(width=PAGE_W, height=PAGE_H)
    r = pymupdf.Rect(70, 190, PAGE_W - 70, 470)
    p.draw_rect(r, color=(0.55, 0.55, 0.55), width=1.2, dashes="[4 3] 0")
    p.insert_htmlbox(pymupdf.Rect(90, 250, PAGE_W - 90, 420), (
        f'<p style="text-align:center;font-size:17pt;font-weight:bold;color:#555555">{TXT["c1"]}</p>'
        f'<p style="text-align:center;font-size:9pt;color:#555555;margin-top:10pt">{TXT["c2"]}</p>'), css=CSS, archive=ARCH)
    p.insert_htmlbox(pymupdf.Rect(70, 500, PAGE_W - 70, 600), (
        f'<p style="text-align:center;font-size:11pt;font-weight:bold;color:{NAVY}">Grupo Bimbo, S.A.B. de C.V. (BMV: BIMBO A)</p>'
        f'<p style="text-align:center;font-size:9pt;color:#555555">{TXT["c3"]}</p>'), css=CSS, archive=ARCH)
    return doc


def header_band(page: pymupdf.Page):
    page.draw_rect(pymupdf.Rect(0, 0, PAGE_W, 68), color=None, fill=(0.949, 0.949, 0.949))
    logo = ASSETS / "bimbo-logo.png"
    with Image.open(logo) as im:
        lw = 78.0
        lh = lw * im.height / im.width
    page.insert_image(pymupdf.Rect(MARGIN_L, 34 - lh / 2, MARGIN_L + lw, 34 + lh / 2), filename=str(logo))
    page.insert_htmlbox(pymupdf.Rect(124, 8, 400, 62), (
        f'<p style="margin:0;font-size:11pt;font-weight:bold;color:{INK};line-height:1.45;text-align:left">Grupo Bimbo, S.A.B. de C.V.</p>'
        f'<p style="margin:0;font-size:10.5pt;font-weight:bold;line-height:1.45;text-align:left"><span style="color:{BLUE}">BMV:</span> BIMBO A</p>'
        f'<p style="margin:0;font-size:10.5pt;font-weight:bold;line-height:1.45;text-align:left"><span style="color:{BLUE}">Sector:</span> {TXT["sector"]}</p>'),
        css=CSS, archive=ARCH)
    page.insert_htmlbox(pymupdf.Rect(360, 8, PAGE_W - MARGIN_R, 62), (
        f'<p style="margin:0;font-size:11pt;font-weight:bold;text-align:right;line-height:1.45">{TXT["rec_pre"]}<span style="color:{RED}">HOLD</span>{TXT["rec_post"]}'
        f'<span style="font-size:8pt;font-weight:normal">{TXT["prov"]}</span></p>'
        f'<p style="margin:0;font-size:10.5pt;font-weight:bold;text-align:right;line-height:1.45"><span style="color:{BLUE}">{TXT["target"]}</span> '
        f'<span style="background-color:{AMBER}">{TXT["tbd"]}</span> <span style="font-size:7.5pt;font-weight:normal">{TXT["tbd_note"]}</span></p>'
        f'<p style="margin:0;font-size:9pt;font-weight:bold;text-align:right;line-height:1.5">{TXT["price"]} MXN {D.PRICE:.2f} ({i18n.tr(D.PRICE_DATE)})</p>'),
        css=CSS, archive=ARCH)


def footers(doc: pymupdf.Document, first_numbered: int, label_offset: int):
    for i in range(first_numbered, doc.page_count):
        page = doc[i]
        size = 6.6
        while pymupdf.get_text_length(FOOT, fontname="helv", fontsize=size) > FULL_W - 62 and size > 5.0:
            size -= 0.1
        page.insert_text((MARGIN_L, PAGE_H - 20), FOOT, fontname="helv", fontsize=size, color=(0.42, 0.42, 0.42))
        label = f"{TXT['page']} {i - first_numbered + 1 + label_offset}"
        w = pymupdf.get_text_length(label, fontname="helv", fontsize=7.2)
        page.insert_text((PAGE_W - MARGIN_R - w, PAGE_H - 20), label, fontname="helv", fontsize=7.2, color=(0.3, 0.3, 0.3))


def appendix_headers(doc: pymupdf.Document, first: int):
    for i in range(first, doc.page_count):
        page = doc[i]
        page.insert_text((MARGIN_L + 4, 46), TXT["appendix"], fontname="hebo", fontsize=17, color=(0.1, 0.1, 0.1))
        page.draw_line((MARGIN_L, 52), (PAGE_W - MARGIN_R, 52), color=(0.1, 0.1, 0.1), width=1.1)


def fix_tounicode(doc: pymupdf.Document) -> int:
    """MuPDF writes ToUnicode maps where the space glyph is U+00A0, the hyphen U+00AD and the semicolon U+037E, which breaks
    copy/paste and search. Point those glyphs back to the plain ASCII characters."""
    fixed, seen = 0, set()
    for page in doc:
        for f in page.get_fonts(full=True):
            xref = f[0]
            if xref in seen:
                continue
            seen.add(xref)
            key = doc.xref_get_key(xref, "ToUnicode")
            if key[0] != "xref":
                continue
            tx = int(key[1].split()[0])
            raw = doc.xref_stream(tx).decode("latin-1")
            new = re.sub(r"(?m)^(<[0-9a-fA-F]{4}>[ \t]+)<00[aA]0>[ \t]*$", r"\g<1><0020>", raw)
            new = re.sub(r"(?m)^(<[0-9a-fA-F]{4}>[ \t]+)<00[aA][dD]>[ \t]*$", r"\g<1><002D>", new)
            new = re.sub(r"(?m)^(<[0-9a-fA-F]{4}>[ \t]+)<037[eE]>[ \t]*$", r"\g<1><003B>", new)
            if new != raw:
                doc.update_stream(tx, new.encode("latin-1"))
                fixed += 1
    return fixed


def main(out: Path) -> int:
    body, spans, warnings, placed = build_body()
    appx = build_appendix()
    final = cover()
    final.insert_pdf(body)
    n_body = body.page_count
    final.insert_pdf(appx)
    header_band(final[1])
    appendix_headers(final, 1 + n_body)
    footers(final, 1, 0)
    final.set_metadata({"title": TXT["title"], "author": "Research team (draft)"})
    out.parent.mkdir(parents=True, exist_ok=True)
    print("ToUnicode maps fixed:", fix_tounicode(final))
    final.save(str(out), garbage=4, deflate=True)
    print(f"cover 1 + body {n_body} + appendix {appx.page_count} pages -> {out}")
    if n_body > 10:
        print(f"WARNING: body has {n_body} pages; the limit is 10")
    if appx.page_count > 10:
        print(f"WARNING: appendix has {appx.page_count} pages; the limit is 10")
    for sid, sp, sy, ep, ey in spans:
        print(f"  {sid:24s} page {sp + 1} y{sy:5.0f}  ->  page {ep + 1} y{ey:5.0f}")
    for it, pg, y in placed:
        print(f"  right col: {it.kind:3s} {it.key:16s} page {pg + 1} y{y:5.0f} h{it.h:5.0f}")
    for w in warnings:
        print("WARNING:", w)
    if i18n.ES_ON and i18n.MISSING:
        print("UNTRANSLATED (" + str(len(i18n.MISSING)) + "):")
        for m in sorted(i18n.MISSING):
            print("   ", repr(m))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else OUT_DEFAULT))
