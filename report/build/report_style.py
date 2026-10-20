"""Shared style for the CFA Research Challenge report on Grupo Bimbo: Bimbo palette, fonts, sizes.

Palette sampled from Grupo Bimbo's own 2025 integrated report ("Celebramos") and the logo in its 2025 annual
report to the BMV (page 2): Bimbo blue #0033A0, logo red #EC1C2D, amber #F8AC39, pink #E12565, teal #58B5AC,
bright blue #008AFF, brown #7C4A21.
"""

from pathlib import Path

import i18n

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "report"
OUTPUT_ES = ROOT / "output" / "reporte-es"
CHARTS = (OUTPUT_ES / "charts") if i18n.ES_ON else (REPORT / "charts" / "en")
SECTIONS = (OUTPUT_ES / "sections") if i18n.ES_ON else (REPORT / "sections")
ASSETS = REPORT / "assets"
DATA = REPORT / "data"

# ---- palette -------------------------------------------------------------------------------------------------
BLUE = "#0033A0"      # primary: headings, key series
NAVY = "#001268"      # dark text accents
RED = "#EC1C2D"       # Bimbo logo red: recommendation, warnings
PINK = "#E12565"
AMBER = "#F8AC39"
TEAL = "#58B5AC"
SKY = "#008AFF"
BROWN = "#7C4A21"
GREEN = "#6FB97A"
INK = "#1A1A1A"
GRAY = "#6B6B6B"
LIGHT = "#D9D9D9"
GRID = "#E8E8E8"
BAND = "#F2F2F2"
PALE_BLUE = "#C9D6F2"

REGION = {"na": BLUE, "mx": RED, "eaa": TEAL, "latam": AMBER}
REGION_NAME = {"na": "North America", "mx": "Mexico", "eaa": "Europe, Asia & Africa", "latam": "Latin America"}

# ---- page geometry (A4, points) ---------------------------------------------------------------------------------
PAGE_W, PAGE_H = 595.28, 841.89
MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B = 28.0, 28.0, 30.0, 36.0
GAP = 14.0
RC_W = 164.0                                   # right (figure) column
LC_W = PAGE_W - MARGIN_L - MARGIN_R - GAP - RC_W   # left (text) column
LC_X0, RC_X0 = MARGIN_L, MARGIN_L + LC_W + GAP
FULL_W = PAGE_W - MARGIN_L - MARGIN_R

# ---- chart canvas sizes in inches (placed at exactly this width, so fonts stay at their nominal size) -----------
IN = 72.0
W_RC, W_LC, W_FULL = RC_W / IN, LC_W / IN, FULL_W / IN
DPI = 300


def setup_matplotlib():
    import matplotlib

    matplotlib.use("Agg")
    from matplotlib import font_manager
    import matplotlib.pyplot as plt

    installed = {f.name for f in font_manager.fontManager.ttflist}
    family = "Arial" if "Arial" in installed else "DejaVu Sans"
    plt.rcParams.update({
        "font.family": family,
        "font.size": 6.2,
        "axes.edgecolor": LIGHT,
        "axes.linewidth": 0.5,
        "axes.labelcolor": GRAY,
        "axes.labelsize": 6.0,
        "xtick.color": GRAY,
        "ytick.color": GRAY,
        "xtick.labelsize": 6.0,
        "ytick.labelsize": 6.0,
        "xtick.major.size": 1.8,
        "ytick.major.size": 1.8,
        "xtick.major.width": 0.4,
        "ytick.major.width": 0.4,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "legend.frameon": False,
        "legend.fontsize": 6.0,
        "text.color": INK,
    })
    i18n.patch_matplotlib()
    return plt
