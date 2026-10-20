"""Donut chart of Grupo Bimbo FY2025 net sales by region (ES and EN versions).

Data [sourced]: Grupo Bimbo, Informe Anual Integrado 2025, estados financieros,
note 26 (segment information), p.85: "Ventas netas consolidadas" by region, i.e.
sales to third parties after removing inter-segment sales. They add up to the
consolidated net sales of MXN 426,952 million.

Usage: python revenue_mix_chart.py <out_es.png> <out_en.png>
"""
import math
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

TOTAL = 426_952
INTERSEGMENT = 16_402
# (key, MXN m) in categorical slot order: colour follows the region in every chart.
REGIONS = [("na", 188_852), ("mx", 140_360), ("eaa", 54_125), ("latam", 43_615)]
assert sum(v for _, v in REGIONS) == TOTAL, "regions must add to consolidated net sales"

# Validated categorical slots 1-4 (dataviz reference palette, light mode).
COLORS = {"na": "#2a78d6", "mx": "#eb6834", "eaa": "#1baf7a", "latam": "#eda100"}
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
LEADER = "#c3c2b7"

TEXT = {
    "es": {
        "names": {"na": "Norteamérica", "mx": "México", "eaa": "Europa, Asia y África", "latam": "Latinoamérica"},
        "sub": {"na": "EE.UU. y Canadá", "mx": "", "eaa": "", "latam": "sin México"},
        "title": "Grupo Bimbo: ventas netas por región, 2025",
        "subtitle": "Participación de cada región en las ventas consolidadas",
        "center_unit": "millones de pesos",
        "center_label": "ventas netas 2025",
        "amount": "MXN {v} mm",
        "note": (
            "Ventas a terceros de cada región, después de eliminar las ventas entre segmentos (MXN {e} millones).\n"
            "La nota de segmentos solo divide las ventas por región.\n"
            "Fuente: Grupo Bimbo, Informe Anual Integrado 2025, estados financieros, nota 26, p. 85."
        ),
    },
    "en": {
        "names": {"na": "North America", "mx": "Mexico", "eaa": "Europe, Asia & Africa", "latam": "Latin America"},
        "sub": {"na": "US and Canada", "mx": "", "eaa": "", "latam": "excl. Mexico"},
        "title": "Grupo Bimbo: net sales by region, FY2025",
        "subtitle": "Share of consolidated net sales",
        "center_unit": "MXN million",
        "center_label": "net sales FY2025",
        "amount": "MXN {v}m",
        "note": (
            "Third-party sales by region, after removing inter-segment sales (MXN {e} million).\n"
            "The segment note splits sales by region only.\n"
            "Source: Grupo Bimbo, 2025 Integrated Annual Report, financial statements, note 26, p.85."
        ),
    },
}


def _font() -> None:
    installed = {f.name for f in font_manager.fontManager.ttflist}
    plt.rcParams["font.family"] = [f for f in ("Segoe UI", "Arial") if f in installed] or ["DejaVu Sans"]


def build(lang: str, path: str) -> None:
    t = TEXT[lang]
    values = [v for _, v in REGIONS]
    keys = [k for k, _ in REGIONS]
    shares = [v / TOTAL * 100 for v in values]
    assert abs(sum(round(s, 1) for s in shares) - 100.0) < 0.05, "rounded shares must add to 100.0"

    dpi = 200
    fig = plt.figure(figsize=(8, 5.6), dpi=dpi, facecolor=SURFACE)
    ax = fig.add_axes([0.16, 0.2, 0.68, 0.64])
    ax.set_facecolor(SURFACE)
    gap_pt = 4 * 72 / dpi  # 4 px at 200 dpi = a 2 px surface gap at the usual 2x downscale
    wedges, _ = ax.pie(
        values,
        colors=[COLORS[k] for k in keys],
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.34, "edgecolor": SURFACE, "linewidth": gap_pt},
    )
    ax.set_aspect("equal")

    # Centre: the whole the slices are parts of.
    ax.text(0, 0.07, f"{TOTAL:,}", ha="center", va="center", fontsize=17, fontweight="bold", color=INK)
    ax.text(0, -0.13, t["center_unit"], ha="center", va="center", fontsize=8, color=INK_2)
    ax.text(0, -0.26, t["center_label"], ha="center", va="center", fontsize=8, color=INK_2)

    # Direct labels: name, share and amount beside each slice, in text ink (never the series colour).
    for w, k, v, s in zip(wedges, keys, values, shares):
        ang = math.radians((w.theta1 + w.theta2) / 2)
        cx, cy = math.cos(ang), math.sin(ang)
        right = cx >= 0
        side = 1 if right else -1
        # Elbow leader: radial tick, then a short horizontal run so the text clears the ring.
        ex, ey = 1.10 * cx, 1.10 * cy
        hx = ex + side * 0.10
        ax.plot([1.02 * cx, ex, hx], [1.02 * cy, ey, ey], color=LEADER, linewidth=0.8, solid_capstyle="round")
        lx, ly = hx + side * 0.04, ey
        ha = "left" if right else "right"
        name = t["names"][k] + (f" ({t['sub'][k]})" if t["sub"][k] else "")
        ax.text(lx, ly + 0.13, f"{s:.1f}%", ha=ha, va="center", fontsize=13, fontweight="bold", color=INK)
        ax.text(lx, ly - 0.025, name, ha=ha, va="center", fontsize=8.5, color=INK)
        ax.text(lx, ly - 0.15, t["amount"].format(v=f"{v:,}"), ha=ha, va="center", fontsize=7.5, color=INK_2)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.25, 1.35)

    fig.text(0.04, 0.94, t["title"], fontsize=13, fontweight="bold", color=INK, ha="left", va="center")
    fig.text(0.04, 0.895, t["subtitle"], fontsize=9, color=INK_2, ha="left", va="center")

    handles = [Patch(facecolor=COLORS[k], edgecolor=SURFACE, label=t["names"][k]) for k in keys]
    leg = fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.115), ncol=4, frameon=False,
                     fontsize=8, handlelength=1.0, handleheight=1.0, columnspacing=1.6)
    for txt in leg.get_texts():
        txt.set_color(INK_2)

    fig.text(0.04, 0.05, t["note"].format(e=f"{INTERSEGMENT:,}"), fontsize=6.5, color=MUTED, ha="left",
             va="center", linespacing=1.5)
    fig.savefig(path, dpi=dpi, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    _font()
    build("es", sys.argv[1])
    build("en", sys.argv[2])
    for (k, v) in REGIONS:
        print(f"{k:6s} {v:>8,} {v / TOTAL * 100:5.1f}%")
