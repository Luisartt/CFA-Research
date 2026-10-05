---
Writer: Claude
Source:
  - raw/Financials/Templated/Pension Details/SPGlobal_GrupoBimbo,S.A.B.deC.V._PensionDetails_19-Sep-2026.xlsx.md
  - raw/Financials/Templated/Pension Details/SPGlobal_GrupoBimbo,S.A.B.deC.V._PensionDetails_9-19-2026.docx.md
  - raw/Financials/Templated/Pension Details/SPGlobal_GrupoBimbo,S.A.B.deC.V._PensionDetails_9-19-2026.pdf.md
  - raw/Financials/Templated/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet_19-Sep-2026.xlsx.md
tags:
  - Financials
  - pensiones
---

# Detalle de pensiones (S&P CapIQ) — Grupo Bimbo

- Fuente: S&P Capital IQ Pension Details, "Standard", Current/Restated, columnas trimestrales 1995 FQ1 - 2026 FQ2, bajada ==19-Sep-2026==. MXN; aquí en ==MXN millones==. Los 3 archivos son el mismo reporte. Solo hay datos en columnas ==FQ4== (anual, fecha de beneficio 31-dic) desde 2004; plan de pensión (no OPEB) con datos por año de 2009 a 2025. ==No hay datos para 2013== (NA) ni para 2026 (los planes se actualizan al cierre anual).
- Líneas vacías en la fuente: costo neto periódico de beneficio definido, tasas de descuento/retorno esperado, OPEB en %. Solo traen datos de flujo de obligación, activos y composición.
- Pasivo en balance (pensiones + OPEB): [[balance-sheet-templated]] y [[balance-sheet-as-reported]].

## Conciliación anual (MXN millones)

| | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ==Obligación proyectada (PBO)== | 30,086 | 32,253 | 35,784 | 35,018 | 29,231 | 37,839 | 42,386 | 41,401 | 27,465 | 27,163 | 28,382 | 29,033 |
| ==Activos del plan== | 21,723 | 24,149 | 26,453 | 26,214 | 24,247 | 29,253 | 34,790 | 36,823 | 24,413 | 24,788 | 26,684 | 27,509 |
| Posición neta (activos - PBO) | -8,363 | -8,104 | -9,331 | -8,804 | -4,984 | -8,586 | -7,596 | -4,578 | -3,052 | -2,375 | -1,698 | -1,524 |
| Fondeo (activos/PBO) | 72.2% | 74.9% | 73.9% | 74.9% | 82.9% | 77.3% | 82.1% | 88.9% | 88.9% | 91.3% | 94.0% | 94.8% |
| Costo de servicio | 523 | 757 | 706 | 826 | 986 | 717 | 991 | 1,128 | 1,013 | 837 | 942 | 909 |
| Costo de interés | 1,378 | 1,565 | 1,775 | 1,720 | 1,656 | 1,618 | 1,851 | 1,745 | 1,867 | 1,821 | 2,073 | 2,140 |
| Variación actuarial (+ = aumenta obligación) | 2,908 | -2,427 | 1,404 | 955 | -5,809 | 7,709 | 3,515 | -2,536 | -8,382 | 529 | -1,835 | 1,326 |
| Beneficios pagados (obligación) | -1,235 | -3,950 | -5,144 | -3,462 | -2,047 | -1,827 | -2,552 | -2,285 | -6,625 | -1,727 | -2,211 | -2,281 |
| Ajuste por tipo de cambio (obligación) | 1,893 | 3,330 | 4,790 | -805 | -550 | -756 | 1,372 | 963 | -1,500 | -1,762 | 2,250 | -1,443 |
| Aportaciones del empleador | 749 | 947 | 1,416 | 1,106 | 375 | 1,345 | 1,483 | 2,064 | 1,000 | 897 | 88 | 75 |
| Retorno real de activos | 2,363 | -268 | 1,577 | 1,231 | -1,001 | 4,269 | 4,242 | 514 | -6,226 | 1,784 | 676 | 2,943 |
| Equities / activos | 56.9% | 37.8% | 31.0% | 26.7% | 22.8% | 23.5% | 25.8% | 19.7% | 25.6% | 25.5% | 26.0% | 26.8% |
| Renta fija / activos | 31.6% | 47.1% | 53.0% | 63.1% | 67.8% | 69.1% | 66.5% | 69.2% | 66.7% | 63.5% | 65.1% | 64.2% |
| Otros / activos | 11.5% | 15.1% | 16.0% | 10.2% | 8.0% | 7.4% | 7.7% | 11.1% | 7.6% | 11.0% | 8.9% | 9.0% |

Conciliación 2025: PBO inicial 28,382 + servicio 909 + interés 2,140 + variación 1,326 - beneficios 2,281 - FX 1,443 = 29,033. Activos: 26,684 + retorno 2,943 + aportaciones 75 - beneficios 856 - FX 1,337 = 27,509. Posición neta -1,524.

### Hitos anteriores (PBO / activos)
- 2009: 13,032 / 8,543 (fondeo 65.6%); 2010: 13,700 / 8,847 (64.6%); 2011: 23,108 / 15,860 (68.6%); 2012: 24,675 / 16,401 (66.5%).
- Salto 2011: PBO +9,408 y activos +7,013, con "Acquired Plan Assets" de 5,573 (2011) y 1,570 (2014); coincide con las adquisiciones de Sara Lee de 2011 (ver [[ma-call-sara-lee-2011-10]]).
- 2004: PBO 4,676 y activos 4,315 (accum. benefit obligation 3,930).

## Lectura

- ==Déficit de fondeo de 1,524 al 31-dic-2025== (PBO 29,033 vs activos 27,509): fondeo 94.8%, el mayor de la serie. En 2014-2017 el déficit era 8-9 mil M (72-75%). Coincide con "Debt equivalent of unfunded PBO" de 1,524 en el balance S&P.
- ==Reducción de la obligación en 2022== (41,401 -> 27,465, -33%): variación actuarial -8,382, beneficios pagados -6,625 y FX -1,500; activos 36,823 -> 24,413 (retorno real -6,226, beneficios, FX). La reversión de provisión de planes multi-empleador del 4T22 ([[resultados-4t22]]) es otro concepto; esta fuente solo cubre los planes de beneficio definido.
- ==Costo anual del plan DB estable en ~2.7-3.0 mil M (2022-2025)== (servicio 909 + interés 2,140 = 3,049 en 2025). Interés / PBO inicial: 6.6% (2023), 7.6% (2024), 7.5% (2025): tasa de descuento implícita (cálculo propio).
- ==Aportaciones mínimas recientes==: 88 (2024) y 75 (2025) vs 1,000 (2022) y 897 (2023); fondeo ya cerca de 95%.
- Mezcla de activos: ~64% renta fija, ~27% acciones, ~9% otros (2025). Menos acciones que en 2014 (57%), mejora sensibilidad a mercado.
- ==Costo de planes de contribución definida==, reportado en la columna FQ1 (no está claro si es anual): 496 (2017), 526 (2019), 603 (2020), 649 (2022), 635 (2023), 595 (2024), ==742 (2025)==; sin datos 2018 y 2021. Alza de 25% en 2025 vs 2024.
- Pasivo de balance (pensiones + OPEB): 36,407 (2020) -> 7,492 (2025) -> 6,202 (2T26). Esa partida es mayor que el déficit DB (1,524): el resto (~6 mil M) corresponde a OPEB y otros beneficios no detallados aquí.

## Key Takeaways
- Plan de beneficio definido casi totalmente fondeado: 94.8% al cierre de 2025 (déficit 1,524 sobre PBO de 29,033).
- Riesgo de pensiones ya no es material vs deuda de 190 mil M: déficit = 0.8% de la deuda total.
- Aportaciones del empleador de solo 88 y 75 millones MXN en 2024-25 (vs ~1,000 en 2022); costo DC sube a 742 en 2025.
- Gran swing de 2022 (PBO -33%) coincide con la caída del pasivo de pensiones del balance; no es recurrente.
- Faltan datos 2013 y 2026; tasas de descuento no vienen en la fuente.
