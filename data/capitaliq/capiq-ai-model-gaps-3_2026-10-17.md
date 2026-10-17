# Capital IQ AI output — model-gaps Prompt 3 (Bimbo bonds, shares, dividends), pricing date 2026-10-16

_Raw source copy. Pasted by the team on 2026-10-17 from the Capital IQ AI assistant, response to Prompt 3 of `BIMBOA/research/capiq-prompts-model-gaps_2026-10-17.md`. Text and numbers are as received (including its stray citation numerals); tab-separated tables were converted to markdown. This file could not be written to `raw/` (write permission denied); move it there unchanged if you want it in the inbox._

_Result in one line: issuance terms, amounts, the S&P issuer rating and share data came back; clean prices, yields, spreads, instrument ratings, USD coupons and the 2026 dividend and buyback detail did not._

---

## Task 3A – Outstanding Debt Securities (as of 10/16/2026)

The context provides detailed issuance terms for Grupo Bimbo's MXN certificados bursátiles (domestic bonds) and USD international senior notes. However, market pricing data (clean price, YTM, spread to benchmark) and per-security Fitch ratings were not returned by the fixed-income ratings tool (ALL_ENTITIES_UNRESOLVED error for the five CUSIPs queried). The S&P issuer credit rating for Grupo Bimbo is BBB+ (Foreign Currency LT, Negative outlook, last reviewed 05/13/2026). Investor presentations as of Q1 2026 and Q4 2025 reference a combined Moody's/S&P/Fitch rating of "Baa1/BBB+" 123 implying Fitch also carries BBB+ at the issuer level, but no instrument-level Fitch rating is available in the data.

### MXN Certificados Bursátiles (BMV-listed, issued by Grupo Bimbo, S.A.B. de C.V.)

| Ticker | Issuer | CCY | Coupon | Maturity | Amount Outstanding | Clean Price | YTM (%) | Spread (bp) | S&P Rating | Fitch Rating |
|---|---|---|---|---|---|---|---|---|---|---|
| BIMBO 17 | Grupo Bimbo | MXN | Fixed | N/A | MXN 10,000M | N/A | N/A | N/A | N/A | N/A |
| BIMBO 23L | Grupo Bimbo | MXN | Fixed (SLB) | N/A | MXN 12,000M | N/A | N/A | N/A | N/A | N/A |
| BIMBO 23-2L | Grupo Bimbo | MXN | Variable (SLB) | N/A | MXN 3,000M | N/A | N/A | N/A | N/A | N/A |
| BIMBO 25 | Grupo Bimbo | MXN | 10.06% fixed | 02/06/2032 | MXN 12,762M | N/A | N/A | N/A | N/A | N/A |
| BIMBO 25-2 | Grupo Bimbo | MXN | TIIE 28D + 0.34% variable | 02/11/2028 | MXN 2,238M | N/A | N/A | N/A | N/A | N/A |
| BIMBO 26 | Grupo Bimbo | MXN | 9.22% fixed | 01/26/2035 | MXN 7,867M | N/A | N/A | N/A | N/A | N/A |
| BIMBO 26-2 | Grupo Bimbo | MXN | TIIE Fondeo + 0.45% variable | 02/01/2030 | MXN 4,133M | N/A | N/A | N/A | N/A | N/A |

Notes on MXN bonds: 45 All notes are guaranteed by the Company's main subsidiaries. 4 BIMBO 17 maturity date not stated in the available data. BIMBO 23L and 23-2L are sustainability-linked bonds; BIMBO 23-2L triggered a 0.20% step-up (Ps. 6M) for missing its 2025 emission-reduction target. 6 The coupon for BIMBO 26-2 as of the 10/16/2026 coupon notice was 6.98% gross (TIIE Fondeo + 0.45%), paid on 10/16/2026 for the period 09/18/2026–10/16/2026. 7 ISIN/CUSIP for MXN bonds not provided in the available data.

### USD International Senior Notes (Rule 144A / Reg S)

| CUSIP | Issuer | CCY | Coupon | Maturity | Amount Outstanding | Clean Price | YTM (%) | Spread (bp) | S&P Rating | Fitch Rating |
|---|---|---|---|---|---|---|---|---|---|---|
| N/A | Grupo Bimbo | USD | N/A | 2044 | $500M | N/A | N/A | N/A | N/A | N/A |
| N/A | Grupo Bimbo | USD | N/A | 2047 | $650M | N/A | N/A | N/A | N/A | N/A |
| N/A | Grupo Bimbo | USD | N/A | 2049 | $600M | N/A | N/A | N/A | N/A | N/A |
| USP1666MAA14 | Bimbo Bakeries USA, Inc. | USD | N/A | 2051 | $600M | N/A | N/A | N/A | N/A | N/A |
| USP1666MAB96 | Bimbo Bakeries USA, Inc. | USD | N/A | 2034 | $550M | N/A | N/A | N/A | N/A | N/A |
| USP1666MAC79 | Bimbo Bakeries USA, Inc. | USD | N/A | 2029 | $450M + $450M reopening | N/A | N/A | N/A | N/A | N/A |
| US09072FAC37 | Bimbo Bakeries USA, Inc. | USD | N/A | 2029 | (reopening – see above) | N/A | N/A | N/A | N/A | N/A |
| US09072FAD10 | Bimbo Bakeries USA, Inc. | USD | N/A | 2036 | $800M | N/A | N/A | N/A | N/A | N/A |

Notes on USD bonds: 5 Issuance amounts are as originally issued; outstanding amounts may differ due to any buybacks (not quantified in available data). The 2029 notes were issued in Nov 2023 ($450M) and reopened in Jan 2024 ($450M additional). Coupon rates for the USD bonds are not stated in the available documents. CUSIPs for the three Grupo Bimbo parent USD bonds (2044, 2047, 2049) are not provided in the available data. The fixed-income ratings tool returned ALL_ENTITIES_UNRESOLVED for the five CUSIPs queried, so no per-security S&P or Fitch instrument ratings are available from that source.

Issuer-level S&P rating (Grupo Bimbo, S.A.B. de C.V.): BBB+ Foreign Currency LT, Negative outlook, effective 03/29/2023, last reviewed 05/13/2026. Source: S&P Capital IQ.

## Task 3B – Share Capital

| Metric | Value | Date |
|---|---|---|
| Total shares outstanding (Series "A", authorized & issued) | 4,304,744,119 | 12/31/2025 4 |
| Total shares outstanding (ECS, S&P CIQ) | 4,296,284,215 | 06/30/2026 |
| Shares outstanding (BMV filing) | 4,295,159,215 | 07/28/2026 8 |
| Weighted avg. basic shares outstanding (LTM Jun 2026) | 4,309,247,348 | LTM 06/30/2026 |
| Diluted shares outstanding | N/A | — |
| Treasury shares (value, USD '000s) | ($429) | LTM 06/30/2026 |
| Reserve for share repurchases (approved ceiling, at face value) | MXN 15,200M | 12/31/2025 49 |
| Free float % | N/A | — |

Treasury shares (number): The 04/30/2026 AGM approved the cancellation of 22,738,214 Series "A" treasury shares repurchased between January and December 2025. 456 After that cancellation, the residual treasury share count is not separately stated in the available data. The financial statements report treasury stock at a carrying value of ($429) thousand USD (MXN-denominated) as of LTM Jun 2026. Source: S&P Capital IQ Financials.

Share repurchases 07/01/2026–10/16/2026: The Q2 2026 earnings release (07/23/2026) states that the Company returned Ps. 5.3 billion to shareholders through dividends and share buybacks during the first half of 2026 (H1 2026, i.e., through 06/30/2026). 10 No separate disclosure of the number of shares repurchased or the MXN amount attributable solely to the period 07/01/2026–10/16/2026 is available in the provided data.

## Task 3C – Dividends Per Share and Buyback Ceiling

| Year | Declaration Date | Ex-Date | Payment Date | Amount per Share (MXN) | Total Dividend (MXN millions) | Approved Annual Buyback Ceiling |
|---|---|---|---|---|---|---|
| 2023 | 04/26/2023 | N/A | 05/18/2023 | MXN 0.78 | MXN 3,458M | MXN 15,200M (face value) 49 |
| 2024 | 04/30/2024 | N/A | 05/14/2024 | MXN 0.94 | MXN 4,125M | MXN 15,200M (face value) 49 |
| 2025 | 04/30/2025 | N/A | 05/14/2025 | MXN 1.00 | MXN 4,316M | MXN 15,200M (face value) 49 |
| 2026 YTD | N/A | N/A | N/A | N/A | N/A | N/A |

Sources: 459 Dividend amounts in MXN millions represent the total declared (e.g., MXN 3,458M for 2023 = MXN 0.78 × ~4.43B shares). Ex-dates are not disclosed in the available documents. The 2025 dividend (MXN 1.00/share) was declared at the 04/30/2025 AGM and paid from 05/14/2025. 4

2026 YTD dividend: No 2026 dividend declaration has been disclosed in the available data. The Q2 2026 earnings call (07/23/2026) references Ps. 5.3 billion returned to shareholders through dividends and share buybacks combined in H1 2026 10 but does not break out a 2026 per-share dividend declaration separately. The 3Q26 earnings release was scheduled for 10/22/2026 11 — after the 10/16/2026 pricing date — so any 2026 dividend announcement therein is not captured here.

Buyback ceiling: The reserve for share repurchases approved at face value is MXN 15,200M, unchanged across 2022–2025. 49 A 2026-specific buyback ceiling approved at the 04/30/2026 AGM is not separately stated in the available data (the AGM approved the cancellation of 22,738,214 treasury shares 4 but did not state a new ceiling amount in the excerpts available).

## Items Not Retrieved

- Task 3A – Clean prices, YTM, and spread to benchmark for all bonds: Market pricing data was not available in the provided context for any security.
- Task 3A – Per-security S&P and Fitch instrument ratings: The fixed-income ratings tool returned ALL_ENTITIES_UNRESOLVED for all five CUSIPs queried (USP1666MAA14, USP1666MAB96, USP1666MAC79, US09072FAC37, US09072FAD10). No instrument-level ratings were returned.
- Task 3A – ISIN/CUSIP for MXN certificados bursátiles: Not disclosed in the available documents.
- Task 3A – ISIN/CUSIP for the three Grupo Bimbo parent USD bonds (2044, 2047, 2049): Not disclosed in the available documents.
- Task 3A – Coupon rates for USD international senior notes: Not stated in the available documents.
- Task 3A – Maturity date for BIMBO 17: Not stated in the available documents.
- Task 3B – Diluted shares outstanding: Returned as N/A (Diluted NAV Shares = NA) in S&P Capital IQ Financials.
- Task 3B – Free float %: Not available in the provided data.
- Task 3B – Treasury share count (post-April 2026 cancellation): Residual number of treasury shares after the 22,738,214-share cancellation approved 04/30/2026 is not stated.
- Task 3B – Share repurchases 07/01/2026–10/16/2026 (number of shares and MXN amount): Not separately disclosed; only an aggregate H1 2026 figure combining dividends and buybacks (Ps. 5.3B) is available.
- Task 3C – Ex-dates for all dividends: Not disclosed in the available documents.
- Task 3C – 2026 dividend per share declaration: No 2026 dividend has been declared or disclosed in the data available as of the 10/16/2026 pricing date.
- Task 3C – 2026 annual buyback ceiling (specific amount): Not stated in the 04/30/2026 AGM disclosures available.
