# Capital IQ data request — Grupo Bimbo (BIMBOA) CFA Research Challenge

_Created 2026-10-16. Purpose: close every open data gap in one pass, so the three pillars (climate, new CEO, debt management) rest on `[sourced]` numbers. Paste the MASTER PROMPT into the Capital IQ AI (ChatIQ / Capital IQ Pro assistant). If it truncates or times out, send one BLOCK at a time, each preceded by the PREAMBLE._

## 0. What was missing (checklist the prompt covers)

| # | Gap | Why we need it | Block |
|---|---|---|---|
| 1 | Net debt/EBITDA, total debt/EBITDA, interest cover of the 9 peers | Verify the claim "Bimbo has 2x the debt of its competitors" | B |
| 2 | Market cap, net debt, EV, EBITDA, FYE, currency of all 10 companies | Derive leverage from multiples and calendarize | A |
| 3 | EV/EBITDA, EV/Sales, P/E, FCF yield, dividend yield: current, NTM, 5y and 10y average | Refresh the unverified multiples inherited from 2026-10-08 | C |
| 4 | Margins, growth, capex, FCF, payout, ROIC of peers, 5 FY + LTM + consensus | Operating comparison and forecast anchors | D |
| 5 | Bimbo debt stack: maturities, currency, fixed/floating, cost, bonds, ratings history, covenants, hedges | Pillar 3 (debt management) | E |
| 6 | Bimbo leverage history by quarter and management's stated leverage target | Pillar 3 | E |
| 7 | Current CEO: appointment date, predecessor, background, mandate, compensation, KPIs, key developments, other management changes, insider ownership | Pillar 2 (new CEO) | F |
| 8 | Climate: emissions (Scope 1/2/3), targets, CDP/MSCI/Sustainalytics/S&P ESG scores, climate capex, commodity and hedging disclosure, weather events in key developments; same for peers | Pillar 1 (climate) | G |
| 9 | Commodity and FX series: wheat (CBOT, KC), sugar, soybean and palm oil, MXN/USD, BRL/USD, with forward curves | Link climate to cost of goods | G |
| 10 | WACC inputs: beta, risk-free (UST 10y, M-Bono 10y), country risk, Bimbo bond yields and spreads, CDS | Valuation | H |
| 11 | Consensus: EPS, EBITDA, sales, target price, rating distribution, revisions | Differentiate from consensus | H |
| 12 | Ownership: Bimbo holders and controlling holders of Gruma, Arca, Lala, Nutresa | Governance and peer structure | I |
| 13 | M&A: Wickbold (Brazil), Nutresa's 39.99% of Bimbo Colombia, other 2024-26 deals; value, multiple, date | Inorganic growth and debt use | I |
| 14 | Market shares and rankings stated in CapIQ documents (US bread/snacks, Mexico, Brazil, Colombia, etc.) | Pendientes 1-6, 11 of the industry report | J |
| 15 | Sector context: IEPS, NOM-051, tariffs, labor reform mentioned in transcripts | Risks | J |

---

## 1. MASTER PROMPT (paste into Capital IQ AI)

```text
ROLE
You are a data analyst supporting a CFA Institute Research Challenge team that covers Grupo Bimbo, S.A.B. de C.V. (BMV: BIMBOA). Use ONLY Capital IQ data, filings, transcripts, key developments, broker research and S&P Global ESG data available in this platform. This is public information only.

RULES (apply to every block)
1. Return markdown tables, one table per item, with units in the column header. Use ISO dates (YYYY-MM-DD).
2. Add the columns "Source" (Capital IQ data item, or document title + date + page) and "As-of date" to every table.
3. Never estimate, interpolate or fill gaps from memory. If a value is not in Capital IQ, write "N/A" and say where you looked.
4. Mark each number as: Reported (company filing), CIQ-standardized, Consensus (Street estimate) or Calculated. For Calculated, show the formula.
5. State the currency (local currency AND USD) and fiscal year-end of every company. Show LTM as of the latest reported quarter, and name that quarter.
6. If two sources disagree, show both values and the difference. Do not pick one silently.
7. For text answers (CEO, shares, climate), quote the passage in no more than 25 words and cite document, date and page. Do not paraphrase numbers.
8. At the end, list every item you could NOT retrieve.

COMPANY UNIVERSE (confirm each identifier before pulling data; if a ticker does not resolve, search by company name and tell me the identifier you used)
| # | Company | Capital IQ ticker | Country | Role |
|---|---|---|---|---|
| 0 | Grupo Bimbo, S.A.B. de C.V. | BMV:BIMBOA | Mexico | TARGET |
| 1 | Flowers Foods, Inc. | NYSE:FLO | USA | Core peer |
| 2 | Gruma, S.A.B. de C.V. | BMV:GRUMAB | Mexico | Core peer |
| 3 | Yamazaki Baking Co., Ltd. | TSE:2212 | Japan | Core peer |
| 4 | Aryzta AG | SWX:ARYN | Switzerland | Core peer |
| 5 | The J.M. Smucker Company | NYSE:SJM | USA | Secondary peer |
| 6 | The Campbell's Company | NasdaqGS:CPB | USA | Secondary peer |
| 7 | Mondelez International, Inc. | NasdaqGS:MDLZ | USA | Secondary peer |
| 8 | Arca Continental, S.A.B. de C.V. | BMV:AC | Mexico | Secondary peer |
| 9 | PepsiCo, Inc. | NasdaqGS:PEP | USA | Secondary peer |
| R | Grupo Nutresa S.A. | BVC:NUTRESA | Colombia | Reference only (ex-partner of Bimbo Colombia) |

BLOCK A — Market data (latest close; give the date)
For all 10 companies + Nutresa: share price, shares outstanding (diluted), market cap, total debt (incl. leases), cash and short-term investments, net debt, minority interest, preferred, enterprise value, LTM EBITDA, LTM EBIT, LTM revenue, fiscal year-end, reporting currency, and the last reported quarter.

BLOCK B — Leverage and credit (answers: "does Bimbo have 2x the debt of its competitors?")
For all 10 companies, for each of the last 5 fiscal years and LTM:
- Total debt, net debt, EBITDA.
- Net debt/EBITDA, total debt/EBITDA, net debt/EV, debt/total capital, debt/equity.
- EBITDA/interest expense, EBIT/interest expense, FFO/total debt.
- Average cost of debt (interest expense / average debt) and the effective tax rate.
- Share of debt in USD / local currency / EUR, and share fixed vs floating, where disclosed.
- Credit ratings (S&P, Moody's, Fitch): current rating, outlook, and every change in the last 10 years with date.
Then build one summary table ranking the 10 companies by net debt/EBITDA (LTM), with the median and mean of (i) the 4 core peers and (ii) all 9 peers. Show Bimbo's ratio divided by each median. Show the same ratio on a total-debt basis and on a net-debt-plus-leases basis, because the answer may change with the definition.

BLOCK C — Multiples (current, NTM and history)
For all 10 companies: EV/EBITDA (LTM and NTM), EV/EBIT, EV/Sales, P/E (LTM and NTM), P/FCF, FCF yield, dividend yield, and the 5-year and 10-year average and median of EV/EBITDA and P/E. Use the same date for all. Also show Bimbo's discount or premium versus each peer and versus the core-4 median, today and on the 5y/10y average.

BLOCK D — Operating comparison (5 FY + LTM + consensus FY26E/FY27E/FY28E)
For all 10 companies: revenue, organic or ex-FX growth where disclosed, gross margin, EBITDA margin, EBIT margin, net margin, capex, capex/sales, free cash flow, FCF conversion (FCF/EBITDA), dividends, buybacks, total shareholder payout, payout ratio, ROIC, ROE. For Bimbo also give the same by segment (North America, Mexico, Latin America, Europe/Asia/Africa): sales, EBITDA, EBITDA margin, last 5 FY + LTM.

BLOCK E — Bimbo debt and financing (pillar: debt management)
1. Debt stack: every outstanding bond, loan and private placement. Columns: instrument, issuer entity, currency, notional (original and USD), coupon type and rate, issue date, maturity date, call features, rating, current yield to maturity and spread, listing/ISIN.
2. Maturity ladder by year for the next 10 years, in local currency and USD, and the cash on hand covering each year.
3. Debt by currency (USD/MXN/EUR/other), by fixed vs floating, and the average life and average cost.
4. Quarterly net debt, EBITDA and net debt/EBITDA for the last 20 quarters, and the date and quote where management states a leverage target or range.
5. Hedging: cross-currency swaps, interest-rate swaps and commodity hedges: notional, maturity, fair value, and the net-investment hedge position, from the latest annual report and the last 4 quarterly reports.
6. Covenants and any change-of-control clauses disclosed in bond documents or the annual report.
7. Every debt issuance, tender offer or repayment announced since 2020: date, amount, use of proceeds, price/yield.
8. Use of cash: capex, dividends, buybacks and acquisitions for the last 10 years, and the share of operating cash flow each consumed.

BLOCK F — New CEO and management (pillar: new CEO)
1. Identify the current CEO and the appointment date, the predecessor, and the reason given for the change. Quote the press release.
2. CEO background: prior roles inside and outside Bimbo, years with the company, education, board seats.
3. All changes in top management (CEO, CFO, regional presidents, board chair) since 2020: person, role, start/end date, reason.
4. Stated priorities, strategy and targets since the new CEO took over (margin, capex, leverage, portfolio, M&A, capital returns). Quote each from earnings calls or releases, with date.
5. Guidance given vs. delivered, quarter by quarter, since the appointment (guidance item, value guided, outcome).
6. Compensation: CEO total compensation, its mix (fixed, annual bonus, long-term incentive), the metrics that drive the bonus, and ownership of shares by the CEO and top executives (percent, value).
7. Key developments tagged to management, restructuring, divestitures (e.g., sale of businesses) and strategy changes since the appointment, with date.
8. Same for the CEO or top management changes at Flowers, Gruma, Arca, and Yamazaki in the last 5 years, to compare transitions.

BLOCK G — Climate and commodities (pillar: climate change)
1. Bimbo: Scope 1, 2 and 3 emissions (tCO2e) for the last 5 years, emissions intensity, targets (SBTi status, net-zero year, interim targets), renewable energy share, water use and water-stress exposure, climate-related capex or spending, TCFD/ISSB disclosure, CDP climate and water scores, MSCI ESG rating, Sustainalytics risk score, S&P Global ESG score, and any carbon price or carbon tax cost disclosed.
2. The same metrics for the 9 peers where available (use S&P Global ESG data in Capital IQ).
3. Raw-material exposure: Bimbo's cost breakdown (wheat/flour, sugar, edible oils, packaging, energy, other), as percent of sales and of cost of goods sold, for the last 5 years; the volume of wheat purchased, the main origins (US, Canada, Mexico, Argentina, Black Sea), and the disclosed hedging policy: percent of the next 12 months hedged and instruments used.
4. Management's own estimate or sensitivity of climate or commodity events (drought, flooding, heat, wheat price shocks) on cost or margin. Quote it, with date.
5. Key developments or transcript mentions of weather, drought, crop failures, heat, hurricanes or climate in Bimbo's markets since 2020, with date and quantified impact if given.
6. Commodity and FX series, monthly for the last 10 years and the current forward curve: CBOT wheat, Kansas City wheat, sugar No. 11, soybean oil, palm oil, natural gas (Henry Hub), diesel, USD/MXN, USD/BRL, USD/EUR. Add the correlation of Bimbo's gross margin with wheat prices over the last 10 years (state the method).
7. Carbon regulation, packaging or climate-related taxes in Mexico, the US, Canada, Europe and Brazil that management or analysts flag as material.

BLOCK H — Valuation inputs and consensus
1. Beta (2y weekly and 5y monthly) of Bimbo and each peer against the local index and against the S&P 500; adjusted beta; unlevered beta using each company's own debt/equity and tax rate.
2. Risk-free rates: UST 10y and 20y, Mexico M-Bono 10y and 20y, Eurozone 10y; Mexico country risk premium or EMBI spread; Mexico 5y CDS; Mexico and US inflation expectations.
3. Bimbo cost of debt: yield to maturity of its longest USD bond and MXN bond, with the matching sovereign spread.
4. Consensus for Bimbo and the 4 core peers: sales, EBITDA, EBIT, EPS, FCF, DPS, capex, net debt, for FY26E-FY28E; number of analysts; high, low, mean, median; and the change in the mean over the last 1, 3 and 6 months.
5. Bimbo target price: mean, median, high, low; buy/hold/sell counts; the list of brokers with their rating, target and date.
6. Last 20 broker notes on Bimbo: broker, date, rating, target price, and the main thesis in one sentence each, quoted.

BLOCK I — Ownership and M&A
1. Top 15 shareholders of Bimbo with percent held, and the controlling family or group with its vehicles (e.g., Normaciel). Same for the controlling holders of Gruma, Arca Continental, Lala (if still covered) and Nutresa, with percent.
2. Insider transactions at Bimbo in the last 3 years.
3. M&A: the Wickbold (Brazil) acquisition and the sale of Nutrella, Bimbo's purchase of Nutresa's 39.99% stake in Bimbo Colombia, and every Bimbo acquisition or divestiture since 2019. Columns: date, target, stake, transaction value, EV, EV/EBITDA and EV/Sales if available, financing (cash, debt), and the source.
4. Sector M&A 2024-26 in bakery and snacks: Mars-Kellanova, Ferrero-WK Kellogg, Flowers-Simple Mills, Smucker-Hostess brand sales; with the same columns.

BLOCK J — Market shares and industry context (quote-only; do not infer)
Search company documents, transcripts, broker research and industry reports in Capital IQ for explicit market-share or ranking statements and list each with document, date and page:
- Bimbo / BBU share in US packaged bread, buns, sweet baked goods, snack cakes, and salty snacks (Circana or NielsenIQ), and Barcel USA's rank in salty snacks.
- Mexico: Bimbo, Sabritas (PepsiCo), Gamesa, Bokados (Arca), Barcel shares in packaged bread, pastries, cookies and salty snacks (Nielsen, Euromonitor, Kantar), and total market size in US$ with the definition.
- Brazil, Colombia, Argentina, Spain, UK: shares of Bimbo and the main competitors.
- Private label share in US packaged bread (dollars and units).
- Any statement about the effect of GLP-1 drugs, the IEPS tax in Mexico (current rate and any proposed change for 2027), NOM-051 labeling, US Section 301 or other tariffs, and the 40-hour work week in Mexico on bakery or snacks, with date and speaker.

OUTPUT ORDER
Return Blocks A to J in order. After each block, add "Gaps in this block" listing what was not found. End with a single "Master gaps list" and a "Data conflicts" list.
```

---

## 2. Short PREAMBLE (use when sending one block at a time)

```text
Context: CFA Research Challenge on Grupo Bimbo (BMV:BIMBOA). Public information only. Use only Capital IQ data. Return markdown tables with units, Source, As-of date and a label (Reported / CIQ-standardized / Consensus / Calculated). Never estimate; write N/A if absent and say where you looked. List what you could not retrieve at the end. Universe: Bimbo (BMV:BIMBOA); core peers Flowers (NYSE:FLO), Gruma (BMV:GRUMAB), Yamazaki (TSE:2212), Aryzta (SWX:ARYN); secondary SJM, CPB, MDLZ, Arca Continental (BMV:AC), PepsiCo (PEP); reference Nutresa. Now run:
```

Then paste one block (A–J) after it.

## 3. When the answers come back

- Paste the output into a new file under `raw/` (we do not edit `raw/`; the team adds it). I will compile it into `wiki/` with `[sourced]` tags and update `docs/context/todo.md`.
- The first thing I compute: the leverage table in Block B, to confirm or refute "2x the debt of the competition" before the thesis is locked.
