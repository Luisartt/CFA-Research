---
name: valuation
description: Value a CFA Research Challenge company with the plugin's model - DCF with Gordon and exit-multiple terminal values, reverse DCF, peer comparables, WACC for LatAm (local risk-free vs USD plus country risk, bottom-up beta, leases in the capital structure), sensitivity grid and football field - by writing valuation/valuation.yaml, running the engine and reading the results. Gathers market and peer data with sources; coaches the team on WACC judgment calls, terminal assumptions, and the target price and recommendation, which the team decides. Use whenever a student asks about WACC, DCF, target price, upside, multiples, comparables, terminal value, football field, or whether to rate the stock buy, hold or sell - even if they don't say valuation.
---

# valuation

## Purpose

Turn the forecast into a defensible target price. Data gathering and mechanics
are the assistant's job; the judgment calls — WACC inputs, terminal assumptions,
the target price and the recommendation — belong to the team.

## Reads

- `model/model-summary.json` with forecast lines — missing or built without
  `drivers.yaml` (its `warnings` contain "model/drivers.yaml not found"): run the
  model skill's build first and say the valuation rests on engine defaults until
  the forecast skill has run.
- `research/industry.md` — the peer set. Missing: propose 4-8 peers and add a
  `todo.md` item to confirm them with the industry skill.
- `research/thesis.md` — direction, catalysts, kill criteria (for the recommendation).
- `data/adjustments.md` and the balance-sheet notes — associates, pensions,
  provisions (bridge items).
- `company-profile.yaml` — currency, fiscal year end.
- `valuation/valuation.yaml` — if present, revise it.
- `references/wacc-latam.md`, `references/valuation-template.yaml`,
  `references/recommendation-guide.md`.

## Steps

1. **Market data.** Current share price, 52-week range and date (web search if
   available, else ask the team); `years_since_fiscal_year_end` from today and
   the fiscal year end. Cite source and date.
2. **WACC inputs** per `references/wacc-latam.md`: choose the currency route,
   risk-free, ERP, CRP (0 unless the reporting currency is USD), bottom-up unlevered beta from
   peers, target D/E with leases, pre-tax cost of debt, marginal tax. Propose
   values with sources; the team confirms (Coach moments).
3. **Peers** from the industry peer set: price, shares, net debt incl. leases +
   NCI, next-year EBITDA and EPS (consensus if available, else say "trailing").
   Drop peers with non-positive EBITDA or EPS and say so.
4. **Bridge items**: `non_operating_assets`, `debt_like_items` from the notes.
5. **Terminal**: propose `growth`, `exit_ev_ebitda`, `lt_nominal_gdp_growth`.
6. **Write `valuation/valuation.yaml`** from the template with `target_price: null`.
   Find Python 3.10 or newer as in init-skills (`python3`, `python`, then `py` on
   Windows; confirm with
   `<python> -c "import sys; assert sys.version_info >= (3, 10)"` — macOS's
   built-in python3 may be 3.9, install from python.org); if Python, openpyxl or
   pyyaml is missing, give the install command from init-skills and stop. From
   the project folder run:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project .`
   (if `${CLAUDE_PLUGIN_ROOT}` does not resolve in the shell, locate
   `skills/model/engine/build_model.py` in the installed plugin folder and use its
   absolute path, in quotes; exit 3 = model definition error: report it as a
   plugin bug; never edit the engine). Read `valuation` and `checks` in `model/model-summary.json`; explain every
   valuation WARN or ERROR in one plain sentence and fix input mistakes.
7. **Coach the target price and recommendation** with
   `references/recommendation-guide.md`. Write the team's `target_price` into
   `valuation.yaml` and rebuild so the football field shows it.
8. **Write `valuation/valuation.md`**: inputs with sources, results by method,
   sensitivity range, reverse-DCF reading, reconciliation, target price,
   recommendation, and what would change it (tie to the thesis kill criteria).

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **WACC judgment calls:** currency route, beta source, target D/E.
- **Terminal assumptions:** g vs long-term GDP, exit multiple vs peers, what
  `tv_ronic` implies.
- **Target price and recommendation:** primary method or weights, how methods
  reconcile, expected return vs the team's convention, the catalyst.

## Writes

- `valuation/valuation.yaml`, `valuation/valuation.md`; a new model version (engine).
- Appends coach-moment answers to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — valuation — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | valuation | valuation/valuation.yaml, valuation.md | gathered market and peer data, ran valuation; team set target <price> and <rating>`
- `docs/context/memory.md`: `# decision: target price <x>, <rating>, primary method <m>`.
- `docs/context/todo.md`: any input still `unverified` (price date, peer data).
