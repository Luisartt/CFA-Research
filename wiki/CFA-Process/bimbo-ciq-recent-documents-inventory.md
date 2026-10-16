---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/News, Events and filings/Recent Documents/Annuals and Interims
  - filings/capitaliq/News, Events and filings/Recent Documents/Carpetas Current Reports Bimbo
  - filings/capitaliq/News, Events and filings/Recent Documents/Environmental, Social and Governance (ESG)
  - filings/capitaliq/News, Events and filings/Recent Documents/Merger Documents
  - filings/capitaliq/News, Events and filings/Recent Documents/Miscellaneous
  - filings/capitaliq/News, Events and filings/Recent Documents/Ownership, Tenders & Insider Holdings
  - filings/capitaliq/News, Events and filings/Recent Documents/Prospectus
  - filings/capitaliq/News, Events and filings/Recent Documents/Proxies
  - filings/capitaliq/News, Events and filings/Recent Documents/Registration Statements
  - filings/capitaliq/News, Events and filings/Recent Documents/Regulatory Filings
tags: [CFA-Process, source-inventory]
---

# CIQ "Recent Documents" — Inventory, Triage and Reading Log

Triage of the S&P Capital IQ download `filings/capitaliq/News, Events and filings/Recent Documents/` (1,503 files in total; **1,255 in scope** here, the remaining 248 in `Transcript & Presentation` belong to another reader), with what each family contains, how decision-relevant it is, what was read and what was not. It complements [[bimbo-filings-source-map]] (which maps `filings/`) and feeds [[bimbo-material-events-timeline]], [[bimbo-bond-prospectus-terms]], [[bimbo-major-deals-terms]], [[bimbo-agm-dividends-and-buybacks]] and [[bimbo-related-party-and-compensation-disclosures]]. Public information only (CFA Standard II(A)).

**Method.** Every file outside `Transcript & Presentation` was converted to text: 1,209 PDFs with `pdftotext -layout`, 43 `.mht` and 3 `.html` with a Python parser. Files with an empty text layer were rendered to images and read visually where decision-relevant. No OCR engine was available, so unreadable scans are listed as gaps. Each leaf item is a folder holding one file with the same stem. Counts below come from the file names (`Entity_date_TYPE_title`).

## 1. Folder-level triage

| Folder | Files | Size | Date range | Content | Relevance | Reading depth |
|---|---|---|---|---|---|---|
| Annuals and Interims | 463 | 2.2 GB | 1996-2026 | Bimbo annual reports (120 files, FY1996-FY2025, mostly re-filings), earnings releases (38), quarterly supplements, Canada Bread annual and quarterly filings (174), 1 Mercator, 2 Fargo, 1 other | High for FY2017-FY2025 reports; low for duplicates | Targeted: dividends, buybacks, debt, related parties, compensation, deal notes |
| Carpetas Current Reports Bimbo | 291 | 31 MB | 1997-2026 | 122 Bimbo press releases, 1 Bimbo MR, 29 Bimbo Bakeries USA product releases, 135 Canada Bread (83 PR, 52 CORR, 1997-2014), 2 Capital Foods 6-K, 1 Ingenio, 1 QSR | High | All 122 Bimbo PRs read or parsed; Canada Bread 2013-14 read; rest skimmed |
| Miscellaneous | 402 | 344 MB | 1996-2026 | Bimbo FINSUPP (69), MISC (9), OTHERFIN (50), RNS (3); Canada Bread FINSUPP (130), MISC (133), OTHERFIN (5); Mercator (2); Gastronomía Avanzada (1) | Medium (duplicates of Annuals; 3 RNS high) | RNS read; remainder triaged |
| Proxies | 49 | 34 MB | 1997-2026 | 11 Bimbo AGM notices (2017-2026) and 38 Canada Bread circulars (1997-2014) | High | All 11 Bimbo notices read (6 visually); Canada Bread 2013-14 read |
| Prospectus | 11 | 3.8 MB | 2000-2025 | 9 Bimbo MXN certificate offer/placement notices (2017, 2023, 2025), 1 Canada Bread 2000 offering circular, 1 Wendy's/Arby's exchange-offer prospectus (misfiled) | High | All 9 Bimbo notices deep-read |
| Merger Documents | 12 | 12 MB | 2009-2021 | Bimbo-Sara Lee presentations (Nov-2010, Oct-2011), Canada Bread presentation (Feb-2014), Bimbo Canada VPPA release (2021), 8 Wendy's/Arby's S-4 filings (misfiled) | High | Deep-read (3); misfiles identified |
| Ownership, Tenders & Insider Holdings | 10 | 0.5 MB | 2001-2002 | Earthgrains: Sara Lee tender offer amendments, SC 14D9/A, GAMCO 13D, 13G | Low (historical precedent) | Skimmed |
| Registration Statements | 9 | 6.3 MB | 2009-2016 | Bimbo F-6 (ADR, 2016) plus the same 8 Wendy's/Arby's S-4 files as in Merger Documents | Medium (F-6) | F-6 read |
| Environmental, Social and Governance (ESG) | 5 | 20 MB | 2016-2026 | Sustainability reports 2016-2018; "management approach" 2025 and 2026 | Medium | Listed, not read (covered by [[bimbo-esg-framework]]) |
| Regulatory Filings | 3 | 9.9 MB | 2020-2024 | AML/KYC submissions of the bylaws (2020, 2023 scans; 2024 English text) | Medium | 2024 read; 2020, 2023 unreadable |
| *Transcript & Presentation (out of scope)* | 248 | 1.2 GB | 2010-2026 | Call transcripts, presentations, 66 audio files | n/a | Not read |

## 2. Family-level detail (entity, type, count, dates)

| Entity | Type (CIQ code) | Files | Dates | What it is |
|---|---|---|---|---|
| Bimbo | AR (annual reports) | 120 | 1996-12 to 2026-08 | Integrated annual reports; FY2017-FY2025 each appear many times (up to ~14 for FY2017) (English, Spanish, summary, CNBV "Reporte Anual", re-filings) |
| Bimbo | ER / QR (earnings releases) | 38 + 6 | 2000-09 to 2026-07 | Quarterly results releases, Spanish and English |
| Bimbo | FINSUPP, MISC, OTHERFIN | Annuals: FINSUPP 67 (+3 untitled), MISC 50; Miscellaneous: FINSUPP 69, MISC 9, OTHERFIN 50 | 1996-2026 | Quarterly BMV filings and financial supplements; 37 stems are identical across Annuals and Miscellaneous |
| Bimbo | PR | 122 | 2014-02 to 2026-09 | See section 3 |
| Bimbo | PROXY | 11 | 2017-03 to 2026-04 | AGM notices and the 127-page 2026 AGM package |
| Bimbo | PROSPECTUS | 9 | 2017-10 to 2025-02 | MXN certificate notices |
| Bimbo | MP / MR | 2 + 2 | 2010-11 to 2021-04 | Sara Lee deal presentations; Canada VPPA release |
| Bimbo | RNS | 3 | 2017-11 to 2019-10 | Euronext Dublin notices for US dollar notes |
| Bimbo | F6 / AML-KYC / ESG | 1 + 3 + 5 | 2016-2026 | ADR registration; bylaws; sustainability |
| Bimbo Bakeries USA | PR | 29 | 2024-08 to 2026-09 | Product and marketing releases (Thomas', Sara Lee, Entenmann's...) plus one Teamsters labour item (2025-09-08) |
| Canada Bread | AR 39, FINSUPP 130 (x2 folders), MISC 5+133, CORR 52, PR 83, PROXY 38, MP 1, PROSPECTUS 1, OTHERFIN 5 | 617 including cross-folder duplicates | 1997-2014 | The listed Canadian subsidiary before the 2014 acquisition |
| Earthgrains | SC TO-T/A 6, 14D9/A 1, 13D 2, 13G/A 1 | 10 | 2001-2002 | Sara Lee tender offer for Earthgrains and holder filings |
| Fargo / Capital Foods | AR 2, 6-K 2 | 4 | 2003-2009 | Argentine bakery (acquired 2011) pre-acquisition filings |
| NewBakeryCompany | S-4, S-4/A, 424B3 | 9 (+8 duplicates) | 2009 | **Not Bimbo** (see section 4) |
| Mercator, Gastronomía Avanzada, Ingenio El Molino | various | 6 | 2005-2015 | **Misattributed** (section 4) |

## 3. Current-report stream (Bimbo PR, 122 files)

| Group | Files | Use |
|---|---|---|
| Daily shares-outstanding notices (BMV, `.mht`), 18-Mar to 29-Jul-2026 | 43 | Buyback pace, [[bimbo-agm-dividends-and-buybacks]] |
| Coupon notices (*Aviso a Tenedores*) for BIMBO 17, 23-2L, 25-2, 26-2 | 20 | Floating-rate prints, [[bimbo-bond-prospectus-terms]] |
| Rating actions (S&P, Fitch) | 11 | Ratings; four Fitch PDFs have a garbled text layer (visual read for 6-Aug-2025 only) |
| Offer and placement notices in the PR folder (2026) | 4 | BIMBO 26 and 26-2 terms |
| Calendar items (call invitations, trading-volume statement) | 6 | Catalyst dates |
| Narrative corporate and ESG releases | ~38 | Timeline, deals, governance |

## 4. Misfiled, mislabelled and duplicate material

> [!warning] Do not cite these as Bimbo documents
> - **NewBakeryCompany (9 files in Merger Documents / Registration Statements / Prospectus)**: the S-4, S-4/A and 424B3 are for **Wendy's/Arby's Restaurants, LLC**'s exchange offer for US$565m 10.00% senior notes due 2016 (The New Bakery Co. of Ohio is a Wendy's subsidiary). The word "Bimbo" appears 0 times in the 9 files [calc]. They carry no Weston Foods or any other Bimbo deal information; **no Weston Foods deal documents exist in the in-scope folders**.
> - **Mercator** (2008, 2015): Slovenian retailer Poslovni sistem Mercator reports.
> - **Gastronomía Avanzada** (2006 FINSUPP): Bimbo's own 2005 annual report under a CIQ affiliate name.
> - **Ingenio El Molino** (2007 AR; 2009 PR): the 2007 file appears to be Bimbo's FY2007 annual report and the 2009-dated item is Bimbo's 2Q06 earnings release.
> - **`Bimbo_2023-06-03_AR_Prospecto-Definitivo`** is the FY2022 integrated annual report, not a prospectus.
> - **Prospectus stems for BIMBO 23 / 23L / 25 / 25-2** are swapped between 30-May and 31-May notices and between `_n2` files; see the warning in [[bimbo-bond-prospectus-terms]].
> - Registration Statements duplicates 8 files from Merger Documents; Annuals and Miscellaneous share 37 identical stems; Bimbo annual reports are filed repeatedly (summary, English, Spanish, CNBV version).

## 5. What was read, and how

| Family | Depth | Output |
|---|---|---|
| Prospectus notices (9) and the 2017-2026 offer/placement PRs | Deep read | [[bimbo-bond-prospectus-terms]] |
| International-note PRs (2017, 2021, 2023, 2024), RNS (3), rating PRs (2024-2026), 20 coupon notices | Deep read | same |
| Merger presentations (3), Canada Bread circular (2014-03-06) and 2013-14 PRs, Bimbo deal PRs 2014-2025, FY2018-FY2020 deal notes | Deep read | [[bimbo-major-deals-terms]] |
| AGM notices 2017-2026 (11), 2026 AGM package, annual-report equity notes and dividend sections FY2008-FY2025, bylaws 2024, daily share counts | Deep read | [[bimbo-agm-dividends-and-buybacks]] |
| Related-party and compensation notes FY2018-FY2025, director-fee sections FY2017-FY2023, Canada Bread 2013 circular and AIF | Deep read | [[bimbo-related-party-and-compensation-disclosures]] |
| All 122 Bimbo PRs | Read or parsed | [[bimbo-material-events-timeline]] |
| Bimbo quarterly releases 2025-2026, FY2025 financial statements (extracts) | Skimmed for dates and headline numbers | timeline |
| Canada Bread 1997-2012 annual, quarterly, proxy, correspondence files (≈430) | Triage only (titles, dates) | none; historical subsidiary data |
| Bimbo FY1998-FY2013 annual reports and quarterly supplements | Targeted greps (dividends, ratios) | [[bimbo-agm-dividends-and-buybacks]] |
| ESG reports (5), Earthgrains tender files (10), Capital Foods 6-Ks | Skimmed | none |

## 6. Gaps (not read or not readable)

- **Image-only files with no text layer** (no OCR available): `Bimbo_1996-12-30_AR`; FINSUPP 1996-03, 1996-06 (2 files), 1996-09 (2 files), 1997-06; `Fargo_2008-03-09_AR` and `Fargo_2009-03-11_AR`; `Bimbo_2020-07-08_AML-KYC` and `Bimbo_2023-08-22_AML-KYC_By-laws` (bylaw scans); `CanadaBread_2009-03-29_AR_Periodo-2008_n2` and `CanadaBread_2010-04-16_PR`; 42 Canada Bread MISC files (2004-2014).
- **Proxies read only visually**: 2017 and 2018 AGM notices are rotated newspaper scans (agenda illegible; dividends taken from annual reports); 2020, 2021, 2022, 2024, 2025 and 2026-04-30 were read as images.
- **Garbled PDF text layers**: Fitch actions of 6-Dec-2024, 9-Jan-2025 and 6-Aug-2025 (only the last read visually; the first two give only the headline: F1+(mex) short-term programme and AAA(mex) for proposed certificates).
- **Documents that do not exist in the folder and matter**: the *Suplemento* (pricing supplements with covenants) of each local issue; US 144A offering memoranda; the 2021-2025 AGM minutes with vote counts and the buyback ceilings; the April-2022 AGM notice; BIMBO 16 offering notice; Weston Foods (2009) and Fargo (2011) deal documents; the Nov-2025 CEO announcement; the Oct-2020 extraordinary AGM notice; Moody's actions; any Bimbo current reports for 2019-2020 other than debt notices.
- **Out of scope but relevant:** M&A call transcripts and audio for Sara Lee (24-Oct-2011) and Canada Bread (12-Feb-2014) and a Nov-2010 Sara Lee merger presentation are in `Transcript & Presentation`.
- **Not reconciled**: the CIQ 2025 share-count notices before 18-Mar-2026 (none), the April-2026 daily series, and 1-25 July 2026.

## 7. Where the decision-relevant data lives

| Question | Answer in this folder | Article |
|---|---|---|
| Bond terms, coupons, covenants, guarantors, step-ups | 9 Spanish offer/placement notices; PRs for USD notes; coupon notices | [[bimbo-bond-prospectus-terms]] |
| What did Bimbo pay and what did it expect | Sara Lee, Iberia, Canada Bread decks and circular; deal PRs | [[bimbo-major-deals-terms]] |
| How much is returned and at what price | AGM notices, equity notes, daily share counts | [[bimbo-agm-dividends-and-buybacks]] |
| Who is paid and who trades with the group | Notes 15 and 20 in the FY2025 statements; AR fee sections | [[bimbo-related-party-and-compensation-disclosures]] |
| What happened when | 122 PRs and RNS notices | [[bimbo-material-events-timeline]] |

## Connections

- Master map of filings: [[bimbo-filings-source-map]]; CIQ-derived articles: [[ciq-corporate-issuance-history]], [[ciq-ownership-structure]], [[ciq-debt-stack-and-maturity-ladder]].
- Governance and ownership that the notices complement: [[bimbo-governance-and-ownership]].
- Acquisition history: [[bimbo-history-2008-2013]], [[bimbo-history-2014-2020]], [[bimbo-acquisitions]].

**Contradictions and extensions of existing claims**

- [[bimbo-history-2008-2013]] and [[bimbo-acquisitions]] expect Weston Foods material; none exists in this folder (the "NewBakeryCompany" S-4s are a restaurant company).
- [[ciq-debt-stack-and-maturity-ladder]] cites CIQ as a data source for bond stacks; the offering notices in this folder show that CIQ's file names for the same bonds are unreliable.

## Key Takeaways

- Only about 15 of 1,255 in-scope files drive the investment case: 9 offer notices, 3 merger presentations, the 2026 AGM package, the 4 AGM notices of 2023-2026 and the FY2025 statements; the rest is history, duplication or noise.
- ==Nine "merger and prospectus" files are Wendy's/Arby's documents misfiled under a Bimbo name; there are no Weston Foods or Fargo deal documents in the folder== [sourced].
- 42 Canada Bread MISC files, two Fargo annual reports, two bylaw scans and four early AGM notices are image-only and unreadable without OCR; they should be re-requested or OCR-processed if needed.
- The covenant text of each local bond (the *Suplemento*) and the AGM minutes with the buyback ceilings are the two highest-value documents missing from the folder.
- The 43 daily share-count notices are the only primary evidence of 2026 buyback activity and are consistent with the 2Q26 filing's share count to within one day [sourced].
