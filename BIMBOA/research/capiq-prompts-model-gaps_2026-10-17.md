# Capital IQ prompts to complete the model (2026-10-17)

Seven separate prompts, one topic each, every one under 5,000 characters. Run them one at a time in the Capital IQ AI assistant and paste each answer back. Prompts 5 and 6 replace the single prompt in `capiq-prompt-peer-market-data_2026-10-17.md`.

| # | Side | Topic | Feeds | Moves the value? |
|---|---|---|---|---|
| 1 | Bimbo | Betas and monthly price history | Unlevered beta, the largest WACC lever | Yes |
| 2 | Bimbo | Government yields, CDS, FX | Risk-free rate, currency consistency | Yes |
| 3 | Bimbo | Bonds, shares, buybacks, dividends | Cost of debt, share count, distributions | Slightly |
| 4 | Peers | Balance-sheet items for Yamazaki, Aryzta, Arca; Gruma consensus | Peer EV, bakery median | Exit multiple |
| 5 | Peers | Market data | Template, PeerAnalysis | No |
| 6 | Peers | Gross profit and consensus | Template | No |
| 7 | Peers | Capital intensity benchmark | Terminal capex and return on new capital | Yes |

Known problem: in the earlier pulls the BMV tickers resolved to the wrong entities (Bimbo as "Bmvb Immo", Gruma as "Bevgru Ab", Arca as "AON"). Each prompt names the entity. If it still fails, use the Capital IQ Excel plugin.

## Prompt 1 - Bimbo: betas and monthly prices

```text
CFA Research Challenge - Grupo Bimbo. Pricing date: 16-Oct-2026. Return values exactly as shown in S&P Capital IQ, with the field name, benchmark index, frequency, window and as-of date. Write N/A when a value is not available; never estimate or compute your own.

Resolve each company by full name if the ticker fails, and state the entity used (name, country, exchange). Grupo Bimbo is "Grupo Bimbo, S.A.B. de C.V." (Mexico, Bolsa Mexicana de Valores, ticker BIMBO A), not "Bmvb Immo".

TASK 1A - Betas. For each company return the 5-year beta, 2-year beta and 1-year beta (Capital IQ defaults), the benchmark index used, the R-squared if shown and the number of observations:
1 Grupo Bimbo (BMV:BIMBO A)
2 Flowers Foods (NYSE:FLO)
3 Gruma, S.A.B. de C.V. (BMV:GRUMA B, Mexico)
4 Yamazaki Baking (TSE:2212)
5 ARYZTA AG (SWX:ARYN)
6 J. M. Smucker (NYSE:SJM)
7 Campbell's (NasdaqGS:CPB)
8 Mondelez (NasdaqGS:MDLZ)
9 Arca Continental (BMV:AC, Mexico, not AON)
10 PepsiCo (NasdaqGS:PEP)

TASK 1B - Month-end closing prices for Grupo Bimbo and the S&P/BMV IPC index (Mexico), from 30-Sep-2021 to 16-Oct-2026 (last row = 16-Oct-2026). Columns: date, BIMBO A close (MXN; say whether it is adjusted for splits and dividends), IPC close. One row per month.

TASK 1C - Grupo Bimbo price statistics at 16-Oct-2026: close, 52-week high and low (with dates), and price change % over 1 day, 1 year, 2 years, 3 years, 5 years, quarter-to-date and year-to-date.

Output: one markdown table per task, then a list of anything not retrieved.
```

## Prompt 2 - Bimbo: government yields, CDS, FX

```text
CFA Research Challenge - Grupo Bimbo, discount-rate inputs. Pricing date: 16-Oct-2026 (if a series has no value that day, use the latest close and state the date). Return values exactly as shown in S&P Capital IQ with the series name, date and unit. Write N/A when a value is not available; never estimate.

TASK 2A - Government yields (%): Mexico M-Bono (MXN fixed-rate) 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y; Mexico Udibono (inflation-linked) real yield 10Y; US Treasury 2Y, 5Y, 10Y, 30Y; Canada government 10Y; Spain government 10Y; Brazil local-currency government 10Y; Germany Bund 10Y.

TASK 2B - Credit and policy: Mexico 5Y sovereign CDS (USD, bp) and 10Y CDS if available; Mexico USD sovereign bond (UMS) 10Y yield; Banxico target rate; TIIE 28-day; Mexico CPI year-over-year (latest month, with the month); US CPI year-over-year (latest month).

TASK 2C - FX: USD/MXN spot at 16-Oct-2026; USD/MXN 1-year, 5-year and 10-year forward rates or forward points (N/A if Capital IQ has none); the 12-month average USD/MXN.

Output: one markdown table per task (series, value, unit, date, source), then a list of anything not retrieved.
```

## Prompt 3 - Bimbo: bonds, shares, buybacks, dividends

```text
CFA Research Challenge - Grupo Bimbo, capital structure. Pricing date: 16-Oct-2026. Entity: "Grupo Bimbo, S.A.B. de C.V." (Mexico, BMV ticker BIMBO A), not "Bmvb Immo". State the entity you used. Write N/A when a value is not available; never estimate.

TASK 3A - Outstanding debt securities of Grupo Bimbo and its guaranteed subsidiaries (for example Bimbo Bakeries USA). One row per security: ISIN or CUSIP, issuer, currency, coupon (%), maturity date, amount outstanding (currency millions), clean price, yield to maturity (%), spread to the benchmark government curve (bp), and the current S&P and Fitch ratings, as of 16-Oct-2026.

TASK 3B - Shares: shares outstanding at the latest date (basic and diluted), treasury shares and repurchase fund, free float %, with the date of each figure. Share repurchases between 01-Jul-2026 and 16-Oct-2026: number of shares and amount (MXN millions) if shown.

TASK 3C - Dividends per share, declared and paid, for 2023, 2024, 2025 and 2026 year to date: declaration date, ex-date, payment date, amount per share (MXN), and any approved annual buyback ceiling.

Output: three markdown tables, then a list of anything not retrieved.
```

## Prompt 4 - Peers: balance-sheet items for enterprise value

```text
CFA Research Challenge - bakery peers, balance-sheet items for enterprise value. Use the latest reported balance sheet of each company and give the balance sheet date, reporting currency and accounting standard (IFRS or J-GAAP). Write N/A when a value is not available; never estimate. If a ticker fails, search by full name and state the entity used.

Companies: Yamazaki Baking Co., Ltd. (TSE:2212); ARYZTA AG (SWX:ARYN); Arca Continental, S.A.B. de C.V. (BMV:AC, Mexico, not "AON"); Gruma, S.A.B. de C.V. (BMV:GRUMA B, Mexico, not "Bevgru Ab").

TASK 4A - For each company, in reporting-currency millions: shares outstanding (basic and diluted, millions); short-term borrowings; current portion of long-term debt; long-term debt; lease liabilities split current and non-current (for J-GAAP, lease obligations or operating-lease commitments if reported); finance leases; cash and short-term investments; minority interest at book value; total debt and net debt as Capital IQ defines them; market cap and enterprise value in local currency and in USD.

TASK 4B - For each company, last twelve months and the last two fiscal years: EBITDA as Capital IQ defines it; depreciation and amortization, with the depreciation of right-of-use assets shown separately if reported; revenue; net income; diluted EPS.

TASK 4C - Gruma only: analyst consensus mean EBITDA, revenue and EPS for the next three fiscal years (say which fiscal year each is), with the number of analysts.

Output: one markdown table per task, then a list of anything not retrieved.
```

## Prompt 5 - Peers: market data

```text
CFA Research Challenge - bakery and packaged-food peers, market data. Pricing date: 16-Oct-2026. Local trading currency unless stated. Write N/A when a value is not available; never estimate. If a ticker fails, search by full name and state the entity used.

Companies: Flowers Foods (NYSE:FLO); Gruma, S.A.B. de C.V. (BMV:GRUMA B, Mexico); Yamazaki Baking (TSE:2212); ARYZTA AG (SWX:ARYN); J. M. Smucker (NYSE:SJM); Campbell's (NasdaqGS:CPB); Mondelez (NasdaqGS:MDLZ); Arca Continental (BMV:AC, Mexico, not "AON"); PepsiCo (NasdaqGS:PEP).

One table, one row per company, columns: close price on 16-Oct-2026; 52-week high; 52-week low; price change % over 1 day, 1 year, 2 years, 3 years, 5 years, quarter-to-date and year-to-date; dividends per share for the last 12 months; dividends per share FY2024; dividends per share FY2025; shares outstanding (millions); market cap (USD millions).

Then list anything not retrieved.
```

## Prompt 6 - Peers: gross profit and consensus

```text
CFA Research Challenge - bakery and packaged-food peers, gross profit and consensus. Capital IQ standardized figures in USD millions unless stated. Write N/A when a value is not available; never estimate. If a ticker fails, search by full name and state the entity used.

Companies: Flowers Foods (NYSE:FLO); Gruma, S.A.B. de C.V. (BMV:GRUMA B, Mexico); Yamazaki Baking (TSE:2212); ARYZTA AG (SWX:ARYN); J. M. Smucker (NYSE:SJM); Campbell's (NasdaqGS:CPB); Mondelez (NasdaqGS:MDLZ); Arca Continental (BMV:AC, Mexico, not "AON"); PepsiCo (NasdaqGS:PEP).

TASK 6A - Gross profit for FY2024, FY2025 and the last twelve months (state the LTM end date). One row per company.

TASK 6B - Consensus mean estimates for the next three fiscal years (say which fiscal year each column is): gross margin %, free cash flow, and dividends per share, with the number of analysts.

Output: one table per task, then a list of anything not retrieved.
```

## Prompt 7 - Peers: capital intensity benchmark

```text
CFA Research Challenge - capital intensity benchmark for Grupo Bimbo and its peers. Capital IQ standardized figures in USD millions unless stated. Write N/A when a value is not available; never estimate. If a ticker fails, search by full name and state the entity used.

Companies: Grupo Bimbo (BMV:BIMBO A, Mexico, not "Bmvb Immo"); Flowers Foods (NYSE:FLO); Gruma, S.A.B. de C.V. (BMV:GRUMA B, Mexico); Yamazaki Baking (TSE:2212); ARYZTA AG (SWX:ARYN); J. M. Smucker (NYSE:SJM); Campbell's (NasdaqGS:CPB); Mondelez (NasdaqGS:MDLZ); Arca Continental (BMV:AC, Mexico, not "AON"); PepsiCo (NasdaqGS:PEP).

TASK 7A - For FY2021, FY2022, FY2023, FY2024, FY2025 and the last twelve months, one table per metric, one row per company: capital expenditures; depreciation and amortization (total, and the depreciation of right-of-use assets separately if reported); revenue.

TASK 7B - Consensus mean capital expenditures and consensus revenue for the next three fiscal years (say which fiscal year each column is), with the number of analysts.

Output: markdown tables, then a list of anything not retrieved.
```
