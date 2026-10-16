# Report structure (CFA Institute Research Challenge, 2026-2027 Official Rules)

Check the current season's rules if they change; these facts are from the
2026-2027 Official Rules (PDF of 2026-07-16).

## Hard rules

- English, at every round (rule 2.6c).
- At most 10 A4 pages, plus an appendix of at most 10 A4 pages (rule 2.6b). The
  official cover page does not count.
- The official CFA Institute cover page goes in front, unaltered except its
  highlighted fields; it carries the required disclosures. Download it from the
  Research Challenge student-preparation page. The plugin never generates it.
- Public information only; the team's original work; a recognized citation
  system (this plugin uses Harvard); written as an independent research analyst.
- Disclose material reliance on AI tools (rule 2.4d, Appendix B).

## First-page header (built from `report/header.yaml`)

Company, exchange and ticker, sector / industry, recommendation (BUY / HOLD /
SELL), current price with date, target price with % upside or downside.

## Sections, files and page budget

| File | Section | Rubric points | Page budget |
|---|---|---|---|
| `01-investment-summary.md` | Investment summary | 15 | 1.5 |
| `02-business-description.md` | Business description | 5 | 0.5 |
| `03-industry.md` | Industry overview and competitive positioning | 10 | 1.0 |
| `04-financial-analysis.md` | Financial analysis | 20 | 2.0 |
| `05-valuation.md` | Valuation | 20 | 2.0 |
| `06-risks.md` | Investment risks | 15 | 1.5 |
| `07-esg.md` | ESG | 15 | 1.5 |
| `98-appendix.md` | Appendix (not graded separately; max 10 pages) | - | - |
| `99-appendix-ai-use.md` | AI-use disclosure (part of the appendix) | - | - |

The rules list the sections without mandating an order; putting the
investment summary first, under the header, is the common practice. File
numbers set the order — rename files to change it.

Budget rule of thumb: about 500 words per page; a full-width chart takes about
0.45 of a page, two half-width charts side by side about 0.3 together.
`build_docx.py --check` does this arithmetic.

## Appendix (suggested)

Income statement, balance sheet and cash flow (history + forecast), DCF summary
and WACC, comps table, sensitivity grid, full risk table, ESG data, references
(Harvard list), and the AI-use disclosure.
