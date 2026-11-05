"""Numbers and charts for report v2 (CFA Research Challenge, Grupo Bimbo), from the TP12m workbook only.

Single source of valuation figures (memory.md, 2026-10-28):
analisis-dcf-2026-10-26/precio-objetivo/BIMBOA_statements_2021-2030_v2_pivot_waccV2_TP12m_v3_taxNCI.xlsx

Run (from the project root):  .venv/bin/python report/build/tp12m_data_charts.py
Writes report/data/tp12m_numbers.json and report/charts/tp12m/*.png (Bimbo palette, sized for A4 Word).
The script re-computes the 12-month target with a Python replica of sheet Valuacion_12m and stops if the replica does not
reproduce the workbook (target, WACC +/- 0.5 pp), so every sensitivity below is tied to the workbook.
Nothing here reads the archived v1-v3 engine files.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from report_style import (AMBER, BLUE, BROWN, GRAY, GRID, INK, LIGHT, NAVY, PALE_BLUE, PINK, RED, SKY, TEAL,  # noqa: E402
                          setup_matplotlib)

ROOT = Path(__file__).resolve().parents[2]
WB = ROOT / "analisis-dcf-2026-10-26/precio-objetivo/BIMBOA_statements_2021-2030_v2_pivot_waccV2_TP12m_v3_taxNCI.xlsx"
OUT_CH = ROOT / "report/charts/tp12m"
OUT_JSON = ROOT / "report/data/tp12m_numbers.json"
PEERS = ROOT / "report/data/peers_v3.json"
PRICES = ROOT / "data/market/bimbo_ipc_monthly_2021-11_2026-10.csv"

plt = setup_matplotlib()
plt.rcParams.update({"font.size": 7.5, "axes.labelsize": 7.5, "xtick.labelsize": 7.2, "ytick.labelsize": 7.2,
                     "legend.fontsize": 7.2})
FS = 7.2
W_HALF, W_FULL = 3.45, 7.0
YEARS = ["FY21A", "FY22A", "FY23A", "FY24A", "FY25A", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E"]
COLS = "BCDEFGHIJK"
PRICE_REF = 67.27                   # close of 4-Nov-2026 (Yahoo Finance), the cut-off date of the report; the 27-Oct-2026 close was 64.85

wb = openpyxl.load_workbook(WB, data_only=True)


def row(sheet: str, r: int, cols: str = COLS) -> list[float]:
    ws = wb[sheet]
    return [ws[f"{c}{r}"].value for c in cols]


# ---------------------------------------------------------------------------------------------------- statements
sales = row("IS", 6)
ebitda = row("IS", 39)
margin = [e / s for e, s in zip(ebitda, sales)]
debt = [a + b for a, b in zip(row("BS", 25), row("BS", 35))]
leases = [a + b for a, b in zip(row("BS", 28), row("BS", 36))]
cash = row("BS", 6)
net_debt = [d + l - c for d, l, c in zip(debt, leases, cash)]
lev = [n / e for n, e in zip(net_debt, ebitda)]
seg = {k: row("Segments", r, "BCDEF") for k, r in (("mx", 61), ("na", 62), ("latam", 63), ("eaa", 64), ("all", 65))}
seg_sales = {k: row("Segments", r) for k, r in (("mx", 6), ("na", 7), ("latam", 8), ("eaa", 9))}
seg_ebitda = {k: wb["Segments"][f"F{r}"].value for k, r in (("mx", 53), ("na", 54), ("latam", 55), ("eaa", 56))}

# ---------------------------------------------------------------------------------------------------- DCF replica
V = wb["Valuacion_12m"]
VA = wb["Valuacion"]
WACC = V["B20"].value
G = V["B18"].value
RONIC = V["B19"].value
KE = V["B45"].value
SHARES = V["B48"].value
KE_F = V["B46"].value
EBIT = [V[f"{c}6"].value for c in "BCD"]
DA = [V[f"{c}10"].value for c in "BCD"]
CAPEX = [V[f"{c}11"].value for c in "BCD"]
NEWL = [V[f"{c}12"].value for c in "BCD"]
NWC = [V[f"{c}13"].value for c in "BCD"]
CLAIMS = sum(V[f"B{r}"].value for r in range(35, 41))  # signed items of the bridge (rows 35-40)
SALES_FWD = sales[7:10]
TAX = V["B7"].value                 # operating tax rate of the workbook (Assumptions B538; v3: the 32.7% effective rate)


def tp_b(wacc=WACC, g=G, ronic=RONIC, d_margin=0.0, d_capex=0.0, nopat_scale_terminal=1.0, d_cash_27=0.0, follow_ronic=True) -> float:
    """12-month target, method B (value at 31-Dec-2027 brought to 16-Oct-2027 with ke); claims and ke factor held."""
    fcff, nopat = [], []
    for i in range(3):
        ebit = EBIT[i] + d_margin * SALES_FWD[i]
        n = ebit * (1 - TAX)
        nopat.append(n)
        fcff.append(n + DA[i] + CAPEX[i] - d_capex * SALES_FWD[i] + NEWL[i] + NWC[i])
    pv = sum(f / (1 + wacc) ** (i + 0.5) for i, f in enumerate(fcff))
    n31 = nopat[2] * nopat_scale_terminal * (1 + g)
    if d_margin and follow_ronic:  # the workbook sets the terminal RONIC to the FY2030E return on tangible capital (Assumptions B697), so it moves with NOPAT
        ronic = ronic * nopat[2] / (EBIT[2] * (1 - TAX))
    tv = n31 * (1 - g / ronic) / (wacc - g)
    ev = pv + tv / (1 + wacc) ** 2.5
    eq = (ev + CLAIMS + d_cash_27) * KE_F
    return eq / SHARES


def tv_share(wacc=WACC) -> float:
    pv = sum(((EBIT[i] * (1 - TAX) + DA[i] + CAPEX[i] + NEWL[i] + NWC[i]) / (1 + wacc) ** (i + 0.5)) for i in range(3))
    n31 = EBIT[2] * (1 - TAX) * (1 + G)
    tv = n31 * (1 - G / RONIC) / (wacc - G) / (1 + wacc) ** 2.5
    return tv / (pv + tv)


TP = tp_b()
assert abs(TP - V["B49"].value) < 1e-6, (TP, V["B49"].value)
assert abs(tp_b(wacc=V["B63"].value) - V["B65"].value) < 1e-6
assert abs(tp_b(wacc=V["B64"].value) - V["B66"].value) < 1e-6
assert abs(tv_share() - V["B34"].value) < 1e-6

# ---------------------------------------------------------------------------------------------------- values for the report
DIV = V["B52"].value
tp_lo, tp_hi = V["B66"].value, V["B65"].value          # WACC +0.5 pp (low) and -0.5 pp (high)
dcf_today = VA["B59"].value
dcf_lo, dcf_hi = VA["B65"].value, VA["B64"].value
ronic_min, ronic_avg = VA["B66"].value, VA["B67"].value
trig_buy, trig_sell = V["C76"].value, V["C77"].value
ret_base = (TP + DIV) / PRICE_REF - 1            # returns at the reference price of 4-Nov-2026
ret_lo, ret_hi = (tp_lo + DIV) / PRICE_REF - 1, (tp_hi + DIV) / PRICE_REF - 1

# peers: EV/EBITDA medians on the team's claim basis (report/data/peers_v3.json, 16-Oct-2026), applied to LTM Sep-26 EBITDA
peers = json.load(open(PEERS))
m_core = peers["medians"]["core_median"]["ev_ebitda_ltm"]
m_all = peers["medians"]["all_median"]["ev_ebitda_ltm"]
A = wb["Assumptions"]
ltm_ebitda = A["E12"].value + A["B39"].value            # 9M26 + 4Q25 adjusted EBITDA
claims_dec26 = A["B605"].value
ke_factor_today = VA["B56"].value
shares_today = VA["B58"].value


def peer_value(mult: float) -> float:
    return (mult * ltm_ebitda - claims_dec26) * ke_factor_today / shares_today


peer_lo, peer_hi = peer_value(m_core), peer_value(m_all)

# sensitivities on the 12-month target
sens = {
    "margin_m50": tp_b(d_margin=-0.005) - TP, "margin_m100": tp_b(d_margin=-0.010) - TP, "margin_p50": tp_b(d_margin=0.005) - TP,
    # capex +/-50 bp of sales from FY2028E, full workbook recalculation (Assumptions B389 = B300/B146 +/- 0.005; terminal RONIC follows
    # B697: 15.17% -> 14.72% / 15.63%), share count held at the base B48 [calc]. The replica above ignores the RONIC link (-1.46).
    "capex_p50": 232904.99168244 / 4217.11805014766 - 58.5421887220088, "capex_m50": 260853.649827028 / 4217.11805014766 - 58.5421887220088,
    "wacc_p50": tp_lo - TP, "wacc_m50": tp_hi - TP,
    "g_m50": tp_b(g=G - 0.005) - TP, "g_p50": tp_b(g=G + 0.005) - TP,
    "ronic_min": tp_b(ronic=A["B695"].value) - TP, "ronic_avg": tp_b(ronic=A["B694"].value) - TP,
    "na_ratio_zero_terminal": tp_b(nopat_scale_terminal=0.98) - TP,
    "na_ratio_hist_terminal": tp_b(nopat_scale_terminal=0.964) - TP,
}
# one-year wheat hit in FY2027E only: -100 bp on FY2027E sales, after tax at the 37% effective rate, reaches cash at Dec-27
wheat_1y = tp_b(d_cash_27=-0.01 * sales[6] * (1 - 0.37)) - TP
# TP12m_v2 already nets 4Q26 and FY2027E buybacks from the share count (B48, B59); B60 is the target without that step
buyback_adj = V["B60"].value - TP

grid_w = [-0.010, -0.005, 0.0, 0.005, 0.010]
grid_g = [-0.010, -0.005, 0.0, 0.005, 0.010]
grid = [[tp_b(wacc=WACC + dw, g=G + dg) for dg in grid_g] for dw in grid_w]
grid_ronic = [[tp_b(wacc=WACC + dw, ronic=r) for r in (A["B695"].value, A["B694"].value, RONIC, 0.20)] for dw in grid_w]

bridge = {k: A[c].value for k, c in (("v1", "B703"), ("g", "B707"), ("ronic", "B708"), ("wacc", "B720"),
                                     ("v2", "B719"))}

# scenario matrix: margin x growth is not modelled by the workbook; scenarios use model levers only
scen = {
    "base": TP,
    "downside": tp_b(d_margin=-0.005, wacc=WACC + 0.005),
    "upside": tp_b(d_margin=0.005, wacc=WACC - 0.005),
}

num = {
    "sources": {"workbook": str(WB.relative_to(ROOT))},
    "price_ref": PRICE_REF, "price_date": "2026-11-04", "target_12m": TP, "upside_price": TP / PRICE_REF - 1,
    "dividend_2027": DIV, "total_return": ret_base, "rating": "BUY" if ret_lo > KE else ("SELL" if ret_hi < KE else "HOLD"), "trigger_buy": trig_buy, "trigger_sell": trig_sell,
    "ret_pess": ret_lo, "ret_opt": ret_hi, "ke": KE, "wacc": WACC, "g": G, "ronic": RONIC, "tv_share_12m": V["B34"].value,
    "tv_share_today": VA["B44"].value, "dcf_today": dcf_today, "dcf_lo": dcf_lo, "dcf_hi": dcf_hi, "tp_lo": tp_lo, "tp_hi": tp_hi,
    "method_a": V["B56"].value, "ronic_min_value": ronic_min, "ronic_avg_value": ronic_avg, "peer_lo": peer_lo, "peer_hi": peer_hi,
    "peer_core_x": m_core, "peer_all_x": m_all, "ltm_ebitda": ltm_ebitda, "tv_multiple": VA["F30"].value,
    "ev_today": VA["B43"].value, "ev_12m": V["B33"].value, "shares": SHARES, "buyback_adj": buyback_adj,
    "tp_without_buyback_adj": V["B60"].value, "sens": sens, "wheat_1y": wheat_1y, "grid_wacc": [WACC + d for d in grid_w],
    "grid_g": [G + d for d in grid_g], "grid": grid, "grid_ronic": grid_ronic, "bridge": bridge, "scen": scen,
    "years": YEARS, "sales": sales, "ebitda": ebitda, "margin": margin, "net_debt": net_debt, "leverage": lev, "seg_margin": seg,
    "seg_sales": seg_sales, "seg_ebitda_fy25": seg_ebitda,
    "fcff_dec26": [VA[f"{c}17"].value for c in "BCDE"], "pv_fcff_dec26": [VA[f"{c}37"].value for c in "BCDE"],
    "eq_claims_dec26": claims_dec26,
}
OUT_JSON.write_text(json.dumps(num, indent=1))

# ---------------------------------------------------------------------------------------------------- charts


def fig(w=W_HALF, h=2.3):
    f = plt.figure(figsize=(w, h), layout="constrained")
    f.get_layout_engine().set(w_pad=4 / 72, h_pad=4 / 72)
    return f


def save(f, name):
    OUT_CH.mkdir(parents=True, exist_ok=True)
    f.savefig(OUT_CH / f"{name}.png", dpi=250)
    plt.close(f)


def rev_margin():
    f = fig(W_HALF, 2.25)
    ax = f.add_subplot(111)
    x = range(len(YEARS))
    ax.bar(x, [s / 1000 for s in sales], color=[BLUE] * 5 + [PALE_BLUE] * 5, edgecolor=[BLUE] * 5 + [BLUE] * 5, linewidth=0.5, width=0.7)
    ax.set_ylim(0, 800)
    ax.set_yticks([0, 200, 400])
    ax.set_ylabel("Net sales, MXN bn", loc="bottom")
    ax.set_xticks(list(x), [y.replace("FY", "") for y in YEARS], rotation=90)
    a2 = ax.twinx()
    a2.plot(list(x), [m * 100 for m in margin], color=RED, marker="o", ms=3, lw=1.4)
    a2.set_ylim(8, 16.5)
    a2.set_yticks([13, 14, 15, 16])
    a2.set_ylabel("Adj. EBITDA margin, %", loc="top")
    a2.spines["right"].set_visible(True)
    a2.spines["right"].set_color(LIGHT)
    for i in (0, 4, 5, 9):
        a2.text(i, margin[i] * 100 + 0.35, f"{margin[i]*100:.1f}", ha="center", color=RED, fontsize=FS)
    from matplotlib.patches import Patch
    f.legend([Patch(facecolor=BLUE), Patch(facecolor=PALE_BLUE, edgecolor=BLUE, linewidth=0.5), plt.Line2D([], [], color=RED, marker="o", ms=3)],
             ["Actual", "Forecast", "Margin"], loc="outside lower center", ncol=3, handlelength=1.0)
    save(f, "rev_margin")


def price_tp():
    rows = list(csv.DictReader(open(PRICES)))
    months = [r["month_end"] for r in rows]
    px = [float(r["bimbo_close_mxn"]) for r in rows]
    f = fig(W_FULL, 2.2)
    ax = f.add_subplot(111)
    ax.plot(range(len(px)), px, color=BLUE, lw=1.4)
    ax.plot([len(px) - 1, len(px)], [px[-1], PRICE_REF], color=BLUE, lw=1.4)
    ax.axhline(TP, color=RED, ls="--", lw=1.0)
    ax.text(0.5, TP + 1.0, f"12-month target MXN {TP:.2f}", color=RED, fontsize=FS + 0.3, va="bottom")
    ax.scatter([len(px)], [PRICE_REF], color=RED, zorder=5, s=14)
    ax.text(len(px) - 0.5, 46.0, f"MXN {PRICE_REF:.2f} (4-Nov-26)", color=INK, fontsize=FS, ha="right")
    ticks = [i for i, m in enumerate(months) if m.endswith(("-03", "-09"))]
    ax.set_xticks(ticks, [months[i][2:4] + "/" + months[i][5:7] for i in ticks])
    ax.set_ylabel("MXN per share")
    ax.set_ylim(40, max(px) + 6)
    ax.grid(axis="y", color=GRID, lw=0.5)
    save(f, "price_tp")


def football():
    f = fig(W_FULL, 2.7)
    ax = f.add_subplot(111)
    ax.axvspan(30, trig_buy, color="#E2F1EF")
    ax.axvspan(trig_buy, trig_sell, color="#FDF1DA")
    ax.axvspan(trig_sell, 90, color="#FBE3E7")
    for xm, lab, c in (((30 + trig_buy) / 2, "BUY", TEAL), ((trig_buy + trig_sell) / 2, "HOLD", "#B07A12"), ((trig_sell + 90) / 2, "SELL", PINK)):
        ax.text(xm, 6.85, lab, ha="center", color=c, fontweight="bold", fontsize=8)
    rows = [
        ("12-month target, method B\n(WACC +/- 0.5 pp)", tp_lo, tp_hi, TP, BLUE),
        ("DCF today, 16-Oct-2026\n(WACC +/- 0.5 pp)", dcf_lo, dcf_hi, dcf_today, BLUE),
        ("DCF today, terminal RONIC\n(historic low to model 15.75%)", ronic_min, dcf_today, dcf_today, BLUE),
        ("Peers, EV/EBITDA core median\n5.5x to eligible median 8.3x", peer_lo, peer_hi, None, SKY),
        ("52-week trading range", 53.03, 68.67, None, GRAY),
        ("Analyst targets (12), median 69.5", 51.0, 87.0, 69.5, GRAY),
    ]
    for i, (lab, lo, hi, mid, c) in enumerate(rows):
        y = 5.8 - i
        ax.barh(y, hi - lo, left=lo, height=0.5, color=c)
        ax.text(lo - 0.6, y, f"{lo:.1f}", ha="right", va="center", fontsize=FS)
        ax.text(hi + 0.8, y, f"{hi:.1f}", ha="left", va="center", fontsize=FS)
        if mid is not None:
            ax.plot([mid, mid], [y - 0.25, y + 0.25], color="white", lw=1.6)
    ax.axvline(PRICE_REF, color=RED, ls="--", lw=1.3)
    ax.text(PRICE_REF + 0.5, -0.65, f"price {PRICE_REF:.2f}", color=RED, fontsize=FS, fontweight="bold")
    ax.axvline(TP, color=NAVY, ls=":", lw=1.3)
    ax.text(TP + 0.5, -1.15, f"target {TP:.2f}", color=NAVY, fontsize=FS, fontweight="bold")
    ax.set_xlim(30, 90)
    ax.set_ylim(-1.5, 7.3)
    ax.set_yticks([5.8 - i for i in range(len(rows))], [r[0] for r in rows], fontsize=FS - 0.2)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("MXN per share (white tick = base case)")
    save(f, "football")


def bridge_chart():
    f = fig(W_HALF, 2.4)
    ax = f.add_subplot(111)
    steps = [("RONIC =\nWACC", bridge["v1"]), ("Terminal\ng", bridge["g"]),
             ("Terminal\nRONIC", bridge["ronic"]), ("Cost of\ncapital", bridge["wacc"]), ("Base\nDCF", bridge["v2"])]
    cum = 0.0
    for i, (lab, v) in enumerate(steps):
        if i == 0 or i == len(steps) - 1:
            ax.bar(i, v, color=BLUE, width=0.65)
            ax.text(i, v + 1, f"{v:.1f}", ha="center", fontsize=FS)
            cum = v if i == 0 else cum
        else:
            ax.bar(i, v, bottom=cum, color=RED, width=0.65)
            ax.text(i, cum + v + 1, f"+{v:.1f}", ha="center", fontsize=FS)
            cum += v
    ax.axhline(PRICE_REF, color=GRAY, ls="--", lw=0.9)
    ax.text(-0.4, PRICE_REF + 1.5, f"price {PRICE_REF:.2f}", ha="left", fontsize=FS - 0.4, color=GRAY)
    ax.set_xticks(range(len(steps)), [s[0] for s in steps], fontsize=FS - 1.2)
    ax.set_ylim(0, 72)
    ax.set_ylabel("MXN per share (DCF, 16-Oct-26)")
    save(f, "dcf_bridge")


def fcff_chart():
    f = fig(W_HALF, 2.2)
    ax = f.add_subplot(111)
    yrs = ["FY27E", "FY28E", "FY29E", "FY30E"]
    x = list(range(4))
    ax.bar([i - 0.19 for i in x], [v / 1000 for v in num["fcff_dec26"]], width=0.36, color=BLUE, label="FCFF")
    ax.bar([i + 0.19 for i in x], [v / 1000 for v in num["pv_fcff_dec26"]], width=0.36, color=RED, label="Present value")
    for i in x:
        ax.text(i - 0.19, num["fcff_dec26"][i] / 1000 + 0.5, f"{num['fcff_dec26'][i]/1000:.1f}", ha="center", fontsize=FS - 0.4)
        ax.text(i + 0.19, num["pv_fcff_dec26"][i] / 1000 + 0.5, f"{num['pv_fcff_dec26'][i]/1000:.1f}", ha="center", fontsize=FS - 0.4)
    ax.set_xticks(x, yrs)
    ax.set_ylim(0, 40)
    ax.set_ylabel("MXN bn")
    ax.legend(loc="upper left", ncol=2)
    save(f, "fcff")


def na_margin():
    q = ["1Q24", "2Q24", "3Q24", "4Q24", "1Q25", "2Q25", "3Q25", "4Q25", "1Q26", "2Q26", "3Q26"]
    m = [8.7, 9.7, 9.5, 5.9, 7.4, 9.0, 10.4, 9.2, 8.6, 10.0, 10.8]
    f = fig(W_HALF, 2.2)
    ax = f.add_subplot(111)
    ax.bar(range(len(q)), m, color=[RED if x == "4Q24" else BLUE for x in q], width=0.68)
    for i, v in enumerate(m):
        ax.text(i, v + 0.25, f"{v:.1f}", ha="center", fontsize=FS - 0.5)
    ax.set_ylim(0, 13)
    ax.set_yticks([0, 5, 10])
    ax.set_ylabel("NA adj. EBITDA margin, %")
    ax.set_xticks(range(len(q)), q, rotation=90)
    save(f, "na_margin")


def regional_margin():
    f = fig(W_HALF, 2.2)
    ax = f.add_subplot(111)
    xs = ["FY21", "FY22", "FY23", "FY24", "FY25"]
    for k, c, lab in (("mx", RED, "Mexico"), ("na", BLUE, "North America"), ("eaa", TEAL, "Europe, Asia & Africa"),
                      ("latam", AMBER, "Latin America"), ("all", GRAY, "Group")):
        ax.plot(xs, [v * 100 for v in seg[k]], marker="o", ms=3, lw=1.3 if k != "all" else 1.0, color=c, ls="-" if k != "all" else "--", label=lab)
        ax.text(4.08, seg[k][4] * 100, f"{seg[k][4]*100:.1f}", fontsize=FS - 0.5, color=c, va="center")
    ax.set_xlim(-0.2, 4.6)
    ax.set_ylim(4, 22)
    ax.set_ylabel("Adj. EBITDA margin, %")
    ax.legend(loc="upper left", ncol=2, fontsize=FS - 0.8)
    save(f, "regional_margin")


def leverage_chart():
    f = fig(W_HALF, 2.2)
    ax = f.add_subplot(111)
    x = list(range(10))
    ax.plot(x[:5], lev[:5], color=BLUE, marker="o", ms=3, lw=1.5)
    ax.plot(x[4:], lev[4:], color=BLUE, marker="o", ms=3, lw=1.5, ls=":")
    for i in (0, 3, 4, 9):
        ax.text(i, lev[i] + 0.12, f"{lev[i]:.2f}x", ha="center", fontsize=FS - 0.3, color=NAVY)
    ax.set_xticks(x, [y[2:] for y in YEARS], rotation=90)
    ax.set_ylim(0.5, 3.8)
    ax.set_ylabel("Net debt incl. leases / adj. EBITDA")
    save(f, "leverage")


def sens_heat():
    f = fig(W_HALF, 2.3)
    ax = f.add_subplot(111)
    import numpy as np
    arr = np.array(grid)
    from matplotlib.colors import LinearSegmentedColormap
    cm = LinearSegmentedColormap.from_list("b", ["#FBE3E7", "#FFFFFF", PALE_BLUE])
    ax.imshow(arr, cmap=cm, vmin=PRICE_REF - 25, vmax=PRICE_REF + 40, aspect="auto")
    for i in range(5):
        for j in range(5):
            ax.text(j, i, f"{arr[i, j]:.1f}", ha="center", va="center", fontsize=FS, fontweight="bold" if (i == 2 and j == 2) else None,
                    color=RED if arr[i, j] < PRICE_REF else INK)
    ax.set_xticks(range(5), [f"{g*100:.1f}%" for g in num["grid_g"]])
    ax.set_yticks(range(5), [f"{w*100:.2f}%" for w in num["grid_wacc"]])
    ax.set_xlabel("Terminal growth g")
    ax.set_ylabel("WACC")
    for s in ax.spines.values():
        s.set_visible(False)
    save(f, "sensitivity")


def growth_organic():
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    R = wb["Ratios_9M26"]
    O = wb["Organic_pass"]
    regions = ["North America", "Mexico", "Latin America", "Europe, Asia\n& Africa"]
    rep = [R["B12"].value, R["B13"].value, R["B14"].value, R["B15"].value]
    org = [O["B17"].value, O["B18"].value, O["B19"].value, O["B20"].value]
    x = range(4)
    ax.bar([i - 0.19 for i in x], [v * 100 for v in rep], width=0.36, color=BLUE, label="Reported, ex-FX")
    ax.bar([i + 0.19 for i in x], [v * 100 for v in org], width=0.36, color=RED, label="Excluding acquisitions")
    for i in x:
        ax.text(i - 0.19, rep[i] * 100 + 0.3, f"{rep[i]*100:.1f}", ha="center", fontsize=FS - 0.3)
        ax.text(i + 0.19, org[i] * 100 + 0.3, f"{org[i]*100:.1f}", ha="center", fontsize=FS - 0.3)
    ax.set_xticks(list(x), regions, fontsize=FS - 0.6)
    ax.set_ylim(0, 17.5)
    ax.set_ylabel("Net sales growth 9M26, % y/y")
    ax.legend(loc="upper left", fontsize=FS - 0.6)
    save(f, "growth_organic")


def margins_gross_ebitda():
    f = fig(W_HALF, 2.25)
    ax = f.add_subplot(111)
    I = wb["IS"]
    gm = [I[f"{c}8"].value / I[f"{c}6"].value * 100 for c in COLS]
    x = list(range(10))
    ax.plot(x[:5], gm[:5], color=BLUE, marker="o", ms=3, lw=1.5)
    ax.plot(x[4:], gm[4:], color=BLUE, marker="o", ms=3, lw=1.5, ls=":", label="Gross margin")
    em = [m * 100 for m in margin]
    ax2 = ax.twinx()
    ax2.plot(x[:5], em[:5], color=RED, marker="o", ms=3, lw=1.5)
    ax2.plot(x[4:], em[4:], color=RED, marker="o", ms=3, lw=1.5, ls=":", label="Adj. EBITDA margin")
    ax.set_ylim(50.5, 54.5)
    ax2.set_ylim(12, 16)
    ax.set_xticks(x, [y[2:] for y in YEARS], rotation=90)
    ax.set_ylabel("Gross margin, %", color=BLUE)
    ax2.set_ylabel("Adj. EBITDA margin, %", color=RED)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(LIGHT)
    ax.text(6, gm[6] - 0.45, f"{gm[6]:.1f}", ha="center", fontsize=FS - 0.3, color=BLUE)
    ax.text(5, gm[5] + 0.2, f"{gm[5]:.1f}", ha="center", fontsize=FS - 0.3, color=BLUE)
    ax2.text(6, em[6] + 0.25, f"{em[6]:.1f}", ha="center", fontsize=FS - 0.3, color=RED)
    ax2.text(4, em[4] - 0.55, f"{em[4]:.1f}", ha="center", fontsize=FS - 0.3, color=RED)
    save(f, "margins")


def wheat_costs():
    f = fig(W_HALF, 2.25)
    ax = f.add_subplot(111)
    A = wb["Assumptions"]
    labels = ["2024", "2025", "2026E", "Sep-26\nspot"]
    vals = [A["B273"].value, A["B274"].value, A["B277"].value, A["B276"].value]
    cols = [BLUE, BLUE, PALE_BLUE, RED]
    ax.bar(range(4), vals, color=cols, edgecolor=[BLUE, BLUE, BLUE, RED], linewidth=0.6, width=0.62)
    for i, v in enumerate(vals):
        ax.text(i, v + 5, f"{v:.0f}", ha="center", fontsize=FS - 0.2)
    ax.axhline(vals[2], color=GRAY, ls="--", lw=0.9)
    ax.text(-0.45, vals[2] + 7, "model 2027E, held flat", ha="left", fontsize=FS - 1.0, color=GRAY)
    ax.annotate("+25.9%", xy=(2, vals[2] + 22), ha="center", fontsize=FS, color=RED, fontweight="bold")
    ax.set_xticks(range(4), labels, fontsize=FS - 0.4)
    ax.set_ylim(0, 290)
    ax.set_ylabel("Wheat, US$ per tonne")
    save(f, "wheat_costs")


def gm_wheat_scenarios():
    """Gross margin FY21A-FY30E: model, wheat at the Sep-2026 spot and wheat +35% from 2027, against the FY23A low."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    I, A = wb["IS"], wb["Assumptions"]
    gm = [I[f"{c}8"].value / I[f"{c}6"].value * 100 for c in COLS]
    e, r27, w26, spot = A["B272"].value, A["B286"].value, A["B277"].value, A["B276"].value
    pp_spot = r27 * ((spot / w26) ** e - 1) * 100
    pp_35 = r27 * (1.35 ** e - 1) * 100
    x = list(range(10))
    ax.axhline(min(gm[:5]), color=GRAY, ls="--", lw=0.9)
    ax.text(0.05, min(gm[:5]) - 0.2, f"FY23A low {min(gm[:5]):.1f}", ha="left", va="top", fontsize=FS - 1.0, color=GRAY)
    ax.plot(x[:5], gm[:5], color=BLUE, marker="o", ms=3, lw=1.5)
    ax.plot(x[4:], gm[4:], color=BLUE, marker="o", ms=3, lw=1.5, ls=":", label="Model")
    for pp, col, lab in ((pp_spot, AMBER, "Wheat at Sep-26 spot, US$247"), (pp_35, RED, "Wheat +35% from 2027")):
        y = gm[:7] + [g - pp for g in gm[7:]]
        ax.plot(x[6:], y[6:], color=col, marker="o", ms=2.5, lw=1.3, label=lab)
    ax.text(9.15, gm[9], f"{gm[9]:.1f}", ha="left", va="center", fontsize=FS - 0.3, color=BLUE)
    ax.text(9.15, gm[9] - pp_spot, f"{gm[9] - pp_spot:.1f}", ha="left", va="center", fontsize=FS - 0.3, color=AMBER)
    ax.text(9.15, gm[9] - pp_35, f"{gm[9] - pp_35:.1f}", ha="left", va="center", fontsize=FS - 0.3, color=RED)
    ax.text(0, gm[0] + 0.12, f"{gm[0]:.1f}", ha="center", fontsize=FS - 0.3, color=BLUE)
    ax.text(6, gm[6] + 0.22, f"{gm[6]:.1f}", ha="center", fontsize=FS - 0.3, color=BLUE)
    ax.legend(loc="upper right", frameon=False, fontsize=FS - 1.0, handlelength=1.6, borderaxespad=0.2)
    ax.set_xlim(-0.4, 10.3)
    ax.set_ylim(50.8, 54.0)
    ax.set_xticks(x, [y[2:] for y in YEARS], rotation=90)
    ax.set_ylabel("Gross margin, %")
    save(f, "gm_wheat_scenarios")
    return pp_spot, pp_35


def growth_fx():
    """Peso net sales growth split into organic, acquisitions and FX translation: 9M26 and FY2027E-FY2030E."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    A, R, O = wb["Assumptions"], wb["Ratios_9M26"], wb["Organic_pass"]
    # 9M26: the 12 region-quarter cells of Organic_pass, weighted by prior-year quarter sales (v33: 4.443 / 3.368 / 1.075 [calc])
    wq = [O[f"C{r}"].value for r in range(3, 15)]
    rep9 = sum(c * O[f"D{r}"].value for c, r in zip(wq, range(3, 15))) / sum(wq) * 100
    org9 = sum(c * O[f"H{r}"].value for c, r in zip(wq, range(3, 15))) / sum(wq) * 100
    peso9 = -2.2  # 9M26 net sales in pesos, 3Q26 release (Grupo Bimbo, 2026h)
    labels = ["9M26", "FY27E", "FY28E", "FY29E", "FY30E"]
    organic = [org9] + [A[f"B{r}"].value * 100 for r in (148, 174, 196, 218)]
    acq = [rep9 - org9, 0, 0, 0, 0]
    fx = [peso9 - rep9] + [A[f"B{r}"].value * 100 for r in (149, 175, 197, 219)]
    peso = [peso9] + [A[f"B{r}"].value * 100 for r in (147, 173, 195, 217)]
    x = list(range(5))
    ax.axhline(0, color=GRAY, lw=0.7)
    ax.bar(x, organic, color=BLUE, width=0.58, label="Organic")
    ax.bar(x, acq, bottom=organic, color=RED, width=0.58, label="Acquisitions")
    fx_bottom = [o + a if v > 0 else 0 for o, a, v in zip(organic, acq, fx)]
    ax.bar(x, fx, bottom=fx_bottom, color=AMBER, width=0.58, label="FX translation")
    ax.scatter(x, peso, marker="D", s=14, color=NAVY, zorder=5, label="Net sales growth in pesos")
    for i in x:
        top = organic[i] + acq[i] + max(fx[i], 0)
        ax.text(i, top + 0.75, f"{peso[i]:.1f}", ha="center", fontsize=FS - 0.3, color=NAVY, fontweight="bold")
        ax.text(i, organic[i] / 2, f"{organic[i]:.1f}", ha="center", va="center", fontsize=FS - 0.8, color="white")
        if fx[i] < 0:
            ax.text(i, fx[i] / 2, f"{fx[i]:+.1f}", ha="center", va="center", fontsize=FS - 0.8, color=INK)
        else:
            ax.text(i + 0.33, fx_bottom[i] + fx[i] / 2, f"{fx[i]:+.1f}", ha="left", va="center", fontsize=FS - 1.0, color=INK)
    ax.set_xticks(x, labels)
    ax.set_xlim(-0.6, 4.6)
    ax.set_ylim(-8, 9.5)
    ax.set_ylabel("Net sales growth, % y/y")
    ax.legend(loc="lower right", frameon=False, fontsize=FS - 1.2, ncol=2, handlelength=1.0, columnspacing=0.8)
    save(f, "growth_fx")
    return {"rep9": rep9, "org9": org9, "organic": organic, "fx": fx, "peso": peso}


def margin_vs_consensus():
    """Adjusted EBITDA margin in the model against the CIQ consensus mean (20-Sep-2026), FY2026E-FY2028E."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    cons = {}
    with open(ROOT / "data/capitaliq/consensus.csv", newline="", encoding="utf-8") as fh:
        for r_ in csv.DictReader(fh):
            if (r_["section"] == "Company Level (Mex$000)" and r_["period_type"] == "FY" and r_["metric"] in ("Revenue", "EBITDA")
                    and r_["stat"].startswith("Mean") and r_["value"] and r_["flag"] == "E" and r_["fiscal_year"] in ("2026", "2027", "2028")):
                cons[(r_["metric"], int(r_["fiscal_year"]))] = float(r_["value"])
    yrs = [2026, 2027, 2028]
    c_m = [cons[("EBITDA", y)] / cons[("Revenue", y)] * 100 for y in yrs]
    m_m = [margin[5] * 100, margin[6] * 100, margin[7] * 100]
    x = [0, 1, 2]
    ax.bar([i - 0.19 for i in x], m_m, width=0.36, color=BLUE, label="Model")
    ax.bar([i + 0.19 for i in x], c_m, width=0.36, color=PALE_BLUE, edgecolor=BLUE, linewidth=0.6, label="Consensus (20-Sep-26)")
    for i in x:
        ax.text(i - 0.19, m_m[i] + 0.06, f"{m_m[i]:.1f}", ha="center", fontsize=FS - 0.3)
        ax.text(i + 0.19, c_m[i] + 0.06, f"{c_m[i]:.1f}", ha="center", fontsize=FS - 0.3)
        ax.text(i, max(m_m[i], c_m[i]) + 0.38, f"{(m_m[i] - c_m[i]) * 100:+.0f} bp", ha="center", fontsize=FS - 0.3, color=RED, fontweight="bold")
    ax.axhline(15.69, color=RED, ls="--", lw=0.9)
    ax.text(3.15, 15.69 + 0.05, "3Q26 15.7", ha="right", fontsize=FS - 0.9, color=RED)
    ax.axhline(14.7, color=GRAY, ls="--", lw=0.9)
    ax.text(3.15, 14.7 + 0.05, "9M26 14.7", ha="right", fontsize=FS - 0.9, color=GRAY)
    ax.set_xticks(x, [f"FY{y}E" for y in yrs])
    ax.set_xlim(-0.6, 3.2)
    ax.set_ylim(13.5, 16.3)
    ax.set_ylabel("Adj. EBITDA margin, %")
    ax.legend(loc="upper left", frameon=False, fontsize=FS - 1.0, handlelength=1.2)
    save(f, "margin_vs_consensus")
    return c_m, m_m


def ev_regimes():
    """TEV / LTM EBITDA by year, 1999-2026 (mean of quarterly averages), CIQ; acquisition build-out 2012-2018 shaded."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    yrs = list(range(1999, 2027))
    # wiki/Valuation/ciq-long-history-multiples-and-returns.md, table 1 (S&P Capital IQ); 2026 is 1H
    m = [9.36, 6.34, 5.97, 7.03, 6.72, 7.49, 7.22, 7.14, 9.47, 8.79, 9.21, 8.93, 10.20, 11.93, 13.30, 11.98, 12.00, 11.94,
         9.34, 8.69, 7.38, 6.75, 6.33, 7.90, 8.70, 7.83, 6.84, 6.86]
    ax.axvspan(2011.5, 2018.5, color=PALE_BLUE, alpha=0.8, lw=0)
    ax.plot(yrs, m, color=BLUE, lw=1.5)
    ax.scatter([2026], [6.29], color=RED, s=16, zorder=5)
    ax.text(2025.6, 5.6, "18-Sep-26\n6.29x", ha="right", va="top", fontsize=FS - 0.8, color=RED)
    ax.text(2015, 14.3, "Acquisition build-out\n2012-18: 11.3x, ROE 7.7%", ha="center", va="center", fontsize=FS - 0.8, color=NAVY)
    ax.text(1999.3, 4.65, "2015-25: EBITDA x2.2, multiple -43%,\nnet debt x2.7, price +28%", ha="left", va="bottom", fontsize=FS - 1.1, color=INK)
    ax.set_ylim(4.5, 15.5)
    ax.set_xlim(1998.5, 2026.8)
    ax.set_ylabel("TEV / LTM EBITDA, x")
    ax.set_xticks([2000, 2005, 2010, 2015, 2020, 2025])
    save(f, "ev_regimes")


def acq_lapping():
    """Ex-FX growth incl. acquisitions against organic, Europe-Asia-Africa and Latin America, 1Q26-3Q26."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    R, O = wb["Ratios_9M26"], wb["Organic_pass"]
    rep = [R[f"E{r}"].value * 100 for r in (6, 7, 8, 3, 4, 5)]  # EAA 1Q-3Q, Latin America 1Q-3Q
    org = [O[f"H{r}"].value * 100 for r in (12, 13, 14, 9, 10, 11)]
    x = [0, 1, 2, 3.8, 4.8, 5.8]
    ax.bar([i - 0.19 for i in x], rep, width=0.36, color=BLUE, label="Reported, ex-FX")
    ax.bar([i + 0.19 for i in x], org, width=0.36, color=RED, label="Excluding acquisitions")
    for xi, a, b in zip(x, rep, org):
        ax.text(xi - 0.19, a + 0.3, f"{a:.1f}", ha="center", fontsize=FS - 1.0)
        ax.text(xi + 0.19, b + 0.3, f"{b:.1f}", ha="center", fontsize=FS - 1.0)
    ax.set_xticks(x, ["1Q", "2Q", "3Q"] * 2, fontsize=FS - 0.6)
    ax.text(1, -4.4, "Europe, Asia & Africa", ha="center", fontsize=FS - 0.6, color=INK)
    ax.text(4.8, -4.4, "Latin America", ha="center", fontsize=FS - 0.6, color=INK)
    ax.set_ylim(0, 18)
    ax.set_ylabel("Net sales growth 2026, % y/y")
    ax.legend(loc="upper center", frameon=False, fontsize=FS - 1.0, ncol=2, handlelength=1.0, bbox_to_anchor=(0.5, 1.02))
    save(f, "acq_lapping")


def cost_passthrough():
    """Change in cost of sales by nature as % of sales, FY2023 to FY2025: where the raw-material relief went."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    # EEFF25 p.82 via wiki/Macro/bimbo-input-costs.md: MXN m; FY2023 sales 399,879; FY2025 sales 426,952
    fy23 = {"Raw\nmaterials": 131052, "Salaries": 34234, "Freight,\nfuel": 17092, "Depreciation": 7698, "Other": 4293}
    fy25 = {"Raw\nmaterials": 129712, "Salaries": 40113, "Freight,\nfuel": 18374, "Depreciation": 10070, "Other": 5196}
    d = {k: fy25[k] / 426952 * 100 - fy23[k] / 399879 * 100 for k in fy23}
    labels = list(d) + ["Cost of\nsales"]
    vals = list(d.values())
    net = sum(vals)
    run = 0.0
    for i, v in enumerate(vals):
        ax.bar(i, v, bottom=run if v > 0 else run, color=BLUE if v < 0 else RED, width=0.6)
        ax.text(i, (run + v) + (0.12 if v > 0 else -0.12), f"{v:+.2f}", ha="center", va="bottom" if v > 0 else "top", fontsize=FS - 0.5)
        run += v
    ax.bar(len(vals), net, color=NAVY, width=0.6)
    ax.text(len(vals), net - 0.12, f"{net:+.2f}", ha="center", va="top", fontsize=FS - 0.5)
    absorbed = sum(v for v in vals if v > 0) / -vals[0] * 100
    ax.text(3.0, 0.62, f"{absorbed:.0f}% of the relief\nabsorbed elsewhere", ha="center", fontsize=FS - 0.6, color=RED)
    ax.axhline(0, color=GRAY, lw=0.7)
    ax.set_xticks(range(len(labels)), labels, fontsize=FS - 1.1)
    ax.set_ylim(-3.2, 1.3)
    ax.set_ylabel("Change FY23-FY25, pp of sales")
    save(f, "cost_passthrough")
    return absorbed


def na_margin_quarterly():
    """North America adjusted EBITDA margin by quarter, 1Q24-3Q26, around the change of CEO (Nov-2025)."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    # wiki/Thesis/bimbo-north-america-turnaround-evidence.md (quarterly releases)
    q = ["1Q24", "2Q24", "3Q24", "4Q24", "1Q25", "2Q25", "3Q25", "4Q25", "1Q26", "2Q26", "3Q26"]
    v = [8.7, 9.7, 9.5, 5.9, 7.4, 9.0, 10.4, 9.2, 8.6, 10.0, 10.8]
    cols = [BLUE] * 7 + [RED] * 4
    ax.bar(range(11), v, color=cols, width=0.62)
    for i, y in enumerate(v):
        ax.text(i, y + 0.15, f"{y:.1f}", ha="center", fontsize=FS - 0.8)
    ax.axvline(6.5, color=GRAY, ls="--", lw=0.9)
    ax.text(6.4, 12.9, "New CEO,\nNov-25", ha="right", va="top", fontsize=FS - 0.8, color=GRAY)
    ax.set_xticks(range(11), q, rotation=90, fontsize=FS - 0.8)
    ax.set_ylim(0, 13.2)
    ax.set_ylabel("North America adj. EBITDA margin, %")
    save(f, "na_margin_quarterly")


def guidance_scorecard():
    """Management targets set on calls since 2011: met, mixed, missed, by the period in which the target was set."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    # wiki/Thesis/bimbo-guidance-vs-delivery-2011-2026.md, section 2 (61 resolved targets)
    eras = ["2011-16", "2017-19", "2020-22", "2023-25"]
    met, mixed, missed = [4, 3, 5, 10], [4, 3, 1, 1], [17, 4, 2, 7]
    n = [a + b + c for a, b, c in zip(met, mixed, missed)]
    y = list(range(len(eras)))[::-1]
    for yi, a, b, c, t in zip(y, met, mixed, missed, n):
        ax.barh(yi, a / t * 100, color=BLUE, height=0.6)
        ax.barh(yi, b / t * 100, left=a / t * 100, color=AMBER, height=0.6)
        ax.barh(yi, c / t * 100, left=(a + b) / t * 100, color=RED, height=0.6)
        ax.text(a / t * 50, yi, f"{a}", ha="center", va="center", fontsize=FS - 0.5, color="white")
        if b:
            ax.text((a + b / 2) / t * 100, yi, f"{b}", ha="center", va="center", fontsize=FS - 0.5, color=INK)
        ax.text((a + b + c / 2) / t * 100, yi, f"{c}", ha="center", va="center", fontsize=FS - 0.5, color="white")
    ax.set_yticks(y, [f"{e} (n={t})" for e, t in zip(eras, n)], fontsize=FS - 0.5)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of targets set in each period, %")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Met"), Patch(color=AMBER, label="Mixed"), Patch(color=RED, label="Missed")],
              loc="upper center", bbox_to_anchor=(0.5, 1.16), ncol=3, frameon=False, fontsize=FS - 0.8, handlelength=1.0)
    save(f, "guidance_scorecard")


def usdmxn():
    """USD/MXN annual average 2019-2030E (S&P Capital IQ history and forecast, as in the model) and the 16-Oct-2026 spot."""
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    F, A = wb["FX"], wb["Assumptions"]
    yrs = list(range(2019, 2031))
    col = {y: 2 + (y - 2015) for y in range(2015, 2031)}
    vals = [F.cell(20, col[y]).value for y in yrs]
    vals[yrs.index(2026)] = A["B79"].value  # FY2026E: nine months actual plus 4Q26, as in the model
    spot = 18.479  # BMV/FX close of 16-Oct-2026 (data/market/usdmxn_daily_2026-09-15_2026-10-16.csv)
    ia = yrs.index(2025)
    ax.plot(yrs[: ia + 1], vals[: ia + 1], color=BLUE, marker="o", ms=3, lw=1.5)
    ax.plot(yrs[ia:], vals[ia:], color=BLUE, marker="o", ms=3, lw=1.5, ls=":")
    ax.axhline(spot, color=RED, ls="--", lw=0.9)
    ax.text(2019.1, spot + 0.18, f"spot 16-Oct-26: {spot:.2f}", fontsize=FS - 0.8, color=RED, va="bottom")
    for y in (2020, 2023, 2025, 2026, 2027, 2030):
        v = vals[yrs.index(y)]
        ax.text(y, v + (0.35 if y not in (2026,) else -0.35), f"{v:.1f}", ha="center", va="bottom" if y != 2026 else "top", fontsize=FS - 0.8, color=BLUE)
    ax.set_ylim(16, 22.5)
    ax.set_xticks([2019, 2021, 2023, 2025, 2027, 2029], ["19", "21", "23", "25", "27E", "29E"])
    ax.set_ylabel("MXN per US$, annual average")
    save(f, "usdmxn")


def acq_leverage():
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    CF = wb["CF"]
    acq = [-CF[f"{c}38"].value / 1000 for c in "BCDEF"]
    yrs = ["FY21", "FY22", "FY23", "FY24", "FY25"]
    ax.bar(range(5), acq, color=RED, width=0.6)
    for i, v in enumerate(acq):
        ax.text(i, v - 1.3, f"{v:.1f}", ha="center", fontsize=FS - 0.3, color="white", fontweight="bold")
    ax.set_ylim(0, 19)
    ax.set_ylabel("Acquisitions paid, MXN bn")
    ax.set_xticks(range(5), yrs)
    a2 = ax.twinx()
    a2.plot(range(5), lev[:5], color=BLUE, marker="o", ms=3, lw=1.5)
    for i in range(5):
        a2.text(i, lev[i] + 0.12, f"{lev[i]:.2f}x", ha="center", fontsize=FS - 0.3, color=BLUE)
    a2.set_ylim(-2.6, 3.9)
    a2.set_yticks([2, 3])
    a2.set_ylabel("Net debt incl. leases / EBITDA", color=BLUE, loc="top")
    a2.spines["right"].set_visible(True)
    a2.spines["right"].set_color(LIGHT)
    save(f, "acq_leverage")


def ebitda_bridge():
    f = fig(W_HALF, 2.0)
    ax = f.add_subplot(111)
    I = wb["IS"]
    pcs = lambda col, r: I[f"{col}{r}"].value / I[f"{col}6"].value * 100
    steps = [("Gross\nmargin", pcs("H", 8) - pcs("F", 8), BLUE),
             ("Selling,\nadmin.", -(pcs("H", 9) - pcs("F", 9)) - (pcs("H", 10) - pcs("F", 10)), BLUE),
             ("Integ.\ncosts", -(pcs("H", 11) - pcs("F", 11)), AMBER),
             ("Other\nexp.", -(pcs("H", 12) - pcs("F", 12)), AMBER)]
    da25 = I["F36"].value + I["F38"].value
    da27 = I["H36"].value + I["H38"].value
    steps.append(("D&A and\nnon-cash", (da27 / I["H6"].value - da25 / I["F6"].value) * 100, BLUE))
    start, end = pcs("F", 39), pcs("H", 39)
    ax.bar(0, start - 13, bottom=13, color=GRAY, width=0.62)
    ax.text(0, start + 0.04, f"{start:.2f}", ha="center", fontsize=FS - 0.3)
    cum = start
    for i, (lab, v, c) in enumerate(steps, start=1):
        ax.bar(i, v, bottom=cum, color=c if v >= 0 else RED, width=0.62)
        ax.text(i, max(cum, cum + v) + 0.04, f"{v*100:+.0f} bp", ha="center", fontsize=FS - 0.5)
        cum += v
    k = len(steps) + 1
    ax.bar(k, end - 13, bottom=13, color=GRAY, width=0.62)
    ax.text(k, end + 0.04, f"{end:.2f}", ha="center", fontsize=FS - 0.3)
    ax.set_xticks(range(k + 1), ["FY25A"] + [s[0] for s in steps] + ["FY27E"], fontsize=FS - 1.3)
    ax.set_ylim(13, 15.5)
    ax.set_ylabel("Adj. EBITDA margin, %")
    save(f, "ebitda_bridge")


def roic_chart():
    f = fig(W_HALF, 2.2)
    ax = f.add_subplot(111)
    A = wb["Assumptions"]
    vals = [A["B690"].value, A["B691"].value, A["B692"].value, A["B693"].value, A["B697"].value]
    labels = ["FY22A", "FY23A", "FY24A", "FY25A", "Terminal\nRONIC"]
    ax.bar(range(5), [v * 100 for v in vals], color=[BLUE] * 4 + [PALE_BLUE], edgecolor=[BLUE] * 5, linewidth=0.6, width=0.62)
    for i, v in enumerate(vals):
        ax.text(i, v * 100 + 0.35, f"{v*100:.1f}", ha="center", fontsize=FS - 0.2)
    ax.axhline(WACC * 100, color=RED, ls="--", lw=0.9)
    ax.text(4.4, WACC * 100 + 0.4, f"WACC {WACC*100:.2f}%", ha="right", fontsize=FS - 0.8, color=RED)
    ax.set_xticks(range(5), labels, fontsize=FS - 0.5)
    ax.set_ylim(0, 21)
    ax.set_ylabel("Return on tangible operating capital, %")
    save(f, "roic")


def tornado():
    f = fig(W_HALF, 2.5)
    ax = f.add_subplot(111)
    items = [("WACC +/-0.5 pp", sens["wacc_p50"], sens["wacc_m50"]), ("Margin +/-50 bp", sens["margin_m50"], sens["margin_p50"]),
             ("Terminal g +/-0.5 pp", sens["g_m50"], sens["g_p50"]), (f"Terminal RONIC\n{A['B695'].value*100:.1f}% / {A['B694'].value*100:.1f}%", sens["ronic_min"], sens["ronic_avg"]),
             ("Capex +/-50 bp", sens["capex_p50"], sens["capex_m50"])]
    items.sort(key=lambda t: abs(t[1]) + abs(t[2]))
    for i, (lab, lo, hi) in enumerate(items):
        ax.barh(i, lo, color=RED, height=0.6)
        ax.barh(i, hi, color=BLUE, height=0.6)
        ax.text(lo - 0.4, i, f"{lo:.1f}", ha="right", va="center", fontsize=FS - 0.3)
        ax.text(hi + 0.4, i, f"{hi:+.1f}", ha="left", va="center", fontsize=FS - 0.3)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_yticks(range(len(items)), [t[0] for t in items], fontsize=FS - 0.3)
    ax.set_xlim(-16, 16)
    ax.set_xlabel(f"MXN per share vs target {TP:.2f}")
    save(f, "tornado")


def risk_matrix():
    f = fig(W_HALF, 2.5)
    ax = f.add_subplot(111)
    from matplotlib.colors import LinearSegmentedColormap
    import numpy as np
    cm = LinearSegmentedColormap.from_list("r", ["#E4F1E3", "#FDF1DA", "#F6B3A8", "#EC6A72"])
    g = np.array([[(p * i) for p in range(1, 6)] for i in range(1, 6)], dtype=float)
    ax.imshow(g, cmap=cm, origin="lower", extent=(0.5, 5.5, 0.5, 5.5), aspect="auto", alpha=0.9)
    pts = [("R2", 3, 5, 0.0), ("R1", 3, 4, -0.28), ("R4", 3, 4, 0.28), ("R7", 3, 4, 0.0), ("R3", 2, 4, 0.0), ("R6", 3, 3, -0.28), ("R5", 3, 3, 0.28)]
    for lab, p, i, dx in pts:
        ax.text(p + dx, i + {"R1": 0.2, "R4": 0.2, "R7": -0.2}.get(lab, 0.0), lab, ha="center", va="center", fontsize=FS + 0.5, fontweight="bold", color=NAVY)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Probability (1 low, 5 high)")
    ax.set_ylabel("Impact on value (1 low, 5 high)")
    for s in ax.spines.values():
        s.set_visible(False)
    save(f, "risk_matrix")


if __name__ == "__main__":
    for fn in (usdmxn, wheat_costs, gm_wheat_scenarios, growth_fx, margin_vs_consensus, ev_regimes, acq_lapping, cost_passthrough, na_margin_quarterly, guidance_scorecard, acq_leverage, ebitda_bridge, roic_chart, growth_organic, margins_gross_ebitda, tornado, rev_margin, price_tp, football, bridge_chart, fcff_chart, na_margin, regional_margin, leverage_chart, sens_heat, risk_matrix):
        fn()
    print("target", round(TP, 2), "dcf today", round(dcf_today, 2), "peer range", round(peer_lo, 1), round(peer_hi, 1))
    print({k: round(v, 2) for k, v in sens.items()}, "wheat1y", round(wheat_1y, 2))
    print("TV share 12m", round(num["tv_share_12m"], 3), "leverage", [round(x, 2) for x in lev])
