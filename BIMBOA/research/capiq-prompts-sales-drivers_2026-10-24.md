# Capital IQ prompts: sales drivers by region (2026-10-24)

Purpose: collect the data needed to choose, with evidence, the variable and the ratio that drive Grupo Bimbo's organic net sales by region in FY2027E-FY2030E (advisor feedback, `docs/context/memory.md` 2026-10-24). Nothing is chosen until these answers are back.

Four prompts, one topic each, every one under 5,000 characters. Run them one at a time in the Capital IQ AI assistant and paste each answer back as a file in `data/capitaliq/` (name: `capiq-sales-drivers-<N>_<date>.md`).

| # | Topic | What it lets us test |
|---|---|---|
| 1 | Macro, Mexico + North America + Latin America countries | Which variable tracks Bimbo's ex-FX growth best (nominal GDP, consumption, food prices) |
| 2 | Macro, EAA countries | Same, for Europe, Asia and Africa |
| 3 | Exchange rates | Translation of each region into MXN, history and forecast |
| 4 | Bimbo by region, acquisitions, peers, industry | Organic growth history and the industry reference |

Known problems from the 2026-10-17 pulls (`data/capitaliq/capiq-ai-model-gaps-2_2026-10-17.md`): every USD/MXN query returned ALL_ENTITIES_UNRESOLVED; CPI came back with "As reported ACTUAL" and "Standardized FORECAST" flags (keep that flag); BMV tickers resolved to wrong entities (name Grupo Bimbo in full). If the AI fails on a series, the Capital IQ Excel plug-in or the Economic Data screen are the fallback.

Output layout asked in every prompt (long format, one value per row, so it loads straight into Python or Excel):

`country_iso3 | bimbo_region | indicator | unit | currency | year_or_period | value | value_type (Actual / Forecast) | provider | series_name_in_CIQ | as_of_date`

## Prompt 1 - Macro: Mexico, North America, Latin America

```text
CFA Research Challenge - Grupo Bimbo, sales drivers. Public data only. Return values exactly as shown in S&P Capital IQ (economic data, S&P Global Market Intelligence forecasts). Never estimate, interpolate or average yourself: write N/A and say where you looked. Do not round: give all decimals shown.

COUNTRIES (ISO3, Bimbo region): MEX Mexico; USA, CAN North America; ARG, BRA, CHL, COL, CRI, ECU, SLV, GTM, HND, NIC, PAN, PRY, PER, URY, VEN Latin America.

PERIOD: annual 2015-2025 actuals, 2026 latest estimate, 2027-2030 forecasts. Mark each value Actual or Forecast exactly as Capital IQ flags it, and give the forecast provider and its vintage date.

INDICATORS (one row per country-indicator-year):
1 Real GDP growth, % y/y
2 Nominal GDP, local currency, level (state the unit, e.g. billions)
3 Nominal GDP growth, local currency, % y/y
4 CPI inflation, annual average, % y/y
5 CPI inflation, December over December, % y/y
6 CPI food and non-alcoholic beverages, annual average, % y/y
7 CPI bread and cereals, annual average, % y/y (N/A if not available)
8 Household final consumption expenditure, nominal, local currency, % y/y
9 Household final consumption expenditure, real, % y/y
10 Retail sales value, % y/y (and real if available)
11 Population, % y/y

OUTPUT: one long table with columns: country_iso3 | bimbo_region | indicator | unit | currency | year | value | value_type (Actual/Forecast) | provider | series_name_in_CIQ | as_of_date.
Then a coverage matrix: rows = countries, columns = indicators 1-11, cell = first year-last year available or N/A.
Then a list of every series you could not retrieve and the identifiers you tried.
For Argentina and Venezuela, say whether the CPI series is official or alternative and flag hyperinflation years.
```

## Prompt 2 - Macro: Europe, Asia and Africa (EAA)

```text
CFA Research Challenge - Grupo Bimbo, sales drivers. Public data only. Return values exactly as shown in S&P Capital IQ (economic data, S&P Global Market Intelligence forecasts). Never estimate, interpolate or average yourself: write N/A and say where you looked. Do not round: give all decimals shown.

COUNTRIES (ISO3, all in Bimbo's EAA region): ESP Spain, PRT Portugal, FRA France, ITA Italy, GBR United Kingdom, CHE Switzerland, ROU Romania, SRB Serbia, SVN Slovenia, HRV Croatia, MNE Montenegro, MKD North Macedonia, RUS Russia, UKR Ukraine, TUR Turkey, CHN China, IND India, KOR South Korea, KAZ Kazakhstan, ZAF South Africa, MAR Morocco, TUN Tunisia. Also the aggregates Euro Area and European Union if available.

PERIOD: annual 2015-2025 actuals, 2026 latest estimate, 2027-2030 forecasts. Mark each value Actual or Forecast exactly as Capital IQ flags it, and give the forecast provider and its vintage date.

INDICATORS (one row per country-indicator-year):
1 Real GDP growth, % y/y
2 Nominal GDP, local currency, level (state the unit)
3 Nominal GDP growth, local currency, % y/y
4 CPI inflation, annual average, % y/y
5 CPI inflation, December over December, % y/y
6 CPI food and non-alcoholic beverages, annual average, % y/y
7 CPI bread and cereals, annual average, % y/y (N/A if not available)
8 Household final consumption expenditure, nominal, local currency, % y/y
9 Household final consumption expenditure, real, % y/y
10 Retail sales value, % y/y (and real if available)
11 Population, % y/y

OUTPUT: one long table with columns: country_iso3 | bimbo_region | indicator | unit | currency | year | value | value_type (Actual/Forecast) | provider | series_name_in_CIQ | as_of_date.
Then a coverage matrix: rows = countries, columns = indicators 1-11, cell = first year-last year available or N/A.
Then a list of every series you could not retrieve and the identifiers you tried.
Flag Turkey, Russia and Ukraine years with inflation above 20%.
```

## Prompt 3 - Exchange rates

```text
CFA Research Challenge - Grupo Bimbo, currency translation. Public data only. Return values exactly as shown in S&P Capital IQ. Never estimate or compute cross rates yourself unless asked, and then show the formula. Write N/A and say where you looked.

Last time every "USD/MXN" query failed with ALL_ENTITIES_UNRESOLVED. Try, in this order, and report which identifier worked: "Mexican Peso per US Dollar", "USD/MXN", "USDMXN", "MXN=X", "US Dollar to Mexican Peso exchange rate", the Capital IQ currency code MXN against USD, and the S&P Global Market Intelligence exchange-rate forecast series for Mexico.

CURRENCIES (all quoted as local currency per 1 US dollar): MXN, CAD, BRL, ARS, CLP, COP, PEN, UYU, PYG, GTQ, HNL, CRC, NIO, EUR, GBP, CHF, RON, RSD, TRY, RUB, UAH, CNY, INR, KRW, KZT, ZAR, MAD, TND. (USD-based economies need no rate: Ecuador, El Salvador, Panama.)

TASK 3A - History, 2015-2025: annual average rate and year-end (31-Dec) rate, per currency per year.
TASK 3B - 2026: monthly average and month-end rate, January 2026 to the latest month, plus the latest daily close with its date.
TASK 3C - Forecasts 2026-2030: annual average and year-end forecast per currency, with provider and vintage date. If Capital IQ has no forecast for a currency, write N/A.
TASK 3D - USD/MXN only: forward rates or forward points for 1, 2, 3, 4 and 5 years at the latest date, and the 2026 year-to-date average.

OUTPUT: one long table with columns: currency | rate_type (annual_avg / year_end / month_avg / month_end / daily_close / forecast_avg / forecast_year_end / forward) | period | value (local per USD) | value_type (Actual/Forecast/Forward) | provider | series_name_in_CIQ | as_of_date.
Then a coverage matrix: rows = currencies, columns = 3A avg, 3A year-end, 3B, 3C, 3D, cell = available or N/A.
Then the list of identifiers tried for anything not retrieved.
```

## Prompt 4 - Bimbo by region, acquisitions, peers and industry

```text
CFA Research Challenge - Grupo Bimbo, organic growth. Entity: "Grupo Bimbo, S.A.B. de C.V." (Mexico, BMV ticker BIMBO A), not "Bmvb Immo"; state the entity used. Public data only. Use Capital IQ financials, filings, transcripts, key developments and transaction records. Never estimate: write N/A and say where you looked. Quote text in max 25 words with document, date and page.

TASK 4A - Bimbo segments, quarterly 1Q2019 to 3Q2026: net sales in MXN for North America, Mexico, Latin America, EAA, eliminations and consolidated; and the % growth excluding FX for each region as reported in each earnings release.
TASK 4B - Any Bimbo disclosure, 2019-2026, of organic vs inorganic growth, contribution of acquisitions to sales, or sales by country (e.g. US, Canada, Brazil, Spain, UK, Romania, India, China, Argentina). Quote the exact text with document, date and page.
TASK 4C - For each acquisition below, from Capital IQ transaction records or target company profiles: closing date, target revenue (latest annual and LTM at announcement, currency, year), deal value, EV/revenue, source. Vel Pitar (Romania, 2023), Natural Bakery (Canada, 2023), Mile Hi Bakery (US, 2023), Fortisa AG (Switzerland, 2023), Amaritta Food (Spain, 2023), Trei Brutari (Romania, 2024), Moulin d'Or (Tunisia, 2024), La Zarcerena (Costa Rica, 2024), Pagnifique (Uruguay, 2024), Karamolegos Bakery (Romania, 2025), Grupo Don Don (Serbia, 2025), Stone House Bread (US, 2025), Grupo Wickbold (Brazil, 2025), Bonel / Bonelle SARL (Tunisia or North Macedonia, 2026).
TASK 4D - Peers, annual 2019-2025 and 9M2026: organic growth (or growth ex-FX and ex-M&A) by geographic segment as reported, for Flowers Foods, Aryzta, Yamazaki Baking, Gruma, Mondelez, Grupo Nutresa (last available), plus any company Capital IQ lists as a packaged-bread competitor in Mexico, Brazil, Spain, Romania or the UK.
TASK 4E - Industry: market size and growth, value and volume, for packaged bread / bakery and for salty snacks, by country (US, Canada, Mexico, Brazil, Spain, UK, Romania, India, China), history 2019-2025 and forecasts to 2030, with provider and whether values are in local currency or USD, current or constant prices.

OUTPUT: one table per task. 4A long format: quarter | region | net_sales_mxn | growth_exfx_pct | source_document | page. 4C: one row per deal. 4D and 4E long format: company_or_country | segment | indicator | unit | currency | period | value | value_type | provider | as_of_date. End with the list of what you could not retrieve.
```

## Re-run 2026-10-24: gaps only, small blocks

Answers to prompts 1-4 are in `BIMBOA/research/Informacion_BIMBO_macro.txt` (Capital IQ data as of 2026-10-15). This section asks only for what is missing. Run one block per message; each block is small enough not to be cut off.

### What is missing and why

| Area | Missing | Cause | Re-run block |
|---|---|---|---|
| Macro, Americas | 2026-2030 forecasts for every country (real GDP, nominal GDP level, CPI) | Tool returned actuals only; it did return forecasts for Spain, so the series exist | M1-M4 |
| Macro, Americas | Real private consumption (ind. 9) and population growth (ind. 11), all countries | Said available, never output (answer cut off) | M1-M4 |
| Macro, Americas | CPI for GTM (blank), HND, NIC, PAN, PRY | Answer cut off at GTM | M3-M4 |
| Macro, Americas | PRY 2015-2018; PER, URY, VEN all data | Not returned | M4-M5 |
| Macro, EAA | GBR from 2024 (real GDP) and all its other indicators; CHE, ROU, SRB, SVN, HRV, MNE, MKD, RUS, UKR, TUR, KAZ, CHN, IND, KOR, ZAF, MAR, TUN all data | Answer cut off after Italy | E1-E5 |
| Macro, EAA | Nominal GDP growth rows flagged "D = Derived" (ESP, PRT, FRA, ITA, EU) | Computed by the Capital IQ AI, not a stored field. **Discarded**; we compute it ourselves from the stored levels and tag it [calc] | none |
| Macro, all | CPI Dec/Dec, CPI food, CPI bread and cereals, nominal household consumption, retail sales (ind. 5-8, 10) | Not held in the Capital IQ economic data tool | Field list in every M/E block; public sources otherwise (INEGI, BLS/FRED) |
| FX | 2015-2025 annual averages for CLP, COP, PYG, KRW marked "~" | Stored in thousands and multiplied by 1,000 (±0.5%): a conversion, not a stored value | F1 |
| FX | 2026 monthly values for KZT, TND, RSD | Banxico does not carry them | F2 |
| FX | USD/MXN forwards 1-5 years | Not in Capital IQ economic data; plug-in formula not found yet | none (Excel plug-in) |
| Bimbo segments | FY2018-FY2020 by region (no local 4Q18, 4Q19, 4Q20 releases); 3Q20, 3Q21 | Not in our `filings/quarterly/` | S1 |
| Bimbo segments | 1Q19-3Q26 quarters we already hold locally | Not needed from Capital IQ: our releases are the primary source; the Capital IQ answer had errors (1Q25 NA "-9%" vs -4.9% in the release) | none |
| Organic / acquisitions | Tasks 4B, 4C | Not answered | S2, S3, S4 |
| Peers, industry | Tasks 4D, 4E | Not answered | P1, P2, I1 |

Every prompt below opens with the same STRICT rule so the Capital IQ AI returns stored values only: no growth rates from levels, no averages, sums, unit conversions, inversions, cross rates or interpolation; N/A plus "not a stored field" when arithmetic would be needed; the Actual/Forecast flag exactly as shown. If an answer is about to be cut off, it must stop at a whole country and write `CONTINUE FROM <country>`.

### M1 - Mexico, United States, Canada

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels, no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: MEX, USA, CAN.
A) Years 2026-2030 only: realGDPGrowth, nominalGDPLCU, consumerPriceInflation. These are the forecast rows ("Standardized FORECAST"); the same tool returned them for Spain with as-of 10/15/2026. If they are not returned for these countries, say so explicitly.
B) Years 2015-2030: realPrivateConsumptionGrowth, populationGrowth.
C) List, names only (no values), every other economic field Capital IQ holds for each country, especially any food CPI, nominal private consumption or retail sales field.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. Then the field list. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### M2 - Argentina, Brazil, Chile, Colombia

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels, no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: ARG, BRA, CHL, COL.
A) Years 2026-2030 only: realGDPGrowth, nominalGDPLCU, consumerPriceInflation (forecast rows, "Standardized FORECAST"). If not returned, say so explicitly.
B) Years 2015-2030: realPrivateConsumptionGrowth, populationGrowth.
C) For ARG: state whether the CPI series is the official INDEC series or an alternative one, as labelled in Capital IQ.
D) List, names only, every other economic field Capital IQ holds for each country, especially any food CPI, nominal private consumption or retail sales field.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. Then the field list. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### M3 - Costa Rica, Ecuador, El Salvador, Guatemala

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels, no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: CRI, ECU, SLV, GTM.
A) Years 2026-2030 only: realGDPGrowth, nominalGDPLCU, consumerPriceInflation (forecast rows). If not returned, say so explicitly.
B) GTM only, years 2015-2025: consumerPriceInflation (it came back blank last time).
C) Years 2015-2030: realPrivateConsumptionGrowth, populationGrowth.
D) List, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. Then the field list. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### M4 - Honduras, Nicaragua, Panama, Paraguay

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels, no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: HND, NIC, PAN, PRY.
A) Years 2015-2030: consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
B) Years 2026-2030 only: realGDPGrowth, nominalGDPLCU (forecast rows). If not returned, say so explicitly.
C) PRY only, years 2015-2018: realGDPGrowth, nominalGDPLCU (the block started in 2019 last time; say whether Capital IQ holds earlier years).
D) List, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. Then the field list. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### M5 - Peru, Uruguay, Venezuela

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels, no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: Peru, Uruguay, Venezuela. Last time no data came back. Try, and report which identifier worked: ISO3 (PER, URY, VEN), ISO2 (PE, UY, VE), "Republic of Peru", "Oriental Republic of Uruguay", "Bolivarian Republic of Venezuela", "Venezuela, RB".
Years 2015-2030: realGDPGrowth, nominalGDPLCU, consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
For VEN: state whether the CPI series is official or alternative, as labelled.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. Then the identifiers tried and the result of each.
```

### E1 - United Kingdom, Switzerland, Romania, Serbia

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels (do not derive nominal GDP growth), no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: GBR, CHE, ROU, SRB.
Years 2015-2030 (actuals and the "Standardized FORECAST" rows): realGDPGrowth, nominalGDPLCU, consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
Then list, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### E2 - Slovenia, Croatia, Montenegro, North Macedonia

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels (do not derive nominal GDP growth), no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: SVN, HRV, MNE, MKD.
Years 2015-2030 (actuals and the "Standardized FORECAST" rows): realGDPGrowth, nominalGDPLCU, consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
Then list, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### E3 - Russia, Ukraine, Turkey, Kazakhstan

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels (do not derive nominal GDP growth), no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: RUS, UKR, TUR, KAZ.
Years 2015-2030 (actuals and the "Standardized FORECAST" rows): realGDPGrowth, nominalGDPLCU, consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
Then list, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### E4 - China, India, South Korea

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels (do not derive nominal GDP growth), no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: CHN, IND, KOR. For IND, state whether years are calendar or fiscal (April-March) as stored.
Years 2015-2030 (actuals and the "Standardized FORECAST" rows): realGDPGrowth, nominalGDPLCU, consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
Then list, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### E5 - South Africa, Morocco, Tunisia

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels (do not derive nominal GDP growth), no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the Actual/Forecast flag exactly as shown.
COUNTRIES: ZAF, MAR, TUN.
Years 2015-2030 (actuals and the "Standardized FORECAST" rows): realGDPGrowth, nominalGDPLCU, consumerPriceInflation, realPrivateConsumptionGrowth, populationGrowth.
Then list, names only, every other economic field Capital IQ holds for each country.
OUTPUT: long table country_iso3 | indicator | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```

### F1 - Exact FX averages (CLP, COP, PYG, KRW)

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data.
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no multiplying by 1,000, no averages of daily or monthly data, no inversions, no cross rates. If the stored value is in thousands, give it in thousands and say so.
CURRENCIES: CLP, COP, PYG, KRW, quoted as local currency per 1 US dollar.
Years 2015-2025: the stored annual average exchange rate (field averageExchangeRate or equivalent).
OUTPUT: currency | ciq_field_name | unit_as_stored | year | value | value_type_flag_as_shown | provider | as_of_date.
```

### F2 - 2026 monthly FX for KZT, TND, RSD

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ.
STRICT: return only values stored explicitly in Capital IQ, exactly as shown, all decimals. Do NOT calculate anything: no averages of daily data, no inversions, no cross rates. If a monthly average is not a stored field, write N/A.
CURRENCIES: KZT, TND, RSD, quoted as local currency per 1 US dollar.
January 2026 to the latest month: stored monthly average and stored month-end rate; plus the latest stored daily close with its date.
OUTPUT: currency | rate_type | period | value | value_type_flag_as_shown | provider | ciq_field_name | as_of_date.
```

### S1 - Bimbo by region, FY2018-FY2020 and two quarters

```text
CFA Research Challenge - Grupo Bimbo. Entity: "Grupo Bimbo, S.A.B. de C.V." (Mexico, BMV: BIMBO A). Public data only: earnings releases and filings in Capital IQ.
STRICT: return only figures printed in the document. Do NOT calculate anything: no sums, differences, growth rates or FX adjustments. If a figure is not printed, write N/A.
From the 4Q2018, 4Q2019 and 4Q2020 earnings releases: full-year and fourth-quarter net sales in MXN millions for North America, Mexico, Latin America, Europe/EAA (as named then), intercompany eliminations and consolidated; and the growth % excluding FX (or "constant currency") per region exactly as printed.
From the 3Q2020 and 3Q2021 earnings releases: the same figures for the quarter.
OUTPUT: period | region_as_named | net_sales_mxn_mm | growth_exfx_pct_as_printed | document | date | page.
```

### S2 - Organic vs inorganic disclosures

```text
CFA Research Challenge - Grupo Bimbo. Entity: "Grupo Bimbo, S.A.B. de C.V." (Mexico, BMV: BIMBO A). Public data only: earnings releases, annual reports, call transcripts and investor presentations in Capital IQ, 2019-2026.
STRICT: quote only text and figures printed in the document; do not calculate or estimate.
Find every disclosure of: organic vs inorganic growth; the contribution of acquisitions to net sales (in % or MXN); net sales by country (e.g. US, Canada, Brazil, Spain, UK, Romania, India, China, Argentina).
OUTPUT: one row per disclosure: period_referred | region_or_country | what_is_disclosed | figure_as_printed | exact quote (max 25 words) | document | date | page.
```

### S3 - Acquisitions 2023-2024 (target revenue)

```text
CFA Research Challenge - Grupo Bimbo. Public data only: Capital IQ transaction records and target company profiles.
STRICT: return only figures stored in the record. Do NOT calculate EV/revenue or convert currencies; if a multiple is not stored, write N/A.
For each deal: announcement date, closing date, target revenue (latest annual and LTM at announcement, currency, fiscal year), deal value, stored EV/revenue, source record.
DEALS: Vel Pitar (Romania, 2023), Natural Bakery (Canada, 2023), Mile Hi Bakery (US, 2023), Fortisa AG (Switzerland, 2023), Amaritta Food (Spain, 2023), Trei Brutari (Romania, 2024), Moulin d'Or (Tunisia, 2024).
OUTPUT: one row per deal: target | country | announced | closed | revenue_latest | revenue_ltm | currency | fiscal_year | deal_value | ev_revenue_stored | source.
```

### S4 - Acquisitions 2024-2026 (target revenue)

```text
CFA Research Challenge - Grupo Bimbo. Public data only: Capital IQ transaction records and target company profiles.
STRICT: return only figures stored in the record. Do NOT calculate EV/revenue or convert currencies; if a multiple is not stored, write N/A.
For each deal: announcement date, closing date, target revenue (latest annual and LTM at announcement, currency, fiscal year), deal value, stored EV/revenue, source record.
DEALS: La Zarcerena (Costa Rica, 2024), Pagnifique (Uruguay, 2024), Karamolegos Bakery (Romania, 2025), Grupo Don Don (Serbia, 2025), Stone House Bread (US, 2025), Grupo Wickbold (Brazil, 2025), Bonel / Bonelle (2026; state the country in the record).
OUTPUT: one row per deal: target | country | announced | closed | revenue_latest | revenue_ltm | currency | fiscal_year | deal_value | ev_revenue_stored | source.
```

### P1 - Peers' organic growth (Flowers, Aryzta, Yamazaki)

```text
CFA Research Challenge - Grupo Bimbo peers. Public data only: company filings, releases and Capital IQ segment data.
STRICT: return only figures printed by the company or stored in Capital IQ. Do NOT calculate organic growth yourself; if the company does not print it, write N/A.
COMPANIES: Flowers Foods, Aryzta AG, Yamazaki Baking.
Annual 2019-2025 and 9M2026: organic growth (or growth ex-FX and ex-M&A) by geographic or business segment, as reported, with the company's own definition.
OUTPUT: company | segment | indicator_as_named | period | value | definition_quote (max 25 words) | document | date | page.
```

### P2 - Peers' organic growth (Gruma, Mondelez, Grupo Nutresa)

```text
CFA Research Challenge - Grupo Bimbo peers. Public data only: company filings, releases and Capital IQ segment data.
STRICT: return only figures printed by the company or stored in Capital IQ. Do NOT calculate organic growth yourself; if the company does not print it, write N/A.
COMPANIES: Gruma, Mondelez International, Grupo Nutresa (last available year).
Annual 2019-2025 and 9M2026: organic growth (or growth ex-FX and ex-M&A) by geographic segment, as reported, with the company's own definition.
Then list (names only) the companies Capital IQ tags as packaged-bread competitors of Grupo Bimbo in Mexico, Brazil, Spain, Romania or the UK.
OUTPUT: company | segment | indicator_as_named | period | value | definition_quote (max 25 words) | document | date | page.
```

### I1 - Industry size and growth

```text
CFA Research Challenge - Grupo Bimbo industry. Public data only: any industry or market data stored in Capital IQ (e.g. S&P Global Market Intelligence industry data, research reports available in Capital IQ).
STRICT: return only figures stored or printed in the source. Do NOT calculate growth, CAGR, conversions or shares; if a figure is not stored, write N/A.
Packaged bread / bakery and salty snacks market size and growth, value and volume, for US, Canada, Mexico, Brazil, Spain, UK, Romania, India, China; history 2019-2025 and forecasts to 2030.
State for each value: provider, local currency or USD, current or constant prices.
OUTPUT: country | category | indicator | unit | currency | price_basis | period | value | value_type | provider | document_or_dataset | as_of_date. End with what is not stored in Capital IQ.
```

### X1 - Same-basis history for the Americas (added after M2)

Why: in the first pull the 2015-2025 history of nominalGDPLCU and consumerPriceInflation came mostly as "As reported ACTUAL", while M1-M2 forecasts 2026-2030 are "Standardized FORECAST". Growth from 2025 to 2026 would then mix two series. This block asks for the Standardized history so history and forecast are on one basis. Run after M5.

```text
CFA Research Challenge - Grupo Bimbo. Public data only. S&P Capital IQ economic data (S&P Global Market Intelligence).
STRICT: return only values stored explicitly in Capital IQ fields, exactly as shown, all decimals, in the unit stored. Do NOT calculate anything: no growth rates from levels, no averages, no sums, no unit conversions, no inversions, no cross rates, no interpolation. If a value would need any arithmetic, write N/A and "not a stored field". Keep the flag exactly as shown.
COUNTRIES: MEX, USA, CAN, ARG, BRA, CHL, COL, CRI, ECU, SLV, GTM, HND, NIC, PAN, PRY (and PER, URY, VEN if M5 found them).
Years 2015-2025: nominalGDPLCU and consumerPriceInflation in their "Standardized" version (Standardized ACTUAL or Standardized BEST_OF), not the "As reported" version. If only the "As reported" version is stored for a country-year, give it and flag it.
OUTPUT: long table country_iso3 | ciq_field_name | unit | currency | year | value | value_type_flag_as_shown | provider | as_of_date. If cut off, stop at a whole country and write CONTINUE FROM <country>.
```
