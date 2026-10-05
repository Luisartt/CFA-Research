---
Writer: Claude
Source:
  - raw/Financials/As-Reported/Cash Flow/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow(AsReported)_19-Sep-2026.xlsx.md
  - raw/Financials/As-Reported/Cash Flow/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow(AsReported)_9-19-2026.docx.md
  - raw/Financials/As-Reported/Cash Flow/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow(AsReported)_9-19-2026.pdf.md
tags:
  - Financials
  - cash-flow
---

# Estado de flujo de efectivo as-reported (S&P CapIQ) — Grupo Bimbo

- Fuente: S&P Capital IQ "Standard", bajada ==19-Sep-2026==. ==Anual== (Period Type: Years), 1995 FY - ==2025 FY==; sin trimestres ni 2026 (para 2026 ver [[cash-flow-templated]]). Partidas con el nombre del filing, NIIF, ==método indirecto==. La fila "Units" cambia: Thousands hasta 2001, Millions desde 2002; aquí todo en ==MXN millones==. Los 3 archivos son el mismo reporte.
- Las etiquetas cambian entre años (p. ej. "Proceeds from Long-term Debts" 2015-2018 -> "Loans Obtained Net of Issuance Expenses" 2019+). Armé las series uniendo etiquetas equivalentes.
- ==Estructura NIIF de Bimbo==: el CFO parte de utilidad antes de impuestos y suma de vuelta el gasto por interés ("Interest Payable" 14,464 en 2025); el ==interés pagado y los pagos de arrendamiento van en financiamiento==. Por eso CFO es antes de intereses.

## Anual 2016-2025 (MXN millones)

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Utilidad antes de impuestos (continuas) | 13,613 | 11,951 | 11,708 | 12,108 | 15,406 | 24,854 | 45,878 | 25,324 | 21,034 | 20,143 |
| Depreciación y amortización | 8,436 | 8,761 | 10,000 | 14,373 | 16,251 | 16,375 | 18,282 | 18,929 | 23,051 | 24,838 |
| Deterioro de activos de larga vida | 1,246 | 545 | 907 | 1,318 | 1,075 | 694 | 1,046 | 383 | 249 | 445 |
| Gasto por interés sumado de vuelta | 5,486 | 5,872 | 7,668 | 8,561 | 9,424 | 7,884 | 8,049 | 10,006 | 13,100 | 14,464 |
| Impuestos pagados (partida de capital de trabajo) | -4,703 | -4,420 | -4,327 | -3,961 | -5,789 | -7,578 | -11,824 | -13,831 | -6,472 | -8,955 |
| Cuentas por cobrar | -1,020 | -591 | -1,250 | -1,348 | -914 | 666 | -6,647 | -4,206 | -319 | 601 |
| Inventarios | -1,097 | -898 | -1,194 | -876 | -769 | -2,320 | -4,163 | -1,078 | -1,104 | 901 |
| Proveedores | 518 | 2,041 | 257 | 2,054 | 3,004 | 8,286 | 9,920 | -851 | -2,825 | -1,108 |
| ==Flujo operativo (CFO)== | 23,127 | 21,170 | 20,982 | 28,520 | 43,877 | 45,776 | 38,851 | 31,411 | 39,907 | 47,753 |
| Compra de PP&E (capex) | -13,153 | -13,446 | -15,067 | -13,117 | -13,218 | -20,671 | -28,669 | -34,754 | -29,402 | -22,530 |
| Venta de PP&E | 1,033 | 333 | 599 | 470 | 763 | 882 | 20 | 152 | 984 | 824 |
| Adquisiciones de negocios (y no controladoras) | -3,966 | -12,482 | -3,600 | -94 | -3,453 | -10,637 | -6,520 | -6,548 | -5,988 | -11,294 |
| Precio por venta de operación discontinua | | | | | | | 25,797 | | | |
| ==Flujo de inversión (CFI)== | -16,315 | -27,070 | -18,391 | -12,642 | -16,688 | -32,459 | -9,122 | -42,440 | -36,138 | -34,652 |
| Préstamos obtenidos | 34,687 | 40,772 | 8,024 | 22,594 | 34,818 | 38,924 | 51,670 | 136,638 | 79,111 | 69,267 |
| Pago de deuda LP | -31,888 | -26,904 | -11,005 | -22,640 | -40,745 | -33,535 | -55,542 | -109,847 | -56,495 | -55,477 |
| Pagos de arrendamiento | n/d | n/d | n/d | -4,784 | -5,544 | -5,372 | -6,385 | -6,278 | -7,072 | -8,060 |
| Intereses pagados | -4,465 | -4,429 | -7,280 | -5,681 | -6,410 | -6,781 | -6,407 | -7,436 | -8,376 | -11,533 |
| Dividendos pagados | -1,129 | -1,364 | -1,646 | -2,103 | -2,433 | -4,636 | -5,885 | -3,549 | -4,234 | -4,451 |
| Recompra de acciones (reserva) | -50 | -53 | -1,107 | -1,748 | -3,740 | -1,901 | -2,568 | -3,586 | -4,433 | -1,253 |
| Pago de derivados | n/d | n/d | -412 | -2,481 | -2,431 | -1,690 | n/d | -1,655 | -1,889 | -1,034 |
| Cobro de derivados | n/d | n/d | 2,222 | 605 | 2,970 | 1,496 | 418 | 2,090 | 692 | 633 |
| ==Flujo de financiamiento (CFF)== | -4,383 | 6,492 | -2,322 | -16,833 | -24,163 | -14,116 | -25,692 | 5,904 | -2,696 | -11,908 |
| Efecto cambiario | 560 | -190 | 99 | -378 | -9 | 279 | -472 | -835 | 631 | -715 |
| ==Cambio neto en efectivo== | 2,989 | 402 | 368 | -1,333 | 3,017 | -520 | 3,565 | -5,960 | 1,704 | 478 |

Notas: 2016-2017 "Pago de derivados/arrendamiento" no tienen línea comparable (otras etiquetas). 2022 "Pago de derivados" no se reporta como línea separada.

### Derivados anuales

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| FCF antes de intereses (CFO + capex) | 9,974 | 7,724 | 5,915 | 15,403 | 30,659 | 25,105 | 10,182 | -3,343 | 10,505 | 25,223 |
| Intereses pagados / CFO | 19% | 21% | 35% | 20% | 15% | 15% | 16% | 24% | 21% | 24% |
| Dividendos + recompras | 1,179 | 1,417 | 2,753 | 3,851 | 6,173 | 6,537 | 8,453 | 7,135 | 8,667 | 5,704 |
| Deuda neta nueva (obtenida - pagada - arrend.) | 2,799 | 13,868 | -2,981 | -4,830 | -11,471 | 17 | -10,257 | 20,513 | 15,544 | 5,730 |

- ==2025: CFO récord 47,753== (+19.7% vs 39,907 de 2024) con capex a la baja (-23.4%, 22,530). Utilidad antes de impuestos baja 4.2% (20,143), así que la mejora viene de D&A (+1.8 mil M) y de capital de trabajo: inventarios +901 (liberación) vs -1,104 en 2024 y cuentas por cobrar +601 vs -319.
- ==2022-2024 es el ciclo de inversión==: capex 28.7 -> 34.8 -> 29.4 mil M; CFI -9,122 en 2022 porque la venta de Ricolino aportó +25,797 (sin ella, CFI habría sido -34.9 mil M); luego CFI -42,440 (2023), -36,138 (2024), -34,652 (2025).
- ==Refinanciamiento masivo==: préstamos obtenidos de 136,638 en 2023 (vs pagos 109,847) y 79,111 en 2024. La deuda neta nueva suma +20.5 mil M en 2023 y +15.5 mil M en 2024 (financia capex y M&A).
- ==Proveedores como fuente de caja==: +8,286 (2021) y +9,920 (2022) por mayores plazos; se revierte a -851 (2023), -2,825 (2024) y -1,108 (2025). Ver DPO en [[balance-sheet-templated]].
- ==Impuestos pagados==: 11,824 (2022) y 13,831 (2023) (los más altos de 2016-2025; la fuente no explica la causa); vuelven a 6,472 (2024) y 8,955 (2025).
- Dividendos: 4,451 en 2025 (2T); recompras caen a 1,253 (2025) desde 4,433 (2024). Retorno total al accionista 5,704 (2025) vs 8,667 (2024).
- Intereses pagados 11,533 (2025) = 24% del CFO; casi 2.6x los de 2016. Gasto por interés sumado de vuelta 14,464 vs interés pagado 11,533 (diferencia 2,931, devengado no pagado). Ver [[capital-structure-summary]].
- Adquisiciones 2025 = 11,294 + 1,468 de compra de participación no controladora (línea aparte); consistente con minoritarios 743 en [[balance-sheet-as-reported]].

## Histórico largo (hitos)

- Serie desde 1995: CFO 2015 = 18,116 (capex -9,604); salto a >43 mil M en 2020-21 con mayor capital de trabajo (proveedores) y D&A más alta: de 10,000 (2018) a 14,373 (2019), año en que aparecen los pasivos por arrendamiento en el balance ([[balance-sheet-as-reported]]).
- CFO 2020 = 43,877 y 2021 = 45,776 son el 3.º y 2.º más altos de 2016-2025 (después de 2025); en 2021 proveedores aportan +8,286.

## Key Takeaways
- CFO 2025 = 47,753, el mayor del histórico; FCF antes de intereses 25,223, después de intereses ~13.7 mil M.
- El CFO es pre-interés (NIIF): intereses pagados 11,533 y arrendamientos 8,060 van en financiamiento; considerarlos al evaluar capacidad de pago.
- Ciclo de capex 2022-24 (hasta 34,754) y M&A se financió con deuda neta nueva de ~36 mil M en 2023-24.
- Retorno al accionista bajó en 2025 (5,704 vs 8,667) por menos recompras.
- Solo anual en esta fuente: para trimestres usar [[cash-flow-templated]].
