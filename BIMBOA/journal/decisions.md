# BIMBOA — decisions journal (append-only)

Labels: observado / guidance / supuesto / output. Every entry is dated; nothing is edited afterwards.

## [2026-10-17] macro — /research-analyst:update-macro (first load of macro/macro-view.yaml)

- **Context:** `macro/` did not exist. It was created from the plugin template; the pre-update state (empty template) is snapshotted at `macro/history/macro-view_2026-10-17.yaml`. FRED was not fetched (no API key; `macro/series/README.md`). Inputs: the sources indexed in `macro/sources/sources-index.md` (Capital IQ prompt 2, Grupo Bimbo RA25 and 2Q26 release, IMF WEO Oct-2026, Banxico survey Sep-2026, Damodaran July 2026, Yahoo USD/MXN).
- **Gate:** the team asked for an automatic run without questions, so no field was confirmed. Only observed values with a citation (and one `output` computed from observed CPI) were loaded, each with `status: propuesto`. No `supuesto` was written. **Pending: the team confirms, corrects or rejects each field.**

| Field | Before | Proposed | Label | Source |
|---|---|---|---|---|
| rates.risk_free_10y | empty | 9.26% (16-Oct-2026) | observado | S&P Capital IQ, prompt 2 Task 2A |
| rates.policy_rate_path | empty | 7.00% at 31-Dec-2025 | observado | RA25 p.57-58 |
| rates.curve_observations (extra) | empty | M-Bono 1Y 6.679%, 5Y 8.298%, 30Y 9.782%; UST 10Y 5.09%; Mexico CDS 5Y 0.95%, 10Y 1.64%; Damodaran default spread 1.75% (Baa3) | observado | Capital IQ prompt 2; Damodaran July 2026 |
| fx.usdmxn_path | empty | 17.97 (31-Dec-2025), 17.47 (30-Jun-2026), 18.479 (16-Oct-2026) | observado | RA25 p.147; 2Q26 release p.6; Yahoo MXN=X |
| fx.usdmxn_annual_average (extra) | empty | 17.7620 / 18.3024 / 19.2244 (2023-2025) | observado | Grupo Bimbo filings |
| inflation.mx_3y_trailing_cumulative | empty | 13.09% (2023-2025) | output | (1.0466 x 1.0421 x 1.0369) - 1, INEGI CPI via RA25 p.57-58 |
| inflation.mx_cpi_yoy_latest / us_cpi_yoy_latest (extra) | empty | 3.45% / 3.74% (Sep-2026) | observado | Capital IQ prompt 2 Task 2B |
| inflation.mx_forecast_path | empty | 3.0% (2029-31, IMF); 3.7% (long run, Banxico survey) | observado | IMF WEO Oct-2026 PCPIPCH; Banxico survey Cuadro 5 p.6 |
| gdp.mx_growth_path | empty | 2.1% (2029-31, IMF); 1.88% (2027-36 average, Banxico survey) | observado | IMF WEO Oct-2026 NGDP_RPCH; Banxico survey Cuadro 6 p.8 |
| equity_risk_premium | empty | 4.20% (1-Oct-2026) | observado (third-party estimate, attributed) | Damodaran implied ERP |
| inflation.us_forecast_path, gdp.us_growth_path, commodity_decks | empty | not proposed | — | no source in macro/sources or macro/series |

**Impact triage (transversal: one coverage in the workspace, BIMBOA).** `issuer-profile.yaml` with materiality thresholds does not exist in this project, so the levels are qualitative. Impact estimates cite the sensitivities already built in `valuation/BIMBOA_DCF_v3.xlsx`; none is computed here.

| Finding | Level | Why | Where it hits | Estimated impact |
|---|---|---|---|---|
| M-Bono 10Y 9.26% | Cosmetic | Same value the model already uses (route A rf; route B starts from it) | WACC | none (already in valuation.yaml) |
| Damodaran ERP 4.20%; Mexico default spread 1.75% (Baa3, July 2026) | Cosmetic | Already in the v3 base | WACC | none |
| Mexico 10Y CDS 1.64% vs the rating-based spread 1.75% | Relevant | The market spread is 11 bp below the rating-based one: a secondary choice inside route B's risk-free rate | WACC (route B rf) | DCF v3 WACC x g grid: ±1 pp of WACC = -11.6 / +16.1 per share; this change is a small fraction of one row |
| USD/MXN 18.479 at 16-Oct-2026 vs 17.47 at 30-Jun-2026 | Relevant | The peso is weaker than at the 1H26 anchor; North America is 44% of sales, so 2H26 peso revenue translates higher than the "flat in pesos" guidance implies | FY2026 revenue (North America translation) | DCF v3 Levers: revenue growth ±50 bp a year = +3.24 / -3.11 per share |
| US CPI 3.74% vs Mexico CPI 3.45% (Sep-2026) | Relevant | Today's inflation gap points to less peso depreciation than the ~1.5% a year inside drivers.yaml (FY2027+) | North America growth in MXN; PPP scenario rows | DCF v3 Scenarios: PPP rows -2.18 / +0.75 per share (Gordon) |
| Banxico long-run inflation expectation 3.7-3.8% vs the 3.0% target | Relevant | At survey inflation the long-run nominal GDP cap would be about 5.6%, not 5.0%: more headroom for g | terminal growth cap | DCF v3 WACC x g grid: g +50 bp at 10.32% = 37.62 (+4.07 per share) |
| IMF 2.1% and Banxico 1.88% real growth | Cosmetic | Already the source of the 5.0% cap | terminal growth cap | none |
| Mexico CPI 2023-25 cumulative 13.09% | Cosmetic | IFRS reporter: the NIF B-10 monitor does not apply; Argentina is already under IAS 29 | — | — |
| Banxico rate 7.00% (end-2025) | Cosmetic | Not a model input (Kd = M-Bono + issue spread) | — | — |

- **Resolution:** pendiente (the analyst was away; the gate stays open). No model, driver or valuation input was changed by this run.
- **Questions for the team (debate protocol):** (1) Does the weaker peso since June change the FY2026 revenue anchor, or is "flat in pesos" still the right reading? (2) Should the long-run GDP cap use the 3.0% target or the survey's 3.7-3.8% inflation?
