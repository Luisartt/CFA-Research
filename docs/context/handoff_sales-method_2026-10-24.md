# Handoff — FY2027E-FY2030E sales method (2026-10-24)

Owner: Jorge Alejandro Gaytan. Coach in simple Spanish; write files in English.
Worktree: `.claude/worktrees/dcf-balance-general-dd4b56` (branch `claude/bimbo-financial-statements-2026-2030-c392ec`). Nothing committed.

## Standing rules (from the user, keep them)
- No commit, stash, checkout, merge, push, cleanup, moving or overwriting files unless the user confirms. Diff before overwriting the Spanish workbook in the main checkout.
- Public information only. No own estimates or illustrative numbers unless asked. Never invent data or present correlation as causation. No future acquisitions without support.
- Every number carries a tag: [sourced] / [guidance] / [assumption] / [calc] / [unverified]. Log all AI work in `docs/context/ai-use-log.md`.
- Do not use what management says about its own stock. The team decides thesis, key assumptions, target and rating. Calibrate theses to the statements, not the reverse.
- Do not revert the diesel and foreign-currency-debt records already in the files.
- Capital IQ answers: only values stored explicitly; discard anything ChatIQ computed itself.
- Before writing any data request: check `filings/` and `data/` first, and ask the team what is known not to exist (`lessons.md`).

## Goal
Replace the FY2027E sales CAGR (1.71%, still in `model/BIMBOA_statements_2021-2030_v1.xlsx`) with the advisor's method (decision in `memory.md`, 2026-10-24): growth per region (Mexico, North America, EAA, Latin America) = team-chosen ratio x a macro or industry variable; organic only; local currency ex-FX, consolidated in MXN through each region's FX path. Then close the FY2027E BS/CF and project FY2028E-FY2030E. Due 2026-10-26 (sales), 2026-10-27 (statements).

## Data collected (all in `data/capitaliq/`, verbatim with AI review notes at the top)
| Block | Content | Status |
|---|---|---|
| First pull | `BIMBOA/research/Informacion_BIMBO_macro.txt` (macro + FX; FX tables lines 1020-1184) | base |
| M1-M5 | MEX/USA/CAN; ARG/BRA/CHL/COL; CRI/ECU/SLV/GTM; HND/NIC/PAN/PRY; PER/URY/VEN: real GDP, nominal GDP (LCU), CPI, real private consumption, population, 2015-2030 | usable with flags |
| X1 | Same-basis history, Americas: no separate Standardized history exists; spliced "As reported ACTUAL" + "Standardized FORECAST" is the only series; PRY 2019 = 236.68 | usable |
| E1-E5 | GBR/CHE/ROU/SRB; SVN/HRV/MNE/MKD; RUS/UKR/TUR/KAZ; CHN/IND/KOR; ZAF/MAR/TUN | usable with flags |
| F1 | CLP/COP/PYG/KRW averages stored with 2 decimals, read as thousands per USD (decision in `memory.md`) | decided |
| F2 | KZT/TND/RSD 2026 monthly FX: no data; annual history and 2026-2030 forecasts are in the first pull | low impact |
| S1 | No data; redundant (regional sales already in `data/capitaliq/segments.csv`, `data/financials.csv`, `filings/`) | AI error |
| S2 | Bimbo never quantifies organic vs inorganic; acquisition calendar by region [guidance, unverified] | timeline only |
| P1 | Flowers/Aryzta/Yamazaki: no data | not usable |
| P2 | Mondelez organic growth by segment only; FY2024 = FY2025 rows duplicated, LatAm FY2020 and Europe FY2023 discarded; verify in Mondelez 10-K | [unverified] |
| I1 | No country-level industry data; only GlobalData global figures quoted by Bimbo (below) | global only |

### Industry anchors checked in local PDFs [sourced]
- `filings/quarterly/GB_Investor_PPT_3Q26.pdf` p.5: Baking US$674 Bn, CAGR 2020-25 3.8%, 2025-30 3.4%; Snacks US$110 Bn, CAGR 2020-25 5.0%, 2025-30 2.9% (ChatIQ misread three of these four).
- `filings/annual/IA25_GB_Celebramos_ESP_200826.pdf` p.16: Baking US$639 Bn (2.8%, 4.7%); Snacks US$183 Bn (4.7%, 3.8%); period labels to confirm on the page. The two vintages disagree (snacks 183 vs 110) [unverified which to use].

### Acquisition calendar (S2, [guidance, unverified] until checked in transcripts/releases)
- EAA: Vel Pitar comparable from 1Q24; Amaritta, Trei Brutari (1Q24); Moulin d'Or, Karamolegos, Don Don (from ~Jun-2025); "Bonel" Tunisia 3Q26.
- Latin America: Pagnifique (Sep-2024); La Zarcerena (1Q25); Wickbold (Oct-2025), out of inorganic from 4Q26.
- Mexico and North America: none named 2024-2026.
- FY2025 ex-FX growth: North America −4.0%, Mexico +2.4%, EAA +11.7%, Latin America +10.1% (check in the 4Q25 release in `filings/quarterly/`).

## Open checks before computing growth (Capital IQ screen or public source)
Screen run 2026-10-24: each nominal GDP step [calc] compared with (1 + real GDP growth) x (1 + CPI) - 1 from the same block [calc].
- KAZ 2026 +28.1% vs 15.3% implied, KOR 2026 +22.4% vs 6.0%, MAR 2026 +10.5% vs 5.3%: likely series breaks, only in the 2025→2026 step. 2027-2030 are consistent (KAZ 2027 12.4 vs 13.5; KOR 4.8 vs 4.6; MAR 4.8 vs 5.8). 2026 stays [unverified]; does not block FY2027E-FY2030E.
- UKR (new): gap 12.6pp in 2026 and 6.0pp in 2027. Affects FY2027E: 2026-2027 [unverified], check before using UKR.
- HRV: levels are euro-scale despite the "knB" label; one unit throughout, so growth is unaffected. Label stays as stored.
- SVN 2025: growth 5.5% vs 4.1% implied, consistent; flag conflict stays [unverified].
- VEN: unusable (2026 gap -109pp); all years [unverified].
- PRY 2026: flagged ACTUAL (label wrong), value 7.9% plausible; kept as [calc].
- India: calendar years confirmed.
- CLP/COP/PYG/KRW "thousands" unit to confirm.
- Hyperinflationary local-currency growth (ARG 2027 18.1%, TUR 2027 20.5% [calc]) would dominate any regional average: weighting is a team decision (open).
- Growth table saved as `data/macro/nominal_gdp_growth_2016-2030.xlsx` (live formulas, not CSV: the team wants every number linked to its source). Sheet `IAS29_test`: 3-year cumulative CPI [calc] from Capital IQ CPI; 100%+ in ARG (to 2027: 122%), TUR (to 2027: 115%), VEN (to 2028). Both ARG and TUR fall below 100% from 2028 in the forecasts.
- How Bimbo treats it [sourced]: applies IAS 29 to hyperinflationary subsidiaries and translates them at the closing rate (`filings/annual/IA25_GB_EEFF_V10.pdf` p.23, p.26). Argentina is inside Latin America ex-FX growth (3T26 release p.3-4: LatAm +15.2% ex-FX vs +12.4% in MXN, Argentina named as a driver). Bimbo does not exclude it; the FX translation offsets the inflation.
- Team rejected "anchor countries" (2026-10-24): no exclusion of real Bimbo markets without a calculation behind it. Proposed test: compare candidate regional aggregates with Bimbo's reported ex-FX growth by region, FY2016-FY2025 (from the 4Q releases in `filings/quarterly/`), and keep the one that tracks best.
- DECIDED 2026-10-25 (memory.md): follow Bimbo's method, every consolidated country in local currency, ARG/TUR included; VEN out (not consolidated since 1-Jun-2017). Workbook sheet `Regional_agg` aggregates at prior-year FX (weights = prior-year GDP in USD) [calc]: 2027 Mexico 6.7%, North America 5.5%, Latin America 7.9%, EAA 6.2%. EAA 2026-2027 carry [unverified] inputs (KAZ/KOR/MAR 2026, UKR 2026-2027). MKD out for lack of FX. Open: GDP weights vs Bimbo's unknown country mix (CHN 45% of EAA, BRA 48% of LatAm); the ratio per region.
- Ratio (2026-10-25, Jorge): historical ratio = Bimbo ex-FX growth by region / regional GDP growth, on the years in the statements. Sheet `Ratio_history` written in `model/build/build_macro_gdp.py` (yearly ratios and ratio of 2023-2025 CAGRs, live formulas) run 2026-10-25. Ratios [calc] FY2023/24/25, compound: Mexico 1.45/0.74/0.47, 0.96; North America 1.03/-0.83/-0.80, -0.13; Latin America 0.61/0.28/0.76, 0.48 (denominator swollen by ARG hyperinflation: LatAm GDP 27.8%/36.3%/13.4%); EAA 2.85/1.07/2.01, 1.98 (numerator includes acquisitions). Team (Jorge) rejects carrying a historical ratio forward mechanically: history is evidence, the ratio is the team's call.
- DECIDED 2026-10-25: North America ratio 0.17x = 1Q26-3Q26 ex-FX (+1.0%) / US nominal GDP 2026 (5.99%) [calc], sheet `Ratio_NA`; implied FY2027E-FY2030E 0.9/0.8/0.7/0.7% [calc]. DECIDED: Mexico 0.77x = 9M26 (+4.78%) / Mexico GDP 2026 (6.17%), sheet `Evidence_MEX`. 9M26 includes acquisitions: Stone House (NA, 2-Jun-2025), Wickbold (LatAm, all of 9M26), Don Don/Karamolegos (EAA 1Q26), Bonel (EAA from Apr-2026), sizes not disclosed. Consistency pass DONE (sheet `Ratios_9M26`): Latin America 1.32x (9M26 14.8% / GDP 11.2%), EAA 0.94x (7.4% / 7.9%) [calc]; implied FY2027E LatAm 10.5%, EAA 5.9%. Organic pass DONE (sheet `Organic_pass`, quarter-by-quarter before/after): NA 0.17x, Mexico 0.77x, LatAm 0.67x, EAA 0.56x [calc]; BASE CASE LOCKED 2026-10-25 (memory.md): organic ratios for all four regions. NEXT = step 4. Long-history cross-check DONE (sheet `Cross_check_history`, medians of yearly ratios): NA 0.15x (FY16-25), Mexico 1.24x (FY16-25), LatAm 0.68x and EAA 2.12x (FY22-25 only; no earlier ex-FX by region). Earlier note: organic-only pass for all four regions (Wickbold inorganic through 3Q26, comparable from 4Q26; Stone House, Don Don, Karamolegos, Bonel) and compare; then step 4 (put the growth into the statements workbook). Only FY2023-FY2025 have ex-FX growth by region [sourced] (wiki `bimbo-income-statement-fy21-fy25` §3b); FY2021-FY2022 not disclosed by region. Ex-FX includes acquisitions (not organic). Next: run the script, read the ratios, log in ai-use-log.

## Next steps (in order)
1. Run the screen checks above (or mark [unverified] and move on).
2. Compute nominal GDP growth per country [calc] from the levels; build regional aggregates (weights are a team decision: FY2025 sales by country are not disclosed, only by region).
3. Show the team the candidates side by side (real GDP + CPI, nominal GDP, real private consumption, global baking CAGR). Team picks variable, ratio per region and FX path. Coach: recommendation, strongest case against, one question.
4. Replace the FY2027E CAGR in the Excel; extend to FY2028E-FY2030E.
5. Close the FY2027E BS/CF; project FY2028E-FY2030E; rebuild EN/ES workbooks (`model/build/build_statements_workbook.py`, `model/build/statements_es.py`); diff before overwriting the Spanish copy in the main checkout.
6. Other open model items: interest rate 6.5% vs implied 7.47%; VPPA; "TACC" → "CAGR" in the Spanish workbook; R15 risk scoring.

## Step 4 status (2026-10-25)
- FY2027E sales now in the statements workbook (Assumptions rows 103-126, EN and ES rebuilt): organic ex-FX growth NA 0.91%, Mexico 5.19%, LatAm 5.31%, EAA 3.49%; 9M26 weights 39.8/37.3/10.9/12.1%; consolidated 3.29% [calc]; net sales FY2027E 441,950 MXN m [calc] (old CAGR: 433,962).
- PROVISIONAL: FX factor row 125 uses USD/MXN for every non-Mexico sale (same rule as 4Q26 and debt). Open for the team: keep the proxy or build a regional FX basket from `Regional_agg` (GDP in USD vs local currency). Recalculation of the Checks sheet not verified by a calc engine (pycel failed); open in Excel to confirm.
- Next: FX decision, then FY2028E-FY2030E, then close BS/CF.
- UPDATE 2026-10-25: provisional factor replaced. Sales by region (Assumptions rows 125-144): FY2026E split with the 9M26 mix (team approved, no 4Q seasonality: Mexico 4Q = 24.9% / 25.5% of FY2024 / FY2025), FX factor to MXN per region (Regional_FX sheet: LatAm 0.9749, EAA 0.9917 local->USD; x USD/MXN 17.77/17.70). FY2027E net sales 440,183; MXN growth 3.17% = business 3.29% + FX -0.13% [calc]. Non-recurring items (integration, restructuring, MEPP, impairments, asset-sale gains) removed from FY2027E. Checks sheet not recalculated by an engine. 4Q26 still uses the USD/MXN proxy (Bimbo guidance rule).
- UPDATE 2026-10-25 (later): FY2027E BS/CF/Equity/OCI closed with FY2026E methods; Excel full recalculation: Checks OK in FY2026E and FY2027E. Open for team: buybacks FY2027E (held at FY2026E 1,372, PROPOSED), payable days trend (83 -> 70 days FY2021-FY2025, held at 70.1), 4Q26 buybacks = 0 vs CFO "program continues", share count not reduced for buybacks, 2028 maturity not reclassified to current debt, EBITDA margin FY2026E includes restructuring (3,846) while FY2027E excludes it. Next: FY2028E-FY2030E.
