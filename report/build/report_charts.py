"""Charts for the CFA Research Challenge report on Grupo Bimbo: English, Bimbo palette, sized for the 2.28-inch right column.

Run: python report_charts.py [name ...]   (no names = all). Titles and sources are set in the PDF builder, not in the images.
"""

from __future__ import annotations

import sys

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch, Rectangle

import report_data as D
from report_style import (AMBER, BLUE, BROWN, CHARTS, DPI, GRAY, GRID, INK, LIGHT, NAVY, PALE_BLUE, PINK, RED, REGION,
                          REGION_NAME, SKY, TEAL, W_RC, setup_matplotlib)

plt = setup_matplotlib()
FS = 6.0
MID_BLUE = "#6E8BD0"


def new(h: float, w: float = W_RC):
    fig = plt.figure(figsize=(w, h), layout="constrained")
    fig.get_layout_engine().set(w_pad=3 / 72, h_pad=3 / 72, hspace=0.02, wspace=0.02)
    return fig


def save(fig, name: str):
    CHARTS.mkdir(parents=True, exist_ok=True)
    path = CHARTS / f"{name}.png"
    fig.savefig(path, dpi=DPI)
    plt.close(fig)
    return path


def legend_below(fig, items, ncol=2):
    handles = [Patch(facecolor=c, edgecolor="none") for c, _ in items]
    fig.legend(handles, [l for _, l in items], loc="outside lower center", ncol=ncol, fontsize=FS, handlelength=0.9,
               handleheight=0.9, columnspacing=1.0, handletextpad=0.4, borderaxespad=0.0)


def donut(ax, vals, colors, center=None, width=0.46, min_pct=5.0):
    total = sum(vals)
    wedges, _ = ax.pie(vals, colors=colors, startangle=90, counterclock=False,
                       wedgeprops=dict(width=width, edgecolor="white", linewidth=0.9))
    for w, v in zip(wedges, vals):
        pct = v / total * 100
        if pct >= min_pct:
            a = np.deg2rad((w.theta1 + w.theta2) / 2)
            r = 1 - width / 2
            ax.text(r * np.cos(a), r * np.sin(a), f"{pct:.1f}%", ha="center", va="center", fontsize=FS, color="white",
                    weight="bold")
    if center:
        ax.text(0, 0, center, ha="center", va="center", fontsize=FS + 0.5, weight="bold", color=NAVY, linespacing=1.15)
    ax.set_aspect("equal")


def hgrid(ax):
    ax.yaxis.grid(True, color=GRID, lw=0.4)
    ax.set_axisbelow(True)


def vgrid(ax):
    ax.xaxis.grid(True, color=GRID, lw=0.4)
    ax.set_axisbelow(True)


# =============================================================== business ==============================================
def fig_sales_region():
    fig = new(1.9)
    ax = fig.add_subplot(111)
    donut(ax, [D.SHARE_SALES[k] for k in D.SEG_KEYS], [REGION[k] for k in D.SEG_KEYS], center="MXN 427bn\nFY2025 sales")
    legend_below(fig, [(REGION[k], REGION_NAME[k]) for k in D.SEG_KEYS])
    return save(fig, "fig_sales_region")


def fig_sales_vs_ebitda():
    fig = new(1.75)
    ax = fig.add_subplot(111)
    x, w = np.arange(4), 0.38
    s = [D.SHARE_SALES[k] for k in D.SEG_KEYS]
    e = [D.SHARE_EBITDA[k] for k in D.SEG_KEYS]
    b1 = ax.bar(x - w / 2, s, w, color=BLUE, label="Net sales")
    b2 = ax.bar(x + w / 2, e, w, color=RED, label="Adj. EBITDA")
    for bars in (b1, b2):
        for r in bars:
            ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 1.0, f"{r.get_height():.1f}", ha="center",
                    va="bottom", fontsize=FS)
    ax.set_xticks(x, ["North\nAmerica", "Mexico", "Europe,\nAsia, Africa", "Latin\nAmerica"])
    ax.set_ylim(0, 68)
    ax.set_ylabel("% of group total")
    ax.legend(loc="upper right", ncol=1)
    hgrid(ax)
    return save(fig, "fig_sales_vs_ebitda")


def fig_ownership():
    fig = new(2.05)
    ax = fig.add_subplot(111)
    vals = [v for _, v in D.OWNERS] + [round(100 - D.CONTROL_PCT, 2)]
    cols = [BLUE, "#2F5BC4", SKY, TEAL, AMBER, PINK, LIGHT]
    donut(ax, vals, cols, center=f"{D.CONTROL_PCT:.1f}%\nsix holders", min_pct=10.0)
    legend_below(fig, list(zip(cols, [f"{n} {v:.1f}%" for n, v in D.OWNERS] + ["Other holders 28.0%"])), ncol=2)
    return save(fig, "fig_ownership")


# =============================================================== industry ==============================================
def fig_market_growth():
    fig = new(1.7)
    ax = fig.add_subplot(111)
    x, w = np.arange(len(D.MARKET)), 0.38
    h1 = [np.nan if a is None else a for _, a, _ in D.MARKET]
    h2 = [b for _, _, b in D.MARKET]
    b1 = ax.bar(x - w / 2, h1, w, color=LIGHT, label="2019-24")
    b2 = ax.bar(x + w / 2, h2, w, color=BLUE, label="2024-29E")
    for bars in (b1, b2):
        for r in bars:
            if not np.isnan(r.get_height()):
                ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 0.12, f"{r.get_height():.1f}", ha="center",
                        va="bottom", fontsize=FS)
    ax.text(x[3] - w / 2, 0.15, "n/a", ha="center", va="bottom", fontsize=FS, color=GRAY)
    ax.set_xticks(x, ["Global", "North\nAmerica", "Latin\nAmerica", "Mexico"])
    ax.set_ylim(0, 7.0)
    ax.set_ylabel("Value CAGR, %")
    ax.legend(loc="upper left", ncol=2)
    hgrid(ax)
    return save(fig, "fig_market_growth")


def fig_market_type():
    fig = new(1.9)
    ax = fig.add_subplot(111)
    art, pl = D.MARKET_TYPE["Artisanal"], D.MARKET_TYPE["Private label"]
    vals = [round(100 - art - pl, 1), art, pl]
    cols = [BLUE, AMBER, RED]
    donut(ax, vals, cols, center="US$639bn\nglobal 2024")
    legend_below(fig, list(zip(cols, ["Branded and other", "Artisanal", "Private label"])), ncol=3)
    return save(fig, "fig_market_type")


def fig_peers():
    short = {"Flowers Foods, Inc.": "Flowers", "Gruma, S.A.B. de C.V.": "Gruma", "Yamazaki Baking Co., Ltd.": "Yamazaki*",
             "ARYZTA AG": "Aryzta*", "The J. M. Smucker Company": "Smucker", "The Campbell's Company": "Campbell's",
             "Mondelez International, Inc.": "Mondelez", "Arca Continental, S.A.B. de C.V.": "Arca Continental*",
             "PepsiCo, Inc.": "PepsiCo", "Grupo Bimbo, S.A.B. de C.V. (subject)": "Grupo Bimbo"}
    rows = sorted(((short[p["name"]], p["ev_ebitda_ltm"], p["group"], p["in_median"]) for p in D.PEERS["peers"]),
                  key=lambda r: r[1])
    cols = []
    for _, _, g, m in rows:
        cols.append(RED if m == "subject" else (BLUE if (g == "Core" and m == "yes") else (MID_BLUE if m == "yes" else PALE_BLUE)))
    fig = new(2.25)
    ax = fig.add_subplot(111)
    y = np.arange(len(rows))
    ax.barh(y, [r[1] for r in rows], color=cols, height=0.62)
    for yi, r in zip(y, rows):
        ax.text(r[1] + 0.2, yi, f"{r[1]:.1f}x", va="center", fontsize=FS, zorder=5,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9))
    ax.set_yticks(y, [r[0] for r in rows])
    core, allm = D.PEERS["medians"]["core_median"]["ev_ebitda_ltm"], D.PEERS["medians"]["all_median"]["ev_ebitda_ltm"]
    for v, lab in ((core, f"core median {core:.2f}x"), (allm, f"all-peer median {allm:.2f}x")):
        ax.axvline(v, color=GRAY, lw=0.7, ls="--")
    ax.text(core - 0.15, -1.15, f"core {core:.2f}x", ha="right", va="center", fontsize=FS, color=GRAY)
    ax.text(allm + 0.15, -1.15, f"all peers {allm:.2f}x", ha="left", va="center", fontsize=FS, color=GRAY)
    ax.set_ylim(-1.7, len(rows) - 0.4)
    ax.set_xlim(0, 18.5)
    ax.set_xlabel("EV / EBITDA, last twelve months")
    vgrid(ax)
    legend_below(fig, [(BLUE, "Core bakers"), (MID_BLUE, "Other peers"), (PALE_BLUE, "*Excluded from medians"),
                       (RED, "Grupo Bimbo")], ncol=2)
    return save(fig, "fig_peers")


def fig_five_forces():
    fig = new(2.2)
    ax = fig.add_subplot(111, projection="polar")
    labels = ["Rivalry", "New\nentrants", "Supplier\npower", "Buyer\npower", "Substitutes"]
    dev = [4.5, 3.0, 3.0, 4.5, 4.0]
    em = [3.0, 2.0, 3.0, 2.0, 3.0]
    ang = np.linspace(0, 2 * np.pi, 5, endpoint=False)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    for vals, col in ((dev, RED), (em, BLUE)):
        ax.plot(list(ang) + [ang[0]], vals + vals[:1], color=col, lw=1.3)
        ax.fill(list(ang) + [ang[0]], vals + vals[:1], color=col, alpha=0.16)
    ax.set_xticks(ang, labels, fontsize=FS)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], fontsize=FS - 0.2, color=GRAY)
    ax.set_rlabel_position(22)
    ax.grid(color=GRID, lw=0.5)
    ax.spines["polar"].set_color(LIGHT)
    legend_below(fig, [(RED, "US, Canada, Europe"), (BLUE, "Mexico, Latin America")], ncol=1)
    return save(fig, "fig_five_forces")


# =============================================================== investment summary =====================================
def fig_thesis_map():
    L = D.LEV
    items = [("Thesis 1: North America margin\ncloses the gap to Flowers (+150 bp)", L["levers"]["na_margin_gap_flowers_p150"]["exit"]),
             ("Thesis 2: wheat takes 50 bp off\nmargin from 2027, for good", L["levers"]["margin_m50_from27"]["exit"]),
             ("Thesis 3: North America -1 pp,\nMexico -2 pp growth", L["levers"]["growth_both"]["exit"]),
             ("All three together", L["scenario_all_three"]["exit"])]
    fig = new(2.0)
    ax = fig.add_subplot(111)
    y = np.arange(len(items))[::-1]
    cols = [BLUE if v > 0 else RED for _, v in items]
    cols[-1] = NAVY
    ax.barh(y, [v for _, v in items], color=cols, height=0.55)
    for yi, (_, v) in zip(y, items):
        ax.text(v + (0.25 if v > 0 else -0.25), yi, f"{v:+.2f}", va="center", ha="left" if v > 0 else "right", fontsize=FS,
                weight="bold")
    ax.axvline(0, color=INK, lw=0.6)
    ax.set_yticks(y, [n for n, _ in items], fontsize=FS - 0.3)
    ax.set_xlim(-9.0, 7.6)
    ax.set_xlabel(f"MXN per share vs base {D.RUN['ps_exit']:.2f}", loc="right")
    vgrid(ax)
    return save(fig, "fig_thesis_map")


def fig_na_margin():
    fig = new(1.95)
    ax = fig.add_subplot(111)
    x = np.arange(len(D.QUARTERS))
    cols = [RED if q == "4Q24" else BLUE for q in D.QUARTERS]
    ax.bar(x, D.NA_MARGIN_Q, color=cols, width=0.66)
    for xi, v in zip(x, D.NA_MARGIN_Q):
        ax.text(xi, v + 0.25, f"{v:.1f}", ha="center", va="bottom", fontsize=FS - 0.2)
    ax.set_ylim(0, 19)
    ax.set_yticks([0, 5, 10])
    ax.set_ylabel("Adj. EBITDA margin, %", loc="bottom")
    ax.set_xticks(x, D.QUARTERS, rotation=90)
    ax2 = ax.twinx()
    ax2.plot(x, D.NA_EXFX_Q, color=AMBER, marker="o", ms=2.6, lw=1.3)
    ax2.axhline(0, color=GRAY, lw=0.5, ls=":")
    ax2.set_ylim(-22, 3.5)
    ax2.set_yticks([-6, -3, 0, 3])
    ax2.set_ylabel("Net sales ex-FX, % y/y", loc="top")
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(LIGHT)
    ax2.tick_params(axis="y", colors=GRAY)
    for xi, v in ((3, D.NA_EXFX_Q[3]), (9, D.NA_EXFX_Q[9])):
        ax2.text(xi, v + (-1.9 if xi == 3 else 0.9), f"{v:+.1f}", ha="center", fontsize=FS - 0.2, color=BROWN)
    fig.legend([Patch(facecolor=BLUE), plt.Line2D([], [], color=AMBER, marker="o", ms=2.6, lw=1.3)],
               ["Margin (bars)", "Sales growth ex-FX (line)"], loc="outside lower center", ncol=2, fontsize=FS,
               handlelength=1.2, columnspacing=1.0)
    return save(fig, "fig_na_margin")


def fig_capex_cfo():
    fig = new(1.75)
    ax = fig.add_subplot(111)
    x, w = np.arange(5), 0.38
    cf = [v / 1000 for v in D.CFO_H]
    cx = [v / 1000 for v in D.CAPEX_PPE_H]
    ax.bar(x - w / 2, cf, w, color=BLUE, label="Cash flow from operations")
    ax.bar(x + w / 2, cx, w, color=RED, label="Capex (PP&E acquired)")
    for xi, v in zip(x, cf):
        ax.text(xi - w / 2, v - 1.0, f"{v:.1f}", ha="center", va="top", rotation=90, fontsize=FS, color="white", weight="bold")
    for xi, v in zip(x, cx):
        ax.text(xi + w / 2, v - 1.0, f"{v:.1f}", ha="center", va="top", rotation=90, fontsize=FS, color="white", weight="bold")
    ax.set_xticks(x, [f"FY{y}" for y in D.YEARS_H], fontsize=FS - 0.3)
    ax.set_ylim(0, 66)
    ax.set_ylabel("MXN bn")
    ax.legend(loc="upper left", ncol=1)
    hgrid(ax)
    return save(fig, "fig_capex_cfo")


def fig_cost_lines():
    rows = sorted(D.COST_LINES, key=lambda r: r[1])
    fig = new(1.6)
    ax = fig.add_subplot(111)
    y = np.arange(len(rows))
    ax.barh(y, [r[1] for r in rows], color=[RED if r[1] > D.SALES_GROWTH_FY25 else BLUE for r in rows], height=0.6)
    for yi, r in zip(y, rows):
        ax.text(r[1] + 0.25, yi, f"+{r[1]:.1f}%", va="center", fontsize=FS, zorder=5,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9))
    ax.axvline(D.SALES_GROWTH_FY25, color=GRAY, lw=0.8, ls="--")
    ax.text(D.SALES_GROWTH_FY25 + 0.15, -0.95, f"net sales +{D.SALES_GROWTH_FY25:.1f}%", fontsize=FS, color=GRAY, va="center")
    ax.set_yticks(y, [r[0] for r in rows])
    ax.set_xlim(0, 17)
    ax.set_ylim(-1.4, len(rows) - 0.4)
    ax.set_xlabel("FY2025 growth, % y/y")
    vgrid(ax)
    return save(fig, "fig_cost_lines")


def fig_growth_gap():
    fig = new(1.85)
    ax = fig.add_subplot(111)
    na = [D.NA_EXFX_FY["FY24"], D.NA_EXFX_FY["FY25"], (0.7 + 1.3) / 2, 1.5]
    mx = [D.MX_GROWTH["FY24"], D.MX_GROWTH["FY25"], (4.5 + 4.7) / 2, 5.25]
    labs = ["FY24", "FY25", "1H26*", "Model\nFY27-30E"]
    x, w = np.arange(4), 0.38
    cols_na = [BLUE, BLUE, BLUE, PALE_BLUE]
    cols_mx = [RED, RED, RED, "#F6B8BD"]
    ax.bar(x - w / 2, na, w, color=cols_na, edgecolor=[BLUE] * 4, lw=0.5)
    ax.bar(x + w / 2, mx, w, color=cols_mx, edgecolor=[RED] * 4, lw=0.5)
    for xi, v in zip(x, na):
        ax.text(xi - w / 2, v + (0.2 if v >= 0 else -0.2), f"{v:+.1f}", ha="center", va="bottom" if v >= 0 else "top", fontsize=FS - 0.2)
    for xi, v in zip(x, mx):
        ax.text(xi + w / 2, v + 0.2, f"{v:.1f}" if xi < 3 else "5.0-5.5", ha="center", va="bottom", fontsize=FS - 0.2)
    ax.axhline(0, color=INK, lw=0.6)
    ax.set_xticks(x, labs)
    ax.set_ylim(-6.5, 7.6)
    ax.set_ylabel("Net sales growth ex-FX, %")
    hgrid(ax)
    fig.legend([Patch(facecolor=BLUE), Patch(facecolor=RED)], ["North America (USD)", "Mexico"], loc="outside lower center",
               ncol=2, fontsize=FS, handlelength=0.9, columnspacing=1.0)
    return save(fig, "fig_growth_gap")


# =============================================================== valuation ============================================
def fig_football():
    F = D.LEV["football"]
    comps = D.CONS["results"]["v3"]
    rows = [("DCF, exit multiple 5.0x to 7.0x", F["dcf_exit_multiple"]["low"], F["dcf_exit_multiple"]["high"], F["dcf_exit_multiple"]["mid"], BLUE),
            ("DCF, exit multiple, WACC 9.4% to 11.4%", F["dcf_exit_wacc"]["low"], F["dcf_exit_wacc"]["high"], F["dcf_exit_wacc"]["mid"], BLUE),
            ("DCF, Gordon growth, g 3.1% to 5.1%", F["dcf_gordon_ronic"]["low"], F["dcf_gordon_ronic"]["high"], F["dcf_gordon_ronic"]["mid"], BLUE),
            ("Comps, core 5.5x to all peers 8.3x", comps["comps_core"], comps["comps_all"], 42.68, SKY),
            ("52-week trading range", D.RANGE_52W[0], D.RANGE_52W[1], None, GRAY),
            (f"Analyst targets ({D.TARGETS['n']}), median {D.TARGETS['median']:.1f}", D.TARGETS["low"], D.TARGETS["high"], D.TARGETS["median"], GRAY)]
    B = D.LEV["bands"]
    fig = new(2.5)
    ax = fig.add_subplot(111)
    xmin, xmax = 20, 92
    ax.axvspan(xmin, B["sell_edge"]["value"], color=PINK, alpha=0.10, lw=0)
    ax.axvspan(B["sell_edge"]["value"], B["buy_edge"]["value"], color=AMBER, alpha=0.14, lw=0)
    ax.axvspan(B["buy_edge"]["value"], xmax, color=TEAL, alpha=0.18, lw=0)
    n = len(rows)
    for i, (lab, lo, hi, mid, col) in enumerate(rows):
        y = n - 1 - i
        ax.barh(y, hi - lo, left=lo, height=0.34, color=col, zorder=3)
        ax.text(xmin + 0.8, y + 0.30, lab, fontsize=FS, va="bottom", ha="left", zorder=7,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.75))
        ax.text(lo - 0.8, y, f"{lo:.1f}", ha="right", va="center", fontsize=FS - 0.2, zorder=4)
        ax.text(hi + 0.8, y, f"{hi:.1f}", ha="left", va="center", fontsize=FS - 0.2, zorder=4)
        if mid is not None:
            ax.plot([mid, mid], [y - 0.17, y + 0.17], color="white", lw=1.6, zorder=5)
    ax.axvline(D.PRICE, color=RED, lw=1.1, ls="--", zorder=6)
    ax.text(D.PRICE + 0.8, -0.78, f"price {D.PRICE:.2f}", color=RED, fontsize=FS, va="center", weight="bold")
    top = n - 0.2
    ax.text((xmin + B["sell_edge"]["value"]) / 2, top + 0.05, "SELL", ha="center", fontsize=FS, color=PINK, weight="bold", va="bottom")
    ax.text((B["sell_edge"]["value"] + B["buy_edge"]["value"]) / 2, top + 0.05, "HOLD", ha="center", fontsize=FS, color="#B97B0A", weight="bold", va="bottom")
    ax.text((B["buy_edge"]["value"] + xmax) / 2, top + 0.05, "BUY", ha="center", fontsize=FS, color="#2E7F76", weight="bold", va="bottom")
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-1.15, n + 0.35)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("MXN per share (white tick = base case)")
    return save(fig, "fig_football")


def fig_multiple_curve():
    L = D.LEV
    c = L["curve"]
    xs = [r["multiple"] for r in c]
    ys = [r["exp_return"] * 100 for r in c]
    fig = new(2.15)
    ax = fig.add_subplot(111)
    ax.axhspan(-40, -10, color=PINK, alpha=0.10, lw=0)
    ax.axhspan(-10, 15, color=AMBER, alpha=0.13, lw=0)
    ax.axhspan(-5, 10, color=AMBER, alpha=0.22, lw=0)
    ax.axhspan(15, 30, color=TEAL, alpha=0.18, lw=0)
    ax.plot(xs, ys, color=BLUE, lw=1.5, zorder=3)
    pts = [(D.STATE["exit_mult"], L["base_exp_return"] * 100, "Base 5.92x\n-10.5%", "right", (-0.12, 6.5)),
           (6.2, next(r for r in L["multiple_table"] if abs(r["multiple"] - 6.2) < 1e-9)["exp_return"] * 100, "6.2x\n-4.0%", "left", (0.12, -7.0)),
           (6.8, next(r for r in L["multiple_table"] if abs(r["multiple"] - 6.8) < 1e-9)["exp_return"] * 100, "6.8x\n+9.6%", "right", (-0.12, 5.5)),
           (L["reverse_multiple"], D.CONS["consolidated"]["run"]["ke"] * 100, f"Price-implied\n{L['reverse_multiple']:.2f}x", "left", (0.10, -7.5))]
    for mx, er, txt, ha, (dx, dy) in pts:
        ax.plot(mx, er, "o", color=RED, ms=3.2, zorder=4)
        ax.text(mx + dx, er + dy, txt, fontsize=FS - 0.2, ha=ha, va="center", color=NAVY, linespacing=1.1)
    ax.text(5.03, -36, "SELL  (≤ -10%)", fontsize=FS, color=PINK, weight="bold", va="center")
    ax.text(5.03, 17.5, "BUY  (≥ +15%)", fontsize=FS, color="#2E7F76", weight="bold", va="center")
    ax.text(5.03, 2.5, "HOLD", fontsize=FS, color="#B97B0A", weight="bold", va="center")
    ax.set_xlim(5.0, 7.5)
    ax.set_ylim(-40, 27)
    ax.set_xlabel("Exit EV/EBITDA multiple on FY2030E")
    ax.set_ylabel("12-month expected return, %")
    ax.grid(True, color=GRID, lw=0.4)
    ax.set_axisbelow(True)
    return save(fig, "fig_multiple_curve")


def fig_tornado():
    rows = sorted(D.LEV["tornado"], key=lambda r: abs(r["down"]) + abs(r["up"]))
    fig = new(1.7)
    ax = fig.add_subplot(111)
    y = np.arange(len(rows))
    ax.barh(y, [r["down"] for r in rows], color=RED, height=0.58)
    ax.barh(y, [r["up"] for r in rows], color=BLUE, height=0.58)
    for yi, r in zip(y, rows):
        ax.text(r["down"] - 0.15, yi, f"{r['down']:.1f}", ha="right", va="center", fontsize=FS - 0.2)
        ax.text(r["up"] + 0.15, yi, f"+{r['up']:.1f}", ha="left", va="center", fontsize=FS - 0.2)
    ax.axvline(0, color=INK, lw=0.6)
    ax.set_yticks(y, [r["label"] for r in rows])
    ax.set_xlim(-8.2, 8.2)
    ax.set_xlabel(f"MXN per share vs base {D.RUN['ps_exit']:.2f}")
    vgrid(ax)
    return save(fig, "fig_tornado")


# =============================================================== financial analysis ===================================
def fig_rev_margin():
    yrs = D.YEARS_H + D.YEARS_F
    rev = [v / 1000 for v in D.REV_H] + [v / 1000 for v in D.REV_F]
    mg = [v * 100 for v in D.ADJ_MARGIN_H] + [v * 100 for v in D.MARGIN_F]
    fig = new(1.95)
    ax = fig.add_subplot(111)
    x = np.arange(len(yrs))
    ax.bar(x, rev, color=[BLUE] * 5 + [PALE_BLUE] * 5, width=0.66, edgecolor=[BLUE] * 10, lw=0.4)
    ax.set_ylim(0, 800)
    ax.set_yticks([0, 200, 400])
    ax.set_ylabel("Net sales, MXN bn", loc="bottom")
    ax.set_xticks(x, [f"{y}{'A' if y <= 2025 else 'E'}" for y in yrs], rotation=90)
    ax2 = ax.twinx()
    ax2.plot(x, mg, color=RED, marker="o", ms=2.4, lw=1.3)
    ax2.set_ylim(8, 16.5)
    ax2.set_yticks([13, 14, 15, 16])
    ax2.set_ylabel("Adj. EBITDA margin, %", loc="top")
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(LIGHT)
    ax2.tick_params(axis="y", colors=GRAY)
    for xi in (0, 4, 5, 9):
        ax2.text(xi, mg[xi] + 0.45, f"{mg[xi]:.1f}", ha="center", fontsize=FS - 0.2, color=RED)
    fig.legend([Patch(facecolor=BLUE), Patch(facecolor=PALE_BLUE, edgecolor=BLUE, lw=0.4), plt.Line2D([], [], color=RED, marker="o", ms=2.4, lw=1.3)],
               ["Actual", "Forecast", "Margin"], loc="outside lower center", ncol=3, fontsize=FS, handlelength=1.0, columnspacing=1.0)
    return save(fig, "fig_rev_margin")


def fig_leverage():
    yrs = list(range(2021, 2026))
    nd = [D.stmt("BS", "Net debt", y) / e for y, e in zip(yrs, D.ADJ_EBITDA_H)]
    ltm = D.PEERS["peers"][-1]["nd_ebitda"]
    fig = new(1.65)
    ax = fig.add_subplot(111)
    x = np.arange(6)
    ax.plot(x[:5], nd, color=BLUE, marker="o", ms=2.8, lw=1.5)
    ax.plot([4, 5], [nd[-1], ltm], color=BLUE, marker="o", ms=2.8, lw=1.5, ls=":")
    ax.plot(5, 2.5, marker="D", ms=3.4, color="white", markeredgecolor=RED, markeredgewidth=1.0, ls="none")
    ax.axhline(2.98, color=RED, lw=0.8, ls="--")
    ax.text(0.0, 3.03, "peer median 2.98x", ha="left", va="bottom", fontsize=FS - 0.2, color=RED)
    for xi, v, dy in ((0, nd[0], 0.14), (1, nd[1], -0.34), (2, nd[2], 0.14), (3, nd[3], 0.14), (4, nd[4], -0.34), (5, ltm, 0.14)):
        ax.text(xi, v + dy, f"{v:.2f}x", ha="center", fontsize=FS - 0.2, color=NAVY, zorder=5,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9))
    ax.text(5, 2.5 - 0.36, "2.5x\ncompany\nbasis", ha="center", va="top", fontsize=FS - 0.4, color=RED, linespacing=1.05)
    ax.set_xticks(x, [f"{str(y)[2:]}A" for y in yrs] + ["LTM\nJun-26"])
    ax.set_xlim(-0.4, 5.5)
    ax.set_ylim(1.2, 3.75)
    ax.set_ylabel("Net debt / EBITDA incl. leases")
    ax.grid(True, axis="y", color=GRID, lw=0.4)
    ax.set_axisbelow(True)
    return save(fig, "fig_leverage")


# =============================================================== risks ================================================
def fig_risk_matrix():
    fig = new(2.35)
    ax = fig.add_subplot(111)
    cmap = LinearSegmentedColormap.from_list("risk", ["#DDF0ED", "#FBE6BC", "#F6B3A5", "#EC6A70"])
    for p in range(1, 6):
        for i in range(1, 6):
            ax.add_patch(Rectangle((p - 0.5, i - 0.5), 1, 1, facecolor=cmap((p * i) / 25), edgecolor="white", lw=1.2))
    cells = {}
    for code, _, p, i in D.RISKS:
        cells.setdefault((p, i), []).append(code)
    for (p, i), codes in cells.items():
        lines = [" ".join(codes[k:k + 2]) for k in range(0, len(codes), 2)]
        ax.text(p, i, "\n".join(lines), ha="center", va="center", fontsize=FS, weight="bold", color=NAVY, linespacing=1.15)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Probability (1 low, 5 high)")
    ax.set_ylabel("Impact on value (1 low, 5 high)")
    ax.set_aspect("equal")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    return save(fig, "fig_risk_matrix")


# =============================================================== ESG ==================================================
def fig_esg_sp():
    fig = new(1.85)
    ax = fig.add_subplot(111)
    ax.plot(D.SP_YEARS, D.SP_TOTAL, color=BLUE, lw=1.8, label="Total")
    ax.plot(D.SP_YEARS, D.SP_E, color=TEAL, lw=1.0, label="Environmental")
    ax.plot(D.SP_YEARS, D.SP_S, color=AMBER, lw=1.0, label="Social")
    ax.plot(D.SP_YEARS, D.SP_G, color=RED, lw=1.0, label="Governance & economic")
    for yr, v, dy in ((2018, 39, -5), (2024, 61, 4), (2026, 59, -6)):
        ax.text(yr, v + dy, f"{v}", ha="center", fontsize=FS - 0.2, color=BLUE, weight="bold")
    ax.set_xticks([2013, 2016, 2019, 2022, 2025], ["2013", "2016", "2019", "2022", "2025"])
    ax.set_ylim(20, 80)
    ax.set_ylabel("S&P Global ESG score (0-100)")
    ax.grid(True, axis="y", color=GRID, lw=0.4)
    ax.set_axisbelow(True)
    fig.legend(loc="outside lower center", ncol=2, fontsize=FS, handlelength=1.2, columnspacing=1.0,
               handles=ax.get_lines())
    return save(fig, "fig_esg_sp")


def fig_esg_lseg():
    rows = sorted(D.LSEG_PEERS, key=lambda r: r[1])
    fig = new(2.15)
    ax = fig.add_subplot(111)
    y = np.arange(len(rows))
    cols = [RED if n == "Grupo Bimbo" else (AMBER if n in ("Flowers Foods", "Gruma") else BLUE) for n, _ in rows]
    ax.barh(y, [v for _, v in rows], color=cols, height=0.62)
    for yi, (_, v) in zip(y, rows):
        ax.text(v + 1, yi, f"{v:.1f}", va="center", fontsize=FS - 0.2)
    ax.set_yticks(y, [n for n, _ in rows])
    ax.set_xlim(0, 108)
    ax.set_xlabel("LSEG ESG score, FY2024 (0-100)")
    vgrid(ax)
    return save(fig, "fig_esg_lseg")


def fig_emissions():
    fig = new(2.25)
    gs = fig.add_gridspec(2, 1, hspace=0.12)
    for k, (series, target, title) in enumerate(((D.SCOPE1_KT, 0.50, "Scope 1, kt CO2e"), (D.SCOPE3_KT, 0.72, "Scope 3, kt CO2e"))):
        ax = fig.add_subplot(gs[k])
        labs = [a.replace(" (restated)", "\nrestated").replace(" prelim.", "\nprelim.") for a, _ in series] + ["2030\ntarget"]
        vals = [b for _, b in series]
        tgt = vals[0] * target
        x = np.arange(len(labs))
        ax.bar(x[:-1], vals, color=[PALE_BLUE] + [BLUE] * 3 + [RED], width=0.62)
        ax.bar(x[-1], tgt, color="white", edgecolor=TEAL, hatch="////", lw=0.8, width=0.62)
        for xi, v in zip(x, vals + [tgt]):
            ax.text(xi, v + max(vals) * 0.03, f"{v:,.0f}", ha="center", fontsize=FS - 0.3)
        ax.set_ylim(0, max(vals) * 1.28)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_title(title, fontsize=FS, loc="left", color=GRAY, pad=1.5)
        ax.set_xticks(x, labs if k == 1 else [""] * len(labs), fontsize=FS - 0.4)
    return save(fig, "fig_emissions")


def fig_governance():
    rows = D.GOV_BLOCKS
    fig = new(1.7)
    ax = fig.add_subplot(111)
    y = np.arange(len(rows))[::-1]
    pct = [a / b * 100 for _, a, b in rows]
    ax.barh(y, [100] * len(rows), color=GRID, height=0.62)
    ax.barh(y, pct, color=[RED if p < 30 else (AMBER if p < 60 else BLUE) for p in pct], height=0.62)
    for yi, (_, a, b), p in zip(y, rows, pct):
        ax.text(min(p, 100) + 2, yi, f"{a}/{b}", va="center", fontsize=FS)
    ax.set_yticks(y, [n for n, _, _ in rows])
    ax.set_xlim(0, 118)
    ax.set_xticks([0, 50, 100])
    ax.set_xlabel("Score, % of maximum")
    return save(fig, "fig_governance")


def fig_ev_bridge():
    r, s = D.RUN, D.STATE
    pv_f, pv_tv, ev = r["pv_explicit"] / 1000, r["pv_tv_exit"] / 1000, r["ev_exit"] / 1000
    net = (-s["debt"] + s["cash"] - r["nci"] + s["assoc_net"]) / 1000
    eq = r["equity_exit_anchor"] / 1000
    fig = new(1.95)
    ax = fig.add_subplot(111)
    labs = ["PV of\nFCFF", "PV of\nterminal", "Enterprise\nvalue", "Net\nclaims", "Equity\nvalue"]
    ax.bar(0, pv_f, color=BLUE, width=0.62)
    ax.bar(1, pv_tv, bottom=pv_f, color=MID_BLUE, width=0.62)
    ax.bar(2, ev, color=NAVY, width=0.62)
    ax.bar(3, -net, bottom=ev + net, color=RED, width=0.62)
    ax.bar(4, eq, color=BLUE, width=0.62)
    tops = [pv_f, pv_f + pv_tv, ev, ev, eq]
    vals = [f"{pv_f:.1f}", f"{pv_tv:.1f}", f"{ev:.1f}", f"{net:.1f}".replace("-", "−"), f"{eq:.1f}"]
    for x, t, v in zip(range(5), tops, vals):
        ax.text(x, t + 9, v, ha="center", va="bottom", fontsize=FS, weight="bold")
    ax.text(1, pv_f + pv_tv / 2, f"{r['tv_share_exit'] * 100:.0f}%\nof EV", ha="center", va="center", fontsize=FS, color="white", weight="bold", linespacing=1.2)
    ax.set_xticks(range(5), labs)
    ax.set_ylim(0, 450)
    ax.set_ylabel("MXN bn")
    hgrid(ax)
    return save(fig, "fig_ev_bridge")


def fig_roic_wacc():
    yrs = list(range(2023, 2026))
    key = [k for k in D.ST["sheets"]["Ratios"] if k.startswith("ROIC")][0]
    roic = [D.stmt("Ratios", key, y) * 100 for y in yrs]
    roe = [D.stmt("Ratios", "Return on average equity", y) * 100 for y in yrs]
    fig = new(1.7)
    ax = fig.add_subplot(111)
    x, w = np.arange(len(yrs)), 0.36
    ax.bar(x - w / 2, roic, w, color=BLUE, label="ROIC")
    ax.bar(x + w / 2, roe, w, color=TEAL, label="ROE")
    for xi, v in zip(x, roic):
        ax.text(xi - w / 2, v + 0.25, f"{v:.1f}", ha="center", fontsize=FS - 0.2, color=BLUE, weight="bold")
    for xi, v in zip(x, roe):
        ax.text(xi + w / 2, v + 0.25, f"{v:.1f}", ha="center", fontsize=FS - 0.2, color="#2E7F76", weight="bold")
    ax.axhline(D.RUN["wacc"] * 100, color=RED, lw=0.9, ls="--")
    ax.axhline(14.6, color=AMBER, lw=0.9, ls=":")
    ax.text(2.45, D.RUN["wacc"] * 100 + 0.2, f"WACC {D.RUN['wacc'] * 100:.1f}%", fontsize=FS - 0.2, color=RED, va="bottom", ha="right")
    ax.text(2.45, 14.8, "Return on new capital in DCF 14.6%", fontsize=FS - 0.2, color="#B97B0A", va="bottom", ha="right")
    ax.set_xticks(x, [f"FY{y}" for y in yrs])
    ax.set_xlim(-0.55, 2.5)
    ax.set_ylim(0, 17.5)
    ax.set_ylabel("%")
    ax.legend(loc="upper left", ncol=2, fontsize=FS - 0.2)
    ax.grid(True, axis="y", color=GRID, lw=0.4)
    ax.set_axisbelow(True)
    return save(fig, "fig_roic_wacc")


ALL = [fig_sales_region, fig_sales_vs_ebitda, fig_ownership, fig_market_growth, fig_market_type, fig_peers, fig_five_forces,
       fig_thesis_map, fig_na_margin, fig_capex_cfo, fig_cost_lines, fig_growth_gap, fig_football, fig_multiple_curve,
       fig_tornado, fig_rev_margin, fig_leverage, fig_risk_matrix, fig_esg_sp, fig_esg_lseg, fig_emissions, fig_governance,
       fig_ev_bridge, fig_roic_wacc]


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for f in ALL:
        if not want or f.__name__ in want:
            print("built", f().name)
