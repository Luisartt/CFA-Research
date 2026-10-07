---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/OwnerShip/OwnerShip Summary/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipSummary(Summary)_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/OwnerShip Detailed/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipDetailed_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/OwnerShip History/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipHistory_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/OwnerShip CrossHoldings/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipCrossholdings_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Securities Summary/SPGlobal_GrupoBimbo,S.A.B.deC.V._SecuritiesSummary_06-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/Corporate Issuance/Equity Listing/SPGlobal_GrupoBimbo,S.A.B.deC.V._EquityListings_06-Oct-2026.xlsx
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/bmv/GB_RA_2024_BMV_VFF1_0.pdf
  - filings/bmv/Reporte Anual 2023_XBRL_VF.PDF
  - filings/bmv/Reporte Anual 2022 VF.pdf
  - filings/bmv/Reporte Anual 2021_0.pdf
  - filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Jun_26.pdf
tags: [Company, ownership]
---

# Grupo Bimbo — Ownership Structure (Capital IQ view, reconciled to filings)

S&P Capital IQ (CIQ) ownership exports downloaded **2026-10-06**, priced at the BMV close of **MXN 55.41** (2026-10-06). Holder positions carry their own filing dates (2025-05 to 2026-10). Tidy data: `data/capitaliq/ownership_summary.csv`, `ownership_detailed.csv`, `ownership_history.csv`, `cross_holdings.csv`. Related: [[bimbo-governance-and-ownership]] (filing-based view), [[bimbo-shareholder-returns]], [[ciq-corporate-issuance-history]], [[ciq-public-holdings-and-investments]].

> [!warning] CIQ misses the controlling shareholders
> CIQ classifies **94.51%** of shares as "Public and Other" and reports **0 shares excluded from float** (float shown as 100%). The company's share register shows six family-linked holding companies with **72.03%** (RA25 p.181). CIQ float and "public" figures must not be used for liquidity, index-weight or free-float market-cap work. Use the filing-based float below.

## 1. Headline split (CIQ, as of 2026-10-06)

| Owner type | Shares | % of shares out | Market value (MXN m) | Source |
|---|---|---|---|---|
| Institutions | 236,048,640 [sourced] | 5.49 [sourced] | 13,079 [sourced] | CIQ OwnershipSummary, sheet 'Summary' |
| Public and Other | 4,060,235,575 [sourced] | 94.51 [sourced] | 224,978 [sourced] | same |
| **Total** | **4,296,284,215** [sourced] | 100 | **238,057** [sourced] | same |
| Individuals / insiders | "No data" [sourced] | – | – | sheet 'Ownership Activity' |
| Other strategic holders | "No data" [sourced] | – | – | sheet 'Ownership Activity' |

- CIQ shares outstanding (4,296,284,215) tie **exactly** to "Total en circulación" at 30-Jun-2026 in the BMV 2Q26 filing (BMV Jun-26 p.96) [sourced]: 4,304,744,119 Series A shares less 8,459,904 treasury shares.
- Market cap 238,057 = 4,296,284,215 × 55.41 [calc] (CIQ SecuritiesSummary, sheet 'Securities Summary').

## 2. Controlling shareholders (company share register — not in CIQ)

Register as of 30-Apr-2026 (RA25 p.181) [sourced]; percentages on 4,304,744,119 authorized Series A shares.

| Holder | Shares | % (RA25) | % of CIQ shares out [calc] |
|---|---|---|---|
| Normaciel, S.A.P.I. de C.V. | 1,763,123,500 | 40.96 | 41.04 |
| Promociones Monser, S. de R.L. de C.V. | 550,268,544 | 12.78 | 12.81 |
| Philae, S.A. de C.V. | 232,692,104 | 5.41 | 5.42 |
| Grupo Valacci, S.A. de C.V. | 221,593,708 | 5.15 | 5.16 |
| Banco Nacional de México, S.A. (as trustee) | 171,869,396 | 3.99 | 4.00 |
| Marlupag, S.A. de C.V. | 161,213,536 | 3.75 | 3.75 |
| **Total** | **3,100,760,788** | **72.03** | **72.17** |

- The PDF text layer scrambles this table; the share counts and percentages above were matched by recomputation (each count / 4,304,744,119 reproduces the printed %) [calc].
- Normaciel "exercises significant influence"; Daniel Javier Servitje Montull (Executive Chairman) "could be considered to have power of command" (RA25 p.181) [sourced].
- RA25 adds that certain directors and officers individually hold >1% and <10%, held through trusts or holding companies, restricted and not freely disposable (RA25 p.181) [sourced]. RA23 and RA22 said no director held 1-10% individually (RA23 p.216; RA22 p.177) [sourced] — wording changed in RA24/RA25.

## 3. Filing-based free float [calc]

| Item | Value | Basis |
|---|---|---|
| Shares outstanding 30-Jun-2026 | 4,296,284,215 | BMV Jun-26 p.96 [sourced] |
| Controlling group | 3,100,760,788 | RA25 p.181 [sourced] |
| Implied free float shares | ==1,195,523,427== | [calc] difference |
| Implied free float % | ==27.8%== | [calc] 1,195.5m / 4,296.3m |
| Free-float market value | ≈ MXN 66.2bn | [calc] 1,195.5m × 55.41 |
| Institutions as % of free float | ≈ 19.7% | [calc] 236.0m / 1,195.5m |
| BlackRock as % of free float | ≈ 8.7% | [calc] 104.1m / 1,195.5m |

- Upper bound: directors' individual 1-10% stakes (restricted, amounts not disclosed) would reduce the true float further [unverified size].
- The ~72% stake has been unchanged in share count since at least Apr-2023 (3,100,760,788 shares in RA22, RA23, RA24, RA25); the % rose only because buybacks cut the share base: 69.3% (Apr-2023, RA22 p.177) → 70.7% (Apr-2024, RA23 p.216) → 71.6% (Apr-2025, RA24 p.180) → 72.03% (Apr-2026, RA25 p.181) [sourced].
- Apr-2022 register (RA21 p.171-172) listed Normaciel with 1,756,513,140 shares and a seventh holder, Sendamos, S.A.P.I. de C.V. (150,000,000; 3.4%), total 3,244,150,428 [sourced]. The table prints 72.5% while the text says "approximately 71.5%"; 3,244,150,428 / 4,516,329,661 = 71.8% [calc] — internal inconsistency in RA21.

## 4. Top institutional holders (CIQ, latest filings)

| # | Holder | Shares | % CSO | Position date | Change in shares | Style / orientation |
|---|---|---|---|---|---|---|
| 1 | BlackRock Inc. | 104,120,971 | 2.42 | 2026-09-30 | +238,701 | Passive |
| 2 | Vanguard Capital Management LLC | 50,654,024 | 1.18 | 2026-08-31 | +163,900 | n/a |
| 3 | Dimensional Fund Advisors LP | 11,755,209 | 0.27 | 2026-08-31 | +496,544 | Active |
| 4 | Geode Capital Management LLC | 6,721,307 | 0.16 | 2026-07-31 | +187,396 | Passive |
| 5 | Charles Schwab Investment Management | 5,233,843 | 0.12 | 2026-08-31 | +150,554 | Passive |
| 6 | Deutsche Asset & Wealth Management | 5,018,549 | 0.12 | 2026-06-30 | 0 | Active |
| 7 | State Street Investment Management | 4,424,954 | 0.10 | 2026-09-30 | +32,209 | Passive |
| 8 | GAMCO Investors Inc. (flagged activist) | 4,190,000 | 0.10 | 2026-06-30 | −14,000 | Active |
| 9 | UBS Asset Management AG | 4,118,618 | 0.10 | 2026-07-31 | 0 | Active |
| 10 | Amundi Asset Management SAS | 3,825,490 | 0.09 | 2026-08-31 | +61,707 | Active |

All [sourced] CIQ OwnershipDetailed, sheet 'Ownership Detailed' (97 holder rows, 3 with zero shares). Top-10 = 200.1m shares, 4.66% of shares out [calc].

- Activist flags: GAMCO and Royal London Asset Management (1,380,241 sh; 0.03%) are tagged "Institution is an Activist? = Yes" [sourced]; both are tiny relative to the 72% controlling block.
- Top mutual funds (sheet 'Top Mutual Fund Holders') [sourced]: iShares NAFTRAC 39,019,798 (0.91%); Vanguard Total International Stock ETF 17,381,900 (0.40%); Vanguard FTSE Emerging Markets ETF 16,618,943 (0.39%); iShares Core MSCI EM ETF 14,806,535 (0.34%); iShares MSCI Mexico ETF 9,581,567 (0.22%). ==Index/passive vehicles dominate== the visible institutional base.

## 5. Institutional mix (CIQ sheets 'Inst. Owner Type', 'Country', 'Turnover', 'Style')

| Cut | Detail [sourced] |
|---|---|
| Owner type | Traditional investment managers 228.8m sh (96.9% of institutional; 87 holders); government pension sponsors 5.96m (2.5%; 4); insurance 1.06m; sovereign wealth 0.17m (NBIM); family office 0.09m; hedge funds 9,067 sh |
| Country | USA 38 holders, 199.2m sh, 4.64% CSO; UK 9 holders, 0.22%; Switzerland 0.11%; France 0.10%; **Mexico 5 holders, 4.43m sh, 0.10%** |
| Turnover | Very low 163.3m sh (69.2% of inst.); low 21.0m (8.9%); moderate 1.1m; unclassified 50.7m (21.5%, mainly Vanguard) |
| Style | Growth 99.7% of institutional shares (CIQ "calculated" style, not a stated mandate) |

- Mexican institutions (Afores, local funds) are almost absent from the CIQ view: 0.10% of shares [sourced]. CIQ coverage relies on 13F and mutual-fund filings; Mexican pension (Afore) holdings are likely under-captured [unverified].

## 6. Change over time (CIQ OwnershipHistory, 31-Dec-2025 vs latest)

| Holder | 31-Dec-2025 | Latest | Change [calc] |
|---|---|---|---|
| BlackRock | 102,522,272 | 104,120,971 | +1.6% |
| Dimensional | 8,856,891 | 11,755,209 | +32.7% |
| Vanguard Group Inc. → Vanguard Capital Management LLC | 52,622,073 | 50,654,024 | −3.7% (entity relabelled; compare with care) |
| Canada Pension Plan IB | 3,925,000 | 2,244,000 | −42.8% |
| Impulsora de Fondos Banamex | 5,857,037 | 19,626 | −99.7% |
| Sum of all listed holders | 237,508,121 | 236,048,640 | −0.6% |

All levels [sourced] CIQ OwnershipHistory, sheet 'Ownership History'; changes [calc].

- On a 31-Dec-2025 base of 4,304,744,119 shares outstanding (BMV Jun-26 p.96), institutional ownership was ≈5.52% [calc: 237.5m / 4,304.7m] vs 5.49% now — ==essentially flat==.
- Quarterly activity, 31-Mar-2026 to 30-Jun-2026 (sheet 'Ownership Activity') [sourced]: 96 positions, 234,500,224 sh; 3 new (294,953 sh), 19 increased (+2,678,548), 20 decreased (−10,066,904), 2 sold out (−46,157). Net ≈ −7.1m sh [calc].
- Top buyers (latest): Dimensional +496,544; American Century +265,169; BlackRock +238,701; Geode +187,396; BMO +184,900. Top sellers: Impulsora del Fondo Mexico −315,448; Sura AGF (Chile) −37,973 (exited); Banamex funds −36,704; Security AGF −36,359 (exited); Manulife −26,200 [sourced] sheet 'Top Buyers and Sellers'.

## 7. Listings (CIQ EquityListings, 2026-10-06)

| Line | Security | Last price | 52-wk range | Avg daily volume (3M) |
|---|---|---|---|---|
| BMV:BIMBO A (primary) | Series A | MXN 55.41 | 53.03–68.67 | 2,122,250 sh |
| OTCQX:BMBO.Y | Level 1 ADR | USD 215.26 (2026-10-01) | 214.54–284.26 | 840 |
| OTCQX:GRBM.F | Series A | USD 56.78 (2026-09-29) | 53.19–71.87 | 616 |
| DB:4GM / DB:4GM0 | Series A / ADR | EUR 53.84 / 214.56 | – | 33 / 0 |

All [sourced]. The ADR programme is Level 1 under ticker BMBOY (RA25 p.205) [sourced]. ADR ratio is not stated in the CIQ files; ADR dividend 4.3359 vs share dividend 1.075 implies about 4 shares per ADR [calc; unverified].
- Daily BMV turnover ≈ 2.12m sh × 55.41 ≈ MXN 118m [calc], ≈ 0.18% of free-float shares per day [calc].

## 8. Reconciliation with filings

| Item | CIQ | Filings | Difference |
|---|---|---|---|
| Shares outstanding | 4,296,284,215 (Securities Summary) | 4,296,284,215 at 30-Jun-2026 (BMV Jun-26 p.96) | none |
| Shares excluded from float | 0 | 3,100,760,788 controlling block (RA25 p.181) | ==CIQ omits 72% strategic stake== |
| Insiders / strategic holders | none listed | six holding companies + restricted director stakes | CIQ gap |
| Institutional % | 5.49% | not disclosed in filings | n/a |
| Dividend yield | 1.94% | 1.075 / 55.41 = 1.94% [calc] | ties |

- [[bimbo-governance-and-ownership]] was not yet written when this article was compiled; check its holder table against section 2 once available.

> [!question] Open items
> (1) Size of the directors' restricted 1-10% stakes (RA25 p.181) — not quantified in filings. (2) Afore holdings: obtain from CONSAR/BMV or a broker note. (3) Who is behind Sendamos (in the 2022 register, absent from 2023 onward)?

## Key Takeaways
- CIQ says 94.5% "public" and 100% float; the share register says ==72.03% sits with six Servitje-family-linked holding companies== (RA25 p.181). Use a filing-based float of ~27.8% [calc].
- Institutions hold only 5.49% of shares (≈19.7% of the real float), led by passive index money: BlackRock 2.42%, Vanguard 1.18%, iShares NAFTRAC 0.91%.
- Visible institutional ownership was flat from Dec-2025 to Oct-2026 (−0.6% in shares); Dimensional added, CPPIB and Banamex funds cut.
- The controlling block has held 3,100,760,788 shares since 2023; its percentage rises mechanically with buybacks (69.3% → 72.03%).
- CIQ share count ties exactly to the 2Q26 BMV filing (4,296,284,215).
- Liquidity is thin outside the BMV line; ADR and foreign lines trade a few hundred units a day.
