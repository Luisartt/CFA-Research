# Central thesis (team final text, 2026-11-02) — figures updated to TP12m_v2

Source model: `analisis-dcf-2026-10-26/precio-objetivo/BIMBOA_statements_2021-2030_v2_pivot_waccV2_TP12m_v2.xlsx`
(the base model; the professor copy `BIMBOA_modelo_revision_profesor_v1.xlsx` was built from it and carries the same values).
Only figures changed; the wording is the team's.

---

**Bimbo is worth what it costs today — due to growth of about 3% once acquisitions and currency are stripped out and a new management that must still prove the margin it inherited, offset by costs that are covered into 2027 and absorbable after it.**

The recovery is real. In 3Q26 the group margin reached 15.7%, 100 bp above a year earlier, leverage fell to 2.4x and management raised its 2026 margin guide for the third time (Grupo Bimbo, 3Q26 earnings call; 2026h). But the base is softer than the headline. Net sales excluding currency grew 4.7% in 9M26, of which about 1.2 points were acquisitions; and the peso, which cut reported sales by 2.2% in those nine months, turns in our model into 1.46 of the 4.75 points of FY2027E growth. Of the 120 bp of margin we model to FY2027E, 114 come from two lines that fall almost to zero, under a CEO who took over in November 2025 a recovery that was already under way (team model).

Costs are what keep this from being a sell. Raw materials are fully hedged for 4Q26 and almost fully for 1H27, and even wheat 35% higher for good would cost about MXN 14.75 of the MXN 66.13 target, 22% of it (Grupo Bimbo, 3Q26 earnings call; team model). That cushion explains why 2026 looks easy, and it sets the date of the test. From 4Q26 Wickbold stops counting as acquired growth, in the second half of 2027 the hedges run out, and 2027 is the first year that the new management cannot lean on what it inherited. The market already pays for the outcome: the share rose 10.7% between 16 and 27 October to MXN 64.85, 1.9% below our 12-month target of MXN 66.13. We rate Bimbo HOLD, not because the recovery is in doubt, but because the price already pays for it and only 2027 can show whether it deserves more.

---

## Where each figure comes from

| Figure in text | Value | Tag | Source |
|---|---|---|---|
| 12-month target | MXN 66.13 | `[calc]` | TP12m_v2, Valuacion_12m: 58.60 x (1 + B51) |
| FY2027E net sales growth / FX effect | 4.75% / 1.46 pp | `[calc]` | TP12m_v2, Assumptions B147, B149 |
| Adj. EBITDA margin FY2025 -> FY2027E | 13.93% -> 15.12% (+120 bp) | `[calc]` | TP12m_v2, Assumptions B49, B361 |
| Of which two lines | 114 bp: other expenses net 1.15% -> 0.14% of sales (101 bp) + integration 541 -> 0 (13 bp) | `[calc]` | TP12m_v2, IS rows 6, 11, 12 |
| Wheat +35% for good | target 66.13 -> 51.38 (-14.75, -22.3%); FY2030E gross margin 52.2% -> 51.2% | `[calc]` | Scratch copy of TP12m_v2, Assumptions B391 = B277 x 1.35 (2027 wheat 35% above the 2026E average, held flat after), full Excel recalculation; base file not modified |
| Share price 27-Oct vs 16-Oct | 64.85 vs 58.60 (+10.7%); 1.9% below target | `[sourced]` / `[calc]` | Yahoo Finance (2026); 64.85 / 66.13 - 1 |
| 3Q26 margin, leverage, guide | 15.7%, +100 bp, 2.4x, third raise | `[sourced]` | Grupo Bimbo 3Q26 release (2026h) and call; leverage path 2.9x Dec-24, 2.7x Dec-25, 2.5x Jun-26 (wiki bimbo-balance-sheet-and-leverage) |
| 9M26 growth ex-FX, acquisitions, FX | 4.7%, ~1.2 pts, -2.2% | `[sourced]` / `[calc]` | Grupo Bimbo (2026h); acquisitions points from Organic_pass (team estimate), unchanged from report v10 |

Note: report v10 quoted the wheat case as "about MXN 11, 17%" on the v1 model (target 64.18). On TP12m_v2 the same case is MXN 14.75 (22%).
