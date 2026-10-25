# Capital IQ ChatIQ answer - block E4 (China, India, South Korea)

Prompt: block E4 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- New coverage: none of these three countries appears in the first pull (`BIMBOA/research/Informacion_BIMBO_macro.txt`).
- **KOR nominalGDPLCU 2026 [unverified].** The stored 2026 level (3,277.04) is 22.4% above the stored 2025 level (2,676.67) [calc]. The same block stores 2026 real growth of 3.16% and CPI of 2.71%, so this looks like a series break (2025 and earlier dated 06/15/2026, 2026 and later dated 10/15/2026, perhaps on a different base). It is the same pattern as KAZ in block E3. Do not use the 2025-to-2026 step for Korea until it is checked in the Capital IQ screen. 2027-2030 grow at rates consistent with each other.
- For comparison, CHN 2025-to-2026 is +5.8% and IND is +13.6% [calc]. Neither shows an obvious break, but IND also changes vintage between 2025 and 2026.
- **India calendar year.** ChatIQ states that India is stored on calendar years (Jan-Dec), not on India's April-March fiscal year. Keep this in mind if we compare with Bimbo's India disclosures.
- **Column shift.** The `provider` column shows "Standardized BEST_OF" (the query-level selection), not the provider name. The provider is S&P Capital IQ per the footer. Formatting only.
- **Date footer.** "Data as of 10/25/2026" is after the run date (2026-10-24), the same impossible footer as in block M3. Use the per-row dates instead: economicAsOfEOP / economicAsofFinl.
- As in E1-E3: realPrivateConsumptionGrowth is "Standardized BEST_OF" for every year, and populationGrowth 2024-2025 is still flagged FORECAST.
- No value needed arithmetic. Nominal GDP growth will be computed by us as [calc] from nominalGDPLCU.

---

```text
Important Notes Before the Table
India — Calendar vs. Fiscal Year: The Capital IQ data for India is stored and returned with calendar-year period labels (e.g., combinePeriod = "2025Y", dateBegun = 2025-01-01, dateEnded = 2025-12-31). The API does not return fiscal-year (April–March) period identifiers for India in this dataset. The periods are stored as calendar years.

Nominal GDP Growth: Not a stored field — not produced (would require arithmetic from nominalGDPLCU levels).

realPrivateConsumptionGrowth value_type_flag: The stored macroDataSource for this field is "Standardized BEST_OF" across all three countries and all years — reproduced exactly as stored.

as_of_date: Two dates are stored per record — economicAsOfEOP (end-of-period as-of) and economicAsofFinl (final as-of). Both are shown in the table as economicAsOfEOP / economicAsofFinl.

Source: S&P Capital IQ

country_iso3	indicator	ciq_field_name	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date (EOP / Final)
CHN	Real GDP Growth	realGDPGrowth	%	—	2015	7.02	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2016	6.75	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2017	6.92	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2018	6.74	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2019	6.09	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2020	2.30	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2021	8.59	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2022	3.12	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2023	5.37	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2024	5.01	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2025	4.95	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2026	4.55	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2027	4.53	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2028	4.37	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2029	4.26	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real GDP Growth	realGDPGrowth	%	—	2030	4.20	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2015	70,251.15	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2016	76,119.30	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2017	84,738.29	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2018	93,601.01	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2019	100,587.24	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2020	103,486.76	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2021	117,382.30	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2022	123,402.94	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2023	129,427.17	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2024	134,806.62	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2025	140,187.92	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2026	148,336.79	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2027	156,685.84	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2028	165,320.91	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2029	174,512.25	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Nominal GDP (LCU)	nominalGDPLCU	CN¥B	CNY	2030	184,342.90	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2015	1.44	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2016	2.01	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2017	1.55	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2018	2.11	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2019	2.90	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2020	2.48	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2021	0.91	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2022	1.96	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2023	0.24	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2024	0.24	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2025	0.05	As reported ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2026	1.01	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2027	1.07	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2028	1.25	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2029	1.55	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Consumer Price Inflation	consumerPriceInflation	%	—	2030	1.64	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2015	7.59	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2016	8.52	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2017	7.34	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2018	7.76	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2019	6.35	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2020	-0.31	Standardized BEST_OF	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2021	9.41	Standardized BEST_OF	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2022	2.77	Standardized BEST_OF	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2023	8.40	Standardized BEST_OF	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2024	3.93	Standardized BEST_OF	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2025	4.49	Standardized BEST_OF	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2026	3.21	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2027	4.26	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2028	4.76	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2029	5.09	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2030	5.21	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Population Growth	populationGrowth	%	—	2015	0.59	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2016	0.57	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2017	0.59	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2018	0.47	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2019	0.32	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2020	0.18	Standardized ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2021	0.02	Standardized ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2022	-0.09	Standardized ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2023	-0.18	Standardized ACTUAL	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2024	-0.23	Standardized FORECAST	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2025	-0.23	Standardized FORECAST	Standardized BEST_OF	08/18/2026 / 10/22/2026
CHN	Population Growth	populationGrowth	%	—	2026	-0.22	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Population Growth	populationGrowth	%	—	2027	-0.23	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Population Growth	populationGrowth	%	—	2028	-0.25	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Population Growth	populationGrowth	%	—	2029	-0.27	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
CHN	Population Growth	populationGrowth	%	—	2030	-0.29	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2015	7.48	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2016	9.00	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2017	6.10	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2018	7.28	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2019	4.59	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2020	-5.83	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2021	9.41	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2022	6.97	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2023	7.15	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2024	7.42	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2025	7.30	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2026	6.65	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2027	6.45	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2028	7.20	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2029	6.72	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real GDP Growth	realGDPGrowth	%	—	2030	5.57	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2015	133,907.27	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2016	149,647.12	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2017	166,281.27	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2018	186,830.70	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2019	197,561.44	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2020	192,451.28	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2021	228,315.09	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2022	255,196.93	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2023	282,618.84	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2024	311,180.11	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2025	337,425.63	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2026	383,341.54	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2027	432,787.46	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2028	489,811.42	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2029	549,509.74	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Nominal GDP (LCU)	nominalGDPLCU	₹B	INR	2030	610,071.20	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2015	4.91	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2016	4.95	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2017	3.33	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2018	3.95	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2019	3.72	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2020	6.62	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2021	5.14	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2022	6.69	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2023	5.65	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2024	4.95	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2025	2.20	As reported ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2026	4.85	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2027	5.81	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2028	4.15	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2029	4.71	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Consumer Price Inflation	consumerPriceInflation	%	—	2030	4.88	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2015	7.99	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2016	8.28	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2017	6.16	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2018	6.97	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2019	5.23	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2020	-5.40	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2021	11.65	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2022	8.53	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2023	6.29	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2024	6.46	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2025	7.24	Standardized BEST_OF	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2026	6.41	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2027	6.83	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2028	7.58	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2029	6.96	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2030	5.79	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2015	1.20	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2016	1.20	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2017	1.17	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2018	1.10	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2019	1.05	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2020	0.98	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2021	0.83	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2022	0.79	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2023	0.89	Standardized ACTUAL	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2024	0.89	Standardized FORECAST	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2025	0.89	Standardized FORECAST	Standardized BEST_OF	09/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2026	0.87	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2027	0.85	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2028	0.82	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2029	0.80	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
IND	Population Growth	populationGrowth	%	—	2030	0.77	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2015	2.92	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2016	3.17	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2017	3.43	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2018	3.18	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2019	2.31	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2020	-0.70	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2021	4.70	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2022	2.91	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2023	1.48	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2024	2.19	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2025	1.14	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2026	3.16	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2027	2.31	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2028	2.00	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2029	1.76	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real GDP Growth	realGDPGrowth	%	—	2030	1.77	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2015	1,740.78	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2016	1,833.03	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2017	1,934.23	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2018	2,006.97	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2019	2,040.59	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2020	2,058.47	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2021	2,223.72	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2022	2,328.17	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2023	2,407.58	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2024	2,564.20	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2025	2,676.67	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2026	3,277.04	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2027	3,434.73	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2028	3,569.81	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2029	3,697.20	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Nominal GDP (LCU)	nominalGDPLCU	₩T	KRW	2030	3,824.81	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2015	0.71	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2016	0.97	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2017	1.94	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2018	1.48	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2019	0.38	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2020	0.54	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2021	2.50	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2022	5.09	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2023	3.60	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2024	2.32	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2025	2.12	As reported ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2026	2.71	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2027	2.23	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2028	1.95	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2029	1.88	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Consumer Price Inflation	consumerPriceInflation	%	—	2030	1.87	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2015	2.58	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2016	2.78	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2017	2.86	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2018	3.28	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2019	2.37	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2020	-4.64	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2021	3.74	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2022	4.23	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2023	2.09	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2024	1.34	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2025	1.50	Standardized BEST_OF	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2026	2.17	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2027	1.89	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2028	1.94	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2029	2.02	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	—	2030	2.00	Standardized BEST_OF	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2015	0.88	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2016	0.62	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2017	0.37	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2018	0.30	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2019	0.25	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2020	0.18	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2021	-0.02	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2022	-0.13	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2023	-0.07	Standardized ACTUAL	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2024	-0.06	Standardized FORECAST	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2025	-0.10	Standardized FORECAST	Standardized BEST_OF	06/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2026	-0.13	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2027	-0.16	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2028	-0.19	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2029	-0.21	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
KOR	Population Growth	populationGrowth	%	—	2030	-0.24	Standardized FORECAST	Standardized BEST_OF	10/15/2026 / 10/15/2026
Data as of 10/25/2026. All periods are calendar years (January–December) for all three countries, including India, as stored in Capital IQ. Source: S&P Capital IQ.

Additional Economic Fields Stored in Capital IQ — Names Only
The following fields are present in the Capital IQ dataset for each country (observed from the all_fields_data payload). Fields are common across all three countries unless noted.

Present for CHN, IND, and KOR:

economicAsOf
population
averageMonthlyWages
budgetBalanceGDP
exportedGoods
realGDP
nominalGDP
gdpPerCapita
unemploymentRate
realGovermentConsumptionGrowth
realGrossFixedInvestmentGrowth
currentAccountBalance
averageConsumerPriceIndex
producerPriceInflation
averageProducerPriceIndex
gdpDeflator
publicDebtGDP
interestPaymentGrowth
publicDebt
debtInterestPaymentGDP
foreignDebtGDP
grossDomesticSavings
industrialProductionGrowth
budgetExpenditureGDP
budgetRevenue
personalDisposableIncome
realPersonalDisposableIncome
realPersonalDisposableIncomeGrowth
currentAccountBalanceGDP
importedGoods
directInvestmentBalance
inwardDirectInvestment
outwardDirectInvestment
tradeBalance
realGrossFixedInvestment
moneyMarketInterestRate
bondYield
domesticCreditGrowth
internationalReservesLessGold
interestPaymentGrowthRate
laborForce
laborProductivityGrowth
laborCostChange
averageExchangeRate
exchangeRateEnd
medianHouseholdIncome
employment
financialAccountBalance
internationalResLessGoldGDP
realGDPUSD
Present for KOR only (not observed for CHN or IND in the returned data):

stockMarketIndex
Stored as null / not populated for any of the three countries in the returned data:

foreignDebt
externalDebtService
goldReserves
grossPersonalIncome

Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
