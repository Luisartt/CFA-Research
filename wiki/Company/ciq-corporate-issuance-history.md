---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/OwnerShip/Corporate Issuance/Securities Summary/SPGlobal_GrupoBimbo,S.A.B.deC.V._SecuritiesSummary_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Fixed Income Profile/Debt Maturity Profile/SPGlobal_GrupoBimbo,S.A.B.deC.V.BMVBIMBOA(MIKEY4276592;SPCIQKEY877906)_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Fixed Income Profile/Securities Pipeline/SPGlobal_GrupoBimbo,S.A.B.deC.V.BMVBIMBOA(MIKEY4276592;SPCIQKEY877906)_06-Oct-2026 (1).xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Fixed Income Profile/Summary/SPGlobal_GrupoBimbo,S.A.B.deC.V._FixedIncomeProfile(CreditRatings)_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Credit Rating/SPGlobal_GrupoBimbo,S.A.B.deC.V._CreditRatings(CurrentRatings)_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Credit Default Swaps/SPGlobal_GrupoBimbo,S.A.B.deC.V._CreditDefaultSwaps_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Dividends & Splits/SPGlobal_GrupoBimbo,S.A.B.deC.V._DividendsAndSplits_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Equity Listing/SPGlobal_GrupoBimbo,S.A.B.deC.V._EquityListings_06-Oct-2026.xlsx
  - filings/annual/IA25_GB_EEFF_V10.pdf
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Jun_26.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf
tags: [Company, corporate-issuance]
---

# Grupo Bimbo — Corporate Issuance History (Capital IQ)

Bonds, loans, ratings, CDS and dividends as carried by S&P Capital IQ (CIQ), downloaded **2026-10-06**. Amounts in **MXN thousands** in the CIQ files; shown here in **MXN millions** (÷1,000) unless stated. Tidy data: `data/capitaliq/corporate_issuance.csv` (sections `debt_maturity_profile`, `securities_summary_debt`, `pipeline_*`, `debt_summary_2026FQ2`, `credit_ratios_2026FQ2`, `credit_rating_*`, `cds_*`, `dividends_*`, `equity_listings`). Filing-based debt detail: [[bimbo-capital-structure-and-debt]]; payouts: [[bimbo-shareholder-returns]]; ownership: [[ciq-ownership-structure]].

> [!warning] Do not sum CIQ instrument rows
> CIQ lists 144A and Reg S CUSIPs of the same bond as separate rows, each with the **full** issue amount (e.g. 2047 notes: 40052VAE4 and P4R52QAC9, 11,679 each). The 2029 BBU notes appear three times (one 144A line for USD 900m plus two Reg S lines of USD 450m). Use the deduplicated table below or the CIQ Debt Summary total.

## 1. Bonds outstanding (deduplicated, CIQ as of 2026-10-06)

| Issue (filing name) | Issuer | Coupon | Issued | Maturity | Amount (MXN m) | Face | S&P issue rating | Price (%) |
|---|---|---|---|---|---|---|---|---|
| Bimbo 17 | Grupo Bimbo | 8.18% fixed | 2017-10-06 | 2027-09-24 | 10,000 | MXN | mxAAA | 95.08 |
| Bimbo 25-2 | Grupo Bimbo | floating (CIQ label 6.85) | 2025-02-14 | 2028-02-11 | 2,238 | MXN | mxAAA | – |
| BBU 6.05% 2029 | Bimbo Bakeries USA | 6.05% | 2023-11-02 (+ re-tap 2024-01-09) | 2029-01-15 | 16,171 | USD 900m [calc] | BBB+ | 100.89 |
| Bimbo 26-2 | Grupo Bimbo | floating (CIQ label 6.95) | 2026-02-06 | 2030-02-01 | 4,133 | MXN | not shown | – |
| Bimbo 25 | Grupo Bimbo | 10.06% fixed | 2025-02-14 | 2032-02-06 | 12,762 | MXN | mxAAA | – |
| Bimbo 23L (sustainability-linked) | Grupo Bimbo | 9.24% fixed | 2023-06-02 | 2033-05-20 | 12,000 | MXN | mxAAA | – |
| BBU 6.40% 2034 | Bimbo Bakeries USA | 6.40% | 2023-11-02 | 2034-01-15 | 9,883 | USD 550m [calc] | BBB+ | 101.57 |
| Bimbo 26 | Grupo Bimbo | 9.22% fixed | 2026-02-06 | 2035-01-26 | 7,867 | MXN | not shown | – |
| BBU 5.375% 2036 | Bimbo Bakeries USA | 5.375% | 2024-01-09 | 2036-01-09 | 14,375 | USD 800m [calc] | BBB+ | 93.42 |
| GB 4.875% 2044 | Grupo Bimbo | 4.875% | 2014-06-27 | 2044-06-27 | 8,984 | USD 500m [calc] | BBB+ | 82.35 |
| GB 4.70% 2047 | Grupo Bimbo | 4.70% | 2017-11-10 | 2047-11-10 | 11,679 | USD 650m [calc] | BBB+ | 77.48 |
| GB 4.00% 2049 | Grupo Bimbo | 4.00% | 2019-09-06 | 2049-09-06 | 10,781 | USD 600m [calc] | BBB+ | 68.20 |
| BBU 4.00% 2051 | Bimbo Bakeries USA | 4.00% | 2021-05-17 | 2051-05-17 | 10,781 | USD 600m [calc] | BBB+ | 67.43 |
| **Total** | | | | | **≈131,654** [calc] | | | |

Amounts, coupons, dates, ratings and prices [sourced] CIQ SecuritiesSummary, sheet 'Securities Summary', and CIQ Debt Maturity Profile, sheet 'Grupo Bimbo S.A.B. de C.V.'. USD face [calc] = MXN amount ÷ 17.968, the conversion rate implied by every USD line (e.g. 14,374,640 / 800,000) — CIQ does not state its FX date. Filing names from EEFF25 p.49 and p.87.

- Also listed, no amount: Compañía de Alimentos Fargo variable-rate notes due 2040 and 2041 (issued 2009-01-20) [sourced]; legacy Argentine subsidiary paper.
- **Issuance timeline** [sourced]: 2014 USD 500m 2044 → 2017 MXN 10bn Bimbo 17 + USD 650m 2047 → 2019 USD 600m 2049 → 2021 USD 600m 2051 (BBU) → Jun-2023 MXN 15bn sustainability-linked (23L 12bn + 23-2L 3bn) → Nov-2023 BBU USD 450m 2029 + USD 550m 2034 → Jan-2024 BBU USD 800m 2036 + USD 450m 2029 re-tap → Feb-2025 MXN 15bn (25 + 25-2) → Feb-2026 MXN 12bn (26 + 26-2). ==Funding has rotated toward BBU (US subsidiary) dollar notes and peso Cebures since 2023.==
- **Callable schedule** (sheet 'Upcoming Callable') [sourced]: par calls 1–6 months before maturity — 2029s from 2028-12-15, 2034s from 2033-10-15, 2036s from 2035-10-09, 2047s from 2047-05-10, 2049s from 2049-03-06, 2051s from 2050-11-17.
- Low dollar coupons (4.0–4.875%) on the 2044–2051 notes trade at 67–82% of par [sourced], i.e. well below face — relevant if the team marks debt to market for EV.

## 2. Bank lines (CIQ, outstanding MXN m)

| Line | Currency | Opened | Maturity | Drawn |
|---|---|---|---|---|
| Banco Citi México revolver | USD | 2023-10-04 | 2027-04-04 | 1,801 |
| Syndicated revolver Tranche B | MXN | 2023-03-15 | 2028-03-15 | 0 |
| Revolving line (MXN, TIIE) | MXN | 2023-04-13 | 2028-04-13 | 5,000 |
| Rabobank line | EUR | 2025-05-22 | 2028-05-22 | 3,030 |
| Caixabank line | EUR | 2025-12-16 | 2028-12-15 | 1,518 |
| HSBC México term loan | USD | 2024-03-13 | 2029-03-15 | 1,684 |
| BNP Paribas line | USD | 2024-09-24 | 2029-09-26 | 2,701 |
| Syndicated revolver Tranche A | MXN | 2022-07-01 | 2030-07-31 | 0 |

All [sourced] CIQ SecuritiesSummary. The listed lines sum to 15,735 [calc], below the CIQ Debt Summary revolver + term total of 23,495 [calc] — the gap (~7.8bn) is not itemised in the CIQ files. A stale "Grupo Bimbo RC" (USD, first lien, matured 2023-10-07) is still flagged "Active" [sourced].

## 3. Debt summary and credit ratios, 2026FQ2 (period ended 2026-06-30)

| Item (CIQ label) | MXN m [sourced] |
|---|---|
| Revolving credit | 20,110 |
| Term loans | 3,385 |
| Senior bonds and notes | 131,002 |
| Leases | 33,361 |
| Total principal due | 187,858 |
| Unamortized premium / other adjustments | 157 / 1,665 |
| **Total debt** | **189,679** |

| Ratio (CIQ) | x [sourced] |
|---|---|
| Net debt / EBITDA | 2.9 |
| Total debt / EBITDA | 3.18 |
| Net debt / (EBITDA − capex) | 4.02 |
| Total debt / (EBITDA − capex) | 4.41 |
| Total senior secured / EBITDA | 2.09 |

Source: CIQ FixedIncomeProfile, sheets 'Debt Summary (Mex$000)' and 'Credit Ratios (x)'.
- Implied LTM EBITDA ≈ 189,679 / 3.177 = **59,704** [calc]; implied capex ≈ 59,704 − 189,679 / 4.406 = 16,654 [calc]. CIQ net debt = 2.9 × 59,704 ≈ 173,116 = total debt − cash 16,563 [calc] → ==CIQ net debt includes leases==.
- "Senior secured / EBITDA 2.09x" implies ~124.7bn secured debt [calc], yet every CIQ instrument except leases is senior unsecured. Treat this ratio as a CIQ classification error [unverified].

## 4. Credit ratings (S&P only; CIQ CreditRatings, sheet 'Current Ratings')

| Scale | Rating | Since | Last review | Outlook (date) |
|---|---|---|---|---|
| Foreign-currency LT issuer | BBB+ | 2023-03-29 | 2026-05-13 | ==Negative (2025-03-20)== |
| Local-currency LT issuer | BBB+ | 2023-03-29 | 2026-05-13 | Negative (2025-03-20) |
| CaVal Mexico national LT | mxAAA (upgraded from mxAA+) | 2023-03-29 | 2026-09-14 | Stable |
| CaVal Mexico national ST | mxA-1+ (new) | 2024-12-06 | 2026-09-14 | – |
| MXN 5bn short-term programme | mxA-1+ | 2024-12-06 | 2026-09-14 | – |

All [sourced]. Subsidiaries: Compañía de Alimentos Fargo NR (previous D, 2003) and Earthgrains Bakery Group NR (previous AA-, 1996) [sourced] sheet 'Subsidiaries'. The 'Ratings History' sheet is empty (subscription-limited).
- Filings state BBB+ (S&P), BBB+ (Fitch), Baa1 (Moody's), upgraded in 1H23 (RA25 p.82) [sourced], but give **no outlooks**. The S&P **negative outlook since Mar-2025** appears only in CIQ — it is new information relative to the filings. Fitch and Moody's are not in the CIQ export.

## 5. Credit default swaps (CIQ, SNRFOR USD CR14, par spread mid, bp)

| Curve date | 1Y | 3Y | 5Y | 7Y | 10Y |
|---|---|---|---|---|---|
| 2026-07-05 | 18.0 | 32.9 | 50.7 | 65.7 | 83.7 |
| 2026-09-05 | 18.9 | 32.3 | 48.5 | 63.0 | 80.4 |
| 2026-10-05 | 22.0 | 38.0 | 54.9 | 69.6 | 86.5 |

[sourced] CIQ CreditDefaultSwaps, sheet 'Sheet1'. 5Y history 2025-10-05 to 2026-10-05 (366 daily points) in the CSV.
> [!warning] Methodology break in the 5Y series
> Points labelled "Composite" (Oct-2025 to 26-May-2026, except 19–23 Apr 2026) sit at **142–158bp**; points labelled "Evaluated" (27-May-2026 onward, and 19–23 Apr) sit at **47–58bp** [sourced]. The jump coincides with the pricing-method switch, not a credit event. Do not read the series as a ~100bp tightening.

## 6. Equity: dividends and splits (CIQ DividendsAndSplits)

| Year | DPS (MXN) | Ex-date | Pay date | CIQ frequency | Filing check |
|---|---|---|---|---|---|
| 2026 | 1.075 | 2026-05-12 | 2026-05-13 | Annual | 4,626.7m declared (BMV Jun-26 p.21); 4,626.7 / 1.075 = 4,304m shares [calc] ≈ 4,304.7m Series A (p.96) → ties |
| 2025 | 1.00 | 2025-05-13 | 2025-05-14 | Annual | 1.00 / 4,316m (RA25 p.121) — ties |
| 2024 | 0.94 | 2024-05-10 | 2024-05-14 | Annual | 0.94 / 4,125m (RA25 p.308) — ties |
| 2023 | 0.78 | 2023-05-16 | 2023-05-18 | "Semi-Annual" | 0.78 / 3,458m (RA25 p.308) — ties; CIQ frequency label wrong (one payment) |
| 2022 | 0.65 + 0.65 | 2022-05-17; 2022-11-24 | 2022-05-19; 2022-11-28 | Annual / Semi-Annual | two 0.65 payments, MXN 2,909m and 2,882m (RA24 p.315) — ties |
| 2021 | 1.00 | 2021-05-13 | 2021-05-17 | Annual | 1.00 (RA23 p.153) — ties |
| 2020 / 2019 / 2018 / 2017 / 2016 | 0.50 / 0.45 / 0.35 / 0.29 / 0.24 | – | – | Annual | not checked (pre-FY21) |

DPS and dates [sourced] CIQ, sheet 'Dividends & Splits'. Current yield 1.94% (BMV) and 2.09% (ADR) [sourced] = 1.075 / 55.41 [calc]. ADR distributions (labelled "Mex$" by CIQ) were 4.3359 in 2026 and 4.0134 in 2025 [sourced], about 4x the share DPS [calc].
- ==The CIQ 2026 DPS of 1.075 resolves the conflict flagged in [[bimbo-shareholder-returns]]==: the Jun-26 BMV filing's "1.75 per share" is inconsistent with its own MXN 4,626.7m total, while 1.075 reconciles to it [calc].
- Splits/adjustments [sourced]: 1.1:1 split (ex 2011-04-25), 20% stock dividend (1999-04-29), 1.1:1 split (1998-03-03). Not verified against filings (pre-2021).
- No primary equity issuance appears in the CIQ files; equity has only shrunk through buybacks and cancellations (see [[ciq-ownership-structure]] for share counts).

## 7. Reconciliation with company filings

| Item | CIQ | Filings | Difference |
|---|---|---|---|
| Debt + leases, 30-Jun-2026 | 187,858 principal | debt 6,299 ST + 147,361 LT = 153,660, leases 7,113 + 26,248 = 33,361; total 187,021 (2Q26 p.8) [sourced] | +837 (+0.4%) [calc] |
| Bonds + loans ex leases | 154,497 [calc] | 153,660 | +837 (CIQ principal vs carrying value) |
| Leases | 33,361 (FQ2 summary); 34,457 (Securities Summary, other date) | 33,361 (2Q26 p.8) | Debt Summary ties; Securities Summary stale |
| Net debt / EBITDA | 2.9x (incl. leases, post-IFRS 16 EBITDA) | 2.5x ex-IFRS 16 (2Q26 p.2, p.6) | basis difference, not an error |
| Feb-2026 Cebures | 7,867 @ 9.22% to 2035 + 4,133 floating to 2030 | MXN 12,000: 7,867 9-yr 9.22% + 4,133 4-yr TIIE de fondeo + 0.45% (EEFF25 p.87) | ties |
| Bimbo 25 / 25-2 | 12,762 @ 10.06% / 2,238 floating | same amounts; 25-2 at TIIE de fondeo + 0.34% (EEFF25 p.49) | ties |
| Bimbo 23L | 12,000 @ 9.24% to 2033 (Securities Summary only) | 12,000 @ 9.24%, due 20-May-2033 (EEFF25 p.49) | ties; ==missing from CIQ Debt Maturity Profile== |
| 2044 notes | USD 500m implied | USD 498m outstanding (EEFF25 p.49-50) | CIQ ≈ USD 2m (≈MXN 36m) high |
| Bimbo 23-2L (MXN 3,000, due 24-Jul-2026) and Bimbo 16 (due Sep-2026) | absent | in FY25 debt notes | consistent with maturity before the 2026-10-06 download; repayment not confirmed in a filing |
| Ratings | S&P BBB+, outlook Negative | S&P/Fitch BBB+, Moody's Baa1; outlooks not given (RA25 p.82) | CIQ adds outlook; lacks Fitch/Moody's |

- Bond sum check: deduplicated bonds ≈ 131,654 [calc] vs CIQ "Senior bonds and notes" 131,002 [sourced] → 653 gap (0.5%), consistent with the 2044 notes at USD 498m and FX-date differences.

> [!question] Open items
> (1) Confirm repayment of Bimbo 23-2L (Jul-2026) and Bimbo 16 (Sep-2026) in the 3Q26 filing. (2) Obtain the S&P research update behind the Mar-2025 negative outlook and current Fitch/Moody's outlooks. (3) Identify the ~7.8bn of loans in the CIQ revolver/term totals not itemised by CIQ.

## Key Takeaways
- Bonds outstanding ≈ MXN 131.7bn across 13 issues [calc]: six peso Cebures (MXN 49.0bn) and seven USD notes (USD 4.6bn), maturities 2027–2051; 144A/Reg S duplicates must be removed before summing.
- CIQ total debt 189.7bn includes 33.4bn leases; it ties to the 2Q26 balance sheet within 0.4%. CIQ net debt/EBITDA (2.9x) and company net debt/EBITDA (2.5x) differ by basis (leases and IFRS 16).
- ==S&P BBB+ carries a Negative outlook since 2025-03-20 per CIQ== — not disclosed in the filings.
- The 5Y CDS series has a pricing-method break (Composite ~150bp vs Evaluated ~50bp); the latest evaluated 5Y is 54.9bp (2026-10-05).
- CIQ DPS history ties to filings for 2021–2025; the CIQ 2026 DPS of 1.075 reconciles the MXN 4,626.7m declared and corrects the filing's "1.75".
- Long-dated USD notes (2044–2051) trade at 67–82% of par, so market and book debt diverge materially.
