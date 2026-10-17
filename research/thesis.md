# Investment thesis — Grupo Bimbo, S.A.B. de C.V. (BIMBOA)

_Version 1 — 2026-10-17 — status: draft (pillars chosen by the team on 2026-10-16; claims, variant perception, kill criteria and direction still to be written by the team)_

This file synthesises what the team has decided so far and puts the evidence next to each pillar. The pillar titles and the debt "hold" stance are the team's (`docs/context/memory.md`, 2026-10-16). Text marked **[team]** is waiting for the team's own wording; the assistant has not supplied it. The coaching questions for each gap are in `docs/context/thesis-journal.md` (2026-10-17).

## One-line thesis

We rate Grupo Bimbo a **[team: BUY / HOLD / SELL — provisional until the team sets the target]** because **[team: pillar 1 — climate change and input costs]**, **[team: pillar 2 — the new CEO's execution]** and **[team: pillar 3 — debt management, a hold]**, which the market misses because **[team]**.

Where the evidence stands today:
- The assistant's DCF proposals value the share below the price: Gordon MXN 33.55 (-43%) and exit MXN 45.72 (-22%) vs MXN 58.60 `[calc]` `valuation/valuation-outputs.yaml` v3.
- Consensus is Hold (2.58) with a mean target of MXN 70.17 (12 analysts, 20-Sep-2026) `[sourced]` CIQ, `wiki/Thesis/ciq-sell-side-sentiment-facts.md`.
- The team's earlier draft (`output/bimbo-tesis-3-pilares.md`, 2026-10-08) said BUY on historical multiples, with different pillars. It is superseded by the 2026-10-16 pillar decision and is kept for the record.

## Pillars

### Pillar 1 — Climate change and input costs

- **Claim:** **[team]** (direction not yet stated: is climate a risk the market underprices, or a cost headwind it overprices?).
- **Evidence:**
  - Raw materials are about 30% of net sales and 64% of cost of sales (FY2025) `[calc]` `wiki/Macro/bimbo-input-costs.md`.
  - Wheat is the climate exposure that reaches the P&L. Gross margin moves against wheat with about a one-year lag (r = -0.74 over 2017-2025, n = 9; small sample, lag chosen after looking at the data) `[calc]`. In 2022, average wheat rose 26.5% while gross margin fell 197 bp (53.73% to 51.76%) `[calc]`; the correlation does not prove the whole fall was wheat `wiki/Risks-ESG/bimbo-climate-metrics-capiq-2026-10.md`.
  - Management commentary turned from "lower raw materials" (1Q24-1Q25) to "higher raw materials" (3Q25, 4Q25, 2Q26); 2Q26 gross margin 52.6% (-20 bp) `[sourced]` quarterly releases.
  - Hedge book at end-2025 about Ps 315m, 64% wheat `[calc]`; about 100% of 2H25 needs and more than half of 1Q26 were hedged. The one-year lag fits a rolling hedge book `[assumption]`, and 2026 wheat is running about +17% `[unverified]` (Capital IQ AI run, `wiki/Risks-ESG/bimbo-climate-metrics-capiq-2026-10.md`), so the pressure would show in 2027.
  - 61% of the 2.39 pp raw-material relief of FY2023-FY2025 was absorbed by labour, depreciation and other cost lines `[calc]` `wiki/Thesis/bimbo-evidence-vs-mentor-tests.md`.
  - Physical and regulatory exposure: 101 plants in high water stress (a second Capital IQ run says 89; unreconciled) `[unverified]`; Mexico's cap-and-trade is the one climate rule management says will hit profits, and its operating rules are unpublished `[sourced]`.
- **Consensus view:** gross margin 52.3% / 52.0% / 52.05% for FY2026-FY2028 `[sourced]` CIQ consensus 20-Sep-2026.
- **Why the market is wrong:** **[team]**.
- **Model link:** `gross_margin` in `model/drivers.yaml` (52.4% FY2026, 52.0% FY2027, 52.5% from FY2030): ±50 bp of gross margin = ±Ps 6.13 per share (DCF v3 Levers) `[calc]`. The model sits on consensus, so this pillar has no variant view in the numbers yet.

### Pillar 2 — The new CEO's execution

- **Claim:** **[team]**.
- **Evidence:**
  - Alejandro Rodríguez Bas (Barcel and PepsiCo background) is CEO since November 2025; two CEO changes in about 18 months (May 2024 and November 2025), and the second exit is unexplained in every file read `[sourced]`/`[calc]` `wiki/Thesis/bimbo-ceo-and-management-changes.md`.
  - 2026 guidance was raised in July: Adj. EBITDA margin +70 to +120 bp, capex US$1.0-1.2bn, leverage about 2.5x `[guidance]` 2Q26 call.
  - North America Adj. EBITDA margin rose from 5.9% (4Q24) to 10.0% (2Q26), four straight quarters of year-on-year expansion; ex-FX sales turned positive only in 1Q26 (+0.7%) and 2Q26 (+1.3%) after eight negative quarters `[sourced]` `wiki/Thesis/bimbo-north-america-turnaround-evidence.md`.
  - Attribution: the files do not support crediting the CEO. The cost program was designed under the predecessor, and the improvement also rests on easy comparisons, one-offs and FX `[calc]` wiki.
- **Consensus view:** Adj. EBITDA MXN 62.1 / 64.9 / 69.0 bn for FY2026-FY2028 `[sourced]` CIQ consensus; the model is within ±1.1% (62.3 / 64.2 / 68.9 bn) `[calc]`.
- **Why the market is wrong:** **[team]**.
- **Model link:** `opex_pct_revenue` (Adj. EBITDA margin 14.7% FY2026 to 15.3% FY2030). For the DCF to reach the price on this lever alone, the margin would need +201 bp in every year `[calc]` `valuation/valuation.md` §8.

### Pillar 3 — Debt management: a hold

- **Claim:** the team's stance is **hold**, measured against all comparables, US and Mexican (team, 2026-10-16). The earlier claim "2x the debt of its competitors" was dropped.
- **Evidence:**
  - Net debt / EBITDA 2.5x at 2Q26 on the company's definition `[sourced]` call 2026-07-23 p.10. On one claim basis with leases (peer workbook v3) Bimbo is at 2.81x against a 2.98x median of nine peers, 5th least leveraged of 10 `[calc]`. The team's 16-Oct reading (6th of 9, median 3.20x, Capital IQ basis) is the earlier, mixed-basis view `[sourced]` thesis journal 2026-10-16.
  - The stated ceiling moved: <2x was held only from Dec-2020 to 3Q23; the ratio reached 2.9x at Dec-2024; the target became 2.0-2.5x and then "around 2.5x" `[sourced]`/`[calc]` `wiki/Thesis/bimbo-leverage-and-deleveraging-commentary.md`.
  - 2025 deleveraging (2.9x to 2.7x) leaned on capex under-spend, FX and a halved buyback `[calc]` wiki.
  - 44% of debt is USD-denominated `[sourced]` RA25; maturities cluster in 2028 (MXN 16.0 bn) and 2029 (MXN 19.1 bn), with an undrawn US$2,350m revolver `[sourced]` `wiki/Thesis/bimbo-catalyst-calendar-facts.md`.
  - In the model, net debt / EBITDA falls to 0.76x by FY2035 because cash piles up (no new debt, 38% payout) `[calc]` `model/review.md`. That is not a "hold": the team has to say what the cash is used for.
- **Consensus view:** Capital IQ net debt FY2025 MXN 149,031m (brokers' definition, without leases) and consensus FY2026E 146,911m `[sourced]` `wiki/Valuation/ciq-consensus-estimates.md`; with leases the FY2025 claim basis is 182,232 `[calc]`.
- **Why the market is wrong:** **[team]**.
- **Model link:** `net_new_debt` and the payout in `model/drivers.yaml`; the DCF (FCFF) does not depend on them, the leverage path does.

## What works

- The North America margin recovery is documented quarter by quarter from sourced releases (5.9% to 10.0%), and is the strongest operating fact available `[sourced]`.
- The debt pillar now rests on a full peer set (nine peers, one claim basis), not on a selective comparison `[calc]` `valuation/BIMBOA_PeerAnalysis_v3.xlsx`.
- The valuation is verified and reproducible (24/24 checks, 30/30 against the engine, 61/61 against the replica) `[calc]` `valuation/verification-v3.json`, so the team can debate assumptions instead of arithmetic.

## Catalysts (next 12 months)

| Catalyst | Expected timing | Pillar | How we will know |
|---|---|---|---|
| 3Q26 results | late Oct-2026 (history: 26-29 Oct; date to confirm) `[sourced]` | 1, 2, 3 | gross margin vs 52.6% (2Q26) `[sourced]`, NA margin vs 10.0% `[sourced]`, net debt / EBITDA vs 2.5x `[sourced]` |
| FY2026 results and 2027 guidance | 19-27 Feb-2027 (history) `[sourced]` | 2, 3 | margin delivery vs +70-120 bp `[guidance]`; 2027 capex guide |
| Wheat into the 2027 hedge book | 1H27 | 1 | gross margin direction one year after the 2026 wheat move |
| AGM: dividend and buyback | by about end-Apr-2027 `[sourced]` | 3 | payout vs leverage |
| Mexico cap-and-trade operating rules | not dated `[sourced]` | 1 | SEMARNAT publication |
| USMCA review outcome and tariffs | after July 2026 (fresh source needed) `[sourced]` | 1, 2 | tariff exposure of Mexican imports into the US |

## Kill criteria — what would change our mind

- **[team]** One per pillar, stated as a number and a date. The assistant's coaching question for each is in the thesis journal (2026-10-17).

## Red flags still open

- **Direction vs valuation.** The assistant's DCF proposals sit 22-43% below the price, while consensus targets sit 20% above it. The thesis direction has to explain which assumption the team believes: terminal capex (6.0% in the model vs about 5.0% consensus; ±50 bp = ∓Ps 9.4), the exit multiple (6.0x vs Bimbo's 7.12x today) or the cost of capital `[calc]` `output/dcf-v3-conclusiones.md`.
- **No operating variant view yet.** Model EBITDA and gross margin sit on consensus, so none of the three pillars shows a gap versus consensus in the numbers.
- **CEO attribution.** The improvement predates the CEO and the second CEO exit is unexplained; a judge will ask what the CEO has changed.
- **Consensus EPS revisions are still negative:** FY2026 EPS -21% over 18 months while targets rose `[sourced]` CIQ.
- **Water-stress plant count** differs between two Capital IQ runs (101 vs 89) `[unverified]`.
- **Dividend per share FY2026:** MXN 1.075 (AGM notice, 13-Apr-2026); the 1.75 in the BMV Jun-26 filing is a typo `[sourced]` `wiki/Thesis/bimbo-catalyst-calendar-facts.md`.

## Next moves

1. The team writes the one-line thesis with a direction, after deciding terminal capex and the exit multiple (the two assumptions that separate the DCF from the price).

## History

- v1 2026-10-17: first synthesis in this file. Pillars as decided by the team on 2026-10-16 (climate change and input costs; new CEO execution; debt management, hold). Evidence added from the wiki and valuation v3 with tags. Claims, variant perception, kill criteria and direction left for the team. Superseded draft: `output/bimbo-tesis-3-pilares.md` (2026-10-08: BUY; pillars NA margin recovery, capex moderation and FCF, valuation discount).
