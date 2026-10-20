"""HTML tables for the report (left-column tables in the body and full-width tables in the appendix). All numbers come from report_data."""

from __future__ import annotations

import i18n
import report_data as D
from report_style import AMBER, BLUE, GRAY, GRID, LIGHT, NAVY, PALE_BLUE, RED

W_BODY, W_APP = 361.3, 539.3     # text widths (pt) of the body column and of the appendix page
FS_BODY = 6.5      # font size (pt) of in-column tables
FS_APP = 6.2       # appendix tables


# ---------------------------------------------------------------------------------------------------------- helpers
def cell(text, align="r", bold=False, color=None, bg=None, italic=False, colspan=None, border=True, pad="1.1pt 2.2pt"):
    st = [f"text-align:{ {'l': 'left', 'r': 'right', 'c': 'center'}[align] }", f"padding:{pad}"]
    if bold:
        st.append("font-weight:bold")
    if italic:
        st.append("font-style:italic")
    if color:
        st.append(f"color:{color}")
    if bg:
        st.append(f"background-color:{bg}")
    if border:
        st.append(f"border-bottom:0.3pt solid {LIGHT}")
    cs = f' colspan="{colspan}"' if colspan else ""
    return f'<td{cs} style="{";".join(st)}">{text}</td>'


def head(text, align="r", colspan=None, color=NAVY, width=None):
    cs = f' colspan="{colspan}"' if colspan else ""
    a = {"l": "left", "r": "right", "c": "center"}[align]
    w = f"width:{width};" if width else ""
    return (f'<th{cs} style="{w}text-align:{a};padding:1.2pt 2.2pt;color:{color};font-weight:bold;'
            f'border-bottom:0.9pt solid {BLUE}">{text}</th>')


def table(header, rows, *, fs=FS_BODY, widths=None, aligns=None, bold_rows=(), hl_rows=(), sub_rows=(), title=None, note=None,
          first_col_bold=False, total_w=None):
    n = len(header)
    if total_w is None:
        total_w = W_APP if fs == FS_APP else W_BODY
    wpt = [f"{max(float(w.strip('%')) / 100 * (total_w - 17.0) - 4.4, 6.0):.1f}pt" for w in widths] if widths else None   # minus the cell padding
    aligns = aligns or (["l"] + ["r"] * (n - 1))
    out = []
    if title:
        out.append(f'<p style="margin:3pt 0 1.5pt 0;font-weight:bold;color:{BLUE};font-size:{fs + 0.8}pt">{title}</p>')
    out.append(f'<table style="width:100%;border-collapse:collapse;font-size:{fs}pt">')
    out.append("<tr>" + "".join(head(h, aligns[i], width=(wpt[i] if wpt else None)) for i, h in enumerate(header)) + "</tr>")
    for r, row in enumerate(rows):
        bold = r in bold_rows
        hl = r in hl_rows
        sub = r in sub_rows
        tds = []
        if sub:
            tds.append(cell(row[0], "l", bold=True, color=BLUE, colspan=n))
        else:
            for i, v in enumerate(row):
                tds.append(cell(v, aligns[i], bold=bold or hl or (first_col_bold and i == 0), color=BLUE if hl else None))
        out.append("<tr>" + "".join(tds) + "</tr>")
    out.append("</table>")
    if note:
        out.append(f'<p style="margin:1.5pt 0 4pt 0;font-size:{fs - 0.6}pt;color:{GRAY};font-style:italic">{note}</p>')
    return "".join(out)


def pm(x, d=1):
    return "n/a" if x is None else f"{x * 100:.{d}f}%"


def n0(x):
    if x is None:
        return "n/a"
    s = f"{abs(x):,.0f}"
    return f"({s})" if x < 0 else s


def n1(x, d=1):
    return "n/a" if x is None else f"{x:,.{d}f}"


# ---------------------------------------------------------------------------------------------------------- body
def keydata() -> str:
    mcap = D.PRICE * D.SHARES_M
    net_debt = D.STATE["debt"] - D.STATE["cash"]
    ev = D.PEERS["peers"][-1]["ev_ebitda_ltm"] * 60919
    rows = [("Price (16-Oct-2026)", f"MXN {D.PRICE:.2f}"), ("52-week range", f"{D.RANGE_52W[0]:.2f} - {D.RANGE_52W[1]:.2f}"),
            ("Shares outstanding", f"{D.SHARES_M:,.1f}m"), ("Market cap", f"MXN {mcap / 1000:,.1f}bn"),
            ("Net debt incl. leases (Jun-26)", f"MXN {net_debt / 1000:,.1f}bn"), ("Enterprise value (peer basis)", f"MXN {ev / 1000:,.1f}bn"),
            ("EV / EBITDA, LTM", f"{D.PEERS['peers'][-1]['ev_ebitda_ltm']:.2f}x"), ("LTM Adj. EBITDA (Jun-26)", "MXN 60.9bn"),
            ("Dividend / yield", f"MXN {D.DPS_LAST:.3f} / {D.DPS_LAST / D.PRICE * 100:.1f}%"),
            ("Free float / control group", f"{D.FREE_FLOAT:.1f}% / {D.CONTROL_PCT:.1f}%"),
            ("Consensus (12 analysts)", f"Hold ({D.CONSENSUS_REC:.2f})"), ("Mean / median target", f"{D.TARGETS['mean']:.2f} / {D.TARGETS['median']:.2f}")]
    if i18n.ES_ON:
        rows = [(a, b) for a, b in rows]
        fixed = []
        for a, b in rows:
            if b.endswith("bn"):
                fixed.append((a + ", MXN mil mill.", b.replace("MXN ", "").replace("bn", "")))
            else:
                fixed.append((a, b))
        rows = fixed
    body = "".join(f"<tr>{cell(a, 'l', border=True)}{cell(b, 'r', bold=True)}</tr>" for a, b in rows)
    return (f'<table style="width:100%;border-collapse:collapse;font-size:6.5pt"><tr>{head("Key data", "l", colspan=2, color=BLUE)}</tr>'
            f"{body}</table>")


def fy25() -> dict:
    """FY2025A base year: reported lines (Grupo Bimbo, 2026f, pp. 85-86); tax on EBIT, NOPAT and FCFF are pro forma at the DCF tax rate."""
    rev, ebitda = D.REV_H[4], D.ADJ_EBITDA_H[4]
    da = D.stmt("IS", "D&A (included in costs above)", 2025)
    capex, lease, wc = D.CAPEX_PPE_H[4], D.stmt("CF", "Lease principal paid (IFRS 16)", 2025), D.stmt("CF", "Change in working capital", 2025)
    ebit = ebitda - da
    tax = ebit * D.STATE["tax_ebit"]
    nopat = ebit - tax
    return {"rev": rev, "g": D.REV_H[4] / D.REV_H[3] - 1, "ebitda": ebitda, "m": ebitda / rev, "da": da, "ebit": ebit, "tax": tax,
            "nopat": nopat, "capex": capex, "lease": lease, "wc": wc, "fcff": nopat + da - capex - lease + wc}


FY25_NOTE = ("*FY2025A: reported figures (Grupo Bimbo, 2026f, pp. 85-86), except new leases (lease principal paid) and working capital, derived from the statements. Tax on EBIT, NOPAT and FCFF "
             "are pro forma at the 32% rate, for comparison only; the valuation counts flows from 30-Jun-2026.")


def forecast() -> str:
    r, f = D.RUN, fy25()
    yrs = ["FY2025A*"] + [f"FY{y}E" for y in D.YEARS_F]
    g = D.STATE["growth"]
    rows = [["Net sales", n0(f["rev"])] + [n0(v) for v in r["rev"]],
            ["  growth, % y/y", pm(f["g"])] + [pm(x) for x in g],
            ["Adj. EBITDA", n0(f["ebitda"])] + [n0(v) for v in r["ebitda"]],
            ["  margin", pm(f["m"])] + [pm(e / v) for e, v in zip(r["ebitda"], r["rev"])],
            ["D&A", n0(f["da"])] + [n0(v) for v in r["da"]],
            ["Capex (excl. new leases)", n0(f["capex"])] + [n0(v) for v in r["capex"]],
            ["New leases", n0(f["lease"])] + [n0(v) for v in r["leases"]],
            ["FCFF", n0(f["fcff"])] + [n0(v) for v in r["fcff"]]]
    return table(["MXN million"] + yrs, rows, bold_rows=(7,), widths=["25%"] + ["12.5%"] * 6,
                 title="Forecast and free cash flow", note="Source: team model. " + FY25_NOTE)


def wacc() -> str:
    s, r = D.STATE, D.RUN
    wd = s["de"] / (1 + s["de"])
    rows = [["Risk-free rate (peso, default-free)", pm(s["rf"], 2), "M-Bono 10y 9.26% less 1.75% default spread"],
            ["Equity risk premium", pm(s["erp"], 2), "Damodaran implied ERP, 1-Oct-2026"],
            ["Country risk premium", pm(s["crp"], 2), "Weighted by FY2025 Adj. EBITDA"],
            ["Unlevered beta", f"{s['beta_u']:.3f}", "Damodaran food processing 0.53-0.56; Bimbo regression 0.54"],
            ["Debt / equity (market, with leases)", pm(s["de"], 1), "Debt MXN 187.0bn; market cap MXN 251.7bn"],
            ["Relevered beta", f"{r['beta_l']:.3f}", "Tax rate 30%"],
            ["Cost of equity", pm(r["ke"], 2), "rf + beta x ERP + CRP"],
            ["Pre-tax cost of debt", pm(s["kd"], 2), "M-Bono 10y + 0.45 pp issue spread"],
            ["After-tax cost of debt", pm(s["kd"] * (1 - s["tax_marg"]), 2), "Tax rate 30%"],
            ["Weights: equity / debt", f"{(1 - wd) * 100:.1f}% / {wd * 100:.1f}%", "Market values"],
            ["WACC", pm(r["wacc"], 2), "Peso, nominal"]]
    return table(["Cost of capital", "Value", "Basis"], rows, aligns=["l", "r", "l"], bold_rows=(6, 10), widths=["38%", "14%", "48%"],
                 title="WACC build", note="Source: Damodaran (2026); S&P Capital IQ (2026); team model.")


def results() -> str:
    r, L, v3 = D.RUN, D.LEV, D.CONS["results"]["v3"]
    p = D.PRICE

    def vs(x):
        return f"{(x / p - 1) * 100:+.1f}%".replace("-", "−")

    rows = [[f"DCF, exit multiple {D.STATE['exit_mult']:.2f}x (base)", f"{r['ps_exit']:.2f}", vs(r["ps_exit"]), f"12-month value {r['target12m_exit']:.2f}; expected return −{abs(r['exp_return_exit']) * 100:.1f}%"],
            ["DCF, Gordon (g 4.125%, RONIC 14.6%)", f"{r['ps_gordon_ronic']:.2f}", vs(r["ps_gordon_ronic"]), "Cross-check; growth needs reinvestment"],
            ["DCF, Gordon, no reinvestment link", f"{r['ps_gordon_naive']:.2f}", vs(r["ps_gordon_naive"]), f"Implies RONIC {r['ronic_naive'] * 100:.1f}%"],
            ["Comps, core bakers 5.53x", f"{v3['comps_core']:.2f}", vs(v3["comps_core"]), "Flowers Foods, Gruma"],
            ["Comps, exit multiple 6.0x", "42.68", vs(42.68), "LTM EBITDA MXN 60,919m"],
            ["Comps, all eligible peers 8.27x", f"{v3['comps_all']:.2f}", vs(v3["comps_all"]), "Median of six peers"],
            ["52-week trading range", f"{D.RANGE_52W[0]:.2f}-{D.RANGE_52W[1]:.2f}", "", "Price on 16-Oct-2026: 58.60"],
            [f"Analyst targets, median ({D.TARGETS['n']})", f"{D.TARGETS['median']:.2f}", vs(D.TARGETS["median"]), f"Range {D.TARGETS['low']:.0f}-{D.TARGETS['high']:.0f}; mean {D.TARGETS['mean']:.2f}"]]
    return table(["Method (MXN per share)", "Value", "vs price", "Note"], rows, aligns=["l", "r", "r", "l"], bold_rows=(0,),
                 widths=["38%", "13%", "11%", "38%"], note="Source: team model; S&P Capital IQ (2026). Comps use the Jun-26 bridge; targets are consensus.")


def _rating(er: float) -> str:
    er = round(er, 3)
    if er >= 0.15:
        return "BUY"
    if er <= -0.10:
        return "SELL"
    return "HOLD (clean)" if -0.05 <= er <= 0.10 else "HOLD"


def multiple_er() -> str:
    L, r = D.LEV, D.RUN
    slope, base_m, base_v, ke = L["slope_per_turn"], D.STATE["exit_mult"], r["ps_exit"], r["ke"]
    refs = [(5.0, ""), (5.526, "Core bakers' median"), (base_m, "Base case"), (L["bands"]["clean_low"]["multiple"], "Clean HOLD, lower bound"),
            (6.5, ""), (L["bands"]["clean_high"]["multiple"], "Clean HOLD, upper bound"), (L["reverse_multiple"], "Price-implied"),
            (L["bands"]["buy_edge"]["multiple"], "BUY threshold")]
    rows = []
    for m, lab in refs:
        v = base_v + slope * (m - base_m)
        er = v * (1 + ke) / D.PRICE - 1
        t12 = v * (1 + ke) - D.DPS_NEXT
        rows.append([f"{m:.2f}x", lab, f"{v:.2f}", f"{t12:.2f}", f"{er * 100:+.1f}%".replace("-", "−"), _rating(er)])
    return table(["Exit multiple", "Reference", "Value today", "12-month value", "Exp. return", "Rating"], rows,
                 aligns=["r", "l", "r", "r", "r", "l"], widths=["13%", "27%", "14%", "17%", "14%", "15%"], bold_rows=(2,),
                 note="Source: team model. Expected return = 12-month value / price - 1 + dividend yield (MXN 1.05).")


def ratios() -> str:
    yrs = list(range(2022, 2026))
    IS, BS, R = "IS", "BS", "Ratios"

    def avg(sheet, label, y):
        return (D.stmt(sheet, label, y) + D.stmt(sheet, label, y - 1)) / 2

    gm = [D.stmt(R, "Gross margin", y) for y in yrs]
    ebitm = [D.stmt(R, "EBIT margin", y) for y in yrs]
    nm = [D.stmt(IS, "Net income to shareholders", y) / D.stmt(IS, "Revenue", y) for y in yrs]
    at = [D.stmt(IS, "Revenue", y) / avg(BS, "Total assets", y) for y in yrs]
    lev = [avg(BS, "Total assets", y) / avg(BS, "Shareholders' equity", y) for y in yrs]
    roe = [a * b * c for a, b, c in zip(nm, at, lev)]
    key_roic = [k for k in D.ST["sheets"]["Ratios"] if k.startswith("ROIC")][0]
    roic = [D.stmt(R, key_roic, y) for y in yrs]
    fcf = [D.stmt(R, "Free cash flow margin", y) for y in yrs]
    nd = [D.stmt("BS", "Net debt", y) / e for y, e in zip(yrs, D.ADJ_EBITDA_H[1:5])]
    ic = [D.stmt(R, "EBIT / interest expense", y) for y in yrs]
    cr = [D.stmt(BS, "Total current assets", y) / D.stmt(BS, "Total current liabilities", y) for y in yrs]
    f = lambda xs: [pm(x) for x in xs]
    x1 = lambda xs: [f"{x:.2f}x" for x in xs]
    rows = [["DuPont analysis"], ["Net margin"] + f(nm), ["Asset turnover"] + x1(at), ["Leverage (assets / equity)"] + x1(lev),
            ["Return on equity"] + f(roe), ["Margins and returns"], ["Gross margin"] + f(gm), ["EBIT margin"] + f(ebitm),
            ["ROIC"] + f(roic), ["FCF margin"] + f(fcf), ["Leverage and liquidity"],
            ["Net debt / Adj. EBITDA"] + x1(nd), ["EBIT / interest"] + x1(ic), ["Current ratio"] + x1(cr)]
    hdr = ["Ratio"] + [f"FY{y}A" for y in yrs]
    note = ("Source: Grupo Bimbo (2026f); team model. FY2022 includes a non-cash pension gain. Average balances for DuPont; "
            "net debt includes leases.")
    return table(hdr, rows, sub_rows=(0, 5, 10), bold_rows=(4,), widths=["36%"] + ["16%"] * 4, fs=6.4, note=note,
                 title="Returns, margins and leverage, history")


# ---------------------------------------------------------------------------------------------------------- appendix
def _stmt_table(title, sheet, labels, years, fs=FS_APP, bold=()):
    hdr = ["MXN million"] + [f"FY{y}{'A' if y <= 2025 else 'E'}" for y in years]
    wnum = f"{(100 - 30) / len(years):.2f}%"
    rows = []
    for lab in labels:
        if lab not in D.ST["sheets"][sheet]:
            continue
        vals = D.stmt_row(sheet, lab, years)
        if all(v is None for v in vals):
            continue
        if lab == "Diluted EPS":
            rows.append([lab] + ["n/a" if v is None else f"{v:.2f}" for v in vals])
        else:
            rows.append([lab] + [n0(v) if v is not None else "" for v in vals])
    b = tuple(i for i, r in enumerate(rows) if r[0] in bold)
    return table(hdr, rows, fs=fs, widths=["30%"] + [wnum] * len(years), bold_rows=b, title=title)


def is_() -> str:
    labels = ["Revenue", "Cost of sales", "Gross profit", "Operating expenses (net)", "EBIT", "Interest expense", "Interest income",
              "Other financial result, net", "Pre-tax income", "Income tax", "Net income", "Attributable to non-controlling interests",
              "Net income to shareholders", "Diluted EPS", "D&A (included in costs above)", "EBITDA (post-IFRS 16)"]
    return _stmt_table("Income statement", "IS", labels, list(range(2021, 2026)), bold=("Gross profit", "EBIT", "Net income"))


def bs() -> str:
    labels = ["Cash and equivalents", "Accounts receivable", "Inventories", "Other current assets", "Total current assets",
              "PP&E and right-of-use assets, net", "Intangibles and goodwill", "Other non-current assets", "Total assets",
              "Accounts payable", "Other current liabilities", "Short-term debt", "Total current liabilities", "Long-term debt",
              "Lease liabilities", "Other non-current liabilities", "Total liabilities", "Shareholders' equity",
              "Non-controlling interests", "Total equity", "Total liabilities and equity", "Net debt"]
    return _stmt_table("Balance sheet", "BS", labels, list(range(2021, 2026)), bold=("Total assets", "Total liabilities", "Total equity", "Net debt"))


def cf() -> str:
    labels = ["Net income", "D&A", "Change in working capital", "Cash flow from operations", "Capital expenditures",
              "Dividends paid", "Lease principal paid (IFRS 16)", "Dividends to non-controlling interests",
              "Net debt issued / (repaid)", "Closing cash", "Free cash flow (CFO - capex - lease principal)"]
    return _stmt_table("Cash flow statement", "CF", labels, list(range(2021, 2026)), bold=("Cash flow from operations", "Free cash flow (CFO - capex - lease principal)"))


def dcf() -> str:
    r, s = D.RUN, D.STATE
    f = fy25()
    yrs = ["FY2025A*"] + [f"FY{y}E" for y in D.YEARS_F]
    rows = [["EBITDA", n0(f["ebitda"])] + [n0(v) for v in r["ebitda"]], ["D&A", n0(-f["da"])] + [n0(-v) for v in r["da"]],
            ["EBIT", n0(f["ebit"])] + [n0(v) for v in r["ebit"]],
            ["Tax on EBIT (32%)", n0(-f["tax"])] + [n0(-v) for v in r["tax"]], ["NOPAT", n0(f["nopat"])] + [n0(v) for v in r["nopat"]],
            ["Plus D&A", n0(f["da"])] + [n0(v) for v in r["da"]],
            ["Less capex (excl. new leases)", n0(-f["capex"])] + [n0(-v) for v in r["capex"]],
            ["Less new leases", n0(-f["lease"])] + [n0(-v) for v in r["leases"]],
            ["Working capital", n0(f["wc"])] + [n0(v) for v in r["dwc"]], ["FCFF", n0(f["fcff"])] + [n0(v) for v in r["fcff"]],
            ["PV of FCFF (stub-adjusted)", "n/a"] + [n0(v) for v in r["pv"]]]
    t1 = table(["MXN million"] + yrs, rows, fs=FS_APP, widths=["27%"] + ["12.2%"] * 6, bold_rows=(9,), title="Free cash flow to the firm",
               note="Source: team model. " + FY25_NOTE)
    tv = r["ebitda"][-1] * s["exit_mult"]
    claims = [("PV of FCFF FY2026E-FY2030E", r["pv_explicit"]), (f"Terminal value ({s['exit_mult']:.2f}x x FY2030E EBITDA {n0(r['ebitda'][-1])})", tv),
              ("PV of terminal value", r["pv_tv_exit"]), ("Enterprise value", r["ev_exit"]),
              ("Less debt including leases", -s["debt"]), ("Plus cash", s["cash"]), ("Less non-controlling interests (market value)", -r["nci"]),
              ("Plus net associates", s["assoc_net"]), ("Equity value at 30-Jun-2026", r["equity_exit_anchor"])]
    rows2 = [[a, n0(v)] for a, v in claims]
    rows2 += [["Per share at 30-Jun-2026 (4,294.9m shares)", f"{r['ps_anchor_exit']:.2f}"], [f"Rolled to 16-Oct-2026 (x {r['roll']:.4f})", f"{r['ps_exit']:.2f}"],
              ["Terminal value share of enterprise value", pm(r["tv_share_exit"], 0)],
              ["Gordon cross-check (RONIC 14.6%): per share", f"{r['ps_gordon_ronic']:.2f}"],
              ["Gordon, no reinvestment link: per share", f"{r['ps_gordon_naive']:.2f}"]]
    t2 = table(["Enterprise value to equity value", "MXN million"], rows2, fs=FS_APP, aligns=["l", "r"], bold_rows=(3, 8, 10), widths=["72%", "28%"],
               title="Equity bridge (exit-multiple method)",
               note="Source: team model. Gordon claims also deduct MXN 18,135 million of pensions, provisions and derivatives.")
    return t1 + t2


def crp() -> str:
    reg = [("North America", 0.17, 28.8), ("Mexico", 2.72, 55.4), ("Europe, Asia and Africa", 2.63, 9.8), ("Latin America", 3.94, 6.0)]
    rows = [[n, f"{c:.2f}%", f"{w:.1f}%", f"{c * w / 100:.2f}%"] for n, c, w in reg]
    rows.append(["Weighted country risk premium", "", "100.0%", f"{sum(c * w / 100 for _, c, w in reg):.2f}%"])
    return table(["Region", "Equity CRP", "Share of FY2025 Adj. EBITDA", "Contribution"], rows, fs=FS_APP, aligns=["l", "r", "r", "r"], bold_rows=(4,),
                 widths=["40%", "15%", "28%", "17%"], note="Source: Damodaran (2026, July update); Grupo Bimbo (2026e, p. 17); team model.")


def sens_exit() -> str:
    g = D.CONS["consolidated"]["grids"]
    hdr = ["WACC \\ exit multiple"] + [f"{m:.2f}x" for m in g["mults"]]
    rows = [[f"{w * 100:.2f}%"] + [f"{v:.2f}" for v in row] for w, row in zip(g["wacc"], g["exit"])]
    t = table(hdr, rows, fs=FS_APP, hl_rows=(2,), widths=["26%"] + ["14.8%"] * 5, title="Value per share, exit-multiple method (MXN)",
              note="Source: team model. Base case WACC 10.38%, multiple 5.92x. NCI claim and roll factor held at the base cost of equity.")
    return t


def sens_gordon() -> str:
    g = D.CONS["consolidated"]["grids"]
    hdr = ["WACC \\ terminal growth"] + [f"{x * 100:.3f}%" for x in g["g"]]
    rows = [[f"{w * 100:.2f}%"] + [f"{v:.2f}" for v in row] for w, row in zip(g["wacc"], g["gordon_ronic"])]
    return table(hdr, rows, fs=FS_APP, hl_rows=(2,), widths=["26%"] + ["14.8%"] * 5, title="Value per share, Gordon method with RONIC 14.6% (MXN)",
                 note="Source: team model.")


def comps() -> str:
    P = D.PEERS
    rows = []
    for p in P["peers"]:
        nm = p["name"].replace(" (subject)", "")
        flag = {"yes": "", "no": " *", "subject": ""}.get(p["in_median"], "")
        rows.append([nm + flag, p["ticker"].split(":")[-1] if False else p["ticker"], f"{p['ev_ebitda_ltm']:.2f}x", f"{p['ev_ebitda_ntm']:.2f}x",
                     f"{p['ev_sales']:.2f}x", f"{p['pe_ltm']:.1f}x", f"{p['nd_ebitda']:.2f}x", pm(p["ebitda_margin"])])
    m = P["medians"]
    for lab, key in (("Core median (Flowers, Gruma)", "core_median"), ("All eligible median", "all_median"), ("All eligible mean", "all_mean")):
        x = m[key]
        rows.append([lab, "", f"{x['ev_ebitda_ltm']:.2f}x", f"{x['ev_ebitda_ntm']:.2f}x", f"{x['ev_sales']:.2f}x", f"{x['pe_ltm']:.1f}x",
                     f"{x['nd_ebitda']:.2f}x", pm(x["ebitda_margin"])])
    n = len(P["peers"])
    return table(["Company", "Ticker", "EV/EBITDA LTM", "EV/EBITDA NTM", "EV/Sales", "P/E LTM", "ND/EBITDA", "EBITDA margin"], rows,
                 fs=FS_APP, aligns=["l", "l", "r", "r", "r", "r", "r", "r"], hl_rows=(n - 1,), bold_rows=(n, n + 1, n + 2),
                 widths=["26%", "14%", "10%", "10%", "9%", "9%", "11%", "11%"],
                 note=f"Source: S&P Capital IQ (2026), prices of {D.PEERS['pricing_date']}; team model. * Excluded from medians (lease or minority-interest data not verified on one basis).")


def segments() -> str:
    yrs = D.YEARS_H
    sales = {"North America": [175369, 205674, 192534, 189330, 190211], "Mexico": [109089, 130401, 145387, 151164, 154809],
             "Europe, Asia and Africa": [34195, 37536, 40545, 45044, 54214], "Latin America": [31109, 38411, 36647, 39879, 44120],
             "Eliminations": [-10970, -13316, -15234, -17082, -16402], "Consolidated": D.REV_H}
    ebitda = {"North America": [21452, 22611, 20217, 15812, 17117], "Mexico": [20771, 23320, 27484, 30762, 31630],
              "Europe, Asia and Africa": [2704, 2626, 2932, 4212, 5830], "Latin America": [1926, 3433, 3531, 3603, 3552],
              "Eliminations and other": [519, 1456, 778, 1084, 1327], "Consolidated": D.ADJ_EBITDA_H}
    hdr = ["MXN million"] + [f"FY{y}" for y in yrs]
    rows = [["Net sales by segment"]] + [[k] + [n0(v) for v in vals] for k, vals in sales.items()]
    rows += [["Adjusted EBITDA by segment"]] + [[k] + [n0(v) for v in vals] for k, vals in ebitda.items()]
    rows += [["Adjusted EBITDA margin (EBITDA / segment sales)"]]
    for k in ("North America", "Mexico", "Europe, Asia and Africa", "Latin America"):
        rows.append([k] + [pm(e / s) for e, s in zip(ebitda[k], sales[k])])
    rows.append(["Consolidated"] + [pm(e / s) for e, s in zip(ebitda["Consolidated"], sales["Consolidated"])])
    return table(hdr, rows, fs=FS_APP, sub_rows=(0, 7, 14), bold_rows=(6, 13, 19), widths=["34%"] + ["13.2%"] * 5,
                 note="Source: Grupo Bimbo (2026f, pp. 85-86; 2026a); team model. FY2021 restated for the Ricolino reclassification. Segment margins exclude intercompany royalties.")


RISK_ROWS = [
    ("R1", "Wheat and climate input costs cut gross margin for good", "ESG", 3, 4, "-3.55 for -50 bp from FY2027E", "Hedges (about one year), pricing, productivity", "No"),
    ("R2", "North America turnaround stalls; margin returns to 8.4%", "Operational", 3, 4, "-3.4 (100 bp = -2.81)", "Transformation programme; record productivity", "Partly"),
    ("R3", "Capex or M&A breaks the debt hold; S&P outlook negative", "Financial", 3, 3, "Not quantified", "2026 capex guide cut; US$2.35bn undrawn revolver", "Partly"),
    ("R4", "Mexican labour and health policy lowers margin", "Regulatory", 3, 4, "-2.79 to -4.19 for -100 to -150 bp", "Reformulation, pricing, route productivity", "Partly"),
    ("R5", "Exit multiple falls to the core bakers' 5.53x", "Market", 3, 3, "-4.62", "None at company level", "Partly"),
    ("R6", "Peso depreciates less than assumed in North America", "Financial", 3, 3, "-1.12 per point of growth", "42% of debt in USD; net-investment hedges", "No"),
    ("R7", "USMCA not renewed; tariffs on inputs or Mexican goods", "Regulatory", 3, 2, "Not quantified", "Local production in each market", "Partly"),
    ("R8", "GLP-1 drugs and health habits lower volume", "Market", 3, 2, "-1.84 per -50 bp of growth", "Protein, clean label, smaller portions", "No"),
    ("R9", "Controlled-company governance: no multiple convergence", "Governance", 4, 2, "Inside R5 (0.5x = -5.90)", "Audit committee 5/5 independent; CEO and chair split", "Yes"),
    ("R10", "Canada Bread antitrust class actions, no provision", "Governance", 2, 1, "-0.24 per MXN 1bn", "Claim against Maple Leaf above CAD 2bn", "No"),
    ("R11", "US multi-employer pension plan liabilities", "Financial", 2, 1, "In the bridge", "Withdrawals negotiated; liability MXN 985m", "Yes"),
    ("R12", "Water stress; packaging law; Scope 3 target missed", "ESG", 4, 1, "-1.43 per MXN 1bn a year", "Treated-water reuse; 99% recyclable packaging", "Partly"),
    ("R13", "Cyber attack on plants or routes", "Operational", 2, 2, "Not quantified", "Insurance with exclusions", "No"),
    ("R14", "Argentina, Venezuela and Russia exposure", "Operational", 2, 1, "Latin America is 6% of EBITDA", "Venezuela deconsolidated; IAS 29 in Argentina", "Yes"),
]


def risks() -> str:
    rows = [[a, b, c, str(p), str(i), v, m, pr] for a, b, c, p, i, v, m, pr in RISK_ROWS]
    return table(["#", "Risk", "Type", "P", "I", "Value impact, MXN/share", "Mitigation", "Priced in?"], rows, fs=FS_APP,
                 aligns=["l", "l", "l", "c", "c", "l", "l", "l"], widths=["4%", "27%", "9%", "3%", "3%", "19%", "27%", "8%"],
                 note="Probability (P) and impact (I): 1 low, 5 high. Value impacts in MXN per share on the DCF of MXN 46.42. Source: team estimate (P, I, priced-in); team model (value impacts); Grupo Bimbo (2026a, 2026d).")


def esg_sp() -> str:
    hdr = ["S&P Global ESG score"] + [str(y) for y in D.SP_YEARS]
    rows = [["Total"] + [str(v) for v in D.SP_TOTAL], ["Environmental"] + [str(v) for v in D.SP_E], ["Social"] + [str(v) for v in D.SP_S],
            ["Governance & economic"] + [str(v) for v in D.SP_G]]
    t = table(hdr, rows, fs=FS_APP, bold_rows=(0,), widths=["20%"] + ["5.7%"] * 14, title="S&P Global ESG score history",
              note="Source: S&P Capital IQ (2026), ESG scores history 2013-2026.")
    rows2 = [["ESG combined score (grade)", "84.62 (A)"], ["Environmental pillar", "87.62"], ["Social pillar", "87.35"], ["Governance pillar (grade)", "76.59 (A-)"],
             ["Rank in food and tobacco", "12 of 416"], ["Emissions, Scope 1 (kt CO2e): 2019 restated / 2025 prelim.", "1,224 / 1,241"],
             ["Emissions, Scope 3 (kt CO2e): 2019 restated / 2025 prelim.", "11,424 / 11,764"]]
    t2 = table(["LSEG and emissions data", "Value"], rows2, fs=FS_APP, aligns=["l", "r"], widths=["72%", "28%"], title="LSEG scores (FY2024) and emissions",
               note="Source: LSEG (2026); Grupo Bimbo (2026e, p. 169).")
    return t + t2


def gov_detail() -> str:
    rows = [["A Controlling shareholder", "5/10", "Six vehicles hold 72.03%; one share, one vote; unexplained 8.5-point gap against a 2022 investor deck (81%)"],
            ["B Board independence", "10/20", "7 of 18 independent (38.9%); executive family chair with casting vote; 7 Servitje directors"],
            ["C Committees", "6/8", "Audit committee 5 of 5 independent; nomination and remuneration committee 2 of 4 independent, chaired by a family member"],
            ["D Related parties", "5/8", "MXN 9,823 million (2.3% of sales); conflict policy excludes directors and shareholders"],
            ["E Takeover defences", "1/10", "Board approval for transfers at 3%; tender trigger at 30%; 10% to call a meeting (36% of free float); no say on pay"],
            ["F Pay, ethics, audit", "4/8", "No individual pay disclosure; UNGC violation flags FY2022 and FY2024; auditor EY (Mancera), clean opinion"]]
    return table(["Governance scorecard (team rubric)", "Score", "Main evidence"], rows, fs=FS_APP, aligns=["l", "c", "l"], widths=["24%", "7%", "69%"],
                 title="Governance scorecard: 31 of 64 points (48%)",
                 note="Source: Grupo Bimbo (2026a, 2026f, 2026g); LSEG (2026); team estimate (scores). The rubric is ours, not a standard.")


BOARD = [("Daniel Javier Servitje Montull", 66, "No", "2013 (chair)", "Executive Chairman since May 2024; Finance"),
         ("Raul Ignacio Obregon Servitje", 53, "No", "2024", "Deputy CEO; Finance"),
         ("Luis Jorba Servitje", 67, "No", "2013", "Nominating and Remuneration chair; Finance"),
         ("Guillermo Lerdo de Tejada Servitje", 41, "No", "2023", "Wealth-advisory firm partner"),
         ("Jordi Mariscal Servitje", 54, "No", "2024", "Film producer"),
         ("Maria del Pilar Mariscal Servitje", 56, "No", "2022", "Finance; Leon XIII Foundation"),
         ("Roberto Mauricio Servitje Labarrere", 42, "No", "2025", "Finance; Grupo Altex"),
         ("Mireya Jorba Aliacar", 45, "No", "2024", "Former Grupo Bimbo treasury"),
         ("Lorenzo Sendra Creixell", 52, "No", "2023", "17+ years at Grupo Bimbo"),
         ("Jose Roberto Quiroz Mata", 37, "No", "2024", "Property management"),
         ("Javier de Pedro Espinola", 62, "No", "n/g", "Nominating, Remuneration, Finance"),
         ("Edmundo Miguel Vallejo Venegas", 68, "Yes", "n/g", "Audit chair since 2015; Governance chair"),
         ("Jaime Antonio El Koury", 72, "Yes", "2016", "Audit; Governance"),
         ("Maria Luisa Jorda Castro", 62, "Yes", "n/g", "Audit, Nominating, Remuneration"),
         ("Juana Francisca de Chantal Llano Cadavid", 46, "Yes", "2023", "Audit; Suramericana president"),
         ("Maria Eugenia Casar Perez", 66, "Yes", "2024", "Audit; former UN CFO"),
         ("Rogelio Miguel Rebolledo Rojas", 81, "Yes", "n/g", "Finance chair since 2022; ex-PepsiCo"),
         ("Leon Lawrence Kraig Eskenazi", None, "Yes", "2026", "Former Mars executive; IGNIA")]


def board() -> str:
    rows = [[n, "n/a" if a is None else str(a), i, s, r] for n, a, i, s, r in BOARD]
    return table(["Director", "Age", "Independent", "Since", "Role and committees"], rows, fs=FS_APP, aligns=["l", "c", "c", "c", "l"],
                 widths=["32%", "6%", "11%", "11%", "40%"], hl_rows=tuple(range(11, 18)),
                 note="Source: LSEG (2026), officers and directors; Grupo Bimbo (2026a). n/g = not given. Independent directors are shown in bold blue.")


REFS = [
    "Bakery & Snacks (2026) 'Private label widens lead over national brands in 2026 grocery unit sales', <i>Bakery &amp; Snacks</i>, 9 July.",
    "Damodaran, A. (2026) <i>Country default spreads and risk premiums</i> (July 2026 update); <i>Betas by sector, global</i> (5 January 2026); <i>Implied equity risk premium</i> (1 October 2026). New York University Stern School of Business.",
    "Flowers Foods, Inc. (2026) <i>Annual report on Form 10-K for fiscal 2025</i> and <i>second quarter 2026 results and fact sheet</i>. Thomasville, GA.",
    "Grupo Bimbo, S.A.B. de C.V. (2025) <i>Quarterly earnings releases, 1Q22 to 3Q25</i>. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026a) <i>Reporte anual 2025</i> [Annual report 2025 to the Bolsa Mexicana de Valores], dated 30 April 2026. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026b) <i>Grupo Bimbo reporta resultados del 4T25</i> [4Q25 results release], 25 February. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026c) <i>Grupo Bimbo reporta resultados del 1T26</i> [1Q26 results release], 29 April. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026d) <i>Grupo Bimbo reporta resultados del 2T26</i> [2Q26 results release], 23 July. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026e) <i>Informe anual integrado 2025 'Celebramos'</i> [Integrated report 2025]. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026f) <i>Estados financieros consolidados auditados 2025</i> [Audited consolidated financial statements 2025]. Mexico City.",
    "Grupo Bimbo, S.A.B. de C.V. (2026g) <i>Estatutos sociales</i> [Corporate by-laws], deed 119069, 6 May. Mexico City.",
    "IMF (2026) <i>World economic outlook, October 2026</i>. Washington, DC: International Monetary Fund.",
    "IndexBox (2026) 'USDA grain futures and canola bids report for October 7, 2026'. IndexBox.",
    "Investing.com (2026) 'Flowers Foods Q2 2026 slides: volume drops 5.8% amid category pressure' and Q2 2026 earnings call transcript, August.",
    "LSEG (2026) <i>ESG scores, controversies, officers and directors, and ownership data for Grupo Bimbo</i>. London Stock Exchange Group. Accessed October 2026.",
    "S&amp;P Capital IQ (2026) <i>ESG scores history, consensus estimates, ownership, rates and peer data</i>. S&amp;P Global Market Intelligence. Accessed 16-19 October 2026.",
    "Team model (2026) Consolidated DCF, three-statement model, WACC and peer workbooks for Grupo Bimbo [unpublished team workbooks].",
    "Trading Economics (2026) <i>Wheat</i>, 8 October. Available at: tradingeconomics.com/commodity/wheat.",
]


def refs() -> str:
    items = REFS_ES if i18n.ES_ON else REFS
    return "".join(f'<p style="margin:0 0 2.2pt 8pt;text-indent:-8pt;font-size:{FS_APP + 0.4}pt">{r}</p>' for r in items)


REFS_ES = [
    "Bakery &amp; Snacks (2026) 'Private label widens lead over national brands in 2026 grocery unit sales', <i>Bakery &amp; Snacks</i>, 9 de julio.",
    "Damodaran, A. (2026) <i>Country default spreads and risk premiums</i> (actualización de julio de 2026); <i>Betas by sector, global</i> (5 de enero de 2026); <i>Implied equity risk premium</i> (1 de octubre de 2026). Escuela de Negocios Stern, Universidad de Nueva York.",
    "Flowers Foods, Inc. (2026) <i>Annual report on Form 10-K for fiscal 2025</i> y <i>second quarter 2026 results and fact sheet</i>. Thomasville, GA.",
    "Grupo Bimbo, S.A.B. de C.V. (2025) <i>Reportes trimestrales de resultados, 1T22 a 3T25</i>. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026a) <i>Reporte anual 2025</i> [reporte anual 2025 a la Bolsa Mexicana de Valores], con fecha 30 de abril de 2026. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026b) <i>Grupo Bimbo reporta resultados del 4T25</i> [reporte de resultados del 4T25], 25 de febrero. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026c) <i>Grupo Bimbo reporta resultados del 1T26</i> [reporte de resultados del 1T26], 29 de abril. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026d) <i>Grupo Bimbo reporta resultados del 2T26</i> [reporte de resultados del 2T26], 23 de julio. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026e) <i>Informe anual integrado 2025 'Celebramos'</i>. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026f) <i>Estados financieros consolidados auditados 2025</i>. Ciudad de México.",
    "Grupo Bimbo, S.A.B. de C.V. (2026g) <i>Estatutos sociales</i>, escritura 119069, 6 de mayo. Ciudad de México.",
    "IMF (2026) <i>World economic outlook, October 2026</i>. Washington, DC: Fondo Monetario Internacional.",
    "IndexBox (2026) 'USDA grain futures and canola bids report for October 7, 2026'. IndexBox.",
    "Investing.com (2026) 'Flowers Foods Q2 2026 slides: volume drops 5.8% amid category pressure' y transcripción de la llamada de resultados del 2T26, agosto.",
    "LSEG (2026) <i>ESG scores, controversies, officers and directors, and ownership data for Grupo Bimbo</i>. London Stock Exchange Group. Consultado en octubre de 2026.",
    "S&amp;P Capital IQ (2026) <i>ESG scores history, consensus estimates, ownership, rates and peer data</i>. S&amp;P Global Market Intelligence. Consultado del 16 al 19 de octubre de 2026.",
    "Modelo del equipo (2026) DCF, WACC y comparables de Grupo Bimbo [hojas de cálculo del equipo, no publicadas].",
    "Trading Economics (2026) <i>Wheat</i>, 8 de octubre. Disponible en: tradingeconomics.com/commodity/wheat.",
]

REGISTRY = {"keydata": keydata, "forecast": forecast, "wacc": wacc, "results": results, "multiple_er": multiple_er, "ratios": ratios,
            "is": is_, "bs": bs, "cf": cf, "dcf": dcf, "crp": crp, "sens_exit": sens_exit, "sens_gordon": sens_gordon, "comps": comps,
            "segments": segments, "risks": risks, "esg_sp": esg_sp, "gov_detail": gov_detail, "board": board, "refs": refs}

if __name__ == "__main__":
    for k, f in REGISTRY.items():
        h = f()
        print(f"{k:12s} {len(h):6d} chars")

if i18n.ES_ON:
    REGISTRY = {k: (lambda f=f: i18n.tr_html(f())) for k, f in list(REGISTRY.items())}
