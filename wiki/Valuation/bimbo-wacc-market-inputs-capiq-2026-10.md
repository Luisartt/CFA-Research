---
Writer: AI-compiled (Claude)
Source: Capital IQ AI response 3F (pasted by the team on 2026-10-17; verbatim file still to be saved in raw/ by the team); market caps from data/capitaliq/capiq-ai-prompt1_2026-10-16.md
tags: [Valuation, wacc-inputs]
---

# WACC Market Inputs — Rates, Sovereign Risk and Capital Structure (Capital IQ AI, 16-Oct-2026)

Inputs for the WACC and for unlevering peer betas. ==Levered betas, the Mexico EMBI spread and Bimbo's bond yields were not returned==, so no WACC can be built from this alone. Related: [[peer-leverage-capiq-2026-10]], [[bimbo-debt-hedging-and-leverage-target-capiq-2026-10]], [[bimbo-credit-risk-lseg]], [[bimbo-valuation-data-gaps]]. Problems: [[capiq-data-discrepancies-2026-10]].

## 1. Capital structure and tax rate (LTM, USD)

Bimbo and Arca are converted from pesos at US$0.05569 per peso (Ps. 17.96/US$) `[sourced]`. Debt includes leases. D/E here is ==book== debt over book equity.

| Company | Ticker | Period end | Total debt (US$m) | Book equity (US$m) | Book D/E | Effective tax rate | Unlever factor (book) `[calc]` |
|---|---|---|---|---|---|---|---|
| Grupo Bimbo | BMV:BIMBO A | 30-Jun-2026 | 10,855 | 6,638 | 1.635x | 35.62% | 2.053 |
| Flowers Foods | NYSE:FLO | 18-Jul-2026 | 2,008 | 1,324 | 1.517x | 30.79% | 2.050 |
| Gruma | BMV:GRUMA B | 30-Jun-2026 | 2,112 | 2,252 | 0.938x | 32.36% | 1.634 |
| Arca Continental | BMV:AC | 30-Jun-2026 | 3,644 | 9,334 | 0.390x | 31.90% | 1.266 |
| Mondelez | NASDAQGS:MDLZ | 30-Jun-2026 | 22,059 | 26,692 | 0.826x | 21.90% | 1.645 |
| PepsiCo | NASDAQGS:PEP | 5-Sep-2026 | 51,881 | 22,487 | 2.307x | 20.10% | 2.845 |

- Unlever factor = 1 + (1 − tax) × D/E (Hamada); unlevered beta = levered beta ÷ factor. The levered betas (2-year weekly, 5-year monthly, local index and S&P 500) were not returned.
- ==Book D/E distorts the factor for large caps==: with market capitalisations from [[peer-multiples-and-operations-capiq-2026-10]] the market D/E is Flowers 1.55x (2,007.8 / 1,295.7), Mondelez 0.27x (22,059 / 81,568.8) and PepsiCo 0.29x (51,881 / 179,200.5), giving factors of 2.072, 1.211 and 1.231 `[calc]`. Use market D/E for unlevering. Bimbo's market capitalisation is about US$13.65bn ([[bimbo-consensus-dashboard-capiq-2026-10]]), so its market D/E is about 0.80x and its unlever factor about 1.51 `[calc]`; Gruma and Arca have no reliable market capitalisation.
- Bimbo's lease-inclusive total debt is US$10,855m and, with cash of about US$948m, net debt US$9,907m `[calc]`, which matches the Capital IQ net debt of the earlier pull ([[peer-leverage-capiq-2026-10]]).
- Bimbo's 35.62% effective tax rate is above the Mexican statutory rate of 30% `[unverified]`. Gruma's total debt of US$2,112m is the first Gruma figure obtained.
- The identifiers `BMV:BIMBO A` and `BMV:GRUMA B` resolved correctly in this pull; the failures of the first pull came from `BMV:BIMBOA` and `BMV:GRUMAB`.

## 2. Government rates and sovereign risk

| Instrument | Value | Date |
|---|---|---|
| UST 10-year / 20-year | 5.09% / 5.48% | 2026-10-16 / 2026-10-15 |
| Mexico M-Bono 10-year / 20-year | 9.26% / 9.72% | 2026-10-16 |
| Eurozone 10-year benchmark / AAA euro-area 10-year (ECB) | 3.409% / 3.390% | 2026-10-16 / 2026-10-15 |
| Mexico 5-year CDS: mid / bid / ask | 95.30 / 94.21 / 96.38 bp | 2026-10-16 |
| Mexico 5-year CDS implied default probability | 6.72% (horizon not stated) | 2026-10-16 |
| Mexico EMBI spread | not returned | n/a |
| 10-year TIPS real yield; 3-year UDI benchmark | 2.74%; 3.72% | 2026-10-16 |

`[sourced]` S&P Capital IQ rates and CDS data.

- Derived `[calc]`: 10-year US breakeven inflation 5.09% − 2.74% = 2.35%; M-Bono 10-year over UST 10-year = 4.17 pp.
- Consensus forecasts for 2026 `[sourced]` (Standardized Forecast, as of 2026-10-15): Mexico CPI 3.76% and 10-year yield 8.78%; US CPI 3.36% and yield 4.66%.
- The output's "breakeven of about 5.5% at three years for Mexico" was ==discarded==: it compares the 10-year M-Bono with the 3-year UDI, and the 10-year UDI returned no data.

## 3. Bimbo cost of debt reference

- Bimbo's average cost of debt is 6.5% at Jun-2026 with a 9.5-year tenor ([[bimbo-debt-hedging-and-leverage-target-capiq-2026-10]]); against the 10-year UST at 5.09% the gap is 141 bp `[calc]`. The output's "140-150 bp over the UST curve" is a rough blended figure across currencies and swaps, not a bond yield `[assumption]`.
- Bimbo's floating BIMBO 26-2 pays TIIE Fondeo + 0.45%, 6.98% for the coupon paid 16-Oct-2026 `[sourced]`.
- Not obtained: yield to maturity of the longest USD bond (the 2051 notes) and the longest MXN fixed bond (BIMBO 26 due 2035), and their spreads; this needs the Capital IQ fixed-income pricing module with ISINs ([[bimbo-bond-prospectus-terms]]).
- The output printed the currency mix 44% USD / 42% MXN, which mixes December 2025 (USD 44%) with June 2026; the June 2026 mix is 42 / 42 / 12 / 3 / 1.

## Key Takeaways

- ==Betas are missing==, so unlevered betas cannot be computed; the unlever factors are ready (book basis) and should be redone with market D/E for the large caps.
- Mexico 5-year CDS is 95 bp; M-Bono 10-year is 9.26% against UST 10-year at 5.09%.
- Bimbo's lease-inclusive total debt is US$10.9bn against book equity of US$6.6bn (D/E 1.64x book) at a 35.6% tax rate.
- Gruma's total debt (US$2.1bn) is now known; the identifiers `BMV:BIMBO A` and `BMV:GRUMA B` work.
- Still needed: levered betas, Mexico EMBI spread, Bimbo bond yields and market capitalisations of Bimbo, Gruma and Arca.
