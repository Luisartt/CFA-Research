# Auditoría de proyecciones y preparación del DCF (2026-10-26)

Esta carpeta reúne el trabajo de la sesión del 26-oct-2026 con Jorge Alejandro Gaytan:
- Auditoría de las proyecciones (H-01 a H-05).
- Auditoría de la valuación (V-1 a V-6).
- Evidencia de la prima cambiaria.
- Insumos listos para el DCF.

**Reglas que respeta:**
- No modifica nada fuera de esta carpeta.
- Los libros originales del equipo (`model/BIMBOA_statements_2021-2030_v1.xlsx` y su versión ES) no se tocaron.
- `valuation/valuation.yaml` sigue igual.
- El DCF se corrió el 2026-10-27 con aprobación del equipo, dentro de los libros V1V3 de esta carpeta. `valuation/` no se tocó.
- Nada está en commit.

## Estructura

| Carpeta | Contenido |
|---|---|
| `build/` | Generadores (Python/openpyxl). Usan los módulos compartidos de `model/build/` (statements_es, macro_es, methodology_rows, glossary_rows) sin modificarlos |
| `datos/fx_premium/` | Series públicas descargadas con aprobación del equipo: FRED (DEXMXUS, DGS10, DFII10, T10YIE, EXPINF10YR, OECD 10 años MX/EUA, CPI), Banxico SIE CF107 (Bono M y Udibono 10 años) y la Encuesta de Especialistas de Banxico de septiembre 2026 |
| `datos/` | `nominal_gdp_growth_2016-2030_auditfix.xlsx`: macro con el ajuste H-02 |
| `datos/bmv_3t26/` | XBRL de 3T26 de la BMV (30-sep-2026), descargado con aprobación del equipo |
| `puente/` | `BIMBOA_bridge_3Q26_v1.xlsx`: puente del valor de la empresa al valor del capital, al 30-sep-2026 |
| `evidencia/` | `BIMBOA_FX_premium_evidence_v1.xlsx`: ¿el 0.63 es prima o depreciación? |
| `proyecciones/` | Ver la tabla siguiente |
| `notas/` | Bitácoras de cambios: `audit_fixes_v1_2026-10-26_ES.md` (H-01 a H-05) y `V1V3_changes_2026-10-26_ES.md` (V-1, V-3, V-6 e insumos del DCF) |

Libros en `proyecciones/` (cada uno con versión EN y ES):

| Libro | Proyecciones de origen | Ajustes de valuación |
|---|---|---|
| `..._v1_auditfix` | Ajustes de auditoría H-01 a H-05 | Ninguno |
| `..._v1_V1V3` | Las del equipo | V-1, V-3 y V-6 |
| `..._v1_auditfix_V1V3` | Ajustes de auditoría H-01 a H-05 | V-1, V-3 y V-6 |

Las dos valuaciones que el equipo planteó salen de los dos libros V1V3.

## Decisiones del equipo en esta sesión

1. **Copia de auditoría H-01 a H-05.** Se hizo como copia, para hacer dos valuaciones: una con las proyecciones del equipo y otra con los ajustes. El equipo no ha elegido entre las dos.
2. **V-1: depreciación esperada del USD/MXN a perpetuidad de 1.7% al año.** Sensibilidades: 1.0% y 2.3%.
   - Evidencia: breakeven M-Bono/Udibono contra Tesoro/TIPS, 1.73%; paridad relativa con la encuesta Banxico (3.70%) contra la meta de la Fed (2%), 1.67%.
   - El resto del diferencial de 2.30% libre de impago (alrededor de 0.6 pp) es prima y se queda solo en el WACC.
   - Evidencia en contra que el equipo debe conocer: la historia 2001-2016 (el peso se depreció más que la inflación) y la encuesta de tipo de cambio a dos años.
3. **V-3: RONIC FY2026E-FY2030E en una sola moneda (opción B).** El NOPAT FY2030E va a tipos de cambio FY2026E. El EBIT FY2026E de la base excluye las partidas no recurrentes (reestructura, integración y planes multipatronales); el ER las conserva.
4. **Reinversión terminal = g / WACC (opción A, RONIC = WACC a perpetuidad).** Con esto, Gordon = NOPAT del primer año terminal / WACC, y g casi no mueve el valor.
5. **V-6: impuesto de 30% sobre el EBIT en la valuación,** igual al del WACC. El ER conserva su tasa efectiva.
6. **Horizonte explícito FY2027E-FY2030E,** con el valor terminal anclado en FY2031E (NOPAT FY2030E x (1 + g) x (1 - g / WACC)).
7. **V-5: minoritarios a valor de mercado con crecimiento 0%,** porque su base en libros se encoge. El resto del puente se mantiene.
   - **Actualizado 2026-10-26:** la base es la utilidad de 9M26 anualizada (1,820), no 1S26 × 2 (1,814). Valor a mercado: 1,820.7 (9M26 del XBRL, 1,365.5 x 4/3) / 12.94% = 14,066 [calc].

## Resultados clave [calc] (impuesto 30%)

| | Proyecciones del equipo (V1V3) | Copia de auditoría (auditfix_V1V3) |
|---|---|---|
| g (base 1.7%) | 3.47% | 3.53% |
| g con 1.0% / 2.3% | 3.03% / 3.85% | 3.09% / 3.91% |
| RONIC V-3 | 12.50% | 7.91% |
| RONIC menos WACC (10.32%) | +2.18 pp | −2.41 pp |
| ROIC FY2030E | 9.42% | 9.12% |
| Reinversión terminal g / WACC | 33.6% | 34.2% |
| FCFF FY2027E / FY2028E / FY2029E / FY2030E | 24,874 / 25,804 / 26,993 / 28,129 | 22,660 / 23,604 / 24,635 / 25,864 |
| FCFF terminal FY2031E | 22,864 | 22,364 |
| Si FY2027E es el único año explícito: FCFF terminal FY2028E | 20,125 | 20,023 |

**Cómo se calcula el FCFF:**
- FCFF = NOPAT (30%) + D&A + compras de PP&E − arrendamientos nuevos + capital de trabajo.
- Todo con fórmulas vivas a los estados (hojas ER, Balance y Flujos).
- Con IFRS 16, los arrendamientos se tratan como deuda: arrendamientos nuevos = cambio en derechos de uso + su depreciación, y el pasivo por arrendamiento va en la deuda neta.

## DCF corrido (2026-10-27)

El DCF está en la hoja Assumptions de los dos libros V1V3 (generador `build/dcf_rows.py`), con fórmulas vivas a los FCFF, al terminal y al puente al 31-dic-2026.
- Descuento a mitad de año, incluido el valor terminal, igual que el motor v3.
- Solo Gordon.
- Verificación: 0 errores; Checks en 0; el terminal es igual a NOPAT FY2031E / WACC; el precio en forma cerrada cuadra; EN = ES; ninguna celda anterior cambió.

| [calc], Ps millones salvo por acción | Proyecciones del equipo | Copia de auditoría |
|---|---|---|
| Valor presente FCFF FY2027E-FY2030E | 87,009 | 79,552 |
| Valor presente del terminal | 236,655 (73% del valor de la empresa) | 233,410 (75%) |
| Valor de la empresa al 31-dic-2026 | 323,664 | 312,962 |
| − Total a restar | 196,167 | 196,167 |
| Valor del capital al 16-oct-2026 (x 0.9750) | 124,306 | 113,873 |
| **Valor por acción** | **Ps 29.01** | **Ps 26.58** |
| Frente a Ps 58.60 | −50.5% | −54.6% |
| WACC 9.82% / 10.82% | Ps 32.84 / 25.55 | Ps 30.34 / 23.17 |
| Depreciación 1.0% / 2.3% | Ps 28.78 / 29.21 | Ps 26.35 / 26.77 |

Diagnóstico [calc] (equipo):
- Valor de la empresa / EBITDA FY2026E: 5.1x. El mercado está en 7.2x (453,686 / 63,299).
- El terminal equivale a 4.4x el EBITDA FY2030E (75,441).
- WACC que iguala Ps 58.60 con la regla g / WACC: 7.41%.
- Si el terminal conservara la reinversión de FY2030E (15.5%, RONIC implícito 22%), el valor sería Ps 43.71.

## Pendientes antes de correr el DCF (decisiones del equipo)

1. ~~Horizonte explícito.~~ **Decidido 2026-10-26: FY2027E-FY2030E, con el valor terminal anclado en FY2031E** (FCFF terminal 22,864 equipo / 22,364 auditoría). Los renglones de la alternativa FY2028E quedan solo como referencia.
2. **Puente al valor del capital (V-5).** En v3 restaban Ps 8.60 por acción (37,054 a dic-25).
   - **Decidido 2026-10-26:** los minoritarios se valúan con crecimiento 0%: utilidad 1,814 / ke 12.94% − libros 743 = 13,276, Ps 3.08 [calc]. Antes eran 17,500 con 3%. Razón: su base en libros se encoge.
   - **Sustituido 2026-10-26:** la base es la utilidad de 9M26 × 4/3 = 1,820. Minoritarios a mercado: 14,066 [calc] (9M26 del XBRL).
   - El resto de las partidas se queda como está.
   - Advertencia: en las proyecciones, la utilidad de los minoritarios crece con las ventas. El puente no supone crecimiento y los flujos sí.
   - **Puente actualizado 2026-10-26, todo al 30-sep-2026,** en `puente/BIMBOA_bridge_3Q26_v1.xlsx` (generador `build/build_bridge_3q26.py`), con fórmulas vivas.
     - Fuentes: reporte de resultados 3T26 y el XBRL de 3T26 de la BMV, descargado con aprobación del equipo a `datos/bmv_3t26/` desde el sitio de inversionistas de Grupo Bimbo.

     | Concepto | Ps millones | Fuente |
     |---|---|---|
     | Deuda | 152,802 | Reporte 3T26 p.8 |
     | Arrendamientos | 34,040 | Reporte 3T26 p.8 |
     | Caja | 17,459 | Reporte 3T26 p.8 |
     | **Deuda neta con arrendamientos** | **169,383** | La deuda neta sin arrendamientos cuadra con la reportada, 135,343 (p.6) |
     | Minoritarios a mercado: 1,365.5 (9M26) x 4/3 / 12.94% | 14,066 | XBRL p.13; libros 610 |
     | Partidas tipo deuda | 15,972 | XBRL p.12, 57-58, 63-64; 18,135 a jun-26 |
     | Asociadas (se suman) | 6,533 | XBRL p.11 |
     | Acciones netas de recompra (millones) | 4,284.6 | XBRL p.24: 4,304.7 emitidas − 20.2 recompradas |

     - **Total a restar del valor de la empresa: 192,888, Ps 45.02 por acción.**
     - La medida comparable al "Ps 8.60" de v3 (partidas tipo deuda + prima de minoritarios) baja a **Ps 6.87**.
     - Partidas tipo deuda: bajan 2,163 frente a jun-26. Los derivados netos pasan de 1,864 a 486, los beneficios a empleados después de impuestos de 4,279 a 3,931 y las provisiones de 10,724 a 10,348.
     - MEPP y compensación diferida siguen sin revelarse por separado; se reparten con las proporciones de dic-25 [assumption], ahora con fórmula viva.
     - El WACC usa 4,294.9 millones de acciones (29-jul-2026); el puente usa 4,284.6 (30-sep-2026). La diferencia es 0.24%.
3. **Ratio terminal de Norteamérica (V-2).** 0.17x sale solo de 9M26; la historia da 1.03, −0.83 y −0.80.
   - **Decidido 2026-10-27: se mantiene 0.17 (9M26) para FY2027E-FY2030E y para el terminal.** Es la tesis del equipo de ganancia de participación en Norteamérica.
   - **Revisión 2026-10-27:** el mismo ratio (Assumptions B113) mueve las ventas de Norteamérica de FY2027E a FY2030E y también g.
   - Con la regla g / WACC, el valor terminal es proporcional al NOPAT FY2031E. El ratio pesa por el periodo explícito; g solo entra con un año de (1 + g).
   - Sensibilidad en una copia temporal del libro V1V3 del equipo [calc], en Ps millones:

     | Ratio | g | NOPAT FY2030E | NOPAT FY2031E | Cambio frente a la base | RONIC |
     |---|---|---|---|---|---|
     | −0.13 (historia 2023-25) | 3.03% | 32,232 | 33,208 | −3.6% | 7.8% |
     | 0 | 3.22% | 32,702 | 33,756 | −2.0% | 10.0% |
     | **0.168 (base, 9M26)** | **3.47%** | **33,300** | **34,456** | — | **12.5%** |
     | 0.5 | 4.00% | 34,525 | 35,906 | +4.2% | 17.3% |
     | 1.0 | 4.87% | 36,475 | 38,252 | +11.0% | 23.8% |

   - Con el ratio 0.168, Norteamérica crece 0.7-0.9% al año en USD (2027-30). La categoría de pan en EUA va de −3% a 0% nominal (volumen −2% a −4%, precio/mezcla +1-2% [assumption], `research/industry.md`). El ratio implica crecer unos 0.7-3.9 pp al año por encima de la categoría.
   - El 9M26 de Norteamérica no descuenta Stone House (2-jun-2025, sin tamaño revelado; hoja Organic_pass), así que puede no ser 100% orgánico.
4. ~~Fecha de valuación y stub.~~ **Decidido 2026-10-27: opción B.**
   - Se valúa al 31-dic-2026: flujos FY2027E-FY2030E más el valor terminal, y el puente con el balance proyectado de FY2026E.
   - El valor del capital se trae al 16-oct-2026 con ke: dividir entre (1 + ke)^(76/365). Del 16-oct al 31-dic hay 76 días.
   - El puente real al 30-sep (`puente/`) queda como referencia y para cuadrar el balance proyectado.
   - **Decidido 2026-10-27:** las partidas tipo deuda (15,972) y las asociadas (6,533) se mantienen en su valor reportado al 30-sep-2026.
   - **Puente al 31-dic-2026E**, construido con fórmulas vivas en la hoja Assumptions de los dos libros V1V3 (generador `build/bridge_dec26_rows.py`). Es igual en ambos, porque los ajustes de auditoría empiezan en FY2027E:

     | Concepto | Ps millones [calc] | Origen |
     |---|---|---|
     | Deuda bruta | 151,250 | Balance FY2026E |
     | Arrendamientos | 34,790 | Balance FY2026E |
     | Caja | 13,379 | Balance FY2026E |
     | **Deuda neta con arrendamientos** | **172,661** | 169,383 reportada al 30-sep |
     | Minoritarios a mercado | 14,066 | 9M26 x 4/3 / ke |
     | Partidas tipo deuda | 15,972 | Al 30-sep; fórmula viva en `puente/`, leída al construir |
     | Asociadas (se suman) | 6,533 | Al 30-sep, XBRL p.11 |
     | **Total a restar** | **196,167** | |
     | Acciones (millones) | 4,284.6 | 30-sep; sin recompras en 4T26 (equipo 2026-10-23) |
     | Días del 16-oct al 31-dic | 76 | Fórmula de fechas |
     | Factor de descuento con ke | 0.9750 | 1 / (1 + ke)^(76/365) |

     - Por qué la deuda neta proyectada al 31-dic es 3,278 mayor que la reportada al 30-sep: la caja proyectada es 4,080 menor y los arrendamientos se mantienen en FY2025.
     - En los XBRL de 2023-2025, la deuda financiera neta de caja también subió de septiembre a diciembre los tres años, con el tipo de cambio pesando mucho.
     - Cómo se relacionan los dos puentes: el de `puente/` (30-sep) queda como referencia y el DCF usa este.
5. **Motor del DCF.** El motor actual (`valuation/build/dcf_core.py`) proyecta desde `model/drivers.yaml` (v3), no desde estos estados. El DCF nuevo debe tomar los FCFF de estos libros con fórmulas vivas.
6. **WACC.** Se usa el 10.32% de v3 como referencia; V-1 no lo cambia. Falta que el equipo lo confirme.
   - **Verificado 2026-10-27:** los 39 países de la tabla de riesgo país de `valuation/BIMBOA_WACC_v3.xlsx` coinciden con `ctrypremJuly26.xlsx` de Damodaran (actualización del 1-jul-2026, spreads corregidos el 9-jul). México: Baa3, spread de impago 1.75%, CRP 2.72%.
   - `valuation/inputs/wacc_inputs.yaml` todavía guarda la tabla de enero (Baa2, 1.62%, 2.46%). Está fuera de esta carpeta y no alimenta el WACC v3.
   - **Estructura de capital:** se mantiene la D/E actual de 0.743. Con el puente de 3T26 da 0.744.
     - Supuesto de Jorge (2026-10-27, provisional): Bimbo no desapalancará y podría crecer de forma inorgánica.
     - Contraste: la D/E de Damodaran para Food Processing (ene-2026) es 0.37 global, 0.44 EUA, 0.35 Europa y 0.38 emergentes. Bimbo está por encima, no por debajo.
   - **Beta: decidido 2026-10-27, se mantiene la beta global de industria 0.53** (Damodaran Food Processing Global, ene-2026). Las demás opciones quedan como sensibilidad:

     | Opción | Beta desapalancada | WACC [calc] |
     |---|---|---|
     | Industria global (actual) | 0.53 | 10.32% |
     | Bottom-up ponderada por región con EBITDA 2025 (EUA 0.457, emergentes 0.560, Europa 0.367; Damodaran ene-2026) | 0.512 | 10.26% |
     | Igual, con ventas | 0.490 | 10.18% |
     | Regresión de Bimbo a 5 años, ajuste Blume | 0.580 | 10.51% |
7. **Fuente no encontrada.** El 35.89 / 23.13 que citó Diego sigue sin fuente [unverified].
8. **Transcripciones faltantes.** Las de 4T25 y 2T26 se necesitan para respaldar eficiencias.

## Cómo reconstruir (desde la raíz del worktree)

```
python analisis-dcf-2026-10-26/build/build_bridge_3q26.py                            (y recalcular antes de los V1V3)
python analisis-dcf-2026-10-26/build/build_macro_gdp_auditfix.py analisis-dcf-2026-10-26/datos/nominal_gdp_growth_2016-2030_auditfix.xlsx
python analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix.py            (y --lang es)
python analisis-dcf-2026-10-26/build/build_statements_workbook_V1V3.py                (y --lang es)
python analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix_V1V3.py       (y --lang es)
python -I analisis-dcf-2026-10-26/build/build_fx_premium_evidence.py
powershell -NoProfile -ExecutionPolicy Bypass -File valuation/build/recalc_excel.ps1 <ruta Windows de cada libro>
```

El libro macro se recalcula antes de construir los estados de auditoría.

## Verificación (2026-10-26)

- Los libros reubicados reproducen exactamente los números previos al traslado.
- Los libros V1V3 tienen 0 errores y la hoja Checks en 0.
- EN = ES en todos los números.
- 0 celdas cambiadas en los estados frente a su libro de origen.
