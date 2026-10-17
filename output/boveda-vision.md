# Bóveda Vision: Grupo Bimbo (BIMBOA)

**Página interactiva:** https://claude.ai/artifact/Esvn6B5gNR7xkWYNkSHhaH
- La página es privada: para que el equipo la abra, compártela desde el menú Share de la página.
- Simulador del DCF v2 con todas las opciones del equipo.
- Su motor coincide con el modelo en Python en 37 de 37 valores `[calc]`.

**Fecha:** 2026-10-17. Valuación al 16-oct-2026, en MXN por acción salvo que se indique otra cosa. Fuente de cifras: `valuation/valuation-outputs.yaml` (v2). Etiquetas: `[sourced]`, `[calc]`, `[assumption]`.

## La pintura completa

| Referencia | Valor por acción (MXN) | Etiqueta |
|---|---|---|
| Precio en bolsa, 16-oct-2026 | 58.60 | `[sourced]` cierre oficial de BMV (PPP), bmv.com.mx |
| Rango de 52 semanas | 53.03 – 68.67 | `[sourced]` CIQ |
| Consenso de 12 analistas (20-sep-2026) | 51 – 87, media 70.17 | `[sourced]` `data/capitaliq/consensus.csv` |
| Tesis del 08-oct: múltiplos históricos, COMPRA | 59.9 – 75.2 | `[calc]` [[bimbo-tesis-3-pilares]] |
| **DCF Gordon, base publicada** | **35.72** (−39.0%) | `[calc]` propuestas del coach |
| **DCF múltiplo de salida 6.0x, base publicada** | **46.60** (−20.5%) | `[calc]` |
| Gordon a 12 meses (dividendo siguiente 1.05) | 39.18 | `[calc]` |
| Comparables EV/EBITDA LTM, 5.64x a 8.27x | 37.5 – 74.7 | `[calc]` |
| Gordon si el crecimiento no crea valor (RONIC = WACC) | 26.79 | `[calc]` |

**Lo que pide el precio.** Para que el Gordon llegue a 58.60 con una sola palanca, haría falta alguna de estas tres `[calc]`:
- ventas creciendo 307 pb más cada año;
- margen 179 pb más alto por productividad;
- capex 118 pb más bajo sobre ventas.

Otra forma de leerlo: el precio implica un crecimiento perpetuo de 6.17%, arriba del tope de 5.0% del PIB nominal.

**La tensión que hay que resolver.** La nota de tesis del 08-oct recomienda COMPRA, y el DCF con las propuestas actuales queda abajo del precio. La recomendación es del equipo: si se mantiene, hay que nombrar el supuesto que la sostiene y su número.

## De v1 a v2

| Paso | Gordon | Múltiplo |
|---|---|---|
| v1 auditada | 46.14 | 47.42 |
| Capital de trabajo sin partidas financieras ni fiscales | −1.50 | −0.59 |
| Provisiones fiscales (UTP 8,537) y beneficios por país | −2.84 | −2.84 |
| Múltiplo: solo los reclamos que también restan los pares | — | +4.98 |
| Arrendamientos que crecen con las ventas | −6.10 | −2.38 |
| **v2 publicada** | **35.72** | **46.60** |

## Todas las opciones (lo que se mueve en la página)

| Grupo | Opciones | Base v2 |
|---|---|---|
| Costo de capital | Ruta A local o B Damodaran (prima país por EBITDA o por ventas); beta 0.53 / 0.46 / pares 0.21; D/E 0.743 / 0.689 / 0.479; Kd 9.26–10.26%; ERP | A, 0.53, 0.743, 9.71%, 4.20% |
| Valor terminal | g 3.0–5.5%; múltiplo 4–10x (5.64x, 6.0x, 6.94x, 8.27x, 9.22x); Gordon con FCFF o con RONIC fijo (incluso = WACC) | 4.25%, 6.0x, FCFF |
| Pilares | Clima: margen bruto ±100 pb. Nuevo CEO: margen por productividad ±100 pb. Deuda y flujo: capex ±100 pb. Crecimiento de ventas ±100 pb por año | 0 |
| Puente y criterios | Arrendamientos crecen o fijos; reclamos del múltiplo con base de pares o puente completo; NCI a mercado g 3% / g 0% / libros; provisiones fiscales sí o no | crecen, pares, g 3%, sí |
| Pesos | Gordon 0–100% contra múltiplo | 50% |

Botón "Copiar escenario para el chat": pega el texto en la conversación para fijar los supuestos del equipo.

## Decisiones abiertas del equipo

1. Ruta del WACC y beta.
2. Supuestos terminales y retorno de largo plazo.
3. Ruta del capex de FY31-35 (la palanca más grande: ±50 pb = ∓9.7 por acción).
4. Puente: prima del NCI (4.61 por acción) y posiciones fiscales inciertas (2.65).
5. Método principal, precio objetivo y recomendación.

Detalle, con recomendación, argumento en contra y pregunta para cada una: `valuation/valuation.md` §11.

## Auditoría

- Codex, tres rondas: 14 hallazgos en la v1, 1 nuevo en la ronda 2 y **PASS** en la ronda 3.
- Excel: 23 de 23 controles OK; conciliación de 30 de 30 filas con el motor y de 61 de 61 con la réplica en Python; 0 errores de fórmula.
- **Actualización de insumos del 17-oct, después de la auditoría.**
  - Seis insumos quedaron documentados con fuente: cierre de BMV, fecha de la beta, PIB real (FMI 2.1%, Banxico 1.88%) y provisiones y derivados a junio del XBRL de BMV.
  - Dos no se publican y quedan como cálculos documentados: los intereses dentro de los pagos de arrendamiento y la ganancia de La Moderna.
  - El valor publicado no cambia. La verificación fechada pasa a Gordon 36.24 (+1.5%) y múltiplo 46.48 (−0.3%) `[calc]`.
- **Pendientes.**
  - El EBIT del 1S26 de la verificación fechada mezcla bases: corregirlo la sube cerca de 0.33 por acción, sin tocar el valor publicado.
  - BMV muestra 4,284.6 millones de acciones en circulación contra 4,294.9 millones al 29-jul.
  - Falta re-exportar de CIQ el extracto del M-Bono.

## Archivos

- `valuation/BIMBOA_DCF_v2.xlsx`, `valuation/BIMBOA_WACC_v2.xlsx`, `valuation/BIMBOA_PeerAnalysis_v1.xlsx`
- `valuation/valuation.md`, `valuation/valuation-outputs.yaml`
- `model/BIMBOA_model_v3.xlsx` (mismos números que la v2), `model/review.md`
- Tesis del 08-oct: [[bimbo-tesis-3-pilares]]
- Generador de la página: `valuation/build/boveda/`. Si cambian los insumos, hay que regenerarla y volver a publicarla:
  1. `python -I valuation/build/boveda/export_data.py --project . --out valuation/build/boveda/data.json`
  2. `node valuation/build/boveda/test_model.js valuation/build/boveda/data.json`
  3. `python -I valuation/build/boveda/build_page.py --project .`
