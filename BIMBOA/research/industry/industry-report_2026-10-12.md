# Análisis de industria — Grupo Bimbo (BIMBOA.MX)

_Actualizado 2026-10-12. Versión completa que reemplaza al borrador del 2026-10-08 (`industry-report_2026-10-08.md`, se conserva como historial). Cada número lleva etiqueta; fuentes al final._

**Etiquetas:** `[sourced]` dato con fuente · `[guidance]` dicho por el management de una emisora · `[calc]` cálculo propio · `[assumption]` interpretación mía, pendiente de que el equipo la valide · `[unverified]` sin fuente primaria local.

**Claves de fuente:** RA25/RA24/RA23 = reportes anuales a la BMV (`filings/bmv/`); EEFF25 = estados financieros auditados FY25; nQyy ER = comunicados trimestrales; wiki = `wiki/Industry/`, `wiki/Company/`, `wiki/Macro/`; Macro = `reports/Bimbo macro outlook 2026.md`; Tesis = `output/bimbo-tesis-3-pilares.md`.

**Qué cambió contra el 08-oct:** (1) se añade la definición de mercado con tamaño ponderado por la mezcla de Bimbo; (2) FODA propuesto (el equipo lo valida); (3) moat con evidencia numérica y veredicto por región; (4) comparables con defensa de cada uno y una conclusión nueva sobre la valuación relativa; (5) lente LatAm; (6) sección 7 ligada a los tres pilares; (7) estado del IEPS actualizado. Las cifras de pares y múltiplos se heredan del 08-oct y **no se reverificaron hoy** (`[unverified]` hasta repasarlas).

---

## Indicador de pendientes abiertos (2026-10-12)

Leyenda: 🔴 abierto, sin fuente verificable · 🟡 parcial, solo fuentes secundarias o foto sin serie · 🟢 resuelto. Detalle en §8, §9 y §10; tareas en `docs/context/todo.md`.

| # | Pendiente | Estado | Qué falta |
|---|---|---|---|
| 1 | Share de EE.UU. en pan | 🟡 | ~27% BBU (Circana 53 sem. al 3-ene-2026, vía Flowers); sin serie histórica comparable |
| 2 | Share de EE.UU. en bollería, pastelitos y botanas | 🔴 | Solo Circana de pago o IR de Bimbo; en pastelitos solo competidores nombrados (10-K de Smucker) |
| 3 | Ranking de Barcel USA en botanas (#5 vs #6) | 🔴 | Sin fuente verificada |
| 4 | Tamaño del mercado de México en US$ | 🟡 | Rango secundario US$6-11bn (IMARC y otros), sin definición común |
| 5 | Shares de México: Sabritas, Gamesa, Bokados | 🔴 | Sin Nielsen, Euromonitor ni Kantar |
| 6 | Shares numéricos de Brasil, Colombia, Argentina, España y Reino Unido | 🔴 | Solo liderazgo cualitativo; la cifra «37%/18%» de Brasil se refutó |
| 7 | Brasil: Wickbold y Nutrella | 🟡 | Aprobado por Cade con venta de Nutrella; precio y peso de Nutrella sin revelar |
| 8 | Bimbo Colombia / Nutresa | 🟡 | Fecha y 39.99% confirmados; precio sin revelar; control actual de Nutresa (Gilinski) sin primario |
| 9 | Accionistas de control de Gruma, Arca y Lala | 🔴 | Solo «grupo de control ~51%» de Gruma, sin nombres; Lala salió de bolsa en 2022 por prensa |
| 10 | IEPS 2027 y Ley de Ingresos | 🟡 | 8% vigente; texto final del Congreso sin publicar al 10-oct (plazo 20-oct / 31-oct) |
| 11 | Botanas: US$106.9bn (RA25) vs US$183bn (informe integrado) y Top 10 vs Top 5 | 🔴 | Contradicción interna de Bimbo sin explicación |
| 12 | Múltiplos y márgenes de los pares | 🟡 | Refrescados el 16-oct con Capital IQ (§11); faltan Gruma, EV de Yamazaki y Arca, y múltiplos históricos |
| 13 | Split volumen/precio de Bimbo en EE.UU. | 🔴 | No publicado |
| 14 | Ruta de reparto vigente (54,000 vs 53,000) | 🔴 | Menor; sin aclaración |
| 15 | Marca propia en pan de EE.UU. | 🟡 | ~26% $ y ~35% unidades (10-K de Flowers, sin periodo ni proveedor de datos) |

Resumen: 🔴 8 · 🟡 7 · 🟢 0 resueltos por completo.

---

## 1. Definición de mercado, tamaño y ciclo de vida

### Dónde compite Bimbo (producto × geografía × cliente)

| Eje | Dentro | Fuera / marginal |
|---|---|---|
| Producto | Pan de caja, bollería, pastelitos y dulces horneados, galletas, tortilla empacada, bagels y muffins, botanas saladas (Barcel, Takis), pan para QSR | Pan artesanal y de panadería de barrio (es competencia, no mercado servido); tortilla de maíz/masa (Gruma); confitería (Ricolino se vendió, RA22) |
| Geografía | 39 países; FY25: NA 44.6%, México 32.4%, EAA 12.7%, LatAm 10.3% de ventas `[sourced]` 4T25 p.4 | Asia es marginal salvo China (débil, 2T26 p.4) |
| Cliente | Retail moderno (Walmart ~15% de ventas `[sourced]` RA25 p.103), tradicional/tienda de conveniencia (OXXO), QSR (McDonald's, RBI, Yum) | Venta directa al consumidor: inmaterial |

### Tamaño y crecimiento (Global Data vía RA25; valor a precio al público, incluye impuestos e inflación)

| Mercado | Tamaño 2024 | CAGR 2019-24 | CAGR 2024-29E | Tag |
|---|---|---|---|---|
| Panificación global | US$638.9bn | 2.8% | 4.7% | `[sourced]` RA25 p.107-108 |
| Norteamérica | US$139.1bn (21.8%) | 4.1% | 4.3% | `[sourced]` RA25 p.108 |
| Latinoamérica | US$121.8bn (19.1%) | 4.0% | 5.5% | `[sourced]` RA25 p.108 |
| Europa occ. / Europa or. / Asia | 134.6 / 71.5 / 116.0 | 2.7 / 1.7 / 2.0% | 3.4 / 6.6 / 5.0% | `[sourced]` RA25 p.108 |
| México (panificación) | n/d en US$ | n/d | 3.5% | `[sourced]` RA25 p.111 |
| Botanas saladas globales | US$106.9bn | 5.3% | 3.7% | `[sourced]` RA25 p.113 |
| QSR global | US$1,210.7bn | 4.0% | 3.9% | `[sourced]` RA25 p.113 |

- **Crecimiento ponderado por la mezcla de Bimbo** (LTM 2T26: NA 42.6%, México 33.7%, LatAm 10.8%, EAA 12.9%): ≈ **4.2% nominal en valor** 2024-29E `[calc]`. Supone ~4.5% para EAA (promedio simple Europa/Asia, `[assumption]`). Es valor al público: incluye precio e impuestos, **no volumen**. La categoría de EE.UU. está en volumen negativo (sección 2).
- Los tamaños de Global Data se **re-basan cada año** (botanas: US$194.4bn en RA24 → US$106.9bn en RA25). No encadenar series `[sourced]` wiki/bakery-market-structure. Hay un dato de tercero de pan en México (~US$11.4bn en 2025, CAGR 5.4% a 2035; consultoras web) que no concilia con la definición de Global Data; **no se usa** `[unverified]`.
- **Ciclo de vida: maduro** `[assumption]`. Valor crece ~3-5% casi todo por precio y mezcla; volumen plano o negativo en mercados desarrollados; solo LatAm, Europa del Este y Asia aportan volumen real. Defensivo en volumen, cíclico en mezcla (trading-down hacia marca propia y artesanal, RA25 p.109).

### Coach moment 1 — definición de mercado (decide el equipo)

- **Mi recomendación:** definir el mercado servido como **«panificación empacada de marca con entrega directa a tienda (DSD)», por país**, y no como «panificación global». En ese mercado Bimbo es líder en México (18.2% pan empacado, 28.2% pastelitos) y tiene 7.4% en EE.UU.
- **Por qué:** el 3.7% global es una cifra de marketing; el cliente elige entre Bimbo, marca propia y panadería local en el anaquel de su tienda, no entre 639 mil millones de dólares.
- **El mejor argumento en contra:** el dato por país mezcla definiciones de Global Data y Nielsen y cambió entre RA24 y RA25 (EE.UU. 8.1%→7.4%, Canadá 10.6%→13.3%, México pastelitos 23.4%→28.2%), así que el «mercado estrecho» también tiene una base débil.
- **Pregunta para el equipo:** ¿en qué mercado elige el consumidor y quién fija el precio: en EE.UU., donde el retailer manda y la marca propia lleva 23.8% de las unidades del súper `[sourced]` Macro, o en México, donde el tendero es atomizado? La respuesta cambia cómo se modela el margen de cada región.

---

## 2. Cinco fuerzas

| Fuerza | Intensidad | Evidencia | Tag |
|---|---|---|---|
| **Rivalidad** | **Alta en EE.UU.; media en México** | EE.UU.: Flowers 2T26 volumen −5.8%, precio/mezcla +1.8%; marca propia de Flowers −7.6%; su guía FY26 se recortó de nuevo (ventas US$5.07-5.14bn) `[sourced]` FLO 10-Q ex99.1; MarketBeat 20-ago-2026. Bimbo dice haber ganado share en todas las categorías en 2T26, primera vez desde 2020 `[guidance]` 2T26 ER p.3: si ambas son ciertas, es juego de suma cero en una categoría que se encoge. Riesgo declarado de presión de precios por exceso de capacidad (RA25 p.24). México: líder con 4-6× el siguiente empacado; competencia artesanal fragmentada | `[sourced]` / `[guidance]` |
| **Entrada de nuevos jugadores** | **Baja en escala, alta en lo local** | Hornear es barato (barreras históricamente bajas, RA25 p.109); la barrera es entregar fresco con vida de anaquel de 14 días (RA25 p.100, p.110). El empaque con más vida útil la erosiona poco a poco. Entrada potencial más real: marca propia y hard-discount (Lidl, Aldi) y delivery de supermercado | `[sourced]` |
| **Poder de proveedores** | **Medio** | Materias primas ~30% de ventas y ~64% del costo de ventas (EEFF25 p.82). Trigo, azúcar y aceites son commodities en USD: el proveedor no tiene poder propio, pero el precio es exógeno y vuelve a subir. Trigo CBOT dic-26 US$6.865/bu (+35% a/a), curva en contango; azúcar +24% a/a `[sourced]` Macro. Cobertura con futuros y swaps | `[sourced]` |
| **Poder de compradores** | **Alto en mercados desarrollados; bajo en emergentes** | Walmart ~15%, ningún otro >10% (RA25 p.103). Canal moderno 77.7% en NA vs ~59-60% tradicional/especialista en LatAm y MENA (RA25 p.110). Consolidación de retailers y formatos alternativos presionan precio y fondos de promoción (RA25 p.31-32) | `[sourced]` |
| **Sustitutos** | **Medio-alto** | Artesanal 44.3% y marca propia 9.6% del mercado global (RA25 p.107). Tortilla de maíz en México. GLP-1: ~22% de hogares de EE.UU. con un usuario (Numerator) `[sourced]` Macro; EY-Parthenon estima hasta US$12bn de ventas de botanas perdidas en una década `[unverified]`; Smucker no ve impacto material en Hostess `[guidance]` | `[sourced]` / `[unverified]` |

**Lectura para márgenes de largo plazo** `[assumption]`: son **dos industrias en una**.
- **México/LatAm**: comprador atomizado, red DSD propia, líder con distancia amplia. Estructura que sostiene márgenes EBITDA de ~20% (Mexico LTM 2T26: 33,119/158,321 = 20.9% `[calc]`).
- **EE.UU./Canadá/Europa**: comprador concentrado, marca propia, categoría que se encoge en volumen. La escala de Bimbo protege volumen, pero **no se ha traducido en margen superior al de pares** (NA 9.6% LTM vs Flowers 9.3% LTM `[sourced]` CIQ 2026-10-16). El techo razonable del margen de NA es el del panificador puro de EE.UU. (~10-12%) salvo que haya evidencia de una ventaja de costo que hoy no existe.

---

## 3. Paisaje competitivo y participación

### Global (Global Data 2024, RA25 p.107-109) `[sourced]`
- Bimbo 3.7% en todas las categorías (4.1% en pan y pastelería), 1.2× el segundo. Mondelez 3.0%, Gruma 1.1%, Kellogg's 0.6%; en core bakery Uno Bakery Corp. 0.7% y Flowers 0.6%. Top-10 = 11.7%, ninguno >4.0%. Marca propia 9.6%, artesanal 44.3%.

### Por país

| Región / categoría | Bimbo | Tendencia (pp, base cambió entre años) | Competidores | Cotiza (ticker) | Nota |
|---|---|---|---|---|---|
| México, pan empacado | 18.2% | 17.4% (RA24) → 18.2% | Artesanal, súper con panadería; regionales (Dulcipan, El Panqué, Pan Filler) | No cotizan | Líder con amplia distancia `[sourced]` RA25 p.111 |
| México, pastelitos | 28.2% | 23.4% → 28.2% | No nombrados en RA25 | PEP | `[sourced]` RA25 p.111 |
| México, botanas saladas | 18.4% (Nielsen) | Base cambia | No nombrados en RA25 (Sabritas-PepsiCo y Bokados-Arca por conocimiento general `[unverified]`) | PEP, AC | Barcel #2 `[sourced]` RA25 p.84, p.113 |
| EE.UU., pan/bollería | 7.4% (Global Data, todo el mercado de panificación); **~27% del pan fresco, bollos y rolls (Circana, 53 sem. al 3-ene-2026, ver §10)** | 8.1% (RA24) → 7.4%; **Bimbo dice que sube desde 2Q25** `[guidance]` | Flowers (Nature's Own, Dave's), marca propia, McKee, Hostess (SJM), Mondelez | FLO, SJM, MDLZ | Sin dato Circana en puntos; share cualitativo `[unverified]` |
| EE.UU., botanas | #6 por ventas (Circana) | n/d | Frito-Lay y otros (no nombrados en RA25) | PEP | `[sourced]` RA25 p.83 |
| Canadá | 13.3% | 10.6% → 13.3% | FGF Brands, marca propia de los retailers | — | Caso de colusión de precios, multa US$38M (2023) `[sourced]` RA25 p.41 |
| LatAm | Líder de pan empacado en cada país; botanas 7.3% (#3) | 4.5% → 7.3% | Artesanal; Nutresa, jugadores locales | NUTRESA, otros | Sin cifras numéricas en Brasil, Colombia, Argentina `[unverified]` |
| España/Portugal, Reino Unido, Rumania | Líder de marca (Nielsen/Circana) | n/d | Warburtons, Kings Mill, marca propia | — | Cualitativo |
| China | 3.0% | n/d | — | — | Marca débil 2T26 |

- **Marca propia:** 23.8% de unidades es **todo el súper** (Circana, 1S26), no pan. En **pan fresco empacado** pesa ~26% de dólares y ~35% de unidades `[sourced]` Flowers 10-K FY25 (sin periodo ni proveedor de datos). Ver §8.
- **Eventos de consolidación del sector 2025-26** `[sourced]` informe 08-oct: Mars compró Kellanova (cierre 11-dic-2025, ~US$36bn); Ferrero compró WK Kellogg (US$3.1bn); Flowers compró Simple Mills, recortó guía y dividendo; Smucker vendió marcas de valor de Hostess; Campbell's recortó su dividendo. La lectura: el panificador de EE.UU. está en defensa mientras los conglomerados de snacks se consolidan.

---

## 4. Posicionamiento y moat

### Qué protege a Bimbo, con evidencia

| Fuente de ventaja | Evidencia | ¿Aparece en números? | Veredicto |
|---|---|---|---|
| **Red de distribución DSD** | 54,000+ rutas, 1,700+ centros de venta, 249 plantas en 39 países; reposición gratis de producto no vendido (RA25 p.14, p.100) | **México sí**: margen EBITDA LTM 20.9%, 19.0% en FY21 → 20.4% en FY25 `[calc]`/`[sourced]`; ventas nominales crecieron los 19 trimestres de 4T21 a 2T26 `[sourced]` Tesis. **EE.UU. no**: NA 9.0% FY25 vs 12.2% FY21; Flowers 9.3% LTM con ¼ del tamaño | **Ancho en México/LatAm; angosto en NA** |
| **Marca** | 9,000+ SKUs; 12.6% de ventas FY25 de innovación (RA25 p.80, p.87); marcas #1 en pan y pastelitos de México | **México sí** (28.2% pastelitos, +4.8 pp en un año según Global Data) | Fuerte en México; medio en EE.UU., donde compite contra marca propia y Nature's Own/Dave's |
| **Escala de compras** | Bimbo cita escala en compras de materias primas (RA25 p.109), sin cifra | **No visible**: el costo de materias primas es commodity y todos los panificadores lo cubren; Flowers tiene un margen bruto comparable | Neutra |
| **QSR global** | Proveedor principal en 40 países (RA25 p.87, p.112); contratos multianuales | Parcial: EAA creció +8.4% ex-FX en 2T26, margen EAA 11.4% LTM `[calc]` | Medio; cliente concentrado |
| Cambio de proveedor / red / regulación | No aplican de forma material | — | — |

### Durabilidad y qué la erosiona
- **Erosión lenta de la barrera de frescura**: empaques con más vida útil amplían el radio de entrega de los jugadores sin DSD (RA25 p.110).
- **Marca propia y trading-down** en EE.UU.; **retailer** con poder de precio.
- **Costo laboral de la ruta en México**: jornada de 48→46 horas en 2027 y 40 horas en 2030 sube el costo por hora ~4% en 2027 `[calc]` Macro; la DSD propia de Bimbo es intensiva en mano de obra. Es la ventaja de México, y también su costo fijo.
- **Regulación de salud** (etiquetado NOM-051, reglas escolares, IEPS): afecta a la mezcla de pastelitos y botanas, que son la parte de más margen.

### Coach moment 2 — moat (decide el equipo)
- **Mi recomendación:** declarar un moat **regional**: ancho en México/LatAm, **sin evidencia hoy en EE.UU.**
- **Por qué:** el margen de México (20.9% LTM) está por encima de comparables locales; el margen de NA (9.6%) apenas supera al de Flowers (9.3% LTM, definiciones de EBITDA distintas) pese a ser 4× más grande.
- **El mejor argumento en contra:** Mexico mezcla Barcel y pastelitos (categorías más rentables que pan de caja), así que el margen alto puede ser mezcla de producto y no distribución; y Arca (19.4% LTM) logra el mismo margen con distribución propia sin ser panificador.
- **Pregunta para el equipo:** ¿qué número del P&L de EE.UU. demostraría que la escala de Bimbo es una ventaja y no solo tamaño? (margen sobre Flowers, estabilidad de share con datos Circana, precio/mezcla sostenido con volumen estable).

---

## 5. FODA (propuesta de la IA — el equipo valida)

| Fortalezas | Debilidades |
|---|---|
| Red DSD con densidad en México: 20.4% de margen EBITDA FY25, líder con 18.2%/28.2% de share | NA con margen bajo (9.0% FY25; 5.9% en 4T24) y 8 trimestres de ventas ex-FX negativas (1T24-4T25) |
| Portafolio diversificado por región (56% emergentes) y canal; ningún cliente >15% | Concentración de EBITDA en México (~55%): un golpe regulatorio o fiscal pega directo |
| Balance: deuda neta/EBITDA 2.5x (2T26), costo 6.5%; capex a la baja (3.4% de ventas en 1S26) | Recuperación de NA es de margen, no de volumen; sin cuantificar |
| Escala en 39 países e infraestructura QSR | Mezcla de monedas: 42% de la deuda en USD con ingresos en MXN |

| Oportunidades | Amenazas |
|---|---|
| Ganancia de share en EE.UU. mientras Flowers y Campbell's recortan | Marca propia (23.8% de unidades) y trading-down con confianza del consumidor en 81.9 |
| Crecimiento inorgánico y orgánico en LatAm (+14.1% ex-FX 2T26) y EAA (+8.4%) | Insumos 2027: trigo, azúcar y aceites suben; margen bruto −150 a −240 pb por una canasta +5-8% `[calc]` Tesis |
| Premiumización: proteína, sourdough, clean label (colorantes artificiales fuera a fines de 2026) | GLP-1 y regulación de salud (NOM-051 fase 3 en 2028, etiquetado, escuelas) |
| Peso menos apreciado: la conversión pasa de −6.7 pp a +1 a +3 pp en 2027 `[calc]` Macro | Impuestos: IEPS de 8% (alimentos ≥275 kcal/100 g); propuesta de 20% sin aprobar; jornada laboral de 40 horas |
| Menor capex libera FCF para recompras o desapalancamiento | Revisiones anuales del T-MEC; arancel 10% Sección 301 desde 24-jul-2026 |

**Estado IEPS (actualizado 2026-10-12)** `[sourced]` búsqueda web: la propuesta de elevar de 8% a 20% se discutió en septiembre (Expansión, 1-sep); sin embargo, reportes posteriores indican que **Morena descartó "por ahora" el incremento al IEPS de cerveza y alimentos con sodio** y que el paquete económico 2027 **no contempla nuevos impuestos** (La Razón, 1-sep; UnoTV). Tratarlo como riesgo de cola, no escenario base. Falta confirmar el texto final de la Ley de Ingresos (votación a fines de octubre) `[unverified]`.

---

## 6. Universo de comparables

EV/EBITDA LTM actualizado el 2026-10-16 con Capital IQ (detalle y discrepancias en `capiq-leverage-comps_2026-10-16.md`); reemplaza las cifras del 08-oct. Flowers, Aryzta, Smucker, Campbell's, Mondelez y PepsiCo son EV/EBITDA recalculados con EV y EBITDA de la misma tabla; Yamazaki y Arca vienen de la herramienta de múltiplos (sin EV); Gruma sigue en el valor del 08-oct. Cierres fiscales distintos: calendarizar antes de usar en Val_Comps.

| Par | Ticker | Por qué comparable (una frase) | Marco | EV/EBITDA | Salvedad |
|---|---|---|---|---|---|
| **Flowers Foods** | FLO | Panificador puro de EE.UU. con DSD e independientes: el mejor espejo del margen de NA | US GAAP | 6.68x `[calc]` | Sin México ni Europa; en deterioro (recorte de guía y dividendo) |
| **Gruma** | GRUMAB | Emisora BMV, IFRS, México + EE.UU., competidor directo en tortilla y harinas | IFRS | 5.7x `[unverified]` | Es masa de maíz y tortilla, no pan; margen bruto 39% vs 52% de Bimbo |
| **Yamazaki** | 2212.T | Mayor panificador puro fuera de América; ancla del múltiplo del pure-play | J-GAAP | 6.58x `[sourced]` | Mercado, moneda y contabilidad distintos; solo ancla |
| **Aryzta** | ARYN | Panificación europea con canal QSR/congelado; traslapa con EAA y QSR de Bimbo | IFRS | 8.33x `[calc]` | Congelado B2B, mucho más pequeño |
| J.M. Smucker | SJM | Hostess compite con Marinela/Bimbo en pastelitos en EE.UU. | US GAAP | 9.06x `[calc]` | Bimbo es un % pequeño del negocio; café domina |
| Campbell's | CPB | Pepperidge Farm (pan fresco) y snacks en EE.UU. | US GAAP | 8.20x `[calc]` | Mayormente sopas y snacks |
| Mondelez | MDLZ | Galletas en México y EE.UU.; #2 global en panificación 3.0% | US GAAP | 16.77x `[calc]` | Prima de calidad, chocolate/galletas; no es par operativo |
| Arca Continental | AC | Consumo mexicano con ruta propia; Bokados compite con Barcel | IFRS | 8.47x `[sourced]` | Bebidas, no panificación |
| PepsiCo | PEP | Sabritas vs Barcel; Gamesa | US GAAP | 11.48x `[calc]` | Mega-cap global |

**Excluidos:** Kellanova (privatizada por Mars), Hostess (dentro de SJM), Grupo Lala (no cotiza), Grupo Nutresa (iliquida tras compra de Gilinski), Herdez (distorsión por desconsolidación de McCormick México), General Mills (traslape parcial), McKee y Uno Bakery (privadas).

**Lectura de valuación relativa (nueva)** `[calc]`: mediana EV/EBITDA del **core de panificación** (FLO, GRUMAB, 2212.T, ARYN) = **6.63x** (6.68x sin Gruma), contra Bimbo 6.29x (base CIQ) o 6.68x (base de la empresa). Es decir: **Bimbo cotiza en línea con los panificadores puros, no con descuento.** El descuento solo existe frente a (i) su propio promedio de 7.7-7.8x a 5-10 años y (ii) los consumidores mexicanos y globales (AC 8.1x, PEP 10.8x, MDLZ 16.1x). Esto matiza el Pilar 3.

### Coach moment 3 — comparables (decide el equipo)
- **Mi recomendación:** usar **core (4) para la mediana** y el resto como rango secundario.
- **El mejor argumento en contra:** el core son panificadores de bajo crecimiento y en estrés (FLO) o de modelo distinto (Gruma, Aryzta); nadie en el core tiene el perfil de 55% del EBITDA en un mercado emergente. Un juez preguntará por qué Arca o PepsiCo no están en la mediana.
- **Pregunta para el equipo:** ¿defienden cada par en una frase, y qué múltiplo esperarían de un panificador **con** el crecimiento y el margen de México? ¿Se justifica una suma por partes (México/LatAm con comps de consumo mexicano, NA con comps de panificación de EE.UU.)?

---

## 7. Implicaciones para el pronóstico y la tesis

### Supuestos de industria que el modelo debe respetar

| Supuesto | Valor propuesto | Fuente / tag |
|---|---|---|
| Mercado de panificación México (valor) | ~3.5% CAGR 2024-29E; ventas de Bimbo MX ≈ ese ritmo más precio y mezcla | `[sourced]` RA25 p.111; hist. +4.0-4.8% 2024-26 |
| Categoría de pan EE.UU. (volumen) | −2% a −4% en 2026-27 (base); ~0% al alza; −5% a −8% a la baja | `[assumption]` proxy FLO −5.8%; Macro |
| Precio/mezcla EE.UU. | +1% a +2% | `[assumption]` FLO +1.8% |
| Share Bimbo EE.UU. | Estable o +0.2 pp/año; sin dato Circana | `[assumption]`; `[guidance]` 2T26 |
| Share Bimbo México | Estable en 18.2%/28.2%; no extrapolar la alza de pastelitos | `[sourced]` RA25 p.111 |
| LatAm / EAA mercado (valor) | 5.5% / 3.4-6.6% | `[sourced]` RA25 p.108; incluye inflación |
| Margen EBITDA NA | 9.6% LTM; techo de referencia 10-12% | `[calc]`; par FLO 9.3% LTM |
| Margen EBITDA México | ~20.5-21% con presión de costo laboral 2027 | `[calc]` |
| IEPS | 8% base; 20% solo escenario bajista | `[sourced]` ver §5 |
| Insumos 2027 | Trigo US$7.0-7.2/bu base; margen bruto bajo presión 1S27 | `[sourced]` Macro |

### Vínculo con los pilares (`output/bimbo-tesis-3-pilares.md`)

| Pilar | Efecto de la industria | Razón |
|---|---|---|
| **1. El margen de NA se recupera por productividad** | **Debilita en parte** | La estructura no respalda un margen >12% en EE.UU.: el par más cercano gana 9.3% y la categoría pierde volumen. Sirve si el objetivo es llegar a ~10-11%; el escenario de 12.2% (FY21) necesita una razón estructural que la industria no da hoy. Además, la ganancia de share que Bimbo reporta es suma cero en una categoría que cae y es cualitativa. Apoya: Flowers y Campbell's en defensa dejan espacio de share |
| **2. Capex a la baja libera FCF y reduce deuda** | **Neutral / apoya** | Capacidad en exceso en la categoría respalda no invertir; el riesgo es lo opuesto: una guerra de precios por capacidad ociosa |
| **3. Valuación bajo su promedio, con México de respaldo** | **Apoya México; matiza la valuación** | Estructura de México (comprador atomizado, líder) respalda el piso de márgenes; pero frente a los panificadores puros Bimbo ya cotiza en línea (6.3x vs 6.45x). El descuento es contra su historia, no contra el sector. Riesgos propios de México: IEPS, NOM-051, jornada de 40 horas |

**Siguiente paso recomendado:** cerrar el hueco más grande: un dato de **share de EE.UU. en puntos (Circana) y split volumen/precio de Bimbo**, porque de eso depende el Pilar 1 y hoy solo hay declaraciones del management.

---

## 8. Complemento de Deep Research (2026-10-12)

Corrida verificada por votación adversarial (103 agentes). Solo se listan hallazgos que sobrevivieron; los demás se excluyen. Fuentes mayormente secundarias, salvo donde se indica.

| # | Hallazgo | Confianza | ¿Contradice el reporte? | Fuente |
|---|---|---|---|---|
| 1 | **Marca propia en pan fresco empacado EE.UU.: ~26% de dólares y ~35% de unidades**; su share subió desde FY22 por trade-down; categoría con caídas de volumen y FY25 débil (sobre todo pan de caja tradicional) | Alta (tendencia); media (26%/35%, sin periodo) | **Corrige el uso de 23.8%**: esa cifra es todo el súper (Circana 1S26, 21.2% en dólares), no pan. Para el pilar 1 usar 35% de unidades | [Flowers 10-K FY25](https://www.sec.gov/Archives/edgar/data/1128928/000119312526071441/flo-20260103.htm) (primaria, parte interesada); [Bakery&Snacks, 28-jul-2026](https://www.bakeryandsnacks.com/Article/2026/07/28/why-grupo-bimbo-is-not-afraid-of-private-label/) |
| 2 | Circana 52 sem. a 19-abr-2026: en pan de caja Bimbo −2.8% vs marca propia −0.4%; en pan crujiente/«meal bread» marca propia US$418M (+5.5%), ~62% de US$676M, Bimbo US$68.6M (−0.8%); «otros panes de centro de tienda» Bimbo −8.6% | Media | Apoya que la marca propia aguanta mejor que Bimbo: **debilita la lectura de «ganancia de share»** en pan | Bakery&Snacks; [Snack & Bakery](https://www.snackandbakery.com/articles/115896-state-of-the-industry-2026-bread-shifts-towards-healthier-alternatives) |
| 3 | CEO de Bimbo, 23-jul-2026: ganó share en todas las categorías de EE.UU., primera vez desde 2020; **sin puntos**, medido contra marcas, no contra la categoría total con marca propia | Media | Ni confirma ni refuta el 7.4% de Global Data | Bakery&Snacks |
| 4 | **GLP-1:** el gasto en súper cae 5.3% en seis meses tras iniciar (>8% en hogares de mayor ingreso); botanas saladas ~−10%, con caídas grandes en dulces, panificados y galletas; sin cifra específica de pan. Muestra de ~2,600 usuarios, observacional, el efecto se atenúa | Media | Cuantifica el riesgo que el reporte solo citaba cualitativamente | [Cornell/JMR vía EurekAlert, dic-2025](https://www.eurekalert.org/news-releases/1110869) |
| 5 | **IEPS México:** tasa de 8% (≥275 kcal/100 g) sin cambio; 20% es propuesta de ONG (Poder del Consumidor, Fundar), no de Hacienda. Los Criterios 2027 (8-sep) no muestran nueva tasa general; IEPS no petrolero 2027 MXN 289.7bn (+1.2% real). **Riesgo no cerrado**: el Congreso puede modificar el paquete (~noviembre) | Media | Confirma tratar 20% como cola; matiza §5 | [Expansión 1-sep](https://expansion.mx/economia/2026/09/01/ieps-impuesto-comida-chatarra-2027-8-20); [UnoTV 8-sep](https://www.unotv.com/nacional/paquete-economico-2027-crecimiento-ieps-y-los-cambios-fiscales-clave/) |
| 6 | **Gruma:** un «grupo accionista primario» tiene ~51% (otras fuentes 52-55%); no nombra tenedores | Media | Llena parcialmente el lente LatAm | [FAQ de Gruma](https://www.gruma.com/en/investors/investors-gruma/faq.aspx) |
| 7 | **Lala:** los controladores anunciaron en 2021 su salida de la BMV; prensa posterior reporta que se completó en 2022 (~99.85%) | Media | Confirma «no cotiza» | [Comunicado Lala, 21-may-2021](https://www.lala.com.mx/storage/app/media/Press%20Events/Press%20Releases/74.%2021.05.21-LALA-Tender_vF.pdf) |

**Excluido por refutación:** caída de penetración y de share de Bimbo en EE.UU. según El Cronista; caída total del pan de caja en dólares (−2.4%); estimaciones de ~MXN 12bn de recaudación por IEPS al sodio.

**Sigue abierto (no se resolvió):**
- Share de EE.UU. en puntos por categoría (Circana/NielsenIQ): 7.4% y 18.2% de Global Data siguen sin verificar.
- Tamaño y shares de México (pan, pastelitos, botanas; Bimbo, Sabritas, Gamesa, Bokados).
- Shares en Brasil, Colombia, Argentina, España y Reino Unido.
- NOM-051 y reglas escolares (ya cubiertas por RA25, sin actualización).
- Accionistas de control de Arca y Nutresa; nombres de los tenedores de Gruma y Lala.
- Texto final de la Ley de Ingresos 2027 sobre IEPS.

**Efecto en la tesis:** el punto 1 y el 2 refuerzan la advertencia sobre el Pilar 1: en pan la marca propia es ~35% de las unidades y sostiene mejor sus ventas que Bimbo, así que la «ganancia de share» probablemente viene de bollería, botanas y desayuno, no del pan de caja. Pedir a Bimbo (IR) el split por categoría.

---

## 9. Resolución de pendientes con los archivos de Bimbo (2026-10-12)

Revisé el texto completo de RA22, RA23, RA24, RA25, EEFF25, el informe integrado 2025 (*Celebramos*), los comunicados 4T25, 1T26 y 2T26 y los CSV de Capital IQ. Resultado: **se resolvieron 4 de 8 pendientes en parte; los datos numéricos de share que faltan no existen en los archivos de Bimbo.**

| Pendiente | Qué dicen los archivos | Estado |
|---|---|---|
| **Share de EE.UU. en puntos (Circana)** | Bimbo solo publica Global Data: 17.6% (RA23, Euromonitor 2022) → 8.1% (RA24) → **7.4%** (RA25). Circana aparece solo como ranking: BBU «principal proveedor de productos horneados» (2024 y 2025), presencia en 83% de hogares (RA23/RA24) y 92% (RA25), Barcel USA #5 (RA23) → #6 (RA24, RA25) en botanas. Los comunicados 2024-2T26 hablan de «ganancias de share» sin un solo punto | **No resoluble con estos archivos.** Hecho nuevo: la caída de #5 a #6 de Barcel USA en botanas (Circana) contradice parcialmente el relato de ganancia de share en botanas saladas |
| **Tamaño y shares de México** | RA25 da solo CAGR 3.5% (2024-29E) y los shares 18.2% (pan empacado), 28.2% (pasteles y pan dulce), Barcel #2 en botanas con 18.4% (Nielsen). **Ningún reporte da US$ del mercado mexicano.** Los CAGR cambian por re-base: 6.6% (RA23, Euromonitor 2022-27) → 2.9% (RA24) → 3.5% (RA25). Competidores nombrados en RA22: **Gamesa (PepsiCo), Nabisco (Mondelez), Cuétara y Dondé** en galletas, donde Bimbo es #2; en pan empacado, regionales **Dulcipán, El Panqué, Pan Filler** (RA23); en tortilla, **Gruma** (Mission, Maseca). Que Barcel sea #2 implica que el #1 es otro; RA25 no lo nombra (Sabritas-PepsiCo es inferencia mía `[assumption]`) | **Parcial:** competidores confirmados; tamaño no |
| **Prueba de razonabilidad del tamaño** `[calc]` | Ventas netas FY25 de Bimbo MXN 427.0bn ≈ US$22.1bn (supone USD/MXN 19.3 `[assumption]`) ÷ US$638.9bn = **3.5%**, cerca del 3.7% declarado: el share global de Global Data es consistente con la escala de Bimbo. Con la misma lógica, ventas de México (MXN 154.8bn ≈ US$8.0bn) serían ~70% del «mercado de pan de México de US$11.4bn» de las consultoras web: **esa cifra no concilia con el 18.2% de Bimbo y se descarta** (las ventas de México incluyen Barcel) | Resuelto (descarte) |
| **Brasil, Colombia, Argentina, España, Reino Unido** | **Ningún reporte (RA22-RA25) da share numérico.** Solo liderazgo cualitativo: líder de pan empacado en cada país de LatAm (Pullman, Plusvita, Nutrella, Fargo, Lactal); España/Portugal: marca líder según Nielsen; Reino Unido: líder en bagels con New York Bakery (competidores Warburtons, Kings Mill, marca privada) y en viennoiserie. En LatAm, botanas 7.3% (#3). Hecho nuevo: **Wickbold (Brasil, 6-oct-2025)** (pan, pan dulce y botanas) se adquirió al 100%; el PPA preliminar de EEFF25 es agregado de las adquisiciones 2025 (crédito mercantil MXN 4,299m, marcas 1,390, relaciones con clientes 2,685) y **no se puede separar por empresa** `[unverified]` | **No resoluble;** Brasil sube de importancia por la adquisición |
| **Marca propia / mercado global** | Marca propia en Europa + artesanal = **52.6%** del mercado regional (RA25 p.111). Bimbo vende marca propia en Canadá y QSR, y salió estratégicamente de parte de ella en EE.UU. y Canadá (RA25 p.133-135), lo que explica en parte los 8 trimestres negativos de NA | Resuelto (cualitativo) |
| **Tamaño de botanas: contradicción interna** | **RA25: US$106.9bn** de botanas saladas, CAGR 5.3% (2019-24) y 3.7% (2024-29E), Bimbo «entre los diez primeros». **Informe integrado 2025 (p.16): US$183bn**, **1.4%** de share, CAGR 4.7% y **3.8%**, «**Top 5**», con otra definición (incluye papas, palomitas y botanas procesadas). Dos tamaños y dos rankings del mismo año y misma fuente (Global Data 2024) | **Hallazgo nuevo:** no usar ninguna cifra sin citar el documento y la definición |
| **Global Data vs Euromonitor (peers)** | RA23 (Euromonitor 2022): Bimbo 3.4%, **Yamazaki 1.4%, Flowers 0.7%** como los tres grandes globales. En RA25 (Global Data 2024) aparecen Mondelez 3.0%, Gruma 1.1% y Kellogg's 0.6% en «todas las categorías». **Bimbo mismo nombra a Yamazaki y Flowers como pares globales** | Respalda incluir FLO y 2212.T en el core de §6 |
| **IEPS, NOM-051, escuelas** | RA25 solo cita el IEPS como factor de precio (p.130) y como ley aplicable, sin tasa ni exposición cuantificada; NOM-051, reglas escolares y publicidad ya están en §5 y en la wiki. Los comunicados 4T25-2T26 no mencionan IEPS, GLP-1 ni marca propia | **Sin información adicional**; se mantiene lo de §8 |
| **Accionistas de control de pares** | Los archivos de Bimbo y de CIQ no contienen la estructura de Gruma, Arca, Lala ni Nutresa. Lo que sí hay: **Nutresa fue socio de Bimbo en Colombia con 40%; Bimbo lo compró el 15-may-2025** y quedó con 100% (RA25 p.77; EEFF25 nota 1). CIQ aún registra a Nutresa como **proveedor** de Bimbo Colombia (US$23.0m, desde 2016) y cliente (US$1.7m) | **No resoluble;** hecho nuevo: Nutresa es proveedor y exsocio, no solo competidor. Flowers aparece en CIQ como «licensee» de Bimbo (2016, 10-K de Flowers): verificar el alcance |
| **Ruta de reparto: cifra vigente** | 54,000+ (RA25 p.14) vs 53,000+ (p.80): sin aclaración en los archivos | Abierto (menor) |

**Lectura para la tesis:**
1. Los shares de Bimbo son **todos de terceros, re-basados cada año y sin series**. Nada en los archivos permite probar una ganancia de share en EE.UU. en puntos: la prueba estará fuera (Circana de Bimbo, IR o sell-side).
2. La caída de Barcel USA de #5 a #6 en botanas (Circana) y el pan de caja con marca propia más resistente que Bimbo (§8) son la evidencia concreta más fuerte contra el relato de «ganancia de share en todas las categorías».
3. Wickbold y la compra de Nutresa en Colombia muestran que **la expansión de LatAm es inorgánica**: el crecimiento de +14% ex-FX de LatAm incluye adquisiciones, así que no es un dato de industria.

---

## 10. Segundo Deep Research sobre los pendientes (2026-10-12)

Corrida verificada por votación adversarial. Solo se listan hallazgos que sobrevivieron; las fuentes de México y LatAm son secundarias.

| Pendiente | Hallazgo | Confianza | ¿Contradice el reporte? |
|---|---|---|---|
| **Share de EE.UU. en puntos** | **Pan fresco empacado, bollos y rolls en EE.UU. (Circana, 53 semanas al 3-ene-2026): BBU ~27%, marca propia 26%, otras marcas 26%, Flowers 16%, Pepperidge Farm 5%.** BBU es el mayor dueño de marca; el 27% contra 26% está dentro del redondeo y Circana advierte no usarlo para comparar en el tiempo. [Ficha de inversionistas de Flowers, ago-2026](https://investors.flowersfoods.com/~/media/Files/F/Flowers-Foods-V3/documents/events/q2-2026/investor-fact-sheet-august-26.pdf) (primaria, pero de un competidor) | Alta (3-0) | **Matiza el 7.4% de Global Data:** son categorías y bases distintas (7.4% es todo el mercado de panificación; ~27% es solo pan y bollos). No se contradicen, pero el 7.4% no sirve para medir la posición en pan |
| **Tamaño EE.UU. del pan** | Flowers estima ~US$48bn retail + US$7bn foodservice de pan fresco, bollos y rolls; el mercado fresco y congelado de panadería es ~US$55bn al retail; el pan es la 3.ª categoría de abarrotes por dólares y 98% de los hogares lo compra ([10-K Flowers FY25](https://www.sec.gov/Archives/edgar/data/1128928/000119312526071441/flo-20260103.htm)) | Alta | Nuevo: tamaño propio del pan en EE.UU. |
| **Pastelitos EE.UU.** | El 10-K de Smucker (periodo al 30-abr-2026) nombra a Bimbo (vía Entenmann's), Little Debbie (McKee), Bon Appetit y marca propia como competidores de Hostess; marca propia ~14.0 de share promedio en 52 semanas al 19-abr-2026 ([10-K SJM](https://www.sec.gov/Archives/edgar/data/0000091419/000009141926000050/sjm-20260430.htm)) | Media (lectura parcial del documento) | Sin share puntual de Bimbo ni de Hostess |
| **México, tamaño** | Solo estimaciones secundarias y dispersas: panadería US$8.2bn en 2025 (IMARC, CAGR 2.95%), galletas US$2.1bn (IMARC) o US$2.9bn (informesdeexpertos); otras fuentes dan US$6.1bn a US$11.4bn en pan. **Citar como rango de US$6-11bn, no como tamaño** | Baja | Confirma el descarte de US$11.4bn como cifra única; sin shares por empresa (Sabritas, Gamesa, Bokados) |
| **Brasil** | **Cade aprobó el 17-sep-2025 (unánime) la compra de Wickbold** (6 de 10 empresas; marcas Wickbold y Seven Boys; ~2.5-2.7 mil empleados; precio no revelado). Condiciones: **Bimbo vende Nutrella y Wickbold desinvierte Tá Pronto** (~4% de share combinado, estimación del CEO de Bimbo Brasil); 3 años de restricción en tortillas (solo Rap10) y sin exclusividad en bisnaguinhas en Centro-Oeste ([Bloomberg Línea](https://www.bloomberglinea.com.br/negocios/cade-aprova-compra-da-wickbold-pela-bimbo-mas-empresa-tera-que-abrir-mao-da-nutrella/), [Brazil Journal](https://braziljournal.com/8kuh)) | Alta | **Corrige §9:** Nutrella, que RA25 lista como marca líder de LatAm, **se vende** por exigencia antitrust. Las cifras de «37% de Bimbo y 18% de Panco» se **refutaron (0-3)**: no usar |
| **Colombia / Nutresa** | Nutresa firmó el 14-may-2025 la venta de su 39.99% de Bimbo Colombia a vehículos de Bimbo (BB Global Investing Holding e inversionista ibérico); precio no revelado ([La República](https://www.larepublica.co/empresas/grupo-nutresa-sigue-saliendo-de-activos-y-decidio-vender-su-participacion-en-bimbo-4134033)). Nutresa pasó a control de JGDB/Nugil (Gilinski): el MOU de 2023 buscaba ≥87% y, según un verificador citando Wikipedia, llegó a ~99.4% en 2024 `[unverified]` | Alta (venta); media (Gilinski) | Concuerda con EEFF25 (15-may-2025). Cierra la fecha; no el precio |
| **IEPS** | Tasa de 8% (≥275 kcal/100 g, desde 2014, antes de IVA) sin cambio; 20% es solo propuesta de ONG. **Al 9-10-oct-2026 la Ley de Ingresos 2027 no estaba aprobada** (plazo 20-oct en Cámara y 31-oct en Senado); falta el texto final ([Infobae, 10-oct](https://www.infobae.com/mexico/2026/10/10/monreal-revelo-que-diputados-preven-aprobar-el-paquete-economico-2027-la-siguiente-semana/)) | Media | Mantiene §5; el hallazgo envejece tras el 20-oct |

**No se resolvió (siguen abiertos):**
- Shares de Sabritas, Gamesa y Bokados en México.
- Shares numéricos en Colombia, Argentina, España y Reino Unido.
- Accionistas de control de Gruma, Arca y Lala.
- Precio de la compra del 40% de Bimbo Colombia.
- Origen de US$106.9bn contra US$183bn y de Top 5 contra Top 10 en botanas.
- Ranking de Barcel USA (#5 contra #6).

**Efecto en la tesis (Pilar 1):** el dato de Circana de ~27% para BBU cambia el tono: Bimbo es **líder de marca en pan fresco de EE.UU.** y la marca propia (26%) apenas lo iguala. Eso no prueba ganancia de share (es una foto), pero sí frena leer el 7.4% como debilidad: es el mercado total de panificación. La debilidad sigue en la variación: pan de caja −2.8% contra marca propia −0.4%.

---

## 11. Apalancamiento y múltiplos de pares con Capital IQ (2026-10-16)

Detalle, fórmulas y registro de 14 discrepancias en `capiq-leverage-comps_2026-10-16.md`. Citable en la wiki: [[peer-leverage-capiq-2026-10]], [[peer-multiples-and-operations-capiq-2026-10]], [[capiq-data-discrepancies-2026-10]].

- **«Bimbo tiene el doble de deuda que su competencia» no se sostiene contra pares de EE.UU. y Europa.** Deuda neta/EBITDA LTM: Bimbo 2.5x `[sourced]` 2T26 p.6 (≈2.9x con arrendamientos `[calc]`) contra mediana de pares 3.20x y núcleo 3.57x `[calc]`; Campbell's 4.36x, Flowers 4.02x, Aryzta 3.57x, Mondelez 3.35x, Smucker 3.05x, PepsiCo 2.12x.
- **Sí se sostiene contra Arca Continental (0.74x; Bimbo 3.4x–3.9x mayor) y contra Yamazaki (caja neta).** En términos absolutos la deuda neta de Bimbo es ~4× la de Flowers, pero es tamaño. Gruma no se obtuvo.
- Flowers bajó a **BB+ (negativa)** de BBB- el 2026-09-09 `[sourced]` S&P vía CIQ. Bimbo: BBB+ / BBB+ / Baa1, S&P con perspectiva negativa desde 2025-03-20 `[sourced]` wiki.
- La mediana de EV/EBITDA del núcleo sube de 6.45x a 6.63x; la conclusión no cambia: Bimbo cotiza en línea con los panificadores puros.
- El margen EBITDA LTM de Flowers es 9.3% (no 10.2%) y el de Arca 19.4% (no 20.2%); el margen de NA de Bimbo (9.6%) queda apenas por encima del de Flowers.
- Se descartaron todas las cifras en US$ de Bimbo y las ventas por segmento de la salida de CIQ: no son datos de Capital IQ y no cuadran entre sí.

## Lente LatAm (checklist)

- **Regulación y concesiones:** NOM-051 (fase 3 al 1-ene-2028), reglas escolares obligatorias desde 29-mar-2025, permisos de publicidad, IEPS 8%, reforma de agua y energía; cuotas de azúcar fuera del T-MEC `[sourced]` RA25 p.23, p.29-31. Sin concesiones ni tarifas reguladas.
- **FX:** ingresos 56% en emergentes pero ~44% en USD/CAD/EUR; deuda 42% USD, 42% MXN, 12% EUR; conversión de NA movió el crecimiento reportado entre −7.8 y +11.1 pp `[sourced]` wiki/bimbo-fx-exposure. Costo de trigo en USD; ingreso de México en MXN.
- **Mercado informal y vacíos de datos:** tienda de abarrotes y panadería artesanal (44.3% global) no se miden con precisión; Nielsen y Global Data no coinciden; sin cifras numéricas de share en Brasil, Colombia y Argentina `[unverified]`.
- **Grupos familiares y accionistas de control:** Bimbo está controlado por la familia Servitje (72.0% entre seis tenedores; Normaciel 40.96%) `[sourced]` wiki/governance. Entre competidores: Gruma, Arca, Nutresa (Grupo Gilinski tras la OPA) y Lala tienen accionistas de control o familiares `[unverified]`: detallar con sus filings. Los pares del core tienen estructuras de control distintas.
- **Jugadores transfronterizos:** Mondelez, PepsiCo y Mars-Kellanova (EE.UU.); Gruma (México); Nutresa (Colombia); FGF Brands (Canadá); Lidl/Aldi en Europa. Entrada de marca propia es la amenaza más estructural.

---

## Fuentes

**Documentos locales**
- `filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf` (RA25) y RA24/RA23: tamaño de mercado, shares, canales, regulación, red de distribución.
- `filings/annual/IA25_GB_EEFF_V10.pdf` (EEFF25): costos de materias primas, segmentos.
- `filings/quarterly/` (4T25, 1T26, 2T26): shares por trimestre, mezcla, FX.
- `wiki/Industry/bakery-market-structure.md`, `wiki/Industry/bimbo-competitive-position.md`, `wiki/Company/bimbo-segments-and-regions.md`, `wiki/Company/ciq-customers-and-suppliers.md`, `wiki/Company/bimbo-governance-and-ownership.md`, `wiki/Macro/bimbo-fx-exposure.md`, `wiki/Risks-ESG/bimbo-risk-factors.md`, `wiki/Thesis/bimbo-north-america-turnaround-evidence.md`.
- `reports/Bimbo macro outlook 2026.md`; `output/bimbo-tesis-3-pilares.md`; `BIMBOA/research/industry/industry-report_2026-10-08.md` (pares, múltiplos, eventos 2025-26).

**Web (consultada 2026-10-12)**
- [Expansión, 1-sep-2026: IEPS comida chatarra 2027](https://expansion.mx/economia/2026/09/01/ieps-impuesto-comida-chatarra-2027-8-20)
- [UnoTV: Dan marcha atrás, por ahora, a incremento de IEPS en cerveza y sodio](https://www.unotv.com/nacional/morena-descarta-aumento-ieps-cerveza-sodio-2027/)
- [La Razón, 1-sep-2026: el paquete económico no contempla nuevos impuestos](https://www.razon.com.mx/mexico/2026/09/01/paquete-economico-no-contempla-nuevos-impuestos/)
- [MarketBeat, 20-ago-2026: Flowers Foods 2T26](https://www.marketbeat.com/instant-alerts/flowers-foods-q2-earnings-call-highlights-2026-08-20/)
- [247WallSt: Flowers Foods, volumen de pan −5.8%](https://247wallst.com/cards/flowers-foods-q2-2026-earnings-flo-01m0gd0ee54e939dta0kmmce32)
