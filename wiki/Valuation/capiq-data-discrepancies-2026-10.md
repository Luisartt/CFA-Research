---
Writer: AI-compiled (Claude)
Source: data/capitaliq/capiq-ai-prompt1_2026-10-16.md
tags: [Valuation, data-quality]
---

# Capital IQ Prompt 1 — Discrepancies, Discarded Data and Gaps (2026-10-16)

Audit of the Capital IQ AI output behind [[peer-leverage-capiq-2026-10]] and [[peer-multiples-and-operations-capiq-2026-10]]. Each row says what was found, how it was checked, and what the wiki uses instead. Checks against the filings use [[bimbo-capital-structure-and-debt]], [[bimbo-cross-source-connections]] and [[bimbo-segments-and-regions]]. Source: `data/capitaliq/capiq-ai-prompt1_2026-10-16.md`.

## 1. Discrepancies and how they were resolved

| # | Finding | Check | Wiki treatment |
|---|---|---|---|
| 1 | Bimbo net debt / EBITDA printed as ~2.3x | Company reports 2.5x at Jun-26, ex-IFRS 16 (2Q26 release p.6) `[sourced]`; the output divides ex-IFRS 16 net debt (137.1bn) by an IFRS 16 EBITDA (~58.5bn) | Use 2.5x `[sourced]`; lease-inclusive ≈2.8x `[calc]` |
| 2 | "Total debt Ps. 137bn" | That is net debt; total debt is MXN 153.66bn at Jun-26 `[sourced]` | Corrected |
| 3 | Bimbo table 1A does not foot: debt 8,200 − cash 1,700 ≠ net debt 7,600; EBITDA US$2,950m (1A) vs US$3,260m (1C); revenue ~US$20,500m vs MXN 427.0bn FY25 | Internal arithmetic | All Bimbo US$ figures discarded (assistant estimates, not CIQ) |
| 4 | Bimbo LTM EBITDA ~MXN 58.5bn | Company LTM 60,919m and CIQ-implied 64,706m `[sourced]` ([[bimbo-cross-source-connections]] C3) | Use 60,919 for the lease-inclusive ratio; show 64,706 as the alternative |
| 5 | Segment net sales FY24/FY25 (e.g. FY25 segments sum to MXN 226.8bn vs total 427.0bn; North America 102.7bn vs 44.6% of sales) | Do not sum or match the mix in [[bimbo-segments-and-regions]]; look like half-year figures labelled annual | Discarded; segment EBITDA and margins kept (they match the filings) |
| 6 | Bimbo rating "N/A" | Filings and LSEG give BBB+ / BBB+ / Baa1; S&P negative outlook since 2025-03-20 `[sourced]` | Kept the filing values ([[bimbo-credit-risk-lseg]]) |
| 7 | EV/EBITDA from the CIQ multiples tool differs from EV ÷ EBITDA in the CIQ table (Flowers 5.15x vs 6.68x; Campbell's 6.47x vs 8.20x; Mondelez 14.48x vs 16.77x; PepsiCo 10.35x vs 11.48x; Aryzta 7.31x vs 8.33x; Smucker 8.57x vs 9.06x) | Recomputed `[calc]` | Table quotient used; tool value kept for audit |
| 8 | CIQ annual leverage ratios differ from simple quotients (Flowers FY25 3.13x vs 4.02x; Campbell's FY21 2.32x vs 2.71x; Mondelez FY21 2.42x vs 2.72x; Aryzta FY21 0.95x vs 1.13x) | Recomputed `[calc]` | CIQ uses another EBITDA basis; historical ratios not compared with LTM quotients |
| 9 | Ranking and summary statistics in the output's Task 1C | Panel 1 order wrong (Flowers 4.01x ranked above Campbell's 4.36x); core median 3.79x excluded Yamazaki; all-peer median printed as 3.20x and 3.35x; mean ~2.97x | Recomputed: core median 3.57x, all-peer median 3.20x, mean 2.57x `[calc]` |
| 10 | Arca Continental diluted shares 212.1m identical to Flowers' 212.1m; market cap resolved to Aon plc | Duplicate value; entity mismatch | Arca shares, market cap and pricing-tool EV discarded; financials-tool values kept |
| 11 | Yamazaki FY2025 revenue US$8,773.2m identical to FY2021 | Possible copy error | Marked `[unverified]`; FY25 revenue not used |
| 12 | Nutresa EV US$50.2bn on EBITDA US$0.83bn (60x) | Implausible | Discarded (COP conversion error) |
| 13 | Mondelez FY25 EBITDA US$4,990m (margin 13.0%) vs LTM US$6,080m (15.3%) and FY24 US$7,740m | Looks like a one-off item | FY25 not used as a base `[unverified]` |
| 14 | Smucker P/E 58.63x | Depressed earnings | Not used as a comparable `[assumption]` |
| 15 | Stray reference numbers in the text ("Reported 23", "13", "256") | Not citations | Ignored |
| 16 | Tickers BMV:BIMBOA and BMV:GRUMAB resolved to "Bmvb Immo" and "Bevgru Ab"; BMV:AC pricing resolved to Aon | Entity names | Re-run by company name with the CIQ identifier stated (§3) |

## 2. Not retrieved

- **Entities:** Gruma (all data); Bimbo on a CIQ-standardized basis (price, market cap, EV, ratios, consensus); EV and market cap of Yamazaki and Arca Continental.
- **Credit:** Moody's and Fitch for the peers (entitlement denied); 10-year rating history; debt by currency and fixed/floating; average cost of debt; FFO / debt; debt / equity; covenants.
- **Multiples:** 5-year and 10-year average EV/EBITDA and P/E (query error); P/FCF, FCF yield, dividend yield; buybacks and payout ratio.
- **Operations:** organic growth and capex for the peers; capex for Bimbo; Bimbo segment history FY21–FY23.
- **Not run yet:** Prompts 2 and 3 (Bimbo debt stack, new CEO, market shares, climate, valuation inputs, ownership and M&A).

## 3. How to repeat the pull

- Search by company name and ask the assistant to state the Capital IQ identifier it used; probable identifiers for the series shares are `BMV:BIMBO A` and `BMV:GRUMA B` `[unverified]`.
- For Bimbo use the local Capital IQ and LSEG files already compiled (see [[bimbo-valuation-data-gaps]]) rather than the assistant's own conversions.

## 4. Second and third pulls (Prompts 2 and 3, pasted 2026-10-17)

| # | Finding | Resolution |
|---|---|---|
| 17 | BIMBO 26-2 printed as "~Ps. 3.2bn, due ~2026" | Principal Ps. 4,133m, due 1-Feb-2030 (filings; recomputed from the 16-Oct-2026 coupon) `[calc]` |
| 18 | Maturity ladder 2034-2036: US$159m, 585m, 560m | Wrong: 585 and 560 are the 2051 and 2049 bond balances; wiki ladder used |
| 19 | US$800m 5.375% notes "due 2035" | Prospectus: 9-Jan-2036 |
| 20 | Issuance table omits the Feb-2026 Ps. 12bn issue (BIMBO 26, 26-2) | Added from 2D and the filings |
| 21 | "Cash covers 2026-2027 maturities more than 11 times" | 948 ÷ 288 = 3.3 times `[calc]` |
| 22 | CEO "effective with the 25-Feb-2026 call" | Effective November 2025; first call 25-Feb-2026 |
| 23 | 20-quarter net debt / EBITDA column | The Jun-2026 level (2.90x) reconciles to Capital IQ net debt incl. leases US$9,907m ÷ EBITDA US$3,393m = 2.92x `[calc]`, but the trend (2.64x to 2.90x) contradicts the company's 2.7x to 2.5x; use it for the level only |
| 24 | Derivative assets 657 exclude the 85 of coupon-only swaps | Unresolved ±85 |
| 25 | Comfort range quote of 2023-02-22 attributed to the then-CEO and to the CFO | Speaker `[unverified]` |
| 26 | "Prior guidance" in the Q4 2025 scorecard | 2025 capex guide US$1.4-1.5bn cut to US$1.3-1.4bn, delivered US$1.2bn: confirmed by the wiki. The year-end leverage guide of ~2.9x is unsourced. (I first marked the capex guide as the 2026 one; that was wrong) |
| 27 | FY2017 acquisitions attributed to Canada Bread | Canada Bread was 2014; 2017 was East Balt |
| 28 | Two runs of 3A differ (101 vs 89 water-stressed sites; Scope 3 regional totals do not add up) | Group totals only |
| 29 | Scope 3 reduction 3.7% (end-2023), 22% (2024), 19% (Q3 2025) vs 2025 target −12.5% and the 23-2L step-up | Unreconciled; check the KPI definition in the prospectus |
| 30 | Scope 2 and Scope 3 both 475,967 in 2019 | Duplicate; Scope 3 2019 unknown |
| 31 | 3C: commodity series, forward curves and quarterly gross margin returned "no data" | Used the chart export supplied by the team (monthly CBOT wheat, annual gross margin); unit of wheat unlabelled |
| 32 | 3D: no peer ESG data in the documents | Only qualitative facts kept |
| 33 | 3F: D/E uses book equity; the "5.5% three-year breakeven" compares a 10-year bond with a 3-year UDI; currency mix 44/42 mixes dates | Market D/E recomputed; breakeven discarded; mix is 42/42/12/3/1 |
| 34 | Consensus target price labelled "Mex$3.80" | It is US$3.80 against a US$3.17 price (+19.9%) |
| 35 | Control of Bimbo "75-80% economic, over 90% voting" from general knowledge; controlling families of Gruma, Arca, Lala | Discarded; register shows 72.03% for the top block |
| 36 | "169,441,413 shares cancelled in October" with no year | 19-Oct-2020 (wiki) |
| 37 | Ricolino value US$1,308m (Ps. 25.8bn) | Wiki EV Ps. 27,000m kept |
| 38 | 2F (market shares) came back empty | Needs a per-document prompt |
| 39 | 3B: no split of cost of goods sold by input, no wheat volume or origin | Not disclosed |

Gaps that remain: levered betas, Mexico EMBI spread, Bimbo bond yields, compensation of executives, covenant text, quarterly gross margin series, commodity forward curves, peer ESG scores and emissions, market shares, broker notes and median/high/low target prices.

## Key Takeaways

- Sixteen problems were found in the first pull and another twenty-three in the second and third (§4); the ones that change conclusions are #1 (2.3x vs 2.5x), #7 (EV/EBITDA bases) and #9 (wrong summary statistics).
- All Bimbo US$ figures and the Bimbo segment sales in the output are unusable; Bimbo's data comes from the filings.
- CIQ's annual leverage ratios and the LTM quotients are on different EBITDA bases and must not be spliced.
- Gruma and a standardized Bimbo are still missing, so the core peer median rests on three peers.
- Use the identifier test in §3 before the next pull.

