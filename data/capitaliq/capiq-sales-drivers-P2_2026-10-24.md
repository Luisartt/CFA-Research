# Capital IQ ChatIQ answer - block P2 (peers' organic growth: Gruma, Mondelez, Grupo Nutresa)

Prompt: block P2 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (line 320).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; tables kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- **Only Mondelez has data.** Gruma and Grupo Nutresa: N/A by segment. Everything below stays [unverified] until checked in Mondelez's own 10-K / earnings releases (SEC EDGAR, public).
- **Rows to discard (break the STRICT rule or are internally inconsistent):**
  - FY2024 and FY2025 segment rows are identical (LatAm +4.6%, AMEA +5.7%, Europe +8.6%, North America (1.9)%), and so are FY2024 and FY2025 EM +7.2% / DM +2.5%. ChatIQ notes this itself. At most one year is right; we cannot tell which from this answer.
  - Latin America FY2020 +3.7% is "implied from EM/DM split", i.e., computed by ChatIQ. Discard.
  - Europe FY2023 gives two values: "+9.0% (5-yr CAGR table)" and "+15.4% (Q3'23 quarter)". Neither is the FY2023 annual figure. Discard.
- **Rows that may be usable after checking the source:** FY2019 LatAm/EM/DM; FY2020-FY2023 North America and Europe (sourced to a 07/31/2025 investor presentation, likely a multi-year chart); FY2021-FY2023 EM/DM; 9M2025 EM/DM; Q4 2025 by segment; FY2025 consolidated +4.3%. The FY2025 10-K (ChatIQ source [3], filed 2026-02-04) is the place to confirm the segment figures.
- **Grupo Nutresa:** consolidated organic figures quoted from calls (FY2021 13.7%; 1Q22 12.7%; 9M22 international 20.6% in USD) are [guidance, unverified]. Its reporting segments are product categories, not geographies.
- **Gruma:** "no organic metric printed" is ChatIQ's statement. Not checked; [unverified].
- **Part 2 (packaged-bread competitors) is not usable.** The screen returned only Bimbo. The general peer set is mostly meat and protein companies. The "practical note" competitor list (Harry-Brot, Warburtons, La Boulangere, Dobrogea, etc.) comes from ChatIQ's general knowledge, not Capital IQ. Our own peer list is already in `research/industry.md`.
- **Relevance:** Mondelez is snacks and confectionery, not bread. Whether it works as an industry proxy for Bimbo's regions is a team decision.

---

```text
CFA Research Challenge — Grupo Bimbo Peer Organic Growth Analysis
Critical Methodology Note
Gruma does not publish an "organic growth" or "growth ex-FX / ex-M&A" metric by geographic segment. Its earnings releases and filings report only total net sales and YoY % change by subsidiary (GRUMA USA, GIMSA, Gruma Europe, Gruma Centroamérica, Gruma Asia & Oceania). No organic growth figure stripping out FX or M&A is printed. All Gruma values below are N/A per the strict instruction.

Grupo Nutresa does not publish an organic growth figure by geographic segment either. Its investor presentations show total sales in COP and USD by business unit and geography, with FX effects noted qualitatively but no printed organic-growth percentage by segment. All Nutresa geographic-segment organic growth values are N/A.

Mondelēz International is the only company among the three that prints a formal "Organic Net Revenue Growth" metric by geographic segment in its earnings releases and SEC filings.

Part 1 — Organic Growth Table
Mondelēz International — "Organic Net Revenue Growth" by Segment (as reported)
Definition (company's own wording): "Organic Net Revenue is defined as net revenues excluding, when they occur, the impacts of acquisitions, divestitures, short-term distributor agreements related to the sale of a business and currency-related items." [1] [2]

Mondelēz reports four geographic segments: Latin America, AMEA, Europe, North America, plus an Emerging Markets / Developed Markets cross-cut. [3]

Company	Segment	Indicator (as named)	Period	Value	Definition Quote (≤25 words)	Document	Date
Mondelēz International	Latin America	Organic Net Revenue Growth	FY 2019	+3.0%	"Net revenues excluding…acquisitions, divestitures, short-term distributor agreements…and currency-related items."	10-K / Annual Investor Presentation [4]	04/27/2023
Mondelēz International	Developed Markets (incl. Europe ex-EM, North America)	Organic Net Revenue Growth	FY 2019	+2.7%	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	FY 2019	+7.5%	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	North America	Organic Net Revenue Growth	FY 2020	+5.2%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Europe	Organic Net Revenue Growth	FY 2020	+7.1%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Latin America	Organic Net Revenue Growth	FY 2020	+3.7% (implied from EM/DM split)	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	FY 2021	+12.0%	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	Developed Markets	Organic Net Revenue Growth	FY 2021	+4.5%	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	North America	Organic Net Revenue Growth	FY 2021	+7.3%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Europe	Organic Net Revenue Growth	FY 2021	+10.3%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	FY 2022	+22.0%	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	Developed Markets	Organic Net Revenue Growth	FY 2022	+7.0%	Same definition	Investor Presentation [4]	04/27/2023
Mondelēz International	North America	Organic Net Revenue Growth	FY 2022	+14.5%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Europe	Organic Net Revenue Growth	FY 2022	+12.4%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	FY 2023	+20.4%	Same definition	10-K [6]	04/03/2025
Mondelēz International	Developed Markets	Organic Net Revenue Growth	FY 2023	+11.1%	Same definition	10-K [6]	04/03/2025
Mondelēz International	North America	Organic Net Revenue Growth	FY 2023	+9.5%	Same definition	Investor Presentation [5]	07/31/2025
Mondelēz International	Europe	Organic Net Revenue Growth	FY 2023	+9.0% (5-yr CAGR table) / +15.4% (Q3'23 quarter)	Same definition	Investor Presentation [5] ; Transcript [7]	07/31/2025
Mondelēz International	Latin America	Organic Net Revenue Growth	FY 2024	+4.6%	Same definition	10-K / FIN SUPP [8]	12/31/2025
Mondelēz International	AMEA	Organic Net Revenue Growth	FY 2024	+5.7%	Same definition	10-K / FIN SUPP [8]	12/31/2025
Mondelēz International	Europe	Organic Net Revenue Growth	FY 2024	+8.6%	Same definition	10-K / FIN SUPP [8]	12/31/2025
Mondelēz International	North America	Organic Net Revenue Growth	FY 2024	(1.9)%	Same definition	10-K / FIN SUPP [8]	12/31/2025
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	FY 2024	+7.2%	Same definition	EP / FIN SUPP [8] [9]	02/03/2026
Mondelēz International	Developed Markets	Organic Net Revenue Growth	FY 2024	+2.5%	Same definition	EP / FIN SUPP [8] [9]	02/03/2026
Mondelēz International	Latin America	Organic Net Revenue Growth	FY 2025	+4.6%	Same definition	FIN SUPP [8]	12/31/2025
Mondelēz International	AMEA	Organic Net Revenue Growth	FY 2025	+5.7%	Same definition	FIN SUPP [8]	12/31/2025
Mondelēz International	Europe	Organic Net Revenue Growth	FY 2025	+8.6%	Same definition	FIN SUPP [8]	12/31/2025
Mondelēz International	North America	Organic Net Revenue Growth	FY 2025	(1.9)%	Same definition	FIN SUPP [8]	12/31/2025
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	FY 2025	+7.2%	Same definition	EP [10]	02/03/2026
Mondelēz International	Developed Markets	Organic Net Revenue Growth	FY 2025	+2.5%	Same definition	EP [10]	02/03/2026
Mondelēz International	Emerging Markets	Organic Net Revenue Growth	9M 2025	+6.9%	Same definition	10-Q [1]	10/28/2025
Mondelēz International	Developed Markets	Organic Net Revenue Growth	9M 2025	+2.1%	Same definition	10-Q [1]	10/28/2025
Mondelēz International	Latin America	Organic Net Revenue Growth	Q4 2025	+4.4%	Same definition	ER [10]	02/03/2026
Mondelēz International	AMEA	Organic Net Revenue Growth	Q4 2025	+7.5%	Same definition	ER [10]	02/03/2026
Mondelēz International	Europe	Organic Net Revenue Growth	Q4 2025	+8.3%	Same definition	ER [10]	02/03/2026
Mondelēz International	North America	Organic Net Revenue Growth	Q4 2025	(0.5)%	Same definition	ER [10]	02/03/2026
Note on FY 2024 vs. FY 2025 reconciliation: The FIN SUPP schedule 4b (filed 12/31/2025) [8] shows the full-year 2025 organic growth by segment as: Latin America +4.6%, AMEA +5.7%, Europe +8.6%, North America (1.9)%. The FY 2024 comparatives from the same schedule are: Latin America +4.6%, AMEA +5.7%, Europe +8.6%, North America (1.9)% — these numbers appear identical in the retrieved chunk. The Q4 2025 earnings release [10] confirms FY 2025 consolidated Organic Net Revenue Growth of +4.3%, Emerging Markets +7.2%, Developed Markets +2.5%. The segment-level FY 2025 breakdown by the four reportable segments is available in the 10-K [3]

9M 2026 (through September 2026): Not available in the context — Mondelēz has not yet reported 9M 2026 results as of the context date (10/25/2026). N/A.

Gruma — Organic Growth by Geographic Segment
Gruma does not print an organic growth or ex-FX/ex-M&A metric. Its earnings releases report total net sales and YoY % changes by subsidiary in USD. [11] [12] [13]

Company	Segment	Indicator (as named)	Period	Value	Note
Gruma	All segments (GRUMA USA, GIMSA, Europe, Centroamérica, Asia & Oceania)	Organic growth / growth ex-FX	FY 2019–FY 2025 & 9M 2026	N/A	Company does not print this metric
Grupo Nutresa — Organic Growth by Geographic Segment
Nutresa reports sales by geography (Colombia, U.S., Central America, Chile, Mexico, etc.) and by business unit in COP and USD. In Q3 2022 earnings, management referenced "organic growth was 20.6% in dollars" for international sales (9M 2022) [14] and in Q4 2021 "organically, the growth was 13.7%" for full-year total [15] and in Q1 2022 "organic sales would be $345 million with a growth of 12.7%" [16] However, these are consolidated organic figures (excluding M&A), not broken out by geographic segment. No geographic-segment-level organic growth is printed.

Company	Segment	Indicator (as named)	Period	Value	Note
Grupo Nutresa	All geographic segments	Organic growth by geography	FY 2019–FY 2025 & 9M 2026	N/A	Not printed by segment; only consolidated organic figures mentioned occasionally in transcripts
The last available full-year data in the context is FY 2025 (annual report filed 10/13/2026). [17] Nutresa's segment structure is by product category (Biscuits, Cold Cuts, Chocolate, Coffee, TMLUC, Ice Cream, Pasta, etc.), not by geography, for financial reporting purposes. [17]

Part 2 — Capital IQ Packaged-Bread Competitors of Grupo Bimbo
The S&P Capital IQ screener returned only Grupo Bimbo itself when filtering for "Bread and Bakery Products" industry companies tagged as competitors of Grupo Bimbo in Mexico, Brazil, Spain, Romania, or the UK. The peer list retrieved for Grupo Bimbo (ranked competitors in Capital IQ) does not include any company classified specifically under packaged bread operating in those five geographies.

Source: S&P Capital IQ

The Capital IQ general peer set for Grupo Bimbo includes:

Gruma, S.A.B. de C.V.
Sigma Foods, S.A.B. de C.V.
MBRF Global Foods Company S.A.
Industrias Bachoco, S.A.B. de C.V.
Minerva S.A.
Grupo Nutresa S. A.
Alicorp S.A.A.
Hormel Foods Corporation
Tyson Foods, Inc.
The J. M. Smucker Company
None of these are tagged under the "Bread and Bakery Products" / packaged bread sub-industry with geographic presence specifically in Mexico, Brazil, Spain, Romania, or the UK in the screener results returned. The screener for "packaged bread competitors of Grupo Bimbo in Mexico, Brazil, Spain, Romania or UK" returned only Grupo Bimbo itself (industry: Bread and Bakery Products, Latin America and Caribbean geography).

Practical note for the CFA team: Grupo Bimbo's direct packaged-bread competitors in those markets (e.g., Bimbo Bakeries USA rivals, Flowers Foods, Harry-Brot in Germany/Europe, Warburtons in UK, Grupo La Boulangère in France/Spain, Dobrogea in Romania) are not surfaced in Capital IQ's peer tagging for Grupo Bimbo as of the data available in this context. A manual screen within Capital IQ using the GICS sub-industry "Packaged Foods & Meats" or SIC 2051 (Bread, Cake, and Related Products) filtered by those geographies would be the recommended next step on-platform.

Summary of Key Gaps
Item	Status
Gruma organic growth by segment (2019–2025, 9M 2026)	N/A — metric not printed by company
Grupo Nutresa organic growth by geographic segment	N/A — metric not printed by segment
Mondelēz organic growth by segment (FY 2019–FY 2025)	Available — printed in earnings releases, 10-K, 10-Q
Mondelēz 9M 2026 organic growth	N/A — not yet reported
Capital IQ packaged-bread competitors of Bimbo in MX/BR/ES/RO/UK	Not returned by screener; only Bimbo itself surfaced
Source: S&P Capital IQ


Sources
Mondelez International, Inc. 10-Q - 2025-10-28
Mondelez International, Inc. Misc. - 2025-10-27
Mondelez International, Inc. 10-K - 2026-02-04
Mondelez International, Inc., Q1 2023 Earnings Call, Apr 27, 2023 - 2023-04-27
Mondelez International, Inc. IP - 2025-07-31
Mondelez International, Inc. Misc. - 2025-04-03
Mondelez International, Inc., Q3 2023 Earnings Call, Nov 01, 2023 - 2023-11-01
Mondelez International, Inc. FIN SUPP - 2025-12-31
Mondelez International, Inc. EP - 2026-02-03
Mondelez International, Inc. ER - 2026-02-03
Gruma, S.A.B. de C.V. Other Financials - 2026-02-19
Gruma, S.A.B. de C.V. EP - 2026-02-18
Gruma, S.A.B. de C.V. EP - 2025-11-11
Grupo Nutresa S. A., Q3 2022 Earnings Call, Oct 31, 2022 - 2022-10-31
Grupo Nutresa S. A., Q4 2021 Earnings Call, Feb 28, 2022 - 2022-02-28
Grupo Nutresa S. A., Q1 2022 Earnings Call, Apr 29, 2022 - 2022-04-29
Grupo Nutresa S. A. FIN SUPP - 2026-10-13

Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
