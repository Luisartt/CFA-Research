# Investment thesis — Grupo Bimbo, S.A.B. de C.V. (BIMBOA)

_Version 2 — 2026-10-19 — status: the three theses are locked (team validation, 2026-10-19); direction (rating) and target price still open_

The team validated three theses on 2026-10-19, as written in the first report draft (`report/BIMBOA_report_v1_draft.pdf`, Investment Summary; `docs/context/memory.md`). Format: "Problem — due to [cause]" (team format, 2026-10-19). They replace the three pillars of 2026-10-16 (climate and input costs; new CEO execution; debt management, a hold), kept in History. The assistant proposed the wording and the sizing; the team accepted them as the base. Every sensitivity below is `[calc]` on the consolidated DCF (`valuation/consolidated-valuation.md`, `report/build/report_levers.py`, `report/data/levers.json`; exit-multiple method, MXN per share, base value 46.42). Text marked **[team]** is waiting for the team's own wording.

## One-line thesis

We rate Grupo Bimbo a **HOLD (provisional until the team sets the exit multiple and the target price)** because North America's margin problem is being corrected (upside) while 2027 margins are at risk from wheat and organic growth may fall short of the model (downside); the three roughly offset (-MXN 2.65 net on a base value of MXN 46.42). What the market misses: **[team]**.

Where the numbers stand:
- Base DCF, exit multiple 5.92x: MXN 46.42 today, MXN 51.42 in 12 months, expected return -10.5% against MXN 58.60 (SELL edge, -10% or lower) `[calc]` `valuation/inputs/consolidated_results.json`.
- The price requires an exit multiple of 6.95x (Bimbo trades at 6.94x LTM; core bakers 5.53x). A clean HOLD (expected return -5% to +10%) needs 6.16x to 6.82x; BUY needs 7.04x or more `[calc]` project convention (`references/recommendation-guide.md`).
- Consensus is Hold (2.58), mean target MXN 70.17 (12 analysts, 20-Sep-2026) `[sourced]` CIQ, `wiki/Thesis/ciq-sell-side-sentiment-facts.md`.

## Theses

### Thesis 1 (upside) — North America's margin problem is being corrected, due to cost restructuring and better price/mix, with capex normalised and Mexico funding the turnaround

- **Claim:** as stated in the title (team, validated 2026-10-19). Attribution to the new CEO is not claimed: the programme was designed under the predecessor `[calc]` `wiki/Thesis/bimbo-ceo-and-management-changes.md`.
- **Evidence:**
  - North America Adj. EBITDA margin 5.9% (4Q24) to 10.0% (2Q26); year-on-year expansion of +90, +330, +120 and +100 bp in the last four quarters `[sourced]` 3T25 p.5, 4T25 p.6-7, 1T26 p.5, 2T26 p.5 via `wiki/Thesis/bimbo-north-america-turnaround-evidence.md`.
  - Net sales ex-FX +0.7% (1Q26) and +1.3% (2Q26) after eight negative quarters; management reports share gains in all US categories in 2Q26, the first time since 2020 (no share data) `[sourced]`/`[guidance]` 2T26 p.3.
  - Causes cited by management: 11 bakery closures worldwide in 2024, "record productivity benefits" from 3Q25, lower raw materials, better price/mix, lower restructuring spend `[sourced]` RA25 p.76-77; 4T25 p.7; 2T26 p.5. Regional gross margin 52.0% to 55.3% (4Q24 to 2Q26) `[calc]`.
  - Cash: capex (PP&E acquired) MXN 34,754m in FY2023 to 22,530m in FY2025; cash flow from operations +20% to a record 47,753m `[sourced]` IA25-EEFF p.85-86. Mexico earns about 55% of Adj. EBITDA at a 20.4% margin `[sourced]` Celebramos p.17 `[calc]`.
- **Consensus view:** Adj. EBITDA MXN 62.1 / 64.9 / 69.0bn for FY2026-FY2028 `[sourced]` CIQ consensus; the DCF is within 0.6% (62.2 / 64.5 / 68.9bn) `[calc]`.
- **Why the market is wrong:** **[team]**.
- **Model link:** `seg_north_america_growth` and the EBITDA margin path in `model/drivers.yaml`; DCF margin 14.6% (FY2026E) to 15.0% (FY2030E) `[calc]`.
- **Value:** North America earns 9.6% LTM against 11.1% for Flowers Foods on a lease-comparable basis `[calc]` peer workbook v3. Closing the 150 bp gap = +4.22; each +100 bp = +2.81 `[calc]`.
- **Against:** the recovery is margin-led, not volume-led, and no volume/price/mix split or programme size (capex, savings, end date) is disclosed `[sourced]` wiki; the margin is still below Flowers.
- **Kill criteria (as drafted, validated with the draft):** a year-on-year fall in North America's margin in 3Q26 (3Q25: 10.4%) or capex back above 6% of sales.

### Thesis 2 (downside) — 2027 margins are at risk, due to wheat, with futures up 35% year on year and hedges placed at 2025 prices rolling off

- **Claim:** as stated in the title (team, validated 2026-10-19).
- **Evidence:**
  - Raw materials are 30.4% of sales and 63.8% of cost of sales (FY2025) `[sourced]` EEFF25 p.82 `[calc]`; wheat flour is the principal input, priced in USD `[sourced]` RA25 p.97.
  - Gross margin moves against wheat with about a one-year lag (r = -0.74, 2017-2025, n = 9; small sample, lag chosen after looking at the data) `[calc]`.
  - CBOT Dec-26 wheat US$6.865/bu, +34.9% y/y (8-Oct-2026); Dec-27 is +5.4% over Dec-26 `[sourced]` Trading Economics; IndexBox/USDA AMS (7-Oct-2026), `research_notes/Bimbo macro outlook 2026/input_costs_commodities.md`. Hedges placed at 2025 prices roll off into 2027, so 1H27 is the likely cost peak `[assumption]`; Bimbo's 2027 hedge coverage is not public.
  - FY2025 cost leakage: salaries +7.5%, depreciation +13.3%, other lines +12.3% against sales +4.6%; gross margin -30 bp to 52.3% `[sourced]` EEFF25 p.82 `[calc]`. 61% of the 2.39 pp raw-material relief of FY2023-FY2025 was absorbed by labour, depreciation and other lines `[calc]` `wiki/Thesis/bimbo-evidence-vs-mentor-tests.md`.
- **Consensus view:** gross margin 52.3% / 52.0% / 52.05% for FY2026-FY2028, no structural step down `[sourced]` CIQ consensus 20-Sep-2026.
- **Why the market is wrong:** **[team]**.
- **Model link:** gross margin / EBITDA margin; the DCF has a 10 bp dip in FY2027E `[calc]`.
- **Value:** -50 bp from FY2027E for good = -3.55; -100 bp for good = -7.09; -100 bp in 2027 only = -0.66 `[calc]`.
- **Against:** 2Q26 gross margin 52.6% (-20 bp y/y); 2026 margin guidance raised to +70 to +120 bp `[guidance]` 2Q26 call; hedges delay the cost.
- **Kill criteria (as drafted):** gross margin above 52.5% in 3Q26 and 4Q26, together with 2027 guidance that absorbs wheat.

### Thesis 3 (downside) — Organic growth falls short of the model, due to record private label, a shrinking US bread category and a Mexico that slowed to +2.4% in 2025

- **Claim:** as stated in the title (team, validated 2026-10-19).
- **Evidence:**
  - What the forecast needs: the regional build has North America at +1.5% a year in USD (+1.5% peso depreciation = 3.0% in pesos) while the US bread category loses 2-4% of units and price/mix adds 1-2%, so Bimbo must outgrow its category by about 3 points; Mexico at +5.0-5.5% a year against a 3.5% market CAGR (Global Data 2024-29E), about 0.3 points of share gain a year from 18.2% `[assumption]`/`[calc]` `research/industry.md` §7.
  - Private label is about 35% of US fresh bread units `[sourced]` Flowers 10-K FY2025 and a record 23.8% of US grocery unit sales in 1H26 `[sourced]` PLMA/Circana via Bakery & Snacks (9-Jul-2026); Flowers Foods' volume -5.8% in 2Q26 `[sourced]` Investing.com.
  - Mexico net sales +4.0% (2024) and +2.4% (2025) `[sourced]` RA25 p.133; North America ex-FX -4.6% (2024) and -4.0% (2025) `[sourced]` 4T25 p.4.
- **Consensus view:** not collected for revenue by region.
- **Why the market is wrong:** **[team]**.
- **Model link:** `seg_north_america_growth` and `seg_mexico_growth`; group growth -0.5% (FY2026E) then 4.4-4.8% a year (CAGR FY2026E-FY2030E 4.6%) `[calc]`.
- **Value:** North America -1 pp a year = -1.12; Mexico -2 pp a year = -2.17; both = -3.29 `[calc]`.
- **Against:** 1H26 contradicts part of it (Mexico +4.5% and +4.7%; North America ex-FX +0.7% and +1.3%) `[sourced]`; the forecast grows revenue above the 4.2% a year expected for Bimbo's markets `[calc]`.
- **Kill criteria (as drafted):** Mexico above +5% for two quarters in a row, or North America above +2% excluding currency.

### The three together

All three at once: -2.65, from 46.42 to 43.77 at the base multiple (thesis 1 offsets about 60% of the two downside theses) `[calc]`. None of the three argues for a premium multiple by itself: thesis 1 moves North America toward a baker that trades at 5.6x (Flowers); a premium would have to come from Mexico (about 55% of EBITDA) `[assumption]`.

## Context kept from v1 (debt management, retired as a pillar)

- Net debt / EBITDA 2.5x at 2Q26 on the company's definition `[sourced]` call 2026-07-23 p.10; 2.81x with leases against a 2.98x peer median (5th least leveraged of 10) `[calc]` peer workbook v3.
- 2025 deleveraging (2.9x to 2.7x) leaned on capex under-spend, FX and a halved buyback `[calc]` `wiki/Thesis/bimbo-leverage-and-deleveraging-commentary.md`; 44% of debt is USD; undrawn US$2,350m revolver `[sourced]`.
- It stays in the report as a risk (R3) and in the Financial Analysis, not as a thesis.

## What works

- The North America recovery is documented quarter by quarter from sourced releases and is the strongest operating fact available `[sourced]`.
- Each thesis is sized in MXN per share on one DCF, with the strongest counter-evidence next to it `[calc]`.
- The valuation is verified and reproducible (replica equals the workbooks to 0.00) `[calc]` `valuation/build/consolidate_models.py`.

## Catalysts (next 12 months)

| Catalyst | Expected timing | Thesis | How we will know |
|---|---|---|---|
| 3Q26 results | late Oct-2026 (history: 26-29 Oct; date to confirm) `[sourced]` | 1, 2, 3 | North America margin vs 10.4% (3Q25) and 10.0% (2Q26); gross margin vs 52.6% (2Q26); Mexico growth vs +4.7% and North America ex-FX vs +1.3% `[sourced]` |
| FY2026 results and 2027 guidance | 19-27 Feb-2027 (history) `[sourced]` | 1, 2 | margin delivery vs +70-120 bp `[guidance]`; 2027 capex guide; how 2027 absorbs wheat |
| Wheat into the 2027 hedge book | 1H27 `[assumption]` | 2 | gross margin one year after the 2026 wheat move |
| AGM and FY2026 dividend | by about end-Apr-2027 `[sourced]` | context | dividend per share vs MXN 1.075 |
| Mexico cap-and-trade operating rules | not dated `[sourced]` | 2 | SEMARNAT publication |
| USMCA review outcome and tariffs | after July 2026 (fresh source needed) `[sourced]` | 2, 3 | tariff exposure of Mexican imports into the US |

## Red flags still open

- **Direction vs valuation.** The rating hangs on one judgement, the exit multiple: 5.92x gives -10.5% (SELL edge); a clean HOLD needs 6.16x-6.82x; the price needs 6.95x; consensus targets sit 20% above the price `[calc]`/`[sourced]`.
- **No stated variant view.** The DCF EBITDA sits within 0.6% of consensus, and the theses are sized risks and opportunities around it; none yet says what consensus misses. A judge will ask `[calc]`.
- **Evidence gaps behind thesis 1 and 3:** North America volume/price/mix and programme size are not disclosed; no Circana share series; the Mexican share gain (about 0.3 points a year) has no named source.
- **Thesis 3 is partly contradicted by 1H26** (see Against).
- **Consensus EPS revisions are still negative:** FY2026 EPS -21% over 18 months while targets rose `[sourced]` CIQ.
- **Water-stress plant count** differs between two Capital IQ runs (101 vs 89) `[unverified]` (ESG, not a thesis).

## Next moves

1. The team decides the exit multiple on its own evidence; the target price and the rating follow.
2. The team states, for each thesis, what the market misses (the **[team]** slots).

## History

- v2 2026-10-19: the team validated the three theses as drafted in the first report (one buy, two sell, format "Problem — due to"). They replace the pillars of 2026-10-16. Evidence, sizing (consolidated DCF) and the drafted kill criteria carried over; claims "why the market is wrong" and direction left for the team. The debt-management pillar became context and a risk.
- v1 2026-10-17: first synthesis. Pillars as decided by the team on 2026-10-16: (1) climate change and input costs, (2) the new CEO's execution, (3) debt management, a hold. Superseded draft: `output/bimbo-tesis-3-pilares.md` (2026-10-08: BUY; pillars NA margin recovery, capex moderation and FCF, valuation discount).
