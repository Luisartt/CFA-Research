# Análisis de industria — Grupo Bimbo (BIMBOA.MX)

_Actualizado 2026-10-17 (refresh de `/research-analyst:industry-analysis`). Reemplaza como vigente a `industry-report_2026-10-12.md`, que se conserva. Las secciones 8, 9 y 10 (Deep Research y resolución de pendientes del 12-oct) no cambian y se leen en esa versión. Cada número lleva etiqueta; fuentes al final._

**Etiquetas:** `[sourced]` dato con fuente · `[guidance]` dicho por el management de una emisora · `[calc]` cálculo propio · `[assumption]` interpretación, pendiente de que el equipo la valide · `[unverified]` sin fuente primaria local. Equivalencia con el plugin research-analyst: observado = `[sourced]`; guidance = `[guidance]`; supuesto = `[assumption]`; output = `[calc]`.

**Claves de fuente:** RA25/RA24/RA23 = reportes anuales a la BMV; EEFF25 = estados financieros auditados FY25; nQyy ER = comunicados trimestrales; wiki = `wiki/Industry/`, `wiki/Company/`, `wiki/Macro/`; Macro = `reports/Bimbo macro outlook 2026.md`; Pares v3 = `valuation/BIMBOA_PeerAnalysis_v3.xlsx` (base de reclamos: deuda + arrendamientos + NCI en libros − caja; EBITDA equivalente a IFRS 16; tipo de cambio 18.479 MXN/USD del 16-oct-2026); macro-view = `macro/macro-view.yaml`.

**Qué cambió contra el 12-oct (detalle en el diff al final):**
1. Los múltiplos y márgenes de pares salen ahora del libro de pares v3 (Capital IQ, prompts 1 y 4-7), con una sola base de reclamos y el tipo de cambio de la fecha de precios. Esto cambia la lectura de valuación relativa: **sobre la misma base, Bimbo (6.94x) cotiza con prima frente al núcleo de panificadores (5.53x)**, no en línea.
2. Gruma entra con consenso, P/U y apalancamiento; Yamazaki, Aryzta y Arca tienen ahora acciones, precio y un EV descriptivo, y siguen fuera de las medianas.
3. Se agrega la intensidad de capital de los pares (capex/ventas de consenso, 3.7-3.8%) como referencia para el capex terminal de Bimbo (consenso ~5.0%).
4. El vínculo con la tesis usa los pilares que el equipo eligió el 16-oct (`research/thesis.md` v1), no los del borrador del 08-oct.
5. El contexto macro sale de `macro/macro-view.yaml` (datos observados, por confirmar).

---

## Indicador de pendientes abiertos (2026-10-17)

Leyenda: `[x]` abierto, sin fuente verificable · `[aviso]` parcial, solo fuentes secundarias o foto sin serie · `[ok]` resuelto.

| # | Pendiente | Estado | Qué falta |
|---|---|---|---|
| 1 | Share de EE.UU. en pan | [aviso] | ~27% BBU (Circana 53 sem. al 3-ene-2026, vía Flowers); sin serie histórica comparable |
| 2 | Share de EE.UU. en bollería, pastelitos y botanas | [x] | Solo Circana de pago o IR de Bimbo |
| 3 | Ranking de Barcel USA en botanas (#5 vs #6) | [x] | Sin fuente verificada |
| 4 | Tamaño del mercado de México en US$ | [aviso] | Rango secundario US$6-11bn, sin definición común |
| 5 | Shares de México: Sabritas, Gamesa, Bokados | [x] | Sin Nielsen, Euromonitor ni Kantar |
| 6 | Shares numéricos de Brasil, Colombia, Argentina, España y Reino Unido | [x] | Solo liderazgo cualitativo |
| 7 | Brasil: Wickbold y Nutrella | [aviso] | Aprobado por Cade con venta de Nutrella; precios sin revelar |
| 8 | Bimbo Colombia / Nutresa | [aviso] | Fecha y 39.99% confirmados; precio sin revelar |
| 9 | Accionistas de control de Gruma, Arca y Lala | [x] | Solo «grupo de control ~51%» de Gruma |
| 10 | IEPS 2027 y Ley de Ingresos | [aviso] | 8% vigente; al 17-oct el texto final no está en las fuentes locales (plazos 20-oct y 31-oct) |
| 11 | Botanas: US$106.9bn (RA25) vs US$183bn (informe integrado) | [x] | Contradicción interna de Bimbo |
| 12 | Múltiplos y márgenes de los pares | [aviso] | **Avance 17-oct:** libro de pares v3 con Gruma completo y Yamazaki/Arca con EV descriptivo; faltan NCI en libros de Aryzta y Arca, arrendamientos operativos de Yamazaki y múltiplos históricos |
| 13 | Split volumen/precio de Bimbo en EE.UU. | [x] | No publicado |
| 14 | Ruta de reparto vigente (54,000 vs 53,000) | [x] | Menor; sin aclaración |
| 15 | Marca propia en pan de EE.UU. | [aviso] | ~26% $ y ~35% unidades (10-K de Flowers, sin periodo) |
| 16 | Precio de cierre oficial de BMV de Gruma (nuevo) | [aviso] | Se usa la cotización con retraso de Yahoo (242.02), corroborada por el gráfico de CIQ dentro de 0.05% |

Resumen: [x] 7 · [aviso] 9 · [ok] 0.

---

## 1. Definición de mercado, tamaño y ciclo de vida

Sin cambios contra el 12-oct; se repite lo esencial.

| Eje | Dentro | Fuera / marginal |
|---|---|---|
| Producto | Pan de caja, bollería, pastelitos, galletas, tortilla empacada, bagels y muffins, botanas saladas (Barcel, Takis), pan para QSR | Pan artesanal (competencia, no mercado servido); tortilla de maíz/masa (Gruma); confitería (Ricolino vendida) |
| Geografía | 39 países; FY25: NA 44.6%, México 32.4%, EAA 12.7%, LatAm 10.3% de ventas `[sourced]` 4T25 p.4 | Asia marginal salvo China |
| Cliente | Retail moderno (Walmart ~15% `[sourced]` RA25 p.103), tradicional/conveniencia, QSR | Venta directa: inmaterial |

| Mercado | Tamaño 2024 | CAGR 2019-24 | CAGR 2024-29E | Tag |
|---|---|---|---|---|
| Panificación global | US$638.9bn | 2.8% | 4.7% | `[sourced]` RA25 p.107-108 |
| Norteamérica | US$139.1bn | 4.1% | 4.3% | `[sourced]` RA25 p.108 |
| Latinoamérica | US$121.8bn | 4.0% | 5.5% | `[sourced]` RA25 p.108 |
| México (panificación) | n/d en US$ | n/d | 3.5% | `[sourced]` RA25 p.111 |
| Botanas saladas globales | US$106.9bn | 5.3% | 3.7% | `[sourced]` RA25 p.113 |

- Crecimiento ponderado por la mezcla de Bimbo ≈ **4.2% nominal en valor** 2024-29E `[calc]` (incluye precio e impuestos, no es volumen).
- **Ciclo de vida: maduro** `[assumption]`: valor +3-5% casi todo por precio y mezcla; volumen plano o negativo en mercados desarrollados.
- **Contraste con el ciclo macro** (`macro/macro-view.yaml`, por confirmar): inflación de México 3.45% y de EE.UU. 3.74% en sep-2026 `[sourced]` CIQ; el FMI espera 2.1% de crecimiento real y 3.0% de inflación en México para 2029-31 `[sourced]`. Con inflación de ~3% y crecimiento real de ~2%, el 4.2% de valor de la industria queda por debajo del PIB nominal (~5%): la categoría crece menos que la economía.
- **Coach moment 1 (definición de mercado)**: sigue abierto; ver la versión del 12-oct.

---

## 2. Cinco fuerzas

| Fuerza | Intensidad | Evidencia | Tag |
|---|---|---|---|
| **Rivalidad** | Alta en EE.UU.; media en México | Flowers 2T26 volumen −5.8%, precio/mezcla +1.8%, guía recortada `[sourced]`; Bimbo dice ganar share en todas las categorías de EE.UU. en 2T26 `[guidance]`. **Nuevo (17-oct):** el mercado castiga a los panificadores de EE.UU.: Flowers −75% en 5 años y −44% en el año, Campbell's −50% y −29% (precio en USD) `[calc]` Pares v3, gráfico CIQ (prompt 5); Bimbo −4% y −1% (en MXN) | `[sourced]` / `[guidance]` / `[calc]` |
| **Entrada** | Baja en escala, alta en lo local | La barrera es entregar fresco con vida de anaquel de 14 días (RA25 p.100, p.110); amenaza real: marca propia y hard-discount | `[sourced]` |
| **Poder de proveedores** | Medio | Materias primas ~30% de ventas y ~64% del costo de ventas (EEFF25 p.82); trigo, azúcar y aceites en USD. Trigo CBOT dic-26 US$6.865/bu (+35% a/a) `[sourced]` Macro. El margen bruto se mueve contra el trigo con ~1 año de rezago (r = −0.74, 2017-2025, n = 9) `[calc]` `wiki/Risks-ESG/bimbo-climate-metrics-capiq-2026-10.md` | `[sourced]` / `[calc]` |
| **Poder de compradores** | Alto en desarrollados; bajo en emergentes | Walmart ~15%; canal moderno 77.7% en NA vs ~59-60% tradicional en LatAm (RA25 p.103, p.110) | `[sourced]` |
| **Sustitutos** | Medio-alto | Artesanal 44.3% y marca propia 9.6% del mercado global (RA25 p.107); GLP-1: gasto en súper −5.3% en seis meses tras iniciar (Cornell/JMR) `[sourced]` | `[sourced]` |

**Lectura de márgenes de largo plazo** `[assumption]`: dos industrias en una. México/LatAm: comprador atomizado, DSD propia, margen EBITDA ~20% (México LTM 2T26 20.9% `[calc]`). EE.UU./Canadá/Europa: comprador concentrado, marca propia, volumen que se encoge. **Nuevo:** sobre la base comparable de arrendamientos (EBITDA equivalente a IFRS 16), Flowers gana 11.1% LTM `[calc]` Pares v3; el margen de NA de Bimbo (9.6% LTM, base de la empresa) queda **por debajo** del panificador puro de EE.UU., no apenas por encima como se leía con márgenes reportados (9.3%).

---

## 3. Paisaje competitivo y participación

Sin cambios en participaciones (ver 12-oct, §3 y §8-§10). Lo esencial:
- Global (Global Data 2024): Bimbo 3.7%, 1.2× el segundo (Mondelez 3.0%); top-10 = 11.7%; marca propia 9.6%; artesanal 44.3% `[sourced]` RA25 p.107-109.
- México: pan empacado 18.2%, pastelitos 28.2%, botanas 18.4% (#2) `[sourced]` RA25 p.111, p.113.
- EE.UU.: ~27% del pan fresco, bollos y rolls (Circana, 53 sem. al 3-ene-2026, vía Flowers) `[sourced]`; 7.4% de toda la panificación (Global Data) `[sourced]`.
- Consolidación 2025-26: Mars-Kellanova, Ferrero-WK Kellogg, Flowers-Simple Mills, venta de marcas de Hostess por Smucker `[sourced]` informe 08-oct.

---

## 4. Posicionamiento y moat

| Fuente de ventaja | Evidencia | ¿Aparece en números? | Veredicto `[assumption]` |
|---|---|---|---|
| **Red DSD** | 54,000+ rutas, 249 plantas en 39 países (RA25 p.14, p.100) | **México sí:** margen EBITDA 20.9% LTM `[calc]`. **EE.UU. no:** NA 9.6% LTM contra Flowers 11.1% en base comparable de arrendamientos `[calc]` Pares v3 | Ancho en México/LatAm; sin evidencia en NA |
| **Marca** | 9,000+ SKUs; 12.6% de ventas de innovación (RA25 p.80, p.87) | México sí (28.2% en pastelitos) | Fuerte en México; medio en EE.UU. |
| **Escala de compras** | Citada sin cifra (RA25 p.109) | **Margen bruto LTM: Bimbo 52.6% contra Flowers 48.6%, Gruma 38.8%, Arca 46.9%, PepsiCo 54.3%** `[calc]` Pares v3 (utilidad bruta de CIQ, prompt 6). El margen bruto sí es superior al del panificador de EE.UU.; la diferencia se va en el costo de distribución | Margen bruto superior; la ventaja no llega al EBITDA en NA |
| **QSR global** | Proveedor principal en 40 países (RA25 p.87, p.112) | Parcial: EAA +8.4% ex-FX en 2T26 | Medio |

**Coach moment 2 (moat)**, actualizado:
- **Mi recomendación:** declarar un moat regional: ancho en México/LatAm, sin evidencia hoy en EE.UU.
- **Por qué:** con la base comparable de arrendamientos, el margen de NA (9.6%) queda debajo del de Flowers (11.1%) pese a ser 4× más grande, aunque su margen bruto consolidado es 4 pp mayor.
- **El mejor argumento en contra:** el 9.6% de NA es base de la empresa y el 11.1% de Flowers suma el costo de arrendamientos operativos; la comparación exacta requiere el EBITDA de NA antes de arrendamientos, que Bimbo no publica por región.
- **Pregunta para el equipo:** ¿qué número del P&L de EE.UU. demostraría que la escala de Bimbo es una ventaja y no solo tamaño?

---

## 5. FODA (propuesta de la IA — el equipo valida)

Sin cambios de contenido contra el 12-oct: es del equipo y sigue sin validar. Ver la tabla en `industry-report_2026-10-12.md` §5. Dos datos nuevos que el equipo puede usar al validarlo, sin que se agreguen aquí como posiciones:
- Para «Balance» (fortaleza): deuda neta/EBITDA en base de reclamos 2.81x contra mediana de nueve pares 2.98x `[calc]` Pares v3 (§11).
- Para «Insumos 2027» (amenaza): trigo de 2026 corriendo ~+17% `[unverified]` (corrida de CIQ AI) y el rezago de ~1 año del margen bruto `[calc]`.

---

## 6. Universo de comparables (libro de pares v3)

Base única de reclamos (EV = capitalización + deuda + arrendamientos + NCI en libros − caja; EBITDA equivalente a IFRS 16), precios al 16-oct-2026, tipo de cambio 18.479 `[calc]` Pares v3. Reemplaza las cifras del 16-oct (base CIQ, que mezclaba bases de arrendamiento).

| Par | Ticker | Por qué comparable | Marco | EV/EBITDA LTM | NTM | P/U LTM | En medianas |
|---|---|---|---|---|---|---|---|
| **Flowers Foods** | FLO | Panificador puro de EE.UU. con DSD: espejo del margen de NA | US GAAP | 5.61x | 6.15x | 23.45x | sí (valuación y P/U) |
| **Gruma** | GRUMAB | Emisora BMV, IFRS, México + EE.UU.; tortilla y harinas | IFRS | 5.44x | 5.64x | 9.36x | **sí, ahora también NTM y P/U** |
| **Yamazaki** | 2212.T | Mayor panificador puro fuera de América | J-GAAP | 6.06x | 5.84x | 17.74x | no: arrendamientos operativos fuera de balance |
| **Aryzta** | ARYN | Panificación europea, QSR/congelado | IFRS | 8.33x | 5.81x | 10.21x | no: NCI sin verificar |
| J.M. Smucker | SJM | Hostess compite en pastelitos | US GAAP | 8.88x | 9.22x | 58.63x | solo valuación (utilidad deprimida) |
| Campbell's | CPB | Pepperidge Farm y snacks | US GAAP | 7.66x | 8.36x | 15.11x | sí |
| Mondelez | MDLZ | Galletas en México y EE.UU. | US GAAP | 16.14x | 13.80x | 23.10x | sí |
| Arca Continental | AC | Consumo mexicano con ruta propia; Bokados | IFRS | 7.85x | 7.11x | 18.71x | no: NCI sin verificar |
| PepsiCo | PEP | Sabritas vs Barcel; Gamesa | US GAAP | 11.19x | 11.03x | 16.15x | sí |
| **Bimbo (sujeto)** | BIMBOA | — | IFRS | **6.94x** | 6.58x | 18.46x | — |

Medianas (elegibles): núcleo de panificación LTM **5.53x** (n=2), NTM 5.89x; todos LTM **8.27x** (n=6), NTM 8.79x; P/U LTM 16.15x y NTM 11.72x (n=5) `[calc]` Pares v3 (102/102 resultados iguales al cálculo independiente).

**Excluidos del universo** (sin cambio): Kellanova (privatizada), Hostess (dentro de SJM), Lala (no cotiza), Nutresa (ilíquida), Herdez, General Mills, McKee y Uno Bakery.

**Lectura de valuación relativa (cambia contra el 12-oct)** `[calc]`:
- Sobre la misma base de reclamos, **Bimbo cotiza a 6.94x contra 5.53x del núcleo: con prima de ~25%**, no en línea. La lectura del 12-oct (6.63x del núcleo contra 6.29-6.68x de Bimbo) mezclaba bases: para Flowers el EV de CIQ ya incluía arrendamientos operativos pero el EBITDA estaba después de su costo (6.68x contra 5.61x en base comparable), y el núcleo incluía a Yamazaki y Aryzta, que hoy no pasan las pruebas de base (arrendamientos y NCI).
- Contra todos los pares elegibles (8.27x), Bimbo sigue con descuento.
- Con el NCI a valor de mercado (la base que usa el DCF), Bimbo cotiza a 7.12x `[calc]` `valuation/valuation.md` §6.

**Coach moment 3 (comparables)**, actualizado:
- **Mi recomendación:** mantener el núcleo (Flowers y Gruma) para la mediana del múltiplo de salida y mostrar los elegibles como rango (seis en EV/EBITDA, cinco en P/U).
- **El mejor argumento en contra:** con solo dos panificadores en el núcleo, la mediana es un promedio de dos empresas en estrés o de otro negocio (tortilla); un juez puede pedir Yamazaki con un ajuste propio de arrendamientos.
- **Pregunta para el equipo:** ¿por qué un panificador con 55% del EBITDA en México debería salir a un múltiplo menor que el que hoy le paga el mercado (6.94x)?

---

## 7. Implicaciones para el pronóstico y la tesis

### Supuestos de industria que el modelo debe respetar

| Supuesto | Valor propuesto | Fuente / tag |
|---|---|---|
| Mercado de panificación México (valor) | ~3.5% CAGR 2024-29E | `[sourced]` RA25 p.111 |
| Categoría de pan EE.UU. (volumen) | −2% a −4% en 2026-27 (base) | `[assumption]` proxy FLO −5.8% |
| Precio/mezcla EE.UU. | +1% a +2% | `[assumption]` FLO +1.8% |
| Share Bimbo EE.UU. / México | Estable | `[assumption]` / `[sourced]` RA25 p.111 |
| LatAm / EAA mercado (valor) | 5.5% / 3.4-6.6% | `[sourced]` RA25 p.108 |
| Margen EBITDA NA | 9.6% LTM; techo de referencia 10-12% (Flowers 11.1% en base comparable de arrendamientos) | `[calc]` |
| Margen EBITDA México | ~20.5-21% con presión laboral 2027 | `[calc]` |
| IEPS | 8% base; 20% solo bajista | `[sourced]` |
| Insumos 2027 | Trigo US$7.0-7.2/bu base; margen bruto bajo presión 1S27 | `[sourced]` Macro |
| **Capex/ventas (nuevo)** | Referencia de pares 3.7-3.8% (consenso FY1-FY3); Bimbo consenso 5.2% / 5.0% / 4.9%; el modelo llega a 6.0% en FY2035 | `[calc]` Pares v3 (prompt 7) |

### Vínculo con los pilares del equipo (`research/thesis.md` v1, pilares del 16-oct)

| Pilar | Efecto de la industria | Razón |
|---|---|---|
| **1. Cambio climático e insumos** | Relevante | El insumo principal es trigo en USD (proveedor sin poder propio, precio exógeno); el margen bruto reacciona con ~1 año de rezago. La industria no da protección: todos los panificadores cubren a plazos cortos |
| **2. Ejecución del nuevo CEO** | Matiza | La comparación con Flowers en base comparable deja a NA por debajo del par; la mejora de margen de NA (5.9% a 10.0%) cierra la brecha, pero no la supera |
| **3. Manejo de deuda (hold)** | Apoya | En base de reclamos, Bimbo 2.81x contra mediana de nueve pares 2.98x (5.º menos apalancado de 10) `[calc]`: «en línea», coherente con un hold |

**Siguiente paso recomendado:** decidir el múltiplo de salida con el dato nuevo de que Bimbo cotiza con prima sobre el núcleo de panificadores (6.94x contra 5.53x).

---

## 8-10. Deep Research y resolución de pendientes (12-oct)

Sin cambios. Ver `industry-report_2026-10-12.md` §8, §9 y §10.

---

## 11. Apalancamiento de pares (base de reclamos, libro de pares v3)

| Empresa | Deuda neta/EBITDA LTM | Nota |
|---|---|---|
| Yamazaki | −0.67x | Caja neta (deuda neta de CIQ; descriptivo) |
| Arca Continental | 0.74x | Descriptivo (sin NCI) |
| Gruma | 1.47x | **Nuevo:** con arrendamientos IFRS 16 y NCI |
| PepsiCo | 2.26x | |
| **Bimbo** | **2.81x** | Con arrendamientos 33,361 y NCI en libros (2.5x en la definición de la empresa `[sourced]` 2T26 p.6) |
| Smucker | 2.98x | Mediana de los nueve pares |
| Mondelez | 3.25x | |
| Flowers | 3.37x | Rebajada a BB+ (negativa) el 2026-09-09 `[sourced]` S&P vía CIQ |
| Aryzta | 3.50x | |
| Campbell's | 4.25x | |

Fuente: `[calc]` Pares v3, columna «Net debt / EBITDA LTM». La conclusión del 16-oct se mantiene: «el doble de deuda que su competencia» no se sostiene; Bimbo está en la mitad del grupo.

---

## Lente LatAm (checklist)

Sin cambios contra el 12-oct (regulación NOM-051, IEPS, reforma de agua y energía; FX: 42-44% de la deuda en USD; vacíos de datos del canal tradicional; control familiar Servitje 72.0%; jugadores transfronterizos). Nuevo dato de FX: USD/MXN 18.479 al 16-oct-2026 contra 17.47 al 30-jun `[sourced]` macro-view.

---

## Diff contra la versión del 2026-10-12

| § | Antes (12-oct) | Ahora (17-oct) | Fuente del cambio | ¿Toca el modelo? |
|---|---|---|---|---|
| 6. Comps | Núcleo 6.63x con base CIQ; Bimbo 6.29-6.68x: «en línea» | Núcleo 5.53x en base de reclamos; Bimbo 6.94x: **prima de ~25%**; todos 8.27x | Pares v3 (CIQ prompts 4-7; tipo de cambio 18.479) | SÍ: múltiplo de salida (DCF v3 'Scenarios': 5.53x da 41.39 por acción) |
| 6. Comps | Gruma 5.7x `[unverified]`, sin consenso | Gruma 5.44x LTM, 5.64x NTM, P/U 9.36x; entra a NTM y P/U | CIQ prompt 4 | SÍ: medianas NTM y P/U de la valuación |
| 6. Comps | Yamazaki y Arca solo con herramienta de múltiplos | EV descriptivo (6.06x y 7.85x); siguen excluidos | CIQ prompts 4-5 | no |
| 2/4. Márgenes | Flowers 9.3% (reportado); NA de Bimbo «apenas por encima» | Flowers 11.1% en base comparable de arrendamientos; NA de Bimbo por debajo | Pares v3 | no directo (techo de margen de NA en drivers.yaml) |
| 4. Moat | Escala de compras: «no visible» | Margen bruto LTM 52.6% contra Flowers 48.6% | CIQ prompt 6 | no |
| 7. Supuestos | Sin referencia de capex | Pares 3.7-3.8%; consenso de Bimbo ~5.0% | CIQ prompt 7 | SÍ: capex terminal (±50 pb = ∓9.4 por acción) |
| 7. Pilares | Pilares del 08-oct (margen NA, capex, valuación) | Pilares del 16-oct (clima e insumos, CEO, deuda hold) | `docs/context/memory.md` | no |
| 11. Deuda | Mediana 3.20x (base CIQ); Gruma sin dato | Mediana 2.98x en base de reclamos; Bimbo 2.81x; Gruma 1.47x | Pares v3 | no |
| 2. Rivalidad | Sin desempeño bursátil | Flowers −75% y Campbell's −50% en 5 años | CIQ prompt 5 | no |

---

## Fuentes

- `valuation/BIMBOA_PeerAnalysis_v3.xlsx` y `valuation/inputs/peer_extras_v3.yaml` (Capital IQ prompts 4-7, 16/17-oct-2026), `valuation/valuation.md` v3, `macro/macro-view.yaml`.
- `data/capitaliq/capiq-ai-model-gaps-4/5/6/7_2026-10-17.md` (salidas crudas de CIQ).
- Todas las fuentes de `industry-report_2026-10-12.md` (RA25, EEFF25, comunicados, wiki, Macro, web del 12-oct).
