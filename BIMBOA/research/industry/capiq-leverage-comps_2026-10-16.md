# Capital IQ: apalancamiento y múltiplos de pares — verificado (2026-10-16)

_Fuente: salida del Prompt 1 de Capital IQ (precios 15/16-oct-2026), repasada contra el reporte anual, los comunicados de Bimbo y `wiki/Valuation/bimbo-capital-structure-and-debt.md`. Todo número lleva etiqueta; los pares son `[sourced]` S&P Capital IQ salvo donde diga `[calc]`. La salida cruda está en `data/capitaliq/capiq-ai-prompt1_2026-10-16.md` (moverla a `raw/`) y ya se compiló en `wiki/Valuation/`: `peer-leverage-capiq-2026-10`, `peer-multiples-and-operations-capiq-2026-10` y `capiq-data-discrepancies-2026-10`._

## 1. Veredicto sobre «Bimbo tiene el doble de deuda que su competencia»

**No se sostiene contra los pares de EE.UU. y Europa; sí contra los pares mexicanos de consumo.** Depende del universo y de la definición.

| Medida (LTM) | Bimbo | Mediana pares núcleo | Mediana todos los pares | Arca Continental |
|---|---|---|---|---|
| Deuda neta/EBITDA, definición de la empresa (sin IFRS 16) | **2.5x** `[sourced]` 2T26 p.6 | 3.57x `[calc]` | 3.20x `[calc]` | 0.74x `[calc]` |
| Deuda neta incl. arrendamientos / EBITDA (comparable con CIQ) | **≈2.9x** `[calc]` | 3.57x | 3.20x | 0.74x |
| Bimbo ÷ mediana (definición de la empresa / con arrendamientos) | — | 0.70x / 0.82x | 0.78x / 0.91x | **3.4x / 3.9x** |

- Bimbo está por debajo de Campbell's (4.36x), Flowers (4.02x), Aryzta (3.57x), Mondelez (3.35x) y Smucker (3.05x), y por encima de PepsiCo (2.12x), Arca (0.74x) y Yamazaki (caja neta).
- **El «2x» solo aparece en términos absolutos** (deuda neta de Bimbo ≈ 4× la de Flowers y ≈ 8× la de Aryzta) y contra Arca: eso es tamaño, no apalancamiento. Gruma, el otro par mexicano, no se obtuvo.
- Cálculo con arrendamientos `[calc]`: deuda neta Ps. 137.1 mil millones + arrendamientos ≈ Ps. 34 mil millones (rango 33-35, wiki) = 171.1; EBITDA LTM de la empresa Ps. 60.9 mil millones `[sourced]` (wiki, `bimbo-cross-source-connections` C3): 171.1 / 60.9 = 2.81x. Con el EBITDA implícito de CIQ (64.7) da 2.64x. El 58.5 de la salida no cuadra con ninguno de los dos. La deuda neta con arrendamientos de CIQ (US$9,907m) entre el EBITDA de la empresa (US$3,393m a 0.05569) da 2.92x: ese es el dato de trabajo.
- **Por qué no usar 2.3x (el de la salida):** divide la deuda neta sin IFRS 16 (137.1) entre un EBITDA con IFRS 16 (58.5). La empresa reporta 2.5x con ambos sin IFRS 16. La mezcla subestima la deuda.

## 2. Apalancamiento LTM de los pares (misma base, de la tabla de CIQ)

Deuda y deuda neta de CIQ incluyen arrendamientos. EBITDA = LTM de CIQ. Ratios recalculados `[calc]`.

| Empresa | Ticker | Deuda neta (US$ m) | Deuda total (US$ m) | EBITDA LTM (US$ m) | Deuda neta/EBITDA | Deuda total/EBITDA | Calificación S&P |
|---|---|---|---|---|---|---|---|
| Campbell's | CPB | 7,056.0 | 7,450.0 | 1,620.0 | 4.36x | 4.60x | BBB- (neg.) |
| Flowers Foods | FLO | 1,955.0 | 2,007.8 | 486.9 | 4.02x | 4.12x | **BB+ (neg.), bajó de BBB- el 2026-09-09** |
| Aryzta | ARYN | 901.9 | 986.9 | 252.4 | 3.57x | 3.91x | n/d |
| Mondelez | MDLZ | 20,343.0 | 22,059.0 | 6,080.0 | 3.35x | 3.63x | BBB |
| J.M. Smucker | SJM | 6,897.0 | 6,940.2 | 2,263.9 | 3.05x | 3.07x | BBB |
| PepsiCo | PEP | 40,718.0 | 51,881.0 | 19,171.0 | 2.12x | 2.71x | A+ |
| Arca Continental | AC | 2,015.4 | 3,644.0 | 2,707.0 | 0.74x | 1.35x | mxAAA (escala nacional, no comparable) |
| Yamazaki | 2212 | (473.5) | 600.9 | 706.7 | −0.67x (caja neta) | 0.85x | NR |
| **Grupo Bimbo** | BIMBOA | ≈ Ps. 137.1 mil millones | Ps. 153.7 mil millones | n/d en CIQ | **2.5x (empresa) / ≈2.9x (con arrendamientos)** | n/d | **BBB+ (S&P, perspectiva negativa desde 2025-03-20) / BBB+ Fitch / Baa1 Moody's** `[sourced]` wiki |
| Gruma | GRUMAB | n/d | n/d | n/d | n/d | n/d | n/d |

- Mediana núcleo (FLO, ARYN, 2212; Gruma sin dato) = **3.57x**. Mediana de los 8 pares con dato = **3.20x**, media 2.57x.
- Las perspectivas de Mondelez, Smucker y PepsiCo en CIQ tienen fecha antigua (2016-2025); **Moody's y Fitch no se obtuvieron** (sin derechos) y no hay historial de 10 años.
- **Flowers pasó a grado especulativo (BB+)** `[sourced]` S&P vía CIQ 2026-09-09: no estaba en el reporte del 12-oct y refuerza la lectura de panificador de EE.UU. en defensa.

## 3. Múltiplos EV/EBITDA LTM — cifras que reemplazan a las del 08-oct

El EV/EBITDA que devuelve la herramienta de múltiplos de CIQ **no coincide con el EV y el EBITDA de la propia tabla**. Se usa el cociente de la tabla (misma fecha, mismas definiciones) y se conserva el valor de la herramienta para auditoría.

| Par | EV (US$ m) / EBITDA | **EV/EBITDA usado** | Valor herramienta CIQ | Valor 08-oct (heredado) |
|---|---|---|---|---|
| Flowers | 3,250.7 / 486.9 | **6.68x** `[calc]` | 5.15x | 6.6x |
| Aryzta | 2,103.3 / 252.4 | **8.33x** `[calc]` | 7.31x | 7.2x |
| J.M. Smucker | 20,509.5 / 2,263.9 | **9.06x** `[calc]` | 8.57x | 8.7x |
| Campbell's | 13,287.9 / 1,620.0 | **8.20x** `[calc]` | 6.47x | 7.9x |
| Mondelez | 101,964.8 / 6,080.0 | **16.77x** `[calc]` | 14.48x | 16.1x |
| PepsiCo | 220,113.5 / 19,171.0 | **11.48x** `[calc]` | 10.35x | 10.8x |
| Yamazaki | EV n/d | **6.58x** `[sourced]` herramienta CIQ, sin EV | 6.58x | 6.3x |
| Arca Continental | EV n/d (mal resuelto) | **8.47x** `[sourced]` herramienta CIQ, sin EV | 8.47x | 8.1x |
| Gruma | n/d | **5.7x** `[unverified]` (08-oct) | n/d | 5.7x |
| Bimbo | n/d en CIQ | 6.29x (base CIQ) / 6.68x (empresa), del reporte 12-oct `[unverified]` | n/d | — |

- **Mediana núcleo** (FLO 6.68, GRUMAB 5.7, 2212 6.58, ARYN 8.33) = **6.63x**, antes 6.45x. Sin Gruma (3 pares) = 6.68x.
- **Bimbo cotiza en línea con el núcleo** (6.29x–6.68x frente a 6.63x), igual que antes: la conclusión del §6 no cambia.
- EV/EBITDA NTM `[sourced]` CIQ: FLO 7.55x, Yamazaki 6.37x, Aryzta 5.94x, SJM 9.86x, CPB 9.07x, MDLZ 14.13x, AC 7.87x, PEP 11.24x. Mediana núcleo NTM (FLO, 2212, ARYN) = 6.37x.
- P/E LTM `[sourced]`: FLO 23.45x, 2212 17.74x, ARYN 10.21x, SJM 58.63x, CPB 15.11x, MDLZ 23.10x, AC 18.71x, PEP 16.15x. El de Smucker está distorsionado (utilidad deprimida), no usarlo.

## 4. Operación de los pares (CIQ, margen EBITDA LTM) — reemplaza cifras del reporte

| Par | Margen EBITDA FY25 | LTM | Margen EBIT LTM | Retorno sobre capital LTM |
|---|---|---|---|---|
| Flowers | 9.8% | **9.3%** | 6.4% | 6.1% |
| Yamazaki | 8.1% | 8.2% | 4.7% | 6.5% |
| Aryzta | 11.4% | 9.8% | 7.4% | 7.8% |
| J.M. Smucker | 24.7% | 24.7% | 18.6% | 7.9% |
| Campbell's | 18.4% | 16.6% | 12.4% | 6.6% |
| Mondelez | 13.0% | 15.3% | 11.8% | 6.1% |
| Arca Continental | 19.5% | **19.4%** | 15.6% | 11.0% |
| PepsiCo | 19.4% | 19.5% | 16.1% | 13.6% |

- **Cambia una cifra del análisis:** el margen EBITDA LTM de Flowers es **9.3%**, no 10.2% (ese era FY24), y el de Arca **19.4%**, no 20.2%. Con eso el margen de NA de Bimbo (9.6% LTM) queda **ligeramente por encima** del de Flowers, en vez de por debajo. Las definiciones de EBITDA difieren (Bimbo ajustado sin IFRS 16; CIQ estandarizado), así que la diferencia de 0.3 pp no es concluyente.
- Consenso FY26E-FY28E de EBITDA (US$ m) `[sourced]` CIQ Estimates: Flowers 458.6 / 430.1 / 432.4 (cae); Mondelez 6,735 / 7,265 / 7,700; PepsiCo 19,051 / 19,587 / 20,590; Arca 2,930 / 3,006 / 3,234; Yamazaki 700 / 742 / 766; Aryzta 355 / 364 / 381. Flowers es el único con EBITDA de consenso a la baja.

## 5. Bimbo por segmento (única parte de la salida que se conserva)

Margen EBITDA ajustado `[sourced]` comunicados de Bimbo, coincide con los ya usados:

| Segmento | FY24 | FY25 | 2T26 |
|---|---|---|---|
| Norteamérica | 8.4% (Ps. 15,813 m) | 9.0% (Ps. 17,117 m) | 10.0% |
| México | 20.3% | 20.4% | 20.7% |
| EAA | 9.4% | 10.8% | 11.7% |
| Latinoamérica | 9.0% | 8.1% | 7.7% |
| Grupo | 13.6% | 13.9% | 14.4% |

Crecimiento ex-FX de EBITDA FY25 vs FY24 `[sourced]`: NA +2.4%, México +2.8%, EAA +26.9%, LatAm −2.2%, Grupo +4.7%.

## 6. Registro de discrepancias (qué se reemplazó y qué se descartó)

| # | Hallazgo | Acción |
|---|---|---|
| 1 | Bimbo deuda neta/EBITDA: 2.3x en la salida vs **2.5x** `[sourced]` 2T26 p.6 | **Reemplazado por 2.5x**; 2.3x mezcla bases |
| 2 | «Deuda total Ps. 137 mil millones» es la deuda **neta**; la deuda total es Ps. 153.7 mil millones | Corregido |
| 3 | Tabla 1A de Bimbo no cuadra: 8,200 − 1,700 ≠ 7,600; EBITDA US$2,950 m (1A) vs US$3,260 m (1C); ingresos US$20,500 m incompatibles con Ps. 427 mil millones | **Todas las cifras en US$ de Bimbo descartadas** (estimaciones del asistente, no CIQ) |
| 4 | Ventas por segmento FY24/FY25 (p. ej. FY25 suma Ps. 226.8 mil millones vs total 427.0; NA 102.7 vs 44.6% del total) | **Descartadas** (parecen cifras de un semestre rotuladas como anuales); se conservan márgenes y EBITDA |
| 5 | Calificación de Bimbo «N/A» en CIQ | Se mantiene la de la wiki: BBB+ / BBB+ / Baa1; S&P negativa desde 2025-03-20 |
| 6 | EV/EBITDA de la herramienta ≠ EV/EBITDA de la tabla (5 de 6 pares con diferencia de 0.5 a 1.7x) | Reemplazado por el cociente de la tabla (§3) |
| 7 | Razones anuales de CIQ ≠ deuda/EBITDA recalculada (Flowers FY25: 3.13x vs 4.02x; Campbell's FY21: 2.32x vs 2.71x; Mondelez FY21: 2.42x vs 2.72x) | CIQ usa otra base de EBITDA; **no comparar las razones históricas de CIQ con las LTM calculadas**. El «deterioro» de Flowers, Aryzta y Campbell's de FY25 a LTM está en parte inflado por esto |
| 8 | Resumen 1C: orden del ranking equivocado; mediana núcleo 3.79x excluía a Yamazaki; mediana de todos 3.20x en la tabla y 3.35x en el texto | Recalculado (§1-§2) |
| 9 | Arca: acciones diluidas 212.1 m = las de Flowers (repetido); capitalización resuelta a AON | Acciones y capitalización de Arca descartadas |
| 10 | Yamazaki: ingresos FY2025 US$8,773.2 m idénticos a FY2021 | Marcado `[unverified]`; no usar ese año |
| 11 | Nutresa: EV US$50.2 mil millones sobre EBITDA de US$0.83 mil millones = 60x | Descartada (error de conversión de COP) |
| 12 | Mondelez EBITDA FY25 US$4,990 m (margen 13.0%) vs LTM US$6,080 m | Probable partida extraordinaria; no usar FY25 como base `[unverified]` |
| 13 | Tickers de Bimbo, Gruma y Arca mal resueltos en CIQ («Bmvb Immo», «Bevgru Ab», AON) | Repetir con identificador explícito (ver §7) |
| 14 | Referencias numéricas pegadas al texto («Reported 23», «13») | No son fuentes; ignoradas |

## 7. Qué sigue faltando

- **Gruma completa, Bimbo en CIQ estandarizado**, EV/capitalización de Yamazaki y Arca, Moody's, Fitch, historial de calificaciones, composición de deuda por moneda y tasa, costo promedio de la deuda, FFO/deuda, múltiplos históricos (5 y 10 años), P/FCF, rendimiento por dividendo y de FCF, consenso de Bimbo.
- **Cómo repetirlo:** buscar por nombre, no por ticker, y pedir el identificador de Capital IQ que usó. Probar `BMV:BIMBO A` y `BMV:GRUMA B` (con espacio, formato de series de la BMV; sin confirmar) y confirmar el nombre de la entidad antes de bajar datos. Los archivos locales de Capital IQ de Bimbo (`filings/capitaliq/`, `filings/refinitiv/`) ya cubren a Bimbo; usarlos para la base estandarizada.
- Resto de los prompts 2 y 3 (deuda de Bimbo, CEO, clima, valuación, accionistas, M&A, participaciones de mercado) siguen sin correr.
