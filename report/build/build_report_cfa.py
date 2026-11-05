"""Build the report body (Word) in the layout of the CFA La Comer report ("CFA LACOMER.pdf"), with Bimbo's palette.

Layout of the template: grey header band on the first page (logo, company, ticker, sector; recommendation, target price,
price); sections Executive Summary, Business Overview, Industry Overview, Investment Summary, Valuation, Financial Analysis,
Risks, ESG and Appendix; in each section the text runs in a left column and the figures in a right column, each with a bold
"Figure n: title" above and an italic "Source: ..." below; the Financial Analysis opens with a wide ratio table.

The content comes from report/sections/*.md (same files as the Times New Roman build); this script reorders and lays them out.
Run:  .venv/bin/python report/build/build_report_cfa.py [--check] [--out report/BIMBOA_report_v9.docx]
The official CFA Institute cover page is put in front by the team.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import yaml
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Mm, Pt, RGBColor

SKILL_TOOLS = Path.home() / ".claude/skills/CFA-report/tools"
sys.path.insert(0, str(SKILL_TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_docx as B  # noqa: E402
from build_report_docx import preprocess  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CFG = {"lang": "en"}


def sd() -> Path:
    return ROOT / ("report/sections_es" if CFG["lang"] == "es" else "report/sections")


def td() -> Path:
    return ROOT / ("report/tables_es" if CFG["lang"] == "es" else "report/tables")


STR = {
    "en": {
        "Executive Summary": "Executive Summary", "Business Overview": "Business Overview", "Industry Overview": "Industry Overview",
        "Investment Summary": "Investment Summary", "Valuation": "Valuation", "Financial Analysis": "Financial Analysis",
        "Risks": "Risks", "ESG": "ESG", "Appendix": "Appendix",
        "mgmt_h": "Management and governance", "relval_h": "Relative valuation", "forecast_h": "Forecast and drivers",
        "lead": "Leadership and track record", "gov": "Corporate governance and evaluation", "said": "What management said against the data",
        "football_start": "Football field", "a7": "A7. Management statements of the 3Q26 call against the data",
        "a5c": "A5c. Football field", "a5d": "A5d. ESG score against peers", "refs_old": "A7. References", "refs_new": "A8. References",
        "fig": "Figure", "tab": "Table", "source": "Source", "analysts": "Analysts: ",
        "football_cap": "Football field: value per share against the price and rating zones | Source: team model; S&P Capital IQ (2026)",
        "rec": "{} Recommendation", "target": "Target price (12M): ", "target_val": "MXN {:.2f} ({:.1f}% upside)", "target_val_dn": "MXN {:.2f} ({:.1f}% below the price)", "price": "Price ({}): ",
        "bmv": "BMV: ", "sector": "Sector: ", "footer": "Grupo Bimbo (BIMBO A) - CFA Institute Research Challenge - page ",
    },
    "es": {
        "Executive Summary": "Resumen ejecutivo", "Business Overview": "Descripción del negocio", "Industry Overview": "Panorama de la industria",
        "Investment Summary": "Resumen de inversión", "Valuation": "Valuación", "Financial Analysis": "Análisis financiero",
        "Risks": "Riesgos", "ESG": "ESG", "Appendix": "Apéndice",
        "mgmt_h": "Administración y gobierno corporativo", "relval_h": "Valuación relativa", "forecast_h": "Proyección y supuestos",
        "lead": "Liderazgo y trayectoria", "gov": "Gobierno corporativo y evaluación", "said": "Qué dijo la administración frente a los datos",
        "football_start": "Campo de fútbol", "a7": "A7. Afirmaciones de la administración en la llamada del 3T26 frente a los datos",
        "a5c": "A5c. Campo de fútbol", "a5d": "A5d. Calificación ASG frente a pares", "refs_old": "A7. Referencias", "refs_new": "A8. Referencias",
        "fig": "Figura", "tab": "Tabla", "source": "Fuente", "analysts": "Analistas: ",
        "football_cap": "Campo de fútbol: valor por acción frente al precio y las zonas de calificación | Source: modelo del equipo; S&P Capital IQ (2026)",
        "rec": "Recomendación: {} (HOLD)", "target": "Precio objetivo (12M): ", "target_val": "MXN {:.2f} (potencial de {:.1f}%)", "target_val_dn": "MXN {:.2f} ({:.1f}% por debajo del precio)", "price": "Precio ({}): ",
        "bmv": "BMV: ", "sector": "Sector: ", "footer": "Grupo Bimbo (BIMBO A) - CFA Institute Research Challenge - página ",
    },
}


def S(key):
    return STR[CFG["lang"]][key]
BLUE, NAVY, RED = "0033A0", "001268", "EC1C2D"
PALE, BAND = "C9D6F2", "F2F2F2"
FONT = "Arial"
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")
import os as _os
MARGIN = float(_os.environ.get("MARGIN", "9"))
PAGE_W, LEFT_W, RIGHT_W = Mm(210 - 2 * MARGIN), Mm(210 - 2 * MARGIN - 67), Mm(63)
import os as _os
FIG_W = Inches(float(_os.environ.get("FIG_W", "2.00")))
BODY_PT = float(_os.environ.get("BODY_PT", "8.3"))

FIGS = {
    "price_tp": ("Share price and 12-month target", "S&P Capital IQ (2026); Yahoo Finance (2026) for 27-Oct-26; team model"),
    "dcf_bridge": ("Build-up of the base DCF, MXN per share", "Team model (sheets Valuacion and WACC)"),
    "rev_margin": ("Net sales and adjusted EBITDA margin, FY2021A-FY2030E", "Grupo Bimbo (2026f); team model"),
    "fig_sales_region": ("FY2025 net sales by region", "Grupo Bimbo (2026b, p. 4)"),
    "fig_sales_vs_ebitda": ("Share of sales and of adjusted EBITDA, FY2025", "Grupo Bimbo (2026b, p. 4; 2026e, p. 17)"),
    "acq_leverage": ("Acquisitions paid and net debt including leases over EBITDA", "Grupo Bimbo (2026f); team model"),
    "regional_margin": ("Adjusted EBITDA margin by region, FY2021-FY2025", "Grupo Bimbo (2026f, p. 85); team model"),
    "wheat_costs": ("Wheat price against the 2026E average held in the model", "IMF (2026); team model"),
    "growth_organic": ("Net sales growth by region, 9M26, reported and excluding acquisitions",
                       "Grupo Bimbo (2026c, 2026d, 2026h); team model. North America includes Stone House"),
    "margins": ("Gross margin and adjusted EBITDA margin, FY2021A-FY2030E", "Grupo Bimbo (2026f); team model"),
    "ebitda_bridge": ("Adjusted EBITDA margin, FY2025A to FY2027E, by line", "Grupo Bimbo (2026f); team model"),
    "leverage": ("Net debt including leases over adjusted EBITDA", "Grupo Bimbo (2026f); team model"),
    "fcff": ("Free cash flow to the firm, FY2027E-FY2030E", "team model"),
    "usdmxn": ("USD/MXN annual average, 2019-2030E, and the 16 October 2026 spot", "S&P Capital IQ (2026); team model"),
    "fig_market_type": ("Global bakery market by type, 2024", "Global Data, in Grupo Bimbo (2026a, p. 107)"),
    "fig_cost_lines": ("Growth of cost-of-sales lines against net sales, FY2025", "Grupo Bimbo (2026f, p. 82); team model"),
    "fig_capex_cfo": ("Cash flow from operations and capex, FY2021-FY2025", "Grupo Bimbo (2026f, p. 86)"),
    "fig_ownership": ("Shareholder structure", "Grupo Bimbo (2026a, pp. 181-182); LSEG (2026)"),
    "fig_governance": ("Governance checklist: score by block", "team estimate from Grupo Bimbo (2026a, pp. 171, 181-182; 2026g)"),
    "fig_esg_lseg": ("LSEG ESG score against peers, FY2024", "LSEG (2026)"),
    "fig_peers": ("EV / EBITDA against peers, last twelve months, 16-Oct-2026", "S&P Capital IQ (2026); team model"),
}
FIGS_ES = {
    "price_tp": ("Precio de la acción y precio objetivo a 12 meses", "S&P Capital IQ (2026); Yahoo Finance (2026) para el 27-oct-26; modelo del equipo"),
    "dcf_bridge": ("Construcción del DCF base, MXN por acción", "Modelo del equipo (hojas Valuacion y WACC)"),
    "football": ("Campo de fútbol: valor por acción frente al precio y las zonas de calificación", "Modelo del equipo; S&P Capital IQ (2026)"),
    "rev_margin": ("Ventas netas y margen EBITDA ajustado, FY2021A-FY2030E", "Grupo Bimbo (2026f); modelo del equipo"),
    "fig_sales_region": ("Ventas netas de FY2025 por región", "Grupo Bimbo (2026b, p. 4)"),
    "fig_sales_vs_ebitda": ("Participación en ventas y en EBITDA ajustado, FY2025", "Grupo Bimbo (2026b, p. 4; 2026e, p. 17)"),
    "acq_leverage": ("Adquisiciones pagadas y deuda neta con arrendamientos sobre EBITDA", "Grupo Bimbo (2026f); modelo del equipo"),
    "regional_margin": ("Margen EBITDA ajustado por región, FY2021-FY2025", "Grupo Bimbo (2026f, p. 85); modelo del equipo"),
    "fig_ownership": ("Estructura accionaria", "Grupo Bimbo (2026a, pp. 181-182); LSEG (2026)"),
    "fig_market_growth": ("Crecimiento del valor del mercado de panificación, 2019-24 y 2024-29E", "Global Data, en Grupo Bimbo (2026a, pp. 107-111)"),
    "fig_market_type": ("Mercado global de panificación por tipo, 2024", "Global Data, en Grupo Bimbo (2026a, p. 107)"),
    "fig_five_forces": ("Cinco fuerzas: Bimbo son dos industrias en una", "estimación del equipo"),
    "wheat_costs": ("Precio del trigo frente al promedio de 2026E que mantiene el modelo", "IMF (2026); modelo del equipo"),
    "usdmxn": ("USD/MXN promedio anual, 2019-2030E, y tipo de cambio spot del 16 de octubre de 2026", "S&P Capital IQ (2026); modelo del equipo"),
    "growth_fx": ("Crecimiento de ventas netas en pesos: orgánico, adquisiciones y conversión cambiaria", "Grupo Bimbo (2026h); modelo del equipo"),
    "acq_lapping": ("Crecimiento de ventas netas 2026, reportado y sin adquisiciones, Europa-Asia-África y Latinoamérica", "Grupo Bimbo (2026c, 2026d, 2026h); modelo del equipo"),
    "ev_regimes": ("TEV / EBITDA UDM por año, 1999-2026", "S&P Capital IQ (2026)"),
    "cost_passthrough": ("Cambio del costo de ventas por naturaleza como porcentaje de las ventas, FY2023 a FY2025", "Grupo Bimbo (2026f, p. 82); modelo del equipo"),
    "gm_wheat_scenarios": ("Margen bruto FY2021A-FY2030E en el modelo y con el trigo al precio de septiembre de 2026 o 35% más alto desde 2027", "IMF (2026); modelo del equipo"),
    "na_margin_quarterly": ("Margen EBITDA ajustado de Norteamérica por trimestre", "Grupo Bimbo (2026h y reportes trimestrales); estimación del equipo"),
    "guidance_scorecard": ("Metas de la administración desde 2011: cumplidas, mixtas y no cumplidas, por periodo en que se fijaron", "estimación del equipo con base en llamadas de resultados"),
    "margin_vs_consensus": ("Margen EBITDA ajustado: modelo y consenso, FY2026E-FY2028E", "S&P Capital IQ (2026); modelo del equipo"),
    "roic": ("Rendimiento sobre el capital operativo tangible frente al RONIC terminal", "modelo del equipo"),
    "sensitivity": ("Valor por acción: WACC contra crecimiento terminal, objetivo a 12 meses", "modelo del equipo"),
    "fig_peers": ("EV / EBITDA frente a pares, últimos doce meses, 16-oct-2026", "S&P Capital IQ (2026); modelo del equipo"),
    "fcff": ("Flujo de caja libre de la empresa, FY2027E-FY2030E", "modelo del equipo"),
    "margins": ("Margen bruto y margen EBITDA ajustado, FY2021A-FY2030E", "Grupo Bimbo (2026f); modelo del equipo"),
    "ebitda_bridge": ("Margen EBITDA ajustado, de FY2025A a FY2027E, por línea", "Grupo Bimbo (2026f); modelo del equipo"),
    "growth_organic": ("Crecimiento de ventas netas por región, 9M26, reportado y sin adquisiciones", "Grupo Bimbo (2026c, 2026d, 2026h); modelo del equipo. Norteamérica incluye Stone House"),
    "fig_cost_lines": ("Crecimiento de las líneas del costo de ventas frente a las ventas, FY2025", "Grupo Bimbo (2026f, p. 82); modelo del equipo"),
    "fig_capex_cfo": ("Flujo de operación y capex, FY2021-FY2025", "Grupo Bimbo (2026f, p. 86)"),
    "risk_matrix": ("Matriz de riesgos", "estimación del equipo (P, I); modelo del equipo (efectos en el valor)"),
    "tornado": ("Sensibilidad del objetivo a 12 meses", "modelo del equipo"),
    "leverage": ("Deuda neta con arrendamientos sobre EBITDA ajustado", "Grupo Bimbo (2026f); modelo del equipo"),
    "fig_esg_sp": ("Historial de la calificación ESG de S&P Global", "S&P Capital IQ (2026)"),
    "fig_emissions": ("Emisiones de gases de efecto invernadero y metas a 2030", "LSEG (2026); Grupo Bimbo (2026e, p. 169)"),
    "fig_esg_lseg": ("Calificación ESG de LSEG frente a pares, FY2024", "LSEG (2026)"),
    "fig_governance": ("Lista de verificación de gobierno corporativo: puntaje por bloque", "estimación del equipo con base en Grupo Bimbo (2026a, pp. 171, 181-182; 2026g)"),
}
FIG_ALT = {}  # filled from the markdown files: file stem -> (title, source)


def scan_alts():
    if CFG["lang"] == "es":
        return
    for p in sorted(sd().glob("*.md")):
        for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", p.read_text()):
            title, _, src = m.group(1).partition(" | ")
            FIG_ALT[Path(m.group(2)).stem] = (title, src.replace("Source: ", ""))


FIG_SCALE = {"tornado": 0.86, "fig_governance": 0.55, "fig_emissions": 0.62}  # fits the empty zone beside the end of the valuation text
FIG_TOP = {"ebitda_bridge", "margin_vs_consensus"}  # sit beside the opening paragraphs of their section (the central thesis)
FIG_HINTS = {  # figure -> phrases of the paragraph it belongs beside (English, Spanish)
    "usdmxn": ["and on the peso", "y del peso"],
    "wheat_costs": ["Hedges give visibility", "Las coberturas dan visibilidad"],
    "dcf_bridge": ["Built up step by step", "Construido paso a paso"],
    "football": ["sits between the base DCF", "se ubica entre el DCF base"],
    "fig_sales_vs_ebitda": ["Mexico earns", "México gana"],
    "leverage": ["Total assets were", "Los activos totales"],
}


def fig_path(stem: str) -> Path:
    for d in ("tp12m", "en"):
        f = ROOT / f"report/charts/{d}/{stem}.png"
        if f.exists():
            return f
    raise FileNotFoundError(stem)


def preprocess_lang(text: str) -> str:
    text = re.sub(r"^\{\{table:\s*([\w]+)\s*\}\}\s*$", lambda m: (td() / f"{m.group(1)}.md").read_text(), text, flags=re.M)
    return re.sub(r"\s*\(\{fig:[\w]+\}\)", "", text)


def md(name):
    return B.parse_markdown(preprocess_lang((sd() / name).read_text()), name)


def no_h1_no_img(blocks):
    return [b for b in blocks if not (b.kind == "heading" and b.level == 1) and b.kind != "image"]


def under(blocks, heading, upto_level=2):
    """Blocks after a heading until the next heading of the same or higher level."""
    out, on = [], False
    for b in blocks:
        if b.kind == "heading":
            if on and b.level <= upto_level:
                break
            on = b.text.strip() == heading
            continue
        if on and b.kind != "image":
            out.append(b)
    return out


class Blk:
    def __init__(self, kind, text="", level=2, rows=None):
        self.kind, self.text, self.level, self.rows = kind, text, level, rows


def thesis_blocks():
    L = (ROOT / "report/sections/01-investment-summary.md").read_text().split("\n")
    pars = [l for l in L if l and not l.startswith("#") and not l.startswith("!") and not l.startswith("- ")]
    bul2 = [l[2:] for l in L if l.startswith("- ")]  # pillar 2 is written as bullets in the source

    def sents(par):
        parts = re.split(r"(?<=[a-z0-9\)\"%])\. (?=[A-Z\"])", par)
        return [p if p.endswith(".") else p + "." for p in parts]

    def strip_lead(label, sent):
        """Drop a lead-in 'xxx: ' of the sentence when it repeats the bullet label."""
        head, sep, tail = sent.partition(": ")
        if not sep or len(head) > 80:
            return sent
        lw = {w for w in re.findall(r"[a-z]+", label.lower()) if w not in ("the", "a", "and", "of")}
        hw = set(re.findall(r"[a-z]+", head.lower()))
        if lw and len(lw & hw) / len(lw) >= 0.6:
            return tail[0].upper() + tail[1:]
        return sent

    central = []
    if pars and pars[0].startswith("**") and pars[0].endswith("**"):  # central thesis: bold title + two opening paragraphs
        central, pars = pars[:3], pars[3:]
    intro, t1, t3, rating = pars[0], pars[1], pars[2], pars[3]
    plan = [
        ("Pillar 1: Reported growth is flattered by acquisitions and FX", t1,
         [("The record of deals.", [0]), ("What was bought.", [2]), ("What is translated.", [3]),
          ("The market price.", [4, 5, 6]), ("What the valuation depends on.", [7])]),
        ("Pillar 2: Costs can rise without breaking the margin: Bimbo has already absorbed a shock almost four times larger", None, None),
        ("Pillar 3: The new management inherits a recovery, and 2027 is its first real test", t3,
         [("Who is new, and what was inherited.", [0, 1]), ("First results.", [2]), ("What the model already includes.", [3, 4]),
          ("The gap with the street.", [5, 6]), ("The record, and what it is worth.", [7])]),
    ]
    out = [Blk("paragraph", c) for c in central] + [Blk("paragraph", intro)]
    for title, par, groups in plan:
        out.append(Blk("heading", title, 2))
        if par is None:
            out += [Blk("bullet", t) for t in bul2]
            continue
        s = sents(par)
        for label, idx in groups:
            body = " ".join(strip_lead(label, s[i]) if k == 0 else s[i] for k, i in enumerate(idx))
            out.append(Blk("bullet", f"**{label}** " + body))
    out.append(Blk("heading", "Rating and what the valuation depends on", 2))
    out.append(Blk("paragraph", rating))
    return out


def compose():
    scan_alts()
    biz = no_h1_no_img(md("03-company-description.md"))
    mgmt = md("04-management-evaluation.md")
    biz += [Blk("heading", S("mgmt_h"), 2)]
    biz += under(mgmt, S("lead")) + under(mgmt, S("gov"))

    val = no_h1_no_img(md("06-valuation.md"))
    peers = no_h1_no_img(md("05-peer-analysis.md"))
    k = next(i for i, b in enumerate(val) if b.kind == "heading" and b.text.startswith(S("football_start")))
    val = val[:k] + [Blk("heading", S("relval_h"), 2)] + peers + val[k:]

    fc = md("10-financial-forecast.md")
    wide, rest = [], []
    mode = 0  # 0 text, 1 caption/table/source of the forecast table
    for b in no_h1_no_img(fc):
        if b.kind == "paragraph" and b.text.startswith("Table:"):
            wide.append(b); mode = 1; continue
        if mode == 1:
            wide.append(b)
            if b.kind == "paragraph" and B.SOURCE_LINE.match(b.text):
                mode = 0
            continue
        rest.append(b)
    fa = no_h1_no_img(md("09-financial-analysis.md")) + [Blk("heading", S("forecast_h"), 2)] + rest

    risk_wide, risk_rest, mode = [], [], 0  # the six-column signals table is set across the full page width
    for b in no_h1_no_img(md("07-investment-risks.md")):
        if b.kind == "paragraph" and b.text.startswith("Table:"):
            risk_wide.append(b); mode = 1; continue
        if mode == 1:
            risk_wide.append(b)
            if b.kind == "paragraph" and B.SOURCE_LINE.match(b.text):
                mode = 0
            continue
        risk_rest.append(b)

    summ = no_h1_no_img(md("00-summary.md"))
    app = md("98-appendix.md")
    stm = under(mgmt, S("said"))
    j = next(i for i, b in enumerate(app) if b.kind == "heading" and b.text.startswith("A7"))
    app = app[:j] + [Blk("heading", S("a7"), 2)] + stm + app[j:]
    def cap(stem):
        return FIGS_ES[stem] if CFG["lang"] == "es" else (FIG_ALT.get(stem) or FIGS[stem])
    ttl, src_ = cap("fig_esg_lseg")
    fb = Blk("image", f"{ttl} | {src_}")
    fb.path = "../charts/en/fig_esg_lseg.png"
    ttl2, src2 = cap("fig_esg_sp")
    fs2 = Blk("image", f"{ttl2} | {src2}")
    fs2.path = "../charts/en/fig_esg_sp.png"
    j6 = next(i for i, b in enumerate(app) if b.kind == "heading" and b.text.startswith("A6"))
    ff = Blk("image", S("football_cap"))
    ff.path = "../charts/tp12m/football.png"
    app = app[:j6] + [Blk("heading", S("a5c"), 2), ff, Blk("heading", S("a5d"), 2), fb, fs2] + app[j6:]
    for b in app:
        if b.kind == "heading" and b.text.startswith(S("refs_old")):
            b.text = S("refs_new")
    app += md("99-appendix-ai-use.md")

    return [
        ("Executive Summary", summ, ["price_tp", "rev_margin"], []),
        ("Business Overview", biz, ["fig_sales_region", "acq_leverage", "regional_margin", "fig_ownership"], []),
        ("Industry Overview", no_h1_no_img(md("02-industry.md")), ["fig_market_growth", "fig_market_type", "fig_five_forces"], []),
        ("Investment Summary", thesis_blocks() if CFG["lang"] == "en" else no_h1_no_img(md("03-investment-summary.md")),
         ["ebitda_bridge", "margin_vs_consensus", "acq_lapping", "growth_fx", "ev_regimes", "usdmxn", "wheat_costs",
          "gm_wheat_scenarios", "na_margin_quarterly", "guidance_scorecard"], []),
        ("Valuation", val, ["fig_peers", "fcff", "roic", "dcf_bridge"], []),
        ("Financial Analysis", fa, ["margins", "fig_sales_vs_ebitda", "growth_organic", "leverage", "fig_cost_lines", "cost_passthrough", "fig_capex_cfo"], wide),
        ("Risks", risk_rest, ["risk_matrix", "tornado"], risk_wide),
        ("ESG", no_h1_no_img(md("08-esg.md")), ["fig_emissions", "fig_governance"], []),
        ("Appendix", app, [], []),
    ]


# ------------------------------------------------------------------------------------------------------ docx helpers
def runs(par, text, size=BODY_PT, bold=False, italic=False, color=None):
    for part in INLINE.split(text):
        if not part:
            continue
        strong = part.startswith("**") and part.endswith("**")
        emph = not strong and part.startswith("*") and part.endswith("*") and len(part) > 2
        r = par.add_run(part.strip("*") if (strong or emph) else part)
        r.font.name, r.font.size = FONT, Pt(size)
        r._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        r.bold = True if (strong or bold) else None
        r.italic = True if (emph or italic) else None
        if color:
            r.font.color.rgb = RGBColor.from_string(color)


def fmt(par, after=3, before=0, align=WD_ALIGN_PARAGRAPH.JUSTIFY, keep_next=False):
    pf = par.paragraph_format
    pf.space_after, pf.space_before, pf.line_spacing = Pt(after), Pt(before), 1.0
    par.alignment = align
    pf.keep_with_next = keep_next
    pf.keep_together = True  # no paragraph is split across pages


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


def borders(table, color="BFBFBF", sz=4, inside=True):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for k in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{k}")
        on = inside or k in ("top", "bottom")
        e.set(qn("w:val"), "single" if on else "nil"); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), "0"); e.set(qn("w:color"), color)
        b.append(e)
    tblPr.append(b)


def no_borders(table):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for k in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:val"), "nil"); b.append(e)
    tblPr.append(b)


def set_col_widths(table, widths):
    table.autofit = False
    tblPr = table._tbl.tblPr
    for tag in ("w:tblLayout", "w:tblW", "w:tblInd"):
        for e in tblPr.findall(qn(tag)):
            tblPr.remove(e)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    tw = OxmlElement("w:tblW"); tw.set(qn("w:type"), "dxa"); tw.set(qn("w:w"), str(int(sum(widths) / 635))); tblPr.append(tw)
    ti = OxmlElement("w:tblInd"); ti.set(qn("w:type"), "dxa"); ti.set(qn("w:w"), "0"); tblPr.append(ti)
    grid = table._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(int(w / 635)))
    for row in table.rows:
        for c, w in zip(row.cells, widths):
            c.width = w


class Report:
    def __init__(self, header):
        self.h = header
        self.doc = Document()
        self.fig_n = self.tab_n = 0
        st = self.doc.styles["Normal"]
        st.font.name, st.font.size = FONT, Pt(BODY_PT)
        self.body_ready = False

    def _body_section(self, sec):
        sec.page_width, sec.page_height = Mm(210), Mm(297)
        sec.left_margin = sec.right_margin = Mm(MARGIN)
        sec.top_margin, sec.bottom_margin = Mm(7), Mm(9.5)
        sec.footer_distance = Mm(3.5)
        sec.footer.is_linked_to_previous = False
        p = sec.footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(S("footer"))
        r.font.size, r.font.name = Pt(7), FONT
        for t in ("begin", None, "end"):
            run = p.add_run(); run.font.size = Pt(7)
            if t:
                f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), t); run._r.append(f)
            else:
                it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = "PAGE"; run._r.append(it)
        # page numbers continue from the cover, so the label of each page is its position in the file
        self.body_ready = True

    def cover(self):
        """Official CFA Institute cover (as in the La Comer report), the highlighted fields adapted to Bimbo."""
        sec = self.doc.sections[0]
        sec.page_width, sec.page_height = Mm(210), Mm(297)
        sec.left_margin = sec.right_margin = Mm(22)
        sec.top_margin, sec.bottom_margin = Mm(18), Mm(12)
        SERIF = "Georgia"

        def run(par, text, size, bold=False, font=FONT, hl=None, fill=None):
            r = par.add_run(text)
            r.font.name, r.font.size, r.bold = font, Pt(size), bold or None
            r._element.rPr.rFonts.set(qn("w:eastAsia"), font)
            if hl:
                r.font.highlight_color = hl
            if fill:
                shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
                r._element.rPr.append(shd)
            return r

        def para(after=2, before=0, align=WD_ALIGN_PARAGRAPH.LEFT):
            p = self.doc.add_paragraph()
            p.paragraph_format.space_after, p.paragraph_format.space_before = Pt(after), Pt(before)
            p.paragraph_format.line_spacing = 1.0
            p.alignment = align
            return p

        p = para(after=26, align=WD_ALIGN_PARAGRAPH.CENTER)
        p.add_run().add_picture(str(ROOT / "report/assets/cfa-institute-logo.png"), width=Mm(138))
        p = para(after=0, align=WD_ALIGN_PARAGRAPH.CENTER); run(p, "CFA Institute Research Challenge", 18, True, SERIF)
        p = para(after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        run(p, "hosted by ", 13.5, True, SERIF); run(p, "CFA Society Mexico", 13.5, True, SERIF)
        p = para(after=8, align=WD_ALIGN_PARAGRAPH.CENTER); run(p, "TEC DE MONTERREY CAMPUS AGUASCALIENTES", 13.5, True, SERIF)
        rule = para(after=10)
        bd = OxmlElement("w:pBdr"); e = OxmlElement("w:bottom")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "8"); e.set(qn("w:space"), "1"); e.set(qn("w:color"), "7F7F7F")
        bd.append(e); rule._p.get_or_add_pPr().append(bd)
        p = para(after=16, align=WD_ALIGN_PARAGRAPH.LEFT)
        run(p, "The CFA Institute Research Challenge is a global competition that tests the equity research and valuation, investment report "
               "writing, and presentation skills of university students. The following report was prepared by a team of university students as "
               "part of this annual educational initiative and should not be considered a professional report.", 11.4)
        p = para(after=2); run(p, "Disclosures:", 15.5, True, SERIF)

        def head(t):
            q = para(after=0, before=4); run(q, t, 9.6, True, SERIF)

        def body(t=None):
            q = para(after=0)
            if t:
                run(q, t, 9.4)
            return q
        head("Ownership and material conflicts of interest")
        q = body("The author(s), or a member of their household, of this report ")
        run(q, "does not hold", 9.4); run(q, " a financial interest in the securities of this company.", 9.4)
        q = body("The author(s), or a member of their household, of this report ")
        run(q, "does not know", 9.4)
        run(q, " of the existence of any conflicts of interest that might bias the content or publication of this report.", 9.4)
        head("Receipt of compensation")
        body("Compensation of the author(s) of this report is not based on investment banking revenue.")
        head("Position as an officer or director")
        body("The author(s), or a member of their household, does not serve as an officer, director, or advisory board member of the subject company.")
        head("Marketing making")
        body("The author(s) does not act as a market maker in the subject company\u2019s securities.")
        head("Disclaimer")
        body("The information set forth herein has been obtained or derived from sources generally available to the public and believed by the "
             "author(s) to be reliable, but the author(s) does not make any representation or warranty, express or implied, as to its accuracy "
             "or completeness. The information is not intended to be used as the basis of any investment decisions by any person or entity. "
             "This information does not constitute investment advice, nor is it an offer or a solicitation of an offer to buy or sell any "
             "security. This report should not be considered to be a recommendation by any individual affiliated with CFA Society Mexico, "
             "CFA Institute, or the CFA Institute Research Challenge with regard to this company\u2019s stock.")
        self._body_section(self.doc.add_section(WD_SECTION.NEW_PAGE))

    # ---- header band
    def band(self):
        h = self.h
        up = h["target_price"] / h["price"] - 1
        t = self.doc.add_table(rows=1, cols=3)
        no_borders(t); cell_margins(t, 60, 60, 80, 80)
        set_col_widths(t, [Mm(36), Mm(68), Mm(86)])
        for c in t.rows[0].cells:
            shade(c, BAND)
        logo = ROOT / "report/assets/bimbo-logo.png"
        c0, c1, c2 = t.rows[0].cells
        if logo.exists():
            c0.paragraphs[0].add_run().add_picture(str(logo), height=Mm(15))
        sector, industry = (h["sector"], h["industry"]) if CFG["lang"] == "en" else ("Consumo básico", "Alimentos empaquetados y panificación")
        lines = [("", h["company"], True), (S("bmv"), h["ticker"], False), (S("sector"), sector, False),
                 ("Industry: " if CFG["lang"] == "en" else "Industria: ", industry, False)]
        for i, (lab, val, big) in enumerate(lines):
            p = c1.paragraphs[0] if i == 0 else c1.add_paragraph()
            fmt(p, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
            if lab:
                runs(p, lab, size=9.5, bold=True, color=BLUE)
            runs(p, val, size=11 if big else 9.5, bold=True)
        rec = h["recommendation"] if CFG["lang"] == "en" else {"HOLD": "MANTENER", "BUY": "COMPRAR", "SELL": "VENDER"}[h["recommendation"]]
        if h.get("bias") == "negative":
            rec += " (negative bias)" if CFG["lang"] == "en" else " con sesgo a la baja"
        right = [("", S("rec").format(rec), None),
                 (S("target"), S("target_val" if up >= 0 else "target_val_dn").format(h["target_price"], abs(up) * 100), True),
                 (S("price").format(h["price_date"]), f"MXN {h['price']:.2f}", True)]
        for i, (lab, val, lb) in enumerate(right):
            p = c2.paragraphs[0] if i == 0 else c2.add_paragraph()
            fmt(p, after=2, align=WD_ALIGN_PARAGRAPH.RIGHT)
            if lab:
                runs(p, lab, size=9, bold=True, color=BLUE)
            runs(p, val, size=11 if i == 0 else 9, bold=True, color=RED if i == 0 else None)
        sp = self.doc.add_paragraph(); fmt(sp, after=0)
        sp.paragraph_format.space_after = Pt(0)

    # ---- section title
    def title(self, text, new_page=False, black=False):
        p = self.doc.add_paragraph()
        p.paragraph_format.page_break_before = new_page
        import os
        fmt(p, after=3, before=5, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=not os.environ.get('NO_KEEP'))
        runs(p, text, size=14, bold=True, color="000000" if black else BLUE)
        pPr = p._p.get_or_add_pPr()
        bd = OxmlElement("w:pBdr"); e = OxmlElement("w:bottom")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "8"); e.set(qn("w:space"), "1"); e.set(qn("w:color"), "000000")
        bd.append(e); pPr.append(bd)
        pf = p.paragraph_format
        pf.right_indent = Mm(190 - 123 - 2) if not black else 0

    # ---- generic content into a container (cell or document)
    def add_par(self, cont, first=[None]):
        return cont.add_paragraph()

    def put_blocks(self, cont, blocks, first_empty=True, width=LEFT_W, wide=False):
        used_first = not first_empty
        def newp():
            nonlocal used_first
            if not used_first:
                used_first = True
                return cont.paragraphs[0]
            return cont.add_paragraph()
        for b in blocks:
            if b.kind == "heading":
                p = newp(); fmt(p, after=1.2, before=2, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=False)
                runs(p, b.text, size=9.2 if b.level == 2 else 8.8, bold=True, color=BLUE)
            elif b.kind == "paragraph":
                if b.text.startswith("Table:"):
                    self.tab_n += 1
                    p = newp(); fmt(p, after=1, before=2, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
                    runs(p, f"{S('tab')} {self.tab_n}: ", size=7.8, bold=True, color=BLUE); runs(p, b.text[6:].strip(), size=7.8, bold=True)
                elif B.SOURCE_LINE.match(b.text):
                    p = newp(); fmt(p, after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
                    runs(p, src_text(b.text), size=6.8, italic=True)
                else:
                    p = newp(); fmt(p, after=2.4); runs(p, b.text)
            elif b.kind in ("bullet", "number"):
                p = newp(); fmt(p, after=1.5)
                p.paragraph_format.left_indent = Mm(3.2); p.paragraph_format.first_line_indent = Mm(-3.2)
                runs(p, "\u2022 ", color=BLUE, bold=True); runs(p, b.text)
            elif b.kind == "table":
                import os
                if os.environ.get("NO_NESTED") and not wide:
                    continue
                self.table(cont, b.rows, width, wide)
                used_first = True
            elif b.kind == "image":
                pass
        if cont.paragraphs and not cont.paragraphs[-1].text and False:
            pass

    def table(self, cont, rows, width, wide):
        n = len(rows[0])
        t = cont.add_table(rows=len(rows), cols=n)
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        borders(t, "BFBFBF", 3, True); cell_margins(t, 12, 12, 35, 35)
        first = Mm(34) if n > 3 else Mm(52)
        if wide:
            first = Mm(46)
        total = (width - Mm(6)) if not wide else width
        rest = int((total - first) / (n - 1)) if n > 1 else 0
        widths = [first] + [rest] * (n - 1)
        avg = [sum(len(r[j]) for r in rows[1:]) / max(1, len(rows) - 1) for j in range(n)]
        if wide and n >= 5 and sum(avg) / n > 25:  # text-heavy wide table: column widths follow the text
            wt = [max(22.0, min(a, 80.0)) for a in avg]
            widths = [int(total * w / sum(wt)) for w in wt]
        set_col_widths(t, widths)
        size = 7.4 if wide else 6.8
        for ri, row in enumerate(rows):
            bold_row = row[0].startswith("**")
            for ci, txt in enumerate(row):
                c = t.cell(ri, ci)
                p = c.paragraphs[0]
                fmt(p, after=0, align=WD_ALIGN_PARAGRAPH.LEFT if ci == 0 or (len(txt) > 14 and not B.looks_numeric(txt.strip("*"))) else WD_ALIGN_PARAGRAPH.CENTER, keep_next=ri < len(rows) - 1)
                runs(p, txt, size=size, bold=(ri == 0) or None, color="FFFFFF" if ri == 0 else None)
                if ri == 0:
                    shade(c, BLUE)
                elif bold_row:
                    shade(c, BAND)
        return t

    # ---- right column figure (caption, picture and source in one row that cannot split)
    def put_figure(self, cell, stem, first):
        title, src = FIGS_ES[stem] if CFG["lang"] == "es" else (FIG_ALT.get(stem) or FIGS[stem])
        self.fig_n += 1
        t = cell.add_table(rows=1, cols=1)
        no_borders(t); cell_margins(t, 0, 0, 0, 0)
        set_col_widths(t, [RIGHT_W - Mm(1)])
        trPr = t.rows[0]._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        c = t.cell(0, 0)
        p = c.paragraphs[0]
        fmt(p, after=1, before=0, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        runs(p, f"{S('fig')} {self.fig_n}: ", size=7.8, bold=True, color=BLUE); runs(p, title, size=7.8, bold=True)
        q = c.add_paragraph(); fmt(q, after=1, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        q.add_run().add_picture(str(fig_path(stem)), width=int(FIG_W * FIG_SCALE.get(stem, 1.0)))
        s_ = c.add_paragraph(); fmt(s_, after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        runs(s_, S("source") + ": " + src, size=6.6, italic=True)
        sp = cell.paragraphs[-1]
        fmt(sp, after=0, before=0)
        for r_ in sp.runs:
            r_.font.size = Pt(3)
        sp.paragraph_format.line_spacing = Pt(5)

    @staticmethod
    def _units(blocks):
        """Paragraph-sized units: a heading stays with the block after it, a table with its caption and source."""
        units, cur, in_table = [], [], False

        def flush():
            nonlocal cur
            if cur:
                units.append(cur)
            cur = []
        for b in blocks:
            if b.kind == "heading":
                flush(); cur = [b]
            elif b.kind == "paragraph" and b.text.startswith("Table:"):
                if not (cur and all(x.kind == "heading" for x in cur)):
                    flush()
                cur.append(b); in_table = True
            elif in_table:
                cur.append(b)
                if b.kind == "paragraph" and B.SOURCE_LINE.match(b.text):
                    flush(); in_table = False
            else:
                cur.append(b)
                if b.kind in ("paragraph", "bullet", "number"):
                    flush()
        flush()
        return units

    @staticmethod
    def _weight(unit):
        """Estimated height (pt) of a paragraph unit in the left column."""
        cpl = (LEFT_W / 12700 - 12) / (0.50 * BODY_PT)  # characters per line
        lh, h = BODY_PT * 1.17, 0.0
        for b in unit:
            txt = getattr(b, "text", "") or ""
            if b.kind == "heading":
                h += 15
            elif b.kind == "table":
                h += len(b.rows) * 9.6 + 4
            elif b.kind in ("paragraph", "bullet", "number"):
                h += max(1, -(-len(txt) // int(cpl))) * lh + 3
        return h

    @staticmethod
    def _fig_h(stem):
        """Estimated height (pt) of a figure block: caption, picture, source."""
        from PIL import Image
        w, hh = Image.open(fig_path(stem)).size
        return 19 + (FIG_W * FIG_SCALE.get(stem, 1.0) / 12700) * hh / w + 16 + 5

    def _plan(self, units, figs):
        """Rows of (units, figures): each figure sits beside the paragraph that cites it, or at its share of the text;
        a row takes paragraphs until the text is as tall as the figures, so that little space is left empty."""
        w = [self._weight(u) for u in units]
        total = float(sum(w)) or 1.0
        start = [sum(w[:i]) for i in range(len(w))]
        anchor = {}
        for ui, u in enumerate(units):
            for b in u:
                for st in getattr(b, "stems", []):
                    anchor.setdefault(st, ui)
        for st, hints in FIG_HINTS.items():
            if st in figs and st not in anchor:
                for ui, u in enumerate(units):
                    if any(h in (getattr(b, "text", "") or "") for b in u for h in hints):
                        anchor[st] = ui
                        break
        pos = []
        for k, st in enumerate(figs):
            pos.append(0.0 if st in FIG_TOP else start[anchor[st]] if st in anchor else (k + 0.5) / len(figs) * total)
            if pos[-1] < (pos[-2] if k else 0):
                pos[-1] = pos[-2]
        where = {}
        for st, p_ in zip(figs, pos):
            ui = max(i for i in range(len(units)) if start[i] <= p_) if units else 0
            where.setdefault(ui, []).append(st)
        rows, i, fig_units = [], 0, sorted(where)
        while i < len(units):
            if i in where:
                fs = where[i]
                need = sum(self._fig_h(st) for st in fs)
                nxt = min((u for u in fig_units if u > i), default=len(units))
                take, acc, k = [], 0.0, i
                while k < nxt and (not take or acc < need):
                    take.append(units[k]); acc += w[k]; k += 1
                rows.append((take, fs)); i = k
            else:
                rows.append(([units[i]], [])); i += 1
        return rows

    def section(self, title, blocks, figs, wide, first_section=False):
        self.title(title)
        wide_last = title == S("Risks")  # the signals table closes the risks section; the forecast table opens the financial analysis
        if wide and not wide_last:
            self.put_blocks(self.doc, wide, first_empty=False, width=PAGE_W, wide=True)
        t = self.doc.add_table(rows=0, cols=2)
        no_borders(t); cell_margins(t, 0, 0, 0, 0)
        set_col_widths(t, [LEFT_W, RIGHT_W])
        for left_units, fs in self._plan(self._units(blocks), figs):
            row = t.add_row()
            if os.environ.get("ROW_NOSPLIT"):  # a row (paragraphs and their figure) never breaks across pages
                row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
            L, R = row.cells
            L.width, R.width = LEFT_W, RIGHT_W
            tcPr = L._tc.get_or_add_tcPr()
            mar = OxmlElement("w:tcMar"); e = OxmlElement("w:right"); e.set(qn("w:w"), str(int(Mm(3) / 635))); e.set(qn("w:type"), "dxa")
            mar.append(e); tcPr.append(mar)
            for n, u in enumerate(left_units):
                self.put_blocks(L, u, first_empty=(n == 0), width=LEFT_W)
            for n, stem in enumerate(fs):
                self.put_figure(R, stem, first=(n == 0))
        sp = self.doc.add_paragraph(); fmt(sp, after=0); sp.paragraph_format.space_after = Pt(0)
        if wide and wide_last:
            self.put_blocks(self.doc, wide, first_empty=False, width=PAGE_W, wide=True)

    def appendix(self, blocks):
        self.title(S("Appendix"), new_page=True, black=True)
        i = 0
        for b in blocks:
            if b.kind == "heading" and b.level == 1:
                if b.text != S("Appendix"):
                    self.title(b.text, black=True)
                continue
            if b.kind == "heading":
                p = self.doc.add_paragraph(); fmt(p, after=2, before=5, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
                runs(p, b.text, size=9.5, bold=True, color=BLUE)
            elif b.kind == "paragraph":
                if b.text.startswith("Table:"):
                    self.tab_n += 1
                    p = self.doc.add_paragraph(); fmt(p, after=1, before=2, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
                    runs(p, f"{S('tab')} {self.tab_n}: ", size=7.8, bold=True, color=BLUE); runs(p, b.text[6:].strip(), size=7.8, bold=True)
                elif B.SOURCE_LINE.match(b.text):
                    p = self.doc.add_paragraph(); fmt(p, after=4, align=WD_ALIGN_PARAGRAPH.CENTER); runs(p, src_text(b.text), size=6.8, italic=True)
                else:
                    p = self.doc.add_paragraph(); fmt(p, after=3); runs(p, b.text)
            elif b.kind in ("bullet", "number"):
                p = self.doc.add_paragraph(); fmt(p, after=2)
                p.paragraph_format.left_indent = Mm(3.2); p.paragraph_format.first_line_indent = Mm(-3.2)
                runs(p, "\u2022 ", color=BLUE, bold=True); runs(p, b.text)
            elif b.kind == "table":
                self.table(self.doc, b.rows, PAGE_W, True)
                self.doc.add_paragraph().paragraph_format.space_after = Pt(1)
            elif b.kind == "image":
                title, _, src = b.text.partition(" | ")
                self.fig_n += 1
                p = self.doc.add_paragraph(); fmt(p, after=1, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
                runs(p, f"{S('fig')} {self.fig_n}: ", size=7.8, bold=True, color=BLUE); runs(p, title, size=7.8, bold=True)
                q = self.doc.add_paragraph(); fmt(q, after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
                q.add_run().add_picture(str((sd() / b.path).resolve()), width=Inches(4.2))
                s = self.doc.add_paragraph(); fmt(s, after=3, align=WD_ALIGN_PARAGRAPH.CENTER); runs(s, S("source") + ": " + src.replace("Source: ", ""), size=6.8, italic=True)
            i += 1


def src_text(t: str) -> str:
    return re.sub(r"^source:", "Fuente:", t, flags=re.I) if CFG["lang"] == "es" else t


def resolve_tokens(secs):
    """Replace '@stem' references in the text with the number of that figure in this layout."""
    order = []
    for title, blocks, figs, wide in secs:
        order += figs
        pass
    num = {stem: i + 1 for i, stem in enumerate(order)}
    for title, blocks, figs, wide in secs:
        for b in list(blocks) + list(wide):
            if isinstance(getattr(b, "text", None), str) and "@" in b.text:
                b.stems = re.findall(r"@([a-z_0-9]+)", b.text)
                b.text = re.sub(r"@([a-z_0-9]+)", lambda m: str(num[m.group(1)]), b.text)
    return secs


def build(out: Path, check_only=False):
    header = yaml.safe_load((ROOT / "report/header.yaml").read_text())
    secs = resolve_tokens(compose())
    if check_only:
        allb = [(Path("98-appendix.md" if t == "Appendix" else f"{i:02d}-{t.lower().replace(chr(32), chr(45))}.md"), blocks) for i, (t, blocks, _, _) in enumerate(secs)]
        un = B.uncited(allb)
        words = sum(B._words(bl) for t, bl, _, _ in secs if t != "Appendix")
        print("body words (excl. appendix):", words)
        print("uncited:", len(un))
        for s, t in un:
            print("  ", s, "|", t)
        return
    r = Report(header)
    r.cover()
    r.band()
    for title, blocks, figs, wide in secs:
        if title == "Appendix":
            continue
        r.section(S(title), blocks, figs, wide)
        if title == "Executive Summary":
            p = r.doc.add_paragraph(); fmt(p, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
            runs(p, S("analysts"), size=8.6, bold=True, color=BLUE)
            runs(p, "Luis Arturo Romo Alba, Diego Benavides Pro, Alexa Garcia Saldivar, Jorge Alejandro Gaytan, Carolina del Rosario Benites", size=8.6)
    r.appendix(next(bl for t, bl, _, _ in secs if t == "Appendix"))
    out.parent.mkdir(parents=True, exist_ok=True)
    r.doc.save(out)
    print("wrote", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--lang", default="en", choices=["en", "es"])
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    CFG["lang"] = a.lang
    out = a.out or str(ROOT / ("report/BIMBOA_reporte_es.docx" if a.lang == "es" else "report/BIMBOA_report_v11.docx"))
    build(Path(out), a.check)
