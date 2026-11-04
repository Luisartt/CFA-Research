# Handoff: report v33, para seguir en la laptop de Luisart (2026-11-04)

> Pega este archivo como primer mensaje de tu sesión. Lo escribió la sesión de Jorge del 2026-11-04.
> Detalle completo de cada paso: `docs/context/thesis-journal.md` (entradas del 2026-11-04) y `docs/context/ai-use-log.md`.

---

## 1. Antes de empezar: los archivos todavía no están en GitHub

Todo lo de abajo está **sin commit** en la laptop de Jorge: worktree `.claude/worktrees/dcf-balance-general-dd4b56`, rama `tp12m-final-2026-10-28`. Para que Luisart lo tenga, Jorge tiene que hacer commit y push de esa rama, o mandarle los archivos. Sin eso, la sesión de Luisart no ve la v33.

Archivos que Luisart necesita:

| Archivo | Qué es |
|---|---|
| `report/v33/BIMBOA_report_v33.docx` (+ `.pdf`) | Reporte en inglés con todas las correcciones de abajo |
| `report/v33/BIMBOA_reporte_es_v33.docx` (+ `.pdf`) | Reporte en español, mismas correcciones |
| `report/v32/` | Originales de Luisart, sin tocar (para comparar) |
| `analisis-dcf-2026-10-26/precio-objetivo/verificacion-v32/BIMBOA_TP12m_v2_copia_verif_v32.xlsx` | Copia de verificación: TP12m_v2 + B538 `=B390` (impuesto del NOPAT 32.715%) + B601 `=B240` (g de minoritarios 4.404%) + precio 64.85. Reproduce la v32 al centavo |
| `docs/context/*` | Bitácoras, decisiones (`memory.md`), este handoff |

**Reglas:** el TP12m_v2 no se modifica (sha1 `54e71c93b1709a5ae7be6deb0330d9417b14aa5e`, sin cambios). Las mediciones se hacen en la copia de verificación. Las cifras no se inventan y todas llevan etiqueta. Un punto a la vez: Jorge cierra cada punto. El equipo decide la tesis, la calificación, el objetivo y la puntuación de los riesgos. No se hace commit ni push sin el sí del equipo.

## 2. Cifras base (copia de verificación) [calc]

| | Valor |
|---|---|
| Objetivo a 12 meses | MXN 58.54 |
| DCF | MXN 52.92 |
| Banda | BUY abajo de 45.50 / SELL arriba de 62.41 |
| RONIC terminal | 15.17% |
| Precio | 64.85 (27-oct-2026) |
| Regla | Da SELL. **El equipo califica HOLD** como juicio (decisión final, `memory.md`) |

## 3. Lo que ya está hecho en la v33 (inglés y español)

Todo validado contra la v32: 1350 párrafos iguales. EN tiene 16 páginas con el apéndice en la p.12, así que el cuerpo es exactamente de 10 páginas. ES tiene 17 páginas con el apéndice en la p.13 (cuerpo de 11).

| Punto | Cambio |
|---|---|
| Punto 1 (HOLD) | Texto nuevo del HOLD (`report/sections/hold-rating-override_v1.md`). Última fila de la Tabla 4: 15.30% → 61.16, banda 47.64-64.96 |
| Punto 3 (etiquetas del ROIC) | ROIC tangible histórico recalculado al 32.7%: FY2022 17.0%, FY2023 16.5%, FY2024 13.3%, FY2025 11.4%, promedio 14.6% (Assumptions B690-B696). Cambia en pp.5-7 y 10, Tablas 12 y 13 y la fila R3 ("-11.7 (RONIC 11.4%)"). Los valores de sensibilidad (46.85 / 57.06 / −11.69) **no cambian**: Excel los confirma con el número de acciones fijo |
| Alan 1 (ke fijo) | p.8, después de "so the rule gives SELL": si el ke se mueve con el WACC, el rendimiento optimista baja a +7.5%, todavía debajo de 11.76%. La regla sigue en SELL |
| Alan 3 (reestructuración) | R7: la reestructuración se trata como no recurrente aunque Bimbo la reporta cada año desde FY2019 (MXN 3,908 millones en FY2025, 0.92% de ventas; Grupo Bimbo 2026f p.83) |
| Alan 4 (rendimiento incremental) | p.7: el valor terminal reinvierte 29% del NOPAT al 15.17%. De FY2027E a FY2030E, el NOPAT crece MXN 4,484 millones con una reinversión neta de 5-8% del NOPAT, un rendimiento implícito cercano a 60% |
| Alan 4 (R3) | El equipo deja R3 en probabilidad 2 e impacto 4. La Figura 31 no cambia (`memory.md`) |
| **Alan 8 (crecimiento)** | Una sola cifra de crecimiento sin tipo de cambio en 9M26: **4.4%**, con **1.1 pts** de adquisiciones y el peso restando **6.6 pts** (antes 4.7% / 4.3% / 1.2 / 6.9). Se aplicó en p.4 (resumen y "What was bought"), p.4-5 ("What is translated"), p.8 y la tabla A7 del apéndice. Para describir el modelo, "organic only" pasa a "excludes acquisitions" (p.9, dos lugares). En EN se recuperó la primera frase perdida del párrafo "The market price." Fuente: Organic_pass ponderado por las ventas del trimestre de 2025, 4.443 total / 3.368 orgánico / 1.075 adquisiciones [calc] |

## 4. Pendientes, en orden

### A. Figura 13: rehacer la imagen (consecuencia de Alan 8). **La deja Luisart.**

Hoy la barra de 9M26 dice 3.5 orgánico, ~1.2 adquisiciones y −6.9 de conversión cambiaria. Con el texto nuevo tiene que decir:

| 9M26 | Antes | Nuevo [calc] |
|---|---|---|
| Orgánico | 3.5 | **3.4** (3.368) |
| Adquisiciones | ~1.2 (pila hasta ~4.7) | **1.1** (1.075; la pila llega a 4.44) |
| Conversión cambiaria | −6.9 | **−6.6** (−6.643) |
| Crecimiento en pesos (rombo) | −2.2 | −2.2 (sin cambio, [sourced] 2026h) |

FY27E-FY30E no cambian (4.8 / 4.1 / 3.9 / 3.1, FX +1.5 / +1.2 / +1.1 / +0.5).

Detalles:
- Por redondeo, 3.4 + 1.1 se lee como 4.5. Las barras deben dibujarse con los valores sin redondear.
- El reporte en español usa la misma imagen en inglés (`word/media/image15.png` en los dos .docx).
- El script que generó esta figura **no está en la laptop de Jorge**: `report/build/report_charts.py` no tiene esa función. Lo más probable es que lo tenga Luisart.
- Para cambiar la imagen hay que reemplazar `word/media/image15.png` en los dos .docx con el mismo nombre y un tamaño parecido, y luego revisar que la página no se mueva.

### B. Alan 9: riesgos fuera del caso base

Confirmar que la semana de 40 horas en México (R4) y el gobierno corporativo están revelados como fuera del caso base, con su efecto. Es decisión del equipo si alguno entra al caso base.

### C. Alan 10: limpieza de la sección de IA

- Quitar los tres "[Team to confirm]" / "[Por confirmar por el equipo]". Los tiene que llenar el equipo.
- "organic only, as the advisor asked" (EN p.16 / ES p.17). Hay que revisarlo contra las reglas sobre la participación del asesor, y en todo caso cambiar "organic only" por "excluding acquisitions".
- Decir quién verificó las citas.
- Ya resuelto en la v32: 2026g en las referencias, la Tabla 17 con el 1T26, la Figura 19 al 3T26 y el resumen que abre con la tesis.

### D. Hallazgos propios (no los pidió Alan)

1. **Capex +50 pb.** Con recálculo completo cuesta **−3.26**, no −1.46. Además, el "57.08, −1.46" de la Tabla 13 es idéntico al caso del RONIC promedio, probablemente un error de copia.
   - Antes de escribirlo, hay que medirlo con el mismo método de la Tabla 13 (número de acciones fijo, B47_escenario / B48_base).
   - Si se confirma, cambian la fila de la Tabla 13, el texto de R5, la fila R5 de la tabla de riesgos y tal vez el impacto de R5 de 2 a 3. **El impacto lo decide el equipo**; si cambia, también se mueve la Figura 31.
2. **Figura 32 (tornado, imagen; la misma en EN y ES).** Las barras del RONIC todavía dicen 11.9% / 15.1%; deben decir 11.4% / 14.6%, con los valores −11.7 / −1.5 sin cambio. La barra de capex depende del punto D1. `report/build/report_charts.py` tiene `fig_tornado()`, pero no está confirmado que la imagen de la v32 salga de ahí.
3. **México 35% contra 38% en R4.** El párrafo usa 35% (mezcla FY2025) y el cálculo usa 38% (mezcla FY2030E). Hay que poner el año en las dos cifras o usar una sola.
4. **Norteamérica 39% contra 43% en R2.** Mismo problema que el punto 3.
5. **"##" suelto en la p.6.** Borrarlo.

### E. Puntos débiles para preparar el Q&A (revisar después de A-D)

- El RONIC terminal de 15.17% está 0.6 pp arriba del promedio de 4 años (14.6%), con una tendencia que baja de 17.0 a 11.4.
- La nota de la reestructuración (EEFF25 p.82) la describe como reestructuración operativa y comercial (cierres de plantas y rutas en Norteamérica y EAA), no como integración de adquisiciones. Esto debilita el argumento de "panadera, no adquiridora".
- En el pronóstico, el NOPAT crece con muy poco capex (rendimiento implícito cercano a 60%).
- R3 en probabilidad 2: Alan lo llama generoso.

### F. Recorte de páginas (al final, una sola vez)

EN ya está en 10 páginas exactas, sin espacio libre; cualquier línea nueva lo pasa a 11. ES tiene 11 páginas de cuerpo y hay que recortarlo para que coincida.

### G. Cerrar la sesión

Correr `/research-challenge:wrap-up` y registrar el trabajo en `ai-use-log.md` y `thesis-journal.md`.

## 5. Cómo se editaron los .docx

- Se descomprime el .docx y se pasa por `merge_runs.py` (skill docx).
- Se reemplazan subcadenas exactas en `word/document.xml`. Cada texto buscado tiene que aparecer exactamente una vez.
- Se vuelve a comprimir con `[Content_Types].xml` primero.
- Se valida con `validate.py --original <v32>`.
- Se exporta a PDF con Word (COM) y se revisa en qué página empieza el apéndice.
- Las figuras son PNG dentro de `word/media/`.
