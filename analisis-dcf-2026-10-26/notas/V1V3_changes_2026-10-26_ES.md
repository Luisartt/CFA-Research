# V-1 y V-3 aplicados en copia (decisiones del equipo, 2026-10-26)

No se corrió el DCF. Los originales no se tocaron. No hay commit.

## Archivos nuevos

| Copia | Proyecciones de origen |
|---|---|
| `analisis-dcf-2026-10-26/proyecciones/BIMBOA_statements_2021-2030_v1_V1V3.xlsx` y `analisis-dcf-2026-10-26/proyecciones/BIMBOA_estados_2021-2030_v1_V1V3_ES.xlsx` | Proyecciones del equipo (originales) |
| `analisis-dcf-2026-10-26/proyecciones/BIMBOA_statements_2021-2030_v1_auditfix_V1V3.xlsx` y `analisis-dcf-2026-10-26/proyecciones/BIMBOA_estados_2021-2030_v1_auditfix_V1V3_ES.xlsx` | Copia con los ajustes de auditoría H-01 a H-05 |

- Generadores: `analisis-dcf-2026-10-26/build/build_statements_workbook_V1V3.py` y `analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix_V1V3.py`, copias exactas de sus originales más los cambios de abajo.
- Textos en español y hoja Metodología: `analisis-dcf-2026-10-26/build/v1v3_es.py`.
- Evidencia de V-1: `analisis-dcf-2026-10-26/evidencia/BIMBOA_FX_premium_evidence_v1.xlsx`.

## Qué cambió (solo la hoja Assumptions; los estados financieros no cambian)

**V-1. Depreciación del peso a perpetuidad.**
- El cambio de largo plazo del USD/MXN (`drT`) pasa de la inflación 2030 de Capital IQ (0.48% al año) a 1 + 1.7% [assumption], la base del equipo.
- Se agregan, como fórmulas vivas, los dos soportes:
  - Breakeven de M-Bono/Udibono contra Tesoro/TIPS: 1.73% [calc].
  - Paridad relativa entre la encuesta Banxico (3.70%) y la meta de la Fed (2%): 1.67% [calc].
- Sensibilidades de g a 1.0% y 2.3%, más la base anterior como referencia.
- América Latina y EAA siguen por paridad de poder de compra; el equipo no las cambió.
- El tramo explícito FY2027E-FY2030E sigue con la trayectoria de Capital IQ (1.85% al año), que es congruente con 1.7%.

**V-3. RONIC FY2026E-FY2030E en una sola moneda (opción B).**
- Fórmula: (NOPAT FY2030E a tipos de cambio FY2026E − NOPAT FY2026E) / (capital invertido dic-30 − dic-26).
- El NOPAT FY2030E se pasa a tipos de cambio FY2026E con el factor cambiario acumulado de las ventas: el producto de (1 + crecimiento en MXN) / (1 + crecimiento del negocio).
- Se agregan dos renglones:
  - Control sin la reestructura FY2026E.
  - Sensibilidad de la opción A (RONIC = WACC).
- La medición anterior queda como referencia.

## Resultados [calc]

| Concepto | Proyecciones del equipo | Copia de auditoría |
|---|---|---|
| g antes (inflación 2030) | 2.71% | 2.76% |
| **g con V-1 (1.7%)** | **3.47%** (negocio 2.65% + tipo de cambio 0.82%) | **3.53%** (2.71% + 0.82%) |
| g con 1.0% / 2.3% | 3.03% / 3.85% | 3.09% / 3.91% |
| g menos crecimiento FY2030E en MXN | +0.33 pp (antes −0.44) | +0.33 pp (antes −0.44) |
| Factor cambiario acumulado 2027-2030 | 1.0416 | 1.0417 |
| RONIC anterior (2028-2030, convertido) | 24.95% | 15.52% |
| **RONIC V-3 opción B (base literal)** | **26.98%** | **17.51%** |
| RONIC V-3 sin reestructura FY2026E | 13.91% | 9.30% |
| WACC de referencia | 10.32% | 10.32% |
| ROIC FY2030E | 9.06% | 8.77% |
| Reinversión que necesita g con el RONIC base | 12.9% del NOPAT | 20.2% |
| Reinversión que necesita g si RONIC = WACC | 33.6% | 34.2% |
| Reinversión neta real FY2030E | 16.2% | 22.1% |

## Lo que el equipo tiene que decidir

1. **El año base del RONIC.**
   - El EBIT FY2026E incluye la reestructura registrada en 9M26, y FY2030E no tiene ninguna. Eso infla el cambio del NOPAT.
   - Con la base literal, el RONIC **sube** (27.0% / 17.5%). Sin la reestructura **cae** a 13.9% / 9.3%. En la copia de auditoría eso queda por debajo del WACC.
   - La regla del asesor ("sin partidas no recurrentes") apunta a quitarla.
   - En contra: Bimbo registró reestructura en 1S25 (1,764) y en 1S26 (1,709) [sourced] BMV jun-26 p.82, así que se puede argumentar que es recurrente; falta revisar más años antes de afirmarlo.
2. **Reinversión en el valor terminal.** Con g de 3.5% y RONIC = WACC, el NOPAT terminal tendría que reinvertir alrededor de 34%, contra 16-22% en FY2030E. La elección entre la opción A y la B mueve el valor terminal.
3. **La g sube con V-1.** Pasa de 2.71% a 3.47%, porque ahora los flujos llevan la misma depreciación que ya cobra la tasa. Ahora g queda 0.33 pp arriba del crecimiento FY2030E en MXN (antes 0.44 pp abajo).

## Pendientes y advertencias

- `valuation/valuation.yaml` sigue con g = 0.0271. No se actualizó porque no se corrió el DCF.
- La hoja Metodología se actualizó en los renglones `drT` y `ronic`. El Glosario no se revisó.
- Verificación:
  - 0 errores en los cuatro libros y la hoja Checks en 0.
  - EN = ES en todos los números.
  - 0 celdas cambiadas en los estados frente a su libro de origen.

## Cómo reconstruir

```
python analisis-dcf-2026-10-26/build/build_statements_workbook_V1V3.py
python analisis-dcf-2026-10-26/build/build_statements_workbook_V1V3.py --lang es
python analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix_V1V3.py
python analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix_V1V3.py --lang es
powershell -NoProfile -ExecutionPolicy Bypass -File valuation/build/recalc_excel.ps1 <ruta Windows de cada libro>
```

## Actualización 2026-10-26: EBIT FY2026E sin reestructura (decisión del equipo)

- La base del RONIC usa ahora el EBIT FY2026E sin reestructura (renglón nuevo `ebit26x` = EBIT del ER + reestructura FY2026E) [calc]. La reestructura se trata como no recurrente, según la regla del asesor.
- Montos de reestructura quitados:
  - Proyecciones del equipo: 3,846, estimado con la mezcla FY2025 (pendiente H-01).
  - Copia de auditoría: 3,418, real 1S26 x 2.
- **El estado de resultados no cambia.** Conserva el gasto que Bimbo efectivamente registró, para que los estados sigan cuadrando con lo reportado. El ajuste vive solo en la base de valuación.

| | Proyecciones del equipo | Copia de auditoría |
|---|---|---|
| EBIT FY2026E sin reestructura | 41,575 | 41,147 |
| **RONIC V-3 (base nueva)** | **13.91%** | **9.30%** |
| RONIC con el EBIT del ER (base anterior, control) | 26.98% | 17.51% |
| RONIC menos WACC (10.32%) | +3.59 pp | **−1.02 pp** |
| Reinversión que necesita g con el RONIC base | 25.0% del NOPAT | 38.0% |
| Reinversión neta real FY2030E | 16.2% | 22.1% |

- En la copia de auditoría el RONIC queda por debajo del WACC: crecer destruye valor.
- En ambas, la reinversión que exige g es mayor que la que proyectan FY2030E.
- Integración (532 / 733) y planes multipatronales (27 / −28) en FY2026E siguen dentro del EBIT. El equipo no ha decidido si también se quitan.

## Actualización 2026-10-26 (2): también salen integración y planes multipatronales (decisión del equipo)

- `ebit26x` = EBIT del ER + reestructura + integración + planes de pensiones multipatronales FY2026E [calc]. El ER no cambia.
- Montos quitados:
  - Proyecciones del equipo: reestructura 3,846 + integración 532 + planes 27, estimados con la mezcla FY2025 (pendiente H-01).
  - Copia de auditoría: 3,418 + 733 − 28, real 1S26 x 2.
- La sección anterior queda superada por esta.

| | Proyecciones del equipo | Copia de auditoría |
|---|---|---|
| EBIT FY2026E sin partidas no recurrentes | 42,134 | 41,852 |
| **RONIC V-3 (base nueva)** | **12.01%** | **7.61%** |
| RONIC con el EBIT del ER (control) | 26.98% | 17.51% |
| RONIC menos WACC (10.32%) | +1.69 pp | **−2.72 pp** |
| Reinversión que necesita g con el RONIC base | 28.9% del NOPAT | 46.4% |
| Reinversión si RONIC = WACC (opción A) | 33.6% | 34.2% |
| Reinversión neta real FY2030E | 16.2% | 22.1% |

## Actualización 2026-10-26 (3): reinversión terminal = g / WACC (decisión del equipo, V-3 opción A)

Renglones nuevos en Assumptions, después del bloque del RONIC [calc]:

| | Proyecciones del equipo | Copia de auditoría |
|---|---|---|
| g | 3.47% | 3.53% |
| Reinversión terminal g / WACC | 33.6% | 34.2% |
| NOPAT FY2031E = NOPAT FY2030E x (1 + g) | 33,120 | 32,666 |
| FCFF FY2031E = NOPAT x (1 − reinversión) | 21,977 | 21,497 |
| Reinversión terminal menos reinversión FY2030E | +17.5 pp | +12.1 pp |

- **Consecuencia algebraica:** con esta reinversión, Gordon = FCFF / (WACC − g) = NOPAT FY2031E / WACC. **g deja de mover el valor terminal**, salvo por el NOPAT del primer año, y la subida de g por V-1 ya no sube el precio.
- `valuation/valuation.yaml` no tiene un campo de reinversión terminal. El motor del DCF tendrá que tomar este FCFF terminal, o adaptarse, cuando se corra.
- La tasa de impuesto del NOPAT es la operativa de la proyección (32.7%), no el 30% del WACC (hallazgo V-6, abierto).

## Actualización 2026-10-26 (4): impuesto de valuación 30% (V-6), insumos del DCF y traslado a esta carpeta

- `rT_tax` = 30% [assumption], decisión del equipo (V-6): la tasa legal, igual que el WACC. Cambian todos los NOPAT de la valuación, el RONIC y el valor terminal.
  - RONIC V-3: 12.50% (equipo) / 7.91% (auditoría).
  - FCFF terminal FY2031E: 22,864 / 22,364.
- Bloque nuevo "Insumos del DCF", con fórmulas vivas a los estados:
  - FCFF FY2027E-FY2030E = NOPAT + D&A + compras de PP&E − arrendamientos nuevos + capital de trabajo.
  - Equipo: 24,874 / 25,804 / 26,993 / 28,129. Auditoría: 22,660 / 23,604 / 24,635 / 25,864.
  - Alternativa de valor terminal anclada en FY2027E: FCFF FY2028E de 20,125 / 20,023.
- Todo el trabajo se trasladó a `analisis-dcf-2026-10-26/`. Las rutas citadas arriba en esta nota son las anteriores; los archivos están ahora en `build/`, `datos/`, `evidencia/`, `proyecciones/` y `notas/` de esta carpeta. Ver `README_ES.md`.
