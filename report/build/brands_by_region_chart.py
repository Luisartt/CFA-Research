"""Grupo Bimbo brand map by region, FY2025 (ES and EN versions).

Bimbo reports a single line of business and no sales by brand or category
[sourced] RA25 p.122 ("La venta de dichos productos constituye la única línea de
negocios"); Capital IQ's line-of-business data has one line ("Bakery Products and
Foods"). The only sales figures here are the FY2025 third-party sales by region
[sourced] EEFF25 note 26, p.85. Brands are listed at the level the annual report
lists them [sourced] RA25 p.83-87, p.100-101; positions (n.º 1, leader) only where
RA25 states them (p.79, p.83-87, p.113), citing Nielsen, Circana and Global Data.

Usage: python brands_by_region_chart.py <out_es.png> <out_en.png>
"""
import sys
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

TOTAL = 426_952
# Third-party net sales FY2025, MXN m, in categorical slot order (colour follows the region).
SALES = {"na": 188_852, "mx": 140_360, "eaa": 54_125, "latam": 43_615}
assert sum(SALES.values()) == TOTAL

COLORS = {"na": "#2a78d6", "mx": "#eb6834", "eaa": "#1baf7a", "latam": "#eda100"}
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"

T = {
    "es": {
        "title": "Grupo Bimbo: sus marcas y dónde las vende, 2025",
        "subtitle": "Bimbo no publica cuánto vende cada marca o producto; la única cifra de ventas es por región.",
        "what": ("Vende más de 9,000 productos con más de 100 marcas: pan de caja y artesanal, bollería, pan dulce, "
                 "pastelitos, galletas, pan tostado, English muffins, bagels, tortillas, flatbread y botanas saladas."),
        "bar": "Ventas netas 2025 por región (MXN 426,952 millones)",
        "share": "{p:.1f}% de las ventas",
        "names": {"na": "Norteamérica", "mx": "México", "eaa": "Europa, Asia y África", "latam": "Latinoamérica"},
        "short": {"na": "Norteamérica", "mx": "México", "eaa": "EAA", "latam": "Latam"},
        "cols": {
            "na": [
                ("h", "EE.UU. (Bimbo Bakeries USA)"),
                ("b", "Bimbo, Oroweat, Arnold, Brownberry, Sara Lee (licencia), Entenmann's, Thomas', Mrs. Baird's, "
                      "Stroehmann, Freihofer's, Boboli, Marinela, Tía Rosa, Francisco, Beefsteak, Lender's"),
                ("n", "Principal proveedor de productos horneados en EE.UU.; Thomas' es n.º 1 en bagels y "
                      "English muffins."),
                ("h", "Canadá"),
                ("b", "Dempster's, Villaggio, POM, Vachon, Stonemill"),
                ("n", "Dempster's lidera el pan empacado."),
                ("h", "Botanas"),
                ("b", "Barcel USA"),
                ("n", "6.º fabricante de botanas saladas en EE.UU."),
            ],
            "mx": [
                ("h", "Marcas principales"),
                ("b", "Bimbo, Oroweat, Wonder, Marinela, Suandy, Lara, Gabi, Del Hogar, Lonchibon"),
                ("n", "N.º 1 en pan empacado y en pastelitos; n.º 2 en galletas."),
                ("h", "Tortillas y tostadas"),
                ("b", "Tía Rosa, Sanissimo, Milpa Real"),
                ("n", "Tía Rosa es n.º 1 en tortillas de harina; Sanissimo y Milpa Real, n.º 1 y 2 en tostadas."),
                ("h", "Botanas (Barcel)"),
                ("b", "Takis, Chips, Big Mix"),
                ("n", "N.º 2 en botanas saladas."),
                ("h", "Pastelería fina (tiendas propias)"),
                ("b", "El Globo, La Balance, El Molino"),
            ],
            "eaa": [
                ("h", "Europa"),
                ("b", "Bimbo, Donuts, Bollycao, Donettes, La Bella Easo, Qe!, Oroweat, The Rustik Bakery, "
                      "New York Bakery, St. Pierre, Vel Pitar, Chef Gourmand, Domneasca, Boierasca"),
                ("n", "Donuts es la marca de donas más vendida en España; New York Bakery lidera los bagels en "
                      "Reino Unido; Vel Pitar lidera el pan empacado en Rumanía."),
                ("h", "Asia y África"),
                ("b", "Bimbo y Mankattan (China); Harvest Gold, Ready Roti y Modern Foods (India); Bimbo y "
                      "Chef du Pain (Marruecos); Moulin d'Or (Túnez)"),
                ("n", "Líder en pan empacado en China."),
            ],
            "latam": [
                ("h", "Marcas principales"),
                ("b", "Bimbo, Pullman, Plus Vita, Nutrella, Wickbold, Seven Boys, Ana Maria, Fargo, Ideal, Supan, "
                      "Artesano, Vital, Pan Todos, Nutra Bien, Crocantissimo, La Zarcerena, Pagnifique, Artepan, "
                      "Urupan, Don Pan, Sanissimo"),
                ("n", "Líder en pan empacado en cada país donde opera. Artesano, creada en Colombia, se vende en "
                      "20 países."),
            ],
        },
        "note": [
            "Bimbo reporta una sola línea de negocio y no desglosa sus ventas por marca ni por categoría "
            "(Reporte Anual 2025, p. 122). Además, Bimbo QSR vende pan congelado a cadenas de comida rápida en "
            "40 países (p. 87).",
            "Barra: ventas a terceros por región, estados financieros 2025, nota 26, p. 85. Marcas y posiciones: "
            "Reporte Anual 2025, pp. 79, 83-87, 100-101 y 113, con datos de Nielsen, Circana y Global Data "
            "citados por la empresa.",
        ],
    },
    "en": {
        "title": "Grupo Bimbo: its brands and where it sells them, FY2025",
        "subtitle": "Bimbo does not disclose sales by brand or product; the only sales split is by region.",
        "what": ("It sells more than 9,000 products under more than 100 brands: packaged and artisan bread, buns, "
                 "sweet bread, cakes, cookies, toast, English muffins, bagels, tortillas, flatbread and salty snacks."),
        "bar": "Net sales FY2025 by region (MXN 426,952 million)",
        "share": "{p:.1f}% of net sales",
        "names": {"na": "North America", "mx": "Mexico", "eaa": "Europe, Asia & Africa", "latam": "Latin America"},
        "short": {"na": "North America", "mx": "Mexico", "eaa": "EAA", "latam": "LatAm"},
        "cols": {
            "na": [
                ("h", "US (Bimbo Bakeries USA)"),
                ("b", "Bimbo, Oroweat, Arnold, Brownberry, Sara Lee (licensed), Entenmann's, Thomas', Mrs. Baird's, "
                      "Stroehmann, Freihofer's, Boboli, Marinela, Tia Rosa, Francisco, Beefsteak, Lender's"),
                ("n", "Top baked-goods supplier in the US; Thomas' is #1 in bagels and English muffins."),
                ("h", "Canada"),
                ("b", "Dempster's, Villaggio, POM, Vachon, Stonemill"),
                ("n", "Dempster's leads packaged bread."),
                ("h", "Snacks"),
                ("b", "Barcel USA"),
                ("n", "Sixth-largest US salty-snack maker."),
            ],
            "mx": [
                ("h", "Main brands"),
                ("b", "Bimbo, Oroweat, Wonder, Marinela, Suandy, Lara, Gabi, Del Hogar, Lonchibon"),
                ("n", "#1 in packaged bread and in cakes; #2 in cookies."),
                ("h", "Tortillas and tostadas"),
                ("b", "Tia Rosa, Sanissimo, Milpa Real"),
                ("n", "Tia Rosa is #1 in flour tortillas; Sanissimo and Milpa Real are #1 and #2 in tostadas."),
                ("h", "Snacks (Barcel)"),
                ("b", "Takis, Chips, Big Mix"),
                ("n", "#2 in salty snacks."),
                ("h", "Fine pastry (own stores)"),
                ("b", "El Globo, La Balance, El Molino"),
            ],
            "eaa": [
                ("h", "Europe"),
                ("b", "Bimbo, Donuts, Bollycao, Donettes, La Bella Easo, Qe!, Oroweat, The Rustik Bakery, "
                      "New York Bakery, St. Pierre, Vel Pitar, Chef Gourmand, Domneasca, Boierasca"),
                ("n", "Donuts is Spain's best-selling doughnut brand; New York Bakery leads bagels in the UK; "
                      "Vel Pitar leads packaged bread in Romania."),
                ("h", "Asia and Africa"),
                ("b", "Bimbo and Mankattan (China); Harvest Gold, Ready Roti and Modern Foods (India); Bimbo and "
                      "Chef du Pain (Morocco); Moulin d'Or (Tunisia)"),
                ("n", "Leader in packaged bread in China."),
            ],
            "latam": [
                ("h", "Main brands"),
                ("b", "Bimbo, Pullman, Plus Vita, Nutrella, Wickbold, Seven Boys, Ana Maria, Fargo, Ideal, Supan, "
                      "Artesano, Vital, Pan Todos, Nutra Bien, Crocantissimo, La Zarcerena, Pagnifique, Artepan, "
                      "Urupan, Don Pan, Sanissimo"),
                ("n", "Packaged-bread leader in every country where it operates. Artesano, created in Colombia, is "
                      "sold in 20 countries."),
            ],
        },
        "note": [
            "Bimbo reports a single line of business and does not split sales by brand or category "
            "(2025 Annual Report, p.122). Bimbo QSR also sells frozen bread to fast-food chains in 40 countries "
            "(p.87).",
            "Bar: third-party sales by region, 2025 financial statements, note 26, p.85. Brands and positions: "
            "2025 Annual Report, pp.79, 83-87, 100-101 and 113, citing Nielsen, Circana and Global Data figures "
            "quoted by the company.",
        ],
    },
}

MULTIWORD = ["La Bella Easo", "The Rustik Bakery", "New York Bakery", "St. Pierre", "Vel Pitar", "Chef Gourmand",
             "Harvest Gold", "Ready Roti", "Modern Foods", "Chef du Pain", "Moulin d'Or", "Mrs. Baird's", "Sara Lee",
             "Tía Rosa", "Tia Rosa", "Seven Boys", "Plus Vita", "Ana Maria", "Pan Todos", "Nutra Bien",
             "La Zarcerena", "Don Pan", "Big Mix", "Milpa Real", "Del Hogar", "El Globo", "La Balance", "El Molino",
             "Barcel USA", "Bimbo Bakeries USA"]


def _keep_brands(text: str) -> str:
    for name in MULTIWORD:
        text = text.replace(name, name.replace(" ", " "))
    return text


STYLE = {"h": (8.2, "bold", INK, 0.016), "b": (7.6, "normal", INK, 0.004), "n": (7.1, "normal", INK_2, 0.005)}


def _font() -> None:
    installed = {f.name for f in font_manager.fontManager.ttflist}
    plt.rcParams["font.family"] = [f for f in ("Segoe UI", "Arial") if f in installed] or ["DejaVu Sans"]


def _fit_text(fig, renderer, x, y, text, width_frac, size, weight, color, italic=False):
    """Draw text top-left at (x, y), wrapping until it fits width_frac; return its height (fig fraction)."""
    width_px = width_frac * fig.bbox.width
    chars = max(12, int(len(text)))
    while True:
        wrapped = textwrap.fill(text, width=chars, break_long_words=False)
        t = fig.text(x, y, wrapped, fontsize=size, fontweight=weight, color=color, ha="left", va="top",
                     linespacing=1.38, fontstyle="italic" if italic else "normal")
        bb = t.get_window_extent(renderer)
        if bb.width <= width_px or chars <= 12:
            return bb.height / fig.bbox.height
        t.remove()
        chars -= 1


def build(lang: str, path: str) -> None:
    t = T[lang]
    keys = list(SALES)
    dpi = 200
    fig = plt.figure(figsize=(8.6, 6.6), dpi=dpi, facecolor=SURFACE)
    renderer = fig.canvas.get_renderer()
    left, right = 0.045, 0.955

    fig.text(left, 0.962, t["title"], fontsize=13.5, fontweight="bold", color=INK, ha="left", va="center")
    fig.text(left, 0.925, t["subtitle"], fontsize=9, color=INK_2, ha="left", va="center")
    _fit_text(fig, renderer, left, 0.902, t["what"], right - left, 7.8, "normal", INK_2)

    # 100% stacked bar of the only sourced sales split.
    fig.text(left, 0.828, t["bar"], fontsize=8, fontweight="bold", color=INK, ha="left", va="center")
    ax = fig.add_axes([left, 0.73, right - left, 0.08])
    ax.set_xlim(0, TOTAL)
    ax.set_ylim(0, 1)
    ax.axis("off")
    x0 = 0
    for k in keys:
        v = SALES[k]
        ax.add_patch(Rectangle((x0, 0), v, 1, facecolor=COLORS[k], edgecolor=SURFACE, linewidth=4 * 72 / dpi))
        ax.text(x0 + v / 2, 0.64, t["short"][k], ha="center", va="center", fontsize=8.2, color=INK)
        ax.text(x0 + v / 2, 0.32, f"{v / TOTAL * 100:.1f}%", ha="center", va="center", fontsize=9.5,
                fontweight="bold", color=INK)
        x0 += v

    # Four equal brand columns; a colour swatch ties each to its bar segment.
    gutter = 0.022
    col_w = (right - left - 3 * gutter) / 4
    top = 0.672
    lowest = 1.0
    sw_h = 0.018
    sw_w = sw_h * fig.bbox.height / fig.bbox.width
    for i, k in enumerate(keys):
        x = left + i * (col_w + gutter)
        fig.patches.append(Rectangle((x, top - sw_h), sw_w, sw_h, transform=fig.transFigure,
                                     facecolor=COLORS[k], edgecolor="none"))
        nh = _fit_text(fig, renderer, x + sw_w + 0.008, top + 0.002, t["names"][k], col_w - sw_w - 0.008,
                       9.2, "bold", INK)
        y = top - max(nh, sw_h) - 0.006
        fig.text(x, y, t["share"].format(p=SALES[k] / TOTAL * 100), fontsize=7.8, color=INK_2,
                 ha="left", va="top")
        y -= 0.022
        for kind, text in t["cols"][k]:
            size, weight, color, gap = STYLE[kind]
            y -= gap
            y -= _fit_text(fig, renderer, x, y, _keep_brands(text), col_w, size, weight, color,
                           italic=(kind == "n"))
        lowest = min(lowest, y)

    ny = lowest - 0.035
    for line in t["note"]:
        ny -= _fit_text(fig, renderer, left, ny, line, right - left, 6.6, "normal", MUTED) + 0.006
    assert ny > 0.0, "footer runs off the canvas"
    fig.savefig(path, dpi=dpi, facecolor=SURFACE, bbox_inches="tight", pad_inches=0.28)
    plt.close(fig)


if __name__ == "__main__":
    _font()
    build("es", sys.argv[1])
    build("en", sys.argv[2])
    print("ok")
