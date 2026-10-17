# Capital IQ prompts (each under 5,000 characters)

Paste the HEADER first, then ONE task below it. Seven tasks, in this order of priority: 1, 3, 4, 5, 2, 6, 7.

## HEADER (paste before every task)

```text
CONTEXT: CFA Research Challenge on Grupo Bimbo, S.A.B. de C.V. Public information only. Use ONLY Capital IQ data (financials, filings, transcripts, key developments, broker research, S&P ESG).
RULES: Markdown tables, units in column headers, ISO dates. Add columns Source (CIQ item, or document+date+page) and As-of date. Label each number Reported / CIQ-standardized / Consensus / Calculated (show formula). Never estimate or use memory: write N/A and say where you looked. Show local currency and USD, fiscal year-end, and the LTM quarter. If sources conflict, show both. Quote text in max 25 words with document, date, page. End with a list of what you could not retrieve.
UNIVERSE (if a ticker does not resolve, search by name and tell me which identifier you used):
0 Grupo Bimbo BMV:BIMBOA (TARGET) | 1 Flowers Foods NYSE:FLO | 2 Gruma BMV:GRUMAB | 3 Yamazaki Baking TSE:2212 | 4 Aryzta SWX:ARYN | 5 J.M. Smucker NYSE:SJM | 6 Campbell's NasdaqGS:CPB | 7 Mondelez NasdaqGS:MDLZ | 8 Arca Continental BMV:AC | 9 PepsiCo NasdaqGS:PEP | R Grupo Nutresa BVC:NUTRESA (reference only).
Companies 1-4 = "core peers"; 5-9 = "secondary peers".
```

## TASK 1 — Market data and leverage

```text
TASK 1 of 7: MARKET DATA AND LEVERAGE (question: does Bimbo have 2x the debt of its peers?)
A. For companies 0-9 and R, latest close (give the date): price, diluted shares, market cap, total debt incl. leases, cash and ST investments, net debt, minority interest, EV, LTM revenue, EBITDA, EBIT, fiscal year-end, currency.
B. For companies 0-9, last 5 fiscal years + LTM: total debt, net debt, EBITDA; net debt/EBITDA, total debt/EBITDA, net debt/EV, debt/total capital, debt/equity; EBITDA/interest, EBIT/interest, FFO/total debt; average cost of debt; effective tax rate; share of debt by currency (USD/local/EUR) and fixed vs floating where disclosed; ratings S&P, Moody's, Fitch (current, outlook, every change in the last 10 years with date).
C. Summary table: rank the 10 companies by LTM net debt/EBITDA; median and mean for core peers (1-4) and for all peers (1-9); Bimbo's ratio divided by each median. Repeat on a total-debt basis and on a net debt + leases basis, since the answer may change with the definition.
```

## TASK 2 — Multiples and operations

```text
TASK 2 of 7: MULTIPLES AND OPERATING COMPARISON
A. Multiples for companies 0-9, all on the same date: EV/EBITDA (LTM and NTM), EV/EBIT, EV/Sales, P/E (LTM, NTM), P/FCF, FCF yield, dividend yield; 5y and 10y average and median of EV/EBITDA and P/E. Show Bimbo's premium/discount vs each peer and vs the core-peer median, today and vs the 5y/10y averages.
B. Operations for companies 0-9, last 5 FY + LTM + consensus FY26E-FY28E: revenue, organic or ex-FX growth, gross, EBITDA, EBIT and net margins, capex, capex/sales, free cash flow, FCF/EBITDA, dividends, buybacks, payout ratio, ROIC, ROE.
C. Bimbo by segment (North America, Mexico, Latin America, Europe/Asia/Africa), last 5 FY + LTM: sales, EBITDA, EBITDA margin, ex-FX growth.
```

## TASK 3 — Bimbo debt and financing

```text
TASK 3 of 7: GRUPO BIMBO (BMV:BIMBOA) DEBT AND FINANCING
1. Debt stack: every outstanding bond, loan and private placement. Columns: instrument, issuer entity, currency, notional (original and USD), coupon type and rate, issue date, maturity, call features, rating, current yield to maturity, spread, ISIN.
2. Maturity ladder for the next 10 years in local currency and USD, versus cash on hand.
3. Debt by currency (USD/MXN/EUR/other), fixed vs floating, average life, average cost.
4. Net debt, EBITDA and net debt/EBITDA for the last 20 quarters. Quote where management states a leverage target or range (date, speaker).
5. Hedging from the latest annual report and last 4 quarterly reports: cross-currency swaps, interest-rate swaps, commodity hedges, net-investment hedge. Notional, maturity, fair value.
6. Covenants and change-of-control clauses in bond documents or the annual report.
7. Every issuance, tender offer or repayment announced since 2020: date, amount, use of proceeds, price/yield.
8. Use of cash for the last 10 years: capex, dividends, buybacks, acquisitions, and each as a share of operating cash flow.
```

## TASK 4 — New CEO and management

```text
TASK 4 of 7: NEW CEO AND MANAGEMENT
1. Who is the current CEO of Grupo Bimbo (BMV:BIMBOA)? Appointment date, predecessor, reason for the change. Quote the press release.
2. CEO background: prior roles inside and outside Bimbo, years at the company, education, board seats.
3. Every change in top management (CEO, CFO, regional presidents, board chair) since 2020: person, role, start/end date, reason.
4. Priorities and targets stated since the CEO took over (margin, capex, leverage, portfolio, M&A, capital returns). Quote each from calls or releases with date.
5. Guidance given vs delivered, quarter by quarter, since the appointment.
6. CEO total compensation and its mix (fixed, annual bonus, long-term incentive), the metrics that drive the bonus, and share ownership by the CEO and top executives (percent, value).
7. Key developments since the appointment: restructurings, divestitures, strategy changes, with date.
8. Same facts (items 1 and 3 only) for Flowers Foods (NYSE:FLO), Gruma (BMV:GRUMAB), Arca Continental (BMV:AC) and Yamazaki Baking (TSE:2212) over the last 5 years.
```

## TASK 5 — Climate and commodities

```text
TASK 5 of 7: CLIMATE AND COMMODITIES
1. Grupo Bimbo (BMV:BIMBOA), last 5 years: Scope 1, 2, 3 emissions (tCO2e), intensity, targets (SBTi status, net-zero year, interim), renewable energy share, water use and water-stress exposure, climate capex, TCFD/ISSB disclosure, CDP climate and water scores, MSCI ESG rating, Sustainalytics risk score, S&P Global ESG score, any carbon cost disclosed.
2. The same metrics for companies 1-9, where available (use S&P Global ESG data).
3. Bimbo raw-material exposure, last 5 years: cost breakdown (wheat/flour, sugar, edible oils, packaging, energy, other) as % of sales and % of cost of goods sold; wheat volume bought, main origins; hedging policy: % of next 12 months hedged and instruments.
4. Management's own sensitivity of cost or margin to climate or commodity events (drought, flooding, heat, wheat shocks). Quote with date.
5. Key developments and transcript mentions of weather, drought, crop failure, heat, hurricanes or climate in Bimbo's markets since 2020, with date and quantified impact.
6. Monthly series for 10 years plus the current forward curve: CBOT wheat, KC wheat, sugar No. 11, soybean oil, palm oil, Henry Hub gas, diesel, USD/MXN, USD/BRL, USD/EUR. Correlation of Bimbo's gross margin with wheat over 10 years (state the method).
7. Carbon, packaging or climate taxes in Mexico, US, Canada, Europe, Brazil that management or analysts flag as material.
```

## TASK 6 — Valuation inputs, consensus, ownership, M&A

```text
TASK 6 of 7: VALUATION INPUTS, CONSENSUS, OWNERSHIP AND M&A
1. Beta (2y weekly, 5y monthly) of companies 0-9 vs local index and vs S&P 500; adjusted beta; unlevered beta using each company's own debt/equity and tax rate.
2. Risk-free and country risk: UST 10y and 20y, Mexico M-Bono 10y and 20y, Eurozone 10y; Mexico EMBI spread and 5y CDS; Mexico and US inflation expectations.
3. Bimbo yield to maturity of its longest USD and MXN bonds, with the sovereign spread.
4. Consensus for Bimbo and core peers (1-4), FY26E-FY28E: sales, EBITDA, EBIT, EPS, FCF, DPS, capex, net debt; analyst count, high/low/mean/median; change in the mean over 1, 3, 6 months.
5. Bimbo target price (mean, median, high, low), buy/hold/sell counts, and the last 20 broker notes: broker, date, rating, target, thesis in one quoted sentence.
6. Top 15 holders of Bimbo with % and the controlling family vehicles (e.g., Normaciel). Controlling holders of Gruma, Arca Continental, Lala (if covered) and Nutresa with %. Bimbo insider transactions, last 3 years.
7. M&A with date, target, stake, value, EV, EV/EBITDA, EV/Sales, financing, source: Bimbo's Wickbold purchase and Nutrella sale; Bimbo's purchase of Nutresa's 39.99% of Bimbo Colombia; every Bimbo deal since 2019; sector deals 2024-26 (Mars-Kellanova, Ferrero-WK Kellogg, Flowers-Simple Mills, Smucker-Hostess brand sales).
```

## TASK 7 — Market shares and industry context

```text
TASK 7 of 7: MARKET SHARES AND INDUSTRY CONTEXT (quote only; do not infer)
Search company documents, transcripts, broker research and industry reports for explicit share or ranking statements. For each: quote, document, date, page, data provider (Circana, NielsenIQ, Euromonitor, Kantar).
- Bimbo / BBU share in US packaged bread, buns, sweet baked goods, snack cakes and salty snacks; Barcel USA's rank in salty snacks.
- Mexico: shares of Bimbo, Sabritas (PepsiCo), Gamesa (PepsiCo), Bokados (Arca Continental) and Barcel in packaged bread, pastries, cookies, salty snacks; Mexico market size in US$ with its definition.
- Brazil, Colombia, Argentina, Spain, UK: shares of Bimbo and main competitors.
- Private label share in US packaged bread (dollars and units).
- Statements on the effect of GLP-1 drugs, Mexico's IEPS tax (current rate, any proposed 2027 change), NOM-051 labeling, US Section 301 and other tariffs, and Mexico's 40-hour work week on bakery or snacks, with date and speaker.
```
