---
Writer: AI-compiled (Claude)
Source: Capital IQ AI responses 2A, 2B and 2C (pasted by the team on 2026-10-17; verbatim file still to be saved in raw/ by the team). Underlying documents named in the output: Q2 2026 earnings release and investor presentation (2026-07-23), BMV coupon notices BIMBO 26-2 (2026-07-23, 2026-08-20, 2026-10-15), FY2025 and FY2024 annual reports and financial supplements, earnings-call transcripts 2022-2026
tags: [Valuation, debt-hedging]
---

# Grupo Bimbo — Debt Mix, Hedging, Leverage Target and Financing Activity (Capital IQ AI, Oct-2026)

Complements [[bimbo-capital-structure-and-debt]], [[ciq-debt-stack-and-maturity-ladder]] and [[bimbo-bond-prospectus-terms]], which remain the instrument-level reference. This article holds what the Capital IQ AI output adds, after checking it against those articles. Items that conflicted with the filings are marked and were not used. Peer context: [[peer-leverage-capiq-2026-10]]. Problems: [[capiq-data-discrepancies-2026-10]] (second pull).

## 1. Debt mix at 30-Jun-2026

| Metric | Jun-2026 | Dec-2025 | Tag |
|---|---|---|---|
| Total debt | US$8,796m (≈ Ps. 154bn at Ps. 17.47/US$) | Ps. 154bn | `[sourced]` 2Q26 release/presentation via CIQ AI |
| Currency: USD / MXN / EUR / CAD / GBP | 42% / 42% / 12% / 3% / 1% | 44% / 39% / 12% / 3% / 2% | `[sourced]`, matches [[bimbo-capital-structure-and-debt]] |
| Fixed / floating | 82% / 18% | n/d | `[sourced]` presentation via CIQ AI; consistent with 17.7% floating before swaps at Dec-25 `[calc]` in [[bimbo-capital-structure-and-debt]]; after-swap split not disclosed |
| Average tenor | 9.5 years | 9.7 years | `[sourced]` |
| Average cost of debt | 6.5% (includes derivatives, withholding tax, other costs) | 6.3% | `[sourced]` |
| Long-term share of debt | 96% | 92% | `[sourced]` |
| Net debt / Adj. EBITDA (ex-IFRS 16) | 2.5x | 2.7x (2.9x a year earlier) | `[sourced]` |
| Net debt | Ps. 137bn (≈ US$7.8bn) | Ps. 145bn | `[sourced]` |

- The output's reading that the USD-to-MXN shift of the mix (−2 pp / +3 pp) comes from peso appreciation, not from a rebalancing, is an interpretation `[assumption]`.
- ==Currency exposure is smaller than the gross 42% USD suggests==: cross-currency swaps convert part of the USD bonds into MXN, EUR and GBP (§4), and North America is 44.6% of sales (USD/CAD), so USD debt is close to the share of USD-linked revenue `[calc]` ([[bimbo-segments-and-regions]]).

## 2. Liquidity and near-term maturities

| Item | Amount | Tag |
|---|---|---|
| Cash and equivalents, 30-Jun-2026 | Ps. 16,563m (≈ US$948m) | `[sourced]` |
| Undrawn syndicated revolving facility | US$2,350m | `[sourced]` |
| Total liquidity | ≈ US$3,298m | `[calc]` 948 + 2,350 |
| Remaining 2026 maturities / 2027 maturities | ≈ US$181m / US$107m | `[sourced]` presentation amortisation chart |
| 2028 / 2029 / 2030 / 2031 maturities | US$705m / 900m / 800m / 731m (sum US$3,136m) | `[sourced]`, sum `[calc]` |

- Cash covers the 2026-2027 maturities (≈ US$288m `[calc]`) about 3.3 times (948 / 288 `[calc]`); the output said "more than 11x", which is wrong.
- ==Maturity ladder for 2034-2036 in the output was discarded==: it shows 2034 US$159m, 2035 US$585m, 2036 US$560m. The prospectus-based ladder in [[ciq-debt-stack-and-maturity-ladder]] has 2034 US$550m (6.40% notes), 2035 Bimbo 26 (Ps. 7,867m) and 2036 US$800m (5.375% notes); the output's 2035 and 2036 amounts equal the outstanding balances of the 2051 (US$585m) and 2049 (US$560m) bonds. The 2026-2033 years are consistent with the wiki.
- The Ps. 12bn MXN issuance of 6-Feb-2026 funded the refinancing of existing debt `[sourced]`.

## 3. Instruments added or corrected

| Instrument | Terms | Check |
|---|---|---|
| BIMBO 26 | Ps. 7,867m, 9.22% fixed, 9 years (due 26-Jan-2035) | Matches wiki `[sourced]` |
| BIMBO 26-2 | **Ps. 4,133m**, TIIE Fondeo + 0.45%, 4 years (due 1-Feb-2030); coupon 9 paid 16-Oct-2026 at 6.98% for 28 days (interest Ps. 22,439,634); prior coupon 6.97% | Output said "~Ps. 3.2bn, ~2026": wrong. Principal recomputed from the coupon: 22,439,634 / (6.98% × 28/360) ≈ Ps. 4,133m `[calc]`, equal to the wiki |
| BIMBO 23-2L | Ps. 3,000m, TIIE 28d + 0.10%, due 24-Jul-2026; sustainability-linked (Scope 3); step-up of +0.20% on face value (≈ Ps. 6m) applied for missing the target | Matured after the 30-Jun-2026 cut-off `[sourced]`; step-up 0.20% × 3,000 = 6 `[calc]` |
| BIMBO 23L | Ps. 12,000m, 9.24% fixed, due 20-May-2033; sustainability-linked (28% Scope 3 reduction by 2030) | Output called it "fixed or floating": fixed `[sourced]` |
| BIMBO 25 / 25-2 | Ps. 12,762m 10.06% fixed due 6-Feb-2032 / Ps. 2,238m TIIE 28d + 0.34% due 11-Feb-2028, issued 14-Feb-2025 | `[sourced]` |
| Syndicated revolving facility | US$2,350m (renewed 31-Jul-2025, new lenders BNP Paribas, CaixaBank, Bank of Nova Scotia), undrawn; earlier US$1,931m (Tranche A US$875m, Tranche B US$1,056m) renewed 15-Mar-2023 at SOFR + 0.90% / 1.05% | ESG link on the 2025 goals lapsed 1-Jan-2026 `[sourced]` |
| Three bilateral bank loans | ≈ US$480m, floating, 2027-2034 | ESG-linked to the same 2025 goals, lapsed `[sourced]` |

Not available from the output: ISIN, issue dates, call schedules, per-bond ratings and yields of the USD and EUR notes (use [[bimbo-bond-prospectus-terms]]).

## 4. Hedging programme (FY2025 annual report and FY2024 supplement, via CIQ AI)

Amounts are fair values in MXN millions (the output prints "$" but states MXN millions) `[sourced]`.

| Category | FV 2025 | FV 2024 | FV 2023 | Notes |
|---|---|---|---|---|
| Cross-currency swaps, USD bond notional and coupon to MXN/EUR (assets) | 135 | 663 | 252 | Bond 2049 US$150m to €126m (due 6-Mar-2031); bond 2049 US$25m x2 to Ps. 494m (6-Sep-2030); bond 2044 US$150m to Ps. 1,829m (27-Jun-2028) settled in 2025 |
| Notional-only swaps and net-investment hedges (assets) | 516 | 115 | 204 | Net-investment hedges new in 2025: MXN to £100m (31-Oct-2029) FV 168; MXN to €100m x2 (6-Feb-2032) FV 62 and 64 |
| Cross-currency swaps (liabilities) | 264+ | 190+ | 221+ | Bond 2049 US$200m to Ps. 3,733m; EUR swaps on bonds 2044 and 2047 |
| Coupon-only swaps added in 2025 | 85 | — | — | Seven swaps on bonds 2044, 2047, 2049 converting coupons to MXN, maturing 2032 |
| Interest-rate swaps, assets (Italy lease, €15m Euribor to fixed ~1.25-1.28%) | 6 | 6 | 10 | |
| Interest-rate swaps, SOFR to fixed (liabilities) | 0 | 0 | 23 | Settled in 2024 (US$35m collected) |
| Total long-term derivative assets / liabilities, 2025 | 657 / 2,314 | — / 689 | | |

- The liability of 2,314 in 2025 reflects the mark-to-market of swaps that pay MXN and receive USD while the peso appreciated; it offsets the lower MXN value of the USD bonds and is an accounting effect, not a cash loss `[assumption]` (the output's explanation; not verified in the filing).
- The asset total of 657 does not include the 85 of coupon-only swaps listed as "new in 2025" (135 + 516 + 6 = 657); unresolved `[unverified]`.
- FX forwards for raw-material purchases at 31-Dec-2024 (notional in millions of the foreign currency, average rate, fair value): Canada USD/CAD 112 at 1.35 (138); Colombia USD/COP 14 at 4,259.29 (12); Mexico USD/MXN 520 at 19.79 (717); Mexico EUR/MXN 3 at 21.56 (1); Chile USD/CLP 60 at 952.10 (56); Peru USD/PEN 11 at 3.75 (1); Uruguay USD/UYU 10. At 31-Dec-2025: USD/CAD 59 at 1.35, FV about 1 `[sourced]`.
- Commodity futures, options, zero-cost collars and input swaps exist, but notionals and fair values are not broken out; virtual power purchase agreements affected Q2 2026 net financing cost `[sourced]` 2Q26 release.

## 5. Leverage target and path

- ==Stated comfort zone: 2.0x to 2.5x net debt / EBITDA, measured without IFRS 16== (call of 22-Feb-2023: "between 2 times to 2.5 times"; the output attributes it to the then-CEO in one place and to the CFO in another, so the speaker is `[unverified]`; the range is also in [[bimbo-leverage-and-deleveraging-commentary]]).
- Q3 2024 call (2024-10-29, CFO): comfort "around 2.5x"; the company was "slightly above that level" and it was "not a concern" `[sourced]`.
- Q2 2026 call (2026-07-23, CFO): "We are now at 2.5x"; 2.7x at end-2025 and 2.9x a year earlier `[sourced]`. ==Bimbo is at the top of its own range==, so further deleveraging is no longer a stated priority beyond that.
- Capital IQ's 20-quarter net debt / EBITDA column (for example 2.90x at Jun-2026, 2.64x at Dec-2025, 3.53x at Mar-2025) was ==not used for the trend==: it does not reproduce from its own columns, it rises from Dec-2025 to Jun-2026 while the company's ratio falls from 2.7x to 2.5x, and it mixes period-end and average exchange rates. Use the management series in [[bimbo-leverage-and-deleveraging-commentary]] and the company's 2.5x.
- Lease-inclusive net debt / EBITDA is ≈2.9x: Capital IQ net debt including leases of US$9,907m (total debt US$10,855m) ÷ LTM EBITDA of MXN 60.9bn at US$0.05569 per peso (US$3,393m) = 2.92x `[calc]`, matching the 2.90x printed in the column. With leases of about MXN 34bn from the filings it is 2.81x. The level at Jun-2026 therefore reconciles; the column's trend does not (see above); see [[peer-leverage-capiq-2026-10]].

## 6. Covenants and change of control

The output found no covenant or change-of-control text. It states that no financial maintenance covenant is disclosed for the US$2,350m facility; the sustainability-linked step-up of the 23-2L is a pricing adjustment, not a covenant `[sourced]`. The change-of-control put on the Mexican bonds is already in [[bimbo-capital-structure-and-debt]]. EBITDA/interest covenant thresholds remain unknown (source: indentures and credit agreement).

## 7. Issuances, repurchases and use of cash

| Date | Event | Amount | Terms |
|---|---|---|---|
| 17-May-2021 | BBU notes due 2051 | US$600m | 4.000% fixed; refinancing |
| 2022 | Open-market repurchases | 2049 notes US$34.885m; 2051 notes US$14.733m; 2044 notes US$2.5m | |
| 30-May to 2-Jun-2023 | BIMBO 23L and 23-2L | Ps. 12,000m / 3,000m | Sustainability-linked; repaid the perpetual subordinated note and bank debt |
| 2-Nov-2023 | BBU notes | US$450m due 2029 (6.050%); US$550m due 2034 (6.400%) | Refinancing |
| 3-Nov-2023 | Cash tender, 3.875% notes due 2024 (US$800m issue) | US$391.638m; remainder (≈ US$392m) prepaid | |
| 9-Jan-2024 | Reopening 2029 notes; new notes | US$450m (total 2029 notes US$900m); US$800m at 5.375% (the output says due 2035; the prospectus says 9-Jan-2036) | |
| 14-Feb-2025 | BIMBO 25 and 25-2 | Ps. 12,762m / 2,238m | Repaid bank debt |
| 6-Feb-2026 | BIMBO 26 and 26-2 | Ps. 7,867m / 4,133m | Refinancing |

- Issuance prices and re-offer yields are not disclosed in the filings (only coupons) `[sourced]`.
- Cash acquisitions (US$, Capital IQ, period-average FX): FY2016 213m; FY2017 662m; FY2018 187m; FY2019 5m; FY2020 162m; FY2021 525m; FY2022 324m; FY2023 370m; FY2024 329m; FY2025 666m `[sourced]`. The output's attribution of FY2017 to Canada Bread is wrong (Canada Bread was 2014; 2017 was East Balt, [[bimbo-cross-source-connections]]).
- Capex growth by year (2016-2025): +36.95%, +2.23%, +12.06%, −12.94%, +0.77%, +56.39%, +38.69%, +21.23%, −15.40%, −23.37% `[sourced]`. Absolute capex, operating cash flow, dividends and buybacks were not returned, so the share of operating cash flow for each use cannot be computed.
- FY2025 returns to shareholders: Ps. 5.6bn through dividends and buybacks; 22,738,214 Series A treasury shares cancelled and a dividend of Ps. 1.075 per share (+7.5%) approved at the April 2026 meeting `[sourced]` (see [[bimbo-agm-dividends-and-buybacks]]).

## Key Takeaways

- ==Bimbo is at 2.5x, the top of its own 2.0x-2.5x comfort range==; the ratio fell from 2.9x to 2.5x in a year and management does not plan extra capital returns.
- Debt is long and mostly fixed: 9.5-year tenor, 6.5% average cost, 82% fixed, 96% long-term; liquidity of about US$3.3bn covers 2026-2027 maturities about 3.3 times; the 2028-2031 cluster is US$3.1bn.
- USD debt is 42% of the total but cross-currency swaps and North American revenue (44.6% of sales) reduce the net exposure.
- Pasted ladder for 2034-2036, the BIMBO 26-2 size and date, and the 20-quarter leverage column were wrong and replaced by the filings.
- Open: after-swap fixed/floating split, covenant thresholds, absolute capex and operating cash flow, and the instrument-level data of the USD and EUR notes.
