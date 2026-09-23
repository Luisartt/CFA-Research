---
name: init-skills
description: One-time setup for a CFA Research Challenge team project. Interviews the team (company, exchange, sector, accounting framework, report language, roles, deadlines), builds a LatAm sector-specialist analyst persona, and writes AGENTS.md, CLAUDE.md, company-profile.yaml, the docs/context memory files and the project folders. Idempotent - audits first, fills only gaps, never overwrites silently. Run it once per team folder before the other research-challenge skills, or again to repair a broken setup.
disable-model-invocation: true
---

# init-skills

## Purpose

Set up a team's project so every other skill has a persona, shared facts
(`company-profile.yaml`) and memory (`docs/context/`). A project that is already
set up must cost the team nothing: audit first, act only on gaps.

## Reads

- The current project folder (what already exists).
- `filings/` if present — infer company, exchange and currency from the files.
- `templates/` and `references/framework-inference.md` in this skill's base directory.

## Steps

### Step 1 — Audit (before touching anything)

Check each item and print a table `item | present | missing | non-conforming`:

1. `AGENTS.md` exists with a non-empty `## System Persona` and the headings
   `## Who decides what`, `## Coaching rules`, `## Data tags`, `## AI-use log`.
2. `CLAUDE.md` exists and its first non-empty line is `@AGENTS.md`.
3. `company-profile.yaml` exists and contains no `{{`.
4. The six files in `docs/context/` exist.
5. Folders exist: `filings/ data/ research/ model/ valuation/ report/ pitch/`.
6. `.gitattributes` contains the three `merge=union` lines from `templates/gitattributes`.

All conform -> say "Project already set up. Nothing changed." and stop.

### Step 2 — Environment check (warn, never block)

Try `python3 --version`, then `python --version`, then (Windows) `py --version`;
use the first that works to run `<cmd> -c "import openpyxl, yaml"`. Phase-1 skills do
not need Python; the model skills will. If missing, print the exact command and
offer to run it:

- Python missing -> Windows: `winget install Python.Python.3.12`; macOS: install
  from python.org (or `brew install python` if Homebrew is installed)
- openpyxl or PyYAML missing -> Windows: `py -m pip install openpyxl pyyaml python-docx`; macOS: `python3 -m pip install openpyxl pyyaml python-docx`

### Step 3 — Interview (only for what the audit found missing)

One question at a time. Always offer a default the student can accept with
"ok". If `filings/` has documents, infer answers and ask to confirm instead.

1. Company, ticker and exchange.
2. Sector. Then propose the persona and ask accept/edit:
   "Senior equity research analyst with 15 years covering LatAm {sector} at a
   top-tier investment bank, based in {city}. Known for tying every forecast to
   how the business actually makes money. Has mentored dozens of junior
   analysts: demanding on the story, generous with technique."
3. Accounting framework, reporting currency, fiscal year end, units — propose
   from `references/framework-inference.md`, ask to confirm. Bank, insurer or
   REIT -> read the issuer-type table there and warn what changes.
4. Report language: en / es / pt.
5. Team members and roles (optional): model, industry, valuation, writer, all.
6. Report deadline and presentation date (YYYY-MM-DD).
7. "Is all the material you will use public information?" (CFA Standard II(A)).
   If not yes, explain the rule and do not record `true`.

### Step 4 — Create missing files

Copy from `templates/` in this skill's base directory; never edit the templates.
Replace every token:

| Token | Value |
|---|---|
| `{{COMPANY_NAME}}` `{{TICKER}}` `{{EXCHANGE}}` `{{COUNTRY}}` `{{SECTOR}}` | Q1-Q2 |
| `{{ISSUER_TYPE}}` | non_financial, bank, insurer or reit |
| `{{SYSTEM_PERSONA}}` | Persona text accepted in Q2 |
| `{{FRAMEWORK}}` `{{CURRENCY}}` `{{FISCAL_YEAR_END}}` `{{UNITS}}` | Q3 |
| `{{FRAMEWORK_CONFIRMED}}` | `true` if the team confirmed, else `false` |
| `{{REPORT_LANGUAGE}}` | Q4 |
| `{{TEAM}}` | One line, e.g. `Ana (model), Luis (industry)` or `not assigned yet` |
| `{{TEAM_YAML}}` | One `  - name: "..."` / `    role: "..."` pair per member, or `  []` |
| `{{REPORT_DEADLINE}}` `{{PRESENTATION_DATE}}` | Q6 |
| `{{MILESTONES}}` | See below |
| `{{MNPI_CONFIRMED}}` | `true` only on an explicit yes in Q7, else `false` |
| `{{TODAY}}` | Today, YYYY-MM-DD |

`{{MILESTONES}}`: count back from the report deadline D, one todo line each:
thesis v1 (D-42), industry analysis (D-35), model v1 (D-28), valuation and target
price (D-21), report draft (D-10), final report (D), presentation (presentation
date). Format: `- [pending] <milestone> — owner: <role or all> — due: <date>`.

Create the seven folders with an empty `.gitkeep` in each.

Copy `templates/gitattributes` to `.gitattributes` in the project root; if a
`.gitattributes` already exists, append only the missing lines (no k/o/m
prompt needed).

A file that exists but does not conform: show the difference and ask
`[k] keep / [o] overwrite / [m] merge` (default keep). Merge = add the missing
sections from the template, keep every existing line. Never overwrite silently.

### Step 5 — Verify and report

Re-run the Step 1 audit. Print `file | created / kept / merged`. Then give one
next step: "Next: say \"let's work on our thesis\" (or run
`/research-challenge:thesis`), or \"analyze the industry\"
(`/research-challenge:industry`). Drop the latest annual and quarterly reports
into `filings/`."

## Coach moments

- **Persona (Q2):** the persona sets the bar for every later answer — invite the
  team to sharpen the sector focus rather than accept a generic one.
- **Framework (Q3):** ask the team to open the accounting policies note and
  confirm; one minute now avoids comparing IFRS and US GAAP numbers later.

## Writes

`AGENTS.md`, `CLAUDE.md`, `company-profile.yaml`, `docs/context/*.md` (6),
`.gitattributes`, `filings/ data/ research/ model/ valuation/ report/ pitch/`.

## Log

- `docs/context/ai-use-log.md`: `YYYY-MM-DD | <member> | init-skills | project setup | created project files and persona`
- `docs/context/memory.md`: `# decision: framework = <framework> (confirmed by team: yes/no)` and `# decision: report language = <lang>`
- `docs/context/session-log.md`: `[YYYY-MM-DD]: project set up with init-skills — <member>`
