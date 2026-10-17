# Investment risks — Grupo Bimbo (BIMBOA)

_Updated 2026-10-17. Assistant proposal: the team decides the key risks, the scores and what is priced in. Supersedes `BIMBOA/research/risks.md` (2026-10-14), which sized risks on a static multiple bridge before the model existed. Scores in `research/risks.yaml`; matrix in `report/charts/risk-matrix.png`._

Tags: `[sourced]` `[guidance]` `[assumption]` `[calc]` `[unverified]`. MXN millions unless stated.

## 1. How impact is measured

- Base: the published DCF v3 values (proposals): **Gordon MXN 33.55, exit 6.0x MXN 45.72** per share `[calc]` `valuation/valuation-outputs.yaml`. Each risk is run through the Python replica of the DCF (`valuation/build/dcf_core.py`, published basis), changing only the driver the risk moves. Scores use the Gordon change (exception: R5 moves only the exit value, so its score uses the exit change); the exit change is shown next to it. Where a risk has a range, the score uses the central case.
- Rules of thumb from the DCF v3 sensitivities `[calc]`: gross margin ±50 bp = ±Ps 6.13; capex ±50 bp = ∓Ps 9.44; revenue growth ±50 bp a year = +Ps 3.24 / -Ps 3.11; WACC ±1 pp = -Ps 11.59 / +Ps 16.13; exit multiple ±1x = ±Ps 9.11 (exit value only).
- Scale (`risk-framework.md`): impact 1 <2%, 2 2-5%, 3 5-10%, 4 10-20%, 5 >20%; probability over the next 12-24 months. All probability and impact scores and every "priced in?" call are `[assumption]` (proposals for the team); every value impact is `[calc]`.
- Pillars are the team's (`research/thesis.md` v1): 1 climate change and input costs; 2 new CEO execution; 3 debt management (hold).

## 2. Key risks proposed (5)

| ID | Risk: cause → effect → driver → value | Pillar | P | I | Value impact (Gordon / exit) | Mitigation | Priced in? |
|---|---|---|---|---|---|---|---|
| **R1** | Climate-driven wheat costs (CBOT Dec-26 US$6.865/bu, +35% y/y `[sourced]` Macro report; gross margin follows wheat with ~1-year lag, r = -0.74 `[calc]`) lower gross margin by 50 bp for good after hedges and pricing → `gross_margin` | 1 | 3 | 4 | **-Ps 6.13 (-18.3%) / -Ps 4.40 (-9.6%)** `[calc]`. A one-year hit (-100 bp in FY2027 only) costs just -1.9% / -1.4%: the risk is a structural step, not a bad year | Hedges (book ~Ps 315m, 64% wheat `[calc]`), pricing, productivity; hedges delay the cost by about a year | **No**: consensus gross margin 52.3% / 52.0% / 52.05% `[sourced]` CIQ has no step down |
| **R2** | The North America turnaround stalls under the new CEO: NA Adj. EBITDA margin back to FY2024's 8.4% from 9.6% LTM `[sourced]`/`[calc]` (-2,081 on LTM NA sales 179,408) → `opex_pct_revenue` +0.49 pp | 2 | 3 | 4 | **-Ps 6.10 (-18.2%) / -Ps 4.38 (-9.6%)** `[calc]` | Transformation program, plant closures, price/mix; NA margin 10.0% in 2Q26 `[sourced]` | **Partly** `[assumption]`: the model assumes ~20 bp a year of consolidated EBITDA-margin gains to FY2030 (productivity), not a North America-specific path |
| **R3** | Capital allocation breaks the debt hold: capex re-accelerates (+50 bp of sales in FY2026-28) or a large deal at 8-9x EBITDA (+0.29x leverage per US$1bn `[calc]` wiki), and S&P's BBB+ negative outlook (since 20-Mar-2025 `[sourced]`) becomes a downgrade (+50 bp on Kd) → `capex_pct_revenue`, `pre_tax_cost_of_debt` | 3 | 3 | 3 | Capex: **-Ps 1.46 (-4.4%) / -Ps 1.46 (-3.2%)**; Kd +50 bp: **-Ps 1.96 (-5.9%) / -Ps 0.97 (-2.1%)** `[calc]` | 2026 capex guide cut to US$1.0-1.2bn `[guidance]`; net debt 137,097 at Jun-26 `[sourced]`; undrawn US$2,350m revolver | **Partly** |
| **R4** | Mexico policy (central case -100 bp scored; -150 bp would score 5): 46-hour week in 2027 and 40 hours by 2030 (route network is labour-intensive), IEPS above 8% (tail), NOM-051 phase 3 in 2028 → Mexico margin -100 to -150 bp on LTM Mexico sales 158,321 → `opex_pct_revenue` +0.38 to +0.56 pp | 2 | 3 | 4 | **-Ps 4.73 to -Ps 6.98 (-14.1% to -20.8%) / -Ps 3.40 to -Ps 5.01 (-7.4% to -11.0%)** `[calc]` | Reformulation, pricing, route productivity; no new IEPS rate in the 2027 package (Ley de Ingresos not final at 17-Oct) `[sourced]` | **Partly**: IEPS 8% in the base; hours not modelled |
| **R5** | The exit multiple lands at the core bakery median of 5.53x (one claim basis) `[calc]` peer workbook v3 instead of the 6.0x base → `exit_ev_ebitda` | valuation (no pillar yet) | 3 | 3 | Exit only (scored on the exit change): **-Ps 4.32 (-9.5%)** vs the 6.0x base; from Bimbo's 7.12x today to 5.53x the fall is **-Ps 14.54** (55.94 to 41.39); the reverse case (exit at 7.12x) is **+Ps 10.22 (+22.4%)** `[calc]` | Mexico's ~20% margin and the DSD network argue for a premium to US bakers | **Partly**: the base 6.0x sits between the two |

**Kill criteria** (thresholds are `[sourced]` history; their use as triggers is `[assumption]`). `research/thesis.md` v1 has no kill criteria yet (team). The candidates proposed in the thesis journal (2026-10-17) map to these risks: R1 → gross margin below the 2022 trough (51.76%) for two quarters; R2 → NA margin back below 8.4%; R3 → net debt / EBITDA above the Dec-2024 peak of 2.9x.

## 3. Downside scenario (run on a copy of the project)

R1, R2 and R4 hit together and the multiple de-rates to the core (R5). The scenario changed only these inputs in a copy of the project (`model/drivers.yaml` and `valuation/valuation.yaml` of the copy; the team's base files were not touched): `gross_margin` -50 bp every year; `opex_pct_revenue` +0.87 pp every year (NA to 8.4%, +0.49 pp; Mexico -100 bp, +0.38 pp); exit multiple 5.53x. The copy was rebuilt with the engine (`build_model.py --project <copy>`; 123 checks OK).

| Case | FY2026 Adj. EBITDA margin | Gordon | Exit | vs MXN 58.60 (Gordon / exit) |
|---|---|---|---|---|
| Base, published basis (gate) | 14.70% | 33.55 | 45.72 | -42.7% / -22.0% |
| **Downside, published basis** | 13.33% | **16.58** | **29.60** | -71.7% / -49.5% |
| Base, engine basis (reconciliation) | 14.70% | 39.48 | 43.08 | |
| Downside, engine basis (copy's `model/model-summary.json`) | 13.33% | 22.51 | 26.97 | |

`[calc]`. The published basis is the one the report quotes. In the downside the terminal return on new capital falls to 12.5% (from 14.6%) and the price would need 7.6% perpetual growth.

**Reading.** Margins carry the risk: the three operating risks together cost about half of the Gordon value, while the multiple alone costs a tenth of the exit value. A judge will ask which of the three margin risks the thesis can rule out.

## 4. Appendix: remaining risks

| ID | Risk | Category | P | I | Note |
|---|---|---|---|---|---|
| R6 | Peso depreciation below the ~1.5% a year inside NA growth (US CPI 3.74% vs Mexico 3.45%, Sep-2026 `[sourced]`) | financial | 3 | 3 | PPP at the inflation targets: Gordon 31.37 (-6.5%), exit 44.80 (-2.0%) `[calc]` DCF v3 'Scenarios'; at survey inflation +2.2% |
| R7 | USMCA not renewed (annual reviews to 2036) and tariffs | regulatory | 3 | 2 | Local production; the US declined to renew on 1-Jul-2026 `[sourced]` (BIMBOA/research/risks.md §3) |
| R8 | GLP-1 and health habits | market | 3 | 2 | Grocery spend -5.3% six months after starting; snacks ~-10% (Cornell/JMR, observational) `[sourced]`; no bread figure |
| R9 | Governance: family control 72.03%, 38.9% independent board, anti-takeover clauses | governance | 4 | 2 | Shows in the multiple, not in the cash flows (`research/esg.md`) |
| R10 | Canada Bread class actions without provision | governance | 2 | 1 | Fine US$38m paid in 2023 `[sourced]` RA25 |
| R11 | US multi-employer pension plans | financial | 2 | 1 | In the bridge (MEPP 738.75 after tax) `[sourced]`/`[calc]` |
| R12 | Water stress, water and circular-economy laws, Scope 3 target missed | ESG | 4 | 1 | Not quantifiable: no climate capex or EPR cost disclosed (`research/esg.md`) |
| R13 | Cyber attack | operational | 2 | 2 | RA25 pp.36-37 |
| R14 | Argentina, Venezuela, Russia | operational | 2 | 1 | Latin America ~6% of segment EBITDA `[calc]` |

## 5. Coach moments (team decides; logged in `docs/context/thesis-journal.md`)

1. **Which 4-6 risks threaten the thesis?**
   - *Recommendation:* R1, R2, R4 and R5, plus R3 for the debt pillar. They move a pillar or the value by more than 5% and each has a number.
   - *Strongest case against:* R5 is the mirror of the valuation call, not a business risk; and R4 is linked to pillar 2 only as the assistant's proposal (management must offset it), not by the team.
   - *Question:* which pillar does Mexico's labour and tax policy belong to, or does it need its own place in the story?
2. **Mitigated, priced in, or neither?**
   - *Recommendation:* R1 neither (consensus margins show no structural step); R2, R3 and R4 partly; R5 partly.
   - *Strongest case against:* "not priced in" for R1 cannot be proven: consensus does not split gross margin by input.
   - *Question:* what market data would show that the 2026 wheat move is already in the price?

## 6. Sources

`valuation/valuation.md` v3 and `valuation/BIMBOA_DCF_v3.xlsx` (sensitivities, Scenarios); `valuation/BIMBOA_PeerAnalysis_v3.xlsx`; `model/drivers.yaml`; `wiki/Risks-ESG/bimbo-risk-factors.md` (RA25 pp.22-61); `wiki/Risks-ESG/bimbo-climate-metrics-capiq-2026-10.md`; `wiki/Macro/bimbo-input-costs.md`; `wiki/Thesis/bimbo-leverage-and-deleveraging-commentary.md`; `BIMBOA/research/industry/industry-report_2026-10-17.md`; `reports/Bimbo macro outlook 2026.md`; `BIMBOA/research/risks.md` (2026-10-14, facts verified then: USMCA, IEPS).
