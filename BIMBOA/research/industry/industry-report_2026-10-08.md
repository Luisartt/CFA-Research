# Industry Report — Panificación empacada y botanas / BIMBOA   [2026-10-08]

**Estado:** primer reporte (no hay versión anterior, así que no hay diff). El FODA (§5) está **pendiente del analista**: aquí solo va la propuesta de estructura y la evidencia.

**Etiquetas:** `observado` = dato con fuente · `guidance` = lo que dice el management de cualquier emisora · `supuesto` = interpretación del analista o de esta skill, hasta que el analista la valide.

**Fuentes y claves:**
- **RA25 / RA24 / RA23:** reportes anuales de Bimbo a la BMV (`filings/bmv/`), compilados en el wiki: [[bakery-market-structure]], [[bimbo-competitive-position]], [[bimbo-segments-and-regions]].
- **nQyy ER:** releases trimestrales de Bimbo.
- **Competidores:** filings y releases públicos, con la URL en cada fila (§3).
- **Múltiplos:** stockanalysis.com, consultado el 2026-10-08. Es un agregador gratuito, no un filing.
- **Insumos que faltan:** no existe `research/industry/sources/` con research de terceros ni `macro/macro-view.yaml`, así que el contraste contra el ciclo macro (§2) queda abierto.

---

## 1. Estructura de la industria (five forces)

| Fuerza | Intensidad | Evidencia | Tag |
|---|---|---|---|
| **Amenaza de entrada** | Baja en escala, alta en lo local | Las barreras históricamente bajas mantienen la industria poco concentrada (RA25 p.109). La vida de anaquel de 14 días limita a los jugadores sin red de distribución a mercados locales (RA25 p.100, p.110). La tecnología de empaque está alargando la vida útil y el radio de entrega, así que la barrera se erosiona (RA25 p.110). | observado |
| **Poder de proveedores** | Medio | Las materias primas son ~30% de ventas y ~64% del costo de ventas (FY25). El trigo es el insumo principal y se cotiza en USD; Bimbo lo cubre con futuros y swaps ([[bimbo-input-costs]]; RA25 p.97). Al ser commodities, el proveedor no tiene poder propio, pero el precio es exógeno. | observado |
| **Poder de compradores** | **Alto y creciente** en mercados desarrollados | Walmart pesa ~15% de las ventas FY25 (RA25 p.103). En Norteamérica el canal moderno es 77.7% (RA25 p.110). La consolidación de retailers presiona precio y fondos de promoción (RA25 p.32), y los formatos alternativos pueden generar deflación (RA25 p.31). En LatAm y MENA el canal tradicional/especialista pesa ~59-60% (RA25 p.110), así que ahí el comprador está atomizado. | observado |
| **Sustitutos** | Medio-alto | Panaderías artesanales 44.3% y marca propia 9.6% del mercado global de 2024 (RA25 p.107). Tortilla en México. GLP-1: casi tres docenas de empresas no farmacéuticas lo mencionaron en llamadas de inicios de 2026, contra 14 un año antes (Reuters/LSEG). EY-Parthenon estima hasta US$12bn de ventas de snacks perdidas en una década. Smucker dice que no ve impacto material en Hostess (Food Business News, ago-2025). | observado / guidance (Smucker) |
| **Rivalidad** | **Alta en EE.UU.**, moderada en México | **EE.UU.:** categoría con volumen negativo. Flowers en 2Q26: volumen −5.8%, price/mix +1.8%; volumen de marca propia de Flowers −7.6% ([10-Q ex99.1 de FLO](https://www.sec.gov/Archives/edgar/data/0001128928/000119312526359191/flo-ex99_1.htm)). Bimbo afirma que ganó participación en todas las categorías de EE.UU. en 2Q26, la primera vez desde 2020 (2Q26 ER p.3). Si ambas cosas son ciertas, la ganancia es de suma cero contra competidores en una categoría que encoge. **México:** Bimbo lidera con 18.2% en pan empacado y 28.2% en pastelitos (RA25 p.111). La competencia es artesanal y fragmentada. | observado / guidance (Bimbo) |

**Lectura (`supuesto`):** la estructura no es una sola, son **dos industrias**:
- **México y LatAm:** comprador fragmentado, red DSD propia y líder con 4-6x la participación del siguiente jugador empacado. Es una estructura favorable.
- **EE.UU., Canadá y Europa:** comprador concentrado, marca propia y categoría madura o en contracción. Es una estructura adversa, donde la escala de Bimbo protege volumen pero no margen (ver §4).

## 2. Ciclo de vida y drivers

- **`life_cycle_stage`: `mature`** (`supuesto`).
  - Panificación global: CAGR 2.8% en 2019-24 y 4.7% esperado para 2024-29E, en valor RSP con impuestos e inflación incluidos (Global Data vía RA25 p.107-108; `observado`).
  - Norteamérica: CAGR 4.1% en 2019-24 y 4.3% en 2024-29E, también en valor (RA25 p.108). Por volumen la categoría de EE.UU. está en contracción (ver Flowers en §1).
  - Bolsillos de crecimiento: México (3.5% CAGR 2024-29E, RA25 p.111), LatAm (5.5%), Europa del Este (6.6%) y Asia (5.0%) (RA25 p.108).
- **Cíclica vs defensiva:** defensiva en volumen. El ciclo pega por trading-down hacia marca propia y artesanal, y por la mezcla de canales (RA25 p.109, `observado`). Bimbo atribuyó a "débil consumo de la industria" ocho trimestres negativos de NA ex-FX, del 1Q24 al 4Q25 ([[bimbo-competitive-position]] §4, `guidance`).
- **Sensibilidades:**
  - **Commodities:** trigo, aceites, azúcar y gas natural; las materias primas pesan ~30% de las ventas.
  - **Tipo de cambio:** la conversión de NA da un swing de −7.8 a +11.1 pp en el crecimiento reportado ([[bimbo-fx-exposure]]).
  - **Tasas:** deuda neta/EBITDA de 2.5x.
  - **Regulación (México):** NOM-051 fase 3 al 1-ene-2028; reglas escolares obligatorias desde el 29-mar-2025 (RA25 p.29-31). **IEPS:** la tasa de 8% sobre alimentos con ≥275 kcal/100g (pan dulce, galletas, botanas) sigue igual en 2026. Subirla a 20% se discute para el paquete 2027, sin aprobar ([Expansión, 1-sep-2026](https://expansion.mx/economia/2026/09/01/ieps-impuesto-comida-chatarra-2027-8-20)).
  - **Regulación (EE.UU.):** la FDA revocó el Rojo No. 3, con cumplimiento al 15-ene-2027. Bimbo promete quitar los colorantes artificiales a nivel global para fin de 2026, y BBU quitará conservadores, colorantes y saborizantes artificiales de 5 marcas top para 2028 ([FoodNavigator, 8-jul-2026](https://www.foodnavigator.com/Article/2026/07/08/grupo-bimbo-sets-2028-deadline-for-artificial-ingredient-removal-in-us/); `guidance`).
- **Mercado vs PIB, insumo de la ruta top-down (`supuesto`):**
  - México: el mercado (3.5% nominal en valor) crece aproximadamente con el PIB nominal.
  - EE.UU.: el volumen va por debajo del PIB real y el valor depende de precio.
  - **Pendiente:** contrastar contra `macro-view.yaml` cuando exista.

## 3. Landscape competitivo

Participación global en 2024 (Global Data vía RA25 p.107-109; `observado`):
- Bimbo: 3.7% en todas las categorías (4.1% en core bread/cakes), 1.2x el segundo jugador.
- Top-10: 11.7%.
- Artesanal 44.3% y marca propia 9.6%.

**Participación por país** (RA25 p.83, p.110-111; `observado`):
- EE.UU.: 7.4% (RA24 decía 8.1%, base re-estimada).
- Canadá: 13.3%.
- México: 18.2% en pan empacado y 28.2% en pastelitos.
- Botanas México (Barcel): 18.4% (Nielsen).

**Benchmark de métricas.** Las cifras son del último año fiscal (FY). Las columnas tienen bases distintas:
- **GM** = margen bruto, el reportado salvo que se indique otra cosa. En Flowers excluye D&A.
- **EBITDA** = EBITDA ajustado de la compañía, salvo marca **(agr.)**: dato TTM del agregador, menos confiable.

| Emisora | Marco | Ventas FY (US$bn aprox.) | GM | EBITDA | Mg. operativo | DN/EBITDA | Crecimiento orgánico (vol / precio) | Traslape con Bimbo | EV/EBITDA LTM |
|---|---|---|---|---|---|---|---|---|---|
| **Grupo Bimbo** | IFRS | FY25: MXN 427.0bn (~22.2) | 52.3% | 13.9% (NA 9.0%, MX 20.4%) | 8.0% | 2.5x (2Q26) | +1.6% ex-FX (sin split cuantificado) | — | n/d en este reporte |
| Flowers Foods (FLO) | US GAAP | 5.26 | 48.9% | 10.2% | 7.0% | 3.2x | ~−2% / ~−0.8%; 2Q26: −5.8% / +1.8% | EE.UU., 100% panificación | 6.6x |
| Gruma (GRUMAB) | IFRS | 6.37 | 39.1% | 17.8% | ~14.0% | 1.3x | Vol. plano; ventas −1.7% | Tortilla EE.UU. y México | 5.7x |
| Yamazaki (2212.T) | J-GAAP | ~8.7 | ~32.7% (agr.) | ~8.2% (agr.) | 4.7% | caja neta | n/d | Panificación core; Asia marginal | 6.3x |
| Aryzta (ARYN) | IFRS | ~2.5 | ~20% (agr.) | 13.8% | ~7.4% | ~3.4x | +1.5% (ambos positivos) | Europa, canal QSR, congelado | 7.2x |
| J.M. Smucker (SJM) | US GAAP | 9.05 | 34.9% aj. | ~20.3% | 18.5% aj. | ~3.8x | 4Q: vol −4 / precio +10 | Hostess (10.7% de ventas, mg. de segmento 10.0% vs 18.6%) | 8.7x |
| Campbell's (CPB) | US GAAP | 9.74 | 28.5% aj. | ~16.6% (agr.) | ~12.1% | ~4.2x | −3 / +1; Snacks −5 / … | Pepperidge Farm, pan fresco | 7.9x |
| Mondelez (MDLZ) | US GAAP | 38.5 | 28.4% (GAAP, con mark-to-market de cacao) | ~15.3% (agr.) | 13.2% aj. | ~3.2x | −3.7 / +8.0 | Galletas; EE.UU., México, UE | 16.1x |
| PepsiCo (PEP) | US GAAP | 93.9 | 54.5% core | ~20.2% (agr.) | ~15.9% core | ~2.4x | PFNA: −2 / +1; LatAm Foods: ~0 / +4 | Sabritas vs Barcel | 10.8x |
| Arca Continental (AC) | IFRS | ~12.9 | ~46.9% (agr.) | 20.2% | ~15.6% | ~1.3x | 4Q25 vol −1.1% | Bokados vs Barcel; ruta en México | 8.1x |

**Fuentes de la tabla** (todas `observado`, salvo lo marcado como agregador):
- Bimbo: [[bimbo-income-statement-fy21-fy25]] y [[bimbo-segments-and-regions]].
- FLO: [release 4Q FY25](https://investors.flowersfoods.com/~/media/Files/F/Flowers-Foods-V3/documents/events/q4-fy-2025/flowers-foods-inc-reports-fourth-quarter-2025-results.pdf). El split de volumen FY25 viene de Food Business News y falta verificarlo en el release.
- GRUMAB: [reporte 4Q25 p.12](https://www.gruma.com/media/731211/4q25-gruma-e.pdf).
- SJM: [ex99.1 FY26](https://www.sec.gov/Archives/edgar/data/0000091419/000009141926000047/sjm06092026exhibit991.htm).
- CPB: [ex99.1 4Q FY26](https://www.sec.gov/Archives/edgar/data/0000016732/000001673226000020/exhibit991-q42026.htm).
- MDLZ: [10-K FY25](https://www.sec.gov/Archives/edgar/data/1103982/000162828026005345/mdlz-20251231.htm).
- PEP: [release 4Q25, p.4 y A-10](https://investors.pepsico.com/docs/pepsico-5v9wci20/media/Files/investors/q4-2025-earnings-release.pdf).
- Yamazaki: [kessan tanshin FY25](https://www2.jpx.co.jp/disc/22120/081220260118535320_tse-acedjpsm-22120-20260118535320-ixbrl.htm).
- Aryzta: [resultados FY25](https://www.gettex.de/en/news-overview/newsdetail/aryzta-ag-2025-annual-results/).
- AC: [release FY25](https://www.arcacontal.com/en/noticia/corporate/arca-continental-reporta-crecimiento-de-46-de-ventas-y-de-30-de-ebitda-en-2025).
- EV/EBITDA: stockanalysis.com, 2026-10-08.

**Notas de comparabilidad:**
- Los cierres fiscales difieren: GIS cierra en mayo, SJM en abril, CPB en agosto, y el FY25 de FLO tuvo 53 semanas. Hay que calendarizar antes de usar los múltiplos en Val_Comps.
- El margen bruto de Bimbo incluye una parte de la distribución en el costo de ventas, y ~36% de las ventas se va en gastos de distribución y venta ([[bimbo-business-model]]). Comparar GM entre emisoras con DSD y sin DSD es engañoso; **la métrica comparable es el margen EBITDA**.

**Eventos sectoriales 2025-26** (`observado`):
- Mars cerró la compra de Kellanova (~US$36bn) el 11-dic-2025.
- Ferrero compró WK Kellogg por US$3.1bn.
- Flowers compró Simple Mills, recortó guidance FY26 (ventas −3.5% a −2.2%) y redujo el dividendo a la mitad (may-26).
- Smucker vendió las marcas de valor de Hostess (mar-25); el margen del segmento Hostess cayó a la mitad.
- Campbell's recortó su dividendo 36%.
- Aryzta está revisando "todas las opciones" para Alemania (ago-26).

**Lectura (`supuesto`):** el panificador puro de EE.UU. está en modo defensa: el par más cercano a BBU (Flowers) recorta dividendo y guidance en el mismo periodo en que Bimbo reporta ganancias de share. Las fuentes del agregador están en el reporte del agente y se pueden copiar a `sources/`.

## 4. Posicionamiento de la emisora

| Moat | Evidencia | Fuerza (`supuesto`) |
|---|---|---|
| **Costo y escala en distribución (DSD)** | Más de 54,000 rutas, más de 1,700 centros de venta y 249 plantas en 39 países (RA25 p.14). Rutas propias en México y LatAm; distribuidores independientes en EE.UU., Canadá y Europa (RA25 p.100). Reposición gratuita de producto no vendido con vida de anaquel de 14 días (RA25 p.100). | **Fuerte en México** (margen EBITDA 20.4% vs Gruma 17.8% y Arca 20.2%). **Media en EE.UU.:** el margen de NA de 9.0% está por debajo del 10.2% de Flowers, que tiene la cuarta parte del tamaño. La escala no se traduce en ventaja de margen. |
| **Marca** | Bimbo, Marinela, Barcel, Sara Lee, Thomas', Entenmann's y Dempster's; más de 9,000 SKUs (RA25 p.87); 12.6% de ventas FY25 vino de innovación (RA25 p.80). | Fuerte en México (28.2% en pastelitos). Media en EE.UU.: competencia contra marca propia y trading-down. |
| **Relación con QSR** | Proveedor principal de panificación al canal QSR en 40 países (RA25 p.87, p.112). | Media: cliente concentrado (McDonald's, RBI, Yum) y contrato industrial. |
| Switching / red / IP | No aplica de forma material. | — |

**Posición global (`supuesto`):** **fuerte** en México, LatAm (líder de pan empacado en cada país, RA25 p.111) e Iberia; **media** en EE.UU. y Canadá; **débil o en construcción** en China (2Q26 ER p.4 cita debilidad en el negocio de marca).

**Materialidad para impact-triage:** cerca del 55% del EBITDA viene de México y ~29% de NA (Celebramos p.17). Un evento en México (IEPS 20% o etiquetado) pega directo al motor de márgenes. Un evento en EE.UU. pega al volumen, pero sobre una base de margen más baja.

## 5. FODA — **PENDIENTE DEL ANALISTA**

La skill propone la estructura y la evidencia; el contenido final lo decide el analista. Cada candidato trae su reto.

| | Candidato (`supuesto`, sin validar) | Evidencia a favor | Reto |
|---|---|---|---|
| F | Red DSD con densidad en México | MX 20.4% de margen; 18.2% y 28.2% de share | ¿Es replicable por Gruma, Arca o Sabritas, que ya tienen ruta en México? |
| F | Escala global y compras de trigo | 3.7% de share global, 1.2x el segundo | NA rinde 9.0% contra 10.2% de Flowers. ¿Dónde está la ventaja de costo en EE.UU.? |
| D | NA con margen bajo y volumen débil | 8 trimestres negativos ex-FX; 5.9% de margen en 4Q24 | La recuperación a 10.0% en 2Q26: ¿estructural (productividad) o insumos más baratos? |
| D | Concentración en Walmart | ~15% de ventas | — |
| O | Ganancia de share en EE.UU. mientras los rivales se debilitan | 2Q26 ER: share en todas las categorías; Flowers en retirada | Son afirmaciones cualitativas, sin datos de Circana. ¿Share comprada con precio? |
| O | Crecimiento inorgánico en LatAm y EAA | Wickbold, Don Don, Karamolegos | LatAm bajó a 7.6% de margen por la integración |
| A | IEPS 8% → 20% en 2027 | En discusión (Expansión) | Pan dulce, galletas y Barcel están en la base gravable |
| A | GLP-1 y la ola "clean label" / MAHA | Tendencia en llamadas de pares | Bimbo va adelantado en colorantes; ¿eso es oportunidad o costo? |
| A | Marca propia y trading-down en mercados desarrollados | 9.6% global; Flowers −7.6% de volumen en marca propia | Bimbo salió de parte de su marca propia en EE.UU. y Canadá: ¿cede volumen? |

## 6. Universo de comparables

| Ticker | Rol | selected_because |
|---|---|---|
| **FLO** | Core | Es el par más directo de BBU: panificación de EE.UU. con DSD y distribuidores independientes. Es la mejor referencia del margen de NA. |
| **GRUMAB** | Core | Panificación y harinas, emisora de la BMV con IFRS y exposición a EE.UU. y México muy parecida a la de Bimbo. |
| **2212.T** (Yamazaki) | Core | Panificador puro de mayor tamaño fuera de América. Ancla de múltiplo para el pure-play. |
| **ARYN** | Core | Panificación europea y canal QSR; traslapa con EAA y Bimbo QSR. |
| **SJM** | Secundario | Hostess compite contra los pastelitos de Bimbo en EE.UU. |
| **CPB** | Secundario | Pepperidge Farm (pan fresco) y snacks en EE.UU. |
| **MDLZ** | Secundario | Galletas en México y EE.UU.; segundo lugar global en "todas las categorías" (3.0%). Es una prima de calidad, no un par operativo. |
| **AC** | Secundario | Consumo mexicano con ruta propia; Bokados compite contra Barcel. |
| **PEP** | Secundario | Sabritas y Frito-Lay contra Barcel. Su múltiplo es de mega-cap global. |

**Excluidos y por qué:**
- **Kellanova:** privatizada por Mars (dic-2025). Queda solo como comp de transacción.
- **Hostess:** dentro de SJM desde nov-2023.
- **Grupo Lala:** fuera de bolsa; solo deuda.
- **Grupo Nutresa:** iliquida tras la recompra de Gilinski; no hay múltiplo confiable.
- **Herdez:** sin panificación, y su P&L está distorsionado por la desconsolidación de McCormick de México (ene-2026). Va a watchlist.
- **GIS:** traslape parcial (Pillsbury); además, el FY26 viene con desinversiones y deterioros. Va a watchlist.
- **McKee:** privada.
- **"Uno Bakery Corporation":** aparece en la tabla de Global Data (RA25 p.109) con 0.7% de share, pero no es identificable como emisora listada.

**Decisión del analista pendiente:** ¿Val_Comps usa solo el core (4) o core + secundario (9)? Recomendación (`supuesto`): **el core para la mediana** y el secundario como rango.

## 7. Supuestos de industria para el modelo (→ assumptions)

| Supuesto | Valor propuesto | Fuente / tag |
|---|---|---|
| Crecimiento del mercado de panificación en México (valor) | 3.5% CAGR 2026-29 | Global Data vía RA25 p.111 — `observado` (dato de tercero) |
| Crecimiento de la categoría de pan en EE.UU. (volumen) | −2% a −4% en 2026; 0% a −1% a mediano plazo | Proxy de FLO: FY25 ~−2%, 2Q26 −5.8% — `supuesto` |
| Precio en la categoría EE.UU. | +1% a +2% | FLO 2Q26 price/mix +1.8%; PFNA +1 — `supuesto` |
| Share de Bimbo en EE.UU. | Estable a +0.2 pp/año | Solo `guidance` cualitativa (2Q26 ER); sin Circana — `supuesto` |
| Share de Bimbo en México | Estable (18.2% en pan, 28.2% en pastelitos) | RA25 p.111 — `observado` |
| Crecimiento de mercado LatAm y EAA | 5.5% y 3.4-6.6% en valor | Global Data vía RA25 p.108 — `observado`. Ojo: incluye inflación |
| IEPS México | 8% caso base; 20% desde 2027 en escenario bajista | Expansión, 1-sep-2026 — `observado` (propuesta) |
| Márgenes de referencia de pares | Panificador de EE.UU. ~10%; Mexico consumer 18-20% | §3 — `observado` |

**Advertencia:** Global Data re-basa sus cifras cada año (por ejemplo, botanas pasaron de US$194.4bn en RA24 a US$106.9bn en RA25). No hay que encadenar sus tamaños en series.

**Datos que faltan:**
- Datos de Circana o Nielsen en puntos.
- Tamaño de mercado por país.
- Share de marca propia por país.
- Split volumen/precio de Bimbo.
