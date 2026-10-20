# Grupo Bimbo (BMV: BIMBO A) — valuación consolidada de los tres modelos del equipo (borrador del asistente, 19-oct-2026)

> **Estado:** propuesta del asistente construida con los tres DCF del equipo.
> - No cambia ningún archivo de la v3: `valuation.md`, `valuation.yaml` y la compuerta de publicación `valuation-outputs.yaml` siguen como se publicaron.
> - El precio objetivo y la recomendación son decisión del equipo.
> - Valores por acción en MXN al 16-oct-2026 (precio 58.60), salvo indicación. Montos en millones de MXN.
> - Versión en inglés (la canónica para el reporte): `valuation/consolidated-valuation.md`.

## Archivos

| Archivo | Qué contiene |
|---|---|
| `valuation/BIMBOA_DCF_consolidated_v1.xlsx` | Fórmulas vivas, recalculadas en Excel: 328 celdas con fórmula, 0 errores, todos los controles en OK |
| `valuation/build/consolidate_models.py` | Réplica de los libros de los dos compañeros, los puentes de valor y la consolidación |
| `valuation/build/build_consolidated_workbook.py` | Construye el libro de Excel |
| `valuation/inputs/consolidated_results.json` | Todos los resultados |
| `valuation/team-models/` | Copias de los archivos de Diego y de Alejandro (los originales en Descargas no se tocaron) |

**Verificación:** la réplica reproduce el 47.13 (múltiplo) y el 36.91 (Gordon) de Alejandro, y el 54.94 de Diego, a partir de sus propios supuestos. La diferencia es 0.00 `[calc]`.

## 0. Conclusión

1. **Hay dos juegos de supuestos, no tres.**
   - El libro de Alejandro corre los supuestos de la v3 en la plantilla de S&P Capital IQ. Sus flujos libres 2026-30 son iguales a los de la v3 al peso (117,350) y su WACC también (10.3233%) `[calc]`. Coincide con la v3 por construcción, no como segunda opinión.
   - El de Diego es el único juego independiente en proyección, beta, múltiplo y puente de valor. Sus fuentes del costo de capital son las mismas que las de la v3.
2. **Los WACC coinciden porque las fuentes son las mismas.**
   - Los tres modelos usan tasa libre de riesgo de 7.51%, prima de mercado de 4.20%, costo de deuda de 9.71% y la misma prima país, ponderada por dónde Bimbo genera su EBITDA (2.05%).
   - Solo cambian la beta desapalancada (0.53 contra 0.56) y la cifra de deuda de Diego. Los WACC quedan en 10.32% y 10.40% `[calc]`.
3. **El valor más alto de Diego (54.94 contra 47.13) casi no es una diferencia de opinión.**
   - Su múltiplo de 6.4x suma 4.63 y la participación no controladora a valor en libros suma 4.07.
   - En sentido contrario, tres cosas restan 2.50: la reconversión de su deuda, los derivados incluidos dentro de la deuda de Capital IQ y un periodo parcial que pierde 3.5 meses de flujo.
   - Con los mismos datos y la misma mecánica, sus juicios dan **45.71** y los de la v3 **47.13**. Los dos analistas quedan a Ps 1.42 de distancia `[calc]`.
4. **DCF consolidado.** Promedia 50/50 los juicios y concilia los datos y la mecánica.

   | Método | Valor hoy | vs 58.60 |
   |---|---|---|
   | Múltiplo de salida | **46.42** | −20.8% |
   | Gordon con el rendimiento sobre capital nuevo de la v3 (14.6%) | **30.76** | −47.5% |

   El WACC es 10.38% `[calc]`. Con la configuración que recomiendo (50/50, 5.92x, minoritarios a mercado e impuesto sobre EBIT de 34% en lugar del promedio de 32%), el múltiplo da **45.69**.
5. **Banda de recomendación (convención del equipo).**
   - El valor a 12 meses del múltiplo (51.42) implica un rendimiento esperado de **−10.5%**, medio punto debajo del piso de HOLD. Con la configuración recomendada, **−11.9%**. Gordon da −40.7%.
   - HOLD necesita un valor hoy de al menos 46.66. Por eso se apoya en el múltiplo de salida y además en al menos una de estas decisiones:
     - el múltiplo sin ajustar de Diego (49.75; −4.0%)
     - minoritarios en libros (50.61; −2.4%)
     - impuesto de 30% (47.15; −9.1%) `[calc]`
6. **ESG no mueve la tasa de descuento.** Su efecto en el valor pasa por el margen, el capex, el múltiplo y el puente (sección 9). El único costo ESG contractual, el aumento de cupón del bono BIMBO 23L, vale menos de un centavo por acción `[calc]`.

## 1. Qué es cada modelo

| | v3 (`valuation/`) | Alejandro | Diego |
|---|---|---|---|
| Libro | `BIMBOA_DCF_v3.xlsx` | `Bimbo_DCF_Alejandro.xlsm` | `SPG_DCF_independent_Diego.xlsm` |
| Plantilla / horizonte | Motor + formato S&P; 10 años (FY2026-35) | Plantilla S&P; 5 años (2S26-FY2030) | Plantilla S&P; 5 años (periodo parcial de 76 días a FY2030) |
| Proyección | Supuestos de la v3 (suma por regiones, pilares 1-3) | Supuestos de la v3, copiados (sus controles en Supuestos_DCF: flujo libre = v3) | Consenso de Capital IQ FY26-28 + desaceleración. Él lo llama un marcador neutral |
| Fecha de valuación | Avance desde el cierre del año fiscal (0.79 años) | Anclada al 30-jun y llevada al 16-oct con ke | Descontada desde el 16-oct; balance al 30-jun |
| Valor terminal | Gordon g 4.25% y múltiplo 6.0x sobre FY2035 | Múltiplo 6.0x y Gordon sobre FY2030 | Múltiplo 6.4x sobre FY2030 |
| Puente de valor | Minoritarios a mercado; pensiones, provisiones y derivados solo en Gordon | Igual que la v3 | Minoritarios en libros; sin asociadas; sin otros pasivos |
| **Valor hoy, múltiplo / Gordon** | **45.72 / 33.55** | **47.13 / 36.91** | **54.94 / n.d.** |

## 2. Comparación lado a lado

| Supuesto | v3 / Alejandro | Diego | Consolidado | Tipo |
|---|---|---|---|---|
| Tasa libre de riesgo (M-Bono 9.26% − spread de default 1.75%) | 7.51% | 7.51% | 7.51% | Dato |
| Prima de mercado / prima país (por EBITDA) / costo de deuda antes de impuestos | 4.20% / 2.05% / 9.71% | igual | igual | Dato |
| Beta desapalancada (Damodaran, alimentos procesados, global) | 0.53 | 0.56 | 0.545 | Juicio |
| D/E a mercado, deuda con arrendamientos | 0.743 | 0.774 | 0.743 | Dato (deuda de la empresa) |
| Beta apalancada / ke / WACC | 0.806 / 12.94% / 10.32% | 0.863 / 13.19% / 10.40% | 0.828 / 13.04% / 10.38% | `[calc]` |
| Ventas FY2030 (crecimiento anual FY2025-30) | 504,070 (3.4%) | 511,536 (3.7%) | 507,797 (3.5%) | Juicio |
| Margen EBITDA FY2030 (EBITDA) | 15.3% (77,123) | 14.7% (75,348) | 15.0% (76,245) | Juicio |
| Depreciación y amortización / ventas | 5.9% → 5.85% | plantilla: sube a 100% del capex + arrendamientos | ruta de la v3 | Mecánica |
| Capex sin arrendamientos, FY2026 → FY2030 | 4.6% → 5.5% | 5.2% → 4.8% | 4.9% → 5.1% | Juicio |
| Arrendamientos nuevos / ventas FY2030 | 1.74% (principal + crecimiento del pasivo) | 1.39% (solo principal) | 1.73% | Mecánica |
| Impuesto sobre EBIT | 34% (efectivo) | 30% (estatutario) | 32% | Juicio, señalado |
| Flujo libre FY2026-30, suma | 117,350 | 137,621 | 123,642 | `[calc]` |
| Múltiplo de salida VE/EBITDA (FY2030) | 6.0x | 6.4x | 5.92x | Juicio + base de datos |
| Crecimiento terminal g | 4.25% | 4.00% | 4.125% | Juicio |
| Deuda con arrendamientos / efectivo | 187,021 / 16,563 | 194,918 / 17,023 | 187,021 / 16,563 | Dato |
| Participación no controladora | 18,243 (mercado) | 743 (libros) | 18,069 (mercado, con ke de 13.04%) | Mecánica, provisional |
| Asociadas − ISR estacional por pagar | +1,959 | 0 | +1,959 | Mecánica |
| Otros pasivos tipo deuda (solo Gordon) | 18,135 | 0 | 18,135 | Mecánica |
| Acciones (millones) | 4,294.9 (BMV) | 4,296.3 (Capital IQ) | 4,294.9 | Dato |

## 3. Por qué el valor de Diego es más alto: de Alejandro a Diego paso a paso

Método del múltiplo de salida, un cambio a la vez y en este orden. El recorrido cierra exactamente en el 54.94 de Diego `[calc]`.

| Paso | Valor | Cambio | Tipo |
|---|---|---|---|
| Alejandro: supuestos de la v3 en la plantilla de S&P | 47.13 | | |
| Fecha de valuación: periodo parcial de 76 días desde el 16-oct, con el balance al 30-jun | 46.38 | −0.75 | Mecánica |
| Deuda: derivados incluidos dentro de la deuda total de Capital IQ (+2,658) | 45.76 | −0.62 | Dato |
| Deuda y efectivo reconvertidos a 17.96 MXN/US$, cuando las cifras en pesos y en dólares de Capital IQ implican 17.47 | 44.65 | −1.11 | Dato (por confirmar) |
| Acciones: 4,296.3 millones (Capital IQ) en lugar de 4,294.9 millones (BMV) | 44.64 | −0.01 | Dato |
| Sin asociadas (+6,498) ni ISR estacional por pagar (−4,538) | 44.18 | −0.46 | Mecánica |
| Minoritarios en libros (743) en lugar de a valor de mercado (18,243) | 48.25 | **+4.07** | Mecánica, provisional |
| WACC 10.32% → 10.40% (beta 0.53 → 0.56; D/E con su deuda) | 48.02 | −0.23 | Juicio + dato |
| Ventas: suma por regiones de la v3 → consenso + desaceleración | 49.30 | +1.27 | Juicio |
| Margen EBITDA: v3 (a 15.3%) → consenso (fijo en 14.7%) | 46.01 | **−3.28** | Juicio |
| Depreciación: ruta de la v3 → mecánica de la plantilla | 46.17 | +0.16 | Mecánica |
| Capex sin arrendamientos: v3 → consenso | 47.39 | +1.21 | Juicio |
| Arrendamientos nuevos: principal + crecimiento → solo principal | 48.63 | +1.24 | Mecánica |
| Capital de trabajo | 49.00 | +0.37 | Juicio |
| Impuesto sobre EBIT 34% → 30% | 50.31 | +1.32 | Juicio, señalado |
| Múltiplo de salida 6.0x → 6.4x | **54.94** | **+4.63** | Juicio + base de datos |

Subtotales:

| Grupo | Cambio |
|---|---|
| Datos y fechas | −2.50 |
| Decisiones del puente | +3.62 |
| WACC | −0.23 |
| Juicios de proyección | +0.89 |
| Mecánica de depreciación y arrendamientos | +1.40 |
| Múltiplo | +4.63 |
| **Total** | **+7.80** |

Diego señaló la mayoría de estos puntos en la sección 7 de su nota:
- las fechas, unos Ps 1.5 por acción;
- la base de arrendamientos de los comparables en US GAAP;
- el EBITDA de Gruma;
- los minoritarios en libros.

## 4. Dónde difieren de verdad los dos analistas

Aquí se pasa del juego de la v3 al de Diego un juicio a la vez. Los datos y la mecánica se mantienen iguales: deuda de la empresa, minoritarios a mercado, depreciación y arrendamientos de la v3, y anclaje al 30-jun `[calc]`.

| Juicio | Múltiplo | Cambio | Gordon (RONIC 14.6%) | Cambio |
|---|---|---|---|---|
| Juego de la v3 (= Alejandro) | 47.13 | | 30.36 | |
| Beta desapalancada 0.53 → 0.56 | 46.88 | −0.26 | 29.10 | −1.26 |
| Ventas → consenso | 48.08 | +1.21 | 30.10 | +1.01 |
| **Margen EBITDA → consenso** | 44.75 | **−3.33** | 25.92 | **−4.18** |
| Capex sin arrendamientos → consenso | 45.81 | +1.06 | 26.98 | +1.06 |
| Capital de trabajo | 46.18 | +0.37 | 27.35 | +0.37 |
| Impuesto sobre EBIT 34% → 30% | 47.63 | +1.45 | 32.15 | **+4.80** |
| Múltiplo de salida 6.0x → 5.83x (su regla con datos consistentes en arrendamientos) | **45.71** | −1.93 | 32.15 | 0.00 |
| g 4.25% → 4.00% | 45.71 | 0.00 | **31.09** | −1.06 |

**Lectura.** La diferencia de fondo es el margen.
- La v3 espera que el plan de productividad (pilar 2) lleve el margen EBITDA a 15.3%. El consenso lo deja en 14.7%.
- El juego de Diego es más generoso en ventas, capex e impuesto, y eso compensa la diferencia de margen.

**Pregunta que deja:** ¿los 60 pb de margen arriba del consenso en FY2030 son algo que el equipo puede respaldar con evidencia, o son la tesis misma?

## 5. Cómo se construyó el DCF consolidado

La regla es promediar los juicios, no los errores:
- Los datos llevan un solo valor con fuente.
- La mecánica lleva una sola convención, la técnicamente correcta.
- Solo se promedian los juicios.

Promediar un error de datos con la cifra correcta solo reduce el error a la mitad.

### 5.1 Datos

**Deuda con arrendamientos: 187,021 (cifra de la empresa).** La de Diego, 194,918, es 7,897 más alta. Esta conciliación debe confirmarla Diego; no es un error confirmado `[calc]`.
- **Derivados (2,658).** La deuda total de Capital IQ a jun-26 es 189,679: deuda financiera de 153,660, más arrendamientos de 33,361, más ajustes por derivados de 2,658 (wiki `ciq-debt-stack-and-maturity-ladder`). Los derivados ya están entre los otros pasivos que resta Gordon.
- **Tipo de cambio (5,239).** Diego reconvirtió los US$10,855 millones a 17.96 MXN/US$, el tipo que la wiki `bimbo-wacc-market-inputs-capiq-2026-10` dice que usó Capital IQ. Sin embargo, las cifras de Capital IQ en pesos (189,679) y en dólares (10,855) implican 17.47. El efectivo respalda el 17.47: US$948 millones × 17.47 = 16,565, contra 16,563 de la empresa.

**Otros datos:**
- **Efectivo:** 16,563. La misma reconversión le suma 460 a la cifra de Diego.
- **Acciones:** 4,294.9 millones (aviso a la BMV del 29-jul-2026).

### 5.2 Mecánica

- **Fecha de valuación.** Los flujos y el balance se anclan al 30-jun-2026 y el valor se lleva al 16-oct con ke (el método de Alejandro).
- **Depreciación.** Se usa la ruta de la v3 (5.85-5.9% de las ventas). La de Diego es mecánica de la plantilla, no un juicio, y él mismo la etiqueta así. Lleva la depreciación al 100% del capex más arrendamientos en FY2030, lo que equivale a cero inversión neta mientras las ventas crecen cerca de 4% al año.
- **Arrendamientos nuevos.** Son el principal (1.39% de las ventas) más el crecimiento del pasivo por arrendamiento, que se mantiene en 8.15% de las ventas. Es la base publicada de la v3. La base de Diego, solo el principal, deja fijo el pasivo mientras las ventas crecen.
- **Puente de valor.**
  - Se suman las asociadas y se resta el ISR estacional por pagar.
  - Pensiones, provisiones y derivados (18,135) se restan solo en Gordon, porque los valores empresa de los comparables no los incluyen.
  - Los minoritarios van a valor de mercado: utilidad de los minoritarios 1,814 / (ke − 3%). Es el tratamiento de la v3 y sigue siendo provisional.

### 5.3 Juicios

Los juicios se promedian con peso w para la v3. Recomiendo w = 0.5 porque hay dos juegos de supuestos. Con w = 0.6667, cada modelo pesa un tercio.

### 5.4 Múltiplo de salida

La regla de Diego es la mediana de sus cuatro comparables núcleo. La aplicó a múltiplos de Capital IQ que no están en una misma base:
- Los comparables en US GAAP dejan el costo de arrendamiento operativo dentro del EBITDA, mientras su deuda incluye arrendamientos.
- El EBITDA de Gruma en Capital IQ es 995.0, contra 1,108.9 de la empresa.

En la tabla de la v3, consistente en arrendamientos, los mismos cuatro dan 5.83x:

| Comparable | Tabla de Diego | Consistente en arrendamientos (tabla v3) |
|---|---|---|
| Flowers Foods | 6.68x | 5.61x |
| Gruma | 6.01x | 5.44x |
| Yamazaki | 6.06x | 6.06x |
| Aryzta | 8.33x | 8.33x |
| **Mediana** | **6.37x** | **5.83x** |

La base usa (6.0x + 5.83x) / 2 = **5.92x**. El promedio sin ajustar, 6.2x, se muestra como variante (+3.33 por acción).

### 5.5 Horizonte y reinversión terminal

Los dos compañeros usaron la plantilla de cinco años, así que el consolidado también. Los valores de la v3 a diez años quedan como referencia.

Con cinco años desaparece el juicio principal de la v3: el capex que sube a 6.0% en 2035. Por eso la reinversión terminal entra como supuesto explícito: un rendimiento sobre capital nuevo (RONIC) de 14.6%, el que implica el valor terminal publicado de la v3. Diego no tiene un Gordon ni un juicio de reinversión, así que aquí no hay nada que promediar.

## 6. Resultados consolidados

| Método | Valor hoy | vs 58.60 | Valor a 12 meses* | Rendimiento esperado* |
|---|---|---|---|---|
| **Múltiplo de salida 5.92x** | **46.42** | −20.8% | 51.42 | −10.5% |
| **Gordon, RONIC 14.6%** | **30.76** | −47.5% | 33.72 | −40.7% |
| Gordon al estilo de la plantilla (flujo FY2030 × (1 + g)) | 41.65 | −28.9% | 46.03 | −19.7% |
| Gordon con RONIC = WACC (crecer no crea valor) | 21.36 | −63.6% | 23.09 | −58.8% |

\* Convención de `references/recommendation-guide.md`:
- valor a 12 meses = valor × (1 + ke) − siguiente dividendo (Ps 1.05);
- rendimiento esperado = valor a 12 meses / precio − 1 + dividendo / precio;
- BUY con +15% o más; SELL con −10% o menos.

Con ke de 13.04%, HOLD necesita un valor hoy de al menos **46.66** y BUY de al menos 59.62 `[calc]`.

Supuestos clave:
- WACC 10.38%; ke 13.04%; beta apalancada 0.828
- g 4.125%; múltiplo de salida 5.92x
- impuesto sobre EBIT 32%
- el valor terminal pesa 76% del valor empresa (múltiplo)
- el múltiplo implica que el flujo libre crece 4.16% a perpetuidad `[calc]`

**Un cambio a la vez contra la base**

| Variante | Múltiplo | Gordon (RONIC) | Rendimiento esperado, múltiplo |
|---|---|---|---|
| Base (w = 0.5; 5.92x; minoritarios a mercado; impuesto 32%) | 46.42 | 30.76 | −10.5% |
| **Configuración recomendada: impuesto sobre EBIT 34%** | **45.69** | **28.31** | **−11.9%** |
| Impuesto sobre EBIT 30% | 47.15 | 33.21 | −9.1% |
| Un tercio por modelo (w = 0.6667) | 46.66 | 30.63 | −10.0% (justo en el piso) |
| Promedio sin ajustar del múltiplo, 6.2x | 49.75 | 30.76 | −4.0% |
| Minoritarios en libros | 50.61 | 34.94 | −2.4% |
| Solo el juego de la v3, misma mecánica (= Alejandro) | 47.13 | 30.36 | −9.2% |
| Juego de Diego conciliado (5.83x) | 45.71 | 31.09 | −11.8% |
| Juego de Diego conciliado, con su 6.4x | 52.29 | 31.09 | +0.9% |

**Promediar resultados contra promediar supuestos**

| Enfoque | Valor | Por qué difiere |
|---|---|---|
| Promedio simple de los tres valores publicados por múltiplo (45.72, 47.13, 54.94) | 49.26 | Le da dos votos a la v3 y arrastra los problemas de datos de Diego |
| Promedio de Alejandro y Diego tal como se publicaron | 51.04 | Arrastra los problemas de datos |
| **Juicios promediados con datos conciliados (este modelo)** | **46.42** | |

Los resultados publicados cargan las diferencias de puente y de datos de la sección 3. Promediarlos mezcla errores con juicios.

**Por qué los dos métodos del DCF difieren 34%.**
- El múltiplo de 5.92x se comporta como el Gordon al estilo de la plantilla, cuyo múltiplo implícito es 5.88x.
- Ese Gordon deja crecer el flujo a g casi sin reinversión adicional, lo que exige un rendimiento de 27.7% sobre el capital nuevo.
- Con el 14.6% de la v3, el múltiplo terminal justificado sería 4.96x `[calc]`.

Los jueces van a preguntar por esta brecha; la guía señala las diferencias mayores a 20%. La respuesta del equipo es su visión del rendimiento de largo plazo de Bimbo sobre el capital nuevo.

**Horizonte.** El Gordon de la v3 a diez años (33.55) queda arriba del Gordon a cinco años con los mismos supuestos de la v3 y RONIC consistente (30.36). La versión a cinco años aplica la reinversión terminal desde 2031, mientras que la v3 sube el capex por etapas hasta 6.0% en 2035.

## 7. Sensibilidad (viva en el libro de Excel)

Múltiplo de salida: WACC (filas) × VE/EBITDA de salida (columnas).

| WACC \ múltiplo | 5.0x | 5.5x | **5.92x** | 6.5x | 7.0x |
|---|---|---|---|---|---|
| 9.38% | 38.49 | 44.64 | 49.77 | 56.93 | 63.08 |
| 9.88% | 37.03 | 43.05 | 48.07 | 55.09 | 61.11 |
| **10.38%** | 35.59 | 41.49 | **46.42** | 53.29 | 59.19 |
| 10.88% | 34.20 | 39.98 | 44.80 | 51.54 | 57.32 |
| 11.38% | 32.83 | 38.49 | 43.22 | 49.82 | 55.49 |

Gordon con RONIC de 14.6%: WACC (filas) × g (columnas).

| WACC \ g | 3.125% | 3.625% | **4.125%** | 4.625% | 5.125% |
|---|---|---|---|---|---|
| 9.38% | 38.81 | 41.76 | 45.25 | 49.43 | 54.55 |
| 9.88% | 32.45 | 34.73 | 37.37 | 40.49 | 44.23 |
| **10.38%** | 26.96 | 28.73 | **30.76** | 33.10 | 35.86 |
| 10.88% | 22.19 | 23.57 | 25.12 | 26.90 | 28.95 |
| 11.38% | 18.00 | 19.07 | 20.26 | 21.61 | 23.14 |

El derecho de los minoritarios y el factor para llevar el valor al 16-oct se mantienen con el ke base.

## 8. DCF inverso y comparables

**Qué necesita el precio** (múltiplo de salida, una palanca a la vez) `[calc]`, cualquiera de estas tres:
- un múltiplo de salida de **6.95x** (Bimbo cotiza a 6.94x UDM con minoritarios en libros y a 7.12x con minoritarios a mercado);
- un WACC de 6.96%;
- un crecimiento de ventas 3.10 pp mayor cada año de la proyección.

**Comparables.** Valores con el mismo puente de comparables de la v3: EBITDA UDM 60,919; deuda neta con arrendamientos; minoritarios a mercado; asociadas.

| Múltiplo | Valor por acción |
|---|---|
| Mediana de panificadoras núcleo, tabla v3 (Flowers, Gruma): 5.53x | 35.95 |
| Los cuatro núcleo de Diego en la tabla consistente: 5.83x | 40.33 |
| 6.0x (juicio de salida de la v3) | 42.68 |
| Los cuatro núcleo de Diego como él los calculó: 6.37x | 47.93 |
| Los nueve comparables, tabla de Diego: 8.20x | 73.92 |
| Todos los comparables elegibles, tabla v3: 8.27x | 74.87 |

Los comparables secundarios (Mondelez, PepsiCo, Smucker, Campbell's) tienen márgenes EBITDA de 16-25% contra 14.5% de Bimbo. Los dos compañeros toman su mediana como techo, no como base.

## 9. Riesgos y ESG traducidos a valor

Fuente: Reporte General ESG v2 de Diego (`valuation/team-models/BIMBOA_ESG_Report_EN_Diego.pdf`). Sus cifras marcadas `[unverified]` no se usan como evidencia.

| Palanca (un cambio contra la base) | Tema ESG o de riesgo y evidencia | Múltiplo | Gordon (RONIC) |
|---|---|---|---|
| Margen EBITDA −50 pb cada año | Trigo y clima. Las materias primas son ~64% del costo de ventas `[sourced/calc]`. El director de finanzas atribuyó 60 pb del margen EBITDA de 2022 al ciclo del trigo `[guidance]`. El alza del trigo en 2026 (+17%) es `[unverified]` | −3.72 | −4.59 |
| Capex +50 pb de las ventas cada año | Agua. 101 centros de trabajo están en estrés hídrico alto o extremadamente alto `[sourced]`. La extracción de agua subió 15.1% desde FY2019 `[calc]`. Existe una bolsa de capex de sustentabilidad desde 2025; el monto no se divulga `[sourced]` | −2.05 | −2.05 |
| Crecimiento de ventas −50 pb cada año | Regulación de salud: fase 3 del etiquetado frontal desde el 1-ene-2028 y reglas de alimentos escolares desde el 29-mar-2025 `[sourced]`. Los consumidores se alejan del azúcar y la harina refinada | −1.84 | −1.57 |
| Múltiplo de salida −0.5x | Gobierno corporativo. El grupo de control tiene 72.03% y los consejeros independientes son 38.9% `[sourced]`. La protección a minoritarios califica 1 de 10 en su rúbrica `[assumption]`. El gobierno es el pilar débil en todas las fuentes de calificación | −5.90 | 0.00 |
| Pasivo único de MXN 1,000 millones | Litigios. Las demandas colectivas de Canada Bread por fijación de precios siguen abiertas y sin provisión; la multa de CAD 50 millones se pagó en 2023 `[sourced]`. Las posiciones fiscales inciertas (8,537) ya se restan en Gordon | −0.24 | −0.24 |
| Costo recurrente de MXN 1,000 millones al año antes de impuestos, desde FY2027 | Mercado de carbono en México: piloto 2020-25, sin reglas publicadas `[sourced]`. Responsabilidad extendida del productor por la ley del 19-ene-2026 `[sourced]` | −1.43 | −1.77 |
| Aumento de cupón del bono BIMBO 23L | Alcance 3 / SBTi. +25 pb sobre MXN 12,000 millones del 21-nov-2031 al 20-may-2033 si no se verifica la meta de −28% `[sourced]`. El Alcance 3 de 2025 quedó 46.7% arriba de la base del bono `[calc]`. La certificación SBTi está en pausa | −0.004 | −0.004 |
| WACC +50 pb (no es ESG) | Riesgo país y cambiario | −1.62 | −5.64 |

**Lectura.**
- **Dónde pega el ESG.** Entra al valor sobre todo por el trigo y el agua (margen y capex) y por el gobierno corporativo (el múltiplo). Nada de eso requiere una tasa de descuento más alta.
- **Sin prima ESG en la tasa.** El reporte de Diego no encuentra ninguna fuente que ligue las calificaciones ESG de Bimbo con su costo de deuda o de capital. Agregar una prima contaría dos veces riesgos que ya están en los flujos.
- **Calificaciones como contexto.** LSEG da 84.62 (A) y S&P da 59, contra un promedio de la industria de 29. Son contexto, no un supuesto de valuación.
- **Pasivos.** Cada MXN 1,000 millones de pasivo sin provisión cuesta unos Ps 0.24 por acción.

## 10. Momento de decisión: qué significa para el HOLD

**Su idea, en sus palabras.** Tienen HOLD y quieren defender por qué se quedan: ni venden ni compran.

**Qué dice la evidencia consolidada.**
- El múltiplo de salida queda justo debajo del piso de HOLD: 46.42 hoy contra 46.66, o 45.69 con el impuesto recomendado.
- El método de flujos (Gordon con 14.6% de rendimiento sobre el capital nuevo) queda muy dentro de SELL.
- HOLD solo se sostiene si el equipo argumenta dos cosas: que el múltiplo terminal del mercado guía mejor que su propio cálculo de reinversión, y que Bimbo sí llega a un margen de 15.0% en FY2030.

**Mi recomendación.**
- Si mantienen HOLD, usen el DCF por múltiplo de salida como método principal y presenten Gordon como escenario bajista.
- Anclen el múltiplo en evidencia que puedan mostrar: Bimbo cotiza hoy a 6.9-7.1x, tiene la mezcla de México, y las panificadoras núcleo cotizan a 5.4-6.1x.
- Decidan primero el peso, la base del múltiplo y la tasa de impuesto, y solo después vean la banda. No escojan las reglas para caer dentro de HOLD; los jueces preguntan por qué cambiaron las reglas.

**El argumento más fuerte en contra.**
- Los dos métodos del DCF difieren 34%.
- Un múltiplo cercano a 6x supone un rendimiento de 27.7% sobre el capital nuevo, casi el doble del 14.6% que implica la ruta de capex de su propia v3.
- Con la configuración recomendada, el múltiplo mismo da −11.9%.
- Un juez puede decir que el HOLD descansa en un supuesto que su propio Gordon rechaza. Visto así, la evidencia apunta a SELL.

**Pregunta para el equipo.** Para el valor terminal de Bimbo, ¿en qué confían más: en el múltiplo que el mercado les da a los comparables (5.4-6.1x para las panificadoras núcleo) o en su propio cálculo de reinversión (14.6% sobre el capital nuevo)?

## 11. Decisiones que le corresponden al equipo

1. **Peso:** 50/50 entre los dos juegos de supuestos (recomendado) o un tercio por modelo.
2. **Base del múltiplo de salida:** la regla de Diego con datos consistentes en arrendamientos, 5.92x (recomendado), o el 6.2x sin ajustar.
3. **Impuesto sobre EBIT:** efectivo de 34% (recomendado para impuestos en efectivo), estatutario de 30%, o el promedio de 32% de la base.
4. **Minoritarios:** a valor de mercado (v3, provisional) o en libros.
5. **Horizonte:** la plantilla de cinco años (los dos compañeros) o los diez años de la v3 con el aumento gradual del capex. Esto fija la reinversión terminal.
6. **Precio objetivo y recomendación:** método principal, ponderación de métodos, precio objetivo y recomendación.

## 12. Pendientes

- **Deuda y efectivo de Diego.** Sus libros todavía usan la deuda (194,918) y el efectivo (17,023) reconvertidos de Capital IQ. Diego debe confirmar el tipo de cambio y pasar a las cifras de la empresa (187,021 / 16,563).
- **EBITDA de Gruma** (punto abierto de Diego). La v3 usa la cifra de la empresa, 1,108.9, no el 995.0 de Capital IQ.
- **Minoritarios a valor de mercado.** Siguen como provisionales hasta que el equipo decida; también está abierto en la v3.
- **Proyección de Diego.** Por su propia descripción es un marcador de consenso. Los supuestos de la historia del equipo están en `model/drivers.yaml`.
- **Compuerta de publicación.** Los valores consolidados no están en ella. Si el equipo los adopta, hay que actualizar `valuation-outputs.yaml` antes de que el reporte, la presentación o el pitch usen cualquier cifra.
- **Cifras `[unverified]` del reporte ESG de Diego.** Por ejemplo, el alza del trigo en 2026 y los 89 contra 101 sitios con estrés hídrico. Hay que resolverlas o retirarlas antes del reporte oficial (sección 6 de su propio documento).
