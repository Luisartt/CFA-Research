"""PDF (Spanish): how Bimbo's value is built (cash flow, country risk, WACC), what moves it, and the industry reading.

Numbers that come from the model are read from valuation/inputs/consolidated_results.json (written by
valuation/build/consolidate_models.py), so the PDF always matches the consolidated DCF. Country-risk weights and
industry facts are typed from valuation/valuation.md and research/industry.md and tagged in the sources note.

Usage (from the project folder): python -I report/build/valuation_concepts_pdf.py
Writes output/bimbo-flujo-wacc-riesgo-pais-e-industria.pdf
"""

from __future__ import annotations

import io
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "bimbo-flujo-wacc-riesgo-pais-e-industria.pdf"
R = json.loads((ROOT / "valuation/inputs/consolidated_results.json").read_text(encoding="utf-8"))

C = R["consolidated"]
run, st = C["run"], C["state"]
A = R["inputs"]["alejandro"]
lev = {x["lever"]: x for x in C["levers"]}
rev_ = C["reverse"]
PRICE = R["price"]


def n(x: float, d: int = 0) -> str:
    return f"{x:,.{d}f}"


def sg(x: float) -> str:  # signed value per share with a true minus sign
    return f"{x:+.2f}".replace("-", "−")


def pct(x: float, d: int = 2) -> str:
    return f"{x * 100:.{d}f}%"


# ---- model numbers -------------------------------------------------------------------------------------------
y = 4  # FY2030 index
rev, ebitda, da = run["rev"][y], run["ebitda"][y], run["da"][y]
ebit = ebitda - da
tax = ebit * st["tax_ebit"]
nopat = ebit - tax
capex, leases, dwc, fcff = run["capex"][y], run["leases"][y], run["dwc"][y], run["fcff"][y]
flows = " / ".join(f"{v / 1000:.1f}" for v in run["fcff"])
rf, erp, crp = A["rf"], A["rm"] - A["rf"], A["crp"]
ke, wacc, beta_l = run["ke"], run["wacc"], run["beta_l"]
wd = st["de"] / (1 + st["de"])
kd, tax_m = A["kd"], A["tax_marg"]
mcap = PRICE * st["shares"]

HTML = f"""
<h1>Bimbo: cómo se construye el valor y qué lo mueve</h1>
<p class="sub">Flujo de caja, riesgo país, WACC, factores que mueven el precio e industria. DCF consolidado al 19-oct-2026;
precio {PRICE:.2f} (16-oct-2026). Valores por acción en MXN; montos en millones de MXN.</p>

<h2>1. El flujo de caja (FCFF)</h2>
<p>El flujo libre es lo que deja el negocio después de impuestos e inversión, antes de pagarles a acreedores y accionistas.
Ejemplo con FY2030:</p>
<table>
<tr><th>Concepto</th><th class="r">Monto</th><th>De dónde sale</th></tr>
<tr><td><b>Ventas</b></td><td class="r">{n(rev)}</td><td>Promedio de la suma por regiones de la v3 (México 5.25-5.5%, Latinoamérica 6.5%, Norteamérica 3% en pesos, Europa-Asia-África 4.5%) y del consenso de Capital IQ</td></tr>
<tr><td><b>EBITDA</b> (margen {pct(ebitda / rev, 1)})</td><td class="r">{n(ebitda)}</td><td>Margen bruto (trigo) menos gastos (productividad): promedio de la v3 (15.3%) y del consenso (14.7%)</td></tr>
<tr><td>&#8722; Depreciación</td><td class="r">{n(da)}</td><td>5.85% de las ventas</td></tr>
<tr><td>&#8722; Impuestos ({pct(st["tax_ebit"], 0)} del EBIT)</td><td class="r">{n(tax)}</td><td>Promedio de la tasa efectiva (34%) y la estatutaria (30%)</td></tr>
<tr><td><b>= Utilidad operativa después de impuestos</b></td><td class="r"><b>{n(nopat)}</b></td><td></td></tr>
<tr><td>+ Depreciación</td><td class="r">{n(da)}</td><td>No es salida de efectivo</td></tr>
<tr><td>&#8722; Capex ({pct(capex / rev, 1)} de las ventas)</td><td class="r">{n(capex)}</td><td>Plantas y rutas: promedio de la v3 (5.5%) y del consenso (4.8%)</td></tr>
<tr><td>&#8722; Arrendamientos nuevos</td><td class="r">{n(leases)}</td><td>Principal (1.39% de las ventas) más el crecimiento del pasivo por arrendamiento (8.15% de las ventas)</td></tr>
<tr><td>+ Capital de trabajo</td><td class="r">{n(dwc)}</td><td>Bimbo cobra en ~20 días y paga en ~70, así que crecer le libera efectivo</td></tr>
<tr><td><b>= Flujo libre</b></td><td class="r"><b>{n(fcff)}</b></td><td></td></tr>
</table>
<p>De 2026 a 2030 el flujo va {flows} mil millones. Se descuentan al WACC y se suma el valor terminal, que pesa
{pct(run["tv_share_exit"], 0)} del valor de la empresa. A ese valor se le restan la deuda (con arrendamientos) y los minoritarios,
se suma el efectivo y se divide entre las acciones: eso da el valor por acción.</p>

<h2>2. El riesgo país (2.05%)</h2>
<ul>
<li><b>Punto de partida.</b> Los flujos están en pesos, así que la base es el M-Bono a 10 años ({pct(0.0926)}, Capital IQ, 16-oct-2026).
Ese bono ya trae el riesgo de impago de México (1.75%, Damodaran, julio 2026). Se lo quitamos, queda una tasa libre de riesgo de
{pct(rf)}, y el riesgo país se suma una sola vez.</li>
<li><b>Ponderación.</b> Cada región tiene su prima, y se pondera por dónde Bimbo gana su EBITDA:</li>
</ul>
<table>
<tr><th>Región</th><th class="r">Prima país</th><th class="r">Peso por EBITDA FY2025</th></tr>
<tr><td>Norteamérica</td><td class="r">0.17%</td><td class="r">28.8%</td></tr>
<tr><td>México (1.75% &#215; 1.55, la volatilidad relativa de las acciones frente a los bonos)</td><td class="r">2.72%</td><td class="r">55.4%</td></tr>
<tr><td>Europa, Asia y África</td><td class="r">2.63%</td><td class="r">9.8%</td></tr>
<tr><td>Latinoamérica (sin Venezuela)</td><td class="r">3.94%</td><td class="r">6.0%</td></tr>
<tr><td><b>Ponderado</b></td><td class="r"><b>2.05%</b></td><td class="r">100%</td></tr>
</table>
<ul>
<li><b>Por qué EBITDA y no ventas.</b> México es 32% de las ventas pero 55% del EBITDA, y el valor sale de los flujos. Ponderado por
ventas da 1.70%, y el Gordon de la v3 sube de 33.55 a 36.05. Es una decisión abierta del equipo.</li>
<li><b>Por qué no se multiplica por la beta.</b> El riesgo soberano no es riesgo de mercado, así que se suma directo.</li>
</ul>

<h2>3. El WACC ({pct(wacc)})</h2>
<ul>
<li><b>Costo de capital (ke)</b> = {pct(rf)} + {beta_l:.3f} &#215; {pct(erp)} + {pct(crp)} = <b>{pct(ke)}</b>.
La beta desapalancada de Damodaran para alimentos procesados es 0.53 (v3) o 0.56 (Diego); el consolidado usa {st["beta_u"]:.3f}.
Reapalancada con la deuda de Bimbo da {beta_l:.3f}, y la regresión propia de Bimbo (0.82) la confirma.
Las betas de los comparables (0.04 a 0.43) son demasiado bajas para usarlas.</li>
<li><b>Costo de deuda</b> = M-Bono + 0.45% (el spread del bono BIMBO 26) = {pct(kd)}, que después de impuestos ({pct(tax_m, 0)}) es {pct(kd * (1 - tax_m))}.</li>
<li><b>Pesos a valor de mercado.</b> Capital {pct(1 - wd, 1)} ({PRICE:.2f} &#215; {n(st["shares"], 1)} millones de acciones = {n(mcap)}) y
deuda con arrendamientos {pct(wd, 1)} ({n(st["debt"])}).</li>
<li><b>WACC</b> = {pct(1 - wd, 1)} &#215; {pct(ke)} + {pct(wd, 1)} &#215; {pct(kd * (1 - tax_m))} = <b>{pct(wacc)}</b>.</li>
</ul>

<h2>4. Qué mueve más el precio</h2>
<p>Efecto por acción de cada cambio, contra la base del DCF consolidado (múltiplo de salida {run["ps_exit"]:.2f}; Gordon {run["ps_gordon_ronic"]:.2f}):</p>
<table>
<tr><th>Factor</th><th>Cambio</th><th class="r">Múltiplo de salida</th><th class="r">Gordon</th></tr>
<tr><td>Cuánto rinde el capital que se reinvierte</td><td>14.6% &#8594; {pct(run["ronic_naive"], 1)}</td><td class="r">&#8212;</td><td class="r">{run["ps_gordon_ronic"]:.2f} &#8594; {run["ps_gordon_naive"]:.2f}</td></tr>
<tr><td>Múltiplo de salida</td><td>&#8722;0.5x</td><td class="r">{sg(lev["Exit multiple -0.5x"]["d_exit"])}</td><td class="r">&#8212;</td></tr>
<tr><td>Tasa de descuento (tasas en México, riesgo país)</td><td>+0.5 pp</td><td class="r">{sg(lev["WACC +50 bp"]["d_exit"])}</td><td class="r">{sg(lev["WACC +50 bp"]["d_gordon_ronic"])}</td></tr>
<tr><td>Margen EBITDA (trigo, productividad en EE.UU.)</td><td>&#8722;50 pb cada año</td><td class="r">{sg(lev["EBITDA margin -50 bp every year"]["d_exit"])}</td><td class="r">{sg(lev["EBITDA margin -50 bp every year"]["d_gordon_ronic"])}</td></tr>
<tr><td>Capex</td><td>+50 pb de las ventas</td><td class="r">{sg(lev["Capex +50 bp of revenue every year"]["d_exit"])}</td><td class="r">{sg(lev["Capex +50 bp of revenue every year"]["d_gordon_ronic"])}</td></tr>
<tr><td>Crecimiento de ventas</td><td>&#8722;50 pb al año</td><td class="r">{sg(lev["Revenue growth -50 bp every year"]["d_exit"])}</td><td class="r">{sg(lev["Revenue growth -50 bp every year"]["d_gordon_ronic"])}</td></tr>
</table>
<p>Lo que más pesa es el valor terminal (múltiplo y reinversión) y la tasa; la operación del día a día pesa menos.
Para justificar los {PRICE:.2f} actuales se necesitaría una de estas tres cosas: un múltiplo de salida de
{rev_["exit_multiple_for_price"]:.2f}x, un WACC de {pct(rev_["wacc_for_price_exit"])}, o ventas creciendo
{rev_["growth_shift_for_price_exit"] * 100:.1f} puntos más cada año.</p>
<p><b>Fuera del modelo, lo que hay que vigilar:</b></p>
<ul>
<li>El trigo: cotiza en dólares, el margen bruto lo sigue con un año de rezago y el futuro de diciembre 2026 en Chicago sube 35% anual.</li>
<li>El tipo de cambio: 44.6% de las ventas son de Norteamérica y 42-44% de la deuda está en dólares.</li>
<li>Las tasas de Banxico, que mueven la tasa libre de riesgo.</li>
<li>Los márgenes en Norteamérica con el nuevo CEO.</li>
</ul>

<h2>5. La industria: qué cae y por qué Bimbo aguanta</h2>
<p><b>El matiz.</b> La industria no cae en valor: la panificación global crece 4.7% al año entre 2024 y 2029 (Global Data).
Lo que cae es el volumen en mercados desarrollados (el pan de Flowers: &#8722;5.8% en el 2T26) y el precio en bolsa de las panificadoras puras
(Flowers &#8722;75% en cinco años, Campbell&#8217;s &#8722;50%). El valor crece por precio, no por volumen.</p>
<p><b>Por qué cae en mercados desarrollados:</b></p>
<ol>
<li><b>Marca propia.</b> Es ~35% de las unidades de pan fresco en EE.UU., y los supermercados tienen mucho poder de negociación
(Walmart es ~15% de las ventas de Bimbo).</li>
<li><b>Salud y regulación.</b> Hay rechazo al azúcar y a la harina refinada. Los usuarios de GLP-1 recortan 5.3% su gasto en el súper
en seis meses (estudio observacional de Cornell). En México pesan el etiquetado frontal (fase 3 en 2028), el IEPS de 8% y las reglas en escuelas.</li>
<li><b>Panaderías artesanales.</b> Son 44.3% del mercado global.</li>
<li><b>Trigo.</b> Es un insumo en dólares que nadie controla; el futuro de diciembre 2026 en Chicago sube 35% anual.</li>
<li><b>Empaques de mayor vida en anaquel.</b> Le restan ventaja a la distribución directa a tienda.</li>
</ol>
<p><b>Por qué Bimbo aguanta:</b></p>
<ul>
<li><b>México y Latinoamérica compensan.</b> El comprador está fragmentado (tienditas) y Bimbo es dueño de más de 54,000 rutas.
El margen EBITDA es ~20.9% en México contra 9.6% en Norteamérica.</li>
<li><b>Escala.</b> Es el n.º 1 mundial con 3.7% del mercado, ~27% del pan fresco en EE.UU. y 28.2% del pan dulce en México.</li>
<li><b>Mejor margen bruto del sector.</b> 52.6% contra 48.6% de Flowers, gracias a su escala de compras.</li>
</ul>
<p>Pero en EE.UU. no es inmune: Norteamérica tuvo ocho trimestres negativos (1T24-4T25) sin contar el tipo de cambio, y su margen está
debajo del de Flowers (9.6% contra 11.1%, en base comparable). &#8220;Se mantiene&#8221; en realidad quiere decir que México compensa a Estados Unidos.</p>

<h2>6. Para pensar y siguiente paso</h2>
<p><b>Para pensar.</b> Si el volumen de pan en EE.UU. cae 2-4% al año, ¿de dónde sale el 3% de crecimiento en pesos que suponemos para
Norteamérica: precio, participación de mercado o tipo de cambio? El supuesto actual es ~1.5% en dólares más ~1.5% de depreciación del peso,
con la categoría cayendo 2-4% en volumen y subiendo 1-2% en precio y mezcla: Bimbo tendría que superar a la categoría por ~3 puntos al año.</p>
<p><b>Siguiente paso.</b> Conseguir la serie de participación de mercado de Circana por categoría y la división de volumen contra precio de
Bimbo en EE.UU. Es la evidencia que hoy le falta al pilar 2 de la tesis.</p>

<p class="src"><b>Etiquetas y fuentes.</b> Flujo, WACC, sensibilidades y DCF inverso: <i>[calc]</i> del DCF consolidado
(<code>valuation/BIMBOA_DCF_consolidated_v1.xlsx</code>; propuesta del asistente, pendiente de decisión del equipo).
M-Bono y consenso: <i>[sourced]</i> Capital IQ (16-oct-2026). Spread de default, prima de mercado, primas país y betas: <i>[sourced]</i>
Damodaran (enero y julio de 2026); pesos por región: <code>valuation/valuation.md</code> sección 7. Industria: <i>[sourced]</i> Reporte Anual 2025
(pp. 100-113), Flowers 10-K, Circana y reporte macro, vía <code>research/industry.md</code> (el estudio de GLP-1 es observacional).
Por qué Bimbo aguanta: <i>[assumption]</i> del asistente, pendiente de validación del equipo.</p>
"""

CSS = """
body { font-family: sans-serif; font-size: 9.2pt; color: #0b0b0b; line-height: 1.28; }
h1 { font-size: 16pt; margin: 0 0 2pt 0; color: #1f4e79; }
.sub { color: #52514e; font-size: 8.8pt; margin: 0 0 6pt 0; }
h2 { font-size: 11pt; color: #1f4e79; margin: 8pt 0 3pt 0; border-bottom: 0.6pt solid #c3c2b7; }
p { margin: 3pt 0 3pt 0; text-align: left; }
ul, ol { margin: 2pt 0 3pt 0; }
li { margin: 0 0 2.5pt 0; }
table { width: 100%; border-collapse: collapse; margin: 4pt 0 5pt 0; }
th { text-align: left; color: #1f4e79; font-size: 8.6pt; padding: 2.5pt 3pt; border-bottom: 1pt solid #1f4e79; }
td { vertical-align: top; padding: 2.5pt 3pt; border-bottom: 0.4pt solid #e1e0d9; font-size: 8.6pt; }
th.r, td.r { text-align: right; }
.src { font-size: 7.6pt; color: #52514e; margin-top: 8pt; }
code { font-size: 7pt; }
"""

FOOTER = "Grupo Bimbo (BIMBOA) — flujo, WACC, riesgo país e industria — borrador del asistente, 19-oct-2026"


def build() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    media = pymupdf.paper_rect("a4")
    where = pymupdf.Rect(42, 40, media.width - 42, media.height - 52)
    story = pymupdf.Story(html=HTML, user_css=CSS)
    buf = io.BytesIO()  # in memory: no temporary file to clean up
    writer = pymupdf.DocumentWriter(buf)
    more = True
    while more:
        dev = writer.begin_page(media)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
    writer.close()
    doc = pymupdf.open("pdf", buf.getvalue())
    total = doc.page_count
    grey = (0.32, 0.32, 0.31)
    for i in range(total):
        page = doc[i]
        page.insert_text((42, media.height - 30), FOOTER, fontname="helv", fontsize=7.2, color=grey)
        label = f"Página {i + 1} de {total}"
        width = pymupdf.get_text_length(label, fontname="helv", fontsize=7.2)
        page.insert_text((media.width - 42 - width, media.height - 30), label, fontname="helv", fontsize=7.2, color=grey)
    doc.save(str(OUT), garbage=3, deflate=True)
    doc.close()
    print("pages:", total, "->", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
