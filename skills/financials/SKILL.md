---
name: financials
description: Turn a CFA Research Challenge company's filings (annual reports, 10-K / 20-F, audited statements from BMV, B3, CMF, SMV) into the model's input file data/financials.csv - every figure mapped to the model's chart of accounts with document and page - plus data/adjustments.md explaining every mapping and accounting adjustment in plain words. The assistant does all extraction and accounting (IFRS 16 leases, PTU, costs by nature, associates, restatements) and validates the result with the model engine. Use whenever a student asks to extract, capture, load or map financial statements, "put the numbers in", "pull the last five years", or asks why a model number differs from the annual report - even if they don't mention the model.
---

# financials

## Purpose

Get the history right so the team can spend its time on the story. Extraction
and accounting are the assistant's job, done completely and explained plainly
in `data/adjustments.md` so any team member can defend the numbers in Q&A.

## Reads

- `company-profile.yaml` — framework, currency, units, fiscal year end. Missing:
  ask for company, framework and units in one line, suggest
  `/research-challenge:init-skills`, continue.
- `filings/` — annual reports / audited statements. Empty or fewer than 3 years:
  stop and list exactly which documents to download and where (see
  `references/extraction-guide.md`); add a `todo.md` item.
- `data/financials.csv` and `data/adjustments.md` — if present, update them
  (new year, restatement) instead of starting over.
- `references/chart-of-accounts.md`, `references/extraction-guide.md`,
  `references/adjustments-template.md`.

## Steps

1. **Inventory.** List each document in `filings/`: type, fiscal years covered,
   framework, currency, units. Target 5 historical years (minimum 3). The most
   recent report's comparative columns win for earlier years.
2. **Extract** the income statement, balance sheet and cash-flow statement for
   every year, recording document and page for every figure.
3. **Map** each reported line to the chart in `references/chart-of-accounts.md`,
   following `references/extraction-guide.md` (opex netting, D&A from the cash
   flow, costs by nature, PTU, associates, leases under IFRS 16 or US GAAP).
   Add `total_assets_reported` and `net_income_reported` rows.
4. **Tie out** every year: assets = liabilities + equity, EBIT = reported
   operating income, net income = reported. A gap means a missed line — find it.
5. **Write `data/financials.csv`**: columns
   `line_item,year,value,tag,source_doc,page,note`; UTF-8; plain numbers in the
   profile's units; costs positive. Tag `sourced`, or `unverified` when a figure
   could not be tied to a page (add a `todo.md` item for each).
6. **Validate with the engine.** Find Python as in init-skills (`python3`,
   `python`, then `py` on Windows) and run from the project folder:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project . --check`
   Fix every `[x]` input error and rerun until it prints
   `[ok] inputs are valid`. Warnings about drivers are expected at this stage.
   A lease warning is not: add `lease_principal_paid`.
7. **Write `data/adjustments.md`** from `references/adjustments-template.md`:
   sources, mapping table, each adjustment in plain words, one-off items (kept in
   the numbers, flagged for the forecast), open items, and three questions a
   judge may ask with answers.
8. **Close** with five lines: years captured, framework and units, number of
   adjustments, open items, and the next step ("next: the forecast skill").

## Coach moments

No story decisions here. One review checkpoint: ask the model member to read the
three judge questions in `adjustments.md` and explain one answer back in their
own words. If the explanation is off, clarify it — the team must be able to
defend numbers they did not extract.

## Writes

- `data/financials.csv`
- `data/adjustments.md`

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | financials | data/financials.csv, data/adjustments.md | extracted and mapped <years> statements; <n> adjustments`
- `docs/context/memory.md`: `# decision: history <first>-<last>, <currency> <units>, <framework>`
- `docs/context/todo.md`: one item per `unverified` figure or missing document.
