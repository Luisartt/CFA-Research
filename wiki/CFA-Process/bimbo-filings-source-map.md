---
Writer: AI-compiled (Claude)
Source:
  - filings/annual/IA25_GB_Celebramos_ESP_200826.pdf
  - filings/annual/IA25_GB_EEFF_V10.pdf
  - filings/annual/bimbo_informe_anual2021.pdf
  - filings/annual/Informe Anual Grupo Bimbo 2023 - Detrás de Nuestras Acciones_2.pdf
  - filings/annual/informe-anual-grupo-bimbo-2024-Acciones-que-transforman.pdf
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/bmv/GB_RA_2024_BMV_VFF1_0.pdf
  - filings/bmv/Reporte Anual 2023_XBRL_VF.PDF
  - filings/bmv/Reporte Anual 2022 VF.pdf
  - filings/bmv/Reporte Anual 2021_0.pdf
  - filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Jun_26.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf
  - filings/financing/Grupo Bimbo - Sustainable Financing Framework (April 2023)_ESP_SELLADO.pdf
tags: [CFA-Process, source-map]
---

# BIMBOA filings source map

Inventory of every file in `filings/` as of ==2026-10-07==. Latest data point: ==2Q26 (period ended 2026-06-30), release dated 2026-07-23== `[sourced]` 2T26 release p.1 (`filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf`). Cite filings by the short names in the first column. Page counts come from the text extraction of each PDF `[calc]`.

- Total files: ==48 PDFs== plus `.gitkeep` `[calc]` directory listing, 2026-10-07. Breakdown: annual 5, bmv 23 (5 annual reports + 18 quarterly XBRL filings), quarterly 19, financing 1 = 48 `[calc]`.
- Language: ==all Spanish==; no English document in `filings/` `[sourced]` file names and text extraction.
- Currency/standard: MXN, IFRS, fiscal year end 12-31 `[sourced]` company-profile.yaml.
- Related: [[cfa-challenge-timeline]], [[cfa-research-standards-checklist]].

## 1. Annual reports to the BMV (Anexo N, regulatory)

Regulatory filing under the Mexican securities regime; contains business description, risk factors, MD&A, governance, ownership, debt, and full consolidated statements. Best primary source for structure, segment, ownership and risk facts.

| Short name | Path | Period | Pages | Use | Reliability |
|---|---|---|---|---|---|
| RA25 | `filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf` | FY2025 (to 2025-12-31) | 342 `[calc]` (cover shows 205 form pages `[sourced]` RA25 p.1) | Latest full-year base: segments, risks, debt, governance, statements | Official BMV filing; statements audited (auditor: Ernst & Young) `[sourced]` EEFF25 p.5 |
| RA24 | `filings/bmv/GB_RA_2024_BMV_VFF1_0.pdf` | FY2024 | 347 `[calc]` | Prior-year base, restatement checks | Official, audited |
| RA23 | `filings/bmv/Reporte Anual 2023_XBRL_VF.PDF` | FY2023 | 361 `[calc]` | 3-year trend | Official, audited |
| RA22 | `filings/bmv/Reporte Anual 2022 VF.pdf` | FY2022 | 335 `[calc]` | 5-year trend | Official, audited |
| RA21 | `filings/bmv/Reporte Anual 2021_0.pdf` | FY2021 | 325 `[calc]` | 5-year trend start | Official, audited |

- FY2021 is the earliest full year in `filings/`; earlier annual reports exist only outside the project folder (section 6).

## 2. Integrated / annual reports (corporate publications)

Glossy investor-facing reports with management narrative, strategy, ESG and sustainability data. Not regulatory-form; useful for strategy language and KPIs, weaker for audited detail.

| Short name | Path | Period | Pages | Use | Reliability |
|---|---|---|---|---|---|
| EEFF25 | `filings/annual/IA25_GB_EEFF_V10.pdf` | FY2025 consolidated financial statements | 88 `[calc]` | Audited statements and notes; auditor's opinion at p.5 | ==Audited== (EY independent auditor's report) `[sourced]` EEFF25 p.5 |
| IA25 | `filings/annual/IA25_GB_Celebramos_ESP_200826.pdf` | FY2025 integrated report ("Celebramos", 80th anniversary) | 182 `[calc]` | Strategy, brands, ESG narrative, CEO letter | Company publication; file stamp 200826 suggests a 2026-08-20 version `[unverified]` |
| IA24 | `filings/annual/informe-anual-grupo-bimbo-2024-Acciones-que-transforman.pdf` | FY2024 integrated report | 402 `[calc]` | Strategy and ESG narrative, 2024 | Company publication |
| IA23 | `filings/annual/Informe Anual Grupo Bimbo 2023 - Detrás de Nuestras Acciones_2.pdf` | FY2023 integrated report | 392 `[calc]` | Strategy and ESG narrative, 2023 | Company publication |
| IA21 | `filings/annual/bimbo_informe_anual2021.pdf` | FY2021 annual report | 260 `[calc]` | Strategy and ESG narrative, 2021 | Company publication |

- ==No FY2022 integrated report== and no FY2020-or-earlier file in this folder `[sourced]` directory listing.

## 3. BMV quarterly financial filings (XBRL "Reporte Definitivo")

Quarterly information filed on the BMV in XBRL format: MD&A section [105000], general information [110000], balance sheet, income statement, cash flows, notes. Same structure each quarter, so best for quarter-by-quarter series and for tying out the press-release figures.

| Period | Files (suffix) | Pages each (range) | Reliability |
|---|---|---|---|
| 1Q22 | `Mzo_22` | 181 `[calc]` | Quarterly, interim; audit status not stated in extract `[unverified]` |
| 2Q22 / 3Q22 / 4Q22 | `Jun_22`, `Sep_22`, `Dic_22` | 176 / 166 / 176 `[calc]` | Same; `Dic` file is the Q4 interim filing, not the audited annual report |
| 1Q23 – 4Q23 | `Mar_23`, `Jun_23`, `Sep_23`, `Dic_23` | 173 / 189 / 189 / 186 `[calc]` | Same |
| 1Q24 – 4Q24 | `Mar_24`, `Jun_24`, `Sep_24`, `Dic_24` | 178 / 178 / 179 / 189 `[calc]` | Same |
| 1Q25 – 4Q25 | `Mar_25`, `Jun_25`, `Sep_25`, `Dic_25` | 152 / 155 / 155 / 164 `[calc]` | Same |
| 1Q26 | `Mar_26` | 152 `[calc]` | Same |
| ==2Q26== | `Jun_26` | 153 `[calc]` | Same; latest filing in the project; header "Trimestre: 2 Año: 2026" `[sourced]` BMV Jun-26 p.1 |

- Full path pattern: `filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_<Mzo|Mar|Jun|Sep|Dic>_<YY>.pdf`. Naming is inconsistent: 2022 Q1 is `Mzo_22`, later years use `Mar_YY`.
- Count: 18 files (4 quarters x 4 years 2022-2025 = 16, plus 1Q26 and 2Q26) `[calc]`. No gaps in 2022-2Q26.
- The searchable text for the 4Q25 XBRL filing states auditors' remuneration for 2025 (MXN 133,749, units as stated in the filing, not verified here) `[sourced]` BMV Dic-25 filing, "remuneración de los auditores" note `[unverified]` page.
- Neither the 4Q25 nor 2Q26 XBRL text nor the 2T26/4T25 releases contain the word "audited" in the extracted text `[calc]` text search; treat interim figures as ==unaudited== until confirmed.

## 4. Quarterly earnings releases ("Grupo Bimbo Reporta Resultados del nTyy")

Press releases with consolidated and regional results, margin bridge, net debt, and guidance language. Short (9-13 pages), the fastest source for the quarterly trend. File names are URL-encoded (`%20`).

| Fiscal year | Releases in `filings/quarterly/` | Pages |
|---|---|---|
| 2021 | 4T21 only | 10 `[calc]` |
| 2022 | 1T22, 2T22, 3T22, 4T22 | 11 / 10 / 10 / 13 `[calc]` |
| 2023 | 1T23, 2T23, 3T23, 4T23 | 9 / 9 / 9 / 11 `[calc]` |
| 2024 | 1T24, 2T24, 3T24, 4T24 | 9 / 9 / 10 / 11 `[calc]` |
| 2025 | 1T25, 2T25, 3T25, 4T25 | 9 / 9 / 9 / 12 `[calc]` |
| 2026 | 1T26, 2T26 | 10 / 9 `[calc]` |

- Count: 19 releases, 4T21 to 2T26, consecutive `[calc]`. Use: [[bimbo-quarterly-trend-4q21-2q26]], [[bimbo-guidance-2026]].
- Latest: 2T26 released 2026-07-23; call held 2026-07-23 17:00, replay until 2026-07-30 `[sourced]` 2T26 release pp.1, 9. The call itself is not in the folder.
- Reliability: company-prepared, unaudited by nature of a results release (the releases do not carry an audit opinion) `[calc]` text search. Management non-IFRS metrics (adjusted EBITDA, etc.) are company-defined; see [[bimbo-ifrs-adjustments]].

## 5. Financing

| Short name | Path | Period | Pages | Use | Reliability |
|---|---|---|---|---|---|
| SFF23 | `filings/financing/Grupo Bimbo - Sustainable Financing Framework (April 2023)_ESP_SELLADO.pdf` | April 2023 | 36 `[calc]` | Use-of-proceeds categories, KPIs, targets; see [[bimbo-sustainable-financing]] | Company framework (Spanish, stamped "SELLADO"); ==image-only PDF, no extractable text== (text extraction returned empty) `[calc]`. Needs OCR or manual reading before quoting. |

- The second-party opinion (SPO) for this framework exists outside the project folder (section 6) but is not in `filings/`.

## 6. Material found outside `filings/` (not in the project)

An additional working directory, `D:\CFA Research\CFA\Reportes BIMBO`, holds a wider library not copied into the project. Treat as unreviewed until moved to `filings/` or `raw/`.

- Annual/integrated reports 1998-2011, 2016-2020 (several), 2017 integrated + summary, 2018 annual + summary, 2019, 2020, plus GRI tables, performance-data annexes and "Enfoque de gestión" sustainability documents `[sourced]` directory listing.
- BMV filings: annual reports 2008, 2010, 2014, 2015, 2017, 2018, 2020 and 2024 (duplicate of RA24); quarterlies 2Q16, 1Q17, 2Q17, 1Q18, 1Q20 (XBRL/definitive) and 3Q14 `[sourced]` directory listing.
- Sustainable Financing Framework second-party opinion (April 2023) `[sourced]` directory listing.
- Use: history before 2021 (pre-2021 margin cycle and acquisition history, if the team needs it). Not yet reviewed; do not cite as a source until read.

## 7. Coverage gaps

| # | Gap | Impact | Suggested fix (public sources only) |
|---|---|---|---|
| 1 | ==No earnings-call transcripts or audio== (incl. 2Q26 call held 2026-07-23) `[sourced]` 2T26 release p.9 | Cannot quote management tone, guidance Q&A or capex commentary | Check Grupo Bimbo investor-relations page for webcast replays; transcribe public audio only |
| 2 | ==No investor presentations or earnings slides== | No segment charts, no medium-term targets beyond release text | Download quarterly presentations from IR site |
| 3 | ==No consensus estimates, broker notes or price data== | `[unverified]` on market expectations; no multiples, beta or share-price history | Public price history, public consensus snapshots; team decides what to use |
| 4 | ==No English-language documents== | Report must be in English; Spanish terms need consistent translation | English releases and annual report on IR site; confirm translations against them |
| 5 | No 2021 quarterly releases except 4T21 (1T21-3T21 missing) | No 2021 quarterly series; quarterly trend starts 4Q21 | Download from IR archive if needed |
| 6 | No FY2022 integrated report in `filings/annual/` (FY2022 is covered only by RA22 and quarterly filings) | ESG/strategy narrative gap for 2022 | Download from IR site if ESG time series needed |
| 7 | No second-party opinion for the 2023 financing framework in `filings/` | Cannot check independent assessment | Copy SPO from `D:\CFA Research\CFA\Reportes BIMBO\Marco de Financiamiento Sustentable` |
| 8 | SFF23 PDF has no extractable text | Cannot search or cite pages | OCR |
| 9 | No FY2025 audited statements for subsidiaries or segment-level audited data | Segment margins come from company disclosures only | Not obtainable; note limit in the report |
| 10 | No peer filings (Mondelez, Grupo Herdez, Flowers Foods, etc.) in `filings/` | Peer table has no primary support | Peer filings from each issuer's IR site; see Industry domain |
| 11 | No macro / FX / commodity series (MXN/USD, wheat) | Forecast drivers lack primary data | Central bank and exchange public series; see Macro domain |
| 12 | No sell-side or rating agency reports | Credit view relies on company disclosures | Public rating-agency press releases only; see [[bimbo-capital-structure-and-debt]] |
| 13 | No 3Q26 data (not yet released as of 2026-10-07 `[assumption]` typical late-October release cadence from prior-year releases) | Report relies on 2Q26 as latest | Check IR calendar; re-run model if 3Q26 appears before 2026-11-04 `[sourced]` company-profile.yaml |

> [!question] Is the 3Q26 release timing known? Prior releases suggest late October for 3Q, which falls before the 2026-11-04 report deadline `[assumption]`. The team should check the investor-relations calendar and decide whether to refresh the model.

## 8. Reading order and reliability hierarchy

1. Audited annual statements: EEFF25, then RA25/RA24 note sections.
2. Regulatory annual reports (RA21-RA25) for business, risk, ownership facts; cite page.
3. Quarterly XBRL filings (interim) for quarterly series.
4. Earnings releases for narrative, guidance and non-IFRS metrics; cross-check to filings.
5. Integrated reports and the financing framework for strategy and ESG, not for audited figures.

- When a later filing restates an earlier period, keep the latest figure and note the earlier one (WIKI.md rule) `[sourced]` WIKI.md.
- Extracted text is not a substitute for the PDF page: confirm table numbers against the original before putting them in the report.

## Key Takeaways
- ==48 PDFs, all Spanish==: 5 BMV annual reports (FY21-FY25), 5 corporate annual/integrated reports (FY25 statements audited by EY), 18 consecutive quarterly XBRL filings (1Q22-2Q26), 19 earnings releases (4Q21-2Q26), 1 financing framework.
- Latest data is ==2Q26 (released 2026-07-23)==; both the release and the XBRL filing are present.
- Only the FY2025 consolidated statements (EEFF25) and the annual BMV reports carry an audit opinion in the project; quarterly material is unaudited or unconfirmed.
- Biggest gaps: call transcripts, investor presentations, consensus/price data, English documents, peer and macro data.
- The financing framework PDF is image-only and needs OCR before use.
- A larger pre-2021 library sits in `D:\CFA Research\CFA\Reportes BIMBO`, not yet in the project.
