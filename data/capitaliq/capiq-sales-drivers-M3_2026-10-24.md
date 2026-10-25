# Capital IQ ChatIQ answer - block M3 (CRI, ECU, SLV, GTM)

Prompt: block M3 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; tables kept tab-separated as returned.

---

Grupo Bimbo – CFA Research Challenge: S&P Capital IQ Economic Data
Notes on Methodology
All values reproduced exactly as stored; no arithmetic performed.
value_type_flag_as_shown = the macroDataSource string exactly as returned.
as_of_date = economicAsOfEOP field (end-of-period as-of date).
CRI = Costa Rica | ECU = Ecuador | SLV = El Salvador | GTM = Guatemala.
Currency codes per stored metadata: CRC (Costa Rica colón), USD (Ecuador/El Salvador), GTQ (Guatemala quetzal). Unit symbols: ¢B = billions of colónes; Q.B = billions of quetzales; $B = billions of USD; M = millions; % = percent.
Source: S&P Capital IQ

Parts A + B + C — Master Data Table

```text
country_iso3	indicator	ciq_field_name	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date
PART A — realGDPGrowth, nominalGDPLCU, consumerPriceInflation · 2026–2030									
CRI	Real GDP Growth	realGDPGrowth	%	CRC	2026	2.91	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Real GDP Growth	realGDPGrowth	%	CRC	2027	2.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Real GDP Growth	realGDPGrowth	%	CRC	2028	3.20	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Real GDP Growth	realGDPGrowth	%	CRC	2029	3.21	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Real GDP Growth	realGDPGrowth	%	CRC	2030	3.27	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Nominal GDP (LCU)	nominalGDPLCU	¢B	CRC	2026	53,076.66	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Nominal GDP (LCU)	nominalGDPLCU	¢B	CRC	2027	55,718.67	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Nominal GDP (LCU)	nominalGDPLCU	¢B	CRC	2028	58,601.23	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Nominal GDP (LCU)	nominalGDPLCU	¢B	CRC	2029	61,624.71	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Nominal GDP (LCU)	nominalGDPLCU	¢B	CRC	2030	64,830.09	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Consumer Price Inflation	consumerPriceInflation	%	CRC	2026	-0.56	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Consumer Price Inflation	consumerPriceInflation	%	CRC	2027	3.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Consumer Price Inflation	consumerPriceInflation	%	CRC	2028	1.95	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Consumer Price Inflation	consumerPriceInflation	%	CRC	2029	1.71	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Consumer Price Inflation	consumerPriceInflation	%	CRC	2030	2.18	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Real GDP Growth	realGDPGrowth	%	USD	2026	2.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Real GDP Growth	realGDPGrowth	%	USD	2027	2.68	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Real GDP Growth	realGDPGrowth	%	USD	2028	2.20	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Real GDP Growth	realGDPGrowth	%	USD	2029	2.04	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Real GDP Growth	realGDPGrowth	%	USD	2030	2.03	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2026	137.64	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2027	144.98	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2028	151.63	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2029	158.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2030	164.80	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Consumer Price Inflation	consumerPriceInflation	%	USD	2026	2.37	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Consumer Price Inflation	consumerPriceInflation	%	USD	2027	2.69	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Consumer Price Inflation	consumerPriceInflation	%	USD	2028	2.18	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Consumer Price Inflation	consumerPriceInflation	%	USD	2029	2.09	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Consumer Price Inflation	consumerPriceInflation	%	USD	2030	2.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
SLV	Real GDP Growth	realGDPGrowth	%	USD	2026	3.06	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Real GDP Growth	realGDPGrowth	%	USD	2027	2.78	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Real GDP Growth	realGDPGrowth	%	USD	2028	2.41	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Real GDP Growth	realGDPGrowth	%	USD	2029	2.31	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Real GDP Growth	realGDPGrowth	%	USD	2030	2.34	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2026	38.37	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2027	40.03	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2028	41.60	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2029	43.20	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Nominal GDP (LCU)	nominalGDPLCU	$B	USD	2030	44.87	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Consumer Price Inflation	consumerPriceInflation	%	USD	2026	2.42	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Consumer Price Inflation	consumerPriceInflation	%	USD	2027	2.62	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Consumer Price Inflation	consumerPriceInflation	%	USD	2028	2.46	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Consumer Price Inflation	consumerPriceInflation	%	USD	2029	2.56	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Consumer Price Inflation	consumerPriceInflation	%	USD	2030	2.65	Standardized FORECAST	S&P Capital IQ	08/25/2026
GTM	Real GDP Growth	realGDPGrowth	%	GTQ	2026	3.89	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Real GDP Growth	realGDPGrowth	%	GTQ	2027	3.47	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Real GDP Growth	realGDPGrowth	%	GTQ	2028	3.27	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Real GDP Growth	realGDPGrowth	%	GTQ	2029	3.28	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Real GDP Growth	realGDPGrowth	%	GTQ	2030	3.13	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Nominal GDP (LCU)	nominalGDPLCU	Q.B	GTQ	2026	1,016.22	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Nominal GDP (LCU)	nominalGDPLCU	Q.B	GTQ	2027	1,123.33	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Nominal GDP (LCU)	nominalGDPLCU	Q.B	GTQ	2028	1,233.62	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Nominal GDP (LCU)	nominalGDPLCU	Q.B	GTQ	2029	1,357.33	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Nominal GDP (LCU)	nominalGDPLCU	Q.B	GTQ	2030	1,492.77	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2026	3.10	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2027	3.54	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2028	3.55	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2029	3.13	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2030	3.04	Standardized FORECAST	S&P Capital IQ	10/15/2026
PART B — GTM consumerPriceInflation · 2015–2025 (Actual)									
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2015	2.39	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2016	4.45	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2017	4.42	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2018	3.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2019	3.70	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2020	3.21	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2021	4.26	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2022	6.89	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2023	6.21	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2024	2.87	As reported ACTUAL	S&P Capital IQ	08/18/2026
GTM	Consumer Price Inflation	consumerPriceInflation	%	GTQ	2025	1.58	As reported ACTUAL	S&P Capital IQ	10/15/2026
PART C — realPrivateConsumptionGrowth & populationGrowth · 2015–2030 (all four countries)									
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2015	4.68	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2016	3.75	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2017	5.55	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2018	2.59	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2019	2.33	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2020	-6.35	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2021	9.03	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2022	3.68	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2023	4.21	Standardized BEST_OF	S&P Capital IQ	03/17/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2024	3.75	Standardized BEST_OF	S&P Capital IQ	06/15/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2025	3.83	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2026	2.51	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2027	2.82	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2028	3.64	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2029	3.41	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CRI	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	CRC	2030	3.33	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2015	1.07	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2016	1.02	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2017	0.95	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2018	0.91	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2019	0.84	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2020	0.70	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2021	0.51	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2022	0.43	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2023	0.47	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	Population Growth	populationGrowth	%	CRC	2024	0.48	Standardized FORECAST	S&P Capital IQ	06/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2025	0.45	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2026	0.42	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2027	0.40	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2028	0.38	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2029	0.36	Standardized FORECAST	S&P Capital IQ	10/15/2026
CRI	Population Growth	populationGrowth	%	CRC	2030	0.34	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2015	4.07	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2016	-5.83	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2017	6.84	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2018	2.08	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2019	2.13	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2020	-10.61	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2021	11.13	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2022	6.00	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2023	3.63	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2024	-1.65	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2025	2.74	Standardized BEST_OF	S&P Capital IQ	06/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2026	3.23	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2027	2.43	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2028	1.85	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2029	1.95	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ECU	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2030	2.02	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ECU	Population Growth	populationGrowth	%	USD	2015	1.44	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2016	1.47	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2017	1.54	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2018	1.73	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2019	1.70	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2020	1.19	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2021	0.78	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2022	0.80	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2023	0.88	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2024	0.86	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2025	0.85	Standardized FORECAST	S&P Capital IQ	06/15/2026
ECU	Population Growth	populationGrowth	%	USD	2026	0.85	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Population Growth	populationGrowth	%	USD	2027	0.84	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Population Growth	populationGrowth	%	USD	2028	0.84	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Population Growth	populationGrowth	%	USD	2029	0.84	Standardized FORECAST	S&P Capital IQ	10/15/2026
ECU	Population Growth	populationGrowth	%	USD	2030	0.82	Standardized FORECAST	S&P Capital IQ	10/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2015	2.84	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2016	1.97	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2017	1.69	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2018	1.36	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2019	1.74	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2020	-8.02	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2021	9.60	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2022	-0.17	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2023	4.60	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2024	2.86	Standardized BEST_OF	S&P Capital IQ	08/25/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2025	2.79	Standardized BEST_OF	S&P Capital IQ	06/15/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2026	3.10	Standardized BEST_OF	S&P Capital IQ	08/25/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2027	3.00	Standardized BEST_OF	S&P Capital IQ	08/25/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2028	1.96	Standardized BEST_OF	S&P Capital IQ	08/25/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2029	2.02	Standardized BEST_OF	S&P Capital IQ	08/25/2026
SLV	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	USD	2030	2.07	Standardized BEST_OF	S&P Capital IQ	08/25/2026
SLV	Population Growth	populationGrowth	%	USD	2015	0.34	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2016	0.28	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2017	0.21	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2018	0.10	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2019	0.04	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2020	0.20	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2021	0.34	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2022	0.39	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2023	0.47	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2024	0.45	Standardized ACTUAL	S&P Capital IQ	08/25/2026
SLV	Population Growth	populationGrowth	%	USD	2025	0.43	Standardized FORECAST	S&P Capital IQ	06/15/2026
SLV	Population Growth	populationGrowth	%	USD	2026	0.40	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Population Growth	populationGrowth	%	USD	2027	0.39	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Population Growth	populationGrowth	%	USD	2028	0.38	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Population Growth	populationGrowth	%	USD	2029	0.36	Standardized FORECAST	S&P Capital IQ	08/25/2026
SLV	Population Growth	populationGrowth	%	USD	2030	0.34	Standardized FORECAST	S&P Capital IQ	08/25/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2015	5.14	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2016	4.07	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2017	3.27	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2018	3.55	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2019	4.72	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2020	-1.64	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2021	8.47	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2022	4.24	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2023	4.34	Standardized BEST_OF	S&P Capital IQ	06/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2024	5.85	Standardized BEST_OF	S&P Capital IQ	08/18/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2025	4.66	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2026	4.38	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2027	3.74	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2028	3.62	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2029	3.66	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GTM	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	GTQ	2030	3.01	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2015	1.85	Standardized ACTUAL	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2016	1.86	Standardized ACTUAL	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2017	1.84	Standardized ACTUAL	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2018	1.68	Standardized ACTUAL	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2019	1.53	Standardized ACTUAL	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2020	1.48	Standardized FORECAST	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2021	1.39	Standardized FORECAST	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2022	1.42	Standardized FORECAST	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2023	1.55	Standardized FORECAST	S&P Capital IQ	06/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2024	1.55	Standardized FORECAST	S&P Capital IQ	08/18/2026
GTM	Population Growth	populationGrowth	%	GTQ	2025	1.53	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2026	1.50	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2027	1.47	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2028	1.43	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2029	1.40	Standardized FORECAST	S&P Capital IQ	10/15/2026
GTM	Population Growth	populationGrowth	%	GTQ	2030	1.37	Standardized FORECAST	S&P Capital IQ	10/15/2026
```

Data as of 10/25/2026. Source: S&P Capital IQ. All values reproduced exactly as stored; no arithmetic applied.

Part D — All Other Economic Fields Stored in S&P Capital IQ for Each Country
The following field names are present in the Capital IQ economic/demographic dataset for these four countries (beyond the five fields already covered in Parts A–C). Availability of individual fields varies by country as noted.

```text
#	Field Name (ciq_field_name)	Available Countries (from returned data)
1	economicAsOf	CRI, ECU, SLV, GTM
2	population	CRI, ECU, SLV, GTM
3	averageMonthlyWages	CRI, ECU, GTM (null for SLV)
4	budgetBalanceGDP	CRI, ECU, SLV, GTM
5	exportedGoods	CRI, ECU, SLV, GTM
6	realGDP	CRI, ECU, SLV, GTM
7	nominalGDP	CRI, ECU, SLV, GTM
8	gdpPerCapita	CRI, ECU, SLV, GTM
9	unemploymentRate	CRI, ECU, SLV, GTM
10	realGovermentConsumptionGrowth	CRI, ECU, SLV, GTM
11	realGrossFixedInvestmentGrowth	CRI, ECU, SLV, GTM
12	currentAccountBalance	CRI, ECU, SLV, GTM
13	averageConsumerPriceIndex	CRI, ECU, SLV, GTM
14	producerPriceInflation	CRI, ECU (null for SLV, GTM)
15	averageProducerPriceIndex	CRI, ECU (null for SLV, GTM)
16	gdpDeflator	CRI, ECU, SLV, GTM
17	publicDebtGDP	CRI, ECU, SLV, GTM
18	interestPaymentGrowth	CRI, ECU, SLV, GTM
19	publicDebt	CRI, ECU, SLV, GTM
20	debtInterestPaymentGDP	CRI, ECU, SLV, GTM
21	foreignDebtGDP	CRI, ECU, SLV, GTM
22	grossDomesticSavings	CRI, ECU, SLV, GTM
23	industrialProductionGrowth	CRI, ECU, SLV, GTM
24	budgetExpenditureGDP	CRI, SLV, GTM (null for ECU)
25	budgetRevenue	CRI, ECU, SLV, GTM
26	personalDisposableIncome	CRI, ECU, SLV, GTM
27	realPersonalDisposableIncome	CRI, ECU, SLV, GTM
28	realPersonalDisposableIncomeGrowth	CRI, ECU, SLV, GTM
29	currentAccountBalanceGDP	CRI, ECU, SLV, GTM
30	importedGoods	CRI, ECU, SLV, GTM
31	directInvestmentBalance	CRI, ECU, SLV, GTM
32	inwardDirectInvestment	CRI, ECU, SLV, GTM
33	outwardDirectInvestment	CRI, ECU, SLV, GTM
34	tradeBalance	CRI, ECU, SLV, GTM
35	realGrossFixedInvestment	CRI, ECU, SLV, GTM
36	moneyMarketInterestRate	CRI, ECU, SLV, GTM
37	bondYield	CRI, ECU (not returned for SLV, GTM)
38	domesticCreditGrowth	CRI, ECU, GTM (not returned for SLV)
39	internationalReservesLessGold	CRI, ECU, SLV, GTM
40	interestPaymentGrowthRate	CRI, ECU, SLV, GTM
41	laborForce	CRI, ECU, SLV, GTM
42	laborProductivityGrowth	CRI, ECU, SLV (not returned for GTM)
43	averageExchangeRate	CRI, ECU, SLV, GTM
44	exchangeRateEnd	CRI, ECU, SLV, GTM
45	medianHouseholdIncome	CRI, ECU, SLV, GTM
46	employment	CRI, ECU, SLV, GTM
47	financialAccountBalance	CRI, ECU, SLV, GTM
48	internationalResLessGoldGDP	CRI, ECU, SLV, GTM
49	realGDPUSD	CRI, ECU, SLV, GTM
50	foreignDebt	CRI, ECU, SLV, GTM (null for all four in returned data)
51	externalDebtService	CRI, ECU, SLV, GTM (null for all four in returned data)
52	goldReserves	CRI, ECU, SLV, GTM (null for all four in returned data)
53	grossPersonalIncome	CRI, ECU, SLV, GTM (null for all four in returned data)
```

Note: Fields marked "null for all four" are present as named fields in the Capital IQ schema but returned no value for any of these four countries in the current data pull. Fields marked as absent for specific countries were not returned for those countries in the current period snapshot.

Disclaimer (ChatIQ, abridged): responses are generated by AI without human review and may be inaccurate or incomplete; the user must verify all information.
