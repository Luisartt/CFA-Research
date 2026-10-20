"""One-page industry summary of Grupo Bimbo (Spanish), built from research/industry.md."""
import sys

import pymupdf

HTML = """
<h1>Industria de Grupo Bimbo: resumen general y riesgos</h1>
<p class="sub">Panificación y botanas empacadas con distribución directa a tienda. Cifras de 2024-2026; fuentes al pie.</p>

<h2>1. Mercado y ciclo de vida</h2>
<p>Bimbo compite en pan empacado, pan dulce, pastelitos, galletas, tortillas, bagels y botanas saladas, en 39 países.
Quedan fuera la panadería artesanal (un sustituto), la masa de maíz y la confitería (Ricolino, vendida en 2022).
Ventas 2025 por región: Norteamérica 44.2%, México 32.9%, Europa-Asia-África 12.7% y Latinoamérica 10.2%.
El mercado global de panificación vale US$638.9 mil millones y crece 2.8% anual (2019-24); se espera 4.7% a 2029.
Ponderado por la mezcla de Bimbo, el crecimiento es de ~4.2% anual, y es en valor (precio e impuestos), no en volumen.
<b>Industria madura</b>: el volumen es plano o cae en países desarrollados (el pan de Flowers cayó 5.8% en volumen en el 2T26) y crece
sobre todo en Latinoamérica y Europa del Este.</p>

<h2>2. Cinco fuerzas</h2>
<table>
<tr><th>Fuerza</th><th>Nivel</th><th>Por qué</th></tr>
<tr><td>Rivalidad</td><td>Alta en EE.UU.; media en México</td><td>Flowers recortó otra vez su guía y su acción cae 75% en cinco años. En México Bimbo lidera con 18.2% del pan empacado ante una competencia fragmentada.</td></tr>
<tr><td>Nuevos entrantes</td><td>Baja a escala, alta local</td><td>Hornear es barato; la barrera es entregar producto fresco (~14 días de vida) con 54,000 rutas. La amenaza real es la marca propia.</td></tr>
<tr><td>Proveedores</td><td>Media</td><td>Las materias primas son ~30% de las ventas. Trigo, azúcar y aceites cotizan en dólares: nadie fija precio, pero el margen bruto sigue al trigo con ~1 año de rezago.</td></tr>
<tr><td>Compradores</td><td>Alta en países desarrollados; baja en emergentes</td><td>Walmart es ~15% de las ventas. El canal moderno pesa 77.7% en Norteamérica; en Latinoamérica domina el canal tradicional.</td></tr>
<tr><td>Sustitutos</td><td>Media-alta</td><td>Artesanal 44.3% y marca propia 9.6% del mercado global; marca propia ~35% de las unidades de pan fresco en EE.UU.; los GLP-1 reducen el gasto en abarrotes.</td></tr>
</table>

<h2>3. Competidores, posición y foso</h2>
<p>Bimbo es el n.º 1 mundial con 3.7% del mercado (1.2 veces el segundo, Mondelez con 3.0%; Gruma 1.1%): el sector es muy fragmentado.
Cuotas de Bimbo: México 18.2% en pan empacado, 28.2% en pan dulce y pastelitos y 18.4% en botanas (n.º 2); EE.UU. ~27% del pan fresco
(marca propia 26%, Flowers 16%); Canadá 13.3%. <b>El foso es regional</b>: ancho en México y Latinoamérica, donde la red de distribución
sostiene un margen EBITDA de ~20.9%, y no demostrado en EE.UU., donde Norteamérica gana 9.6% frente a 11.1% de Flowers en base comparable.
Se erosiona por empaques de mayor vida útil, marca propia, la reforma laboral de México (40 horas hacia 2030) y la regulación de salud
(NOM-051, IEPS de 8% en alimentos de alta densidad calórica).</p>

<h2>4. FODA</h2>
<table>
<tr><td class="w"><b>Fortalezas.</b> Densidad de rutas en México; liderazgos de marca; margen bruto de 52.6%, el más alto entre panificadoras; ningún cliente supera 15%; deuda neta/EBITDA de 2.81x, cerca de la mediana de pares (2.98x).</td>
<td class="w"><b>Debilidades.</b> Norteamérica con menor margen que Flowers y ocho trimestres negativos sin efecto cambiario; ~55% del EBITDA en México; 42-44% de la deuda en dólares frente a flujos en pesos.</td></tr>
<tr><td class="w"><b>Oportunidades.</b> Ganar cuota en EE.UU. mientras Flowers y Campbell's se repliegan; crecimiento y adquisiciones en Latinoamérica y Europa-Asia-África; premiumización (proteína, masa madre); menor capex tras 2025.</td>
<td class="w"><b>Amenazas.</b> Marca propia y cambio a productos baratos; trigo caro hacia 2027; GLP-1 y regulación de salud; revisiones del T-MEC, aranceles y reforma laboral.</td></tr>
</table>

<h2>5. Pares y comparación</h2>
<p>Pares elegibles: Flowers y Gruma (núcleo panificador), más Smucker, Campbell's, Mondelez y PepsiCo. Yamazaki, Aryzta y Arca se muestran pero se excluyen
hasta verificar sus datos. EV/EBITDA de los últimos 12 meses: mediana del núcleo 5.53x, mediana de los seis elegibles 8.27x, Bimbo 6.94x
(7.12x con la participación no controladora a mercado). Bimbo tiene el mayor margen bruto, un margen EBITDA intermedio (14.5%) y la segunda
mayor intensidad de capital (capex 5.2% de ventas frente a ~3.7% de los pares). En cinco años las panificadoras de EE.UU. se desplomaron y Bimbo quedó plano.</p>

<h2>6. Riesgos principales</h2>
<table>
<tr><th>Riesgo</th><th>Qué pasaría</th><th>Efecto en el valor (DCF Gordon)</th></tr>
<tr><td>Trigo y clima</td><td>El trigo sube 35% anual (CBOT dic-26) y el margen bruto lo sigue con ~1 año de rezago; un golpe permanente de 50 pb.</td><td>-Ps 6.1 por acción (-18%)</td></tr>
<tr><td>Norteamérica no se recupera</td><td>El margen vuelve a 8.4% (hoy 9.6%) por consumo débil y marca propia.</td><td>-Ps 6.1 (-18%)</td></tr>
<tr><td>Política en México</td><td>Semana de 46 horas en 2027 y 40 hacia 2030, IEPS mayor a 8%, NOM-051 fase 3 en 2028.</td><td>-Ps 4.7 a -7.0 (-14% a -21%)</td></tr>
<tr><td>Deuda y asignación de capital</td><td>Más capex o una compra grande; S&amp;P tiene perspectiva negativa sobre BBB+ desde mar-2025.</td><td>-Ps 1.5 a -2.0 (-4% a -6%)</td></tr>
<tr><td>Múltiplo de valuación</td><td>El mercado paga el múltiplo de panificadoras (5.53x) y no el de Bimbo hoy (7.12x).</td><td>-Ps 4.3 (-9.5%, método de salida)</td></tr>
</table>
<p>Si los tres riesgos operativos (trigo, Norteamérica y México) coinciden y el múltiplo baja, el valor Gordon caería de 33.55 a 16.58 por acción.
Otros riesgos del sector: tipo de cambio (~44% de las ventas y 42-44% de la deuda en moneda extranjera), aranceles y revisión del T-MEC, y consolidación de competidores.
Las probabilidades e impactos son propuestas <i>[assumption]</i> del asistente; los efectos en valor son <i>[calc]</i> del DCF v3.</p>

<p class="src"><b>Etiquetas:</b> las cifras son <i>[sourced]</i> del Reporte Anual 2025 (pp. 100-113) y la nota 26 de los estados financieros, o <i>[calc]</i> del libro de pares v3;
el juicio sobre ciclo de vida, foso, FODA y riesgos es <i>[assumption]</i> del asistente, pendiente de validación del equipo. Cuotas de México (Sabritas, Gamesa, Bokados) y de Brasil, Colombia y Argentina no tienen fuente local
(<i>[unverified]</i>). Detalle: <code>research/industry.md</code> y <code>research/risks.md</code>.</p>
"""

CSS = """
body { font-family: sans-serif; font-size: 8.7pt; color: #0b0b0b; line-height: 1.22; }
h1 { font-size: 14.5pt; margin: 0 0 1pt 0; }
.sub { color: #52514e; font-size: 8.6pt; margin: 0 0 3pt 0; }
h2 { font-size: 9.8pt; color: #1f4e79; margin: 4pt 0 1pt 0; border-bottom: 0.5pt solid #c3c2b7; }
p { margin: 1pt 0 1pt 0; text-align: justify; }
table { width: 100%; border-collapse: collapse; margin: 1pt 0; }
th { text-align: left; background-color: #e8eef5; font-size: 8.2pt; padding: 1.5pt 2pt; }
td { vertical-align: top; padding: 1.5pt 2pt; border-bottom: 0.4pt solid #e1e0d9; font-size: 8.2pt; }
td.w { width: 50%; border: 0.4pt solid #e1e0d9; }
.src { font-size: 7.2pt; color: #52514e; margin-top: 3pt; }
code { font-size: 6.3pt; }
"""

out = sys.argv[1]
mb = pymupdf.paper_rect("a4") + (-0, -0, -0, -0)
where = pymupdf.Rect(34, 30, mb.width - 34, mb.height - 28)
story = pymupdf.Story(html=HTML, user_css=CSS)
writer = pymupdf.DocumentWriter(out)
pages = 0
more = True
while more:
    dev = writer.begin_page(mb)
    more, _ = story.place(where)
    story.draw(dev)
    writer.end_page()
    pages += 1
writer.close()
print("pages:", pages)
