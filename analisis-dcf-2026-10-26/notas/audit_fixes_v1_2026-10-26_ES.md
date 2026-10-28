# Bitácora de ajustes de auditoría H-01 a H-05 (copia del libro de estados)

**Fecha:** 2026-10-26. **Hecho por:** la IA, a petición de Jorge Alejandro Gaytan: "haz una copia de las proyecciones aplicando lo que creas mejor para los cinco hallazgos".

**Estado:** es una propuesta de la IA. El equipo no ha decidido ningún hallazgo, así que nada de esto entra en `docs/context/memory.md`.

**Uso:** sirve para hacer una segunda valuación y compararla con la del libro original.

**Auditoría de origen:** `.claude/worktrees/bimbo-financial-audit-2021-2030-01a617/model/audit_statements_v1_2026-10-25_ES.md`.

## Qué es original y qué es copia

| | Original (sin cambios) | Copia con ajustes |
|---|---|---|
| Libro EN | `model/BIMBOA_statements_2021-2030_v1.xlsx` | `analisis-dcf-2026-10-26/proyecciones/BIMBOA_statements_2021-2030_v1_auditfix.xlsx` |
| Libro ES | `model/BIMBOA_estados_2021-2030_v1_ES.xlsx` | `analisis-dcf-2026-10-26/proyecciones/BIMBOA_estados_2021-2030_v1_auditfix_ES.xlsx` |
| Constructor de estados | `model/build/build_statements_workbook.py` | `analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix.py` |
| Textos ES y hoja de rastreo | `model/build/statements_es.py` | `analisis-dcf-2026-10-26/build/audit_fix_es.py` (nuevo; solo lo importa la copia) |
| Macro (PIB, inflación, tipo de cambio) | `data/macro/nominal_gdp_growth_2016-2030.xlsx`, construido por `build_macro_gdp.py` | `analisis-dcf-2026-10-26/datos/nominal_gdp_growth_2016-2030_auditfix.xlsx`, construido por `build_macro_gdp_auditfix.py` |

- Los dos constructores copia se generaron desde los originales con reemplazos exactos de texto. Cada reemplazo verificó que el texto original apareciera una sola vez.
- Los generadores están en el scratchpad de la sesión: `make_macro_fix.py` y `make_stmt_fix.py`.
- Cada fórmula nueva lleva en su nota "Audit fix H-0x".
- La copia agrega una hoja **Audit_fixes** (en ES, **Ajustes_auditoría**) junto al README. Tiene un renglón por hallazgo y ligas vivas a las celdas que cambian.
- **Aviso:** en la copia, la hoja Methodology sigue describiendo los métodos originales en esos puntos. Para los cinco puntos, la hoja Audit_fixes es la que manda.

**Cómo reconstruir la copia** (desde la raíz del worktree):

```bash
python analisis-dcf-2026-10-26/build/build_macro_gdp_auditfix.py analisis-dcf-2026-10-26/datos/nominal_gdp_growth_2016-2030_auditfix.xlsx
```
```bash
powershell -NoProfile -ExecutionPolicy Bypass -File valuation/build/recalc_excel.ps1 <ruta Windows del macro auditfix>
```
```bash
cd model/build && python build_statements_workbook_auditfix.py && python build_statements_workbook_auditfix.py --lang es
```

Al final se recalculan los dos libros copia con el mismo `recalc_excel.ps1`.

**Verificación** (2026-10-26):
- 0 errores de fórmula en EN y en ES.
- Cuadres en 0 en todos los años FY2021-FY2030E.
- Ninguna fila ni columna inmovilizada.
- 9,753 celdas numéricas idénticas entre EN y ES.
- El libro EN original conserva su fecha (2026-10-25 16:16).
- El libro ES original tiene fecha 2026-10-26 19:42, anterior a esta copia. Sus 9,716 números coinciden exactamente con el EN original.

## Ajustes, uno por uno

### H-01: reestructura e integración FY2026E desde el 1S26, no desde la mezcla 2025

- **Antes.** Los gastos FY2026E sin D&A (`Assumptions` ond26 = 171,818) se repartían con la mezcla por naturaleza de 2025.
  - Eso daba reestructura 3,846, integración 532 y MEPP 27. Con la parte no recurrente de Otros (60), sumaban 4,465.
  - Esos 4,465 se borran de la base desde FY2027E.
  - La línea de integración del ER tenía otra cifra: 539.8.
- **Después.**
  - `p_rs = 2 × 1,708.999 = 3,418.0`
  - `p_ig = 2 × 366.681 = 733.4`
  - `p_mp = 2 × (−14.032) = −28.1`
  - Todos `[sourced]` BMV jun-26 p.81-82 × 2 `[assumption]`: el segundo semestre igual al primero.
  - Los renglones recurrentes se reparten con `(ond26 − p_mp − p_ig − p_rs) × o_k / Σ o_recurrentes`.
  - La línea de integración del ER 2026E ahora es `= p_ig` (733.4). Distribución y administración se reparten con lo que queda.
- **Fórmulas.**
  - `p_rs` antes: `=B{ond26}*B{o_rs}/(Σ todos)`. Después: `=2*B{h1_rs}`.
  - `a_int` antes: `=B{a_g}*IS!F11/(F9+F10+F11)`. Después: `=B{p_ig}`.
- **Efecto.**
  - La base recurrente 2026 sube unos 282.
  - Margen UAFIDA 2027E-2030E: de 15.12% a 15.06%, contando también H-02, que casi no mueve el margen.
  - El total FY2026E no cambia: margen UAFIDA 2026E sigue en 14.84%.
- **En contra.** El 3T26 menciona "menores gastos de reestructura", así que B podría sobrestimar la reestructura 2026. Cuando consigan el BMV de septiembre 2026, se sustituye por 9M26 real.

### H-02: PIB nominal 2026 de KOR, KAZ, MAR y UKR

- **Antes.** Su crecimiento 2026 salía de los niveles guardados en Capital IQ: 22.4%, 28.1%, 10.5% y 22.3%. Son probables saltos de serie.
  - PIB EAA 2026 = 7.86%.
  - Ratio orgánico EAA = 4.41% / 7.86% = 0.561.
- **Después.** En la hoja macro `Data`, columna J, para esos cuatro países en 2026: `=(1+L)*(1+IAS29_test!N{fila})-1`.
  - La columna L es el crecimiento real 2026 de Capital IQ `[sourced]`:

    | País | Real | Fuente |
    |---|---|---|
    | KOR | 3.16% | E4 L202 |
    | KAZ | 4.48% | E3 L282 |
    | MAR | 4.69% | E5 L123 |
    | UKR | 0.85% | E3 L122 |

  - La inflación como aproximación del deflactor es `[assumption]`.
  - Los niveles 2026 quedan como están, así que el crecimiento 2027-2030 no cambia.
  - Resultado: PIB EAA 2026 = 6.99%; ratio EAA = **0.6307**.
- **Efecto.**
  - Crecimiento orgánico EAA 2027E: de 3.49% a 3.92%.
  - Ventas 2027E: de 446,942 a 447,170.
  - Ventas 2030E: de 498,865 a 499,905.
  - g terminal: de 2.706% a 2.761%.
- **Sigue abierto.** UKR 2027 continúa como `[unverified]`; su peso en EAA es 0.48%.

### H-03: depreciación de PP&E = tasa × PP&E inicial desde FY2027E

- **Antes.** La parte de PP&E de la D&A se movía con `ppd27/ppd26`, pero sobre una base 2026E (ppe_d = 17,254) que incluye deterioros y otras partidas no monetarias del 9M26. Así se aplicaban 17,399 en lugar de los 16,731 decididos.
- **Después.**
  - `dp27 = dp26 / ppe_d × ppd27`.
  - `q27_da = rou27 + amort + (oda26 − rou_d − amort) / ppe_d × ppd27`.
  - Lo mismo en 2028-2030.
  - La parte de PP&E de la D&A es exactamente `ppd_t = 10.54% × PP&E inicial` `[calc]`.
- **Efecto.**
  - La UAFIDA no cambia.
  - La D&A de PP&E baja unos 668 en 2027E.
  - El PP&E neto sube porque se deprecia menos: Dic-30 de 185,268 a 187,776, contando también H-05 vía capex por ventas.
  - FY2026E no cambia.

### H-04: costo de la deuda = ritmo real 2026E

- **Antes.** `kd` = 6.5% `[sourced]` 3T26 p.6, que es el costo que reporta Bimbo.
- **Después.** `kd = (c_int − l_int) / ((deuda Dic-25 + deuda Dic-26)/2) / fxf26` = (12,223 − 2,137) / ((153,663 + 151,250)/2) / 0.9952 = **6.648%** `[calc]`.
  - Es la tasa que, en la misma fórmula de 2027E, reproduce el interés neto 2026E.
  - Ese interés es 9M26 real + 4T26 = 3T26.
  - El 6.5% queda como referencia en `kd_rep`.
- **Por qué no 7.47% (la propuesta del auditor).** Es una tasa bruta: los 955 de otros costos financieros de 2025 los compensaban 897 de ingresos por intereses, y el modelo deja esos ingresos en 0.
- **Efecto.**
  - Intereses 2027E: de 12,091 a 12,419 (+328). Unos 103 de esos vienen de los arrendamientos de H-05.
  - Ningún efecto en el FCFF.

### H-05: arrendamientos crecen con las ventas desde FY2027E

- **Antes.** Derechos de uso (32,757), pasivo por arrendamiento, depreciación de derechos de uso (6,142) e interés (2,137) se mantenían fijos todos los años.
- **Después.**
  - `rou_t = 6,142 × ventas_t / ventas 2026E` y `li_t = 2,137 × ventas_t / ventas 2026E`.
  - En el BG, derechos de uso y pasivo (corto y largo plazo) = año anterior × ventas_t / ventas_t−1.
  - FE: pagos de arrendamiento = −(rou_t + li_t) − Δ derechos de uso + Δ pasivo. Así Cuadres cierra.
  - PP&E: se resta `rou_t` en lugar de 6,142.
  - FY2026E no cambia.
- **Efecto.**
  - Depreciación de derechos de uso 2030E: 7,196 (+1,054).
  - Interés de arrendamientos 2030E: 2,504 (+367).
  - Derechos de uso Dic-30: 38,379 (+5,622).
  - Pagos de arrendamiento 2030E: 9,626 (+1,347).
  - La UAFIDA no cambia; la UAIIR baja.
- **En contra.** La D&A del 1S26 bajó contra el 1S25: hoy no se ve crecimiento de arrendamientos.

## Efecto conjunto (original → copia) `[calc]`

Cifras en millones de pesos y margen en % de ventas. FY2026E es igual en los dos libros.

| | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|
| Ventas | 446,942 → 447,170 | 465,382 → 465,852 | 483,639 → 484,386 | 498,865 → 499,905 |
| UAFIDA | 67,589 → 67,328 | 70,377 → 70,141 | 73,138 → 72,931 | 75,441 → 75,268 |
| Margen UAFIDA | 15.12 → 15.06 | 15.12 → 15.06 | 15.12 → 15.06 | 15.12 → 15.06 |
| D&A | 25,716 → 25,343 | 26,404 → 26,343 | 27,123 → 27,369 | 27,870 → 28,375 |
| UAIIR | 41,872 → 41,985 | 43,973 → 43,797 | 46,015 → 45,562 | 47,571 → 46,893 |
| Margen UAIIR | 9.37 → 9.39 | 9.45 → 9.40 | 9.51 → 9.41 | 9.54 → 9.38 |
| Intereses | 12,091 → 12,419 | 12,243 → 12,669 | 12,362 → 12,883 | 12,431 → 13,032 |
| Utilidad neta controladora | 16,832 → 16,695 | 19,339 → 18,932 | 20,555 → 19,896 | 21,490 → 20,626 |
| Margen neto controladora | 3.77 → 3.73 | 4.16 → 4.06 | 4.25 → 4.11 | 4.31 → 4.13 |
| Caja Dic | 18,170 → 17,412 | 24,749 → 23,029 | 32,143 → 29,235 | 40,388 → 36,090 |

**Prueba de reinversión de g:**

| | Original | Copia |
|---|---|---|
| g | 2.706% | 2.761% |
| RONIC FY2028E-30E | 24.95% | **15.52%** |
| ROIC 2030E | 9.06% | 8.77% (WACC 10.32%) |

- La caída del RONIC es el cambio más grande para la valuación. El capital invertido ahora crece más (derechos de uso, y PP&E con menos depreciación), mientras la UAIIR crece menos.
- El RONIC sigue arriba del WACC: +5.2 pp, antes +14.6 pp.

## Lo que no se hizo

- No se corrió la valuación con la copia. El DCF es el siguiente paso.
- No hay commit. No se modificó ningún archivo original.
