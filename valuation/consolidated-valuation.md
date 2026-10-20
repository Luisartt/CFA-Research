# Grupo Bimbo (BMV: BIMBO A) — consolidated valuation of the team's three models (assistant draft, 2026-10-19)

> **Status:** assistant proposal built from the team's three DCFs.
> - No v3 file changes: `valuation.md`, `valuation.yaml` and the publication gate `valuation-outputs.yaml` stay as published.
> - Target price and rating are the team's decisions.
> - Values per share are MXN at 16-Oct-2026 (price 58.60) unless stated; money is in MXN millions.

## Files

| File | What it holds |
|---|---|
| `valuation/BIMBOA_DCF_consolidated_v1.xlsx` | Live formulas, recalculated in Excel: 328 formula cells, 0 errors, all checks OK |
| `valuation/build/consolidate_models.py` | Replica of both teammates' workbooks, both walks and the consolidation |
| `valuation/build/build_consolidated_workbook.py` | Builds the workbook |
| `valuation/inputs/consolidated_results.json` | All results |
| `valuation/team-models/` | Copies of Diego's and Alejandro's files (originals in Downloads unchanged) |

**Verification:** the replica reproduces Alejandro's 47.13 (exit) and 36.91 (Gordon) and Diego's 54.94 from their own inputs, with a difference of 0.00 `[calc]`.

## 0. Bottom line

1. **There are two input sets, not three.**
   - Alejandro's workbook runs the v3 inputs on the S&P Capital IQ template. His FY2026-30 FCFF equal v3's to the peso (117,350) and his WACC equals v3's (10.3233%) `[calc]`. He agrees with v3 by construction, not as a second opinion.
   - Diego's set is the only independent one on forecast, beta, multiple and bridge. His cost-of-capital sources are the same as v3's.
2. **The WACCs agree because the sources are shared.**
   - All three models use risk-free 7.51%, ERP 4.20%, the same country risk premium weighted by where Bimbo earns its EBITDA (2.05%), and Kd 9.71%.
   - Only the unlevered beta (0.53 vs 0.56) and Diego's debt figure differ. The WACCs are 10.32% vs 10.40% `[calc]`.
3. **Diego's higher value (54.94 vs 47.13) is mostly not a difference of opinion.**
   - His 6.4x multiple adds 4.63 and NCI at book adds 4.07.
   - His debt reconversion, the derivatives inside Capital IQ debt and a stub that drops 3.5 months of cash flow take off 2.50.
   - On the same facts and mechanics, his judgments give **45.71** and v3's give **47.13**. The two analysts are Ps 1.42 apart `[calc]`.
4. **Consolidated DCF.** Judgments are weighted 50/50, and facts and mechanics are reconciled.

   | Method | Value today | vs 58.60 |
   |---|---|---|
   | Exit multiple | **46.42** | −20.8% |
   | Gordon, v3 return on new capital (14.6%) | **30.76** | −47.5% |

   WACC is 10.38% `[calc]`. On the settings I recommend (50/50, 5.92x, NCI at market, tax on EBIT 34% instead of the 32% average), exit is **45.69**.
5. **Rating band (team convention).**
   - The exit method's 12-month value is 51.42, an expected return of **−10.5%**. That is 0.5 pp below the HOLD floor.
   - On the recommended settings it is **−11.9%**. Gordon gives −40.7%.
   - HOLD needs a value today of at least 46.66, so HOLD rests on the exit method plus at least one more choice:
     - Diego's raw multiple: 49.75, −4.0%
     - NCI at book: 50.61, −2.4%
     - Tax at 30%: 47.15, −9.1% `[calc]`
6. **ESG does not move the discount rate.** Its value effects run through margin, capex, the multiple and the bridge (section 9). The one contractual ESG cost, the Bimbo 23L coupon step-up, is worth less than one centavo per share `[calc]`.

## 1. What each model is

| | v3 (`valuation/`) | Alejandro | Diego |
|---|---|---|---|
| Workbook | `BIMBOA_DCF_v3.xlsx` | `Bimbo_DCF_Alejandro.xlsm` | `SPG_DCF_independent_Diego.xlsm` |
| Template / horizon | engine + S&P layout; 10 years (FY2026-35) | S&P template; 5 years (2H26-FY2030) | S&P template; 5 years (76-day stub to FY2030) |
| Forecast | v3 drivers (regional build, pillars 1-3) | v3 drivers, copied (his Supuestos_DCF controls: FCFF = v3) | Capital IQ consensus FY26-28 + fade (he calls it a neutral placeholder) |
| Valuation date | fiscal-year-end roll (0.79 y) | 30-Jun anchor, rolled to 16-Oct at ke | discounted from 16-Oct; balance sheet at 30-Jun |
| Terminal value | Gordon g 4.25% and exit 6.0x on FY2035 | exit 6.0x and Gordon on FY2030 | exit 6.4x on FY2030 |
| Bridge | NCI at market; pensions, provisions, derivatives in Gordon only | same as v3 | NCI at book; no associates; no other claims |
| **Value today, exit / Gordon** | **45.72 / 33.55** | **47.13 / 36.91** | **54.94 / n.a.** |

## 2. Side by side

| Input | v3 / Alejandro | Diego | Consolidated | Bucket |
|---|---|---|---|---|
| Risk-free (M-Bono 9.26% − default spread 1.75%) | 7.51% | 7.51% | 7.51% | Fact |
| ERP / CRP (EBITDA-weighted) / pre-tax Kd | 4.20% / 2.05% / 9.71% | same | same | Fact |
| Unlevered beta (Damodaran, Food Processing, Global) | 0.53 | 0.56 | 0.545 | Judgment |
| D/E, market value, debt incl. leases | 0.743 | 0.774 | 0.743 | Fact (company debt) |
| Levered beta / ke / WACC | 0.806 / 12.94% / 10.32% | 0.863 / 13.19% / 10.40% | 0.828 / 13.04% / 10.38% | `[calc]` |
| Revenue FY2030 (CAGR FY2025-30) | 504,070 (3.4%) | 511,536 (3.7%) | 507,797 (3.5%) | Judgment |
| EBITDA margin FY2030 (EBITDA) | 15.3% (77,123) | 14.7% (75,348) | 15.0% (76,245) | Judgment |
| D&A / revenue | 5.9% → 5.85% | template: rises to 100% of capex + leases | v3 path | Mechanic |
| Capex excluding leases, FY2026 → FY2030 | 4.6% → 5.5% | 5.2% → 4.8% | 4.9% → 5.1% | Judgment |
| New leases / revenue FY2030 | 1.74% (principal + growth in the liability) | 1.39% (principal only) | 1.73% | Mechanic |
| Tax on EBIT | 34% (effective) | 30% (statutory) | 32% | Judgment, flagged |
| FCFF FY2026-30, sum | 117,350 | 137,621 | 123,642 | `[calc]` |
| Exit EV/EBITDA (FY2030) | 6.0x | 6.4x | 5.92x | Judgment + data basis |
| Terminal growth g | 4.25% | 4.00% | 4.125% | Judgment |
| Debt incl. leases / cash | 187,021 / 16,563 | 194,918 / 17,023 | 187,021 / 16,563 | Fact |
| Non-controlling interests | 18,243 (market) | 743 (book) | 18,069 (market, at ke 13.04%) | Mechanic, provisional |
| Associates − seasonal tax payable | +1,959 | 0 | +1,959 | Mechanic |
| Other debt-like claims (Gordon only) | 18,135 | 0 | 18,135 | Mechanic |
| Shares (millions) | 4,294.9 (BMV) | 4,296.3 (Capital IQ) | 4,294.9 | Fact |

## 3. Why Diego's value is higher: walk from Alejandro to Diego

Exit method, one change at a time, in this order. The walk closes exactly on Diego's 54.94 `[calc]`.

| Step | Value | Change | Type |
|---|---|---|---|
| Alejandro: v3 inputs on the S&P template | 47.13 | | |
| Valuation date: 76-day stub from 16-Oct; balance sheet still 30-Jun | 46.38 | −0.75 | Mechanic |
| Debt: derivative liabilities inside Capital IQ total debt (+2,658) | 45.76 | −0.62 | Fact |
| Debt and cash reconverted at 17.96 MXN/US$; Capital IQ's own peso and dollar figures imply 17.47 | 44.65 | −1.11 | Fact (to confirm) |
| Shares 4,296.3m (Capital IQ) instead of 4,294.9m (BMV) | 44.64 | −0.01 | Fact |
| Drop associates (+6,498) and the seasonal tax payable (−4,538) | 44.18 | −0.46 | Mechanic |
| NCI at book (743) instead of market value (18,243) | 48.25 | **+4.07** | Mechanic, provisional |
| WACC 10.32% → 10.40% (beta 0.53 → 0.56; D/E from his debt) | 48.02 | −0.23 | Judgment + fact |
| Revenue: v3 regional build → consensus + fade | 49.30 | +1.27 | Judgment |
| EBITDA margin: v3 (to 15.3%) → consensus (held at 14.7%) | 46.01 | **−3.28** | Judgment |
| D&A: v3 path → template mechanics | 46.17 | +0.16 | Mechanic |
| Capex excluding leases: v3 → consensus | 47.39 | +1.21 | Judgment |
| New leases: principal + growth → principal only | 48.63 | +1.24 | Mechanic |
| Working capital path | 49.00 | +0.37 | Judgment |
| Tax on EBIT 34% → 30% | 50.31 | +1.32 | Judgment, flagged |
| Exit multiple 6.0x → 6.4x | **54.94** | **+4.63** | Judgment + data basis |

**Subtotals:**

| Group | Change |
|---|---|
| Facts and timing | −2.50 |
| Bridge choices | +3.62 |
| WACC | −0.23 |
| Forecast judgments | +0.89 |
| D&A and lease mechanics | +1.40 |
| Multiple | +4.63 |
| **Total** | **+7.80** |

Diego flagged most of these himself in section 7 of his note: the timing (about Ps 1.5 per share), the lease basis of the US GAAP peers, Gruma's EBITDA and NCI at book.

## 4. Where the two analysts really differ

Here v3's set moves to Diego's one judgment at a time. Facts and mechanics are held the same: company debt, NCI at market, v3 D&A and lease mechanics, and the 30-Jun anchor `[calc]`.

| Judgment | Exit | Change | Gordon (RONIC 14.6%) | Change |
|---|---|---|---|---|
| v3 set (= Alejandro) | 47.13 | | 30.36 | |
| Unlevered beta 0.53 → 0.56 | 46.88 | −0.26 | 29.10 | −1.26 |
| Revenue path → consensus | 48.08 | +1.21 | 30.10 | +1.01 |
| **EBITDA margin → consensus** | 44.75 | **−3.33** | 25.92 | **−4.18** |
| Capex excluding leases → consensus | 45.81 | +1.06 | 26.98 | +1.06 |
| Working capital | 46.18 | +0.37 | 27.35 | +0.37 |
| Tax on EBIT 34% → 30% | 47.63 | +1.45 | 32.15 | **+4.80** |
| Exit multiple 6.0x → 5.83x (his rule on lease-consistent data) | **45.71** | −1.93 | 32.15 | 0.00 |
| g 4.25% → 4.00% | 45.71 | 0.00 | **31.09** | −1.06 |

**Reading:**
- The real disagreement is the margin. v3 expects the productivity plan (pillar 2) to lift EBITDA margin to 15.3%; consensus holds 14.7%.
- Diego's set is more generous on revenue, capex and tax, and these offset the margin gap.

**Question:** is the 60 bp of margin above consensus by FY2030 something the team can evidence, or is it the thesis itself?

## 5. How the consolidated DCF was built

The rule is to average the judgments, not the mistakes.
- **Facts** take one sourced value.
- **Mechanics** take one convention, the technically correct one.
- **Judgments** are averaged with weight w on v3.

Averaging a data error with a correct figure only halves the error.

### 5.1 Facts

**Debt incl. leases: 187,021 (company).** Diego's 194,918 is 7,897 higher. This is a reconciliation for Diego to confirm, not a confirmed error `[calc]`:
- **Derivatives (2,658).** Capital IQ total debt at Jun-26 is 189,679 = financial debt 153,660 + leases 33,361 + derivative adjustments 2,658 (wiki `ciq-debt-stack-and-maturity-ladder`). The derivatives are already among the other claims that Gordon deducts.
- **Exchange rate (5,239).** He reconverted US$10,855m at 17.96 MXN/US$, the rate that wiki `bimbo-wacc-market-inputs-capiq-2026-10` says Capital IQ used. Capital IQ's own peso total (189,679) and dollar total (10,855) imply 17.47. The cash supports 17.47: US$948m × 17.47 = 16,565, against the company's 16,563.

**Cash and shares:**
- Cash is 16,563. The same reconversion adds 460 to Diego's figure.
- Shares are 4,294.9m (BMV notice, 29-Jul-2026).

### 5.2 Mechanics

**Valuation date.** Cash flows and the balance sheet are anchored at 30-Jun-2026, then rolled to 16-Oct at ke (Alejandro's method).

**D&A uses the v3 path (5.85-5.9% of revenue).** Diego's path is the template's mechanics, not a judgment: he labels it "template mechanics". It raises D&A to 100% of capex plus leases by FY2030, which means no net investment while revenue grows about 4% a year.

**New leases** = principal (1.39% of revenue) + growth in the lease liability, held at 8.15% of revenue. This is the published v3 basis. Diego's principal-only basis keeps the liability flat while revenue grows.

**Bridge:**
- Associates are added and the seasonal tax payable is deducted.
- Pensions, provisions and derivatives (18,135) are deducted in Gordon only, because peer EVs exclude them.
- NCI is at market value: NCI income 1,814 / (ke − 3%). This is the v3 treatment, still provisional.

### 5.3 Judgments

Judgments are averaged with weight w on v3. I recommend w = 0.5 because there are two input sets. Setting w = 0.6667 gives each model one third.

### 5.4 Exit multiple

Diego's rule is the median of his core four peers. He applied it to Capital IQ multiples that are not on one basis:
- US GAAP peers keep operating-lease cost inside EBITDA while their debt includes leases.
- Gruma's Capital IQ EBITDA is 995.0, against 1,108.9 for the company.

On the lease-consistent v3 table, the same four peers give 5.83x:

| Peer | Diego's table | Lease-consistent (v3 table) |
|---|---|---|
| Flowers Foods | 6.68x | 5.61x |
| Gruma | 6.01x | 5.44x |
| Yamazaki | 6.06x | 6.06x |
| Aryzta | 8.33x | 8.33x |
| **Median** | **6.37x** | **5.83x** |

The base uses (6.0x + 5.83x) / 2 = **5.92x**. The raw average of 6.2x is shown as a variant (+3.33 per share).

### 5.5 Horizon and terminal reinvestment

Both teammates used the five-year template, so the consolidated model does too. The v3 ten-year values stay as a reference.

On five years, v3's main judgment (capex rising to 6.0% by 2035) drops out. The terminal reinvestment is therefore an explicit input: a return on new capital (RONIC) of 14.6%, the figure implied by the published v3 terminal value. Diego has no Gordon or reinvestment judgment, so nothing is averaged here.

## 6. Consolidated results

| Method | Value today | vs 58.60 | 12-month value* | Expected return* |
|---|---|---|---|---|
| **Exit multiple 5.92x** | **46.42** | −20.8% | 51.42 | −10.5% |
| **Gordon, RONIC 14.6%** | **30.76** | −47.5% | 33.72 | −40.7% |
| Gordon, template style (FCFF FY2030 × (1 + g)) | 41.65 | −28.9% | 46.03 | −19.7% |
| Gordon, RONIC = WACC (growth adds no value) | 21.36 | −63.6% | 23.09 | −58.8% |

\* Convention from `references/recommendation-guide.md`:
- 12-month value = value × (1 + ke) − next dividend (Ps 1.05).
- Expected return = 12-month value / price − 1 + dividend / price.
- BUY at +15% or more; SELL at −10% or less.
- At ke 13.04%, HOLD needs a value today of at least **46.66** and BUY at least 59.62 `[calc]`.

**Key inputs:**

| Item | Value |
|---|---|
| WACC / ke / levered beta | 10.38% / 13.04% / 0.828 |
| g | 4.125% |
| Exit multiple | 5.92x |
| Tax on EBIT | 32% |
| Terminal value share of EV (exit) | 76% |
| Perpetual FCFF growth implied by the multiple | 4.16% `[calc]` |

**One change at a time against the base**

| Variant | Exit | Gordon (RONIC) | Expected return, exit |
|---|---|---|---|
| Base (w = 0.5, 5.92x, NCI at market, tax 32%) | 46.42 | 30.76 | −10.5% |
| **Recommended settings: tax on EBIT 34%** | **45.69** | **28.31** | **−11.9%** |
| Tax on EBIT 30% | 47.15 | 33.21 | −9.1% |
| One third per model (w = 0.6667) | 46.66 | 30.63 | −10.0% (on the floor) |
| Raw multiple average 6.2x | 49.75 | 30.76 | −4.0% |
| NCI at book | 50.61 | 34.94 | −2.4% |
| v3 set only, same mechanics (= Alejandro) | 47.13 | 30.36 | −9.2% |
| Diego's set, reconciled (5.83x) | 45.71 | 31.09 | −11.8% |
| Diego's set, reconciled, his 6.4x | 52.29 | 31.09 | +0.9% |

**Averaging outputs vs averaging inputs.** Averaging the published outputs blends errors with judgments, because those outputs carry the bridge and data differences of section 3.

| Approach | Value | Why it differs |
|---|---|---|
| Simple average of the three published exit values (45.72, 47.13, 54.94) | 49.26 | gives v3 two votes and carries Diego's data issues |
| Average of Alejandro and Diego as published | 51.04 | carries the data issues |
| **Averaged judgments on reconciled facts (this model)** | **46.42** | |

**Why the two DCF methods disagree by 34%.** The 5.92x multiple behaves like the template-style Gordon, whose implied multiple is 5.88x. That Gordon lets FCFF grow at g with little extra reinvestment, which needs a 27.7% return on new capital. With the 14.6% from v3, the justified terminal multiple is 4.96x `[calc]`. Judges will ask about this gap; the guide flags gaps above 20%. The team's answer is its view of Bimbo's long-run return on new capital.

**Horizon.** v3's ten-year Gordon (33.55) is above the five-year RONIC-consistent value on the same v3 inputs (30.36). The five-year version applies the terminal reinvestment from 2031, while v3 phases capex up to 6.0% by 2035.

## 7. Sensitivity (live in the workbook)

Exit method: WACC (rows) × exit EV/EBITDA (columns):

| WACC \ multiple | 5.0x | 5.5x | **5.92x** | 6.5x | 7.0x |
|---|---|---|---|---|---|
| 9.38% | 38.49 | 44.64 | 49.77 | 56.93 | 63.08 |
| 9.88% | 37.03 | 43.05 | 48.07 | 55.09 | 61.11 |
| **10.38%** | 35.59 | 41.49 | **46.42** | 53.29 | 59.19 |
| 10.88% | 34.20 | 39.98 | 44.80 | 51.54 | 57.32 |
| 11.38% | 32.83 | 38.49 | 43.22 | 49.82 | 55.49 |

Gordon (RONIC 14.6%): WACC (rows) × g (columns):

| WACC \ g | 3.125% | 3.625% | **4.125%** | 4.625% | 5.125% |
|---|---|---|---|---|---|
| 9.38% | 38.81 | 41.76 | 45.25 | 49.43 | 54.55 |
| 9.88% | 32.45 | 34.73 | 37.37 | 40.49 | 44.23 |
| **10.38%** | 26.96 | 28.73 | **30.76** | 33.10 | 35.86 |
| 10.88% | 22.19 | 23.57 | 25.12 | 26.90 | 28.95 |
| 11.38% | 18.00 | 19.07 | 20.26 | 21.61 | 23.14 |

The NCI claim and the roll-forward factor are held at the base ke.

## 8. Reverse DCF and comparables

**What the price needs (exit method, one lever at a time)** `[calc]`:
- an exit multiple of **6.95x**: Bimbo trades at 6.94x LTM with NCI at book and 7.12x with NCI at market;
- or a WACC of 6.96%;
- or revenue growth 3.10 pp a year higher in every forecast year.

**Comparables.** All values use the v3 comps bridge: LTM EBITDA 60,919; net debt incl. leases; NCI at market; associates.

| Multiple | Value per share |
|---|---|
| Core bakery median, v3 table (Flowers, Gruma): 5.53x | 35.95 |
| Diego's core four on the lease-consistent table: 5.83x | 40.33 |
| 6.0x (v3 exit judgment) | 42.68 |
| Diego's core four as he computed them: 6.37x | 47.93 |
| All nine peers, Diego's table: 8.20x | 73.92 |
| All eligible peers, v3 table: 8.27x | 74.87 |

The secondary peers (Mondelez, PepsiCo, Smucker, Campbell's) earn 16-25% EBITDA margins against Bimbo's 14.5%. Both teammates treat their median as a ceiling, not a base.

## 9. Risks and ESG translated into value

Source: Diego's General ESG Report v2 (`valuation/team-models/BIMBOA_ESG_Report_EN_Diego.pdf`). His figures tagged `[unverified]` are not used as evidence.

| Lever (one change against the base) | ESG / risk theme and evidence | Exit | Gordon (RONIC) |
|---|---|---|---|
| EBITDA margin −50 bp every year | Wheat and climate. Raw materials are about 64% of cost of sales `[sourced/calc]`. The CFO tied 60 bp of 2022 EBITDA margin to the wheat cycle `[guidance]`. The 2026 wheat move (+17%) is `[unverified]` | −3.72 | −4.59 |
| Capex +50 bp of revenue every year | Water. 101 work centres sit in high or extremely high water stress `[sourced]`. Withdrawal is up 15.1% since FY2019 `[calc]`. A separate sustainability capex envelope exists since 2025, amount not disclosed `[sourced]` | −2.05 | −2.05 |
| Revenue growth −50 bp every year | Health regulation. Front-of-pack labelling phase 3 starts 1-Jan-2028 and school-food rules started 29-Mar-2025 `[sourced]`. Consumers are shifting away from sugar and refined flour | −1.84 | −1.57 |
| Exit multiple −0.5x | Governance. The control group holds 72.03% and 38.9% of directors are independent `[sourced]`. Minority protection scores 1 of 10 on his compiled rubric `[assumption]`. Governance is the weak pillar in every rating source | −5.90 | 0.00 |
| One-off claim of MXN 1bn | Litigation. The Canada Bread price-fixing class actions are open with no provision; the CAD 50m fine was paid in 2023 `[sourced]`. Uncertain tax positions (8,537) are already deducted in Gordon | −0.24 | −0.24 |
| Recurring pre-tax cost of MXN 1bn a year from FY2027 | Carbon market: the Mexican pilot ran 2020-25 and its rules are unpublished `[sourced]`. Extended producer responsibility under the law of 19-Jan-2026 `[sourced]` | −1.43 | −1.77 |
| Bimbo 23L coupon step-up | Scope 3 / SBTi. +25 bp on MXN 12,000m from 21-Nov-2031 to 20-May-2033 if the −28% target is not verified `[sourced]`. 2025 Scope 3 was 46.7% above the bond base `[calc]`. SBTi certification is paused | −0.004 | −0.004 |
| WACC +50 bp (not ESG) | Country and currency risk | −1.62 | −5.64 |

**Reading:**
- **Where ESG reaches value.** Mainly through wheat and water (margin and capex) and governance (the multiple). None of these needs a higher discount rate.
- **No ESG premium on the discount rate.** Diego's report finds no source linking Bimbo's ESG scores to its cost of debt or equity. A premium would double-count risks already in the cash flows.
- **Ratings are context, not a valuation input.** LSEG gives 84.62 (A) and S&P gives 59, against an industry average of 29.
- **Liabilities.** Each MXN 1bn of unprovisioned liability costs about Ps 0.24 per share.

## 10. Coach moment: what this means for the HOLD

**Your idea, restated.** You have a HOLD and want to defend why you stay: neither sell nor buy.

**What the consolidated evidence says.**
- The exit method lands just under the HOLD floor: 46.42 today against 46.66, or 45.69 on the recommended tax rate.
- The cash-flow method lands deep in SELL: Gordon with a 14.6% return on new capital.
- HOLD is defensible only if the team argues that the market's terminal multiple is a better guide to Bimbo's long-run value than its own reinvestment math, and that a 15.0% FY2030 margin is earned.

**My recommendation.**
- If you keep HOLD, make the exit-multiple DCF the primary method and present Gordon as the downside case.
- Anchor the multiple on evidence you can show: Bimbo's own 6.9-7.1x today, the Mexico mix, and the core peers at 5.4-6.1x.
- Decide the weighting, the multiple basis and the tax rate first. Read the rating band only after that. Do not pick averaging rules to land inside HOLD; judges ask why the rules changed.

**Strongest case against.**
- The two DCF methods disagree by 34%.
- A multiple near 6x implies a 27.7% return on new capital, almost twice the 14.6% that the team's own v3 capex path implies.
- On the recommended settings the exit method itself gives −11.9%.
- A judge can say the HOLD rests on an assumption that your own Gordon rejects. On that view the evidence points to SELL.

**Question for the team.** For Bimbo's terminal value, which do you trust more: the peers' market multiple (5.4-6.1x for the core bakers) or your own reinvestment math (a 14.6% return on new capital)?

## 11. Decisions the team owns

1. Weighting: 50/50 between the two input sets (recommended), or one third per model.
2. Exit-multiple basis: Diego's rule on lease-consistent data, 5.92x (recommended), or the raw 6.2x.
3. Tax on EBIT: effective 34% (recommended for cash taxes), statutory 30%, or the 32% average used in the base.
4. NCI: market value (v3, provisional) or book.
5. Horizon: the five-year template (both teammates), or v3's ten years with the capex ramp. This sets the terminal reinvestment.
6. Primary method, weights, target price and rating.

## 12. Open items

- Diego's workbooks still use the reconverted Capital IQ debt (194,918) and cash (17,023). Diego should confirm the exchange rate and switch to the company figures (187,021 / 16,563).
- Gruma LTM EBITDA (Diego's open point): v3 uses the company figure of 1,108.9, not Capital IQ's 995.0.
- NCI at market value stays provisional until the team decides. It is also open in v3.
- Diego's forecast is a consensus placeholder by his own description. The team's story drivers are in `model/drivers.yaml`.
- The consolidated values are not in the publication gate. If the team adopts them, update `valuation-outputs.yaml` before the report, the deck or the pitch uses any number.
- Diego's ESG report has `[unverified]` items, for example the 2026 wheat move and the 89 vs 101 water-stressed sites. They must be resolved or removed before the official report (his own section 6).
