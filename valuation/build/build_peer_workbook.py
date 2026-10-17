"""S&P 'Financials & Peer Analysis' workbook v3 for Grupo Bimbo, in English and Spanish.

Built ON TOP of valuation/BIMBOA_PeerAnalysis_v1.xlsx, whose claim-basis logic (~525 formulas) was reviewed:
  - v1 sheets kept as Detail_TearSheet / Detail_PeerAnalysis (formula references rewritten), Inputs_Sources, Checks;
  - Mondelez current operating leases (164, Dec-25 proxy) added to the claim basis; BMV close re-sourced;
  - new front sheets TearSheet and PeerAnalysis laid out like valuation/SPG_FinancialsAndPeerAnalysis_VA_v1.xlsx
    (FY2023A-FY2029E; Market Data / Financials / Performance Valuations), linked to the detail sheets and inputs;
  - template fields the local data cannot fill stay blank, shaded and marked 'pending CIQ refresh' (never zero).
v3 (2026-10-17): the Capital IQ prompts 4-7 data, the pricing-date FX (USD/MXN 18.479) and the eligibility decisions
come from valuation/inputs/peer_extras_v3.yaml (calculator spec transcribed by the writer agent); the Checks sheet
compares the rebuilt multiples and medians with that spec's expected values and lists the v2 -> v3 changes.

  python -I valuation/build/build_peer_workbook.py --project .              # writes v3 and v3_ES
  (then recalc both with recalc_excel.ps1 and scan them with scan_errors.py)
  python -I valuation/build/build_peer_workbook.py --project . --peers-yaml # after recalc: regenerate peers.yaml numbers
The S&P template is never opened for writing.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_workbook as tw  # noqa: E402

NAVY = "1F3864"
F_TITLE = Font(name="Calibri", size=14, bold=True, color=NAVY)
F_HDR = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
F_BOLD = Font(name="Calibri", size=10, bold=True)
F_NORM = Font(name="Calibri", size=10)
F_NOTE = Font(name="Calibri", size=9, italic=True, color="595959")
F_LINK = Font(name="Calibri", size=10, color="00803C")
F_INPUT = Font(name="Calibri", size=10, color="0000FF")
FILL_HDR = PatternFill("solid", fgColor=NAVY)
FILL_SUB = PatternFill("solid", fgColor="D9E1F2")
FILL_PEND = PatternFill("solid", fgColor="F2F2F2")
FILL_IN = PatternFill("solid", fgColor="FFF2CC")
FMT = {"m": '#,##0.0;(#,##0.0);"-"', "m0": '#,##0;(#,##0);"-"', "p": '0.0%;(0.0%);"-"', "x": '0.00"x"',
       "px": '#,##0.00', "eps": '0.00'}

PEERS = ["FLO", "GRUMA", "YMZ", "ARYN", "SJM", "CPB", "MDLZ", "AC", "PEP"]          # v1 row order
ROW_A = {"BIMBO": 11, **{k: 12 + i for i, k in enumerate(PEERS)}}                 # market data block
ROW_B = {"BIMBO": 25, **{k: 26 + i for i, k in enumerate(PEERS)}}                 # financials block
ROW_C = {"BIMBO": 39, **{k: 40 + i for i, k in enumerate(PEERS)}}                 # valuation block
ROW_CAL = {"BIMBO": 60, **{k: 61 + i for i, k in enumerate(PEERS)}}               # calendarisation block
VERSION = 3
PX_DATES = ["2026-10-16", "2026-09-30", "2025-12-31", "2025-10-31", "2024-10-31", "2023-10-31", "2021-10-29"]
PERF = [("perf_qtd", 1), ("perf_ytd", 2), ("perf_1y", 3), ("perf_2y", 4), ("perf_3y", 5), ("perf_5y", 6)]   # base index
PERF_COL = {"perf_1y": 12, "perf_2y": 13, "perf_3y": 14, "perf_5y": 15, "perf_qtd": 16, "perf_ytd": 17}  # PeerAnalysis L..Q
ORDER = PEERS + ["BIMBO"]                                                         # front-sheet row order
PERF_KEY = re.compile(r"^(\w+)\.(perf_(?:qtd|ytd|1y|2y|3y|5y))$")


def load_extras(project: Path) -> dict:
    """valuation/inputs/peer_extras_v3.yaml (written from the calculator agent's spec)."""
    import yaml
    path = project / "valuation" / "inputs" / f"peer_extras_v{VERSION}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

# ---------------------------------------------------------------- bilingual labels
T = {
    "ts_title": ("Financials & Peer Analysis", "Financieros y análisis de pares"),
    "setup": ("Company set-up (static values: the CIQ Excel plugin is not used)",
              "Configuración (valores fijos: no se usa el complemento de CIQ para Excel)"),
    "step1": ("Step 1. Company identifier", "Paso 1. Identificador de la empresa"),
    "step2": ("Step 2. Latest completed year", "Paso 2. Último año completo"),
    "step3": ("Step 3. As-of date", "Paso 3. Fecha de corte"),
    "step4": ("Step 4. Currency", "Paso 4. Moneda"),
    "step5": ("Step 5. Magnitude", "Paso 5. Magnitud"),
    "step6": ("Step 6. Source", "Paso 6. Fuente"),
    "step7": ("Step 7. Refresh", "Paso 7. Actualizar"),
    "v_ccy": ("Mexican peso (MXN)", "Peso mexicano (MXN)"),
    "v_mag": ("Millions", "Millones"),
    "v_src": ("Company filings and CIQ (A); S&P Capital IQ consensus mean (E)",
              "Reportes de la empresa y CIQ (A); promedio de consenso de S&P Capital IQ (E)"),
    "v_refresh": ("Not linked to CIQ: re-run valuation/build/build_peer_workbook.py",
                  "Sin liga a CIQ: volver a correr valuation/build/build_peer_workbook.py"),
    "notes": ("Notes:", "Notas:"),
    "note1": ("Layout after the S&P Capital IQ Pro 'Financials & Peer Analysis' template. Numbers are static and "
              "tagged; detail and sources are in Detail_TearSheet and Inputs_Sources.",
              "Formato de la plantilla 'Financials & Peer Analysis' de S&P Capital IQ Pro. Las cifras son fijas y "
              "llevan etiqueta; el detalle y las fuentes están en Detail_TearSheet e Inputs_Sources."),
    "note2": ("A = actual (CIQ quarterly sums or company filings); E = consensus mean (CIQ, 20-Sep-2026). "
              "Shaded blank = not in the local data; pending a CIQ refresh.",
              "A = real (sumas trimestrales de CIQ o reportes de la empresa); E = promedio de consenso (CIQ, "
              "20-sep-2026). Celda sombreada vacía = no está en los datos locales; pendiente de actualizar con CIQ."),
    "data_in": ("Data in (MXN m), except per share", "Cifras en millones de MXN, salvo por acción"),
    "chart": ("Chart 1: Revenue and EBITDA (MXN m)", "Gráfica 1: Ventas y EBITDA (millones de MXN)"),
    "is": ("Income Statement", "Estado de resultados"),
    "bs": ("Balance Sheet", "Balance general"),
    "cf": ("Cash Flow", "Flujo de efectivo"),
    "mr": ("Margins / Ratios", "Márgenes / razones"),
    "tag": ("Tag / source", "Etiqueta / fuente"),
    "src_line": ("Source: S&P Capital IQ Pro (CIQ CSV exports and consensus, 19/20-Sep-2026) and Grupo Bimbo filings; "
                 "compiled in Inputs_Sources and Detail_TearSheet.",
                 "Fuente: S&P Capital IQ Pro (exportaciones CSV y consenso de CIQ, 19/20-sep-2026) y reportes de Grupo "
                 "Bimbo; compilado en Inputs_Sources y Detail_TearSheet."),
    "pa_title": ("Performance Valuation - Grupo Bimbo and peers", "Valuación y desempeño - Grupo Bimbo y pares"),
    "pa_n1": ("Pricing date 16-Oct-2026. USD m; MXN figures converted at the pricing-date rate, MXN 18.479 per USD "
              "(Bimbo's own multiples are computed in MXN).",
              "Fecha de precios: 16-oct-2026. Millones de USD; las cifras en MXN se convierten al tipo de cambio de la "
              "fecha de precios, 18.479 MXN por USD (los múltiplos de Bimbo se calculan en MXN)."),
    "pa_n2": ("Enterprise value on one claim basis for every company: financial debt + lease liabilities + NCI at book "
              "- cash (pensions, MEPP and derivatives excluded); US GAAP EBITDA + operating lease cost.",
              "Valor de la empresa con una sola base de reclamos para todas: deuda financiera + pasivos por "
              "arrendamiento + participación no controladora en libros - caja (sin pensiones, MEPP ni derivados); "
              "EBITDA US GAAP + costo de arrendamientos operativos."),
    "pa_n3": ("Shaded blank = not available (peers' 52-week range and 1-day change were not returned by Capital IQ). "
              "Price changes over 1, 2, 3 and 5 years are month-end approximations (base 31-Oct); QTD and YTD are exact.",
              "Celda sombreada vacía = no disponible (Capital IQ no devolvió el rango de 52 semanas ni el cambio de 1 "
              "día de los pares). Los cambios a 1, 2, 3 y 5 años son aproximaciones de fin de mes (base 31-oct); "
              "trimestre y año en curso son exactos."),
    "capint": ("Capital intensity: consensus capex / consensus revenue (Capital IQ, FY1-FY3)",
               "Intensidad de capital: capex de consenso / ventas de consenso (Capital IQ, FY1-FY3)"),
    "capint_med": ("Peer median (excluding Bimbo)", "Mediana de pares (sin Bimbo)"),
    "capint_note": ("FY1-FY3 = FY2026E-FY2028E; Smucker FY2027E-FY2029E (April year-end); Campbell's FY2027E-FY2029E "
                    "(July year-end). The DCF terminal capex is a team decision: compare it with this benchmark.",
                    "FY1-FY3 = FY2026E-FY2028E; Smucker FY2027E-FY2029E (cierre en abril); Campbell's FY2027E-FY2029E "
                    "(cierre en julio). El capex terminal del DCF es decisión del equipo: compárenlo con esta referencia."),
    "pa_n4": ("NTM and STM: CIQ consensus calendarised from the pricing date with fiscal-year day weights "
              "(STM = the 12 months after NTM).", "NTM y STM: consenso de CIQ calendarizado desde la fecha de "
              "precios con pesos por días del año fiscal (STM = los 12 meses posteriores a NTM)."),
    "data_usd": ("Data in ($M)", "Cifras en millones de USD"),
    "mkt": ("Market Data", "Datos de mercado"),
    "fin": ("Financials ($M)", "Financieros (millones de USD)"),
    "ratios": ("Ratios & Margins", "Razones y márgenes"),
    "perf": ("Performance Valuations", "Valuación por desempeño"),
    "claim": ("Valuation on the claim basis (lease-normalised; drives the exit multiple in the DCF)",
              "Valuación con la base de reclamos (normalizada por arrendamientos; define el múltiplo de salida del DCF)"),
    "company": ("Company Name", "Empresa"),
    "group": ("Group", "Grupo"),
    "ticker": ("Exchange:Ticker", "Bolsa:Clave"),
    "price": ("Share Price ($)", "Precio por acción (USD)"),
    "hi": ("Price High ($)", "Precio máximo (USD)"),
    "lo": ("Price Low ($)", "Precio mínimo (USD)"),
    "mc": ("Market Cap. ($M)", "Valor de mercado (millones de USD)"),
    "ev": ("Enterprise Value ($M)", "Valor de la empresa (millones de USD)"),
    "pp": ("Price Performance (%)", "Desempeño del precio (%)"),
    "dps": ("Dividends per share", "Dividendo por acción"),
    "w52": ("52W", "52 sem"),
    "rev": ("Total revenue", "Ventas totales"),
    "gp": ("Gross Profit / (loss)", "Utilidad bruta"),
    "eyoy": ("EBITDA, YoY (%)", "EBITDA, crecimiento anual (%)"),
    "fcfy": ("Free Cash Flow Yield (%)", "Rendimiento de flujo libre (%)"),
    "ps": ("Price / Sales (x)", "Precio / ventas (x)"),
    "pfcf": ("Price / Free Cash Flow (x)", "Precio / flujo libre (x)"),
    "subject": ("Subject Company >>", "Empresa analizada >>"),
    "core": ("Core", "Núcleo"),
    "secondary": ("Secondary", "Secundario"),
    "evebitda_ltm": ("EV/EBITDA LTM (x)", "EV/EBITDA LTM (x)"),
    "evebitda_ntm": ("EV/EBITDA NTM (x)", "EV/EBITDA NTM (x)"),
    "evsales": ("EV/Sales LTM (x)", "EV/ventas LTM (x)"),
    "pe_ltm": ("P/E LTM (x)", "P/U LTM (x)"),
    "pe_ntm": ("P/E NTM (x)", "P/U NTM (x)"),
    "nd_ebitda": ("Net debt / EBITDA LTM (x)", "Deuda neta / EBITDA LTM (x)"),
    "margin": ("EBITDA margin LTM", "Margen EBITDA LTM"),
    "elig": ("In median: valuation", "En la mediana: valuación"),
    "elig_pe": ("In median: P/E", "En la mediana: P/U"),
    "core_med": ("Core median (eligible)", "Mediana del núcleo (elegibles)"),
    "all_med": ("All-peer median (eligible)", "Mediana de todos los pares (elegibles)"),
    "all_mean": ("All-peer mean (eligible)", "Promedio de todos los pares (elegibles)"),
    "all_n": ("All-peer: number eligible", "Todos los pares: número de elegibles"),
    "src_pa": ("Source: S&P Capital IQ Pro (Task 1A/2A/2B pulls, 15/16-Oct-2026), SEC XBRL filings and company "
               "reports; compiled in Inputs_Sources and Detail_PeerAnalysis.",
               "Fuente: S&P Capital IQ Pro (consultas 1A/2A/2B, 15/16-oct-2026), reportes XBRL de la SEC y de las "
               "empresas; compilado en Inputs_Sources y Detail_PeerAnalysis."),
}
TS_ROWS = [  # (row, key, EN label, ES label, CIQ metric, detail row or None, kind)
    (28, "sales", "Sales", "Ventas", "Total revenue", 7, "m"),
    (29, "sales_g", " - growth YoY", " - crecimiento anual", "", None, "p"),
    (30, "gp", "Gross Profit", "Utilidad bruta", "Gross Profit / (loss)", 9, "m"),
    (31, "sga", "SG&A", "Gastos de venta y administración", "Selling, general and administrative expenses", 12, "m"),
    (32, "opex", "Operating Expenses", "Gastos de operación", "Total operating expenses", 14, "m"),
    (33, "ebit", "EBIT", "EBIT", "Operating income/(loss), company basis", 16, "m"),
    (34, "ebitda", "EBITDA", "EBITDA", "Adjusted EBITDA, company (IFRS 16)", 19, "m"),
    (35, "pbt", "Pre tax profit", "Utilidad antes de impuestos", "Income from continuing operations before taxes", 21, "m"),
    (36, "npat", "NPAT", "Utilidad neta", "Net income to majority", 22, "m"),
    (37, "eps", "EPS", "UPA", "EPS, basic, total (E: normalised)", 24, "eps"),
    (38, "eps_g", " - growth YoY", " - crecimiento anual", "", None, "p"),
    (39, "dps", "DPS", "Dividendo por acción", "Dividend per share", 25, "eps"),
    (42, "cash", "Cash and Equivalents", "Caja y equivalentes", "Cash and short-term investments", 28, "m"),
    (43, "ca", "Current Assets", "Activo circulante", "Total current assets", 29, "m"),
    (44, "nca", "Non-Current Assets", "Activo no circulante", "Total non-current assets", 31, "m"),
    (45, "cl", "Current Liabilities", "Pasivo circulante", "Total current liabilities", 32, "m"),
    (46, "ncl", "Non-Current Liabilities", "Pasivo no circulante", "Total non-current liabilities", 34, "m"),
    (47, "nd", "Net Debt", "Deuda neta", "Net debt (A: CIQ incl. IFRS 16 leases; E: consensus)", 37, "m"),
    (50, "capex", "Capex", "Inversión de capital (capex)", "Capital expenditures", 42, "m"),
    (51, "dwc", "Change in working capital", "Cambio en capital de trabajo", "(Increase)/decrease in working capital", 46, "m"),
    (52, "cfo", "Net cash flow from operations", "Flujo neto de operación", "Net cash flows from operating activities", 41, "m"),
    (53, "cfi", "Net cash flow from investing activities", "Flujo neto de inversión", "Net cash flows from investing activities", 44, "m"),
    (54, "cff", "Net cash flow from financing activities", "Flujo neto de financiamiento", "Net cash flows from financing activities", 45, "m"),
    (57, "gm", "Gross margin", "Margen bruto", "Gross margin", None, "p"),
    (58, "sga_s", "SG&A / Sales", "Gastos de venta y adm. / ventas", "SG&A / Sales", None, "p"),
    (59, "om", "Operating margin", "Margen de operación", "Operating margin", None, "p"),
    (60, "em", "EBITDA margin", "Margen EBITDA", "EBITDA margin", None, "p"),
    (61, "nm", "Net margin", "Margen neto", "Net margin", None, "p"),
]
YEARS = [2023, 2024, 2025, 2026, 2027, 2028, 2029]
TS_COL = {y: 5 + i for i, y in enumerate(YEARS)}           # E..K
DETAIL_COL = {2023: "E", 2024: "F", 2025: "G", 2026: "H", 2027: "I", 2028: "J"}


def L(lang: str, key: str) -> str:
    en, es = T[key]
    return es if lang == "es" else en


# ---------------------------------------------------------------- data from the CIQ prompt 1 output and consensus
def ciq_prompt_extras(Y: dict | None = None) -> dict:
    """Peer history and consensus from data/capitaliq/capiq-ai-prompt1_2026-10-16.md (Task 2B tables), USD m,
    merged with the v3 template data (Capital IQ prompts 4-7) from peer_extras_v3.yaml."""
    rev23 = {"FLO": 5090.8, "YMZ": 8383.8, "ARYN": 2238.6, "SJM": 8529.2, "CPB": 9357.0, "MDLZ": 36016.0, "AC": 12179.4, "PEP": 91471.0}
    margin23 = {"FLO": 0.096, "YMZ": 0.071, "ARYN": 0.106, "SJM": 0.188, "CPB": 0.191, "MDLZ": 0.192, "AC": 0.193, "PEP": 0.184}
    lfcf24 = {"FLO": 157.0, "YMZ": 184.1, "ARYN": 161.6, "SJM": 590.5, "CPB": 576.8, "MDLZ": 2747.8, "AC": 864.2, "PEP": 7200.9}
    lfcf25 = {"FLO": 221.1, "YMZ": 168.9, "ARYN": 154.9, "SJM": 600.3, "CPB": 717.6, "MDLZ": 3588.0, "AC": 529.1, "PEP": 8232.8}
    cons3_rev = {"FLO": 5032.6, "YMZ": 8960.6, "ARYN": 2609.1, "MDLZ": 42656.1, "AC": 15637.8, "PEP": 105151.4}
    cons3_ebitda = {"FLO": 432.4, "YMZ": 765.9, "ARYN": 381.1, "MDLZ": 7700.3, "AC": 3234.2, "PEP": 20589.6}
    fy26_actual = {"SJM": (9050.9, 2024.7), "CPB": (9744.0, 1594.0)}   # FY2026 closed (CIQ consensus table 'A')
    X = {"rev23": rev23, "margin23": margin23, "lfcf24": lfcf24, "lfcf25": lfcf25, "cons3_rev": cons3_rev,
         "cons3_ebitda": cons3_ebitda, "fy26_actual": fy26_actual}
    t = (Y or {}).get("template") or {}
    gr = t.get("gruma") or {}
    if gr.get("rev") and gr.get("ebitda"):
        X["cons3_rev"] = {**cons3_rev, "GRUMA": gr["rev"][2]}
        X["cons3_ebitda"] = {**cons3_ebitda, "GRUMA": gr["ebitda"][2]}
    rev_c = t.get("rev_cons") or {}
    for k in ("SJM", "CPB"):            # FY3 revenue (FY2029E) from prompt 7 completes their STM revenue
        if k not in X["cons3_rev"] and rev_c.get(k) and rev_c[k][2] is not None:
            X["cons3_rev"] = {**X["cons3_rev"], k: rev_c[k][2]}
    for key in ("gruma", "px", "px_bimbo_mxn", "dps_ltm", "dps_fy24", "dps_fy25", "gp", "gp_ltm", "gm_cons", "fcf_cons",
                "dps_cons", "capex_cons", "rev_cons", "fy_labels"):
        X[key] = t.get(key) or {}
    X["sources"] = (Y or {}).get("sources") or {}
    return X


def bimbo_consensus(project: Path) -> dict:
    """Consensus mean (MXN m; per share in MXN) from data/capitaliq/consensus.csv."""
    want = {"Revenue": "rev", "EBITDA": "ebitda", "EBIT": "ebit", "Net Income Normalized": "ni", "EPS Normalized": "eps",
            "Dividend per share": "dps", "Capital Expenditures": "capex", "Cash From Operations": "cfo",
            "Free Cash Flow": "fcf", "Net Debt": "nd", "Gross Margin (%)": "gm",
            "Selling, General and Administrative Expense": "sga"}
    out: dict[str, dict[int, float]] = {v: {} for v in want.values()}
    with (project / "data" / "capitaliq" / "consensus.csv").open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            m = want.get(r["metric"])
            if not m or not r["stat"].startswith("Actual (A) / Consensus mean") or not r["period"].startswith("FY 20"):
                continue
            y = int(r["period"][3:7])
            try:
                v = float(r["value"])
            except ValueError:
                continue
            if r["unit"] == "Mex$000":
                v /= 1000.0
            out[m][y] = v
    return out


# ---------------------------------------------------------------- workbook surgery
SHEET_REF = re.compile(r"(?<![A-Za-z0-9_.])'?(TearSheet|PeerAnalysis)'?!")


def rename_detail_sheets(wb) -> None:
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("=") and SHEET_REF.search(c.value):
                    c.value = SHEET_REF.sub(lambda m: f"'Detail_{m.group(1)}'!", c.value)
    wb["TearSheet"].title = "Detail_TearSheet"
    wb["PeerAnalysis"].title = "Detail_PeerAnalysis"


def key_rows(ins) -> dict[str, int]:
    return {str(ins.cell(r, 1).value): r for r in range(1, ins.max_row + 1) if ins.cell(r, 1).value}


def set_input(ins, rows, key, value=None, tag=None, source=None, note=None, item=None):
    r = rows[key]
    if value is not None:
        ins.cell(r, 4).value = value
    if item is not None:
        ins.cell(r, 3).value = item
    if tag is not None:
        ins.cell(r, 7).value = tag
    if source is not None:
        ins.cell(r, 8).value = source
    if note is not None:
        ins.cell(r, 10).value = note


def apply_v2_input_changes(ins, rows, lang) -> None:
    es = lang == "es"
    set_input(ins, rows, "bmv_price", tag="sourced",
              source=("Cierre oficial BMV 16-oct-2026 = PPP 58.60 (último hecho 58.62), bmv.com.mx/es/emisoras/estadisticas/BIMBO-5163"
                      if es else "BMV official close 16-Oct-2026 = PPP 58.60 (last trade 58.62), bmv.com.mx/es/emisoras/estadisticas/BIMBO-5163"))
    src = ("Arrendamientos operativos no circulantes 609 (10-Q 30-jun-2026) + circulantes 164 (10-K 31-dic-2025, como "
           "aproximación) [assumption]" if es else
           "Noncurrent operating leases 609 (10-Q 30-Jun-2026) + current 164 (31-Dec-2025 10-K, proxy) [assumption]")
    set_input(ins, rows, "MDLZ.lease", value=773.0, tag="assumption", source=src)
    set_input(ins, rows, "MDLZ.op_liab", value=773.0, tag="assumption", source=src)
    set_input(ins, rows, "MDLZ.claims", value=(
        "Deuda financiera 21,450 (incluye arrendamientos financieros) + pasivos por arrendamiento operativo 773 (no "
        "circulantes 609 al 30-jun-26 + circulantes 164 al 31-dic-25 como aproximación) + NCI 53 - caja 1,716. CIQ EV + 164."
        if es else
        "Financial debt 21,450 (includes finance leases, not separated at 30-Jun-26; 423 at 31-Dec-25) + operating lease "
        "liabilities 773 (noncurrent 609 at 30-Jun-26 + current 164 at 31-Dec-25 as a proxy) + NCI 53 - cash 1,716. "
        "CIQ EV + 164."))


def apply_v3_overrides(ins, rows, Y: dict) -> tuple[list[str], dict[str, float]]:
    """Overrides from peer_extras_v3.yaml (calculator spec), applied by key after append_inputs() so that the
    section G keys exist. The pricing-date USD/MXN rate is held once (fx_mxn_spot) and every MXN conversion links
    to it. Price-performance keys have no input row (the front sheet computes them from the month-end prices), so
    their spec values come back as expected results for the Checks sheet. Returns (keys changed, expected perf)."""
    changed, perf_expected = [], {}
    fx = ((Y.get("fx") or {}).get("mxn_per_usd") or {})
    if fx.get("value") is not None:
        set_input(ins, rows, "fx_mxn_spot", value=float(fx["value"]), tag=fx.get("tag", "sourced"),
                  source=str(fx.get("source", "")))
        changed.append("fx_mxn_spot")
    for o in Y.get("overrides") or []:
        key = str(o.get("key"))
        if key not in rows:
            m = PERF_KEY.match(key)
            if m and m.group(1) in ORDER and isinstance(o.get("value"), (int, float)):
                perf_expected[key] = float(o["value"])
                continue
            raise SystemExit(f"peer_extras_v3.yaml override key not in Inputs_Sources: {key}")
        if key == "fx_mxn_spot":
            continue
        val = o.get("value")
        set_input(ins, rows, key, value=val if val is not None else "n/a", tag=o.get("tag"), source=o.get("source"))
        changed.append(key)
    r_fx = rows["fx_mxn_spot"]
    set_input(ins, rows, "fx_bmv_disp", value=f"=$D${r_fx}", tag="calc", source="Same rate as fx_mxn_spot (link)")
    for key in ("GRUMA.fx", "AC.fx"):          # MXN-quoted peers: one pricing-date rate, linked
        set_input(ins, rows, key, value=f"=1/$D${r_fx}", tag="calc", source="USD per MXN = 1 / fx_mxn_spot (link)")
    return changed, perf_expected


def _set_text(ws, coord: str, old_start: str, new: str) -> None:
    """Replace a v1 text only if it is still the one reviewed (guards against a silent overwrite)."""
    cur = ws[coord].value
    if not (isinstance(cur, str) and cur.startswith(old_start)):
        raise SystemExit(f"{ws.title}!{coord}: expected text starting {old_start!r}, found {str(cur)[:60]!r}")
    ws[coord].value = new


def apply_v3_texts(wb, rows, Y: dict) -> None:
    """v3 leftovers from the calculator spec (changes_vs_v2): Yamazaki and Arca descriptive EVs link to the Capital IQ
    net debt (their claim components are not available), the Checks dashboard test keeps the dashboard's own 17.46,
    and the v1 texts that still described the 17.46 rate or coordinator-supplied inputs are brought up to date.
    English only: the Spanish copy translates these cells through the --es-dict dictionary."""
    dp, ck, ins = wb["Detail_PeerAnalysis"], wb["Checks"], wb["Inputs_Sources"]
    dp["N14"] = f"=Inputs_Sources!$D${rows['YMZ.nd']}"
    dp["N19"] = f"=Inputs_Sources!$D${rows['AC.nd']}"
    claims = {str(o.get("key")): str(o.get("value")) for o in Y.get("overrides") or []}.get("ARYN.claims")
    _set_text(dp, "R14", "Not built:",
              "Descriptive only, not the claim basis: EV = market cap + Capital IQ net debt -473.5 (includes J-GAAP "
              "finance-lease obligations, JPY 7,853m; operating leases are off balance sheet; NCI not returned). "
              "Excluded from medians.")
    if claims:
        _set_text(dp, "R15", "CIQ basis, NOT verified:", claims)
    _set_text(dp, "R19", "Not built:",
              "Descriptive only, not the claim basis: EV = market cap + Capital IQ net debt 2,015.4 (includes IFRS 16 "
              "leases, MXN 1,832.2m; NCI not returned: the CIQ tool's 8.47x implies about MXN 19.9bn of claims missing "
              "from this EV). Excluded from medians.")
    _set_text(dp, "A6", "Bimbo price MXN 58.60",
              "Bimbo price MXN 58.60 (BMV official close 16-Oct-2026) and shares 4,294.9m (BMV notice 29-Jul-2026: "
              "4,294,943,715). USD columns convert at the pricing-date rate (Inputs_Sources fx_bmv_disp = fx_mxn_spot, "
              "MXN 18.479 per USD on 16-Oct-2026) for size only; multiples are computed in MXN.")
    _set_text(dp, "A7", "P/E for peers",
              "P/E for peers = CIQ multiples tool (NTM / LTM), EPS derived as price / P/E; Gruma = price / EPS (Capital "
              "IQ prompt 4: diluted EPS LTM and consensus FY2026E-FY2027E, day-weighted). Gross profit, dividends and "
              "price performance are on the front sheets (Capital IQ prompts 5-6); blank = not retrieved, never zero.")
    _set_text(dp, "A8", "Medians and means",
              "Medians and means use only peers with in-median flag = yes (AGGREGATE / SUMPRODUCT formulas; n/a cells "
              "are ignored). Core = Flowers, Gruma, Yamazaki, Aryzta; at present Yamazaki (lease basis) and Aryzta "
              "(NCI not verified) are excluded.")
    _set_text(dp, "T11", "Subject.",
              "Subject. Price: BMV official close 16-Oct-2026; shares: BMV notice 29-Jul-2026. EBITDA includes "
              "consolidated IO earnings.")
    for coord, start, new in (
            ("G8", "Exact: NCI 53 is the CIQ residual",
             "Exact except the current operating lease portion (164, 31-Dec-2025 proxy), which our claim basis adds "
             "(v2); NCI 53 is the CIQ residual"),
            ("G10", "Carried as the CIQ residual",
             "Lease split reconciled to CIQ total debt (791.2 + 195.7 = 986.9); the CIQ TEV residual -17.4 is kept "
             "(unexplained, not a book NCI); the 0.01 gap is the EUR conversion of the components")):
        _set_text(ck, coord, start, new)
    for r in range(1, ck.max_row + 1):
        a = ck.cell(r, 1).value
        if isinstance(a, str) and a.startswith("Consensus FY2026E EBITDA in USD at 17.46"):
            f = ck.cell(r, 2).value
            if not (isinstance(f, str) and f"Inputs_Sources!$D${rows['fx_bmv_disp']}" in f):
                raise SystemExit(f"Checks!B{r}: unexpected dashboard test formula {f!r}")
            ck.cell(r, 2).value = f.replace(f"Inputs_Sources!$D${rows['fx_bmv_disp']}", "17.46")
            ck.cell(r, 1).value = ("Consensus FY2026E EBITDA in USD at 17.46 (the rate implied in the CIQ dashboard, "
                                   "not the pricing-date rate) minus CIQ dashboard US$3,558.4m (should be about 0)")
            break
    else:
        raise SystemExit("Checks: dashboard test row not found")
    memo = {
        "Gross profit:": "Gross profit LTM: Capital IQ (prompt 6) for seven peers; Gruma (company report) and Mondelez "
                         "(SEC) unchanged and equal to CIQ; Campbell's and PepsiCo moved from the SEC calculations "
                         "(2,742 and 53,216) to the CIQ basis. Price performance: CIQ chart (prompt 5).",
        "Arca and Yamazaki:": "Yamazaki (lease basis fails under J-GAAP), Aryzta and Arca (NCI not verified) are excluded "
                              "from medians; their EVs are descriptive (Detail rows 14, 15 and 19). Shares and prices are "
                              "now sourced from Capital IQ (prompts 4-5).",
        "Gruma price is a delayed quote": "Gruma price is a delayed quote (Yahoo, 16-Oct-2026), corroborated by the CIQ "
                                          "chart within 0.05%; replace it with the BMV official close before the report.",
        "Bimbo price MXN 58.60": "Bimbo price MXN 58.60 (BMV official close 16-Oct-2026) and shares 4,294.9m (BMV notice "
                                 "29-Jul-2026) are sourced; each MXN 1 per share moves EV/EBITDA by about 0.07x.",
        "MXN per USD 17.46": "MXN per USD 18.479 (USD/MXN close 16-Oct-2026, Yahoo Finance MXN=X; the CIQ chart implies "
                             "about 18.49) is used for every MXN market value (Gruma and Arca prices; Bimbo USD display). "
                             "v1/v2 used 17.46, the rate implied in the CIQ consensus dashboard, not a pricing-date rate.",
        "CIQ's note of 0.055690": "CIQ's 0.055690 USD per MXN (17.957), stated for its LTM USD figures, is neither the "
                                  "30-Jun-2026 closing rate (17.47, company 2Q26 release) nor the 16-Oct rate (18.479); "
                                  "it is used only to put Arca's MXN lease figure on CIQ's USD basis.",
        "CIQ's USD net debt for Bimbo": "CIQ's USD net debt for Bimbo (9,907) implies 17.47 MXN per USD (173,116 / "
                                        "9,907): the 30-Jun-2026 balance-sheet rate, not the pricing-date rate.",
        "Consensus for peers is in USD": "Consensus for peers is in USD as converted by CIQ; Bimbo's MXN consensus against "
                                         "CIQ's USD values implies 17.46 for FY1 and about 18.50 for FY2-FY3, so NTM "
                                         "figures may differ from LTM by a few percent (Gruma: judgment_calls in "
                                         "valuation/inputs/peer_extras_v3.yaml).",
    }
    hit = set()
    for r in range(1, ck.max_row + 1):
        a = ck.cell(r, 1).value
        for start, new in memo.items():
            if isinstance(a, str) and a.startswith(start) and start not in hit:
                ck.cell(r, 1).value = new
                hit.add(start)
    if hit != set(memo):
        raise SystemExit(f"Checks memo rows not found: {sorted(set(memo) - hit)}")
    set_input(ins, rows, "bmv_shares", item="Shares outstanding (m)", tag="sourced",
              source="BMV notice 29-Jul-2026: 4,294,943,715 shares (valuation/inputs/spg_inputs.yaml shares_out); "
                     "4,294.9m used here (market cap -0.001% vs full precision). CIQ balance sheet 2026 FQ2 shows "
                     "4,296.3m (filing 2026-07-24)")
    for key in ("GRUMA.fx", "AC.fx"):
        set_input(ins, rows, key, note="Linked: 1 / fx_mxn_spot (USD/MXN 18.479 on 16-Oct-2026); v1/v2 used 17.46")
    set_input(ins, rows, "YMZ.price_local", note="TSE close 16-Oct-2026 (Yahoo Finance Japan, aggregator); CIQ chart within 0.07%")
    set_input(ins, rows, "AC.price_local", note="Quote 16-Oct-2026 (Yahoo, Rankia); CIQ chart within 0.05%; Yahoo 15-Oct close 206.85")


def apply_eligibility(wb, Y: dict) -> None:
    """In-median flags (valuation and P/E) and the eligibility note, per the calculator spec."""
    dp = wb["Detail_PeerAnalysis"]
    for e in Y.get("eligibility") or []:
        k = str(e.get("key"))
        if k not in ROW_A:
            raise SystemExit(f"peer_extras_v3.yaml eligibility key unknown: {k}")
        ra = ROW_A[k]
        dp[f"P{ra}"] = str(e.get("in_median", dp[f"P{ra}"].value))
        dp[f"Q{ra}"] = str(e.get("in_median_pe", dp[f"Q{ra}"].value))
        if e.get("note"):
            dp[f"T{ra}"] = str(e["note"])


def patch_gruma(wb, rows, X_rows) -> None:
    """Gruma now has consensus EBITDA, revenue and EPS (prompt 4C): wire them into the reviewed v1 calendarisation
    row and P/E inputs. Eligibility itself comes from the spec (apply_eligibility)."""
    if "GRUMA.eps_fy1" not in X_rows:
        return
    ins, dp = wb["Inputs_Sources"], wb["Detail_PeerAnalysis"]
    xr = lambda key: f"$D${X_rows[key]}"                                  # noqa: E731
    r_px, r_fx = rows["GRUMA.price_local"], rows["GRUMA.fx"]
    ins.cell(rows["GRUMA.pe_ltm"], 4).value = f'=IFERROR($D${r_px}*$D${r_fx}/{xr("GRUMA.eps_ltm")},"n/a")'
    ins.cell(rows["GRUMA.pe_ntm"], 4).value = (f"=IFERROR($D${r_px}*$D${r_fx}/('Detail_PeerAnalysis'!$D$62*{xr('GRUMA.eps_fy1')}"
                                               f"+'Detail_PeerAnalysis'!$E$62*{xr('GRUMA.eps_fy2')}),\"n/a\")")
    for key, txt in (("GRUMA.pe_ltm", "calc: price in USD / diluted EPS LTM USD 1.40 (Capital IQ, prompt 4B)"),
                     ("GRUMA.pe_ntm", "calc: price in USD / NTM EPS (FY2026E 1.40 and FY2027E 1.33 consensus, day-weighted; "
                                      "Capital IQ, prompt 4C)")):
        ins.cell(rows[key], 7).value = "calc"
        ins.cell(rows[key], 8).value = txt
    if "GRUMA.cons1_ebitda" in rows:
        dp["F62"] = f"=Inputs_Sources!$D${rows['GRUMA.cons1_ebitda']}"
    dp["G62"] = f"=Inputs_Sources!{xr('GRUMA.cons2_ebitda')}"
    dp["I62"] = f"=Inputs_Sources!{xr('GRUMA.cons1_rev')}"
    dp["J62"] = f"=Inputs_Sources!{xr('GRUMA.cons2_rev')}"
    dp["L62"] = f"=Inputs_Sources!{xr('GRUMA.eps_fy1')}"
    dp["M62"] = f"=Inputs_Sources!{xr('GRUMA.eps_fy2')}"
    dp["N62"] = '=IFERROR(D62*L62+E62*M62,"n/a")'
    dp["O62"] = ("CIQ consensus (prompt 4C, company EBITDA basis), USD as converted by Capital IQ at the query-date rate")


def append_inputs(ins, rows, lang, X, C) -> dict[str, int]:
    """Section G: template extras. Returns key -> row."""
    es = lang == "es"
    r = ins.max_row + 2
    ins.cell(r, 1).value = ("G. Extras de la plantilla (v3, 17-oct-2026): historia y consenso de pares (prompts 1 y 4-7 de "
                            "Capital IQ), consenso FY2029 de Bimbo y datos de mercado; vacío sombreado = no disponible"
                            if es else
                            "G. Template extras (v3, 17-Oct-2026): peer history and consensus (Capital IQ prompts 1 and 4-7), "
                            "Bimbo FY2029 consensus and market data; shaded blank = not available")
    ins.cell(r, 1).font = F_BOLD
    r += 1
    out: dict[str, int] = {}
    prompt = "data/capitaliq/capiq-ai-prompt1_2026-10-16.md"
    cons_src = "data/capitaliq/consensus.csv (CIQ consensus mean, 20-Sep-2026)"
    srcs = X.get("sources") or {}
    p4 = srcs.get("gruma") or "data/capitaliq/capiq-ai-model-gaps-4_2026-10-17.md Task 4C"

    def add(key, entity, item_en, item_es, value, unit, ccy, tag, source, note=""):
        nonlocal r
        vals = [key, entity, item_es if es else item_en, value, unit, ccy, tag, source, "2026-10-17", note]
        for j, v in enumerate(vals, start=1):
            c = ins.cell(r, j)
            c.value = v
            if j == 4:
                c.font = F_INPUT
                if v is None:
                    c.fill = FILL_PEND
        out[key] = r
        r += 1

    names = {k: str(ins.cell(rows[f"{k}.fye"], 2).value) for k in PEERS if f"{k}.fye" in rows}
    gr = X.get("gruma") or {}
    if gr.get("rev") and gr.get("ebitda") and gr.get("eps"):
        ent = names.get("GRUMA", "Gruma")
        for fld, en, sp, v in (("cons1_rev", "Revenue, consensus FY1 (FY2026E)", "Ventas, consenso FY1 (FY2026E)", gr["rev"][0]),
                               ("cons2_rev", "Revenue, consensus FY2 (FY2027E)", "Ventas, consenso FY2 (FY2027E)", gr["rev"][1]),
                               ("cons2_ebitda", "EBITDA, consensus FY2 (FY2027E)", "EBITDA, consenso FY2 (FY2027E)", gr["ebitda"][1]),
                               ("eps_fy1", "EPS normalised, consensus FY1 (USD)", "UPA normalizada, consenso FY1 (USD)", gr["eps"][0]),
                               ("eps_fy2", "EPS normalised, consensus FY2 (USD)", "UPA normalizada, consenso FY2 (USD)", gr["eps"][1]),
                               ("eps_ltm", "EPS diluted, LTM Jun-2026 (USD)", "UPA diluida, LTM jun-2026 (USD)", gr.get("eps_ltm"))):
            key = f"GRUMA.{fld}"
            if key in rows:          # already an Inputs_Sources key: the override sets it
                continue
            add(key, ent, en, sp, v, "USD m" if "eps" not in fld else "USD/share", "USD",
                "sourced" if v is not None else "pending", p4 if fld != "eps_ltm" else
                "data/capitaliq/capiq-ai-model-gaps-4_2026-10-17.md Task 4B")
        rows = {**rows, **{k_: v_ for k_, v_ in out.items()}}
    for k in PEERS:
        ent = names.get(k, k)
        if k in X["rev23"]:
            add(f"{k}.ebitda_fy23", ent, "EBITDA, FY2023 (reported, CIQ margin x revenue)", "EBITDA, FY2023 (reportado, margen CIQ x ventas)",
                round(X["rev23"][k] * X["margin23"][k], 1), "USD m", "USD", "calc",
                f"{prompt} Task 2B: revenue FY2023 {X['rev23'][k]:,.1f} x EBITDA margin {X['margin23'][k]:.1%} (margin rounded to 0.1 pp)")
        else:
            add(f"{k}.ebitda_fy23", ent, "EBITDA, FY2023", "EBITDA, FY2023", None, "USD m", "USD", "pending", "Not in the CIQ pull; pending CIQ refresh")
        if k in X["fy26_actual"]:
            rv, eb = X["fy26_actual"][k]
            add(f"{k}.rev_fy26", ent, "Revenue, FY2026 (actual: fiscal year closed)", "Ventas, FY2026 (real: año fiscal cerrado)", rv, "USD m", "USD", "sourced", f"{prompt} consensus table ('A')")
            add(f"{k}.ebitda_fy26", ent, "EBITDA, FY2026 (actual)", "EBITDA, FY2026 (real)", eb, "USD m", "USD", "sourced", f"{prompt} consensus table ('A')")
        elif f"{k}.cons1_rev" in rows:
            add(f"{k}.rev_fy26", ent, "Revenue, FY2026E (= consensus FY1)", "Ventas, FY2026E (= consenso FY1)", f"=Inputs_Sources!$D${rows[f'{k}.cons1_rev']}", "USD m", "USD", "calc", "Link to cons1_rev")
            add(f"{k}.ebitda_fy26", ent, "EBITDA, FY2026E (= consensus FY1)", "EBITDA, FY2026E (= consenso FY1)", f"=Inputs_Sources!$D${rows[f'{k}.cons1_ebitda']}", "USD m", "USD", "calc", "Link to cons1_ebitda")
        else:
            add(f"{k}.rev_fy26", ent, "Revenue, FY2026E", "Ventas, FY2026E", None, "USD m", "USD", "pending", "No consensus in the CIQ pull; pending CIQ refresh")
            add(f"{k}.ebitda_fy26", ent, "EBITDA, FY2026E", "EBITDA, FY2026E", None, "USD m", "USD", "pending", "No consensus in the CIQ pull; pending CIQ refresh")
        for fld, en, sp, src in (("cons3_rev", "Revenue, consensus FY3", "Ventas, consenso FY3", X["cons3_rev"]),
                                 ("cons3_ebitda", "EBITDA, consensus FY3", "EBITDA, consenso FY3", X["cons3_ebitda"])):
            v = src.get(k)
            s_ = (srcs.get("rev_cons") if (fld == "cons3_rev" and k in ("SJM", "CPB")) else
                  p4 if k == "GRUMA" else f"{prompt} consensus table (FY2028E)")
            add(f"{k}.{fld}", ent, en, sp, v, "USD m", "USD", "sourced" if v is not None else "pending",
                s_ if v is not None else "FY3 consensus not returned by Capital IQ")
        for fld, en, sp, src in (("lfcf_fy24", "Levered FCF, FY2024 (CIQ)", "Flujo libre apalancado, FY2024 (CIQ)", X["lfcf24"]),
                                 ("lfcf_fy25", "Levered FCF, FY2025 (CIQ)", "Flujo libre apalancado, FY2025 (CIQ)", X["lfcf25"])):
            v = src.get(k)
            add(f"{k}.{fld}", ent, en, sp, v, "USD m", "USD", "sourced" if v is not None else "pending",
                f"{prompt} Task 2B levered FCF table" if v is not None else "Not returned by Capital IQ")
        for fld, en, sp in (("w52_high", "Price high, 52 weeks (USD)", "Precio máximo, 52 semanas (USD)"),
                            ("w52_low", "Price low, 52 weeks (USD)", "Precio mínimo, 52 semanas (USD)"),
                            ("perf_1d", "Price performance 1D (%)", "Desempeño 1D (%)")):
            add(f"{k}.{fld}", ent, en, sp, None, "", "USD", "pending",
                "Not returned by Capital IQ (data/capitaliq/capiq-ai-model-gaps-5_2026-10-17.md)")
        pxs = (X.get("px") or {}).get(k) or [None] * len(PX_DATES)
        for d, v in zip(PX_DATES, pxs):
            add(f"{k}.px_{d}", ent, f"Share price USD, month-end {d}", f"Precio por acción USD, fin de mes {d}", v,
                "USD/share", "USD", "sourced" if v is not None else "pending",
                srcs.get("px") or "data/capitaliq/capiq-ai-model-gaps-5_2026-10-17.md chart table")
        for fld, en, sp, dct in (("dps", "Dividend per share, last 12 months (USD)", "Dividendo por acción, últimos 12 meses (USD)", "dps_ltm"),
                                 ("dps_fy24", "Dividend per share FY2024 (USD)", "Dividendo por acción FY2024 (USD)", "dps_fy24"),
                                 ("dps_fy25", "Dividend per share FY2025 (USD)", "Dividendo por acción FY2025 (USD)", "dps_fy25")):
            v = (X.get(dct) or {}).get(k)
            add(f"{k}.{fld}", ent, en, sp, v, "USD/share", "USD", "sourced" if v is not None else "pending",
                srcs.get(dct) or "data/capitaliq/capiq-ai-model-gaps-5_2026-10-17.md")
        gpv = (X.get("gp") or {}).get(k) or [None, None]
        for i, fld in enumerate(("gp_fy24", "gp_fy25")):
            add(f"{k}.{fld}", ent, f"Gross profit, FY20{24 + i}", f"Utilidad bruta, FY20{24 + i}", gpv[i], "USD m", "USD",
                "sourced" if gpv[i] is not None else "pending",
                srcs.get("gp") or "data/capitaliq/capiq-ai-model-gaps-6_2026-10-17.md Task 6A")
        for dct, en, sp, unit in (("gm_cons", "Gross margin, consensus", "Margen bruto, consenso", "%"),
                                  ("fcf_cons", "Free cash flow, consensus", "Flujo libre, consenso", "USD m"),
                                  ("dps_cons", "Dividend per share, consensus", "Dividendo por acción, consenso", "USD/share"),
                                  ("capex_cons", "Capex, consensus", "Capex, consenso", "USD m"),
                                  ("rev_cons", "Revenue, consensus (prompt 7)", "Ventas, consenso (prompt 7)", "USD m")):
            vals = (X.get(dct) or {}).get(k) or [None, None, None]
            for i in range(3):
                v = vals[i] if i < len(vals) else None
                add(f"{k}.{dct}_{i + 1}", ent, f"{en} FY{i + 1}", f"{sp} FY{i + 1}", v, unit, "USD",
                    "sourced" if v is not None else "pending", srcs.get(dct) or "data/capitaliq/capiq-ai-model-gaps-6/7_2026-10-17.md")
    ent = "Grupo Bimbo"
    for y in (2026, 2027, 2028, 2029):
        for fld, en, sp, unit in (("rev", "Revenue", "Ventas", "MXN m"), ("ebitda", "EBITDA (company basis)", "EBITDA (base empresa)", "MXN m"),
                                  ("ebit", "EBIT (company basis)", "EBIT (base empresa)", "MXN m"),
                                  ("ni", "Net income, normalised", "Utilidad neta normalizada", "MXN m"),
                                  ("eps", "EPS, normalised", "UPA normalizada", "MXN/share"), ("dps", "Dividend per share", "Dividendo por acción", "MXN/share"),
                                  ("capex", "Capital expenditures", "Inversión de capital", "MXN m"), ("cfo", "Cash from operations", "Flujo de operación", "MXN m"),
                                  ("fcf", "Free cash flow (consensus definition)", "Flujo libre (definición de consenso)", "MXN m"),
                                  ("nd", "Net debt (consensus definition)", "Deuda neta (definición de consenso)", "MXN m"),
                                  ("gm", "Gross margin (%)", "Margen bruto (%)", "%"), ("sga", "SG&A", "Gastos de venta y administración", "MXN m")):
            v = C[fld].get(y)
            add(f"BIMBO.cons_{fld}_{y}", ent, f"{en}, FY{y}E consensus", f"{sp}, consenso FY{y}E", v, unit, "MXN",
                "sourced" if v is not None else "pending", cons_src if v is not None else "Not in consensus.csv")
    add("BIMBO.w52_high", ent, "Price high, 52 weeks (MXN)", "Precio máximo, 52 semanas (MXN)", 68.67, "MXN", "MXN", "sourced", "CIQ corporate_issuance.csv, as of 06-Oct-2026")
    add("BIMBO.w52_low", ent, "Price low, 52 weeks (MXN)", "Precio mínimo, 52 semanas (MXN)", 53.03, "MXN", "MXN", "sourced", "CIQ corporate_issuance.csv, as of 06-Oct-2026")
    add("BIMBO.perf_1d", ent, "Price performance 1D (%)", "Desempeño 1D (%)", 0.010868, "%", "MXN", "sourced", "BMV estadísticas BIMBO serie A, 16-Oct-2026: 58.60 vs 57.97")
    pxb = X.get("px_bimbo_mxn") or [None] * len(PX_DATES)
    for d, v in zip(PX_DATES, pxb):
        add(f"BIMBO.px_{d}", ent, f"Share price MXN, month-end {d}", f"Precio por acción MXN, fin de mes {d}", v,
            "MXN/share", "MXN", "sourced" if v is not None else "pending",
            srcs.get("px_bimbo_mxn") or "data/market/bimbo_ipc_monthly_2021-11_2026-10.csv; 29-Oct-2021 Capital IQ")
    add("BIMBO.dps_ltm", ent, "Dividend paid, last 12 months (MXN)", "Dividendo pagado, últimos 12 meses (MXN)", 1.075, "MXN/share", "MXN", "sourced", "Paid 13-May-2026 (valuation/inputs/wacc_inputs.yaml C1-C4)")
    return out


def build_tearsheet(wb, lang, X_rows) -> None:
    ws = wb.create_sheet("TearSheet", 0)
    ws.sheet_view.showGridLines = False
    for col, w in {"A": 2, "B": 34, "C": 44, "D": 2, "L": 70}.items():
        ws.column_dimensions[col].width = w
    for y, ci in TS_COL.items():
        ws.cell(1, ci).value = None
        ws.column_dimensions[ws.cell(1, ci).column_letter].width = 12
    es = lang == "es"
    ws["B2"].value = L(lang, "ts_title"); ws["B2"].font = F_TITLE
    ws["B4"].value = L(lang, "setup"); ws["B4"].font = F_BOLD
    setup = [(5, "step1", "BMV:BIMBO A"), (8, "step2", "FY2025"), (11, "step3", "2026-10-16"), (14, "step4", L(lang, "v_ccy")),
             (16, "step5", L(lang, "v_mag")), (18, "step6", L(lang, "v_src")), (21, "step7", L(lang, "v_refresh"))]
    for r, k, v in setup:
        ws.cell(r, 2).value = L(lang, k)
        ws.cell(r, 5).value = v
        ws.cell(r, 5).font = F_INPUT
    ws["H5"].value = L(lang, "notes"); ws["H5"].font = F_BOLD
    ws["H6"].value = L(lang, "note1"); ws["H6"].font = F_NOTE
    ws["H7"].value = L(lang, "note2"); ws["H7"].font = F_NOTE
    ws["B25"].value = "Grupo Bimbo, S.A.B. de C.V."; ws["B25"].font = F_TITLE
    ws["K25"].value = L(lang, "data_in"); ws["K25"].font = F_NOTE
    for y, ci in TS_COL.items():
        ws.cell(26, ci).value = "A" if y <= 2025 else "E"
        ws.cell(26, ci).alignment = Alignment(horizontal="right")
        h = ws.cell(27, ci)
        h.value = f"FY{y}"
        h.font = F_HDR
        h.fill = FILL_HDR
        h.alignment = Alignment(horizontal="right")
    for r, key in ((27, "is"), (41, "bs"), (49, "cf"), (56, "mr")):
        ws.cell(r, 2).value = L(lang, key)
        for c in range(2, 13):
            ws.cell(r, c).fill = FILL_HDR if r == 27 else FILL_SUB
        ws.cell(r, 2).font = F_HDR if r == 27 else F_BOLD
    ws.cell(27, 12).value = L(lang, "tag"); ws.cell(27, 12).font = F_HDR
    D = "'Detail_TearSheet'!"
    I = "Inputs_Sources!"

    def cons(fld, y):
        return f"{I}$D${X_rows[f'BIMBO.cons_{fld}_{y}']}"

    for (r, key, en, sp, metric, drow, kind) in TS_ROWS:
        ws.cell(r, 2).value = sp if es else en
        ws.cell(r, 3).value = metric
        ws.cell(r, 3).font = F_NOTE
        for y, ci in TS_COL.items():
            col = ws.cell(r, ci).column_letter
            prev = ws.cell(r, ci - 1).column_letter
            f = None
            if key == "sales_g":
                f = f'=IFERROR({col}28/{prev}28-1,"")' if y > 2023 else f'=IFERROR({col}28/{D}D7-1,"")'
            elif key == "eps_g":
                f = f'=IFERROR({col}37/{prev}37-1,"")' if y > 2023 else f'=IFERROR({col}37/{D}D24-1,"")'
            elif key in ("gm", "sga_s", "om", "em", "nm"):
                num = {"gm": 30, "sga_s": 31, "om": 33, "em": 34, "nm": 36}[key]
                f = f'=IFERROR({col}{num}/{col}28,"")'
            elif y <= 2028 and drow is not None:
                d = f"{D}{DETAIL_COL[y]}{drow}"
                if key == "gp" and y >= 2026:
                    f = f'=IFERROR({col}28*{D}{DETAIL_COL[y]}11/100,"")'
                elif key == "opex" and y >= 2026:
                    f = f'=IFERROR({col}30-{col}33,"")'
                elif key == "nd" and y >= 2026:
                    f = f"={cons('nd', y)}"
                elif key == "cfo" and y >= 2026:
                    f = f"={cons('cfo', y)}"
                elif key in ("cash", "ca", "nca", "cl", "ncl", "dwc", "cfi", "cff") and y >= 2026:
                    f = None
                else:
                    f = f'=IF(ISNUMBER({d}),{d},"")'
            elif y == 2029:
                f = {"sales": f"={cons('rev', 2029)}", "gp": f'=IFERROR({col}28*{cons("gm", 2029)}/100,"")',
                     "sga": f"={cons('sga', 2029)}", "opex": f'=IFERROR({col}30-{col}33,"")', "ebit": f"={cons('ebit', 2029)}",
                     "ebitda": f"={cons('ebitda', 2029)}", "npat": f"={cons('ni', 2029)}", "eps": f"={cons('eps', 2029)}",
                     "dps": f"={cons('dps', 2029)}", "nd": f"={cons('nd', 2029)}", "capex": f"=-{cons('capex', 2029)}"}.get(key)
            c = ws.cell(r, ci)
            if f is None:
                c.fill = FILL_PEND
                continue
            c.value = f.replace('""', '"n/a"')     # an empty-string result would read as a missing value
            c.number_format = FMT[kind]
            c.font = F_LINK if f.startswith(f"={D}") or f.startswith(f"=IF(ISNUMBER({D}") else F_NORM
        tag = {"sales_g": "[calc]", "eps_g": "[calc]", "gm": "[calc]", "sga_s": "[calc]", "om": "[calc]", "em": "[calc]", "nm": "[calc]"}.get(key)
        if tag is None:
            tag = ("[sourced] A: Detail_TearSheet (CIQ / filings); E: CIQ consensus mean" if not es else
                   "[sourced] A: Detail_TearSheet (CIQ / reportes); E: promedio de consenso CIQ")
            if key == "gp":
                tag += "; E = revenue x consensus gross margin [calc]" if not es else "; E = ventas x margen bruto de consenso [calc]"
            if key == "opex":
                tag += "; E = gross profit - EBIT [calc]" if not es else "; E = utilidad bruta - EBIT [calc]"
            if key == "nd":
                tag += ("; E = consensus net debt (broker definition; FY25A 149,031 vs 182,232 incl. leases)" if not es else
                        "; E = deuda neta de consenso (definición de los analistas; FY25A 149,031 vs 182,232 con arrendamientos)")
            if key in ("cash", "ca", "nca", "cl", "ncl", "dwc", "cfi", "cff", "pbt"):
                tag += "; E: not in CIQ consensus" if not es else "; E: no está en el consenso de CIQ"
        ws.cell(r, 12).value = tag
        ws.cell(r, 12).font = F_NOTE
    ws["B63"].value = L(lang, "src_line"); ws["B63"].font = F_NOTE
    ch = BarChart()
    ch.type = "col"
    ch.title = L(lang, "chart")
    ch.y_axis.title = "MXN m"
    data = Reference(ws, min_col=5, max_col=11, min_row=28, max_row=28)
    data2 = Reference(ws, min_col=5, max_col=11, min_row=34, max_row=34)
    cats = Reference(ws, min_col=5, max_col=11, min_row=27, max_row=27)
    ch.add_data(data, from_rows=True, titles_from_data=False)
    ch.add_data(data2, from_rows=True, titles_from_data=False)
    ch.series[0].tx = None
    ch.set_categories(cats)
    from openpyxl.chart.series import SeriesLabel
    ch.series[0].tx = SeriesLabel(v=("Ventas" if es else "Sales"))
    ch.series[1].tx = SeriesLabel(v="EBITDA")
    ch.height, ch.width = 7.5, 16
    ws.add_chart(ch, "N27")
    ws.freeze_panes = "E28"


def build_peer_sheet(wb, lang, rows, X_rows) -> None:
    ws = wb.create_sheet("PeerAnalysis", 1)
    ws.sheet_view.showGridLines = False
    es = lang == "es"
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 34
    ws.column_dimensions["C"].width = 2
    ws.column_dimensions["D"].width = 11
    ws.column_dimensions["E"].width = 18
    for ci in range(6, 24):
        ws.column_dimensions[ws.cell(1, ci).column_letter].width = 11
    ws["B2"].value = L(lang, "pa_title"); ws["B2"].font = F_TITLE
    ws["B4"].value = L(lang, "notes"); ws["B4"].font = F_BOLD
    for i, k in enumerate(("pa_n1", "pa_n2", "pa_n3", "pa_n4")):
        ws.cell(5 + i, 2).value = L(lang, k)
        ws.cell(5 + i, 2).font = F_NOTE
    ws["B9"].value = L(lang, "data_usd"); ws["B9"].font = F_NOTE
    DP = "'Detail_PeerAnalysis'!"
    DT = "'Detail_TearSheet'!"
    I = "Inputs_Sources!"
    order = PEERS + ["BIMBO"]

    def inp(k, fld):
        key = f"{k}.{fld}"
        return f"{I}$D${X_rows[key]}" if key in X_rows else (f"{I}$D${rows[key]}" if key in rows else None)

    def head(r, title):
        ws.cell(r, 6).value = title
        for c in range(2, 24):
            ws.cell(r, c).fill = FILL_SUB
        ws.cell(r, 6).font = F_BOLD

    def ident(r, k):
        ra = ROW_A[k]
        ws.cell(r, 2).value = f"={DP}A{ra}"
        ws.cell(r, 4).value = L(lang, "subject") if k == "BIMBO" else L(lang, "core" if ra in (12, 13, 14, 15) else "secondary")
        ws.cell(r, 5).value = f"={DP}B{ra}"
        for c in (2, 5):
            ws.cell(r, c).font = F_LINK

    def put(r, c, formula, fmt):
        cell = ws.cell(r, c)
        if formula is None:
            cell.fill = FILL_PEND
            return
        cell.value = formula.replace('""', '"n/a"')   # an empty-string result would read as a missing value
        cell.number_format = FMT[fmt]
        cell.alignment = Alignment(horizontal="right")

    # ---- block 1: market data
    head(10, L(lang, "mkt"))
    hdr = {6: L(lang, "price"), 7: L(lang, "hi"), 8: L(lang, "lo"), 9: L(lang, "mc"), 10: L(lang, "ev"), 11: L(lang, "pp"), 18: L(lang, "dps")}
    for c, t in hdr.items():
        ws.cell(11, c).value = t
        ws.cell(11, c).font = F_BOLD
        ws.cell(11, c).alignment = Alignment(wrap_text=True, vertical="top")
    sub = {2: L(lang, "company"), 4: L(lang, "group"), 5: L(lang, "ticker"), 7: L(lang, "w52"), 8: L(lang, "w52"),
           11: "1D", 12: "1Y", 13: "2Y", 14: "3Y", 15: "5Y", 16: "QTD", 17: "YTD"}
    for c, t in sub.items():
        ws.cell(12, c).value = t
        ws.cell(12, c).font = F_HDR
    for c in range(2, 19):
        ws.cell(12, c).fill = FILL_HDR
    FXR = f"{I}$D${rows['fx_mxn_spot']}"                     # USD/MXN at the pricing date (one cell)
    perf_col = PERF_COL
    for i, k in enumerate(order):
        r = 13 + i
        ra = ROW_A[k]
        ident(r, k)
        put(r, 6, f'=IFERROR({DP}F{ra}*{DP}H{ra},"")', "px")
        if k == "BIMBO":
            put(r, 7, f"={inp(k, 'w52_high')}/{FXR}", "px")
            put(r, 8, f"={inp(k, 'w52_low')}/{FXR}", "px")
            put(r, 11, f'=IF(ISNUMBER({inp(k, "perf_1d")}),{inp(k, "perf_1d")},"")', "p")
        else:
            put(r, 7, None, "px")
            put(r, 8, None, "px")
            put(r, 11, None, "p")
        now = inp(k, f"px_{PX_DATES[0]}")
        for fld, base_i in PERF:      # Bimbo in MXN; peers in USD (Capital IQ chart)
            base = inp(k, f"px_{PX_DATES[base_i]}")
            put(r, perf_col[fld], (f'=IF(AND(ISNUMBER({now}),ISNUMBER({base})),{now}/{base}-1,"")'
                                   if now and base else None), "p")
        if k == "BIMBO":
            put(r, 18, f"={inp(k, 'dps_ltm')}/{FXR}", "eps")
        else:
            d = inp(k, "dps")
            put(r, 18, f'=IF(ISNUMBER({d}),{d},"")' if d else None, "eps")
    # ---- block 2: financials
    r0 = 27
    ws.cell(r0, 18).value = L(lang, "eyoy")
    ws.cell(r0, 18).font = F_BOLD
    head(28, L(lang, "fin"))
    ws.cell(28, 18).value = L(lang, "ratios"); ws.cell(28, 18).font = F_BOLD
    periods = ["FY2024", "FY2025", "FY2026", "LTM", "NTM", "STM"]
    for g, start in enumerate((6, 12, 18)):
        for j, p in enumerate(periods):
            c = ws.cell(29, start + j)
            c.value = p
            c.font = F_HDR
            c.fill = FILL_HDR
    for c, t in {2: L(lang, "company"), 4: L(lang, "group"), 5: L(lang, "ticker"), 6: L(lang, "rev"), 12: L(lang, "gp"), 18: L(lang, "eyoy")}.items():
        ws.cell(30, c).value = t
        ws.cell(30, c).font = F_BOLD
    for i, k in enumerate(order):
        r = 31 + i
        rb, rc, ra = ROW_B[k], ROW_CAL[k], ROW_A[k]
        ident(r, k)
        if k == "BIMBO":
            fx = FXR
            rev = [f"={DP}B{rb}", f"={DP}C{rb}", f"={inp(k, 'cons_rev_2026')}/{fx}", f"={DP}D{rb}", f"={DP}E{rb}",
                   f"=({DP}D{rc}*{inp(k, 'cons_rev_2027')}+{DP}E{rc}*{inp(k, 'cons_rev_2028')})/{fx}"]
            gp = [f"={DT}F9/{fx}", f"={DT}G9/{fx}", f"={inp(k, 'cons_rev_2026')}*{inp(k, 'cons_gm_2026')}/100/{fx}", f"={DP}M{rb}",
                  f"=({DP}D{rc}*{inp(k, 'cons_rev_2026')}*{inp(k, 'cons_gm_2026')}+{DP}E{rc}*{inp(k, 'cons_rev_2027')}*{inp(k, 'cons_gm_2027')})/100/{fx}",
                  f"=({DP}D{rc}*{inp(k, 'cons_rev_2027')}*{inp(k, 'cons_gm_2027')}+{DP}E{rc}*{inp(k, 'cons_rev_2028')}*{inp(k, 'cons_gm_2028')})/100/{fx}"]
            eb = [f'=IFERROR({DT}F19/{DT}E19-1,"")', f'=IFERROR({DT}G19/{DT}F19-1,"")', f'=IFERROR({inp(k, "cons_ebitda_2026")}/{DT}G19-1,"")', None,
                  f'=IFERROR({DP}K{rb}/{DP}H{rb}-1,"")',
                  f'=IFERROR(({DP}D{rc}*{inp(k, "cons_ebitda_2027")}+{DP}E{rc}*{inp(k, "cons_ebitda_2028")})/({DP}H{rc})-1,"")']
        else:
            r26, e26, c3r, c3e = inp(k, "rev_fy26"), inp(k, "ebitda_fy26"), inp(k, "cons3_rev"), inp(k, "cons3_ebitda")
            c2r, c2e = inp(k, "cons2_rev"), inp(k, "cons2_ebitda")
            rev = [f"={DP}B{rb}", f"={DP}C{rb}", f'=IF(ISNUMBER({r26}),{r26},"")', f"={DP}D{rb}", f'=IF(ISNUMBER({DP}E{rb}),{DP}E{rb},"")',
                   (f'=IF(AND(ISNUMBER({c2r}),ISNUMBER({c3r})),{DP}D{rc}*{c2r}+{DP}E{rc}*{c3r},"")' if c2r else None)]
            g24, g25 = inp(k, "gp_fy24"), inp(k, "gp_fy25")
            gm1, gm2, gm3 = inp(k, "gm_cons_1"), inp(k, "gm_cons_2"), inp(k, "gm_cons_3")
            c1r = inp(k, "cons1_rev")
            fy1_is_26 = k not in ("SJM", "CPB")          # their FY1 consensus is FY2027E (fiscal year-ends Apr/Jul)
            gp = [f'=IF(ISNUMBER({g24}),{g24},"")', f'=IF(ISNUMBER({g25}),{g25},"")',
                  (f'=IF(AND(ISNUMBER({r26}),ISNUMBER({gm1})),{r26}*{gm1}/100,"")' if fy1_is_26 and gm1 else None),
                  f'=IF(ISNUMBER({DP}M{rb}),{DP}M{rb},"")',
                  (f'=IF(AND(ISNUMBER({c1r}),ISNUMBER({c2r}),ISNUMBER({gm1}),ISNUMBER({gm2})),'
                   f'({DP}D{rc}*{c1r}*{gm1}+{DP}E{rc}*{c2r}*{gm2})/100,"")' if (c1r and c2r and gm1) else None),
                  (f'=IF(AND(ISNUMBER({c2r}),ISNUMBER({c3r}),ISNUMBER({gm2}),ISNUMBER({gm3})),'
                   f'({DP}D{rc}*{c2r}*{gm2}+{DP}E{rc}*{c3r}*{gm3})/100,"")' if (c2r and c3r and gm2) else None)]
            e23 = inp(k, "ebitda_fy23")
            eb = [f'=IF(ISNUMBER({e23}),IFERROR({DP}F{rb}/{e23}-1,""),"")', f'=IFERROR({DP}G{rb}/{DP}F{rb}-1,"")',
                  f'=IF(ISNUMBER({e26}),IFERROR({e26}/{DP}G{rb}-1,""),"")', None,
                  f'=IFERROR({DP}K{rb}/{DP}H{rb}-1,"")',
                  (f'=IF(AND(ISNUMBER({c2e}),ISNUMBER({c3e})),IFERROR(({DP}D{rc}*{c2e}+{DP}E{rc}*{c3e})/{DP}K{rb}-1,""),"")'
                   if c2e else None)]
        for j in range(6):
            put(r, 6 + j, rev[j], "m")
            put(r, 12 + j, gp[j], "m")
            put(r, 18 + j, eb[j], "p")
    # ---- block 3: performance valuations
    ws.cell(45, 6).value = L(lang, "fcfy"); ws.cell(45, 12).value = L(lang, "ps"); ws.cell(45, 18).value = L(lang, "pfcf")
    for c in (6, 12, 18):
        ws.cell(45, c).font = F_BOLD
    head(47, L(lang, "perf"))
    for start in (6, 12, 18):
        for j, p in enumerate(periods):
            c = ws.cell(48, start + j)
            c.value = p
            c.font = F_HDR
            c.fill = FILL_HDR
    for c, t in {2: L(lang, "company"), 4: L(lang, "group"), 5: L(lang, "ticker")}.items():
        ws.cell(49, c).value = t
        ws.cell(49, c).font = F_BOLD
    for i, k in enumerate(order):
        r = 50 + i
        rb, rc, ra = ROW_B[k], ROW_CAL[k], ROW_A[k]
        rr = 31 + i                                      # this company's revenue row in block 2
        ident(r, k)
        mc = f"{DP}I{ra}"
        if k == "BIMBO":
            mcx = f"({I}$D${rows['bmv_price']}*{I}$D${rows['bmv_shares']})"   # market cap in MXN m
            fcf = [None, f"{DT}G48", f"{inp(k, 'cons_fcf_2026')}", f"{DP}N{rb}*{FXR}",
                   f"({DP}D{rc}*{inp(k, 'cons_fcf_2026')}+{DP}E{rc}*{inp(k, 'cons_fcf_2027')})",
                   f"({DP}D{rc}*{inp(k, 'cons_fcf_2027')}+{DP}E{rc}*{inp(k, 'cons_fcf_2028')})"]
            base = mcx
        else:
            f1, f2, f3 = inp(k, "fcf_cons_1"), inp(k, "fcf_cons_2"), inp(k, "fcf_cons_3")
            fy1_is_26 = k not in ("SJM", "CPB")
            fcf = [inp(k, "lfcf_fy24"), inp(k, "lfcf_fy25"), (f1 if fy1_is_26 else None), f"{DP}N{rb}",
                   (f"({DP}D{rc}*{f1}+{DP}E{rc}*{f2})" if f1 and f2 else None),
                   (f"({DP}D{rc}*{f2}+{DP}E{rc}*{f3})" if f2 and f3 else None)]
            base = mc
        for j in range(6):
            f = fcf[j]
            put(r, 6 + j, (f'=IFERROR(IF(ISNUMBER({f}),({f})/{base},""),"")' if f else None), "p")
            col = ws.cell(rr, 6 + j).column_letter
            put(r, 12 + j, f'=IFERROR({mc}/{col}{rr},"")', "x")
            put(r, 18 + j, (f'=IFERROR(IF(ISNUMBER({f}),IF(({f})>0,{base}/({f}),"n.m."),""),"")' if f else None), "x")
    # ---- extra block: claim-basis valuation (links to the reviewed v1 logic)
    r = 62
    head(r, L(lang, "claim"))
    r += 1
    cols = [(6, "evebitda_ltm", "B", "x"), (7, "evebitda_ntm", "C", "x"), (8, "evsales", "D", "x"), (9, "pe_ltm", "E", "x"),
            (10, "pe_ntm", "F", "x"), (11, "nd_ebitda", "H", "x"), (12, "margin", "I", "p")]
    for c, key, _, _ in cols:
        ws.cell(r, c).value = L(lang, key)
        ws.cell(r, c).font = F_BOLD
        ws.cell(r, c).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 13).value = L(lang, "elig"); ws.cell(r, 14).value = L(lang, "elig_pe")
    for c in (13, 14):
        ws.cell(r, c).font = F_BOLD
        ws.cell(r, c).alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
    for k in order:
        rc_, ra = ROW_C[k], ROW_A[k]
        ident(r, k)
        for c, _, dcol, fmt in cols:
            put(r, c, f'={DP}{dcol}{rc_}', fmt)
        ws.cell(r, 13).value = f'={DP}P{ra}'
        ws.cell(r, 14).value = f'={DP}Q{ra}'
        r += 1
    for label_key, drow in (("core_med", 50), ("all_med", 53), ("all_mean", 54), ("all_n", 55)):
        ws.cell(r, 2).value = L(lang, label_key)
        ws.cell(r, 2).font = F_BOLD
        for c, _, dcol, fmt in cols:
            put(r, c, f'={DP}{dcol}{drow}', "eps" if label_key == "all_n" else fmt)
        r += 1
    # ---- extra block: capital intensity (consensus capex / consensus revenue), the benchmark for terminal capex
    r += 1
    head(r, L(lang, "capint"))
    r += 1
    for j, p in enumerate(("FY1", "FY2", "FY3")):
        c = ws.cell(r, 6 + j)
        c.value = p
        c.font = F_HDR
        c.fill = FILL_HDR
    r += 1
    first_peer = r
    for k in PEERS:
        ident(r, k)
        for j in range(3):
            cx, rv = inp(k, f"capex_cons_{j + 1}"), inp(k, f"rev_cons_{j + 1}")
            put(r, 6 + j, f'=IF(AND(ISNUMBER({cx}),ISNUMBER({rv})),{cx}/{rv},"")' if cx and rv else None, "p")
        r += 1
    last_peer = r - 1
    ws.cell(r, 2).value = L(lang, "capint_med")
    ws.cell(r, 2).font = F_BOLD
    for j in range(3):
        cl = ws.cell(first_peer, 6 + j).column_letter
        put(r, 6 + j, f"=MEDIAN({cl}{first_peer}:{cl}{last_peer})", "p")
    wb._capint_cells = {"median_row": r}
    r += 1
    ident(r, "BIMBO")
    for j, y in enumerate((2026, 2027, 2028)):
        cx, rv = inp("BIMBO", f"cons_capex_{y}"), inp("BIMBO", f"cons_rev_{y}")
        put(r, 6 + j, f'=IF(AND(ISNUMBER({cx}),ISNUMBER({rv})),{cx}/{rv},"")', "p")
    wb._capint_cells["bimbo_row"] = r
    r += 1
    ws.cell(r, 2).value = L(lang, "capint_note")
    ws.cell(r, 2).font = F_NOTE
    r += 1
    ws.cell(r + 1, 2).value = L(lang, "src_pa")
    ws.cell(r + 1, 2).font = F_NOTE
    ws.freeze_panes = "F13"


EXPECTED_MEDIANS = [  # (spec key, Detail_PeerAnalysis cell, label)
    ("core_ev_ltm", "B50", "Core median EV/EBITDA LTM"), ("core_ev_ntm", "C50", "Core median EV/EBITDA NTM"),
    ("all_ev_ltm", "B53", "All-peer median EV/EBITDA LTM"), ("all_ev_ntm", "C53", "All-peer median EV/EBITDA NTM"),
    ("all_pe_ltm", "E53", "All-peer median P/E LTM"), ("all_pe_ntm", "F53", "All-peer median P/E NTM"),
]
EXPECTED_COMPANY = [("ev_ebitda_ltm", "B"), ("ev_ebitda_ntm", "C"), ("pe_ltm", "E"), ("pe_ntm", "F")]


def add_checks(wb, lang, Y: dict, perf_expected: dict | None = None) -> None:
    """Section 10: the rebuilt workbook against the calculator spec's expected values (same tolerance as the
    rest of the project, 1e-6 relative), then the v2 -> v3 change list."""
    ws = wb["Checks"]
    es = lang == "es"
    r = ws.max_row + 2
    ws.cell(r, 1).value = ("10. v3: resultados contra los valores esperados del cálculo independiente y cambios v2 -> v3" if es else
                           "10. v3: results against the independent calculation's expected values, and v2 -> v3 changes")
    ws.cell(r, 1).font = F_BOLD
    r += 1
    for j, h in enumerate(("Item", "Workbook", "Expected (spec)", "Flag", "v2")):
        ws.cell(r, 1 + j).value = h
        ws.cell(r, 1 + j).font = F_BOLD
    r += 1
    DP = "'Detail_PeerAnalysis'!"
    exp = (Y.get("expected") or {})
    med, med2 = exp.get("medians") or {}, exp.get("medians_v2") or {}
    items = []
    for key, cell, label in EXPECTED_MEDIANS:
        if med.get(key) is not None:
            items.append((label, f"={DP}{cell}", med[key], med2.get(key)))
    for k, d in (exp.get("per_company") or {}).items():
        if k not in ROW_C:
            continue
        for fld, col in EXPECTED_COMPANY:
            if isinstance(d.get(fld), (int, float)):
                items.append((f"{k} {fld}", f"={DP}{col}{ROW_C[k]}", d[fld], None))
    for key, val in sorted((perf_expected or {}).items()):     # price performance: front-sheet formulas vs spec
        k, fld = PERF_KEY.match(key).groups()
        col = wb["PeerAnalysis"].cell(1, PERF_COL[fld]).column_letter
        items.append((f"{k} {fld}", f"=PeerAnalysis!{col}{13 + ORDER.index(k)}", val, None))
    for label, formula, expected, v2 in items:
        ws.cell(r, 1).value = label
        ws.cell(r, 2).value = formula
        ws.cell(r, 3).value = expected
        ws.cell(r, 4).value = f'=IF(ISNUMBER(B{r}),IF(ABS(B{r}-C{r})<=0.000001*MAX(1,ABS(C{r})),"ok","FLAG"),"FLAG")'
        if v2 is not None:
            ws.cell(r, 5).value = v2
        r += 1
    wb._checks_rows = (r - len(items), r - 1)
    ws.cell(r, 1).value = ("Celdas de la plantilla con dato (TearSheet E28:K61 y PeerAnalysis F13:W59)" if es else
                           "Template cells filled (TearSheet E28:K61 and PeerAnalysis F13:W59)")
    ws.cell(r, 2).value = "=COUNT(TearSheet!E28:K61)+COUNT(PeerAnalysis!F13:W59)"
    r += 1
    ws.cell(r, 1).value = ("Celdas no disponibles (sombreadas, vacías)" if es else "Cells not available (shaded, blank)")
    ws.cell(r, 2).value = "=COUNTBLANK(PeerAnalysis!F13:W22)+COUNTBLANK(PeerAnalysis!F31:W40)+COUNTBLANK(PeerAnalysis!F50:W59)"
    r += 2
    ws.cell(r, 1).value = "Changes v2 -> v3 (calculator spec)"
    ws.cell(r, 1).font = F_BOLD
    r += 1
    for line in Y.get("changes_vs_v2") or []:
        ws.cell(r, 1).value = str(line)
        r += 1


def build(project: Path, lang: str, X: dict, C: dict, Y: dict, tr: dict | None) -> Path:
    src = project / "valuation" / "BIMBOA_PeerAnalysis_v1.xlsx"
    wb = load_workbook(src)
    rename_detail_sheets(wb)
    ins = wb["Inputs_Sources"]
    rows = key_rows(ins)
    apply_v2_input_changes(ins, rows, lang)
    X_rows = append_inputs(ins, rows, lang, X, C)
    _, perf_expected = apply_v3_overrides(ins, {**rows, **X_rows}, Y)    # by key, after section G exists
    patch_gruma(wb, rows, X_rows)
    apply_eligibility(wb, Y)
    apply_v3_texts(wb, rows, Y)
    build_tearsheet(wb, lang, X_rows)
    build_peer_sheet(wb, lang, rows, X_rows)
    add_checks(wb, lang, Y, perf_expected)
    if lang == "es" and tr:
        n = 0
        for _, c, v in list(tw.translatable(wb)):
            t = tr.get(v)
            if t:
                c.value = t
                n += 1
        print(f"  translated {n} detail cells")
    out = project / "valuation" / (f"BIMBOA_PeerAnalysis_v{VERSION}_ES.xlsx" if lang == "es"
                                   else f"BIMBOA_PeerAnalysis_v{VERSION}.xlsx")
    if out.name.upper().startswith("SPG_"):
        raise SystemExit("refusing to write over an S&P template")
    wb.save(out)
    return out


# ---------------------------------------------------------------- peers.yaml from the recalculated v2
NUM_FIELDS = ("price", "shares", "net_debt", "financial_debt", "lease_liabilities", "nci_book", "cash", "market_cap", "ev",
              "ebitda_ltm", "ebitda_fwd", "eps_fwd")


def _export_gate(wb, wbf, Y: dict) -> list[str]:
    """Problems that must stop the peers.yaml export.
    (1) Any formula without a cached result (workbook not recalculated); intentional 'n/a' results are cached text.
    (2) Checks section 10 must hold one passing row for every expected median in the spec.
    (3) EV-eligible peers need every claim component, price, shares, FX, EV and a positive LTM EBITDA, and must satisfy
        net debt = debt + leases + NCI - cash and EV = market cap + net debt; P/E-eligible peers need price, FX and a
        positive P/E LTM or NTM."""
    import math
    probs = []
    for ws in wbf.worksheets:
        wv = wb[ws.title]
        n_missing = 0
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("=") and wv[c.coordinate].value is None:
                    n_missing += 1
                    if n_missing <= 3:
                        probs.append(f"{ws.title}!{c.coordinate}: formula without a cached result")
        if n_missing > 3:
            probs.append(f"{ws.title}: {n_missing} formulas without cached results in total")
    dp, ck = wb["Detail_PeerAnalysis"], wb["Checks"]
    exp_keys = {label for key, _, label in EXPECTED_MEDIANS
                if ((Y.get("expected") or {}).get("medians") or {}).get(key) is not None}
    sec10, seen = False, set()
    for row in ck.iter_rows(min_row=1, max_row=ck.max_row, values_only=True):
        a = str(row[0] or "")
        if a.startswith("10. v3"):
            sec10 = True
            continue
        if sec10 and len(row) > 3 and isinstance(row[2], (int, float)):
            seen.add(a)
            if row[3] != "ok":
                probs.append(f"Checks: '{a}' is {row[3]!r}")
    if not sec10:
        probs.append("Checks section 10 not found")
    for lab in sorted(exp_keys - seen):
        probs.append(f"Checks section 10 has no comparison row for '{lab}'")
    if not exp_keys:
        probs.append("the spec has no expected medians to compare")

    def num(cell, positive=False):
        x = dp[cell].value
        ok = isinstance(x, (int, float)) and math.isfinite(float(x)) and (float(x) > 0 if positive else True)
        return float(x) if ok else None

    for k in PEERS:
        ra, rb, rc = ROW_A[k], ROW_B[k], ROW_C[k]
        if dp[f"P{ra}"].value == "yes":
            need = {"price": (f"F{ra}", True), "shares": (f"G{ra}", True), "FX": (f"H{ra}", True),
                    "market cap": (f"I{ra}", True), "financial debt": (f"J{ra}", False), "leases": (f"K{ra}", False),
                    "NCI": (f"L{ra}", False), "cash": (f"M{ra}", False), "net debt": (f"N{ra}", False),
                    "EV": (f"O{ra}", True), "EBITDA LTM": (f"J{rb}", True)}
            got = {}
            for what, (cell, pos) in need.items():
                got[what] = num(cell, pos)
                if got[what] is None:
                    probs.append(f"{k}: {what} ({cell}) is {dp[cell].value!r}")
            if all(v is not None for v in got.values()):
                nd = got["financial debt"] + got["leases"] + got["NCI"] - got["cash"]
                if abs(nd - got["net debt"]) > 1e-6 * max(1.0, abs(nd)):
                    probs.append(f"{k}: net debt {got['net debt']} != components {nd}")
                if abs(got["market cap"] + got["net debt"] - got["EV"]) > 1e-6 * max(1.0, got["EV"]):
                    probs.append(f"{k}: EV {got['EV']} != market cap + net debt")
        if dp[f"Q{ra}"].value == "yes":
            if num(f"F{ra}", True) is None or num(f"H{ra}", True) is None:
                probs.append(f"{k}: P/E-eligible without price or FX")
            if num(f"E{rc}", True) is None and num(f"F{rc}", True) is None:
                probs.append(f"{k}: P/E-eligible without a positive P/E LTM or NTM")
    return probs


def regen_peers_yaml(project: Path) -> int:
    import yaml
    src = project / "valuation" / f"BIMBOA_PeerAnalysis_v{VERSION}.xlsx"
    wb = load_workbook(src, data_only=True)
    wbf = load_workbook(src, data_only=False)
    probs = _export_gate(wb, wbf, load_extras(project))
    if probs:
        raise SystemExit("peers.yaml NOT written - recalculate the workbook and fix:\n  " + "\n  ".join(probs))
    dp = wb["Detail_PeerAnalysis"]

    def v(cell):
        x = dp[cell].value
        return x if isinstance(x, (int, float)) else None

    vals, flags = {}, {}
    for k in PEERS:
        ra, rb = ROW_A[k], ROW_B[k]
        fx = v(f"H{ra}")
        if fx is None or fx <= 0:
            raise SystemExit(f"peers.yaml NOT written - {k} FX (H{ra}) is missing; recalculate the workbook")
        price = v(f"F{ra}")
        eps = v(f"R{rb}")
        vals[k] = {"price": price * fx if price is not None else None, "shares": v(f"G{ra}"), "net_debt": v(f"N{ra}"),
                   "financial_debt": v(f"J{ra}"), "lease_liabilities": v(f"K{ra}"), "nci_book": v(f"L{ra}"), "cash": v(f"M{ra}"),
                   "market_cap": v(f"I{ra}"), "ev": v(f"O{ra}"), "ebitda_ltm": v(f"J{rb}"), "ebitda_fwd": v(f"L{rb}"),
                   "eps_fwd": eps * fx if eps is not None else None}
        flags[k] = {"in_median": str(dp[f"P{ra}"].value), "in_median_pe": str(dp[f"Q{ra}"].value)}
    path = project / "valuation" / "inputs" / "peers.yaml"
    text = path.read_text(encoding="utf-8").splitlines()
    out, key, changed = [], None, []
    for line in text:
        m = re.match(r"^  - key: \"(\w+)\"", line)
        if m:
            key = m.group(1)
        if line.startswith("subject:"):
            key = None
        m2 = re.match(r"^(    )(" + "|".join(NUM_FIELDS) + r"): ([^#\s]+)(\s*#.*)?$", line)
        if key in vals and m2:
            fld, old = m2.group(2), m2.group(3)
            new = vals[key][fld]
            try:
                oldv = None if old == "null" else float(old)
            except ValueError:
                oldv = None
            same = (new is None and oldv is None) or (new is not None and oldv is not None and abs(new - oldv) <= 1e-6 * max(1.0, abs(oldv)))
            if new is None and oldv is not None:
                if flags.get(key, {}).get("in_median") == "yes" and fld in ("price", "shares", "net_debt", "ev", "ebitda_ltm"):
                    raise SystemExit(f"peers.yaml NOT written - eligible {key} lost required field {fld}")
                line = f"{m2.group(1)}{fld}: {old}  # kept from the earlier export: v{VERSION} workbook cell is n/a"
                changed.append(f"{key}.{fld}: kept {old} (workbook cell is n/a; marked in the file)")
            elif not same:
                newtxt = "null" if new is None else f"{round(new, 6):.6f}".rstrip("0").rstrip(".")
                if newtxt and "." not in newtxt and newtxt != "null":
                    newtxt += ".0"
                line = f"{m2.group(1)}{fld}: {newtxt}" + (m2.group(4) or "")     # keep the provenance comment
                changed.append(f"{key}.{fld}: {old} -> {newtxt}")
        m3 = re.match(r'^(    )(in_median|in_median_pe): "(\w+)"', line)
        if key in flags and m3:
            new_flag = flags[key][m3.group(2)]
            if new_flag in ("yes", "no") and new_flag != m3.group(3):
                line = f'{m3.group(1)}{m3.group(2)}: "{new_flag}"'
                changed.append(f"{key}.{m3.group(2)}: {m3.group(3)} -> {new_flag}")
        if line.startswith("# Generated from valuation/BIMBOA_PeerAnalysis_v"):
            line = (f"# Generated from valuation/BIMBOA_PeerAnalysis_v{VERSION}.xlsx (Detail_PeerAnalysis) by valuation/build/"
                    "build_peer_workbook.py --peers-yaml after an Excel recalc. Change the inputs and re-run; do not edit by hand.")
            changed.append("header")
        if line.startswith('  price_tag: "[unverified]'):
            line = '  price_tag: "[sourced] BMV official close 16-Oct-2026 = PPP 58.60 (bmv.com.mx/es/emisoras/estadisticas/BIMBO-5163)"'
            changed.append("subject.price_tag")
        out.append(line)
    tmp = path.with_suffix(".yaml.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")   # keep the file's LF line endings
    doc = yaml.safe_load(tmp.read_text(encoding="utf-8"))                   # validate the complete export first
    for p in doc.get("peers") or []:
        if p.get("in_median") == "yes":
            for fld in ("price", "shares", "net_debt", "ev", "ebitda_ltm"):
                if not isinstance(p.get(fld), (int, float)) or p[fld] <= 0 and fld not in ("net_debt",):
                    tmp.unlink()
                    raise SystemExit(f"peers.yaml NOT written - eligible {p.get('key')} has invalid {fld}: {p.get(fld)!r}")
    tmp.replace(path)
    print("peers.yaml changes:", changed)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", default=".")
    ap.add_argument("--es-dict", default=None, help="JSON {English: Spanish} for the v1 detail sheets")
    ap.add_argument("--peers-yaml", action="store_true", help="regenerate peers.yaml numbers from the recalculated v2")
    ap.add_argument("--only", choices=("en", "es"), default=None, help="build one language only")
    a = ap.parse_args(argv)
    project = Path(a.project).resolve()
    if a.peers_yaml:
        return regen_peers_yaml(project)
    Y = load_extras(project)
    X, C = ciq_prompt_extras(Y), bimbo_consensus(project)
    tr = json.loads(Path(a.es_dict).read_text(encoding="utf-8")) if a.es_dict else None
    for lang in ((a.only,) if a.only else ("en", "es")):
        out = build(project, lang, X, C, Y, tr)
        print("wrote", out.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
