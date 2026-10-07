---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Capital Structure Details/2026FQ2 filed Jul 24, 2026/SPGlobal_GrupoBimbo,S.A.B.deC.V._CapitalStructureDetails_19-Sep-2026 (43).xlsx
  - filings/capitaliq/Financials/Templated/Capital Structure Details/2026FQ1 filed Apr 30, 2026/SPGlobal_GrupoBimbo,S.A.B.deC.V._CapitalStructureDetails_19-Sep-2026 (42).xlsx
  - filings/capitaliq/Financials/Templated/Capital Structure Details/2025FY filed May 01, 2026/SPGlobal_GrupoBimbo,S.A.B.deC.V._CapitalStructureDetails_20-Sep-2026 (22).xlsx
  - filings/capitaliq/Financials/Templated/Capital Structure Summary/SPGlobal_GrupoBimbo,S.A.B.deC.V._CapitalStructureSummary_19-Sep-2026.xlsx
  - filings/annual/IA25_GB_EEFF_V10.pdf
tags: [Valuation, debt-stack]
---

# Grupo Bimbo — Debt Stack and Maturity Ladder, 30-Jun-2026 (Capital IQ)

Instrument-level debt at **2026FQ2 (period ended 30-Jun-2026, filed 24-Jul-2026)** from S&P Capital IQ (CIQ) "Capital Structure Details" (basis "As Reported") and "Capital Structure Summary" (basis "Current/Restated"), downloaded **2026-09-19/20**. CIQ magnitude is MXN thousands; shown here in **MXN millions**. CIQ converts foreign-currency instruments into MXN; the column "Repayment Currency" gives the original currency. Tidy data: `data/capitaliq/debt_instruments_by_period.csv` (all 74 periods 2002FY–2026FQ2) and `data/capitaliq/capital_structure_summary.csv`. Filing-based view (covenants, ratings, hedges, company maturity table): [[bimbo-capital-structure-and-debt]]. CIQ bond-level market data (prices, CUSIPs): [[ciq-corporate-issuance-history]]. History: [[ciq-debt-evolution-2019-2026]].

Instrument rows: [sourced] CIQ CapitalStructureDetails 2026FQ2, sheet 'Capital Structure Details'. Aggregates: [sourced] CIQ CapitalStructureSummary, sheet 'Capital Structure Summary', column 2026 FQ2.

## 1. Tranche table, 30-Jun-2026

### 1a. USD senior notes (fixed)

| Note | Coupon | Maturity | MXN m | Implied USD m [calc] | Filing face USD m (EEFF25 p.47–48) |
|---|---|---|---|---|---|
| 2029 | 6.050% | 15-Jan-2029 | 15,723.0 | 900.0 | 900 (450 + 450 reopening) |
| 2034 | 6.400% | 15-Jan-2034 | 9,608.5 | 550.0 | 550 |
| 2036 | 5.375% | 9-Jan-2036 | 13,976.0 | 800.0 | 800 |
| 2044 | 4.875% | 27-Jun-2044 | 8,691.3 | 497.5 | 498 outstanding |
| 2047 | 4.700% | 10-Nov-2047 | 11,355.5 | 650.0 | 650 |
| 2049 | 4.000% | 6-Sep-2049 | 9,783.5 | 560.0 | 560 outstanding |
| 2051 | 4.000% | 17-May-2051 | 10,224.6 | 585.3 | 585 outstanding |
| **Total** | **5.13% wtd [calc]** | | **79,362.4** | **4,542.8** | **4,543** |

Implied USD [calc] = MXN amount ÷ 17.47, the conversion rate implied by the 2029 line (15,723,000 ÷ 900,000) and consistent with every round USD tranche. The 2Q26 release also converts at 17.47 (per [[bimbo-capital-structure-and-debt]]).

### 1b. MXN Certificados Bursátiles

| Series | Rate | Maturity | MXN m |
|---|---|---|---|
| Bimbo 23-2L | TIIE 28d + 10 bp | 24-Jul-2026 | 3,006.0 |
| Bimbo 17 | 8.18% fixed | 24-Sep-2027 | 9,633.1 |
| Bimbo 25-2 | TIIE + 34 bp | 11-Feb-2028 | 2,238.0 |
| Bimbo 26-2 | TIIE + 45 bp | 1-Feb-2030 | 4,133.4 |
| Bimbo 25 | 10.06% fixed | 6-Feb-2032 | 12,762.0 |
| Bimbo 23L | 9.24% fixed | 20-May-2033 | 12,000.0 |
| Bimbo 26 | 9.22% fixed | 26-Jan-2035 | 7,866.6 |
| **Total** | fixed portion 9.24% wtd [calc] | | **51,639.1** |

- Bimbo 16 (7.56%, due 2-Sep-2026) is **absent** at 2026FQ2 and shows 0 at 2026FQ1 [sourced], i.e. it was retired before 31-Mar-2026, ahead of its maturity.
- Bimbo 23-2L carries 3,006.0 vs 3,000 face in the company table at Dec-25 (EEFF25 p.49) — a +6.0 difference [calc] not explained in CIQ. It matured on 24-Jul-2026, the CIQ filing date.

### 1c. Bank debt and other

| Facility | Type (CIQ) | Rate | Maturity | Currency | MXN m | Implied original ccy [calc] |
|---|---|---|---|---|---|---|
| Syndicated revolver Tranche A | Revolving | various benchmarks | 31-Jul-2030 | multi | 0 | undrawn |
| Syndicated revolver Tranche B | Revolving | various benchmarks | 15-Mar-2028 | multi | 0 | undrawn |
| Revolving line (BBVA, per filings) | Revolving | TIIE 28d + 85 bp | 13-Apr-2028 | MXN | 5,000.0 | — |
| Citi México | Revolving | SOFR + 95 bp | 4-Apr-2027 | USD | 1,747.0 | USD 100.0m |
| Bank of America loan (sust.-linked, amortising) | Term | SOFR + 120 bp | 11-Aug-2026 to 11-Aug-2028 | USD | 1,747.0 | USD 100.0m |
| HSBC México loan (amortising) | Term | SOFR + 120 bp | 15-Sep-2027 to 15-Mar-2029 | USD | 1,637.8 | USD 93.75m |
| BNP Paribas | Revolving | SOFR + 110 bp | 26-Sep-2029 | USD | 2,620.5 | USD 150.0m |
| Rabobank | Revolving | EURIBOR + 95 bp | 22-May-2028 | EUR | 2,988.4 | EUR 150.0m (at 19.92) |
| CaixaBank | Revolving | EURIBOR + 90 bp | 15-Dec-2028 | EUR | 1,494.2 | EUR 75.0m |
| Bank of America (USD line) | Revolving | SOFR + 110 bp | 2-Dec-2030 | USD | 1,746.9 | USD 100.0m |
| Bank of America (CAD line) | Revolving | CORRA + 110 bp | 2-Dec-2030 | CAD | 1,036.8 | CAD 84.0m (at 12.34) |
| Subsidiary operating lines | Revolving | n/d | n/d | MXN | 3,476.4 | — |
| **Bank debt total (CIQ "Total Bank Debt")** | | | | | **23,495.1** | |
| Lease liabilities (IFRS 16) | Capital lease | — | — | MXN | 33,360.9 | — |

- ==HSBC loan fell from USD 125m (Dec-25: 2,246 ÷ 17.966 [calc]) to USD 93.75m by 2026FQ1== [calc], although the filings describe four equal semi-annual payments starting 15-Sep-2027 (per [[bimbo-capital-structure-and-debt]]). A USD 31.25m early repayment is implied [calc]; the cause is not in CIQ [unverified].
- The JPMorgan Chase USD loan (SOFR + 125 bp) shows 0 at 2026FQ1 and is absent at 2026FQ2 [sourced] — repaid.
- Undrawn revolving credit: 41,062.3 [sourced, Summary] ≈ USD 2,350m × 17.47 = 41,054.5 [calc], i.e. the full syndicated revolver.

### 1d. Totals and bridge to the Summary

| MXN m | Amount | Check |
|---|---|---|
| USD notes | 79,362.4 | |
| MXN Certificados Bursátiles | 51,639.1 | |
| Bank debt | 23,495.1 | |
| **Principal ex leases** | **154,496.6** [calc] | |
| Leases | 33,360.9 | |
| **Total principal due (CIQ)** | **187,857.5** [sourced] | instrument sum = 187,857.5 [calc], ties exactly |
| Unamortized premium | 157.2 [sourced] | |
| Total adjustments | 1,664.6 [sourced] | = hedging & derivative adjustments 2,658.4 [sourced] − issuance costs ≈ 994 [calc] |
| **CIQ total debt** | **189,679.4** [sourced] | |
| Cash & ST investments | 16,563.0 [sourced] | |
| **CIQ net debt** | **173,116.4** [sourced] | |

## 2. Maturity ladder by final maturity (principal ex leases, MXN m)

| Year | Amount [calc] | % of 154,497 [calc] | Cumulative % [calc] | Instruments |
|---|---|---|---|---|
| 2026 (2H) | 3,006 | 1.9% | 1.9% | Bimbo 23-2L |
| 2027 | 11,380 | 7.4% | 9.3% | Bimbo 17; Citi |
| 2028 | 13,468 | 8.7% | 18.0% | Bimbo 25-2; BBVA revolver 5,000; Rabobank; CaixaBank; BofA amortising loan (final) |
| 2029 | 19,981 | 12.9% | 31.0% | USD 6.05% 2029; BNP; HSBC (final) |
| 2030 | 6,917 | 4.5% | 35.4% | Bimbo 26-2; BofA USD and CAD lines |
| 2031 | 0 | 0% | 35.4% | — |
| 2032 | 12,762 | 8.3% | 43.7% | Bimbo 25 |
| 2033 | 12,000 | 7.8% | 51.5% | Bimbo 23L |
| 2034 | 9,609 | 6.2% | 57.7% | USD 6.40% 2034 |
| 2035 | 7,867 | 5.1% | 62.8% | Bimbo 26 |
| 2036 | 13,976 | 9.0% | 71.8% | USD 5.375% 2036 |
| 2044 | 8,691 | 5.6% | 77.4% | USD 4.875% 2044 |
| 2047 | 11,356 | 7.3% | 84.8% | USD 4.70% 2047 |
| 2049 | 9,783 | 6.3% | 91.1% | USD 4.00% 2049 |
| 2051 | 10,225 | 6.6% | 97.7% | USD 4.00% 2051 |
| No maturity given | 3,476 | 2.3% | 100% | Subsidiary operating lines |

- Amortising loans (BofA, HSBC) are placed in their **final** maturity year; the filings' schedules (BofA USD 12.5m Aug-26 and Aug-27; HSBC semi-annual from Sep-27) would move roughly 0.2–0.9bn into 2026–2028 [calc, approximate].
- ==Weighted average remaining tenor: 9.4 years [calc]== (amount-weighted, final maturity, ex leases and undated lines) vs company-reported 9.5 years at Jun-26 (2Q26 release p.6, via [[bimbo-capital-structure-and-debt]]).
- Only 18.0% of principal falls due before end-2028 [calc]; the largest single year is 2029 (19,981, 12.9%).
- CIQ Summary "Fixed Payment Schedule" is populated only at fiscal year-ends; the latest (Dec-25, debt + finance and capitalised leases) is: +1 yr 19,711; +2 16,992; +3 20,463; +4 23,229; +5 5,672; after 5 yrs 102,386 [sourced]. These tie to the company maturity table plus lease schedule (e.g. +2 = 12,386 debt + 4,606 leases [calc] per EEFF25 p.52 and p.43 as reported in [[bimbo-capital-structure-and-debt]]).

## 3. Fixed vs floating

| MXN m | Amount | % of principal ex leases [calc] |
|---|---|---|
| Fixed (USD notes + Bimbo 17/23L/25/26) | 121,624.1 [sourced, CIQ "Fixed Rate Debt"] | 78.7% |
| Floating (TIIE CBs 9,377.4; BBVA 5,000; bank lines 15,018.6) | 29,396.0 [sourced, CIQ "Variable Rate Debt"] | 19.0% |
| Rate not given (subsidiary operating lines) | 3,476.4 [calc] | 2.3% |

- Instrument-level sums tie to the CIQ Summary [calc: fixed 79,362.4 + 42,261.7 = 121,624.1; floating 3,006 + 2,238 + 4,133.4 + 5,000 + 12,234.9 + 2,783.7 = 29,396.0].
- This split is **before swaps**; the company does not disclose a post-swap fixed/floating split (see [[bimbo-capital-structure-and-debt]] §5).

## 4. Currency mix (repayment currency, before derivatives)

| Currency | MXN m [calc] | Share [calc] | Company mix after derivatives, Jun-26 |
|---|---|---|---|
| USD | 88,861.6 | 57.5% | 42% |
| MXN | 60,115.5 | 38.9% | 42% |
| EUR | 4,482.6 | 2.9% | 12% |
| CAD | 1,036.8 | 0.7% | 3% |
| GBP | 0 | 0% | 1% |

Company column [sourced] 2Q26 release p.6 as reported in [[bimbo-capital-structure-and-debt]]. ==The gap (USD 57.5% pre-swap vs 42% post-swap) is the cross-currency swap overlay== that converts part of the USD notes into EUR, GBP and MXN [calc, inference from the two bases]. See [[bimbo-fx-exposure]].

## 5. Coupon

| Bucket | Principal MXN m | Weighted coupon [calc] | Annual coupon MXN m [calc] |
|---|---|---|---|
| USD notes | 79,362.4 | 5.13% | 4,075.1 |
| MXN fixed CBs | 42,261.7 | 9.24% | 3,905.9 |
| **All fixed-rate debt** | **121,624.1** | **6.56%** | **7,981.1** |

- Floating instruments carry spreads of TIIE + 10 to 85 bp, SOFR + 95 to 120 bp, EURIBOR + 90 to 95 bp and CORRA + 110 bp [sourced]; CIQ gives no base-rate fixings, so an all-in floating coupon is not computed.
- CIQ "W/Average Interest Rate: Long-term Debt" at 2026FQ2: 6.5% [sourced], equal to the company's average cost of 6.5% (2Q26 release p.6, via [[bimbo-capital-structure-and-debt]]).

## 6. CIQ classifications to treat with care

> [!warning] "Secured" flag is a CIQ misclassification
> CIQ marks all seven USD notes and Bimbo 26 / 26-2 as "Secured? Yes — Tangible Asset", giving "Secured Debt" of 124,723.3 [sourced] = USD notes 79,362.4 + Bimbo 26/26-2 12,000.0 + leases 33,360.9 [calc]. The filings describe the notes as senior obligations ranking pari passu, backed by **subsidiary guarantees** ("Dada la estructura de garantías…", EEFF25 p.47), not collateral; the older Bimbo CBs are flagged "No" in the same file. Only the leases are secured (on the leased vehicles, per [[bimbo-capital-structure-and-debt]]). The CIQ Securities Summary lists the same notes as senior unsecured ([[ciq-corporate-issuance-history]]). Do not use CIQ secured/unsecured ratios.

- CIQ "Net Debt" (173,116) **includes leases (33,361) and derivative liabilities (2,658)**; company net debt is 137,097 [calc: 173,116.4 − 33,360.9 − 2,658.4 = 137,097.1], matching the company figure exactly (2Q26 release p.6, via [[bimbo-capital-structure-and-debt]]).
- CIQ "Net Debt / EBITDA" 2.9x [sourced] is on CIQ's lease-inclusive basis and is not comparable with the company's 2.5x (ex-IFRS 16).

## 7. Reconciliation with company filings

| Item | CIQ | Company (via [[bimbo-capital-structure-and-debt]]) | Difference [calc] |
|---|---|---|---|
| USD notes, Jun-26 | 79,362.4 | 79,362 (BMV Jun-26 p.52) | 0 |
| MXN CBs, Jun-26 | 51,639.1 | 51,639 | 0 |
| Bilateral bank loans (Citi, BofA loan, HSBC, BNP, Rabo, Caixa), Jun-26 | 12,234.9 [calc] | 12,235 | 0 |
| Subsidiary bilaterals (BofA USD + CAD), Jun-26 | 2,783.7 [calc] | 2,784 | 0 |
| Debt ex leases, carrying value, Jun-26 | 189,679.4 − 33,360.9 − 2,658.4 = 153,660.1 [calc] | 153,660 | 0 |
| Leases, Jun-26 | 33,360.9 | 33,361 | 0 |
| Net debt, Jun-26 | 137,097.1 [calc, ex leases and derivatives] | 137,097 | 0 |
| Debt ex leases, Dec-25 | 190,767 − 34,790 − 2,314 = 153,663 [calc] | 153,663 (EEFF25 p.52) | 0 |
| Net debt, Dec-25 | 182,232 − 34,790 − 2,314 = 145,128 [calc] | 145,128 | 0 |
| Each USD note, Dec-25 (2029 / 2034 / 2036 / 2044 / 2047 / 2049 / 2051) | 16,170 / 9,882 / 14,373 / 8,938 / 11,678 / 10,062 / 10,515 [sourced, CIQ 2025FY] | identical (EEFF25 p.47–48) | 0 |

The CIQ stack ties to the filings at instrument level; the only reconciling items are CIQ's inclusion of leases and derivative liabilities in total and net debt.

## Key Takeaways

- At 30-Jun-2026 CIQ shows principal of 154,497 ex leases [calc]: USD notes 79,362 (51%), MXN bonds 51,639 (33%), bank debt 23,495 (15%); leases add 33,361.
- The ladder is long: 18.0% of principal matures by end-2028, 31.0% by end-2029 and 35.0% in 2036 or later [calc: 54,031 / 154,497]; weighted tenor 9.4 years [calc] vs company 9.5.
- 78.7% fixed before swaps [calc]; weighted fixed coupon 6.56% (USD notes 5.13%, MXN fixed bonds 9.24%) [calc].
- Pre-swap currency mix is 57.5% USD / 38.9% MXN [calc] vs the company's post-swap 42/42 — swaps move USD debt into EUR, GBP and MXN.
- CIQ total and net debt include leases and derivative liabilities; removing them reproduces company total debt (153,660) and net debt (137,097) exactly. CIQ "secured" flags on the notes are wrong.
