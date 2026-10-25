# Capital IQ ChatIQ answer - block M5 (PER, URY, VEN)

Prompt: block M5 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; tables kept tab-separated as returned.

Review note (AI, 2026-10-24): VEN nominalGDPLCU is not usable for growth rates: 2018 is stored as 0.00 and 2018-2025 are flagged "Standardized FORECAST" although they are past years, while CPI for the same years is "As reported ACTUAL" (2018: 65,374.08%). Treat VEN nominal GDP 2015-2025 as [unverified].

---

Identifier Resolution Results
Before the main table, here is what each identifier tried returned:

```text
Identifier Tried	Result
Peru	✅ Resolved → keyCountry = PE
PER (ISO3)	✅ Resolved → keyCountry = PE
PE (ISO2)	✅ Resolved → keyCountry = PE
Republic of Peru	✅ Resolved → keyCountry = PE
Uruguay	✅ Resolved → keyCountry = UY
URY (ISO3)	✅ Resolved → keyCountry = UY
UY (ISO2)	❌ Unresolved — "No valid country identifier found"
Oriental Republic of Uruguay	❌ Unresolved — "No valid country identifier found"
Venezuela	✅ Resolved → keyCountry = VE
VEN (ISO3)	✅ Resolved → keyCountry = VE
VE (ISO2)	✅ Resolved → keyCountry = VE
Bolivarian Republic of Venezuela	✅ Resolved → keyCountry = VE
Venezuela, RB	❌ Unresolved — "No valid country identifier found"
```

Note on Venezuela CPI series: The consumerPriceInflation field for Venezuela carries the macroDataSource label "As reported ACTUAL" (historical years) or "Standardized FORECAST" (forecast years). The data is not separately labelled as "official" or "alternative" within the stored field — it is stored under the standard consumerPriceInflation field with no additional qualifier distinguishing official vs. alternative series. The label shown is exactly as stored.

Main Data Table
Source: S&P Capital IQ Economic & Demographic Data (S&P Global Market Intelligence) Data as of: economicAsofFinl dates ranging from 09/17/2026 to 10/23/2026 (per field, see as_of_date column)

```text
country_iso3	indicator	ciq_field_name	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date
PER	realGDPGrowth	realGDPGrowth	%	N/A	2015	3.25	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2016	3.95	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2017	2.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2018	3.97	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2019	2.24	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2020	-10.93	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2021	13.42	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2022	2.82	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2023	-0.35	Standardized ACTUAL	S&P Capital IQ	10/19/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2024	3.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2025	3.43	As reported ACTUAL	S&P Capital IQ	10/23/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2026	3.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2027	3.01	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2028	2.83	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2029	2.80	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	realGDPGrowth	realGDPGrowth	%	N/A	2030	2.89	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2015	619.29	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2016	671.56	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2017	715.87	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2018	755.47	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2019	788.91	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2020	733.98	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2021	892.25	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2022	952.40	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2023	1,018.13	As reported ACTUAL	S&P Capital IQ	10/19/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2024	1,109.22	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2025	1,213.90	As reported ACTUAL	S&P Capital IQ	10/23/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2026	1,343.24	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2027	1,422.81	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2028	1,496.79	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2029	1,572.11	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	nominalGDPLCU	S/.B	PEN	2030	1,658.78	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2015	3.55	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2016	3.59	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2017	2.80	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2018	1.32	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2019	2.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2020	1.83	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2021	3.98	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2022	7.88	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2023	6.26	As reported ACTUAL	S&P Capital IQ	10/19/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2024	2.35	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2025	1.50	As reported ACTUAL	S&P Capital IQ	10/23/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2026	3.88	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2027	3.38	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2028	2.01	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2029	2.34	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	consumerPriceInflation	%	N/A	2030	2.77	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2015	4.02	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2016	3.74	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2017	2.64	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2018	3.83	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2019	3.24	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2020	-9.86	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2021	12.54	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2022	3.55	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2023	0.06	Standardized BEST_OF	S&P Capital IQ	10/19/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2024	2.77	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2025	3.63	Standardized BEST_OF	S&P Capital IQ	10/23/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2026	3.29	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2027	3.03	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2028	2.94	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2029	2.72	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2030	2.95	Standardized BEST_OF	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2015	1.13	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2016	1.34	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2017	1.48	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2018	1.83	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2019	1.73	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2020	1.20	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2021	0.97	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2022	0.96	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2023	1.11	Standardized ACTUAL	S&P Capital IQ	10/19/2026
PER	populationGrowth	populationGrowth	%	N/A	2024	1.10	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2025	1.05	Standardized FORECAST	S&P Capital IQ	10/23/2026
PER	populationGrowth	populationGrowth	%	N/A	2026	1.00	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2027	0.96	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2028	0.92	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2029	0.88	Standardized FORECAST	S&P Capital IQ	10/15/2026
PER	populationGrowth	populationGrowth	%	N/A	2030	0.84	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2015	0.37	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2016	0.88	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2017	1.74	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2018	0.16	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2019	0.93	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2020	-7.36	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2021	5.84	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2022	4.61	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2023	0.76	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2024	3.33	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2025	1.78	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2026	1.67	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2027	2.17	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2028	2.78	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2029	2.92	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	realGDPGrowth	realGDPGrowth	%	N/A	2030	2.81	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2015	1,620.07	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2016	1,733.77	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2017	1,864.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2018	2,007.73	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2019	2,193.67	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2020	2,250.20	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2021	2,645.46	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2022	2,933.06	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2023	3,075.19	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2024	3,310.43	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2025	3,515.52	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2026	3,688.20	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2027	3,922.70	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2028	4,210.25	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2029	4,523.67	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	nominalGDPLCU	$B	UYU	2030	4,854.60	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2015	8.67	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2016	9.64	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2017	6.22	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2018	7.61	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2019	7.88	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2020	9.76	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2021	7.75	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2022	9.10	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2023	5.87	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2024	4.85	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2025	4.65	As reported ACTUAL	S&P Capital IQ	10/19/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2026	4.99	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2027	5.92	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2028	4.76	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2029	3.96	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	consumerPriceInflation	consumerPriceInflation	%	N/A	2030	3.11	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2015	-0.49	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2016	0.09	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2017	4.04	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2018	1.79	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2019	0.86	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2020	-8.65	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2021	3.25	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2022	5.79	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2023	3.33	Standardized BEST_OF	S&P Capital IQ	10/19/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2024	1.69	Standardized BEST_OF	S&P Capital IQ	10/19/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2025	2.07	Standardized BEST_OF	S&P Capital IQ	10/19/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2026	2.24	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2027	1.39	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2028	2.31	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2029	2.13	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2030	1.83	Standardized BEST_OF	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2015	0.35	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2016	0.33	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2017	0.27	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2018	0.18	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2019	0.08	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2020	0.05	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2021	-0.07	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2022	-0.17	Standardized ACTUAL	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2023	-0.08	Standardized ACTUAL	S&P Capital IQ	10/19/2026
URY	populationGrowth	populationGrowth	%	N/A	2024	-0.04	Standardized FORECAST	S&P Capital IQ	10/19/2026
URY	populationGrowth	populationGrowth	%	N/A	2025	-0.06	Standardized FORECAST	S&P Capital IQ	10/19/2026
URY	populationGrowth	populationGrowth	%	N/A	2026	-0.06	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2027	-0.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2028	-0.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2029	-0.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
URY	populationGrowth	populationGrowth	%	N/A	2030	-0.08	Standardized FORECAST	S&P Capital IQ	10/15/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2015	-3.89	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2016	-17.00	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2017	-14.45	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2018	-21.39	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2019	-29.00	Standardized ACTUAL	S&P Capital IQ	08/25/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2020	-33.24	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2021	1.29	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2022	15.04	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2023	5.70	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2024	8.88	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2025	9.00	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2026	6.51	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2027	6.75	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2028	5.62	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2029	5.13	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	realGDPGrowth	realGDPGrowth	%	N/A	2030	3.74	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2015	0.08	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2016	0.28	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2017	2.01	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2018	0.00	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2019	0.31	Standardized FORECAST	S&P Capital IQ	08/25/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2020	12.97	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2021	213.28	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2022	733.24	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2023	2,172.21	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2024	4,376.58	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2025	16,671.53	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2026	79,820.16	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2027	145,644.40	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2028	201,725.77	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2029	253,313.66	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	nominalGDPLCU	nominalGDPLCU	Bs. SB	VES	2030	296,875.64	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2015	121.89	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2016	254.82	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2017	438.12	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2018	65,374.08	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2019	19,906.29	As reported ACTUAL	S&P Capital IQ	08/25/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2020	2,354.79	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2021	1,589.52	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2022	186.65	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2023	337.46	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2024	49.39	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2025	252.08	As reported ACTUAL	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2026	452.15	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2027	84.98	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2028	19.85	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2029	14.44	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	consumerPriceInflation	consumerPriceInflation	%	N/A	2030	11.77	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2015	-5.03	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2016	-21.91	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2017	-14.59	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2018	-18.13	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2019	-25.16	Standardized BEST_OF	S&P Capital IQ	08/25/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2020	-21.14	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2021	2.50	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2022	13.51	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2023	5.16	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2024	7.77	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2025	5.97	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2026	2.95	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2027	4.12	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2028	3.63	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2029	3.59	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	realPrivateConsumptionGrowth	realPrivateConsumptionGrowth	%	N/A	2030	3.72	Standardized BEST_OF	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2015	1.06	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2016	0.63	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2017	-0.65	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2018	-2.48	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2019	-2.92	Standardized ACTUAL	S&P Capital IQ	08/25/2026
VEN	populationGrowth	populationGrowth	%	N/A	2020	-1.71	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2021	-0.73	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2022	-0.09	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2023	0.31	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2024	0.37	Standardized ACTUAL	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2025	0.39	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2026	0.41	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2027	0.44	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2028	0.44	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2029	0.45	Standardized FORECAST	S&P Capital IQ	09/17/2026
VEN	populationGrowth	populationGrowth	%	N/A	2030	0.47	Standardized FORECAST	S&P Capital IQ	09/17/2026
```

Notes
Venezuela CPI series clarification: The consumerPriceInflation field for Venezuela is stored under the single standard field name consumerPriceInflation. The data carries the macroDataSource label "As reported ACTUAL" for historical periods and "Standardized FORECAST" for future periods. There is no separate "official" vs. "alternative" label stored within the Capital IQ field for Venezuela — the series is not distinguished as such in the stored data. Users should be aware that Venezuela's official CPI statistics have historically been subject to significant methodological concerns; however, Capital IQ does not apply an explicit "official" or "alternative" tag to this field as returned.

Uruguay nominalGDPLCU currency: The stored magnitude is $B (Uruguayan pesos, billions). The currency column reflects UYU (Uruguayan peso) as the local currency unit, consistent with the LCU designation.

Venezuela nominalGDPLCU: The stored magnitude is Bs. SB (bolívares soberanos, billions). The 2018 value is stored as 0.00 (exactly as returned). The currency column reflects VES (bolívar soberano).

as_of_date column: Populated from the economicAsofFinl field (the final data-as-of date), exactly as stored.

Disclaimer (ChatIQ, abridged): responses are generated by AI without human review and may be inaccurate or incomplete; the user must verify all information.
