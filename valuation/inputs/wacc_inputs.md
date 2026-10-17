# WACC inputs (Grupo Bimbo, BIMBOA) - valuation date 2026-10-16

Draft v1, prepared 2026-10-17 by the missing-data agent. Written in English (AGENTS.md). Machine-readable twin: `wacc_inputs.yaml` (built from the same dict).

* Currency route: local MXN. Route L = rf is the M-Bono 10y with CRP 0. Route D = Damodaran-consistent: rf is the M-Bono 10y less the Mexico default spread, plus a lambda-weighted equity CRP.
* Tags: sourced (filing or public source, cited), guidance, assumption, calc (formula given), unverified (not yet tied to a source). Numbers in % unless the unit says otherwise.
* Source codes (S-, W-, WEB-) are listed in section N. Nothing here is a recommendation: the team decides the thesis, the 3-5 drivers, the target price and the rating.

## A. Market data at the valuation date (2026-10-16)

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A1 | BMV close, BIMBO A (last close found for valuation date) | 58.60 | MXN per share | sourced | investing.com BIMBOA historical data (row 'Oct 16, 2026: 58.600 MXN', delayed quote) [WEB-INV]; Yahoo BIMBOA.MX monthly table row 'Oct 16, 2026: 58.60' [WEB-YHH] | 2026-10-16 | Two web sources agree. The official BMV closing file was not retrieved; check against it before the report. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A2 | Previous close (15-Oct-2026) | 57.97 | MXN per share | sourced | investing.com BIMBOA historical data [WEB-INV] | 2026-10-15 | Equals Yahoo's implied previous close (58.60 minus the +0.63 change shown on the key-statistics page). |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A3 | Last CIQ close in the files (fallback anchor) | 55.41 | MXN per share | sourced | data/capitaliq/corporate_issuance.csv, equity_listings 'Last Price' [S-CORP] | 2026-10-06 | Use only if the 16-Oct close is not accepted. Also in cross_holdings.csv [S-XH]. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A4 | 52-week high (BMV) | 68.67 | MXN per share | sourced | data/capitaliq/corporate_issuance.csv '52 Week High' [S-CORP] | 2026-10-06 | CIQ window as of 6-Oct; not re-verified for 16-Oct. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A5 | 52-week low (BMV) | 53.03 | MXN per share | sourced | data/capitaliq/corporate_issuance.csv '52 Week Low' [S-CORP] | 2026-10-06 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A6 | FX: US$ per MXN (CIQ pricing rate) | 0.055690 | US$ per MXN | sourced | data/capitaliq/capiq-ai-prompt1_2026-10-16.md, header note 'MXN converted at 0.055690 USD/MXN' [S-PR1] | 2026-10-15/16 (CIQ pricing) | Banxico FIX for 16-Oct not retrieved; the CIQ rate is used for all peer conversions. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A7 | FX: MXN per US$ | 17.957 | MXN per US$ | calc | 1 / A6 | 2026-10-16 | Formula: 1 / FX (A6) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A8 | Shares outstanding, latest sourced count (net of treasury) | 4,294,943,715 | shares | sourced | wiki/Valuation/bimbo-agm-dividends-and-buybacks.md section 4, BMV daily 'Shares Outstanding' notice [W-ACT] | 2026-07-29 | No later notice is in the sources. CIQ's 4,296,284,215 (06-Oct) equals the 30-Jun figure and is one notice stale. The change is 0.03 percent. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A9 | Market capitalisation (valuation date) | 251,683.7 | MXN m | calc | A1 x A8 / 1,000,000 | 2026-10-16 (price); shares 2026-07-29 | Formula: A1 x A8 / 1,000,000 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A10 | Market capitalisation (valuation date), US$ | 14,016.3 | US$ m | calc | A9 x A6 | 2026-10-16 | Formula: A9 x A6 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A11 | Memo: CIQ market cap at 06-Oct (55.41 x 4,296,284,215) | 238,057.1 | MXN m | sourced | data/capitaliq/cross_holdings.csv 'Market Capitalization (Mex$M)' [S-XH] | 2026-10-06 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| A12 | Memo: 52-week range is CIQ, not Investing or Yahoo | not verified for 16-Oct | text | unverified | CIQ corporate_issuance.csv [S-CORP] | 2026-10-06 |  |

## B. Shares: issued, treasury, outstanding and weighted average

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B1 | Shares outstanding, 31-Dec-2025 (net of treasury) | 4,304,744,119 | shares | sourced | wiki/Company/bimbo-governance-and-ownership.md (RA25 p.308, shares in circulation) [W-GOV] | 2025-12-31 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B2 | Treasury shares held at 31-Dec-2025 (cancelled 30-Apr-2026) | 22,738,214 | shares | sourced | wiki/Valuation/bimbo-agm-dividends-and-buybacks.md section 3 (AGM 30-Apr-2026, CONV-2026 p.1) [W-ACT] | 2025-12-31 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B3 | Issued shares before the 30-Apr-2026 cancellation | 4,327,482,333 | shares | calc | B1 + B2 (matches the 30-Apr-2025 register count 4,327,482,333 in W-GOV) | 2025-12-31 | Formula: B1 + B2 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B4 | Treasury shares cancelled at the 30-Apr-2026 AGM | 22,738,214 | shares | sourced | W-ACT section 3 | 2026-04-30 | Cancelling treasury shares reduces issued capital only. Outstanding shares do not change, so B4 is not deducted from outstanding again. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B5 | Issued shares after the cancellation (bylaw Article 6) | 4,304,744,119 | shares | calc | B3 - B4 (matches bylaw Article 6 in wiki/Risks-ESG/bimbo-governance-checklist-latam.md) | 2026-04-30 | Formula: B3 - B4 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B6 | Treasury shares at 30-Jun-2026 (bought in 1H26) | 8,459,904 | shares | sourced | BMV Jun-26 p.25 via wiki/Financials/bimbo-guidance-2026.md [W-GUIDE] | 2026-06-30 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B7 | Shares outstanding at 30-Jun-2026 | 4,296,284,215 | shares | calc | B5 - B6; ties to BMV Jun-26 p.96 and to CIQ Securities Summary [S-CORP] | 2026-06-30 | Formula: B5 - B6 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B8 | Treasury shares at 29-Jul-2026 | 9,800,404 | shares | calc | B5 - A8 (= 8,459,904 + July buybacks 1,340,500) | 2026-07-29 | Formula: B5 - A8 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B9 | Shares bought back in July 2026 (no cash amount disclosed) | 1,340,500 | shares | calc | B7 - A8, from BMV daily notices [W-ACT section 4] | 2026-07-29 | Formula: B7 - A8 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B10 | Weighted-average diluted shares, FY2025 | 4,310,531 | thousand shares | sourced | wiki/Financials/bimbo-income-statement-fy21-fy25.md table (FY25 4,310,531) [W-IS]; EEFF25 p.13 via bimbo-ifrs-adjustments.md | FY2025 | CIQ quarterly FY25 rows average 4,335.0 m, which does not reconcile (see B13). Use the company figure. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B11 | Weighted-average shares, 1H26 (time-weighted outstanding) | 4,303,271.7 | thousand shares | calc | Step-function average of the 2026 BMV notices (B1 and A8 series) over 1-Jan to 30-Jun-2026, 181 days | 1H26 | Formula: sum(outstanding_i x days_i) / 181, from the BMV notices in W-ACT section 4; The company's own 1H26 figure is not in the wiki. Diluted = basic here: CIQ shows identical basic and diluted counts [assumption]. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B12 | Buybacks, 1H26 (shares) | 8,459,904 | shares | sourced | BMV Jun-26 p.25 and p.18 via W-GUIDE | 1H26 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| B13 | Memo: CIQ quarterly weighted diluted shares (not used) | FQ1-26 4,297.5 m; FQ2-26 4,316.1 m; FY25 quarters 4,354.1 / 4,347.4 / 4,312.7 / 4,325.8 m | text | sourced | data/capitaliq/income_statement.csv 'Weighted Avg. Diluted Shares Out.' [S-IS] | 2025-2026 | Quarterly CIQ counts do not reconcile with the outstanding series or with the company FY25 figure (4,310.5 m). Flagged, not used. |

## C. 2026 dividend and buybacks (reconciliation to the valuation-date bridge)

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C1 | Dividend per share paid in 2026 | 1.075 | MXN per share | sourced | AGM 30-Apr-2026 (W-ACT section 3); CIQ dividends table [S-CORP]; Yahoo history row 'May 12, 2026: 1.075 Dividend' [WEB-YHH] | 2026-05-12 (ex-date) |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C2 | Ex-dividend date | 2026-05-12 | date | sourced | CIQ dividends table [S-CORP]; Yahoo history [WEB-YHH] | 2026-05-12 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C3 | Payment date | 2026-05-13 | date | sourced | CIQ dividends table [S-CORP]; wiki/Company/ciq-corporate-issuance-history.md section 6 [W-CIQDIV] | 2026-05-13 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C4 | Total dividend paid in 2026 | 4,626.7 | MXN m | sourced | BMV Jun-26 p.21 via W-CIQDIV section 6 | 2026-05-13 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C5 | Check: implied shares receiving the dividend | 4,303.9 | m shares | calc | C4 / C1 (ties to about 4,304.7 m outstanding) | 2026-05-12 | Formula: C4 / C1 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C6 | Conflicting DPS: MXN 1.75 per share | not used | text | unverified | Stated in wiki/Thesis/bimbo-catalyst-calendar-facts.md and W-GUIDE | 2026-04-30 | 1.75 x 4,304.7 m = MXN 7,533 m, not 4,626.7 m. It would need 2,644 m shares, so it is rejected. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C7 | Buybacks, 1H26 (cash) | 496 | MXN m | sourced | W-GUIDE (BMV Jun-26 p.18, p.25) | 1H26 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C8 | Returns to shareholders, 1H26 (dividend + buybacks, calc) | 5,122.7 | MXN m | calc | C4 + C7 | 1H26 | Formula: C4 + C7 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C9 | Returns to shareholders, 1H26 (company release) | 5,300 | MXN m | sourced | 2Q26 release p.1 as quoted in W-ACT section 4 ('MXN 5.3bn') | 1H26 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C10 | Gap between C9 and C8 (unexplained) | 177.3 | MXN m | calc | C9 - C8 | 1H26 | Not reconciled. Do not force it; ask IR or read the 2Q26 cash-flow statement. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| C11 | Shares bought back in 2026 to 29-Jul (BMV notices) | 9,800,404 | shares | calc | B1 - A8 (treasury purchases only; the April cancellation is not counted again) | 2026-07-29 | Formula: B1 - A8 |

## D. Capital structure (filings; MXN m unless stated)

**D1 Capital structure at 31-Dec-2025 and 30-Jun-2026**

| Item | 31-Dec-2025 | 30-Jun-2026 | Tag | Source |
|---|---|---|---|---|
| Total debt excl. leases | 153,663 | 153,660 | sourced | EEFF25 p.52; BMV Jun-26 p.52 [W-CAP section 1] |
| Cash and equivalents | 8,535 | 16,563 | sourced | RA25 p.16; 2Q26 p.8 [W-CAP section 1] |
| Net debt excl. leases (company) | 145,128 | 137,097 | sourced | 2Q26 release p.6 [W-CAP section 1] |
| Lease liabilities (IFRS 16) | 34,790 | 33,361 | sourced | EEFF25 p.43 (7,076 + 27,714); 2Q26 p.8 (7,113 + 26,248) |
| Total debt incl. leases | 188,453 | 187,021 | calc | debt excl. leases + leases |
| Non-controlling interest | 743 | 722 | sourced | RA25 p.18; 2Q26 p.7-8 [W-BS] |
| Investments in associates | 7,018 | 6,497 | sourced | 2Q26 p.7-8 table in W-BS (candidate non-operating asset) |
| Employee benefits, non-current | 6,507 | 6,202 | sourced | W-BS table (candidate debt-like item) |
| Defined-benefit net deficit (PBO less plan assets) | 1,524 | n/d | sourced | CIQ pension file, ties to IA25-EEFF p.77-78 [W-PEN] |
| MEPP exit liability | 985 | n/d | sourced | EEFF25 note 19, p.79-80 (via W-BS section 5) |
| Equity attributable to controlling shareholders | 119,512 | 115,272 | sourced | EEFF25 p.15; 2Q26 p.8 |
| Net debt / Adj. EBITDA, ex-IFRS 16 (company) | 2.7x | 2.5x | sourced | RA25 p.18; 2Q26 p.6 |
| Average cost of debt (company; mixed currencies) | 6.3% | 6.5% | sourced | RA25 p.135; 2Q26 p.6 |

Note: 'n/d' = not in the wiki sources for that date. Leases are excluded from net debt but included in the WACC debt weight.

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| D2 | Market debt / equity, incl. leases (Jun-26 debt, valuation-date market cap) | 0.7431 | x | calc | (153,660 + 33,361) / A9 | 2026-10-16 / 2026-06-30 | Formula: (DEBT_EX + LEASE) / A9 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| D3 | Market debt / equity, excl. leases | 0.6105 | x | calc | 153,660 / A9 | 2026-10-16 / 2026-06-30 | Formula: DEBT_EX / A9 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| D4 | Weight of equity E/V (incl. leases) | 0.5737 | share | calc | A9 / (A9 + debt incl. leases) | 2026-10-16 | Formula: E / (E + D) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| D5 | Weight of debt D/V (incl. leases) | 0.4263 | share | calc | 1 - E/V | 2026-10-16 | Formula: 1 - E/V |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| D6 | Memo: CIQ total debt US$10,855m at 17.955 (basis check) | 194,918 | MXN m | calc | US$10,855m (W-WACC, CIQ 3F pull, Jun-26) x 17.955 | 2026-06-30 | About MXN 7.9 bn above the filings basis (187,021). Different debt definition or FX. Filings used for Bimbo. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| D7 | Tax rate for Bimbo (statutory Mexico) | 30.00% | share | sourced | Damodaran ctryprem 30.00% (Jan-2026); EEFF25 p.56 statutory table [WEB-DCTRY] | 2026-01 | The 3F pull reports a 35.6% effective rate; not used for the WACC. |

## E. Bimbo's own beta

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| E1 | Regression beta (5Y monthly vs IPC, or any window) | not computed | text | unverified | Monthly history for BIMBOA.MX returned only 13 closes (Nov-2025 to Oct-2026) [WEB-YHH]; IPC (^MXX) 13 monthly closes [WEB-YHX]; investing.com snapshot covered June-July only | 2026-10-16 | A 5-year monthly regression needs 60 returns. No return series in data/capitaliq. Not computed; one attempt only, per instruction. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| E2 | Published Bimbo beta (investing.com overview) | 0.32 | x (levered, raw) | unverified | investing.com BIMBOA overview, 'Beta' field 0.32 [WEB-INVB]; FAQ 'As of Oct 17, 2026'; price header 'Closed 16/10' | 2026-10-16 | Window and benchmark not printed; date of the beta not explicit. Yahoo shows '--' [WEB-YHK]. Used only as option C, which is not a verified regression. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| E3 | Beta used for Bimbo in the WACC candidates | derived from peers and industry (section H, I, K) | text | assumption | Options A and B in section K | 2026-10-16 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| E4 | Blume-adjusted Bimbo beta (0.67 x raw + 0.33) | 0.5444 | x | calc | E2 (raw published beta) | 2026-10-16 | Formula: 0.67 x E2 + 0.33; Used in the sensitivities of K2 (option C, Blume). |

## F. Rates, sovereign risk and inflation

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F1 | M-Bono 10-year yield (local risk-free) | 9.26 | % | sourced | CIQ rates (3F pull), via W-WACC section 2; verbatim file not yet in raw/ | 2026-10-16 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F2 | M-Bono 20-year yield | 9.72 | % | sourced | CIQ rates, via W-WACC section 2 | 2026-10-16 | No M-Bono 2035 or 5/7-year yield in the sources; the 10-year is the matched proxy for the 2035 bond. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F3 | UST 10-year yield | 5.09 | % | sourced | CIQ rates, via W-WACC section 2 | 2026-10-16 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F4 | UST 20-year yield | 5.48 | % | sourced | CIQ rates, via W-WACC section 2 | 2026-10-15 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F5 | US 10-year TIPS real yield | 2.74 | % | sourced | CIQ rates, via W-WACC section 2 | 2026-10-16 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F6 | US 10-year breakeven inflation | 2.35 | % | calc | F3 - F5 | 2026-10-16 | Formula: F3 - F5 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F7 | Mexico 5-year CDS (sovereign, mid) | 0.953 | % | sourced | 95.30 bp, CIQ, via W-WACC section 2 | 2026-10-16 | 5-year tenor applied to a 10-year bond; a caveat only. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F8 | Memo: BIMBO senior unsecured 5-year CDS (not used) | 0.549 | % | sourced | data/capitaliq/corporate_issuance.csv cds_5y_history, method 'Evaluated' [S-CORP] | 2026-10-05 | Before 27-May-2026 the same series is 'Composite' (142-158 bp). Methodology break; not used. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F9 | Mexico CPI 2026 consensus (CIQ) | 3.76 | % | sourced | CIQ standardized forecast, via W-WACC section 2 | 2026-10-15 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F10 | Banxico inflation target | 3.0 | % | unverified | Secondary only: Bloomberg Tax (Sep-2026) and Oxford Business Group via web search; banxico.org.mx pages returned 404 or a redirect | 2026-10-17 | Confirm on banxico.org.mx before the report. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F11 | Banxico variability band | 1.0 | pp (+/-) | unverified | As F10 (secondary sources) | 2026-10-17 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F12 | Mexico long-term real GDP growth | not retrieved | text | unverified | IMF DataMapper pages returned a template with no data [WEB-IMF]. The Banxico July-2026 survey long-term item was not found; a secondary figure of 1.83% (next decade) could not be confirmed and is not used. | 2026-10-17 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F13 | Mexico long-term nominal MXN GDP growth | not computed | text | unverified | Formula (1 + g_real) x (1 + pi) - 1, with pi = F10 (3.0%); needs F12 | 2026-10-17 |  |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| F14 | Mexico long-term CPI expectation (survey) | not retrieved | text | unverified | Banxico survey long-term item not retrieved | 2026-10-17 |  |

## G. Damodaran inputs (data as of January 2026)

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| G1 | Mature-market implied equity risk premium (monthly, trailing 12m with adjusted payout) | 4.20 | % | sourced | Damodaran home page 'Implied ERP on October 1, 2026: 4.20%' [WEB-DHOME]; previous month 4.14% | 2026-10-01 | Both routes use this value. Memo: annual implied ERP (FCFE) for 2025 = 4.23% in histimpl.html (Jan-2026) [WEB-DERP]. Other Damodaran variants on the home page (3.30% to 5.67%) are not used. |

**G2 Country risk table, Damodaran (ctryprem, last updated 5-Jan-2026)**

| Country | Moody's | Default spread (%) | Country risk premium (%) | Total ERP (%) | Corporate tax (%) | Source |
|---|---|---|---|---|---|---|
| United States | Aa1 | 0.23 | 0.23 | 4.46 | 25.00 | WEB-DCTRY |
| Canada | Aaa | 0.00 | 0.00 | 4.23 | 26.14 | WEB-DCTRY |
| Mexico | Baa2 | 1.62 | 2.46 | 6.69 | 30.00 | WEB-DCTRY |
| Spain | A3 | 1.02 | 1.55 | 5.78 | 25.00 | WEB-DCTRY |
| United Kingdom | Aa3 | 0.51 | 0.78 | 5.01 | 25.00 | WEB-DCTRY |
| China | A1 | 0.60 | 0.91 | 5.14 | 25.00 | WEB-DCTRY |
| Brazil | Ba1 | 2.13 | 3.24 | 7.47 | 34.00 | WEB-DCTRY |
| Japan | n/a | n/a | n/a | n/a | 29.74 | WEB-DCTRY (tax only) |
| Switzerland | n/a | n/a | n/a | n/a | 19.61 | WEB-DCTRY (tax only; national rate, canton not verified) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| G3 | Mexico equity-to-bond volatility multiplier (CRP / default spread) | 1.519 | x | calc | 2.46 / 1.62 (Mexico row) | 2026-01 | Formula: CRP / default spread |

**G4 Damodaran synthetic default spreads (large firms, January 2026)**

| Rating (Moody's / S&P) | Interest coverage (lower to upper) | Spread (%) | Source |
|---|---|---|---|
| Aaa / AAA | 8.50 and above | 0.40 | WEB-DRAT |
| Aa2 / AA | 6.50 to 8.50 | 0.55 | WEB-DRAT |
| A1 / A+ | 5.50 to 6.50 | 0.70 | WEB-DRAT |
| A2 / A | 4.25 to 5.50 | 0.78 | WEB-DRAT |
| A3 / A- | 3.00 to 4.25 | 0.89 | WEB-DRAT |
| Baa2 / BBB | 2.50 to 3.00 | 1.11 | WEB-DRAT |
| Baa1 / BBB+ (interpolated) | not in table | 1.00 | calc: midpoint of A3/A- and Baa2/BBB |
| Ba1 / BB+ | 2.25 to 2.50 | 1.38 | WEB-DRAT |

Note: Bimbo's EBIT-based coverage was not computed; the rating-based spread is used because Bimbo is BBB+/Baa1 (LSEG).

**G5 Damodaran Food Processing (US, January 2026)**

| Metric | Value | Source |
|---|---|---|
| Number of firms | 78 | WEB-DBETA |
| Levered beta | 0.61 | WEB-DBETA |
| D/E | 43.73% | WEB-DBETA |
| Effective tax rate | 10.37% | WEB-DBETA (effective, not marginal) |
| Unlevered beta | 0.46 | WEB-DBETA |
| Cash / firm value | 2.56% | WEB-DBETA |
| Unlevered beta corrected for cash | 0.47 | WEB-DBETA |

**G6 Damodaran Food Processing (Global, dataset January 2026; footer reads January 2025)**

| Metric | Value | Source |
|---|---|---|
| Number of firms | 1,450 | WEB-DBETAG |
| Levered beta | 0.67 | WEB-DBETAG |
| D/E | 37.10% | WEB-DBETAG |
| Effective tax rate | 16.35% | WEB-DBETAG (effective; marginal option exists) |
| Unlevered beta | 0.53 | WEB-DBETAG |
| Cash / firm value | 5.82% | WEB-DBETAG |
| Unlevered beta corrected for cash | 0.56 | WEB-DBETAG |

Note: Emerging-market and other regional Food Processing rows were not retrieved.

## H. Peer betas, market caps and unlevering (valuation date 16-Oct-2026)

**H1 Peer inputs (debt incl. leases in US$ m; market cap in US$ m; betas levered, 5Y monthly)**

| Company (ticker) | Total debt (US$ m) | Market cap (US$ m) | Market D/E (x) | Statutory tax | Levered beta | Blume-adjusted levered beta | Unlevered beta | Beta source | Market cap source |
|---|---|---|---|---|---|---|---|---|---|
| Flowers Foods (NYSE:FLO) | 2,007.8 | 1,295.7 | 1.5496 | 25.00% | 0.43 | 0.6181 | 0.1989 | stockanalysis.com 5Y (16-Oct) | CIQ 15/16-Oct |
| Gruma B (BMV:GRUMA B) | 2,112.0 | 4,406.7 | 0.4793 | 30.00% | n/a | n/a | n/a | n/a (Yahoo '--'; stockanalysis not found) | Yahoo MXN 79.13bn (16-Oct) x CIQ FX |
| Yamazaki Baking (TSE:2212) | 600.9 | 4,654.8 | 0.1291 | 29.74% | n/a | n/a | n/a | n/a (Yahoo '--'; stockanalysis not found) | Yahoo JPY 718.11bn (16-Oct) x CIQ FX 0.006482 |
| Aryzta (SWX:ARYN) | 986.9 | 1,218.8 | 0.8097 | 19.61% | 0.38 | 0.5846 | 0.2302 | stockanalysis.com 5Y (16-Oct) | CIQ 15/16-Oct (stockanalysis CHF 1.00bn) |
| J.M. Smucker (NYSE:SJM) | 6,940.2 | 13,612.5 | 0.5098 | 25.00% | 0.27 | 0.5109 | 0.1953 | stockanalysis.com 5Y (Yahoo 0.27) | CIQ 15/16-Oct (stockanalysis 13.61bn) |
| Campbell's (NasdaqGS:CPB) | 7,450.0 | 5,925.9 | 1.2572 | 25.00% | 0.04 | 0.3568 | 0.0206 | stockanalysis.com 5Y (Yahoo 0.04) | CIQ 15/16-Oct (stockanalysis 5.93bn) |
| Mondelez (NasdaqGS:MDLZ) | 22,059.0 | 81,568.8 | 0.2704 | 25.00% | 0.39 | 0.5913 | 0.3242 | stockanalysis.com 5Y (Yahoo 0.39) | CIQ 15/16-Oct (stockanalysis 81.57bn) |
| Arca Continental (BMV:AC) | 3,644.0 | 18,683.4 | 0.1950 | 30.00% | 0.08 | 0.3836 | 0.0704 | Yahoo only (not on stockanalysis) | Yahoo MXN 335.49bn (16-Oct) x CIQ FX; does not reconcile with shares shown |
| PepsiCo (NasdaqGS:PEP) | 51,881.0 | 179,200.5 | 0.2895 | 25.00% | 0.36 | 0.5712 | 0.2958 | stockanalysis.com 5Y (Yahoo 0.36) | CIQ 15/16-Oct (stockanalysis 179.19bn) |

Note: Unlevered beta = beta_l / (1 + (1 - t) x D/E), gross debt incl. leases, no cash correction (plain Hamada). Statutory tax from Damodaran ctryprem (US 25.00%, Mexico 30.00%, Japan 29.74%, Switzerland 19.61%). Gruma and Yamazaki betas not retrieved. Arca's beta comes from Yahoo only. Debt: CIQ LTM totals (S-PR1); Gruma 2,112 from the 3F pull (W-WACC section 1; verbatim file not in raw/).

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H2 | Median unlevered beta, core peers with data (Flowers, Aryzta; Gruma and Yamazaki n/a) | 0.2145 | x | calc | section H1 (n = 2 of 4) | 2026-10-16 | Formula: median(bu_FLO, bu_ARYN) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H3 | Median unlevered beta, six peers with stockanalysis 5Y betas (used in option A) | 0.2145 | x | calc | section H1 (FLO, ARYN, SJM, CPB, MDLZ, PEP) | 2026-10-16 | Formula: median(bu of six peers) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H4 | Mean unlevered beta, six peers | 0.2108 | x | calc | section H1 | 2026-10-16 | Formula: mean(bu of six peers) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H5 | Median unlevered beta, seven peers including Arca (Yahoo beta) | 0.1989 | x | calc | section H1 | 2026-10-16 | Formula: median(bu of seven peers) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H6 | Mean unlevered beta, seven peers including Arca | 0.1908 | x | calc | section H1 | 2026-10-16 | Formula: mean(bu of seven peers) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H9 | Median Blume-adjusted unlevered beta, six peers (Blume applied to levered betas before unlevering) | 0.3618 | x | calc | section H1 (FLO, ARYN, SJM, CPB, MDLZ, PEP) | 2026-10-16 | Formula: median of [(0.67 x beta + 0.33) / (1 + (1 - t) x D/E)] |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H7 | Caveat on peer betas | very low (0.04 to 0.43 levered) | text | unverified | stockanalysis.com and Yahoo agree on SJM, CPB, MDLZ, PEP. Benchmark index not printed on either page. | 2026-10-16 | The unlevered median of about 0.21 implies a cost of equity close to the risk-free rate plus 0.9 pp. Not credible alone; treat option A as a low-end cross-check. |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| H8 | Peer market caps (CIQ) vs Yahoo/stockanalysis | agree within 1 to 5 percent for US names | text | sourced | section H1; data/capitaliq/capiq-ai-prompt1_2026-10-16.md [S-PR1] | 2026-10-16 | Cross-check with valuation/inputs/peers.yaml (other workstream; FLO price 6.108911, market cap 1,295.7): consistent. |

## I. Operating exposure (lambda) for the country risk premium

**I1 Revenue and EBITDA weights by region and proxy CRP**

| Region (Bimbo segment) | Revenue weight FY25 | EBITDA weight FY25 | CRP proxy (%) | Proxy basis | Source |
|---|---|---|---|---|---|
| North America (US + Canada) | 44.6% | 28.8% | 0.18 | US 0.23% x 60/77 plants + Canada 0.00% x 17/77 plants (Damodaran ctryprem) | W-SEG sections 2-4; RA25 p.82-83 |
| Mexico | 32.4% | 55.4% | 2.46 | Damodaran Mexico CRP 2.46% (Baa2) | W-SEG; EBITDA weight includes eliminations |
| EAA (Europe, Asia, Africa) | 12.7% | 9.8% | 1.55 | Proxy: Spain 1.55% (largest European plant base; 61 of 92 EAA plants in Europe). Assumption. | W-SEG; RA25 p.115-116 |
| Latin America | 10.3% | 6.0% | 3.24 | Proxy: Brazil 3.24% (14 of 42 LatAm plants). Argentina and Venezuela excluded (hyperinflation, not in table). Assumption. | W-SEG; RA25 p.85, p.115 |

Note: Revenue shares: FY25, consolidated basis (W-SEG section 3). EBITDA shares: FY25 Adj. EBITDA (W-SEG section 3, Celebramos p.17).

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| I2 | Operating-exposure CRP, revenue weights (lambda, used in route D) | 1.4075 | % | calc | sum of revenue weight x CRP proxy (I1) | FY2025 weights | Formula: sum(w_rev x CRP) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| I3 | Operating-exposure CRP, EBITDA weights (sensitivity) | 1.7608 | % | calc | sum of EBITDA weight x CRP proxy (I1) | FY2025 weights | Formula: sum(w_ebitda x CRP) |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| I4 | Equity risk premium in route D = mature ERP + I2 | 5.6075 | % | calc | G1 + I2 | 2026-01 / FY2025 | Formula: G1 + I2 |

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| I5 | Note on the CRP definition | CRP = default spread x (equity vol / bond vol) | text | sourced | Damodaran ctryprem: CRP for Mexico = 2.46 = 1.62 x 1.52 (G3) | 2026-01 | Route L (local rf, CRP = 0) and route D (rf net of default spread, plus lambda CRP) are shown side by side. Both are proposals for the team. |

## J. Pre-tax cost of debt in MXN (valuation date)

| ID | Item | Value | Unit | Tag | Source | As of | Formula / note |
|---|---|---|---|---|---|---|---|
| J1 | Bimbo credit ratings (global) | BBB+ (S&P), BBB+ (Fitch), Baa1 (Moody's) | text | sourced | LSEG issuer ratings via wiki/Valuation/bimbo-credit-risk-lseg.md (S&P negative since 20-Mar-2025; Fitch stable 29-Jul-2026; Moody's stable 15-Nov-2024) | 2026-07-29 | National scale AAA(mex) on local bonds (W-BOND). Used only to justify the synthetic spread in candidate C. |

**J2 Cost of debt candidates**

| Candidate | Pre-tax kd (%) | Basis | Tag | Source / as of |
|---|---|---|---|---|
| A. BIMBO 23L market yield (primary) | 9.26 | Yield on MXN 9.24% 2033 bond, price 99.87 (LSEG) | sourced | W-LSEG section 3a; export 2026-10-10, pricing date not stated |
| B. Matched-maturity spread | 9.71 | M-Bono 10y 9.26% + 0.45 pp (BIMBO 26 spread at Feb-2026 issue) | calc | F1 + spread (W-BOND) |
| C. Synthetic rating spread | 10.26 | M-Bono 10y 9.26% + 1.00 pp (Damodaran BBB+/Baa1, interpolated) | calc | F1 + G4 (Jan-2026) |
| Fallback: BIMBO 26 coupon (not a yield) | 9.22 | Issue coupon 9.22%, due 26-Jan-2035 (Feb-2026 issue) | sourced | W-BOND; W-CAP section 4 |
| Memo: BIMBO 25 coupon 10.06% (due 6-Feb-2032); yield not in sources | 10.06 | Issue coupon 14-Feb-2025; fixed spread +30 bp over M-Bono at issue | sourced | W-BOND; W-CAP section 3b |
| Memo: BIMBO 23L coupon 9.24% (due 20-May-2033) | 9.24 | Issue coupon 2-Jun-2023 (the basis of candidate A's yield) | sourced | W-BOND; W-CAP section 3b |
| Memo: company average cost of debt (not MXN) | 6.50 | USD/MXN/EUR mix after swaps | sourced | 2Q26 p.6 (Jun-26) |
| Memo: USD notes YTM 2036 (not MXN) | 6.30 | LSEG; USD spread about 107 bp | sourced | W-LSEG section 3a (pricing date not stated) |

Note: Route L and route D use the same pre-tax MXN cost of debt. Candidate A is used in the WACC table; B and C are sensitivities. Candidate A equals the 10-year M-Bono (9.26%), so route L would show no credit spread on a naive reading. It is not zero: the 23L matures in 2033, shorter than the 10-year benchmark, and the curve slopes upward (10y 9.26%, 20y 9.72%), so the 2033 government yield is below 9.26% and the 23L carries a positive spread. Its pricing date (about 10-Oct) is about a week before the valuation date; the team can switch to B (9.71%), which follows the coordinator's matched-maturity fallback.

## K. WACC candidate table (proposals for the team, not decisions)

**K1 WACC candidates: 3 beta options x 2 routes (MXN, valuation date 2026-10-16)**

| Case | Route | Beta option | Unlevered beta | Levered beta (D/E 0.743, tax 30%) | rf (%) | ERP + CRP (%) | ke (%) | kd pre-tax (%) | kd after tax (%) | E/V | D/V | WACC (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L-A | Local (MXN) | A. Bottom-up: median unlevered beta of six peers with 5Y betas | 0.2145 | 0.3261 | 9.26 | 4.20 | 10.63 | 9.26 | 6.48 | 0.5737 | 0.4263 | 8.86 |
| L-B | Local (MXN) | B. Damodaran Food Processing, US (unlevered 0.46) | 0.4600 | 0.6993 | 9.26 | 4.20 | 12.20 | 9.26 | 6.48 | 0.5737 | 0.4263 | 9.76 |
| L-B2 | Local (MXN) | B2. Damodaran Food Processing, Global (unlevered 0.53) | 0.5300 | 0.8057 | 9.26 | 4.20 | 12.64 | 9.26 | 6.48 | 0.5737 | 0.4263 | 10.02 |
| L-C | Local (MXN) | C. Published Bimbo beta 0.32 (investing.com; window and benchmark not printed) | 0.2105 | 0.3200 | 9.26 | 4.20 | 10.60 | 9.26 | 6.48 | 0.5737 | 0.4263 | 8.85 |
| D-A | Damodaran-consistent | A. Bottom-up: median unlevered beta of six peers with 5Y betas | 0.2145 | 0.3261 | 7.64 | 5.61 | 9.47 | 9.26 | 6.48 | 0.5737 | 0.4263 | 8.20 |
| D-B | Damodaran-consistent | B. Damodaran Food Processing, US (unlevered 0.46) | 0.4600 | 0.6993 | 7.64 | 5.61 | 11.56 | 9.26 | 6.48 | 0.5737 | 0.4263 | 9.40 |
| D-B2 | Damodaran-consistent | B2. Damodaran Food Processing, Global (unlevered 0.53) | 0.5300 | 0.8057 | 7.64 | 5.61 | 12.16 | 9.26 | 6.48 | 0.5737 | 0.4263 | 9.74 |
| D-C | Damodaran-consistent | C. Published Bimbo beta 0.32 (investing.com; window and benchmark not printed) | 0.2105 | 0.3200 | 7.64 | 5.61 | 9.43 | 9.26 | 6.48 | 0.5737 | 0.4263 | 8.18 |

Note: ke = rf + beta_l x (ERP + CRP). WACC = E/V x ke + D/V x kd x (1 - 0.30). Route L: rf = 9.26%, CRP 0. Route D: rf = 9.26% - 1.62% = 7.64%, ERP + lambda CRP (1.41%). Option B uses Damodaran's plain unlevered beta (effective-tax basis). Option C uses the published raw beta 0.32 at Bimbo's own leverage (no relevering); its window and benchmark are not printed. The regression is not computed.

**K2 Sensitivities (not proposals)**

| Sensitivity | WACC (%) | kd (%) |
|---|---|---|
| L-C with Blume-adjusted published beta (0.5444) | 9.39 | 9.26 |
| D-C with Blume-adjusted published beta (0.5444) | 8.90 | 9.26 |
| L-A with Blume-adjusted median unlevered beta (option A, Blume) | 9.40 | 9.26 |
| D-A with Blume-adjusted median unlevered beta (option A, Blume) | 8.92 | 9.26 |
| L-B (US) with matched-maturity kd (M-Bono 10y + 45 bp) | 9.89 | 9.71 |
| D-B with Mexico spread = 5y CDS (0.953%) | 9.78 | 9.26 |
| D-B with EBITDA-weighted CRP | 9.54 | 9.26 |
| L-B with cash-corrected unlevered beta 0.47 | 9.80 | 9.26 |
| D-B with cash-corrected unlevered beta 0.47 | 9.44 | 9.26 |

## L. Open issues (flags)

* Bimbo regression beta not computed: only 13 monthly closes and 13 IPC closes were retrievable; 60 are needed.
* Bimbo published beta 0.32 is from investing.com's overview (option C). Window and benchmark are not printed and the date is not explicit. Yahoo shows '--'; stockanalysis Bimbo pages not found. Treat C as a single-source fallback.
* Core peer betas: Gruma and Yamazaki not retrieved; Flowers and Aryzta come from stockanalysis.com only. Option A is therefore thin (two core peers).
* Peer 5Y betas are very low (0.04 to 0.43 levered). Benchmark index not printed on either source. The lower-bound result is not credible alone.
* Damodaran's home page says the country-risk update is as of 1 July 2026, but the country table fetched here is the January 2026 version. Mexico CRP and default spread may have changed; re-check before the report. ERP is the monthly 4.20% (1-Oct-2026) from the home page.
* Damodaran Food Processing rows use effective tax rates (US 10.37%; Global 16.35%). The Global page footer reads January 2025 while its header reads January 2026.
* Mexico default spread: Damodaran 1.62% (Baa2, used in route D to match the CRP table) vs CIQ 5y CDS 0.953% (sovereign, 5-year tenor). Sensitivity in K2.
* BBB+/Baa1 synthetic spread interpolated (1.00 pp): Damodaran's table has no Baa1/BBB+ row.
* Banxico target (3%, +/-1 pp): primary page not reachable (404 and redirect). Secondary sources only; confirm on banxico.org.mx.
* Long-term real GDP growth and long-term nominal MXN growth not retrieved. The 1.83% figure seen in one summary was not confirmed and is not used.
* Shares outstanding after 29-Jul-2026 not verified. CIQ's 06-Oct count (4,296,284,215) is one notice stale; the difference is 0.03 percent.
* Weighted-average shares 1H26 is a time-weighted calc from BMV notices. CIQ quarterly counts do not reconcile (B13).
* 2026 DPS: 1.075 used (ties to MXN 4,626.7 m). The 1.75 figure in two wiki articles is rejected (C6).
* 1H26 returns: 4,626.7 + 496 = 5,122.7 versus the release's MXN 5.3 bn. Gap of about 177 m not explained (C10).
* Bimbo total debt: CIQ US$10,855m converts to MXN 194.9 bn vs filings 187.0 bn (incl. leases). Filings used (D6).
* BMV close 58.60 (16-Oct) from two delayed-quote pages, not the official BMV file. The 52-week range is CIQ at 6-Oct.
* Gruma total debt (US$2,112 m) is from the 3F CIQ pull (wiki); the verbatim CIQ file is not in raw/. Its market cap (Yahoo, MXN 79.13 bn) has no displayed share count to check.
* Arca Continental market cap from Yahoo (MXN 335.49 bn) does not reconcile with the 1.7 bn shares shown (about MXN 356 bn). Its beta (0.08) is from Yahoo only.
* Aryzta tax rate is the Swiss national rate (19.61%); the canton is not verified.
* LSEG bond yield pricing date not stated (export 2026-10-10). Treat the 9.26% 23L yield as about 9-10 October.
* Pension and debt-like items: DB net deficit 1,524 and MEPP 985 (Dec-25); employee benefits non-current 6,507 (Dec-25) / 6,202 (Jun-26). Team decides which enter net debt.
* CIQ FX 0.055690 (17.955 MXN per US$) is the pricing-date rate in the CIQ header. Banxico FIX not retrieved.

## M. Not retrieved

* Bimbo regression beta (needs 60 monthly returns). The investing.com beta 0.32 has no stated window or benchmark.
* Investing.com cross-check of the peer betas (for example SJM); the investing.com page URL was not found. Stockanalysis and Yahoo agree on SJM.
* Damodaran country-risk table dated 1 July 2026 (the site says so; the fetched copy is January 2026).
* Gruma B and Yamazaki Baking 5Y betas (Yahoo '--'; stockanalysis not found).
* Damodaran regional CRP averages (Latin America, Europe, Asia, Africa); the CRP proxies in section I are country-level.
* Damodaran Emerging-market and other regional Food Processing rows (only US and Global retrieved).
* Banxico inflation target from banxico.org.mx (primary); Banxico survey long-term GDP and inflation items (July 2026).
* Mexico long-term real GDP growth (IMF DataMapper returned an empty template).
* Mexico M-Bono 2035 matched-maturity yield (only 10y and 20y in sources); BIMBO 26, 25 and 25-2 yields.
* Bimbo USD notes and MXN bond yields dated 16-Oct-2026 (LSEG export pricing date unknown).
* Aryzta canton (Swiss tax); US state tax (Damodaran combined rate used instead of 21% federal plus state).
* Company 1H26 weighted-average diluted shares (2Q26 filing); reconciliation of 1H26 returns (MXN 5.3 bn).
* Shares outstanding after 29-Jul-2026 (BMV notices beyond that date).
* Gruma total debt in the verbatim CIQ file (3F); Gruma and Arca share counts on a verified basis.
* Bimbo EBIT-based interest coverage (Damodaran synthetic rating by coverage).

## N. Source codes

| Code | Source |
|---|---|
| S-PR1 | data/capitaliq/capiq-ai-prompt1_2026-10-16.md (CIQ AI paste; pricing 15/16-Oct-2026; FX header) |
| S-CORP | data/capitaliq/corporate_issuance.csv (equity listings, dividends, CDS history) |
| S-XH | data/capitaliq/cross_holdings.csv (price 55.41 and market cap 238,057 at 06-Oct-2026) |
| S-IS | data/capitaliq/income_statement.csv (weighted-average shares rows) |
| W-ACT | wiki/Valuation/bimbo-agm-dividends-and-buybacks.md (AGM, cancellations, 2026 share-count notices, section 4) |
| W-GOV | wiki/Company/bimbo-governance-and-ownership.md (register and shares in circulation) |
| W-CAP | wiki/Valuation/bimbo-capital-structure-and-debt.md (debt, cash, leases, ratings, dividends) |
| W-WACC | wiki/Valuation/bimbo-wacc-market-inputs-capiq-2026-10.md (CIQ rates, CDS, 3F pull: Gruma debt, tax) |
| W-PEER | wiki/Valuation/peer-leverage-capiq-2026-10.md (peer debt and leverage) |
| W-BS | wiki/Financials/bimbo-balance-sheet-and-leverage.md (associates, employee benefits, NCI) |
| W-PEN | wiki/Financials/ciq-pension-obligations.md (DB deficit) |
| W-SEG | wiki/Company/bimbo-segments-and-regions.md (segment sales, EBITDA, plants) |
| W-IS | wiki/Financials/bimbo-income-statement-fy21-fy25.md (weighted-average shares FY21-FY25) |
| W-BOND | wiki/Valuation/bimbo-bond-prospectus-terms.md (issue coupons and spreads) |
| W-LSEG | wiki/Valuation/bimbo-credit-risk-lseg.md (bond yields, ratings, pricing-date caveat) |
| W-GUIDE | wiki/Financials/bimbo-guidance-2026.md (1H26 buybacks, treasury shares) |
| W-CIQDIV | wiki/Company/ciq-corporate-issuance-history.md (dividends and CDS) |
| WEB-INV | https://www.investing.com/equities/bimbo-a-historical-data (retrieved 2026-10-17): 16-Oct close 58.600; 15-Oct 57.970 |
| WEB-YHH | https://finance.yahoo.com/quote/BIMBOA.MX/history/?frequency=1mo (retrieved 2026-10-17): 'Oct 16, 2026: 58.60'; 'May 12, 2026: 1.075 Dividend' |
| WEB-YHX | https://finance.yahoo.com/quote/%5EMXX/history/?frequency=1mo (retrieved 2026-10-17): IPC monthly closes (13 rows) |
| WEB-YHK | https://finance.yahoo.com/quote/<TICKER>/key-statistics/ (retrieved 2026-10-17): betas and market caps for peers; Bimbo '--' |
| WEB-SA | https://stockanalysis.com/stocks/<ticker>/statistics/ (retrieved 2026-10-17): FLO 0.43, ARYN 0.38, SJM 0.27, CPB 0.04, MDLZ 0.39, PEP 0.36 (5Y beta; 16-Oct close) |
| WEB-DCTRY | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html (Last updated January 5, 2026) |
| WEB-DERP | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html (Data used as of January 2026) |
| WEB-DBETA | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html (Data used as of January 2026) |
| WEB-DBETAG | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html (date of analysis January 2026; footer January 2025) |
| WEB-DRAT | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html (Data used as of January 2026) |
| WEB-DHOME | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm (retrieved 2026-10-17): 'Implied ERP on October 1, 2026': 4.20% trailing 12m with adjusted payout (previous month 4.14%); country-risk update as of July 1, 2026 |
| WEB-INVB | https://www.investing.com/equities/bimbo-a (retrieved 2026-10-17): 'Beta' 0.32, no window or benchmark printed; FAQ 'As of Oct 17, 2026' |
| WEB-IMF | https://www.imf.org/external/datamapper/NGDP_RPCH@WEO/MEX (template only; no data retrieved) |
| WEB-BX | Secondary: Bloomberg Tax (Sep-2026) and Oxford Business Group (Banxico 3% +/-1 pp) via web search; banxico.org.mx returned 404 |
