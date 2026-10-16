---
Writer: AI-compiled (Claude)
Source:
  - filings/refinitiv/Debt & Credit/Debt/Issuer Ratings/IssuerRatings_Grupo Bimbo SAB de CV_Sat Oct 10 2026_T22_21_45.xls
  - filings/refinitiv/Debt & Credit/Debt/Debt and Estructure/GRUPO_BIMBO_SAB_DE_CV_10-Oct-2026_221859.xlsx
  - filings/refinitiv/Debt & Credit/Debt/Exchangables & CNV/EXCHANGEABLES AND CNVS.xlsx
  - filings/refinitiv/Debt & Credit/Credit/CDS overview/CDSOverview.xlsx
  - filings/refinitiv/Debt & Credit/Credit/Smart Ratios credit Risk/SmartRatiosModel.xlsx
  - filings/refinitiv/Debt & Credit/Credit/Structural Credit Risk/SM_Export_10_10_2026_22-30-26.xlsx
  - filings/refinitiv/Debt & Credit/Credit/Text Mining Credit Risk/CM_Export_10_10_2026_22-29-36.xlsx
  - filings/refinitiv/Filings/Receipt Date - 2026-Jul-24 - BIMBOA.MX - Grupo Bimbo SAB de CV - Half Year Presentation - gb investor ppt 2q26 vf 0 pdf - cr22276039.pdf
  - filings/refinitiv/Filings/Receipt Date - 2026-Feb-26 - BIMBOA.MX - Grupo Bimbo SAB de CV - Full Year Presentation - Q4 2025 presentation - cr21198567.pdf
  - filings/refinitiv/Filings/Receipt Date - 2026-Apr-30 - BIMBOA.MX - Grupo Bimbo SAB de CV - Quarterly Presentation - first quarter investor presentation - cr21571676.pdf
  - filings/refinitiv/Filings/Receipt Date - 2025-Mar-03 - BIMBOA.MX - Grupo Bimbo SAB de CV - Full Year Presentation - Grupo Bimbo Sab De Cv_investor Presentation - cr19693117.pdf
tags: [Valuation, credit-risk]
---

# Grupo Bimbo — credit risk per LSEG (ratings, model scores, debt structure) and reconciliation

LSEG (Refinitiv) credit and debt exports dated **2026-10-10** (21:18-22:30 local). Reconciled to [[ciq-debt-stack-and-maturity-ladder]] (instrument-level view at 30-Jun-2026), [[bimbo-capital-structure-and-debt]] (filing view) and [[ciq-corporate-issuance-history]] (CIQ bond-level market data). Currency: the LSEG debt workbook is in MXN and converts USD notes at **about MXN 18.39 per USD** [calc: 16,551 / 900 for the 2029 notes; also 239,593 / 13,028.4 for market cap in [[bimbo-ownership-lseg]]], not the 17.47 of 30-Jun-2026.

**Citation key.** `IR` = Issuer Ratings workbook (the file has an `.xls` extension but is Excel 2007+ format; some readers fail on it, see gaps). `DS-Sum` / `DS-Bonds` / `DS-Loans` = Debt Structure workbook, sheets 'Summary', 'Bonds', 'Loans'. `SR` = SmartRatiosModel, sheet 'SmartRatios Credit Risk'. `SM` = Structural Credit Risk export, sheet 'SM Export'. `CM` = "Text Mining Credit Risk" folder export, sheet 'CM Export' (**its content is the Combined Credit Risk model**, not a standalone text-mining score). `CDS` = CDSOverview, sheet 'GRUPO BIMBO A ORD'. `2Q26-p` / `4Q25-p` / `1Q26-p` = company investor presentations (cr22276039, cr21198567, cr21571676), PDF page.

## 1. Issuer ratings (IR, 2026-10-10)

| Agency / scale | Rating | Rating date | Outlook | Outlook date | Last affirmed |
|---|---|---|---|---|---|
| S&P long-term issuer, foreign and domestic | BBB+ | 2023-03-29 | **NEGATIVE** | 2025-03-20 | 2025-03-24 |
| S&P senior unsecured (foreign) | BBB+ | 2023-03-29 | n/a | n/a | 2025-03-24 |
| S&P national scale long-term | mxAAA | 2023-03-29 | Stable | 2023-03-29 | 2025-03-24 |
| S&P national scale short-term | mxA-1+ | 2024-12-06 | n/a | n/a | 2025-03-24 |
| Moody's long-term issuer / senior unsecured (foreign) | Baa1 | 2023-04-21 | Stable (derived rating, STA) | 2024-11-15 | 2024-11-15 |
| Fitch long-term IDR (foreign and domestic) | BBB+ | 2023-03-31 | Stable | 2026-07-29 | 2026-07-29 |
| Fitch senior unsecured (foreign) | BBB+ | 2023-03-31 | n/a | n/a | 2026-07-29 |
| Fitch national scale long-term / short-term | AAA(mex) / F1+(mex) | 2020-06-03 / 2024-12-06 | Stable | 2026-07-29 | 2026-07-29 |

All [sourced] IR. History visible in the file [sourced] IR: Fitch IDR BBB (2010-06-11) to BBB+ (2023-03-31); Fitch national AA(mex) (2009), AA+(mex) (2010), AAA(mex) (2002 and again 2020); Moody's Baa2 (2001), Baa1 (2006), Baa2 (2009), Baa1 (2023); Moody's national-scale ratings withdrawn 2017. LSEG states "You are not permissioned to export historical S&P ratings", so S&P history is not available.

- **Fills a known gap.** [[bimbo-valuation-data-gaps]] item 12 and [[bimbo-capital-structure-and-debt]] say outlooks are "not disclosed". LSEG gives **Fitch stable (affirmed 29-Jul-2026), Moody's stable (15-Nov-2024)** and corroborates the **S&P negative outlook since 20-Mar-2025** that [[ciq-corporate-issuance-history]] had found only in CIQ.
- The S&P negative outlook is ==about 19 months old at the export date== [calc: 2025-03-20 to 2026-10-10] with no later action visible; Bimbo's own decks present "Baa1 / BBB+ / BBB+" without outlooks [sourced] 2Q26-p3. Net debt / EBITDA fell from 2.9x (Dec-24) to 2.5x (Jun-26) over the same period [sourced] 4Q24 deck p.3 (via [[bimbo-investor-presentations-2024-2026]]); 2Q26-p3.
- National-scale ratings (mxAAA, AAA(mex)) are top-of-scale and not comparable with the global scale; Mexican CB investors price off them.
- Exchangeable and convertible bonds: none found for the issuer or subsidiaries (both equity of the company and of other companies) [sourced] EXCHANGEABLES AND CNVS.xlsx. No equity-linked dilution risk from the debt stack.
- CDS: **no data**. Markit entity GRUPO BIMBO, SOCIEDAD ANONIMA BURSATIL DE CAPITAL VARIABLE, ticker GRBICV, RED code PTDDDK, "No end of day pricing data available", no intraday pricing, no reference-obligation information, not an index constituent [sourced] CDS. Bimbo CDS levels cannot be quoted from this source; use the bond OAS in section 4 as the market-implied spread proxy.

## 2. LSEG credit-model scores (2026-10-10)

Scores are 1-100 percentile-style ranks within the LSEG emerging-markets universe (higher = lower risk); the model-implied rating and probability of default (PD) are LSEG outputs, not agency ratings.

| Model | Bimbo score | Implied rating | PD | Components (score) |
|---|---|---|---|---|
| **Combined** (CM) | **16** | **BBB-** | **0.16%** | Structural 53; SmartRatios 9; Text mining 70 |
| Structural (SM) | 53 | A- | 0.03% | Structural leverage 15; asset volatility 84; asset drift 39 |
| SmartRatios (SR) | 9 | BB | 0.90% (0.8956) | Profitability 28; Leverage 7; Coverage 29; Liquidity 9; Growth and stability 52 |
| Text mining (inside CM) | 70 | n/a | n/a | Transcripts 88; Reuters news 58; Filings N/A; Research 44 |

All [sourced] CM, SM, SR; agency reference rows show S&P BBB+ and Moody's Baa1.

- ==The combined model implies BBB-, two notches below the agencies' BBB+== [calc: BBB+ to BBB to BBB-]. The driver is the SmartRatios block (score 9, implied BB), led by **Leverage 7 and Liquidity 9**; the market-based structural model alone implies A- (PD 0.03%) [sourced] SM.
- **Structural model inputs** [sourced] SM: asset level MXN 210,427.6m; asset minus debt 177,539.6m, which implies a debt barrier of MXN 32,888.0m [calc: 210,427.6 − 177,539.6]; structural leverage 0.2 (value); asset volatility 20.6%; asset drift −5.2%. Sensitivity: assets +41.1% = 296,952.7; +20.6% = 253,690.1; −20.6% = 167,165.1; −41.1% = 123,902.6 (asset minus debt 91,014.6, still positive).
- **SmartRatios inputs** [sourced] SR (TTM / NTM where given): return on tangible capital 7.3% / 7.8%; net profit margin 3.0% / 3.1%; equity / assets 0.31 / 0.33; net debt / equity 1.13 / 0.97; underfunded pension / equity 0.05; intangibles / assets 31.8 (%); EBIT / interest 2.49 / 2.55; EBITDA / interest 4.22 / 4.36; free cash flow / debt 0.13 / 0.10; cash / total debt 0.09; short-term debt / total debt 7.17 (read as %, field label has no unit); quick ratio 0.65 (change −0.04); stabilised ROE growth −0.64; EPS standard deviation 0.91; revenue standard deviation 0.06.
- Cross-checks to filing-based ratios: EBITDA / interest 4.22x vs 4.1x for FY25 in [[bimbo-balance-sheet-and-leverage]] and 4.14x in [[ciq-key-ratios-and-performance]] (consistent); net debt / equity 1.13 (LSEG TTM) vs 1.18x at Jun-26 in [[bimbo-balance-sheet-and-leverage]] (LSEG basis differs in debt definition `[unverified]`).

### Peer comparison (CM, SM, SR; same export)

| Company | Combined score | PD | Implied rating | S&P / Moody's | Structural | SmartRatios | Text mining |
|---|---|---|---|---|---|---|---|
| **Grupo Bimbo** | 16 | 0.16% | BBB- | BBB+ / Baa1 | 53 | 9 | 70 |
| Arca Continental | 94 | 0.02% | AA | -- / -- | 91 | 58 | 82 |
| Coca-Cola FEMSA | 83 | 0.03% | AA- | A- / WR | 80 | 54 | 57 |
| Gruma | 68 | 0.05% | A+ | BBB+ / WR | 80 | 30 | 95 |
| Becle (Cuervo) | 67 | 0.05% | A+ | BBB- / -- | 55 | 30 | 79 |
| Chedraui | 67 | 0.05% | A+ | -- / -- | 66 | 27 | 75 |
| Sigma Foods | 15 | 0.17% | BBB- | BBB / -- | 68 | 6 | 62 |
| Embotelladora Andina | 14 | 0.17% | BBB- | NR / -- | N/A | N/A | 63 |
| Peer average (as printed) | 53 | 0.09% | BBB+ | "B+ / Ca" (artefact) | 62 | 27 | 73 |

[sourced] CM; the structural-model peer table adds Bimbo asset volatility 84 vs Arca 91, Gruma 90, Sigma 86, KOF 89, Chedraui 91 and structural leverage score 15 vs Arca 34, Gruma 28, Sigma 14, KOF 18, Chedraui 19 [sourced] SM. The printed peer-average agency cell "B+ / Ca" is an export artefact and should not be quoted.

- Only Bimbo, Sigma Foods and Embotelladora Andina sit at BBB- (combined score 14-16); Arca, Coca-Cola FEMSA, Gruma, Becle and Chedraui rank at 67-94. The SmartRatios gap versus Arca (9 vs 58) is mostly leverage (7 vs 21) and liquidity (9 vs 46) [sourced] SR.

## 3. Debt structure (DS, 2026-10-10)

| Instrument bucket | Issues | Outstanding (MXN m) | Issued (MXN m) | Source |
|---|---|---|---|---|
| Bonds | 23 | 133,616.1 | 135,800.8 | DS-Sum |
| Loans (committed facilities) | 2 facility groups, 3 facilities | not stated | 48,211.9 | DS-Sum, DS-Loans |
| Total | 25 | 133,616.1 | 184,012.7 | DS-Sum |
| Inactive bonds | 21 | n/a | 100,463.8 | DS-Sum |

The 23 "bonds" are 15 distinct issues: the seven USD notes and the Fargo item appear twice (144A and Regulation S lines, flagged "Asset Duplicated"), and Fargo and Wickbold are data artefacts (see section 5) [calc from DS-Bonds].

### 3a. Bond table with LSEG market data (priced lines only)

USD amounts are MXN / 18.39 [calc]. "Company outstanding" is the Jun-26 amount in [[ciq-debt-stack-and-maturity-ladder]] (USD notes ties to EEFF25 p.47-48; MXN to the company table).

| Bond | Maturity | LSEG outstanding (MXN m) | Implied USD m [calc] | Company outstanding | Price | Yield | OAS (bp) | Mod. duration |
|---|---|---|---|---|---|---|---|---|
| 6.05% USD 2029 | 2029-01-15 | 16,551.0 | 900.0 | USD 900 | 100.67 | 5.73% | 85.1 | 2.05 |
| 6.40% USD 2034 | 2034-01-15 | 10,114.5 | 550.0 | USD 550 | 101.54 | 6.13% | 97.1 | 5.67 |
| 5.375% USD 2036 | 2036-01-09 | 14,712.0 | 800.0 | USD 800 | 93.58 | 6.30% | 107.4 | 7.00 |
| 4.875% USD 2044 | 2044-06-27 | 9,195.0 | 500.0 | USD 497.5 | 82.75 | 6.53% | 95.2 | 10.88 |
| 4.70% USD 2047 | 2047-11-10 | 11,953.5 | 650.0 | USD 650 | 77.76 | 6.68% | 102.9 | 11.79 |
| 4.00% USD 2049 | 2049-09-06 | 11,034.0 | 600.0 | USD 560 | 68.49 | 6.71% | 105.6 | 12.91 |
| 4.00% USD 2051 | 2051-05-17 | 11,034.0 | 600.0 | USD 585.3 | 67.53 | 6.72% | 107.4 | 13.04 |
| Bimbo 17, 8.18% MXN | 2027-09-24 | 10,000.0 | n/a | MXN 9,633.1 | 101.43 | 7.03% | 22.7 | 0.90 |
| Bimbo 23L, 9.24% MXN | 2033-05-20 | 12,000.0 | n/a | MXN 12,000.0 | 99.87 | 9.26% | −29.6 | 4.69 |

[sourced] DS-Bonds (144A line shown; Regulation S lines differ by 0.02-0.04 pt of price). Yield "event" is maturity for all; the pricing date is not stated (export timestamp 2026-10-10, a Saturday, so prices are presumably from the prior session `[unverified]`).

- Unpriced lines (zero fields): Bimbo 25-2 FRN 2028 (2,238.0), Bimbo 26-2 FRN 2030 (4,133.4), Bimbo 25 10.06% 2032 (12,762.0), Bimbo 26 9.22% 2035 (7,866.6) [sourced] DS-Bonds. The February 2025 pair sums to MXN 15,000m and the February 2026 pair to MXN 12,000m [calc], matching the issuance announced in the 4Q24 deck p.15 and 4Q25 deck p.3 ([[bimbo-investor-presentations-2024-2026]]).
- ==USD curve:== OAS rises from 85 bp (2029) to 107 bp (2036 and 2051) with a flat 95-107 bp band beyond 2034; all long USD bonds trade at deep discounts (67.5-82.8) because of 4.0-4.9% coupons [sourced] DS-Bonds. Yield-to-maturity 5.7-6.7%.
- The negative OAS on the 2033 MXN CB (−29.6 bp) and +22.7 bp on the 2027 CB are against LSEG's own MXN benchmark curve and mix instruments of different convexity; treat as indicative `[unverified]`.

### 3b. Facilities (DS-Loans)

| Facility | Amount (MXN m) | Maturity (LSEG) | Filings |
|---|---|---|---|
| Revolver/line, working capital (BBVA) | 5,000.0 | 2028-04-13 | Ties (13-Apr-2028) per [[bimbo-capital-structure-and-debt]] |
| Syndicated revolver, USD, Tranche B | 19,419.8 (USD 1,056 [calc]) | **2028-08-19** | **Filings: 15-Mar-2028** per [[bimbo-capital-structure-and-debt]] |
| Syndicated revolver, USD, Tranche A | 23,792.1 (USD 1,294 [calc]) | 2030-07-31 | Ties |
| Total | 48,211.9 | | USD 2,350m syndicated undrawn plus BBVA |

[sourced] DS-Loans; issue date 2025-07-31 for the syndicated pair. The Tranche B maturity differs by five months from the company filings (LSEG 19-Aug-2028 vs 15-Mar-2028) and no extension is described in the sources reviewed `[unverified]`.

## 4. Reconciliation with existing debt articles

| Item | LSEG (10-Oct-2026) | CIQ / company (30-Jun-2026) | Difference | Reading |
|---|---|---|---|---|
| USD notes, USD m | 4,600 [calc] | 4,542.8 [[ciq-debt-stack-and-maturity-ladder]] | +57.2 [calc] | LSEG carries 2044 at 500 (vs 497.5), 2049 at 600 (vs 560), 2051 at 600 (vs 585.3): **original issue size, not outstanding after repurchases** |
| MXN CBs, MXN m | 49,000.0 (excl. matured 23-2L) | 48,633.1 (51,639.1 less 3,006.0 maturing 24-Jul-2026) | +366.9 | Bimbo 17: LSEG 10,000 vs 9,633.1; the company slide shows USD 551m of MXN bonds in 2027, equal to MXN 9,633m at 17.47 [calc] [sourced] 2Q26-p17 |
| Maturity of Bimbo 23-2L (24-Jul-2026) | absent | 3,006.0 included at Jun-26 | n/a | LSEG correctly drops it after maturity |
| Bank loans drawn | not listed (facility sizes only) | 23,495.1 [[ciq-debt-stack-and-maturity-ladder]] | LSEG omits bilateral term loans and lines (Citi, BofA, HSBC, BNP Paribas, Rabobank, CaixaBank) | LSEG is a **bond and big-facility** view, not a full debt stack |
| Revolver Tranche B maturity | 2028-08-19 | 2028-03-15 | +5 months | see 3b |
| USD/MXN used | ~18.39 | 17.47 | +5.3% [calc] | LSEG values USD notes at export-date FX; the MXN had weakened since 30-Jun-2026 if both are right `[unverified]` |

- **Company cross-check of the debt profile** [sourced] 2Q26-p17: total debt USD 8,796m (net of issuance costs, at 17.47), average tenor 9.5 years, average cost 6.5% (including derivatives, withholding tax and costs), 82% fixed / 18% floating, currency mix after derivatives USD 42% / MXN 42% / EUR 12% / CAD 3% / GBP 1%, undrawn committed revolver USD 2.35bn; subsidiary-level long-term debt of USD 110m is excluded. The maturity bars on that slide (USD m, bonds + bank loans, labelled sums) are 2026 253; 2027 658; 2028 833; 2029 1,081; 2030 396; 2032 731; 2033 687; 2034 550; 2035 450; 2036 800; 2044 498; 2047 650; 2049 560; 2051 585 [calc sums of the labelled segments], about USD 8.73bn vs the USD 8,796m headline (a USD 64m gap, labelled-segment rounding or omitted small items `[unverified]`).
- Time series of the company's own debt profile (Dec-23 to Jun-26) is in [[bimbo-investor-presentations-2024-2026]]: total debt USD 6.5bn to 8.8bn, tenor 12.1 to 9.5 years, average cost 7.12% to 6.5%.
- The 2Q26 deck puts net debt / adjusted EBITDA (ex-IFRS 16) at 2.5x vs 2.7x at Dec-25 and 2.9x at Dec-24 [sourced] 2Q26-p16, 4Q25-p3, 4Q24 deck p.3.

## 5. Data-quality items in the LSEG debt file

- Fargo (Compañia de Alimentos Fargo, Argentina) 13.25% 2008 notes, flagged "In Default", appear with MXN 22.1m "outstanding" (MXN 2,206.8m issued): a legacy item from an acquired company, not a live exposure `[unverified]` [sourced] DS-Bonds row "2008".
- Wickbold & Nosso Pao FRN 2031 (Brazilian real, 16.146%, issued 2024-06-25) is shown at an amount of 3,688 (units unclear); it is a subsidiary commercial-paper line from the 2025 Wickbold acquisition [sourced] DS-Bonds; per [[bimbo-acquisitions]] `[unverified]` link.
- 21 "inactive bonds" with MXN 100.5bn issued [sourced] DS-Sum are historical.
- `IssuerRatings...xls` is an OOXML file mislabelled `.xls`; `xlrd`-style readers fail on it.

## Connections

- [[ciq-debt-stack-and-maturity-ladder]] and [[bimbo-capital-structure-and-debt]]: LSEG matches maturities and instrument counts for bonds; it **overstates** three USD notes and Bimbo 17 (pre-buyback amounts) and **lags** one revolver date. Use filing/CIQ amounts for modelling.
- [[ciq-corporate-issuance-history]]: S&P negative outlook now confirmed by a second source; Fitch and Moody's outlooks stable.
- [[bimbo-valuation-data-gaps]]: item 12 (outlooks) can be closed with this article; item on CDS remains open (no data).
- [[bimbo-balance-sheet-and-leverage]], [[bimbo-sustainable-financing]], [[bimbo-investor-presentations-2024-2026]].

## Key Takeaways

- Agency view: BBB+ / BBB+ / Baa1 with **S&P negative (Mar-2025)**, Fitch stable (Jul-2026) and Moody's stable (Nov-2024) [sourced] IR; no convertibles or exchangeables; **no CDS data** in LSEG.
- LSEG's own combined model implies **BBB- (PD 0.16%)**, two notches below the agencies, because SmartRatios (leverage 7, liquidity 9) outweighs a structural model that implies A- [sourced] CM, SM, SR.
- Among seven Mexican/LatAm peers Bimbo ranks near the bottom with Sigma Foods and Andina; Arca (94) and Coca-Cola FEMSA (83) are the credit-quality benchmark [sourced] CM.
- USD bonds trade 85-107 bp over LSEG's benchmark with yields of 5.7-6.7%; the 2049/2051 notes sit near 68 [sourced] DS-Bonds.
- LSEG's debt table is not model-grade: it carries issue-size amounts for three USD notes and Bimbo 17, omits bilateral loans and dates revolver Tranche B five months later than the filings.
- The company's own profile (2Q26): USD 8.8bn debt, 9.5-year tenor, 6.5% cost, 82% fixed, net leverage 2.5x [sourced] 2Q26-p17, p16.
