---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores/SPGlobal_GrupoBimbo,S.A.B.deC.V._ESGScores_06-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores History/SPGlobal_GrupoBimbo,S.A.B.deC.V._ESGScoresHistory_06-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/Sustainability Overview/SPGlobal_GrupoBimbo,S.A.B.deC.V.BMVBIMBOA(MIKEY4276592;SPCIQKEY877906;TCUID53231)_SustainabilityAndClimateOverview_06-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/Business Involvement  Screens/SPGlobal_GrupoBimbo,S.A.B.deC.V._BusinessInvolvementScreens_06-Oct-2026.xlsx
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/annual/IA25_GB_Celebramos_ESP_200826.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T25.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T24.pdf
tags: [Risks-ESG, esg-ratings]
---

# S&P Global ESG scores, profiles and involvement screens (Capital IQ)

**What this covers.** The S&P Global ESG Score (from the Corporate Sustainability Assessment, CSA) for Grupo Bimbo, its five-year history, the "Sustainability & Climate Overview" metrics and the Business Involvement Screens, all exported from CIQ on 2026-10-06. Tidy data: `data/capitaliq/esg_profiles.csv` (current breakdown, history, overview) and `data/capitaliq/esg_involvement.csv`. For the company's own ESG targets see [[bimbo-esg-framework]].

## 1. Headline score (2026 methodology year, updated 2026-10-06)

All figures [sourced] CIQ ESGScores, sheet 'ESG Scores'.

| Item | Value |
|---|---|
| ==S&P Global ESG Score (incl. modeled)== | **59** / 100 |
| Industry (FOA Food Products) average | 29 |
| Gap vs industry average | +30 points [calc: 59 − 29] |
| S&P Global CSA score | 58 |
| Environmental / Social / Governance & Economic | 69 / 63 / 46 |
| Pillar weights | 37% / 31% / 32% |
| Survey status | "Survey Respondent"; data points shared: Partial |
| Questions answered by modeling | 4 of 123; modeled scores flag = 1 |
| Media & Stakeholder Analysis (controversies) | ==No Data Available== (no controversy adjustment shown) |

- The weighted pillar check gives 69×0.37 + 63×0.31 + 46×0.32 = 59.8 [calc], against a published 59. S&P says the score accounts for "Media & Stakeholder Analysis adjustments", but none is listed, so the small gap is unexplained [unverified].
- **Disclosure.** Required public disclosure rate is 88% ("High" vs peers); additional disclosure is 86% ("Very High"). Score from required public disclosure: actual 40 vs potential 55 (industry max 62). From additional disclosure: actual 19 vs potential 32 (industry max 38) [sourced]. Bimbo discloses widely, but the content behind the disclosures scores well below the maximum available.

## 2. History (2022-2026)

[sourced] CIQ ESGScoresHistory, sheet 'ESG Scores History'. Years before 2023 include modeled scores "for comparative assessment"; S&P says these are not restatements.

| Methodology year | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| **Total ESG Score** | 55 | 55 | **61** | 58 | 59 |
| Environmental (weight %) | 67 (32) | 68 (33) | 72 (38) | 71 (37) | 69 (37) |
| Social (weight %) | 52 (35) | 51 (34) | 61 (33) | 58 (32) | 63 (31) |
| Governance & Economic (weight %) | 46 (33) | 46 (33) | 46 (29) | 43 (31) | 46 (32) |

- The score peaked at 61 in 2024 and has stayed between 58 and 59 since [sourced]. Governance & Economic has been stuck at 43-46 for five years and is the structural drag.

**Largest criterion moves, 2025 → 2026** [sourced, history sheet; YoY column in 'ESG Scores']

| Criterion | 2025 | 2026 | Driver questions (2026 score) |
|---|---|---|---|
| Climate Strategy (E, 8% weight) | 81 | ==54== | Scope 1 emissions 77→23; Scope 3 81→46; climate scenario analysis 100→0; TCFD disclosure 100→25; internal carbon pricing 70→0 |
| Customer Relations (S) | 63 | ==16== | Customer satisfaction measurement 100→1 |
| Biodiversity (E) | 53 | 72 | Risk assessment 61→91; exposure & assessment 9→42 |
| Health & Nutrition (S) | 70 | 93 | Policy 40→100 |
| Human Rights (S) | 56 | 71 | Mitigation & remediation 34→100 |
| Occupational Health & Safety (S) | 37 | 49 | Employee LTIFR 45→82 |
| Information Security (G) | 0 | 13 | Governance 0→20; programs 0→15; policy still 0 |

> [!question] Why did Climate Strategy fall 27 points?
> The 2026 drops are concentrated in emissions-performance and climate-disclosure questions. The company says it asked SBTi to temporarily suspend certification of its targets while it re-baselines 2025 emissions (IC25 p.101, via [[bimbo-esg-framework]]). That could explain part of the fall, but S&P gives no reason. [unverified] link.

## 3. Strengths and weaknesses vs industry (2026)

[sourced] CIQ ESGScores; industry average and best score in brackets.

| Highest-scoring criteria | Score (ind. avg / best) | Lowest-scoring criteria | Score (ind. avg / best) |
|---|---|---|---|
| Health & Nutrition | 93 (12 / 93) | Responsible AI | 0 (2 / 65) |
| Packaging | 91 (24 / 91) | Information Security | 13 (19 / 79) |
| Materiality | 88 (37 / 100) | Customer Relations | 16 (27 / 99) |
| Transparency & Reporting | 88 (40 / 100) | Tax Strategy | 21 (30 / 100) |
| Energy | 84 (42 / 98) | ==Corporate Governance== | ==32 (43 / 78)== |
| Business Ethics | 83 (46 / 89) | Supply Chain Management | 38 (19 / 92) |
| Water | 80 (34 / 90) | Policy Influence | 42 (17 / 84) |

- Only five criteria score below their industry average: Corporate Governance, Customer Relations, Information Security, Tax Strategy and Responsible AI. Supply Chain (38) and Policy Influence (42) score low in absolute terms but are still above the industry average [calc from sheet].
- **Corporate Governance is the only one of the five with a large weight (6%); the other four weigh 1-2%** [calc from sheet]. Zero scores on: board type, board diversity policy, CEO compensation success metrics, management ownership requirements, non-executive chair / lead director. Other low scores: board accountability 20, CEO long-term pay alignment 8. Board independence scores 100 and board average tenure 87 [sourced]. These scores line up with the founding-family control and executive-chair structure described in [[bimbo-governance-and-ownership]].
- Other zero-score questions: climate scenario analysis, internal carbon pricing, labor practices programs, human rights assessment, contractor LTIFR, supplier screening, tax strategy & governance, tax reporting, emerging risks, information security policy, CEO-to-employee pay ratio (no data shared), certifications of animal products [sourced].

## 4. Sustainability & Climate Overview (current)

[sourced] CIQ SustainabilityAndClimateOverview, single sheet.

| Theme | Metric | Bimbo | vs industry |
|---|---|---|---|
| Biodiversity & land use | Published biodiversity policy / commitment | Yes | "Minority": 40.85% of industry say yes |
| Energy transition | GHG Scope 1 intensity (t CO2e / US$ mm revenue) | 49.95 | "Ahead": 55.28% below average |
| Climate transition | ==Paris alignment== | ==3-4 °C== | "Behind": 3.13% of industry is within 1.5-2 °C |
| Physical risk | Composite score, 2030 medium-risk scenario | 59/100 | "Adequate": 4.33% above average |
| Employment practices | Women in all management positions | 25.00% | 3.96% below average |
| Health & safety | Employee LTIFR | 1.42 | "Ahead": 48.58% below average |
| Human rights | Published human rights policy | Yes | Majority (69.01%) |
| Ethics | Code of conduct covers corruption and bribery | Yes | Majority (76.06%) |
| Corporate governance | Number of female directors | 5 | 3 above average |
| Not available | Employee turnover; CEO-to-employee pay ratio; published risk-management processes | blank | No data |

## 5. Business Involvement Screens (as of 2026-04-03; FY2025; analysis date 2026-03-30)

[sourced] CIQ BusinessInvolvementScreens, sheet 'Business Involvement Screens'.
- Total revenue used: MXN 413,096 M. Revenue exposed to screened activities: ==0 (0%)==. Expansion exposure: 0 of 3 involvements.
- Consumer Products & Services: "No Involvement" on every screen. That covers tobacco, alcohol, gambling, cannabis, adult entertainment, predatory lending, pesticides, fur, animal testing, GMO development or growth, and palm oil **growers / processors and traders**. The palm-oil screen covers growing and processing, not use of palm oil as an ingredient.
- Defense & Weapons, Energy & Fossil Fuels and Healthcare: totals show no screen revenue and 0 exclusionary ownership counts, but the details are "locked due to subscription permissions" [sourced]. Treat these three as **not fully verified**.

## Reconciliation

| Item | CIQ | Company filings | Difference |
|---|---|---|---|
| FY2025 revenue (involvement screen base) | MXN 413,096 M | Net sales MXN 426,952 M (4T25 p.2). CIQ quarterly income statement FY25 sum ≈ 426,963 M (see [[bimbo-income-statement-fy21-fy25]]) | ==−13,856 M (−3.2%)== [calc]. Also differs from FY24 net sales of 408,335 M (4T24 p.2). Basis unexplained [unverified]; do not use as a revenue figure |
| Female directors | 5 | 5 women of 18 directors (28%) (RA25 p.169) | Agrees |
| Women in management | 25.00% (all management positions) | 30.51% women in leadership, 2025 (RA25 p.79) | Different definitions (all management vs leadership positions); not a contradiction, but quote the definition |
| Employee safety | LTIFR 1.42 | TRIR 1.59 reported in IC25 (via [[bimbo-esg-framework]]) | Different metrics (lost-time vs total recordable) |
| CDP | Not in CIQ export | CDP climate "A" (RA25 p.76); CDP water "B" 2025 (IC25 p.98) | CIQ does not cover CDP |
| Controversies | Media & Stakeholder Analysis: no data | Risk factors in RA25 (see [[bimbo-risk-factors]]) | No S&P controversy case shown as of 2026-10-06 |

- These ESG exports contain no EBITDA, net income or net debt, so only revenue can be reconciled to the financial statements.

## Key Takeaways
- ==S&P Global ESG Score 59 (2026), about 30 points above the FOA Food Products average of 29==. E 69, S 63, G&E 46. CSA score 58. Survey respondent with high disclosure rates (88% required, 86% additional).
- The score has been flat since its 2024 peak (55 → 55 → 61 → 58 → 59). Governance & Economic has stayed at 43-46 throughout, and Corporate Governance (32 vs industry 43) is the clearest weak spot: no non-executive chair, no board diversity policy, CEO pay not tied to disclosed metrics.
- 2026 brought a sharp fall in Climate Strategy (81 → 54) on emissions and disclosure questions, possibly linked to the SBTi target re-baselining [unverified]. S&P puts Bimbo's Paris alignment at 3-4 °C, "behind" the industry.
- Strong relative scores in Health & Nutrition (93), Packaging (91), Energy (84), Water (80) and Scope 1 intensity (55% below the industry average).
- Business involvement: 0% revenue in screened activities (FY2025). Defense, fossil-fuel and healthcare details are locked in this subscription. No controversy (MSA) case is shown.
- The CIQ revenue base (MXN 413,096 M) does not match reported FY25 net sales (MXN 426,952 M). Do not cite it.
