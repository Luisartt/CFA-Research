# Thesis journal

Append-only. One entry per coach moment:
`## YYYY-MM-DD — <skill> — <decision point>` then the question, the team's
answer, and what changed. Never edit past entries.
Soft cap: see AGENTS.md > Context files.

## 2026-10-16 — thesis — debt pillar scope

**Question:** the team said Bimbo has "2x the debt of its competition". After the Capital IQ pull, which peer set do you defend, and is the pillar bullish or bearish?
**Team answer so far:** narrow the claim to Mexican peers (Capital IQ shows Bimbo 2.5x net debt/EBITDA vs 3.20x peer median and 4.0x+ for Flowers/Campbell's; vs Arca 0.74x it is 3.4x higher). Direction not yet stated.
**What changed:** the pillar can no longer be "more leveraged than everyone". Open: only one Mexican peer has data (Gruma missing).


## 2026-10-16 — thesis — debt pillar stance
**Question:** with the full Capital IQ peer set, is the debt pillar bullish or bearish?
**Team answer:** hold. Use all comparables (US and Mexican), not only Mexican peers. The "2x the debt of competitors" claim is dropped from the thesis for now; the data goes to the wiki so it can be cited.
**What changed:** the pillar is a hold on debt. Bimbo is 6th of 9 on net debt/EBITDA (2.5x vs 3.20x peer median). Thesis wording to be rewritten later.

## 2026-10-17 — valuation v3 — cost-of-capital route and the gap to the price
**Question:** route B (default-free rf 7.51% + EBITDA-weighted CRP 2.05%) or route A (M-Bono 9.26%, no CRP)? And which assumption explains the gap between the DCF (Gordon 33.55, exit 45.72) and the price (58.60)?
**Team answer:** pending (the team asked for an automatic run without questions; the assistant's proposal is route B as the base).
**What changed:** valuation v3 is published on route B as a proposal. The gap comes mainly from terminal capex (6.0% vs consensus ~5.0% and peers 3.7-3.8%; 50 bp = Ps 9.4), the exit multiple (6.0x vs Bimbo's 7.12x) and beta; FX is not the gap. Discussion brief: output/dcf-v3-conclusiones.md.

## 2026-10-17 — update-macro — first load of the macro view
**Question:** confirm, correct or reject each observed macro field (M-Bono 9.26%, USD/MXN 18.479, Mexico CPI 3.45%, IMF 2.1% growth, Banxico survey, ERP 4.20%); does the weaker peso since June change the FY2026 revenue anchor; should the GDP cap use the 3.0% target or the survey's 3.7-3.8% inflation?
**Team answer:** pending (gate open; every field status: propuesto).
**What changed:** macro/macro-view.yaml created from observed, cited data; no model input changed. Triage in BIMBOA/journal/decisions.md.

## 2026-10-17 — thesis — synthesis v1 and open coach moments (team away; all pending)
**Question 1 (pillar selection):** recommendation: fold "new CEO" into the execution evidence or cut it, because the files do not support crediting the CEO (the cost program and the NA recovery predate him). Strongest case against: the CEO change is the most visible catalyst and judges expect a view on management. Question: what number in the next two quarterly reports would show the CEO's own impact?
**Question 2 (variant perception):** recommendation: place the variant view where the DCF disagrees with the price (terminal capex and the exit multiple), because model EBITDA and gross margin sit on consensus. Strongest case against: capex guidance was already cut and consensus expects about 5.0%. Question: in one number, where do you differ from consensus?
**Question 3 (kill criteria):** recommendation, one per pillar: gross margin below the 2022 trough (51.76%) for two quarters; NA Adj. EBITDA margin back below FY2024's 8.4%; net debt / EBITDA above the Dec-2024 peak of 2.9x. Strongest case against: thresholds taken from history may be too loose to ever trigger. Question: which of these would actually make you change the recommendation?
**Direction:** provisional until the team sets the target (DCF proposals below the price; consensus target above it).
**Team answer:** pending.
**What changed:** research/thesis.md v1 created from the 2026-10-16 pillar decision with tagged evidence; claims, variant view, kill criteria and direction left for the team.

## 2026-10-17 — industry-analysis — where Bimbo competes and what protects it (refresh)
**Question:** on one claim basis Bimbo trades at 6.94x LTM EV/EBITDA against 5.53x for the core bakers (Flowers, Gruma): what justifies the ~25% premium, and is it the Mexico DSD network or the snack mix? A second challenge: on a lease-comparable basis Flowers earns 11.1% EBITDA margin against 9.6% for Bimbo's North America, so where does scale show up in the US P&L?
**Team answer:** pending (team away).
**What changed:** BIMBOA/research/industry/industry-report_2026-10-17.md replaces the 12-Oct version as current; the relative-valuation reading flips from "in line with pure bakers" to "premium to the core"; the debt pillar's "in line with peers" holds (2.81x vs 2.98x median).

## 2026-10-17 — risks-esg — key risks, priced in, material ESG and governance (team away; all pending)
**Question 1 (key risks):** recommendation: R1 (structural wheat cost, -18% Gordon), R2 (NA turnaround stalls, -18%), R4 (Mexico labour and tax policy, -14% to -21%), R5 (exit de-rates to 5.53x, -9.5% exit) and R3 for the debt pillar. Strongest case against: R5 mirrors the valuation call and R4 is not tied to any chosen pillar. Question: which pillar does Mexico's labour and tax policy belong to?
**Question 2 (priced in):** recommendation: R1 not priced in (consensus margins show no structural step); R2-R5 partly. Question: what market data would show that the 2026 wheat move is already in the price?
**Question 3 (material ESG):** recommendation: climate/input costs, nutrition regulation, water, packaging, sourcing; the first two move value. Question: if you could defend only three, which ones and which number backs each?
**Question 4 (governance):** recommendation: governance explains part of the gap to consumer peers (6.94x vs 8.27x), not a discount to pure bakers (5.53x); no WACC premium. Question: what evidence would show the discount is governance and not the category?
**Team answer:** pending.
**What changed:** research/risks.yaml, risks.md and esg.md created (English; impacts from the DCF v3 replica); downside scenario on a project copy: Gordon 16.58 / exit 29.60 (published basis), 22.51 / 26.97 (engine); risk matrix drawn.

## 2026-10-17 — forecast — story drivers and what must be true (team away; all pending)
**Question 1 (which drivers carry the story):** recommendation: gross_margin (pillar 1), opex_pct_revenue / EBITDA margin (pillar 2), capex_pct_revenue (pillar 3) and North America growth (pillar 2). Strongest case against: Mexico growth (55% of EBITDA) has no pillar, yet it drives more value than NA. Question: which single driver would you defend first in front of a judge?
**Question 2 (values, history -> proposal):** gross margin 51.4-53.5% (FY21-25) -> 52.4% / 52.0% (wheat dip) / 52.5%, consensus 52.3/52.0/52.05%; EBITDA margin 13.6-13.8% (FY23-25; 14.4% FY21) -> 14.7% FY26 (guidance +70-120 bp) to 15.3% FY30, above the clean historical best; capex 5.3-8.9% (FY21-25) -> 4.6% (guidance) rising to 6.0%, vs consensus ~5.0% and peers 3.7-3.8%. Question: what must be true for EBITDA margin to beat its best clean year by 90 bp?
**Question 3 (revenue vs industry):** North America +3.0% a year in MXN is ~+1.5% in USD against a category at -2% to -4% volume and +1-2% price, so Bimbo must outgrow the category by ~3 points a year (share gains of ~0.8 pp a year on ~27% of US fresh bread); Mexico +5.0-5.5% against a 3.5% market implies ~0.3 pp a year of share gains on 18.2%. Question: say the share path out loud: which competitor loses it?
**Team answer:** pending.
**What changed:** no driver value changed; rationales updated (v3 capex benchmarks, DCF v3 references, PPP alternatives for NA FX); engine rebuilt as model v7 (123 checks OK, 0 warnings, same values).

## 2026-10-17 — industry — market definition, moat and peer set (team away; all pending)
**Question 1 (market definition):** recommendation: branded packaged bakery with direct-store delivery, by country. Question: in which market does the consumer choose, and who sets the price, the US retailer or the Mexican shopkeeper?
**Question 2 (moat):** recommendation: regional moat, wide in Mexico and Latin America, not shown in the US (North America 9.6% vs Flowers 11.1% on a lease-comparable basis, despite a 52.6% vs 48.6% gross margin). Question: which US P&L number would prove scale is an advantage?
**Question 3 (peer set):** recommendation: Flowers and Gruma for the core median; the eight eligible peers as the range; Yamazaki, Aryzta and Arca shown but excluded. Question: why should Bimbo exit below the 6.94x the market pays today?
**Team answer:** pending.
**What changed:** research/industry.md written in English as the report-ready synthesis, complementing BIMBOA/research/industry/industry-report_2026-10-17.md with an operating benchmark of the peers on one basis and the link to the team's pillars (pillar 1 relevant but unprotected, pillar 2 weakened, pillar 3 supported).

## 2026-10-17 — valuation — is HOLD our position given the current picture? (team question)
**Question:** the team asked whether the position is HOLD. On the project rule (expected return = 12-month target / price - 1 + dividend yield 1.8%; HOLD between -10% and +15%), HOLD needs a 12-month target of about 51.7-66.3. Current proposals give SELL (Gordon 36.84, -35%; exit 6.0x 50.58, -12%); HOLD appears with terminal capex at 5.0% (52.09 / 53.71, -9% / -7%) or an exit near Bimbo's 7.12x today (62.13, +8%); consensus target 70.17 (+21%). Recommendation: a provisional HOLD is coherent only if the team defends ~5% terminal capex and/or a ~7x exit. Strongest case against: with the current proposals the DCF says SELL. Question back: which assumption will you change so HOLD comes out of the numbers, terminal capex or the exit multiple?
**Team answer:** pending (not recorded as a decision until confirmed).
**What changed:** nothing in the model.
