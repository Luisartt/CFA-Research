"""One-page industry summary of Grupo Bimbo (Spanish), built from research/industry.md."""
import sys

import pymupdf

HTML = """
<h1>Industria de Grupo Bimbo: análisis general y riesgos</h1>
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

<h2>6. Riesgos de inversión (los 14)</h2>
<p>Probabilidad (P) e impacto (I) en escala de 1 a 5 a 12-24 meses; puntaje = P x I. El efecto en valor se mide sobre el DCF Gordon de 33.55 por acción
(cambiando solo el supuesto que mueve cada riesgo). Si los tres riesgos operativos (R1, R2 y R4) coinciden y el múltiplo baja a 5.53x, el valor Gordon cae a 16.58.</p>
<table>
<tr><th>ID</th><th>Riesgo</th><th>Qué pasaría</th><th>P</th><th>I</th><th>Pts</th><th>Efecto en valor</th><th>¿Ya en el precio?</th></tr>
<tr><td>R1</td><td><b>Trigo y clima</b></td><td>Trigo +35% anual (CBOT dic-26); el margen bruto lo sigue con ~1 año de rezago; golpe permanente de 50 pb</td><td>3</td><td>4</td><td>12</td><td>-Ps 6.1 (-18%)</td><td>No: el consenso no ve baja del margen bruto</td></tr><tr><td>R2</td><td><b>Norteamérica no se recupera</b></td><td>El margen vuelve a 8.4% (hoy 9.6%) por consumo débil y marca propia</td><td>3</td><td>4</td><td>12</td><td>-Ps 6.1 (-18%)</td><td>Parcial</td></tr><tr><td>R3</td><td><b>Deuda y capital</b></td><td>Más capex o compra grande a 8-9x EBITDA; S&amp;P con perspectiva negativa sobre BBB+ desde mar-2025</td><td>3</td><td>3</td><td>9</td><td>-Ps 1.5 a -2.0 (-4% a -6%)</td><td>Parcial</td></tr><tr><td>R4</td><td><b>Política en México</b></td><td>Semana de 46 horas en 2027 y 40 hacia 2030, IEPS mayor a 8%, NOM-051 fase 3 en 2028</td><td>3</td><td>4</td><td>12</td><td>-Ps 4.7 a -7.0 (-14% a -21%)</td><td>Parcial: IEPS 8% sí está</td></tr><tr><td>R5</td><td><b>Múltiplo de salida</b></td><td>El mercado paga 5.53x (panificadoras) y no 7.12x (Bimbo hoy)</td><td>3</td><td>3</td><td>9</td><td>-Ps 4.3 (-9.5%, método de salida)</td><td>Parcial</td></tr><tr><td>R6</td><td><b>Tipo de cambio</b></td><td>El peso se deprecia menos de 1.5% anual (inflación EE.UU. 3.74% vs México 3.45%)</td><td>3</td><td>3</td><td>9</td><td>-Ps 2.2 (-6.5%)</td><td>—</td></tr><tr><td>R7</td><td><b>T-MEC y aranceles</b></td><td>El T-MEC no se renueva (revisiones anuales a 2036); aranceles a insumos o productos</td><td>3</td><td>2</td><td>6</td><td>Sin cuantificar</td><td>Produce localmente</td></tr><tr><td>R8</td><td><b>GLP-1 y hábitos de salud</b></td><td>Menos volumen de pan dulce y botanas: el gasto en abarrotes baja 5.3% a seis meses (observacional)</td><td>3</td><td>2</td><td>6</td><td>Sin cuantificar</td><td>—</td></tr><tr><td>R9</td><td><b>Gobierno corporativo</b></td><td>Familia Servitje controla 72.03%; 7 de 18 consejeros independientes; cláusulas anti-adquisición</td><td>4</td><td>2</td><td>8</td><td>Se ve en el múltiplo, no en el flujo</td><td>—</td></tr><tr><td>R10</td><td><b>Demandas colectivas Canadá</b></td><td>Pan Canadá, sin provisión (multa de US$38m pagada en 2023)</td><td>2</td><td>1</td><td>2</td><td>Menor</td><td>—</td></tr><tr><td>R11</td><td><b>Pensiones multi-patrón EE.UU.</b></td><td>Pasivos por retiro y contribuciones (2,700 en 2025)</td><td>2</td><td>1</td><td>2</td><td>Ya en el puente a valor (0.19 por acción)</td><td>Sí</td></tr><tr><td>R12</td><td><b>Agua y economía circular</b></td><td>101 plantas en estrés hídrico; nueva ley de aguas y de economía circular; meta de alcance 3 incumplida</td><td>4</td><td>1</td><td>4</td><td>No cuantificable</td><td>—</td></tr><tr><td>R13</td><td><b>Ciberataque</b></td><td>A plantas o a la red de rutas</td><td>2</td><td>2</td><td>4</td><td>Menor</td><td>—</td></tr><tr><td>R14</td><td><b>Argentina, Venezuela, Rusia</b></td><td>Hiperinflación y exposición residual; Latinoamérica ~6% del EBITDA</td><td>2</td><td>1</td><td>2</td><td>Menor</td><td>—</td></tr>
</table>
<h2>7. Temas ASG relevantes</h2>
<table>
<tr><th>Tema</th><th>Dato</th></tr>
<tr><td><b>Clima e insumos</b></td><td>Alcance 1: 1.24 millones de t (+8.6%); alcance 3: 11.8 millones de t (+3.0%); la meta de reducir 12.5% al 2025 no se cumplió; calificación climática de S&amp;P bajó de 81 a 54 en 2026.</td></tr><tr><td><b>Nutrición y regulación</b></td><td>48% de las ventas con perfil óptimo (3.5 estrellas o más); NOM-051 fase 3 el 1-ene-2028; IEPS de 8% vigente.</td></tr><tr><td><b>Agua</b></td><td>101 plantas en estrés hídrico alto; uso de agua por tonelada -7% frente a 2019 contra meta de -20% a 2030; reforma de la ley de aguas (dic-2025).</td></tr><tr><td><b>Empaques y economía circular</b></td><td>99% de los empaques cumple estándares de reciclaje (meta 100% a 2030); la ley de economía circular (ene-2026) crea responsabilidad extendida del productor, costo aún sin fijar.</td></tr><tr><td><b>Abastecimiento sostenible</b></td><td>85% del aceite de palma libre de deforestación; el reglamento de deforestación de la UE puede bloquear ventas en Europa; más de 520,000 ha con prácticas regenerativas.</td></tr>
</table>
<p>También se miden, sin proponerlos como relevantes: seguridad laboral (TRIR 1.59 en 2025, frente a 2.38 en 2021) y diversidad (30.5% de mujeres en liderazgo).</p>
<p class="src"><b>Etiquetas:</b> las cifras son <i>[sourced]</i> del Reporte Anual 2025 (pp. 100-113) y la nota 26 de los estados financieros, o <i>[calc]</i> del libro de pares v3;
el juicio sobre ciclo de vida, foso, FODA y riesgos y ASG es <i>[assumption]</i> del asistente, pendiente de validación del equipo. Cuotas de México (Sabritas, Gamesa, Bokados) y de Brasil, Colombia y Argentina no tienen fuente local
(<i>[unverified]</i>). Detalle: <code>research/industry.md</code> y <code>research/risks.md</code>, <code>research/esg.md</code>.</p>
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
