# BIMBOA — Rating pivots by pillar (team-approved 2026-11-03)

Source of figures: `analisis-dcf-2026-10-26/precio-objetivo/BIMBOA_statements_2021-2030_v2_pivot_waccV2_TP12m_v2.xlsx` (TP12m_v2). Management statements: 3Q26 call, `raw/bimbo-3q26-earnings-call-2026-10-22-team-transcript.txt` (line numbers).

Rating rule (unchanged, decision 2026-10-28): HOLD while ke 12.26% `[calc]` (Valuacion_12m C74) sits between the pessimistic (-0.69%, C71) and optimistic (+33.48%, C73) expected returns. Price lines: BUY below MXN 51.84 (C76), SELL above MXN 69.68 (C77) `[calc]`.

Every pivot below is an observable public fact with a threshold anchored in the model or in what management said. They do not depend on changing a model parameter.

## Pivot table

| Pillar | Direction | What we watch | Threshold and anchor | When we know | What it breaks |
|---|---|---|---|---|---|
| 1. Growth (~3% ex-acquisitions, ex-FX) | → BUY | Group net sales growth ex-FX, minus the inorganic contribution Bimbo reports, once Wickbold leaves the inorganic base from 4Q26 (l.209) | Above 4% `[assumption]` for two quarters (4Q26 and 1Q27), vs model organic growth 3.29% FY2027E `[calc]` (Assumptions B148) | 4Q26 results (late Feb 2027) and 1Q27 (late Apr 2027) | Growth is no longer ~3%: the ceiling of pillar 1 lifts |
| 1. Growth | Catalyst | Latin America 4Q26 net sales growth ex-FX, first quarter without Wickbold as inorganic | ≤9.1% confirms (best 2026 organic quarter, Organic_pass H11 `[calc]`); ≥14.1% refutes for Latin America (lowest 2026 reported quarter with Wickbold, 2Q26 release p.3 `[sourced]`); in between inconclusive. If refuted, adjust (Latin America 11.06% of FY2030E sales, Assumptions B235 `[calc]`), do not abandon the HOLD | 4Q26 results (late Feb 2027) | Tests whether Latin America growth was bought |
| 1. Growth | → SELL | Net debt/EBITDA after a debt-funded acquisition while Wickbold integration still lags (l.413, l.491) | ≥3.0x, the level the CFO used on the 3Q26 call; today 2.4x, comfort range 2.0x-2.5x `[guidance]` (l.248, 308, 311) | Any deal announcement; quarterly leverage | Growth bought again with debt before the last deal pays off |
| 2. Costs (covered into 2027, absorbable after) | → SELL | IMF global wheat price (FRED PWHEAMTUSDM, the model's series), Jan-Jun 2027 average, the window in which 2H27 is hedged (l.395: 4Q26 fully hedged, 1H27 almost 100%, never 15 months ahead) | Above US$294/t `[calc]` (model 2026E wheat US$217.92, Assumptions B277, x 1.35), the documented stress at which FY2030E gross margin falls to 51.2%, below the FY2021-FY2025 range of 51.4%-53.5% `[calc]` (IS). Conservative: the exact break point lies between US$246.85 (Sep-2026, B276; gross margin 51.8%) and US$294. Confirmation: quarterly gross margin below 51.4% in 3Q27, the first quarter not fully hedged | Monthly; full window in Jul 2027; 3Q27 results (late Oct 2027) | Costs stop being absorbable: the floor of the HOLD fails |
| 2. Costs | → BUY | None, by design | — | — | Pillar 2 is the floor. Cheaper wheat removes a threat but does not lift the ceilings of pillars 1 and 3 |
| 3. Management / margin (must prove the margin it inherited) | → BUY | Formal 2027 adjusted EBITDA margin guidance, given on the 4Q26 call (l.254) | Low end of the range above +28 bp, the model's FY2027E improvement (Assumptions B361 15.12% vs B52 14.84%) `[calc]`; same company definition of adjusted EBITDA as the model (IS row 39) | 4Q26 call (late Feb 2027) | Management backs, with its own number, a margin above what the model needs |
| 3. Management / margin | → SELL | "Other (income) expenses, net" and integration expenses in the 1Q27 report | Other expenses at or above 0.76% of sales, the 9M26 level (Assumptions E18), vs 0.14% in the model for FY2027E (IS H12 / H6) `[calc]`; or integration expenses still reported (model: 0 from FY2027E, IS H11) | 1Q27 results (late Apr 2027) | 114 of the 120 bp of margin improvement FY2025-FY2027E depend on these two lines falling; without it, the improvement does not arrive |

Price lines also apply: BUY below MXN 51.84, SELL above MXN 69.68 (Valuacion_12m C76-C77).

## Paragraph for the report ("Rating and what the valuation depends on")

Each pillar has a public test with a date. On growth, we would move toward BUY if net sales ex-FX, net of the inorganic contribution Bimbo reports, grow above 4% in 4Q26 and 1Q27, the first two quarters after Wickbold leaves the inorganic base, against the 3.29% our model assumes for FY2027E. We would move toward SELL if a debt-funded acquisition takes net debt/EBITDA to 3.0x or more while Wickbold's integration still lags. On management and margin, we would move toward BUY if the formal 2027 guidance on the 4Q26 call puts the low end of the margin range above the +28 bp in our model, and toward SELL if other expenses, net, stay at or above 0.76% of sales in 1Q27 instead of falling to the 0.14% our margin depends on. On costs, the pillar that keeps us from selling, the test is wheat in the first half of 2027, when Bimbo hedges the second half: above US$294 per tonne, gross margin leaves its 2021-2025 range and the floor fails. Cheaper wheat would not make us buyers, because it lifts neither growth nor the margin management still has to prove.

## Open before the report

- Report v13 Table 6 shows the leverage SELL trigger at 2.5x; the team decision of 2026-10-28 is 3.0x. Align the report to 3.0x.
- The 4% growth threshold is a team judgment `[assumption]`; Bonel (acquired Apr 2026) stays in Bimbo's inorganic contribution until 2Q27, so use the net-of-inorganic figure Bimbo reports.
- The exact wheat break point (between US$246.85 and US$294) needs one run on a copy of the model; US$294 is used until then.
