---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores History/ESG Scores History 2013 - 2016.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores History/ESG Scores History 2017 - 2021.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores History/ESG Scores History 2022 - 2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores History/SPGlobal_GrupoBimbo,S.A.B.deC.V._ESGScoresHistory_06-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores/SPGlobal_GrupoBimbo,S.A.B.deC.V._ESGScores_06-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores/SPGlobal_GrupoBimbo,S.A.B.deC.V._ESGScores_10-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores Raw Data/
  - filings/capitaliq/Sustainability/Sustainability Overview/SPGlobal_GrupoBimbo,S.A.B.deC.V.BMVBIMBOA(MIKEY4276592;SPCIQKEY877906;TCUID53231)_SustainabilityAndClimateOverview_10-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/Sustainability Overview/SPGlobal_GrupoBimbo,S.A.B.deC.V.BMVBIMBOA(MIKEY4276592;SPCIQKEY877906;TCUID53231)_SustainabilityAndClimateOverview_06-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/Business Involvement  Screens/SPGlobal_GrupoBimbo,S.A.B.deC.V._BusinessInvolvementScreens_10-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/Business Involvement  Screens/SPGlobal_GrupoBimbo,S.A.B.deC.V._BusinessInvolvementScreens_06-Oct-2026.xlsx
tags: [Risks-ESG, esg-score-history]
---

# Grupo Bimbo — S&P Global ESG Profile History (Capital IQ, 2013-2026)

The 14-year history of the S&P Global ESG Score for Bimbo and the question-level evidence behind it. [[ciq-esg-scores-and-profiles]] covers methodology years 2022-2026 from the 06-Oct-2026 exports; the folder now also holds three history files (2013-2016, 2017-2021, 2022-2026), 875 question-level PDFs ("ESG Scores Raw Data", 2020-2026) and a 10-Oct-2026 refresh. This article gives the pillar and criterion series back to 2013, the question-level pattern by year and pillar (all 875 PDFs parsed `[calc]`), the persistent zero-score questions, and what changed between 6 and 10 October. Company-side ESG: [[bimbo-esg-framework]], [[bimbo-sustainable-financing]]; risks: [[bimbo-risk-factors]]. ==Facts only: whether a score is "good" for valuation is a team judgment.==

**Citation key.** `CIQ-ESGH` = ESG Scores History files, sheet 'ESG Scores History' ("ESG Score Breakdown": score and weight per criterion and question for each methodology year). `CIQ-ESG` = ESG Scores (2026 breakdown with industry average and highest score). `CIQ-RAW` = one PDF per question and year ("Performance Summary": question-level company performance, question weight, year-on-year change, industry average and highest score; parsed with `pdftotext`). Scores 0-100. "Methodology year" = the S&P Global Corporate Sustainability Assessment cycle (updated each autumn; 2026 updated 6-Oct-2026). S&P states that years before 2023 include modeled scores "for comparative assessment" and are not restatements `[sourced]` CIQ-ESGH note.

## 1. Headline and pillar scores, 2013-2026

`[sourced]` CIQ-ESGH. Weights are the pillar weights S&P applied that year.

| Methodology year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Total ESG score** | 43 | 43 | 45 | 45 | 52 | 39 | 44 | 50 | 54 | 55 | 55 | 61 | 58 | 59 |
| Environmental | 28 | 37 | 42 | 44 | 54 | 53 | 56 | 58 | 56 | 67 | 68 | 72 | 71 | 69 |
| Social | 49 | 40 | 45 | 42 | 49 | 30 | 32 | 44 | 55 | 52 | 51 | 61 | 58 | 63 |
| Governance & Economic | 49 | 50 | 47 | 49 | 52 | 36 | 44 | 49 | 51 | 46 | 46 | 46 | 43 | 46 |
| E weight % | 29 | 29 | 29 | 28 | 28 | 28 | 28 | 28 | 32 | 32 | 33 | 38 | 37 | 37 |
| S weight % | 31 | 31 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 35 | 34 | 33 | 32 | 31 |
| G&E weight % | 40 | 40 | 41 | 42 | 42 | 42 | 42 | 42 | 38 | 33 | 33 | 29 | 31 | 32 |

Reading `[calc]`:
- ==The total score has risen from 43 (2013-2014) to 59 (2026), with a trough of 39 in 2018 and a peak of 61 in 2024==; the 2018 drop (52 to 39) came from Social (49 to 30) and Governance & Economic (52 to 36) while Environmental barely moved (54 to 53), and 2019-2021 rebuilt it (44, 50, 54).
- Environmental has gone 28 (2013) to 72 (2024) and 69 (2026): the single largest improvement; Social 49 to 63 after a 30-32 trough in 2018-2019; ==Governance & Economic has not improved in 14 years== (49 in 2013, 46 in 2026) and is at 43-46 since 2022, compared with 47-52 in 2013-2017 and 51 in 2021.
- Weights shifted toward Environmental (28% in 2016-2020 to 37%-38% since 2024) and away from Governance (42% in 2016-2020 to 29%-32% since 2024). At 2020 weights (28/30/42) the 2026 pillar scores would give 57.5 against 59.8 at 2026 weights `[calc]`: of the +9 total-score gain from 2020 (50) to 2026 (59), about 7.5 points come from better pillar scores (E +11, S +19, G -3) and about 2.3 from re-weighting, which favours the pillars where Bimbo scores best.
- The existing claim that Governance & Economic "has been stuck at 43-46 for five years" ([[ciq-esg-scores-and-profiles]]) is right for 2022-2026 but the history shows it was 47-52 before 2018 and fell with the 2018 reset; it is a post-2018 weakness, not a permanent level.

## 2. Criterion history

`[sourced]` CIQ-ESGH, criterion score each year (2026 weight in brackets). "–" = criterion not part of the framework or not scored that year. Criteria are those in the 2026 framework; the framework changed in 2017 (Human Rights, Policy Influence), 2020 (Information Security), 2021 (Biodiversity), 2022 (Customer Relations), 2023 (Water, Energy, Waste & Pollutants, Transparency & Reporting), 2025 (Product Quality & Recall Management) and 2026 (Responsible AI).

| Criterion (2026 weight %) | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Climate Strategy (8) | 28 | 42 | 53 | 46 | 55 | 53 | 59 | 65 | 56 | 60 | 65 | 81 | 81 | 54 |
| Biodiversity (5) | – | – | – | – | – | – | – | – | 21 | 39 | 45 | 47 | 53 | 72 |
| Water (6) | – | – | – | – | – | – | – | – | – | – | 80 | 80 | 82 | 80 |
| Energy (2) | – | – | – | – | – | – | – | – | – | – | 70 | 79 | 79 | 84 |
| Packaging (4) | 60 | 53 | 47 | 65 | 83 | 83 | 95 | 54 | 70 | 87 | – | 85 | 91 | 91 |
| Sustainable Raw Materials (5) | 29 | 16 | 36 | 46 | 45 | 50 | 47 | 51 | 53 | 54 | 52 | 61 | 61 | 54 |
| Waste & Pollutants (5) | – | – | – | – | – | – | – | – | – | – | 100 | 80 | 67 | 75 |
| Human Capital Management (7) | 36 | 41 | 39 | 41 | 45 | 37 | 37 | 52 | 73 | 75 | 50 | 62 | 68 | 68 |
| Labor Practices (6) | 55 | 58 | 56 | 32 | 55 | 35 | 33 | 55 | 51 | 51 | 66 | 73 | 57 | 53 |
| Human Rights (5) | – | – | – | – | 58 | 10 | 5 | 5 | 28 | 28 | 25 | 45 | 56 | 71 |
| Occupational Health & Safety (6) | 71 | 40 | 42 | 51 | 45 | 20 | 41 | 43 | 48 | 34 | 31 | 29 | 37 | 49 |
| Health & Nutrition (5) | 56 | 59 | 59 | 76 | 70 | 68 | 74 | 77 | 77 | 77 | 100 | 100 | 70 | 93 |
| Customer Relations (2) | – | – | – | – | – | – | – | – | – | 33 | 35 | 58 | 63 | 16 |
| Supply Chain Management (6) | 44 | 45 | 43 | 48 | 51 | 41 | 57 | 63 | 72 | 67 | 47 | 39 | 46 | 38 |
| Product Quality & Recall Management (3) | – | – | – | – | – | – | – | – | – | – | – | – | 45 | 54 |
| Business Ethics (4) | 64 | 64 | 64 | 67 | 73 | 48 | 70 | 81 | 85 | 71 | 82 | 83 | 79 | 83 |
| Corporate Governance (6) | 52 | 44 | 43 | 42 | 47 | 16 | 37 | 35 | 35 | 34 | 36 | 34 | 33 | 32 |
| Policy Influence (2) | – | – | – | – | 51 | 32 | 21 | 29 | 0 | 0 | 51 | 36 | 33 | 42 |
| Tax Strategy (2) | – | 60 | 48 | 54 | 39 | 27 | 27 | 24 | 21 | 21 | 21 | 21 | 21 | 21 |
| Information Security (2) | – | – | – | – | – | – | – | 31 | 23 | 38 | 45 | 58 | 0 | 13 |
| Risk & Crisis Management (3) | 51 | 57 | 50 | 50 | 49 | 22 | 30 | 36 | 48 | 38 | 23 | 33 | 33 | 44 |
| Materiality (2) | – | – | – | 33 | 33 | 20 | 18 | 58 | 75 | 77 | 56 | 77 | 67 | 88 |
| Transparency & Reporting (1) | – | – | – | – | – | – | – | – | – | – | 88 | 38 | 63 | 88 |

Legacy criteria that left the framework (score by year):

| Legacy criterion | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Operational Eco-Efficiency | 5 | 44 | 42 | 46 | 45 | 56 | 46 | 79 | 85 | 89 | – | – | – | – |
| Environmental Reporting | 52 | 29 | 51 | 55 | 53 | 55 | 66 | 50 | 50 | 80 | – | – | – | – |
| Environmental Policy & Management | 52 | 51 | 63 | 57 | 60 | 41 | 75 | 78 | 51 | 73 | 73 | 55 | 36 | 46 |
| Talent Attraction & Retention | 36 | 30 | 44 | 42 | 42 | 19 | 17 | 49 | 52 | 46 | 43 | – | – | – |
| Corporate Citizenship & Philanthropy | 37 | 32 | 36 | 45 | 57 | 57 | 46 | 46 | 93 | 70 | – | – | – | – |
| Social Reporting | 50 | 28 | 50 | 43 | 54 | 45 | 43 | 50 | 50 | 50 | – | – | – | – |
| Innovation Management | 27 | 26 | 22 | 22 | 30 | 37 | 11 | 20 | 24 | 25 | 29 | – | – | – |

Reading `[calc]`:
- ==Corporate Governance (6% weight) has fallen from 52 (2013) to 32 (2026)== with a collapse to 16 in 2018; it has not exceeded 37 since 2018 and sits below the industry average (43) in 2026.
- Tax Strategy has fallen from 60 (2014) to 21 and has not moved since 2021; Information Security rose to 58 (2024) and was reset to 0 (2025) and 13 (2026); Customer Relations rose from 33 (2022) to 63 (2025) and fell to 16 (2026).
- Climate Strategy (8% weight in 2026, up from 3% in 2013-2019) went 28 (2013) to 81 (2024-2025) and 54 (2026): its weight has risen 2.7x while its score has fallen 27 points in the latest cycle, which is a main driver of the 2026 Environmental decline (71 to 69).
- Strongest and most stable: Business Ethics 71-85 since 2020 (4% weight), Health & Nutrition 68-100 since 2017, Packaging 47-95, Materiality 56-88 since 2020, Water 80-82 and Energy 70-84 since 2023; Human Rights rose from 5 (2019-2020) to 71 (2026).

## 3. Question-level evidence, 2020-2026 (875 PDFs)

All PDFs under `ESG Scores Raw Data` were parsed `[calc]` (116, 131, 137, 124, 121, 123, 123 question PDFs for 2020-2026). 73 of 875 (8%) show the Performance Summary labels but no values in the text layer (2020: 10, 2021: 11, 2022: 11, 2023: 13, 2024: 13, 2025: 7, 2026: 8); they are excluded from the counts below and are gaps. For 2026 their criterion-level scores are still in CIQ-ESG. Scores are unweighted means of question-level scores `[calc]`; the criterion and total scores above are weighted by S&P.

| Year | Pillar | Questions (PDFs) | With performance score | Score 0 | Above industry avg. | Below | Mean score (unweighted) | Mean industry avg. | Gap |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | E | 39 | 35 | 6 | 26 | 9 | 58.2 | 28.3 | +29.9 |
| 2020 | S | 24 | 24 | 9 | 11 | 12 | 37.8 | 24.2 | +13.6 |
| 2020 | G&E | 53 | 47 | 13 | 26 | 20 | 41.9 | 29.0 | +12.9 |
| 2021 | E | 45 | 41 | 6 | 33 | 8 | 55.2 | 28.3 | +26.9 |
| 2021 | S | 33 | 32 | 11 | 20 | 12 | 44.5 | 30.3 | +14.1 |
| 2021 | G&E | 53 | 47 | 15 | 25 | 22 | 44.8 | 33.3 | +11.5 |
| 2022 | E | 47 | 43 | 3 | 37 | 5 | 65.3 | 30.6 | +34.7 |
| 2022 | S | 41 | 39 | 10 | 25 | 14 | 49.7 | 31.5 | +18.2 |
| 2022 | G&E | 49 | 44 | 14 | 24 | 19 | 43.8 | 33.2 | +10.6 |
| 2023 | E | 43 | 40 | 2 | 37 | 3 | 67.5 | 28.1 | +39.3 |
| 2023 | S | 30 | 28 | 7 | 18 | 10 | 47.7 | 30.0 | +17.6 |
| 2023 | G&E | 51 | 43 | 13 | 26 | 16 | 43.5 | 30.9 | +12.6 |
| 2024 | E | 45 | 42 | 1 | 38 | 4 | 70.4 | 32.7 | +37.7 |
| 2024 | S | 30 | 28 | 6 | 20 | 8 | 55.6 | 33.8 | +21.9 |
| 2024 | G&E | 46 | 38 | 14 | 19 | 19 | 41.5 | 36.7 | +4.9 |
| 2025 | E | 44 | 42 | 1 | 37 | 5 | 69.7 | 36.9 | +32.7 |
| 2025 | S | 30 | 29 | 3 | 24 | 5 | 58.4 | 33.6 | +24.8 |
| 2025 | G&E | 49 | 45 | 15 | 25 | 20 | 40.7 | 39.1 | +1.6 |
| 2026 | E | 43 | 41 | 3 | 34 | 7 | 61.9 | 28.9 | +33.0 |
| 2026 | S | 31 | 30 | 3 | 24 | 6 | 60.6 | 26.7 | +33.9 |
| 2026 | G&E | 49 | 44 | 14 | 25 | 19 | 43.5 | 34.2 | +9.3 |

Reading `[calc]`:
- Environmental: 26 (2020) and 33-38 (2021-2026) of the compared questions score above the industry average, zero-score questions fell from 6 (2020-2021) to 1-3 since 2022, and the mean gap to the industry is +27 to +39 points.
- Social improved the most: mean score 37.8 (2020) to 60.6 (2026), zero-score questions 9 to 3, questions above industry average 11 to 24; the gap went from +13.6 to +33.9.
- ==Governance & Economic has barely moved: mean 41.9 (2020), 40.7 (2025), 43.5 (2026), with 13-15 zero-score questions every year, while the industry average rose from 29.0 to 39.1 (2025) and 34.2 (2026)== so the gap shrank from +12.9 to +1.6 (2025) and +9.3 (2026); 16-22 questions score below the industry average each year.
- The 2026 industry averages for E and S (28.9 and 26.7) are lower than in 2025 (36.9, 33.6), a feature of the 2026 question set and peer group, not of Bimbo's score `[unverified]`.

### Questions that have scored zero in every year 2020-2026

`[calc]` from CIQ-RAW (weight = share of the criterion score).

| Criterion | Question | Years scored 0 (of 2020-2026) | Weight in criterion (%) | Industry avg. (latest) |
|---|---|---|---|---|
| Risk & Crisis Management | Emerging Risks | 7 | 15 | 5 |
| Corporate Governance | CEO Compensation - Success Metrics | 7 | 6 | 17 |
| Corporate Governance | Family Ownership | 7 | 4 | 100 |
| Corporate Governance | Management Ownership Requirements | 7 | 6 | 7 |
| Corporate Governance | Board Diversity Policy | 7 | 7 | 37 |
| Corporate Governance | Non-Executive Chairperson/ Lead Director | 7 | 6 | 30 |
| Tax Strategy | Tax Strategy and Governance | 7 | 50 | 11 |
| Occupational Health & Safety | Lost-Time Injury Frequency Rate (LTIFR) - Contractors | 7 | 17 | 27 |
| Human Rights | Human Rights Assessment | 7 | 25 | 22 |

- ==Family Ownership scores 0 every year against an industry average of 100 in 2026 (96 in 2023, 43 in 2020)==: S&P marks down companies in which founding-family members hold more than 5% of the voting rights, and Bimbo's register has family holding companies with 72.03% ([[ciq-ownership-and-holdings-history]], [[bimbo-governance-and-ownership]]). The weight is small (4% of the Corporate Governance criterion) but it cannot improve without a change in ownership.
- The other zero-score governance questions (CEO compensation success metrics, management ownership requirements, board diversity policy, non-executive chair or lead director) are policy-disclosure items that the company could change without altering ownership; the board independence score is 100 and average board tenure 87 ([[ciq-esg-scores-and-profiles]]).
- Two heavily weighted zeros sit outside governance: Tax Strategy and Governance (50% of the Tax Strategy criterion; industry average 11) and Human Rights Assessment (25% of Human Rights; industry average 22).

### Largest question-level moves, 2025 to 2026

`[calc]` CIQ-RAW levels in the two methodology years (the Year-on-Year field is not reliably parsed); weights in 2026.

| Criterion | Question | 2025 | 2026 | Change | 2026 weight in criterion (%) | 2026 industry avg. |
|---|---|---|---|---|---|---|
| Climate Strategy | Climate-Related Scenario Analysis | 100 | 0 | -100 | 6 | 30 |
| Customer Relations | Customer Satisfaction Measurement | 100 | 1 | -99 | 50 | 33 |
| Climate Strategy | TCFD Disclosure | 100 | 25 | -75 | 3 | 41 |
| Climate Strategy | Internal Carbon Pricing | 70 | 0 | -70 | 4 | 24 |
| Climate Strategy | Direct Greenhouse Gas Emissions (Scope 1) | 77 | 23 | -54 | 13 | 44 |
| Corporate Governance | CEO-to-Employee Pay Ratio | 44 | 0 | -44 | 5 | 44 |
| Sustainable Raw Materials | Certifications of Animal Products | 44 | 0 | -44 | 20 | 26 |
| Climate Strategy | Indirect Greenhouse Gas Emissions (Scope 3) | 81 | 46 | -35 | 12 | 32 |
| Supply Chain Management | KPIs for Supplier Assessment and Development | 40 | 5 | -35 | 23 | 17 |
| Climate Strategy | Climate Risk Management | 83 | 54 | -29 | 6 | 46 |
| Water | Water Consumption | 100 | 74 | -26 | 26 | 35 |
| Labor Practices | Gender Pay Indicators | 59 | 37 | -22 | 15 | 28 |
| Human Rights | Human Rights Mitigation & Remediation | 34 | 100 | +66 | 25 | 19 |
| Health & Nutrition | Health & Nutrition Policy | 40 | 100 | +60 | 33 | 10 |
| Water | Water Risk Management Programs | 40 | 90 | +50 | 12 | 30 |
| Transparency & Reporting | Sustainability Reporting Assurance | 50 | 100 | +50 | 50 | 25 |
| Risk & Crisis Management | Risk Governance | 25 | 70 | +45 | 43 | 52 |
| Materiality | Materiality Metrics for Enterprise Value Creation | 60 | 100 | +40 | 25 | 24 |
| Occupational Health & Safety | Lost-Time Injury Frequency Rate (LTIFR) - Employees | 45 | 82 | +37 | 22 | 16 |
| Biodiversity | Biodiversity Exposure & Assessment | 9 | 42 | +33 | 25 | 25 |

- ==Seven of the twelve largest falls are in Climate Strategy and Customer Relations==, consistent with [[ciq-esg-scores-and-profiles]] (scenario analysis 100 to 0, internal carbon pricing 70 to 0, TCFD disclosure 100 to 25, Scope 1 77 to 23, customer satisfaction measurement 100 to 1), and extended by items not listed there: CEO-to-employee pay ratio 44 to 0, certifications of animal products 44 to 0, KPIs for supplier assessment and development 40 to 5, gender pay indicators 59 to 37 and water consumption 100 to 74.
- The largest rises are disclosure and process items (human rights mitigation and remediation 34 to 100, health and nutrition policy 40 to 100, sustainability reporting assurance 50 to 100, water risk management programs 40 to 90, risk governance 25 to 70).

## 4. 10-Oct-2026 refresh versus 06-Oct-2026

`[calc]` cell-by-cell comparison of the 06-Oct and 10-Oct files.

| File | What changed | What did not |
|---|---|---|
| ESG Scores (breakdown) | 94 cells: industry average score in 86 rows (+1 to +3 points, e.g., Climate Strategy 32 to 33; Water 34 to 35; Packaging 24 to 25; Energy 42 to 43; Materiality 37 to 38; Health & Nutrition 12 to 13; Policy Influence 17 to 18) and industry highest score in 8 rows (Climate Strategy 83 to 90; Water 90 to 96; Corporate Governance 78 to 82; Information Security 79 to 83; Exposure of Suppliers to Water Risks 80 to 100; LTIFR contractors 75 to 90; Management Ownership Requirements 68 to 80; Lobbying and Trade Associations - Climate 72 to 85) | the company score of every criterion and question, the total score (59), pillar scores (69 / 63 / 46), weights, industry average (29) and disclosure rates (88% / 86%) |
| Sustainability & Climate Overview | industry comparators in 9 cells: share of industry with a biodiversity policy 40.85% to 44.00%; Scope 1 intensity "55.28% below average" to 54.00%; industry within 1.5-2 C 3.13% to 2.94%; physical-risk composite "4.33% above average" to 3.80%; women in management "Adequate, 3.96% below average" to **"Lagging, 6.51% below average"**; LTIFR "48.58% below" to 46.63%; human rights policy 69.01% to 70.67%; ethics code 76.06% to 77.33% | Bimbo's own responses (25.00% women in management; LTIFR 1.42; Paris alignment 3-4 C; 5 female directors) |
| Business Involvement Screens | total revenue used 413,096.37 to 413,359.04 (MXN millions; +0.06%); rows re-ordered in the sheet | 0% revenue in screened activities; defense, fossil fuel and healthcare detail still locked |

- The industry-average edits are small (about 1-3 points) and none changes a conclusion in [[ciq-esg-scores-and-profiles]]; the table in its section 3 (strengths and weaknesses) should show Corporate Governance 32 (43 / 82) and Information Security 13 (19 / 83) for the highest scores, and Climate Strategy 54 (33 / 90).
- The Overview comparator for women in management moves from "Adequate" to "Lagging": Bimbo's 25.00% share of women in all management positions is now 6.51% below the industry average (it was 3.96% below on 6-Oct). The company reports 30.51% women in leadership under a different definition ([[ciq-esg-scores-and-profiles]] reconciliation).
- The Business Involvement revenue base of 413.4 bn remains 3.2% below FY2025 net sales of 426,952 `[calc]`; the basis is not stated.

## 5. Gaps and flags

| Item | Detail |
|---|---|
| Modeled scores before 2023 | histories include modeled scores for comparison (not restatements) `[sourced]` |
| Framework changes | criteria appear and disappear (section 2), so criterion series are not like-for-like across 2017, 2021, 2023, 2025 |
| Unparsed PDFs | 73 of 875 question PDFs show no values in the text layer (any year) |
| Question-level year-on-year | the PDF "Year-on-Year Change" field was not parsed reliably (negative values); levels in adjacent years were used instead |
| 2013-2016 framework | uses a different question set (e.g., Human Capital Return on Investment, R&D Spending, Innovation Management); only criterion-level scores are comparable |
| Controversies | Media and Stakeholder Analysis: "No Data Available" in both exports |
| CDP and company ratings | not in CIQ; see [[bimbo-esg-framework]] |
| Business Involvement | defense, fossil fuel, healthcare detail locked by subscription |

## Connections
- Snapshot article and company reconciliation: [[ciq-esg-scores-and-profiles]]; company targets and frameworks: [[bimbo-esg-framework]], [[bimbo-sustainable-financing]]; risks: [[bimbo-risk-factors]].
- Governance structure behind the Corporate Governance and Family Ownership scores: [[ciq-ownership-and-holdings-history]], [[bimbo-governance-and-ownership]]; pay and board items: [[ciq-delta-vs-previous-export]] lists the claims to update.
- Valuation context: [[ciq-long-history-multiples-and-returns]]; plant and customer-supplier data for supply-chain scoring: [[ciq-plant-network-and-capacity]], [[ciq-customers-and-suppliers]].

## Key Takeaways

- ==The S&P Global ESG Score rose from 43 (2013) to 59 (2026), with a 2018 trough at 39 and a 2024 peak at 61==; Environmental (28 to 69) and Social (49 to 63) improved, Governance & Economic did not (49 to 46).
- About 7.5 of the 9-point gain since 2020 comes from pillar scores (E +11, S +19, G -3) and about 2.3 from S&P re-weighting toward Environmental (28% to 37%) and away from Governance (42% to 32%).
- In 2020-2026 the Governance & Economic question set stays at a mean score of about 41-44 with 13-15 zero-score questions every year while the industry average rose from 29.0 to 34.2 (39.1 in 2025): Bimbo's lead in governance narrowed from +12.9 to +9.3 points.
- Family Ownership scores 0 against an industry average of 100 every year, and eight other questions have been zero in all seven years; Corporate Governance fell from 52 (2013) to 32 (2026).
- The 2026 drops in Climate Strategy (81 to 54) and Customer Relations (63 to 16) are driven by a handful of questions that went to 0 or near 0 (scenario analysis, carbon pricing, customer-satisfaction measurement), and could be reversed by disclosure.
- The 10-Oct refresh changed only industry comparators (86 industry averages by 1-3 points, 8 industry-best scores, 9 Overview comparators); Bimbo's own scores and the total of 59 are unchanged.
