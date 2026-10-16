---
Writer: AI-compiled (Claude)
Source:
  - filings/bmv/Reporte_Definitivo_BMV_Septiembre_12_Español.pdf
  - filings/annual/informe-anual-grupo-bimbo-2024-Acciones-que-transforman.pdf
  - filings/annual/anexos_datos desempeño_VF JULIO.pdf
  - filings/annual/GB-INFORME ANUAL_30.pdf
  - filings/annual/Grupo-Bimbo-Informe-Anual-2016.pdf
  - filings/quarterly/ER_BIMBO_4T10_ESP_0.pdf
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/bmv/Reporte Anual 2022 VF.pdf
  - filings/bmv/GrupoBimbo_BVM_RA_20020624_esp_0.pdf
tags: [Financials, volume-disclosure]
---

# Volume disclosure audit: what Bimbo reports, and what it does not

**Question.** The mentor (Alan) expected sales volume to be reported to the BMV. The team asked for a volume × price forecast. This article records what 237 text-extracted documents (BMV annual and quarterly filings, results releases, integrated and sustainability reports, 1998–2026) contain on physical volume. 13 batches were searched; each file was classified as numeric volume, qualitative only, or none. Original PDFs are the source of record. Page numbers are PDF page indexes of the extracted text.

**Verdict.** ==Bimbo does not publish sales volume (tonnes, units, cases, kilos) in any BMV filing or results release==. The regulator's form has the field, and the company prints zero in it. The only recurring physical series is production tonnage from the sustainability annexes. `[sourced]` batch review, 13 batches, documents above.

## 1. The BMV form has a VOLUMEN column and Bimbo fills it with 0

- The BMV quarterly form "Distribución de ingresos por producto" carries columns VOLUMEN, IMPORTE, % de participación en el mercado, marcas, clientes. `[sourced]` `filings/bmv/Reporte_Definitivo_BMV_Septiembre_12_Español.pdf` p.88.
- 3Q12 consolidated: pan blanco y dulce, domestic MXN 49,110,109 thousand and foreign subsidiaries MXN 78,553,825 thousand, total MXN 127,663,934 thousand; ==VOLUMEN = 0 on every row and market share = 0== `[sourced]` same file, p.88.
- The same zero-volume pattern appears in the product tables of the 2008–2015 quarterly filings, and the installed-capacity tables of 2009 and 2011 are also zero. `[unverified]` batch review (3Q12 verified by hand; the other quarters are agent-read).
- From 2018 the product-distribution tables disappear from the filings reviewed; volume then appears only in narrative. `[unverified]` batch review.

## 2. Numeric volume that does exist

| Metric | Value | Period | Scope | Source | Caveat |
|---|---|---|---|---|---|
| Tonnes produced (TPE) | 4,693,880 / 5,025,741 / 5,164,538 / 5,268,678 / 5,310,043 / 5,831,747 | 2019 / 2020 / 2021 / 2022 / 2023 / 2024 | Group | `[sourced]` IA24 p.285, p.289 | Production, not sales; energy-intensity denominator |
| Tonnes produced (TPE) | 5,378,788 | 2025 | Group | `[sourced]` `filings/annual/anexos_datos desempeño_VF JULIO.pdf` | 2025 vs 2024 = -7.8% `[calc]`; scope excludes some acquisitions |
| Tonnes produced, regional | Mexico 1,776,962; North America 2,225,295; Latin America 722,658; Europe-Asia-Africa 1,106,832 | 2024 | Region | `[sourced]` IA24 p.289 | Sums to 5,831,747 |
| Tonnes produced, regional | Mexico 1,695,136; North America 2,119,520; Latin America 645,106; Europe-Asia-Africa 808,916 | 2022 | Region | `[sourced]` IA24 p.240 | Sums to 5,268,678 |
| Daily output | ~60 million pieces | 2014 | Group | `[unverified]` BMV annual 2014 p.9, agent-read | Unit "piezas", undefined |
| Daily output | 40m / 46m / 48m packages | FY2016 / FY2019 / FY2021 | Group | `[unverified]` BMV annual reports, agent-read | Unit "paquetes" |
| Daily output | ">31 million equivalent units" | FY2022, FY2023, FY2025 | Group | `[sourced]` RA25 p.81 | Different unit; not comparable with the line above |
| Volume growth | +4.4% (full-year) | FY2010 | United States | `[sourced]` `filings/quarterly/ER_BIMBO_4T10_ESP_0.pdf` p.2 | US only; US peso sales fell 4.0% |
| Volume growth | +1.9% | FY2016 | Group (unconfirmed) | `[sourced]` `filings/annual/Grupo-Bimbo-Informe-Anual-2016.pdf` p.13 | Chairman letter; scope not labelled |
| Volume declines | -23% and -9% (December 2002) | 2002 | Argentina and Venezuela | `[sourced]` `filings/bmv/GrupoBimbo_BVM_RA_20020624_esp_0.pdf` and RA 2003 p.72 | Crisis period |
| Volume growth | +12% | 1Q04 | Latin America | `[unverified]` releases batch 1 | Agent-read |
| Share of volume through traditional trade | 80% / 75% / 70% / 67% | various years 2008-2013 | Mexico | `[unverified]` annual reports batch 2 | Only numeric volume-mix series |
| Monthly units, single brands | 126 million Thomas' muffins (US); 35 million+ Gansitos (Mexico) | c.2009 | Product | `[unverified]` RA 2009 p.10, agent-read | Year not stated |

**TPE restatements.** The FY2022 integrated report prints tonnes produced of 4,597,432 / 4,979,811 / 5,092,028 / 5,201,449 for 2019–2022 `[sourced]` `filings/annual/GB-INFORME ANUAL_30.pdf` p.241. The 2024 report prints 4,693,880 / 5,025,741 / 5,164,538 / 5,268,678 for the same years `[sourced]` IA24 p.285. ==The series was revised up by 0.9% to 2.1% between vintages== `[calc]`. The label also changes: "Toneladas Producidas" in the 2021 and 2022 reports against "Toneladas de Producto Empacado" in the 2025 annex footnote (unresolved).

## 3. What the company says about why it does not publish volume

- The 2025 data annex states that the company cannot obtain a homogeneous figure in equivalent units across products, even when it asks organizations for it. `[sourced]` `filings/annual/anexos_datos desempeño_VF JULIO.pdf` p.4, agent-extracted.
- The BMV annual report 2022 defines "unidades equivalentes" as a volume measure complementary to kilos, pieces and money, equating each product to a 680 g sliced-bread pack, but prints no series. `[sourced]` `filings/bmv/Reporte Anual 2022 VF.pdf`.
- The 2002 BMV annual report says capacity is measured in hours (not tonnes) because the product mix makes weights non-comparable. `[sourced]` RA 2002 p.67.
- Capacity-utilization tables exist but the hours basis changed (134, 150, then 168 hours per week), so they are not comparable across years; the 2023 report swaps them for an OEE table. `[unverified]` annual reports batches 2 and 3.

## 4. Qualitative only

- From 2011 on, no results release or BMV filing gives a volume growth percentage. Volume is named as a driver next to price/mix and FX, never split out. Examples: 2Q26 "growth in volume and favorable price mix"; FY2019 Mexico "strong volume growth". `[sourced]` releases and filings reviewed; 160 lines with "volúmenes" and a digit were re-checked and are sales percentages, not volume.
- The 4Q11 release bridges sales growth into acquisitions (Sara Lee 32.0%, Iberia/IO 14.3%) and organic (13.2%), but never splits organic into volume and price. `[unverified]` releases batch 2.
- Ex-FX sales growth is published (for example FY21 +9.3%, 4Q23 +10.7%, 3Q25 +9.1%), with no volume line to subtract. `[unverified]` releases batch 3.

## 5. What this means for a volume × price forecast

- ==There is no clean historical volume series to forecast==. Anyone stating one is deriving it.
- Options, in order of defensibility: (1) use group TPE (2019–2025) as a production proxy, with the scope and restatement caveats above; (2) use regional TPE (2022 and 2024 only) to split growth by region (North America +5.0%, Mexico +4.8%, Latin America +12.0%, Europe-Asia-Africa +36.8% from 2022 to 2024 `[calc]`, with Europe-Asia-Africa inflated by acquisitions); (3) model sales by region with explicit price and volume assumptions labelled `[assumption]`.
- ==North America TPE rose about 5% from 2022 to 2024 while reported sales fell and management said US volumes were still declining== (see [[bimbo-volume-and-price-disclosures]]). Either TPE scope captured acquired plants or production moved ahead of sales; the team should not read TPE as sales volume.
- Anyone presenting this to judges should say: Bimbo reports no volume; our forecast uses production tonnage and stated assumptions.

## 6. Gaps and what was not checked

- The original BMV XBRL instance files (not the PDF renderings) were not available. Tagged facts may exist that the PDFs do not show.
- Image-only pages (a few per annual report, mostly signatures and scanned statements) were not read.
- Investor presentations (2024–2026) were not part of this audit; see [[bimbo-investor-presentations-2024-2026]].
- Classification by the 13 batches is agent-read text; only the 3Q12 form, the 2022 and 2024 TPE tables and the FY2010 US volume were verified by hand or against page images.

## Connections

- [[bimbo-volume-and-price-disclosures]] covers what management said on calls; its finding of no regional volume matches this audit.
- [[bimbo-history-2014-2020]] reports a group tonnage series (3.85 to 5.03 million tonnes, FY14–FY20); that series is from the same sustainability data and should be read with the restatement note above.
- [[bimbo-business-model]] and [[bimbo-cross-source-connections]] state that volume is never disclosed. This audit confirms it and adds that the BMV form carries the field at zero.
- [[ciq-guidance-and-estimate-history]] has no volume estimates for the same reason.

## Key Takeaways

- ==The BMV form has a VOLUMEN field and Bimbo reports 0 (3Q12 p.88, verified).== The obligation is formal, not filled.
- Sales volume is not published in any of 237 documents reviewed. Volume appears only in words, bundled with price/mix and FX.
- Group production tonnes (TPE) 2019–2025 are the only recurring series: 4.69 to 5.83 million tonnes, then 5.38 in 2025 (-7.8%). Regional TPE exists for 2022 and 2024.
- TPE was restated up 0.9–2.1% between report vintages and its label and scope change; treat it as a proxy, not volume sold.
- The 48m-to-31m daily output drop in 2022 is a unit change (packages to equivalent units), not a volume decline.
- A volume × price forecast must be built on proxies and labelled assumptions; judges should hear that explicitly.
