"""Grupo Bimbo bakeries and plants by organization and activity, end-2025 (Spanish chart).

A proxy, not a revenue split: Bimbo discloses no sales by product (RA25 p.122, single line
of business). Plant counts [sourced] RA25 p.115-116 ("Número de panaderías y plantas");
activity of each subsidiary [sourced] RA25 p.114 (Bimbo S.A. panificación, Barcel S.A.
botanas, BBU and Canada Bread panificación). Plants outside Mexico and North America are
listed by country, not by activity; they are counted with bakery [assumption].

Usage: python plants_by_activity_chart.py <out.png>
"""
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

BAKERY = "#6250d6"        # validated pair with SNACKS (CVD and normal-vision pass)
BAKERY_BY_COUNTRY = "#b7afea"  # same hue, lighter: activity not stated, counted with bakery
SNACKS = "#e87ba4"
OTHER = "#898781"
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"

# (group, [(label, count, kind)]) in RA25 p.115-116 order within each group.
GROUPS = [
    ("México", [("Bimbo S.A.", 30, "bakery"), ("Barcel S.A.", 7, "snacks"),
                ("Moldes y Exhibidores", 1, "other")]),
    ("Norteamérica", [("Bimbo Bakeries USA", 54, "bakery"), ("Bimbo Canadá", 17, "bakery"),
                      ("Bimbo QSR", 4, "bakery"), ("Organización Barcel (EE.UU.)", 2, "snacks")]),
    ("Resto del mundo (listadas por país)", [("Europa", 61, "country"), ("Latinoamérica", 26 + 16, "country"),
                                             ("Asia", 26, "country"), ("África", 5, "country")]),
]
COLOR = {"bakery": BAKERY, "country": BAKERY_BY_COUNTRY, "snacks": SNACKS, "other": OTHER}

totals = {k: sum(c for _, rows in GROUPS for _, c, kind in rows if kind == k) for k in COLOR}
assert sum(totals.values()) == 249, totals
assert (totals["bakery"], totals["country"], totals["snacks"], totals["other"]) == (105, 134, 9, 1), totals


def _font() -> None:
    installed = {f.name for f in font_manager.fontManager.ttflist}
    plt.rcParams["font.family"] = [f for f in ("Segoe UI", "Arial") if f in installed] or ["DejaVu Sans"]


def build(path: str) -> None:
    dpi = 200
    fig = plt.figure(figsize=(8.6, 6.9), dpi=dpi, facecolor=SURFACE)
    left, right = 0.045, 0.955
    fig.text(left, 0.962, "Bimbo es ante todo panificadora: 9 de sus 249 plantas son de botanas",
             fontsize=13.5, fontweight="bold", color=INK, ha="left", va="center")
    fig.text(left, 0.925, "Panaderías y plantas por organización al cierre de 2025. Son plantas, no ventas: "
             "Bimbo no publica sus ventas por producto.", fontsize=8.8, color=INK_2, ha="left", va="center")

    handles = [
        Patch(facecolor=BAKERY, label=f"Panificación: {totals['bakery']}"),
        Patch(facecolor=BAKERY_BY_COUNTRY, label=f"Listadas por país, contadas con panificación: {totals['country']}"),
        Patch(facecolor=SNACKS, label=f"Botanas (Barcel): {totals['snacks']}"),
        Patch(facecolor=OTHER, label=f"Moldes y exhibidores: {totals['other']}"),
    ]
    leg = fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(left - 0.006, 0.905), ncol=4,
                     frameon=False, fontsize=7.6, handlelength=1.0, handleheight=1.0, columnspacing=1.3,
                     handletextpad=0.5)
    for txt in leg.get_texts():
        txt.set_color(INK)

    ax = fig.add_axes([0.33, 0.16, 0.6, 0.68])
    ax.set_facecolor(SURFACE)
    y = 0.0
    yticks, ylabels = [], []
    for g, (group, rows) in enumerate(GROUPS):
        if g:
            y += 0.7
        n = sum(c for _, c, _ in rows)
        ax.text((left - 0.33) / 0.6, y, f"{group}  ·  {n}", transform=ax.get_yaxis_transform(), ha="left", va="center",
                fontsize=8.6, fontweight="bold", color=INK)
        y += 1.0
        for label, count, kind in rows:
            ax.barh(y, count, height=0.62, color=COLOR[kind], edgecolor=SURFACE, linewidth=4 * 72 / dpi)
            ax.text(count + 0.8, y, f"{count}", ha="left", va="center", fontsize=8.2, color=INK)
            yticks.append(y)
            ylabels.append(label)
            y += 1.0
    ax.set_yticks(yticks, labels=ylabels, fontsize=8.2, color=INK)
    ax.tick_params(axis="y", length=0, pad=6)
    ax.set_ylim(y - 0.3, -0.8)
    ax.set_xlim(0, 68)
    ax.xaxis.set_visible(False)
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color("#c3c2b7")
    ax.spines["left"].set_linewidth(0.8)

    notes = [
        "Plantas no son ventas, y la cifra de botanas puede quedarse corta: Barcel USA también vende producto "
        "importado de sus plantas en México (p. 83);",
        "fuera de México y Norteamérica el reporte lista las plantas por país, no por actividad (Bimbo es n.º 3 en "
        "botanas en Latinoamérica, p. 113), y una planta",
        "de botanas puede ser más grande que una panadería.",
        "Fuente: Grupo Bimbo, Reporte Anual 2025: actividad de cada subsidiaria (p. 114) y panaderías y plantas por "
        "organización (pp. 115-116). Bimbo no desglosa sus ventas por producto (p. 122).",
    ]
    fig.text(left, 0.105, "\n".join(notes[:3]), fontsize=6.6, color=MUTED, ha="left", va="top", linespacing=1.5)
    fig.text(left, 0.03, notes[3], fontsize=6.6, color=MUTED, ha="left", va="center")
    fig.savefig(path, dpi=dpi, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    _font()
    build(sys.argv[1])
    print(totals)
