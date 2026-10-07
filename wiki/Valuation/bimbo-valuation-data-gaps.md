---
Writer: AI-compiled (Claude)
Source: filings/annual/IA25_GB_EEFF_V10.pdf, filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf, filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Jun_26.pdf, filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf
tags: [Valuation, data-gaps]
---

# Valuation Data Gaps (what the filings cannot give)

The filings contain company-reported facts, not market data. This article lists (1) the valuation inputs the filings do support, with where to find them, and (2) the inputs that must be sourced externally. Every external item is a **[unverified] placeholder with no number**: nothing here is an estimate. Public information only (CFA Standard II(A)). Related: [[bimbo-capital-structure-and-debt]], [[bimbo-shareholder-returns]], [[bimbo-balance-sheet-and-leverage]], [[bimbo-fx-exposure]], [[bimbo-guidance-2026]], [[cfa-challenge-timeline]].

## 1. What the filings DO support (use these, with the tag shown)

| Input | Value / location | Tag |
|---|---|---|
| Gross debt, net debt, leverage, cost and maturity | MXN 153,660m / 137,097m / 2.5x / 6.5% / 9.5 yrs at 30-Jun-2026 | [sourced] 2Q26 p.6, BMV Jun-26 p.52 — detail in [[bimbo-capital-structure-and-debt]] |
| Average cost of debt (pre-tax) | 6.3% at Dec-25; 6.5% at Jun-26 (6.51% Dec-24; 7.12% Dec-23) | [sourced] RA25 p.135, p.137; 2Q26 p.6; 4Q23 release p.8 |
| Debt currency mix | Dec-25: USD 44 / MXN 39 / EUR 12 / CAD 3 / GBP 2; Jun-26: 42 / 42 / 12 / 3 / 1 | [sourced] RA25 p.135; 2Q26 p.6 |
| Fair value of fixed-rate debt | Senior notes FV 76,555 vs BV 81,618; Mexican bonds FV about BV (Dec-25) | [calc] from EEFF25 p.47–49 |
| Management post-tax discount rates (impairment tests, Dec-25) | Mexico 10.00%; US 7.27%; Canada 6.50%; Spain 7.00%; Brazil 10.25% (2024: 10.50 / 7.03 / 6.75 / 7.00 / 10.35) | [sourced] EEFF25 p.46 — company WACC proxy by cash-generating unit, post-tax; use only as a cross-check, not as the team's WACC |
| Average growth in impairment models | Mexico 13.47%, US 1.70%, Canada 2.56%, Spain 3.64%, Brazil 6.80% ("crecimiento promedio" in the value-in-use models) | [sourced] EEFF25 p.46 (company assumption; it is not a terminal growth rate and its exact definition is not given) |
| Capex / sales in impairment tests | Mexico 4.15%, US 3.96%, Canada 3.50%, Spain 3.31%, Brazil 4.32% (2025) | [sourced] EEFF25 p.46 |
| Impairment sensitivity | +50 bp discount rate or −50 bp growth produces no impairment (US CGU) | [sourced] EEFF25 p.47 |
| Tax rates (statutory by country; effective rate) | Tax note | [sourced] EEFF25 p.56 (statutory table); effective rate from the income statement — see [[bimbo-income-statement-fy21-fy25]] |
| Share count and treasury shares | 4,296,284,215 outstanding at 30-Jun-2026 | [sourced] BMV Jun-26 p.96–97 — see [[bimbo-shareholder-returns]] |
| Year-end share price history (2011–2025) | e.g. Dec-25 close MXN 59.12; market cap MXN 254,496m | [sourced] RA25 p.20 (annual high / low / close only) |
| Dividends and buybacks | DPS FY21–FY25; buyback MXN 1,253m in 2025 | [sourced] [[bimbo-shareholder-returns]] |
| Interest sensitivity | +/-20 bp SOFR ≈ MXN 22m; +/-100 bp TIIE ≈ MXN 102m | [sourced] EEFF25 p.63 |
| Rating (global) | BBB+ (S&P), BBB+ (Fitch), Baa1 (Moody's) | [sourced] RA25 p.82 |
| Management 2026 guidance | See [[bimbo-guidance-2026]] | [guidance] |

> [!warning] Impairment rates are not the team's WACC
> The discount rates above are management's after-tax rates for impairment testing by cash-generating unit. They are a useful sanity check (e.g. US 7.27% vs a WACC built bottom-up) but are not market-derived inputs, and the filing does not say how they were built (RA25 / EEFF25 p.47 only states they use the WACC concept incl. cost of equity and cost of financial debt).

## 2. External inputs needed (all [unverified] until sourced)

| # | Input | Why needed | Status | Suggested public sources (to be cited with date when sourced) |
|---|---|---|---|---|
| 1 | **Current share price** (BIMBO, BMV) and ADR price (BMBOY) | Market cap, EV, multiples, upside | [unverified] — only 31-Dec-2025 close is in filings | Bolsa Mexicana de Valores website (bmv.com.mx); Yahoo Finance / Google Finance; company IR site |
| 2 | **Diluted market capitalisation and EV** | EV/EBITDA, EV/Sales | [unverified] — needs #1 times shares in [[bimbo-shareholder-returns]] plus net debt, leases, NCI, pensions from [[bimbo-balance-sheet-and-leverage]] | Computation by the team once #1 is dated |
| 3 | **Risk-free rate** — MXN (10-year M-Bono) and USD (10-year UST) | CAPM cost of equity; currency choice | [unverified] | Banco de México (banxico.org.mx) market rates; Valmer / PiP Mexican bond curves; US Treasury daily par yield curve (treasury.gov); FRED |
| 4 | **Equity risk premium** (mature market) | CAPM | [unverified] | Damodaran (Stern NYU) implied ERP, monthly update; Kroll / Duff & Phelps recommended ERP; CFA Institute materials on ERP |
| 5 | **Country risk premium — Mexico** | CAPM for peso / USD cash flows | [unverified] | Damodaran country risk table; JPMorgan EMBI spread for Mexico; Mexico CDS (sources: Bloomberg / Refinitiv or public CDS quotes) |
| 6 | **Beta** (raw and adjusted) vs IPC and vs S&P 500; peer betas for unlevering | CAPM | [unverified] | Bloomberg / Refinitiv; Yahoo Finance 5-year monthly beta; Damodaran industry betas (food processing); compute from price history on BMV if exports are available |
| 7 | **Inflation differential and long-run growth** (MXN vs USD) | Terminal growth; currency consistency | [unverified] | Banxico Survey of Private-Sector Forecasts; INEGI; IMF WEO database; US CBO / Fed projections |
| 8 | **Market cost of debt** — yield to maturity on BBU 2029 / 2034 / 2036 USD notes and on Bimbo MXN bonds | Pre-tax cost of debt vs reported 6.3–6.5% | [unverified] | FINRA TRACE bond data (finra-markets.morningstar.com); Bloomberg / Refinitiv; Valmer / PiP price vendors (Mexican bonds); Bolsa Institucional de Valores |
| 9 | **Target capital structure** (market weights, peer averages) | WACC weights | [unverified] — book data in the filings; market weights depend on #1 | Peer data in #10; team judgment recorded in `notes/` |
| 10 | **Peer set and trading multiples** (EV/EBITDA, P/E, EV/Sales, FCF yield, dividend yield) for packaged food / bakery peers | Comps valuation | [unverified]. Peers must be chosen by the team; candidate names to be checked in [[bakery-market-structure]] and [[bimbo-competitive-position]] | Peers' own filings (SEC EDGAR for US names; BMV / CNBV for Mexican names; SEDAR+ for Canada; company IR pages); Yahoo Finance, Google Finance, MarketScreener, Finviz, Stockanalysis.com for screens; check each multiple's date |
| 11 | **Consensus estimates** (revenue, EBITDA, EPS, DPS, target price, recommendation) | Compare team forecasts vs consensus | [unverified] — no consensus in any filing | Bloomberg / Refinitiv / FactSet / Visible Alpha if accessible through the university; company-compiled analyst consensus on the IR website if published; public sell-side summaries (e.g. press coverage after 2Q26 results, 2026-07-23) |
| 12 | **Rating outlooks and rating agency reports** (S&P, Fitch, Moody's) | Credit view, covenant headroom | [unverified] — global ratings only, no outlooks | Agencies' free press releases (spglobal.com, fitchratings.com, moodys.com); company IR "Debt and ratings" page |
| 13 | **Interest-coverage covenant threshold** and exact definition of Conformed EBITDA | Debt headroom | [unverified] — compliance only is disclosed | Bond indentures / offering memoranda (SEC EDGAR for 144A exhibits if filed; BMV prospectuses for Bimbo CBs; supplements on the BMV site) |
| 14 | **Forward FX curve and rates curve** (USD/MXN, TIIE, SOFR, EUR/MXN, CAD/MXN) | Forecast of FX translation and interest | [unverified] | Banxico (FIX, TIIE, futures MexDer); US Fed (SOFR); ECB; Bank of Canada |
| 15 | **ADR ratio, depositary and free float** | Per-share conversion, liquidity | [unverified] | ADR sponsor depositary page; BMV issuer profile; free float from [[bimbo-governance-and-ownership]] plus external ownership data (Bloomberg / MarketScreener) |
| 16 | **Precedent transactions** (bakery / snack deals, EV/EBITDA and EV/Sales paid) | Precedent multiples | [unverified] — Bimbo's own acquisitions are in [[bimbo-acquisitions]], prices partly disclosed in the filings | Press releases and deal filings (SEC EDGAR, SEDAR+); Mergermarket / Capital IQ if available; check each deal for disclosed EBITDA |
| 17 | **Consensus / market-implied dividend yield and buyback expectations** | Dividend discount cross-check | [unverified] | Company IR; Bloomberg DVD / consensus; dividend announcements for 2026 (see warning on the 2026 per-share amount in [[bimbo-shareholder-returns]]) |
| 18 | **Mexican corporate tax and withholding on dividends / interest, US 21% federal plus state, other statutory rates** | After-tax cost of debt | [unverified] for the current year; the statutory table is in EEFF25 p.56 | EEFF25 p.56 (starting point); SAT (Mexico), IRS (US) tax tables |
| 19 | **Industry data for terminal growth and margin benchmarks** | Terminal assumptions | [unverified] | Euromonitor / Statista (often paywalled); USDA, INEGI, Nielsen Mexico summaries cited in [[bakery-market-structure]] |

## 3. Internal consistency checks to run before the team uses market inputs

- Currency match: if the DCF is in MXN, the risk-free rate and growth must be MXN-consistent; if cash flows are translated at forward rates and discounted in USD, use the USD rate. About 44% of debt and 44% of 2025 sales are USD-linked or North American (RA25 p.135; RA25 p.16 note 1 states North America was 44% of consolidated sales in 2025) — see [[bimbo-fx-exposure]] and [[bimbo-segments-and-regions]].
- Lease basis: choose EV and EBITDA both pre- or post-IFRS 16 ([[bimbo-capital-structure-and-debt]], section 1).
- Date alignment: the filings run to 30-Jun-2026 (2Q26 results released 2026-07-23). Every market input must carry its observation date; today's session date is 2026-10-07.
- Beta window and index: state the window (e.g. 2 or 5 years), frequency and index; do not mix BMV and US indices without explanation.
- Peer multiples: align fiscal year-ends and use the same EBITDA definition (Bimbo "UAFIDA Ajustada", RA25 p.18, adds back non-cash and certain items; check each peer's adjustments).

> [!question] Questions for the team (decisions, not data)
> Which currency and cost-of-equity method will the DCF use (MXN WACC or USD WACC with CRP)? Which peers define the multiple set, and are US-listed bakery peers acceptable alongside Mexican staples? These choices determine which of the external inputs above are critical.

## Key Takeaways

- The filings give debt cost, maturity and mix, share count, dividends and buybacks, and year-end price history, but **no current price, beta, risk-free, ERP, peer multiples or consensus**; all are [unverified] and listed above with public sources.
- Management's impairment-test discount rates (post-tax, by CGU: Mexico 10.00%, US 7.27%, Canada 6.50%, Spain 7.00%, Brazil 10.25%) are the only company-provided WACC-like numbers and should be used only as a cross-check.
- The reported cost of debt (6.3–6.5%) is a book average; the market yield on the BBU 2029/2034/2036 USD notes and Bimbo MXN bonds is needed for the WACC.
- Three company-specific items must be resolved before the valuation: the lease / IFRS 16 basis in EV, the "1.75 per share" 2026 dividend inconsistency, and the covenant threshold.
- Every external number must be logged with source, date and an `[sourced]` tag once found, and recorded in `valuation/valuation.yaml` by the valuation skill, not in the wiki, if it reflects team judgment.
