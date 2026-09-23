# research-challenge plugin — design spec

- **Date:** 2026-09-22
- **Status:** approved; phases 1, 2a and 2b implemented
- **Repo:** `Luisartt/CFA-Research` (this repo = the plugin = its own marketplace)

## 1. Goal

A Claude Code plugin for university teams competing in the CFA Institute Research
Challenge (LatAm). It takes a team from raw filings to a finished equity research
report and pitch, producing an institutional-grade financial model on the way.

**Division of labor (the core design rule):**

- **The assistant does the mechanical and technical work**: filing ingestion,
  statement extraction, *all* accounting adjustments, model construction,
  valuation mechanics, drafting prose.
- **Students own the story**: the thesis, how their view differs from consensus,
  the 3-5 assumptions that carry the story, the target price and recommendation,
  which risks matter. Coaching concentrates exclusively on these decisions.
- The assistant is a **co-writer with coaching**, not a ghostwriter and not a
  pure Socratic tutor. AI use is **disclosed** in the report, fed by an automatic
  AI-use log.

## 2. Decisions taken

| # | Decision | Choice |
|---|---|---|
| 1 | Writing boundary | Co-writer with coaching; AI use disclosed |
| 2 | Language | Skills in English; report language chosen at init (EN/ES/PT); coaching follows the student's language |
| 3 | Distribution | Claude Code plugin with own marketplace |
| 4 | Persistent context | No hooks; instruction-driven updates + `/wrap-up` command; soft size caps |
| 5 | Model support | Institutional-grade xlsx built by the plugin |
| 6 | Accounting | Assistant owns it entirely; explains every adjustment in plain words |
| 7 | Skill coupling | Every skill usable independently so team members can split roles |
| 8 | Code origin | Independent plugin; borrows and adapts proven pieces of `cfamexico/research_analyst` (MIT, attributed) |
| 9 | Build order | Coaching skills -> engine -> report/pitch |

## 3. Install

```
/plugin marketplace add Luisartt/CFA-Research
/plugin install research-challenge@cfa-research
```

Then, once per team project folder: `/research-challenge:init-skills`.

Requirements on student machines: Claude Code, Python 3, `openpyxl`
(`python-docx` optional for .docx assembly). `init-skills` checks and prints the
exact install command per OS when something is missing. Works on Windows and macOS.

## 4. Skills

| Skill | Typical owner | Assistant does | Student decides (Coach moments) |
|---|---|---|---|
| `init-skills` | Team lead, once | Interview, writes project files, env check | Interview answers |
| `financials` | Model member | Files filings, extracts statements with page cites, makes all accounting adjustments, writes `adjustments.md` | None required; must read `adjustments.md` before Q&A |
| `industry` | Industry member | Porter five forces, life cycle, peers, market share, structure | Where the company really competes; what protects it |
| `thesis` | Everyone | Roast-me-style coaching on the thesis | 2-3 pillars, variant perception vs consensus, catalysts, kill criteria |
| `forecast` | Model member | Proposes drivers tied to thesis pillars; sanity-checks vs history and guidance | The 3-5 key assumptions |
| `model` | Model member | Builds xlsx (3 statements, schedules, ratios, checks) | Reviews it reflects the business |
| `valuation` | Valuation member | DCF + comps, LatAm WACC, sensitivities, football field | WACC inputs, terminal value, target price, recommendation |
| `risks-esg` | Any member | Risk matrix (probability x impact), LatAm governance checklist | Which risks matter and why |
| `report` | Writer | Co-writes Challenge structure, page budget, AI-use disclosure | Final say on every claim |
| `pitch` | Everyone | Deck outline + speaker notes, judge Q&A drill | Defending it |

Plus command `/wrap-up`: end-of-session update of context files.

Skills other than `init-skills` trigger from natural language ("build my model",
"draft the valuation section") as well as by name. `init-skills` is user-invoked
only (`disable-model-invocation: true`).

### 4.1 SKILL.md anatomy (all skills)

- Frontmatter: `name`, `description`. Description pattern: what it does ->
  "Use whenever ..." -> quoted trigger phrases -> "even if the user doesn't
  explicitly ask".
- Body, max 150 lines, fixed sections:
  1. **Purpose**
  2. **Reads** — input files, and what to do if each is missing
  3. **Steps**
  4. **Coach moments** — the story decisions (2-4 in judgment skills; mechanical
     skills like `financials` and `model` have at most one review checkpoint);
     everything else is just done
  5. **Writes** — output files
  6. **Log** — one line appended to `docs/context/ai-use-log.md` + context updates
- Detail in `references/`, loaded on demand.

### 4.2 Coaching mechanics

Coaching rules live in the project `AGENTS.md` (inherited by every skill):

- Restate the student's idea before challenging it; use their terms.
- Max 2-3 questions per turn, no compound questions.
- Flag weaknesses; do not silently fix the student's *thesis* (mechanical work
  is fixed, story decisions are flagged).
- End every turn with one clear next step.
- At each Coach moment: give a recommendation with its why, the strongest case
  against it, and one question the student must answer. The answer is appended
  to `thesis-journal.md`.
- If something is genuinely solid, say so plainly — false red flags burn trust.

`thesis` and the `pitch` Q&A drill use a graded question bank (adapted from
battle_tested_skills `roast-me`): L1 Frame -> L2 Probe -> L3 Stress. Escalate only
when the current level is answered cleanly; stop when questions stop producing
new information. Output uses a fixed synthesis template (thesis, what works, red
flags, next moves, "what would change my mind").

## 5. `init-skills`

Idempotent (from the user's `scaffold` skill): audit what exists -> interview only
if needed -> create only missing files -> for non-conforming files ask
`[k] keep / [o] overwrite / [m] merge` (default keep) -> verify and report.
A fully conforming project is a no-op.

**Interview** — one question at a time, default offered:

1. Company, ticker, exchange (BMV, B3, Bolsa de Santiago, BVC, BVL, US-listed ADR).
2. Sector -> specialist persona, offered for accept/edit:
   *"Senior equity research analyst, 15 years covering LatAm {sector} at a
   top-tier firm, based in {city}."*
3. Accounting framework — **inferred, then confirmed**: BMV non-financial -> IFRS;
   US domestic filer -> US GAAP; foreign private issuer ADR -> IFRS. Banks and
   insurers -> warning that valuation changes (DDM / residual income) and the
   v1 model does not cover them fully.
4. Report language (EN/ES/PT).
5. Team members and roles (optional) -> ownership in `todo.md`.
6. Report deadline and presentation date -> milestones in `todo.md`.
7. Confirmation that all material is public (CFA Standard II(A)).

**Writes:**

```
AGENTS.md              canonical: persona, coaching rules, who-decides table,
                       data tags, skill map, context-file rules
CLAUDE.md              "@AGENTS.md" import + Claude-only notes
company-profile.yaml   ticker, exchange, country, sector, framework, currency,
                       fiscal year end, report language, team, deadlines
docs/context/
  memory.md            decisions ("# decision: ...")
  thesis-journal.md    append-only: thesis evolution, coaching answers
  todo.md              milestones and tasks by owner (pending / in_progress only)
  lessons.md           corrections, so mistakes are not repeated
  ai-use-log.md        append-only: date | member | skill | section | what the AI did
  session-log.md       one line per work session
filings/  data/  research/  model/  valuation/  report/  pitch/
```

AGENTS.md is canonical so Codex/Cursor users get persona and rules too (they do
not get the skills). Context files are read on demand (grep, never bulk-read);
size caps are soft, stated as comments in each file.

**Data tags** (from research_analyst), required on every number:
`[sourced]` (filing + page), `[guidance]` (management said it),
`[assumption]` (team judgment), `[calc]` (computed). Plus `[unverified]` for an
extracted number that could not be tied to a page.

## 6. Data flow (file contracts)

```
financials -> data/financials.csv        line item x year, value, tag, source doc, page
              data/adjustments.md        each adjustment: what, why, effect, plain words
industry   -> research/industry.md
thesis     -> research/thesis.md (+ append thesis-journal.md)
forecast   -> model/drivers.yaml         driver, history, forecast, tag, rationale,
                                          thesis pillar it serves
valuation  -> valuation/valuation.yaml   WACC inputs, terminal method, peers, methods
model      -> model/<TICKER>_model_v<N>.xlsx   built from the three files above
              model/model-summary.json         computed numbers for downstream skills
risks-esg  -> research/risks-esg.md
report     -> report/sections/NN-<name>.md -> report/<TICKER>_report_v<N>.docx (optional)
pitch      -> pitch/outline.md, pitch/qa-drill.md
```

Independence rule: a skill whose input is missing states what is missing, then
either asks for the minimum it needs or proceeds with a placeholder tagged
`[assumption]` and adds a `todo.md` item. No skill blocks another. Each skill
writes only its own outputs; append-only shared logs use git `merge=union`
(installed by `init-skills` via `.gitattributes`), so parallel team members
merge cleanly. Versioned outputs (`_v<N>`) are never overwritten.

## 7. Model engine

New code in `skills/model/engine/` (research_analyst has no calculation engine;
only its style palette is adapted, attributed in NOTICE). Every cell is defined
once as an expression tree that is both evaluated in Python and rendered as an
Excel formula, so the two cannot drift; tests recalculate the whole workbook
with the `formulas` library as an Excel oracle and compare every formula cell.
Plan: `docs/superpowers/plans/2026-09-23-phase2a-model-engine.md`.

Decisions made while building (after reviews by a finance/valuation reviewer):
- Reported history sits in IS/BS/CF as blue cells with a comment (document,
  page, tag); there is no separate Historical tab.
- IFRS 16: lease liability stays in net debt; new leases (= lease principal
  repaid) are treated like capex in FCFF and added to PP&E.
- Intangible amortization is a separate driver; D&A net of it reduces PP&E.
- Dividends (parent and NCI) are never negative; long-term debt cannot go below
  zero; historical driver ratios with a zero denominator read 0.
- Valuation: mid-year convention with the Gordon terminal value discounted at
  N - 0.5 (exit multiple at N); discount conventions are editable cells; equity
  bridge includes non-operating assets and debt-like items; value per share is
  rolled forward to today at the cost of equity, and a 12-month target
  (value x (1 + ke) - next dividend) is shown. Sensitivity uses formula grids
  (n.m. where WACC - g < 1%), not Excel data tables.
- Excel-vs-Python parity checks show the Python value next to the check and are
  warnings (they go stale if inputs are edited in Excel; rebuild to refresh).
- Engine defaults: a missing driver is held at its last actual value and flagged
  (net new debt, share growth and amortization default to zero; minimum cash to
  last actual cash).
- Runtime dependencies: `openpyxl`, `pyyaml`.

- **Python computes the full model** (source of truth), then writes the xlsx
  with **live formulas**, formatted per excel-standards (blue inputs, black
  formulas, green links).
- Inputs: `data/financials.csv`, `model/drivers.yaml`, `valuation/valuation.yaml`
  (optional — without it, valuation tabs are omitted).
- Periodicity: annual, 3-5 historical years (last 5 used) + 1-10 forecast years
  (default 5).
- Tabs: Cover, Drivers, IS, BS, CF, Schedules (revenue build,
  capex/D&A, working-capital days, debt/interest), Ratios, WACC, DCF, Comps,
  Sensitivity, Football, Checks.
- **Checks tab** (Excel formulas; evaluates in any Excel on Windows or macOS):
  - ERROR: BS balances; CF closing cash = BS cash; equity roll-forward;
    revolver >= 0; cash >= minimum; PP&E >= 0; long-term debt >= 0; reported
    totals tie (total assets, net income from `financials.csv`); revenue
    segments tie to revenue; WACC > g; g <= long-term nominal GDP.
  - WARN (flagged, not a failure): terminal value share of EV < 75%; WACC - g
    spread >= 2 points; revolver unused; Gordon and exit-multiple values per
    share positive; TV methods agree (exit multiple implied by Gordon within
    0.5x-2x of the exit multiple input); **Excel-vs-Python parity** (Excel result
    vs Python-computed value written alongside).
- `model-summary.json` exposes computed figures to `valuation`, `report` and
  `pitch` without requiring Excel recalculation.
- No Excel recalculation at build time (the engine writes formulas; Excel
  recalculates on open), so the build runs the same on Windows and macOS.
- If checks fail, the file is still written, and the Cover shows
  **CHECKS FAILING** in red.
- CLI exit codes: 0 built (even if checks fail; read `status` in
  `model-summary.json`); 2 input error; 3 model definition error; 4 file could
  not be written.
- Console output ASCII-only (`[ok]`, `[x]`, `->`).

**Main build risk:** keeping Python calculation and Excel formulas in parity.
The parity check is the guard; the fallback (LibreOffice headless recalculation)
was rejected because it adds an install for every student.

## 8. `report` and `pitch`

**report**
- Structure and page limits live in `skills/report/references/challenge-structure.md`,
  editable. Default (assumed, to verify against current Challenge rules):
  cover (recommendation, target price, key data), investment summary, business
  description, industry overview and competitive positioning, valuation,
  financial analysis, investment risks, ESG, appendices; ~10 pages + appendices.
- One file per section so members write in parallel.
- Co-writes from upstream files and cites them; flags any claim without a tag;
  tracks the page budget; assembles `.docx` if `python-docx` is installed.
- Drafts the **AI-use disclosure appendix** from `ai-use-log.md`.

**pitch**
- 10-12 slide outline + speaker notes (students build the deck themselves).
- **Judge Q&A drill**: ~30 likely questions generated from the team's own files
  (adjustments, weakest assumption, terminal value share, bear case), run as a
  mock Q&A with a scorecard.

## 9. Error handling

| Situation | Behavior |
|---|---|
| Upstream file missing | Placeholder tagged `[assumption]` + `todo.md` item; continue |
| Python / openpyxl missing | Exact install command for the student's OS; stop that step only |
| Extracted number without a page | Tagged `[unverified]`, listed in `adjustments.md` |
| Model checks fail | xlsx still written; Cover shows CHECKS FAILING |
| Bank / insurer issuer | Warning at init; DDM / residual income guidance; no full model in v1 |
| Existing file differs from template | `[k]/[o]/[m]`, default keep; never silent overwrite |

## 10. Testing

- **Engine:** pytest with a small fictional company fixture — BS balances, parity
  holds, version bump never overwrites, missing `valuation.yaml` omits tabs cleanly.
- **Skills:** 2-3 eval prompts per skill: correct skill triggers; key behavior
  occurs (e.g., `thesis` restates before challenging; `financials` writes a page
  cite for every sourced number; `report` flags untagged claims).
- **End-to-end:** one full run on a real BMV-listed company before release.

## 11. Repo layout

```
.claude-plugin/
  plugin.json
  marketplace.json
skills/
  init-skills/  financials/  industry/  thesis/  forecast/
  model/  valuation/  risks-esg/  report/  pitch/
    SKILL.md (+ references/)
skills/init-skills/templates/   AGENTS.md, CLAUDE.md, docs/context/*, company-profile.yaml
skills/model/engine/            model engine (rcmodel package, build_model.py) + tests/
commands/wrap-up.md
tests/                  structural tests (pytest)
evals/                  manual eval prompts per phase
README.md  LICENSE (MIT)  NOTICE (research_analyst attribution)
```

Skills reference only files inside their own directory (the plugin cache path
differs per machine). Shared code lives inside the skill that owns it: the
engine belongs to `model`; `valuation` writes `valuation/valuation.yaml` and
hands off to `model` to rebuild the workbook.

## 12. Reused material

| From | What | How |
|---|---|---|
| `cfamexico/research_analyst` | xlsx builder style palette only | Adapted (engine is new code) |
| | `framework-mapper` IFRS/US GAAP/NIF reference | Reference file for `financials` |
| | `issuer-profile.yaml` fields | Slimmed into `company-profile.yaml` |
| | Data tags, MNPI guard, 7-section industry report | Adopt |
| `alanvaa06/battle_tested_skills` | `scaffold` audit -> interview -> create -> verify | Pattern for `init-skills`, without hooks |
| | `roast-me` coaching rules and graded question bank | `thesis`, `pitch`, AGENTS.md coaching rules |
| | `excel-standards` formatting rules | Engine formatting |

## 13. Out of scope (v1)

- Quarterly model updates and ongoing coverage maintenance
- Automatic filing download (BMV has no public API; students drop PDFs in `filings/`)
- Full bank / insurer models
- Generating the slide deck file
- Hooks of any kind

## 14. Build order

1. `init-skills`, `thesis`, `industry`, `/wrap-up` + templates + plugin manifests
   (done: plan `docs/superpowers/plans/2026-09-22-phase1-foundation-coaching-skills.md`)
2. `financials`, `forecast`, `model`, `valuation` + engine
   (done: plans 2026-09-23-phase2a-model-engine.md, 2026-09-24-phase2b-model-skills.md)
3. `risks-esg`, `report`, `pitch`

## 15. Open items to verify during implementation

- Current CFA Research Challenge rules: report page limits, section requirements,
  AI-use disclosure wording.
- Resolved: marketplace name is `cfa-research`
  (`/plugin install research-challenge@cfa-research`).
- Resolved: skills reference only their own directory (see §11).
