# Capital IQ ChatIQ answer - block I1 (industry size and growth)

Prompt: block I1 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (line 331).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- **No country-level industry data.** Capital IQ holds no bakery or snacks market series by country or year for any Bimbo market (US, Canada, Mexico, Brazil, Spain, UK, Romania, India, China), in value or volume. A per-region industry ratio cannot be built from Capital IQ.
- **The only usable figures are GlobalData global numbers quoted by Bimbo itself, and we hold both sources locally.** Checked against the local PDFs (word positions read from the page, 2026-10-24):

  | Source (local) | Category | Market size | CAGR 2020-25 | CAGR 2025-30 | ChatIQ said |
  |---|---|---|---|---|---|
  | `filings/quarterly/GB_Investor_PPT_3Q26.pdf` p.5 | Baking | US$674 Bn [sourced] | 3.8% [sourced] | 3.4% [sourced] | 3.8% / **3.7% (wrong)** |
  | same, p.5 | Snacks | US$110 Bn [sourced] | 5.0% [sourced] | 2.9% [sourced] | **3.4% / 3.7% (both wrong)** |
  | `filings/annual/IA25_GB_Celebramos_ESP_200826.pdf` p.16 | Baking (Panificacion) | US$639 Bn [sourced] | 2.8% and 4.7% printed; period labels to confirm on the page | | matches values |
  | same, p.16 | Snacks (Botanas) | US$183 Bn [sourced] | 4.7% and 3.8% printed; period labels to confirm on the page | | matches values |

  - ChatIQ's baking 2025-30 "3.7%" is Bimbo's baking market share on the same slide, not a growth rate. Use the local PDFs, not this table.
  - The deck (674 / 110, "Value M USD-2025") and the annual report (639 / 183) disagree. Snacks falls from 183 to 110, which a broader baking definition does not explain. ChatIQ's explanation (savory biscuits added) is its own inference. Treat as two different GlobalData vintages or scopes; [unverified] which one to use.
  - Both are management's presentation of a third-party source: cite as GlobalData via Grupo Bimbo, with page.
- **Discard the third-party rows** (China via Namchow, India via Gopal Snacks / Grill Splendour / Baba Food, US via Conagra, Canada via Purebread). They are secondary quotes in other companies' reports, with mixed scopes, "~" values, ranges and a "partial figure". None covers a Bimbo region as a whole.
- **Implication for the method:** if the team links sales to the industry, the only sourced anchor is a single global baking CAGR, not one per region. That favours the GDP / consumption route per region, or a global industry rate applied to all regions (team decision).

---

```text
Packaged Bread/Bakery & Salty Snacks: Market Size & Growth Data Available in Capital IQ
After a thorough review of all context documents, the following is a complete inventory of stored figures relevant to your request. Per your strict instruction, no values have been calculated, converted, or derived.

Data Found in Capital IQ Sources
Country	Category	Indicator	Unit	Currency	Price Basis	Period	Value	Value Type	Provider	Document/Dataset	As-of Date
Global	Baking (Bread, Rolls, Cakes, Pastries, Cookies, Morning Goods)	Market Size	USD Billions	USD	Current (2025 value)	2025	639	Actual	GlobalData	Grupo Bimbo AR (2025)	08/06/2026
Global	Baking (Bread, Rolls, Cakes, Pastries, Cookies, Morning Goods)	CAGR	%	N/A	N/A	2019–2024	2.8%	Historical CAGR	GlobalData	Grupo Bimbo AR (2025)	08/06/2026
Global	Baking (Bread, Rolls, Cakes, Pastries, Cookies, Morning Goods)	CAGR	%	N/A	N/A	2024–2029	4.7%	Forecast CAGR	GlobalData	Grupo Bimbo AR (2025)	08/06/2026
Global	Snacks (Popcorn, Potato Chips, Processed Snacks)	Market Size	USD Billions	USD	Current (2025 value)	2025	183	Actual	GlobalData	Grupo Bimbo AR (2025)	08/06/2026
Global	Snacks (Popcorn, Potato Chips, Processed Snacks)	CAGR	%	N/A	N/A	2019–2024	4.7%	Historical CAGR	GlobalData	Grupo Bimbo AR (2025)	08/06/2026
Global	Snacks (Popcorn, Potato Chips, Processed Snacks)	CAGR	%	N/A	N/A	2024–2029	3.8%	Forecast CAGR	GlobalData	Grupo Bimbo AR (2025)	08/06/2026
Global	Baking (broader: Bread, Rolls, Cakes, Pastries, Cookies, Savory Biscuits, Morning Goods)	Market Size	USD Billions	USD	Current (2025 value)	2025	674	Actual	GlobalData	Grupo Bimbo EP (Q3 2026)	10/22/2026
Global	Baking	CAGR	%	N/A	N/A	2020–2025	3.8%	Historical CAGR	GlobalData	Grupo Bimbo EP (Q3 2026)	10/22/2026
Global	Baking	CAGR	%	N/A	N/A	2025–2030	3.7%	Forecast CAGR	GlobalData	Grupo Bimbo EP (Q3 2026)	10/22/2026
Global	Snacks	Market Size	USD Billions	USD	Current (2025 value)	2025	110	Actual	GlobalData	Grupo Bimbo EP (Q3 2026)	10/22/2026
Global	Snacks	CAGR	%	N/A	N/A	2020–2025	3.4%	Historical CAGR	GlobalData	Grupo Bimbo EP (Q3 2026)	10/22/2026
Global	Snacks	CAGR	%	N/A	N/A	2025–2030	3.7%	Forecast CAGR	GlobalData	Grupo Bimbo EP (Q3 2026)	10/22/2026
China	Baking (per capita consumption)	Per Capita Consumption	USD per person	USD	Current	2023	25.9	Actual	Euromonitor	Namchow Food Group SR	08/12/2026
China	Baking	Market Size	RMB Billions	CNY	Current	2025	~148.7	Forecast	Euromonitor	Namchow Food Group SR	08/12/2026
China	Baking	CAGR	%	N/A	N/A	2025–2027	~3.5%	Forecast CAGR	Euromonitor	Namchow Food Group SR	08/12/2026
India	Snacks (organized market)	Market Size	INR Crore	INR	Current	2025	50,590.37	Actual	IMARC Group	Gopal Snacks AR	08/17/2026
India	Snacks (organized market)	Market Size	INR Crore	INR	Current	2034 (forecast)	103,556.03	Forecast	IMARC Group	Gopal Snacks AR	08/17/2026
India	Snacks (organized market)	CAGR	%	N/A	N/A	2026–2034	8.28%	Forecast CAGR	IMARC Group	Gopal Snacks AR	08/17/2026
India	Packaged Food (broad)	Market Size	USD Billions	USD	Current	2020	95.45	Actual	IMARC Group	Gopal Snacks AR	08/17/2026
India	Packaged Food (broad)	Market Size	USD Billions	USD	Current	2025	129.18	Actual	IMARC Group	Gopal Snacks AR	08/17/2026
India	Packaged Food (broad)	Market Size	USD Billions	USD	Current	2030 (forecast)	174.84	Forecast	IMARC Group	Gopal Snacks AR	08/17/2026
India	Bakery	Market Size	USD Billions	USD	Current	2025	~15 (partial figure)	Actual	IMARC Group	Grill Splendour AR	09/07/2026
India	Wheat Flour (packaged atta)	Market Size	USD Billions	USD	Current	2025	8.7–8.8	Actual	N/A (secondary research)	Baba Food Processing AR	10/05/2026
India	Wheat Flour (packaged atta)	Market Size	USD Billions	USD	Current	2031–2034 (forecast)	10.9–12.0	Forecast	N/A (secondary research)	Baba Food Processing AR	10/05/2026
India	Wheat Flour (packaged atta)	CAGR	%	N/A	N/A	2026 onwards	3.4%–3.8%	Forecast CAGR	N/A (secondary research)	Baba Food Processing AR	10/05/2026
US	Snacking (broad — all snack categories)	Market Size	USD Billions	USD	Current	2026 (stated as current)	198.2	Actual/Current	Proprietary (Conagra Brands)	Conagra Brands PR	09/23/2026
Canada	Artisanal Baked Goods segment	Market Size	CAD Billions	CAD	N/A	N/A (stated as current)	3.8	Actual	Agriculture and Agri-Food Canada	Purebread Brands IP	08/22/2026
[1] [2] [3] [4] [5] [6] [7] [8]

Notes on the Above Data
Scope definitions matter significantly across sources:

GlobalData (Grupo Bimbo): The "Baking" category includes bread, rolls, cakes, pastries, cookies/sweet biscuits, morning goods, and energy/cereal bars. "Snacks" covers popcorn, potato chips (baked/fried), and processed snacks (corn chips, extruded snacks, pork rinds, tortilla chips). Artisanal bakeries and private label are excluded from market share rankings. [1] [2]

The EP (Q3 2026) and AR figures differ slightly ($674Bn vs. $639Bn for baking) because the EP uses a broader snacks/baking definition that adds savory biscuits. [1] [2]

Euromonitor (China baking): Market size in RMB, current prices; per capita figure in USD. [4]

IMARC (India snacks): INR Crore, current prices, organized market only. [5]

Conagra (US snacking): Broad "snacking" market ($198.2Bn) — this is wider than packaged salty snacks alone and includes meat snacks, popcorn, seeds, dessert snacks, etc. [7]

Agriculture and Agri-Food Canada (artisanal baked goods): This is a sub-segment of Canada's total baked goods category, stated as representing 34% of the total baked goods category. [8]

What Is NOT Stored in Capital IQ (for this request)
The following data points are absent from the Capital IQ context provided:

Gap	Detail
Country-level market size data (value, USD or local currency)	No stored figures for packaged bread/bakery or salty snacks at the individual country level for US, Canada, Mexico, Brazil, Spain, UK, Romania, India, or China on an annual basis (2019–2025 history or 2026–2030 forecasts) from dedicated food industry market research datasets (e.g., Euromonitor country-level, Mintel, Nielsen/NielsenIQ, SPINS, IRI/Circana, Mordor Intelligence, Grand View Research, or equivalent)
Volume data (tonnes, kg per capita, units)	No volume metrics (kg, tonnes, litre equivalents) for packaged bread or salty snacks in any of the nine countries
Annual time-series data (2019–2025)	No year-by-year historical market size series for any individual country in either category
Forecast series to 2030 by country	No country-level annual forecast series (2026–2030) for packaged bread/bakery or salty snacks
Constant vs. current price splits	No data distinguishes real (constant price) from nominal (current price) for any of the bakery/snacks figures found
Salty snacks separately from broader "snacks"	The GlobalData snacks figures bundle popcorn, potato chips, and processed snacks; no standalone "salty snacks" breakout by country is stored
Romania, Spain, UK — any bakery/snacks market data	Zero stored figures for these three countries in the relevant categories
Mexico, Brazil — country-level bakery/snacks data	No country-specific packaged bread or salty snacks market size stored (only global/regional aggregates referencing these markets contextually)
Dedicated Euromonitor, Mintel, or IRI/Circana country datasets	These standard food industry data providers are referenced by name in some documents but their underlying country-level datasets are not loaded into the available context
Market size in local currencies for non-China/India markets	No local-currency figures for US (USD native), Canada (CAD), Mexico (MXN), Brazil (BRL), Spain (EUR), UK (GBP), or Romania (RON)
In summary: Capital IQ, as represented in the available context, contains only global aggregate baking and snacks market sizes (from GlobalData via Grupo Bimbo filings), a China baking figure (Euromonitor via Namchow), and India snacks/packaged food figures (IMARC via Indian company annual reports). The granular country-by-country, year-by-year, value-and-volume dataset your CFA Research Challenge requires for the nine specified markets is not stored in the provided Capital IQ context. To obtain it, you would need to query dedicated food industry market research datasets within the S&P Global platform (e.g., Euromonitor Passport, Mintel GNPD, or equivalent datasets if licensed).


Sources
Grupo Bimbo, S.A.B. de C.V. EP - 2026-10-22
Grupo Bimbo, S.A.B. de C.V. AR - 2026-08-06
Grupo Bimbo, S.A.B. de C.V. AR - 2026-09-30
Namchow Food Group (Shanghai) Co., Ltd. SR - 2026-08-12
Gopal Snacks Limited AR - 2026-08-17
Grill Splendour Services Limited AR - 2026-09-07
Conagra Brands, Inc. PR - 2026-09-23
Purebread Brands Inc. IP - 2026-08-22

Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
