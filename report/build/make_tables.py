"""Markdown tables for report v2, from the TP12m workbook, report/data/tp12m_numbers.json and report/data/peers_v3.json.

Run after tp12m_data_charts.py:  .venv/bin/python report/build/make_tables.py
Writes report/tables/*.md; the section files include them with a line {{table: name}}.
"""

from __future__ import annotations

import json
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "report/tables"
OUT.mkdir(exist_ok=True)
N = json.load(open(ROOT / "report/data/tp12m_numbers.json"))
P = json.load(open(ROOT / "report/data/peers_v3.json"))
wb = openpyxl.load_workbook(ROOT / N["sources"]["workbook"], data_only=True)
IS, BS, CF, SEG = wb["IS"], wb["BS"], wb["CF"], wb["Segments"]
COLS = "BCDEFGHIJK"
YRS = ["FY2021A", "FY2022A", "FY2023A", "FY2024A", "FY2025A", "FY2026E", "FY2027E", "FY2028E", "FY2029E", "FY2030E"]


def md(rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out) + "\n"


def w(name: str, rows: list[list[str]]) -> None:
    (OUT / f"{name}.md").write_text(md(rows))


def f0(v):
    return f"({abs(v):,.0f})" if v < 0 else f"{v:,.0f}"


def pct(v, d=1):
    return f"{v*100:.{d}f}%"


def val(sheet, col, r):
    return sheet[f"{col}{r}"].value


# ---- peers ----------------------------------------------------------------------------------------------------------
rows = [["Company", "EV/EBITDA LTM", "EV/EBITDA NTM", "P/E LTM", "Net debt / EBITDA", "EBITDA margin"]]
order = ["Grupo Bimbo", "Flowers", "Gruma", "Yamazaki", "ARYZTA", "Smucker", "Campbell", "Mondelez", "Arca", "PepsiCo"]
by = {p["name"]: p for p in P["peers"]}
for key in order:
    p = next(x for n, x in by.items() if key in n)
    star = "*" if p["in_median"] == "no" else ""
    name = {"Grupo Bimbo": "**Grupo Bimbo**", "Flowers": "Flowers Foods", "Gruma": "Gruma", "Yamazaki": "Yamazaki Baking", "ARYZTA": "Aryzta",
            "Smucker": "J.M. Smucker", "Campbell": "Campbell's", "Mondelez": "Mondelez", "Arca": "Arca Continental", "PepsiCo": "PepsiCo"}[key]
    rows.append([name + star, f"{p['ev_ebitda_ltm']:.1f}x", f"{p['ev_ebitda_ntm']:.1f}x", f"{p['pe_ltm']:.1f}x", f"{p['nd_ebitda']:.2f}x",
                 pct(p["ebitda_margin"])])
for lab, k in (("**Core median**", "core_median"), ("**Eligible median**", "all_median")):
    m = P["medians"][k]
    rows.append([lab, f"{m['ev_ebitda_ltm']:.1f}x", f"{m['ev_ebitda_ntm']:.1f}x", f"{m['pe_ltm']:.1f}x", f"{m['nd_ebitda']:.2f}x", pct(m["ebitda_margin"])])
w("peers", rows)

# ---- WACC -----------------------------------------------------------------------------------------------------------
W = wb["WACC_V2"]
rows = [["Component", "Value", "Basis"],
        ["Peso default-free rate", pct(W["B7"].value, 2), "M-Bono 9.26% less 1.75% default spread"],
        ["US 10-year Treasury", pct(W["B8"].value, 2), "FRED, 16-Oct-2026"],
        ["Blended risk-free rate", pct(W["B26"].value, 2), "55% peso, 45% dollar-linked (US rate converted to pesos at 1.7% depreciation)"],
        ["Mature-market equity risk premium", pct(W["B29"].value, 2), "Damodaran implied"],
        ["Unlevered / relevered beta", f"{W['B30'].value:.2f} / {W['B33'].value:.2f}", "Global food processing; D/E 74.3% incl. leases"],
        ["Country risk premium x beta", pct(W["B22"].value * W["B33"].value, 2), "2.05% EBITDA-weighted CRP"],
        ["**Cost of equity (ke)**", f"**{pct(W['B51'].value, 2)}**", "Team model"],
        ["Cost of debt, pre-tax", pct(W["B44"].value, 2), "58% non-peso debt at UST + 100 bp, in pesos; 42% peso debt at 9.71%"],
        ["Debt weight, D/(D+E)", pct(W["B49"].value, 1), "Market value, leases included"],
        ["**WACC**", f"**{pct(W['B50'].value, 2)}**", "Tax rate 30%"]]
w("wacc", rows)

# ---- DCF bridge at Dec-2027 -----------------------------------------------------------------------------------------
V = wb["Valuacion_12m"]
rows = [["MXN million, 31-Dec-2027", "Value"],
        ["PV of FCFF FY2028E-FY2030E", f0(V["B31"].value)],
        ["PV of terminal value", f0(V["B32"].value)],
        ["**Enterprise value**", f"**{f0(V['B33'].value)}**"],
        ["Gross debt", f0(V["B35"].value)], ["Lease liabilities", f0(V["B36"].value)], ["Cash", f0(V["B37"].value)],
        ["Non-controlling interests (income capitalised at ke less g)", f0(V["B38"].value)], ["Other debt-like items", f0(V["B39"].value)],
        ["Associates", f0(V["B40"].value)],
        ["**Equity value, 31-Dec-2027**", f"**{f0(V['B41'].value)}**"],
        ["Equity value at 16-Oct-2027 (ke factor 0.976)", f0(V["B47"].value)],
        ["Shares, net of 4Q26-FY2027E buybacks (millions)", f"{V['B48'].value:,.1f}"],
        ["**12-month target price (MXN)**", f"**{V['B49'].value:.2f}**"]]
w("dcf_bridge", rows)

# ---- one-at-a-time sensitivities on the 12-month target ----------------------------------------------------------------
s = N["sens"]
T = N["target_12m"]


def line(lab, d):
    return [lab, f"{T + d:.2f}", f"{d:+.2f}", f"{d / T * 100:+.1f}%"]


rows = [["Change (one at a time)", "Target (MXN)", "vs base", "%"],
        line("WACC -0.5 pp (9.12%)", s["wacc_m50"]), line("WACC +0.5 pp (10.12%)", s["wacc_p50"]),
        line("Terminal g +0.5 pp", s["g_p50"]), line("Terminal g -0.5 pp", s["g_m50"]),
        line("Adj. EBITDA margin +50 bp from FY2028E", s["margin_p50"]), line("Adj. EBITDA margin -50 bp from FY2028E", s["margin_m50"]),
        line("Adj. EBITDA margin -100 bp from FY2028E", s["margin_m100"]), line("Capex +50 bp of sales from FY2028E", s["capex_p50"]),
        line("Terminal RONIC at FY2022-25 average (15.1%)", s["ronic_avg"]), line("Terminal RONIC at FY2022-25 low (11.9%)", s["ronic_min"]),
        line("North America ratio 0 (terminal NOPAT -2.0%)", s["na_ratio_zero_terminal"]),
        line("One-year -100 bp margin hit in FY2027E only", N["wheat_1y"]),
        ["Without netting 4Q26 and FY2027E buybacks from the share count", f"{N['tp_without_buyback_adj']:.2f}", f"{N['buyback_adj']:+.2f}", f"{N['buyback_adj'] / T * 100:+.1f}%"]]
w("sens_one", rows)

rows = [["WACC \\ g"] + [pct(g, 2) for g in N["grid_g"]]]
for wv, r in zip(N["grid_wacc"], N["grid"]):
    rows.append([pct(wv, 2)] + [f"{x:.2f}" if abs(wv - N["wacc"]) > 1e-9 or abs(g - N["g"]) > 1e-9 else f"**{x:.2f}**" for x, g in zip(r, N["grid_g"])])
w("sens_grid", rows)

# ---- forecast summary -----------------------------------------------------------------------------------------------
def series(sheet, r):
    return [val(sheet, c, r) for c in COLS]


sales, gp, ebit, ebitda, ni, eps = (series(IS, r) for r in (6, 8, 14, 39, 31, 33))
capex = [-v for v in series(CF, 37)]
cfo = series(CF, 34)
ix = [4, 5, 6, 7, 8, 9]
rows = [["MXN million"] + [YRS[i] for i in ix],
        ["Net sales"] + [f0(sales[i]) for i in ix],
        ["Growth"] + [pct(sales[i] / sales[i - 1] - 1) for i in ix],
        ["Gross margin"] + [pct(gp[i] / sales[i]) for i in ix],
        ["Adj. EBITDA"] + [f0(ebitda[i]) for i in ix],
        ["Adj. EBITDA margin"] + [pct(ebitda[i] / sales[i], 2) for i in ix],
        ["Other expenses / sales"] + [pct(val(IS, COLS[i], 12) / sales[i], 2) for i in ix],
        ["EPS (MXN)"] + [f"{eps[i]:.2f}" for i in ix],
        ["Capex / sales"] + [pct(capex[i] / sales[i]) for i in ix],
        ["Net debt / EBITDA"] + [f"{N['leverage'][i]:.2f}x" for i in ix]]
w("forecast", rows)

ixh = [0, 1, 2, 3, 4]
rows = [["MXN million"] + [YRS[i] for i in ixh],
        ["Net sales"] + [f0(sales[i]) for i in ixh],
        ["Growth"] + ["n.a."] + [pct(sales[i] / sales[i - 1] - 1) for i in ixh[1:]],
        ["Gross margin"] + [pct(gp[i] / sales[i]) for i in ixh],
        ["Adj. EBITDA margin"] + [pct(ebitda[i] / sales[i], 2) for i in ixh],
        ["EBIT / interest expense"] + [f"{ebit[i] / val(IS, COLS[i], 17):.1f}x" for i in ixh],
        ["Net income, controlling"] + [f0(ni[i]) for i in ixh],
        ["Cash from operations"] + [f0(cfo[i]) for i in ixh],
        ["Capex (PP&E)"] + [f0(capex[i]) for i in ixh],
        ["Net debt incl. leases / EBITDA"] + [f"{N['leverage'][i]:.2f}x" for i in ixh]]
w("history", rows)

# ---- FCFF projection (Dec-2026 basis) ---------------------------------------------------------------------------------
VA = wb["Valuacion"]
rows = [["MXN million", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "Terminal"]]
for lab, r in (("EBIT", 6), ("NOPAT (tax 32.7%)", 9), ("+ D&A", 13), ("- Capex", 14), ("- New leases", 15), ("+/- Working capital", 16), ("**FCFF**", 17)):
    cells = [f0(val(VA, c, r)) for c in "BCDE"]
    rows.append([lab] + ([f"**{x}**" for x in cells] if r == 17 else cells) + [f0(VA["F27"].value) if r == 17 else ""])
rows.append(["PV of FCFF (WACC 9.62%, mid-year)"] + [f0(val(VA, c, 37)) for c in "BCDE"] + [f"TV {f0(VA['F29'].value)}"])
w("fcff", rows)

# ---- regions --------------------------------------------------------------------------------------------------------
rows = [["Region", "Sales FY2025A", "Sales FY2027E", "Sales FY2030E", "CAGR 25-30E", "Adj. EBITDA margin FY2025A"]]
for k, lab, r in (("na", "North America", 62), ("mx", "Mexico", 61), ("eaa", "Europe, Asia & Africa", 64), ("latam", "Latin America", 63)):
    sv = N["seg_sales"][k]
    rows.append([lab, f0(sv[4]), f0(sv[6]), f0(sv[9]), pct((sv[9] / sv[4]) ** 0.2 - 1), pct(val(SEG, "F", r))])
rows.append(["**Group (after eliminations)**", f0(sales[4]), f0(sales[6]), f0(sales[9]), pct((sales[9] / sales[4]) ** 0.2 - 1), pct(ebitda[4] / sales[4])])
w("regions", rows)

# ---- risks ----------------------------------------------------------------------------------------------------------
rows = [["Risk", "Pillar", "P", "I", "Value effect on target", "Mitigation"],
        ["R1 Input costs: wheat cost persists", "2", "3", "4", "-9.4 (futures US$266); -14.2 if wheat +35%", "Hedges (about one year), pricing, productivity"],
        ["R2 North America turnaround stalls", "3", "3", "5", f"about {s['margin_m100'] * 0.938:.1f} (margin back to 8.4%)", "Transformation programme, 11 closures"],
        ["R3 Terminal return on capital below base", "1", "2", "4", f"{s['ronic_min']:.1f} (RONIC 11.9%)", "Capex discipline, margin delivery"],
        ["R4 Mexico labour and health policy", "3", "3", "4", f"{s['margin_m100'] * 0.3805:.1f} to {s['margin_m100'] * 0.5663:.1f} (-100 to -150 bp)", "Reformulation, pricing, route productivity"],
        ["R5 Capital allocation: capex or deal", "1", "3", "2", f"{s['capex_p50']:.1f} (capex +50 bp)", "Capex guide cut; undrawn US$2.35bn revolver"],
        ["R6 Terminal growth and peso", "1", "3", "3", f"{s['g_m50']:.1f} (g -0.5 pp)", "Dollar debt (42%) hedges part"],
        ["R7 Other expenses and integration costs do not fall", "3", "3", "4", "-10.6 (0.76% of sales and MXN 541 million)", "Integration programme; 1Q27 report is the first check"]]
w("risks", rows)

# ---- appendix statements (condensed) ----------------------------------------------------------------------------------
ia = [3, 4, 5, 6, 7, 8, 9]
hd = ["MXN million"] + [YRS[i] for i in ia]


def srow(lab, sheet, r, sign=1):
    return [lab] + [f0(sign * val(sheet, COLS[i], r)) for i in ia]


rows = [hd, srow("Net sales", IS, 6), srow("Gross profit", IS, 8), srow("Operating income (EBIT)", IS, 14), srow("Financing result", IS, 21, -1),
        srow("Income taxes", IS, 24, -1), srow("Consolidated net income", IS, 27), srow("Controlling interest", IS, 31),
        ["EPS (MXN)"] + [f"{eps[i]:.2f}" for i in ia], srow("Adj. EBITDA", IS, 39)]
w("is", rows)
rows = [hd, srow("Cash", BS, 6), srow("Receivables", BS, 7), srow("Inventories", BS, 8), srow("PP&E", BS, 14), srow("Right-of-use assets", BS, 15),
        ["Goodwill and intangibles"] + [f0(val(BS, COLS[i], 19) + val(BS, COLS[i], 20)) for i in ia], srow("Total assets", BS, 22), srow("Financial debt (current + long term)", BS, 25),
        ["Lease liabilities"] + [f0(val(BS, COLS[i], 28) + val(BS, COLS[i], 36)) for i in ia],
        ["Financial debt"] + [f0(val(BS, COLS[i], 25) + val(BS, COLS[i], 35)) for i in ia], srow("Total equity", BS, 53)]
rows.pop(8)
w("bs", rows)
rows = [hd, srow("Cash from operations", CF, 34), srow("Purchases of PP&E", CF, 37), srow("Business acquisitions", CF, 38), srow("Borrowings", CF, 52),
        srow("Debt repayment", CF, 53), srow("Dividends paid", CF, 57), srow("Lease payments", CF, 59), srow("Interest paid", CF, 54),
        srow("Share repurchases", CF, 62)]
_other = [val(CF, COLS[i], 66) - sum(val(CF, COLS[i], r) for r in (34, 37, 38, 52, 53, 57, 59, 54, 62)) for i in ia]
rows += [["Other items (NCI distributions, derivatives, FX effect, other investing)"] + [f0(x) for x in _other], srow("Net change in cash", CF, 66)]
w("cf", rows)
print("tables written:", sorted(p.name for p in OUT.glob("*.md")))
