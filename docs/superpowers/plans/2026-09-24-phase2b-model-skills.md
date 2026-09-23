# Phase 2b — Model Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the four skills that drive the phase 2a engine — `financials`, `forecast`, `model`, `valuation` — so a team goes from annual reports in `filings/` to a built, checked, valued model, with coaching only on the story decisions.

**Architecture:** Each skill is a `SKILL.md` (max 150 lines, fixed sections) plus on-demand `references/`. The skills never compute numbers themselves: they write the engine's input files (`data/financials.csv`, `model/drivers.yaml`, `valuation/valuation.yaml`) and run the engine at `${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py` (Claude Code substitutes `${CLAUDE_PLUGIN_ROOT}` in skill text). They read results from `model/model-summary.json`. Two small engine additions support this: a `--check` mode (validate and evaluate without writing files) and a richer summary (drivers and key ratios).

**Tech Stack:** Markdown skills; the phase 2a Python engine; pytest structural tests (sync tests import `rcmodel` so references cannot drift from the engine).

**Spec:** `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` §4, §6, §7.

**Branch:** continue on `feat/phase2a-engine`; merge to `main` after this plan (engine + skills ship together).

**Division of labor (from the spec — every SKILL.md must respect it):** the assistant does all extraction, accounting adjustments, file writing and engine runs; the team decides the 3-5 key assumptions, WACC judgment calls, terminal value, target price and recommendation. The AI-use log gets one line per session.

---

## File map

| File | Responsibility |
|---|---|
| `skills/model/engine/rcmodel/cli.py` | add `--check` (no files written) |
| `skills/model/engine/rcmodel/summary.py` | add `drivers` and `ratios` sections |
| `tests/test_plugin_structure.py` | cover the 4 new skills; engine path and reference-sync tests |
| `skills/financials/SKILL.md` + `references/chart-of-accounts.md`, `extraction-guide.md`, `adjustments-template.md` | filings -> financials.csv + adjustments.md |
| `skills/forecast/SKILL.md` + `references/drivers-guide.md`, `drivers-template.yaml` | drivers.yaml tied to thesis pillars |
| `skills/model/SKILL.md` + `references/reading-the-model.md`, `model-summary.md` | build, read, explain, route fixes |
| `skills/valuation/SKILL.md` + `references/wacc-latam.md`, `valuation-template.yaml`, `recommendation-guide.md` | valuation.yaml, run, target price coaching |
| `skills/init-skills/templates/AGENTS.md`, `README.md`, `.claude-plugin/*.json`, `evals/phase2.md` | integration |

---

### Task 1: Engine support for the skills (`--check`, richer summary)

**Files:**
- Modify: `skills/model/engine/rcmodel/cli.py`
- Modify: `skills/model/engine/rcmodel/summary.py`
- Test: `skills/model/engine/tests/test_cli.py`

- [ ] **Step 1: Write the failing tests** — append to `skills/model/engine/tests/test_cli.py`

```python
def test_check_mode_writes_nothing(project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(project), "--check"]) == 0
    assert not list((project / "model").glob("*.xlsx"))
    assert not (project / "model" / "model-summary.json").exists()
    out = capsys.readouterr().out
    assert out.isascii()
    assert "[ok] inputs are valid (check only, no files written)" in out
    assert "status:" in out


def test_check_mode_reports_input_errors(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "cash"}
    write_project(tmp_path, history=history)
    assert main(["--project", str(tmp_path), "--check"]) == 2
    assert "cash" in capsys.readouterr().out


def test_summary_has_drivers_and_ratios(project: Path) -> None:
    assert main(["--project", str(project)]) == 0
    summary = json.loads((project / "model" / "model-summary.json").read_text(encoding="utf-8"))
    gross_margin = summary["drivers"]["gross_margin"]
    assert gross_margin["source"] == "team"
    assert gross_margin["values"]["2026"] == pytest.approx(0.41)
    assert gross_margin["values"]["2025"] == pytest.approx(5500 / 13400)
    assert "r_roic" in summary["ratios"]
    assert "r_ebitda_margin" in summary["ratios"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_cli.py`
Expected: the 3 new tests FAIL (`unrecognized arguments: --check`, `KeyError: 'drivers'`).

- [ ] **Step 3: Add the summary sections** — in `rcmodel/summary.py`

Add after `SUMMARY_VALUES`:

```python
SUMMARY_RATIOS: tuple[str, ...] = (
    "r_revenue_growth", "r_gross_margin", "r_ebitda_margin", "r_ebit_margin", "r_net_margin",
    "r_fcf_margin", "r_roe", "r_roic", "r_net_debt_ebitda", "r_interest_cover", "r_ccc",
)
```

Replace the body of `build_summary` so the per-year extraction is shared and the two new sections are added:

```python
def _series(model: Model, key: str) -> dict[str, float | None]:
    return {
        str(year): None if isinstance(model.cell(key, t), BlankCell) else _clean(model.value(key, t))
        for t, year in enumerate(model.inputs.years)
    }


def build_summary(model: Model, results: Sequence[CheckResult], info: BuildInfo) -> dict[str, Any]:
    inputs = model.inputs
    lines = {key: _series(model, key) for key in SUMMARY_LINES if model.has(key)}
    ratios = {key: _series(model, key) for key in SUMMARY_RATIOS if model.has(key)}
    drivers = {
        line.key: {
            "label": line.label,
            "source": "team" if line.key in inputs.drivers else "engine default",
            "values": _series(model, line.key),
        }
        for line, _ in model.placed.lines
        if line.sheet == "Drivers"
    }
    valuation = {key: _clean(model.value(key, None)) for key in SUMMARY_VALUES if model.has(key)}
    return {
        "company": inputs.profile.name,
        "ticker": inputs.profile.ticker,
        "framework": inputs.profile.framework,
        "currency": inputs.profile.currency,
        "units": inputs.profile.units,
        "model_file": info.filename,
        "version": info.version,
        "built_on": info.built_on.isoformat(),
        "historical_years": list(inputs.hist_years),
        "forecast_years": list(inputs.fcst_years),
        "status": overall_status(results),
        "lines": lines,
        "ratios": ratios,
        "drivers": drivers,
        "valuation": valuation,
        "checks": [
            {"check": r.label, "year": None if r.period is None else inputs.years[r.period], "status": r.status}
            for r in results
        ],
        "warnings": list(inputs.warnings),
    }
```

- [ ] **Step 4: Add `--check`** — in `rcmodel/cli.py`

Add this function after `build`:

```python
def check(project: Path) -> tuple[tuple[CheckResult, ...], tuple[str, ...], str, tuple[int, ...]]:
    """Load, evaluate and run every check without writing any file."""
    inputs = load_inputs(project)
    model, _ = assemble(inputs)
    results = evaluate_checks(model, [*build_checks(inputs), *parity_checks(model)])
    return tuple(results), inputs.warnings, overall_status(results), inputs.years
```

In `main`, add the argument after `--project`:

```python
    parser.add_argument("--check", action="store_true",
                        help="Validate inputs and run every check without writing the workbook or summary")
```

Replace the block from `try:` to the end of `main` with:

```python
    project = Path(args.project).resolve()
    try:
        if args.check:
            results, warnings, status, years = check(project)
        else:
            result = build(project, date.today())
            results, warnings, status, years = result.results, result.warnings, result.status, result.years
    except InputError as exc:
        print("[x] Cannot build the model. Fix these inputs first:")
        for message in exc.messages:
            print("  - " + ascii_safe(message))
        return EXIT_INPUT_ERROR
    except ModelError as exc:
        print("[x] Model definition error: " + ascii_safe(str(exc)))
        return EXIT_MODEL_ERROR
    except OSError as exc:
        target = Path(exc.filename).name if exc.filename else "a file in model/"
        print(f"[x] Could not write {ascii_safe(target)}: {ascii_safe(exc.strerror or str(exc))}.")
        print("    Close it if it is open in Excel or another program (or pause OneDrive sync), then run again.")
        return EXIT_IO_ERROR
    if args.check:
        print("[ok] inputs are valid (check only, no files written)")
    else:
        print(f"[ok] workbook -> model/{ascii_safe(result.workbook.name)}")
        print("[ok] summary  -> model/model-summary.json")
    counts = {s: sum(1 for r in results if r.status == s) for s in ("OK", "ERROR", "WARN")}
    print(f"checks: {counts['OK']} OK, {counts['ERROR']} ERROR, {counts['WARN']} WARN")
    for r in results:
        if r.status != "OK":
            year = "" if r.period is None else f" ({years[r.period]})"
            marker = "[x]" if r.status == "ERROR" else "[warn]"
            print(f"{marker} Not met: {ascii_safe(r.label)}{year}")
    for warning in warnings:
        print("[warn] " + ascii_safe(warning))
    print(f"status: {status}")
    return EXIT_OK
```

- [ ] **Step 5: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests; python -m mypy tests skills/model/engine`
Expected: all pass; mypy `Success`.

- [ ] **Step 6: Commit**

```bash
git add skills/model/engine/rcmodel/cli.py skills/model/engine/rcmodel/summary.py skills/model/engine/tests/test_cli.py
git commit -m "feat(engine): --check mode and drivers/ratios in model-summary.json"
```

---

### Task 2: Structural tests for the new skills

**Files:**
- Modify: `tests/test_plugin_structure.py`

- [ ] **Step 1: Extend the skill list and add engine/sync tests**

In `tests/test_plugin_structure.py`, rename `PHASE1_SKILLS` to `SKILLS` everywhere and set it to:

```python
SKILLS: tuple[str, ...] = ("init-skills", "thesis", "industry", "financials", "forecast", "model", "valuation")
```

Append at the end of the file:

```python
ENGINE_SKILLS: tuple[str, ...] = ("financials", "forecast", "model", "valuation")
ENGINE_CALL = "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py"
ENGINE_DIR = SKILLS_DIR / "model" / "engine"


@pytest.mark.parametrize("name", ENGINE_SKILLS)
def test_engine_skills_call_the_engine_by_plugin_root(name: str) -> None:
    assert ENGINE_CALL in read_text(skill_md(name))
    assert (ENGINE_DIR / "build_model.py").is_file()


def _engine_chart() -> tuple[tuple[str, ...], tuple[str, ...]]:
    import sys

    if str(ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(ENGINE_DIR))
    from rcmodel.chart import CHART, DRIVER_KEYS

    return tuple(item.key for item in CHART), DRIVER_KEYS


def test_chart_reference_lists_every_engine_line_item() -> None:
    chart_keys, _ = _engine_chart()
    text = read_text(SKILLS_DIR / "financials" / "references" / "chart-of-accounts.md")
    missing = [key for key in chart_keys if f"`{key}`" not in text]
    assert not missing, missing


def test_drivers_guide_lists_every_engine_driver() -> None:
    _, driver_keys = _engine_chart()
    for path in (SKILLS_DIR / "forecast" / "references" / "drivers-guide.md",
                 SKILLS_DIR / "forecast" / "references" / "drivers-template.yaml"):
        text = read_text(path)
        missing = [key for key in driver_keys if key not in text]
        assert not missing, (path.name, missing)


def test_valuation_template_matches_the_loader() -> None:
    text = read_text(SKILLS_DIR / "valuation" / "references" / "valuation-template.yaml")
    for field in ("share_price", "price_52w_low", "price_52w_high", "years_since_fiscal_year_end",
                  "non_operating_assets", "debt_like_items", "risk_free", "equity_risk_premium",
                  "country_risk_premium", "beta_unlevered", "target_debt_to_equity", "pre_tax_cost_of_debt",
                  "tax_rate", "growth", "exit_ev_ebitda", "lt_nominal_gdp_growth", "peers", "target_price"):
        assert f"{field}:" in text, field
```

- [ ] **Step 2: Run the tests to verify the new ones fail**

Run: `python -m pytest -q tests`
Expected: the phase 1 tests pass; every test parametrized with `financials`, `forecast`, `model`, `valuation`, plus the three sync tests, FAIL (files missing).

- [ ] **Step 3: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add tests/test_plugin_structure.py
git commit -m "test: structural and engine-sync tests for the model skills"
```

---

### Task 3: `financials` skill

**Files:**
- Create: `skills/financials/references/chart-of-accounts.md`
- Create: `skills/financials/references/extraction-guide.md`
- Create: `skills/financials/references/adjustments-template.md`
- Create: `skills/financials/SKILL.md`

- [ ] **Step 1: Create `skills/financials/references/chart-of-accounts.md`**

```markdown
# Chart of accounts (what goes in data/financials.csv)

One row per line item per year: `line_item,year,value,tag,source_doc,page,note`.
Values in the units of `company-profile.yaml` (e.g. MXN millions), plain numbers,
no thousands separators. **Costs, capex, taxes and dividends are positive**; the
model subtracts them. Tags: `sourced` (from a filing, with page) or `unverified`.

Rule: components must add up to the reported totals. When the company reports
an item the chart has no line for, fold it into the closest "other" line and
record the fold in `data/adjustments.md`.

## Income statement

| Key | Required | What to put there | Typical source |
|---|---|---|---|
| `revenue` | yes | Net sales / total revenue | Income statement, first line |
| `cogs` | yes | Cost of sales, positive (includes D&A if the company puts it there) | Income statement |
| `opex` | yes | SG&A + other operating expenses - other operating income, positive | Income statement lines between gross profit and operating income |
| `da` | yes | Depreciation + amortization (incl. right-of-use assets), positive | Cash-flow statement, operating section add-backs |
| `interest_expense` | yes | Interest expense incl. lease interest, positive | Financial result note |
| `interest_income` | no | Interest income, positive | Financial result note |
| `other_financial_net` | no | FX result, derivatives, share of associates, other non-operating; income positive, loss negative | Financial result + associates lines |
| `income_tax` | yes | Income tax expense (current + deferred), positive = expense | Income statement |
| `nci_income` | no | Net income attributable to non-controlling interests | Bottom of income statement |
| `shares_diluted` | yes | Weighted-average diluted shares, in the model's share units | EPS note |

## Balance sheet

| Key | Required | What to put there |
|---|---|---|
| `cash` | yes | Cash and equivalents + short-term investments treated as cash |
| `receivables` | yes | Trade receivables, net |
| `inventory` | no | Inventories, net |
| `other_current_assets` | no | Every other current asset |
| `ppe_net` | yes | PP&E net + right-of-use assets (IFRS 16) |
| `intangibles_goodwill` | no | Goodwill + intangibles, net |
| `other_noncurrent_assets` | no | Deferred tax assets, investments in associates, other |
| `payables` | yes | Trade payables (suppliers) |
| `other_current_liabilities` | no | Every other current liability except debt and leases |
| `debt_short` | no | Short-term borrowings + current portion of long-term debt |
| `debt_long` | no | Long-term borrowings (bonds, bank loans) |
| `lease_liabilities` | no | Lease liabilities, current + non-current (IFRS 16) |
| `other_noncurrent_liabilities` | no | Deferred tax liabilities, provisions, pensions, other |
| `equity_parent` | yes | Equity attributable to the parent's shareholders |
| `nci_equity` | no | Non-controlling interests in equity |

## Cash-flow statement

| Key | Required | What to put there |
|---|---|---|
| `cfo` | yes | Net cash from operating activities, as reported |
| `capex` | yes | Purchases of PP&E + intangibles, positive |
| `dividends_paid` | no | Dividends paid to the parent's shareholders, positive |
| `lease_principal_paid` | no | Principal paid on lease liabilities (financing section), positive. **Required in practice if `lease_liabilities` > 0** — without it free cash flow ignores lease payments |

## Tie-out lines (used only for checks)

| Key | What to put there |
|---|---|
| `total_assets_reported` | Total assets exactly as reported |
| `net_income_reported` | Consolidated net income exactly as reported (before NCI split) |

## Revenue segments (optional)

`seg_<key>` rows, e.g. `seg_mexico`, `seg_usa`, `seg_eliminations` (negative).
Segments must add up to `revenue` in every year; declare them in
`model/drivers.yaml` under `revenue_segments` (the forecast skill does this).
```

- [ ] **Step 2: Create `skills/financials/references/extraction-guide.md`**

```markdown
# Extraction guide

## Where the documents are

| Market | Annual report / audited statements |
|---|---|
| Mexico (BMV/BIVA) | Emisnet (bmv.com.mx) and BIVA: "Reporte anual" + "Estados financieros dictaminados"; company IR site |
| Brazil (B3) | CVM (rad.cvm.gov.br): DFP (annual), ITR (quarterly); company IR site |
| Chile | CMF (cmfchile.cl): "Estados financieros" |
| Colombia | SFC / company IR site |
| Peru | SMV (smv.gob.pe) |
| US-listed | SEC EDGAR: 10-K (domestic) or 20-F (foreign private issuer) |

Students download the PDFs into `filings/`. The assistant never guesses a number
that is not in a document there.

## Which number wins

- Use the **most recent** report's comparative columns for earlier years
  (restated figures win over the originally reported ones). Note each restatement
  in `adjustments.md`.
- Use the audited annual statements, not press releases, when both exist.
- Consolidated figures only.

## Mapping rules that matter

- **Operating expenses (`opex`)**: everything between gross profit and operating
  income, netted (other operating income reduces it). Then EBIT = revenue - cogs -
  opex must equal reported operating income; if not, find the missing line.
- **Costs presented by nature** (common for telecoms, airlines, miners): there is
  no "cost of sales" line. Put costs directly tied to delivering the product or
  service in `cogs` (e.g. cost of equipment and services, fuel, raw materials) and
  the rest in `opex`; explain the split in `adjustments.md`. `cogs` must be > 0.
- **D&A**: take it from the cash-flow statement add-backs (it is already inside
  cogs/opex; the model only uses it for EBITDA, PP&E and cash flow).
- **Mexico PTU** (employee profit sharing): an operating cost — keep it in `opex`
  even if the company shows it near taxes.
- **Associates / joint ventures** (share of results): `other_financial_net`.
- **Discontinued operations**: exclude them from revenue and costs; put their
  result in `other_financial_net` and say so.
- **Argentina (IAS 29)**: figures are restated to current purchasing power;
  use the latest restated set for every year and flag it prominently.

## Leases

- **IFRS 16 (and NIF D-5)**: right-of-use assets go in `ppe_net`, lease liabilities
  in `lease_liabilities`, principal paid (financing section of the cash flow) in
  `lease_principal_paid`, lease interest inside `interest_expense`.
- **US GAAP (ASC 842)**: *finance* leases as above. *Operating* lease cost stays in
  `opex`; operating right-of-use assets go in `other_noncurrent_assets` and
  operating lease liabilities in `other_current_liabilities` /
  `other_noncurrent_liabilities` (so they are not counted as debt, consistent with
  their cost sitting in operating expenses). Say this in `adjustments.md` —
  it matters when comparing EBITDA with IFRS peers.

## Tie-outs before writing

For every year: assets = liabilities + equity (after mapping), `total_assets_reported`
and `net_income_reported` equal the reported figures, and EBIT matches reported
operating income. A difference means a line was missed — find it; never force it
into a random line.
```

- [ ] **Step 3: Create `skills/financials/references/adjustments-template.md`**

```markdown
# Accounting adjustments and mapping — <Company> (<TICKER>)

_Updated <YYYY-MM-DD> — framework: <IFRS / US GAAP / NIF> — units: <currency units>_

Read this before Q&A: a judge may ask why a number differs from the annual report.

## Sources

| Document | Years covered | File in filings/ |
|---|---|---|

## How reported lines map to the model

| Model line | Reported lines included | Years |
|---|---|---|

## Adjustments (each one in plain words)

### 1. <short title>
- **What:** 
- **Why:** 
- **Effect:** <which lines, how much, which years>
- **If a judge asks:** <one or two sentences the team can say>

## One-off items (kept in the numbers, flagged for the forecast)

The figures in `financials.csv` are reported, mapped, not normalized. These items
are unusual and the forecast should not extrapolate them:

| Year | Item | Amount | Line |
|---|---|---|---|

## Open items

- <anything tagged `unverified`, with what is needed to resolve it>

## Three questions a judge may ask about our numbers

1. **Q:** 
   **A:** 
2. **Q:** 
   **A:** 
3. **Q:** 
   **A:** 
```

- [ ] **Step 4: Create `skills/financials/SKILL.md`**

````markdown
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
````

- [ ] **Step 5: Run the structural tests for this skill**

Run: `python -m pytest -q tests -k "financials or chart_reference"`
Expected: all selected tests pass (skill exists, frontmatter, sections, length, references exist, engine call present, chart sync).

- [ ] **Step 6: Commit**

```bash
git add skills/financials/
git commit -m "feat(financials): extraction and mapping skill with chart of accounts and adjustments template"
```

---

### Task 4: `forecast` skill

**Files:**
- Create: `skills/forecast/references/drivers-guide.md`
- Create: `skills/forecast/references/drivers-template.yaml`
- Create: `skills/forecast/SKILL.md`

- [ ] **Step 1: Create `skills/forecast/references/drivers-guide.md`**

```markdown
# Drivers guide

Every forecast number in the model comes from a driver in `model/drivers.yaml`:
one value per forecast year, plus `tag`, `rationale` and `pillar`. A driver not
set is held at its last actual value (a few default to zero) and the engine warns.

## Story drivers vs mechanical drivers

- **Story drivers** (usually 3-5): the ones the thesis depends on — typically
  `revenue_growth` or segment growth, `gross_margin`, `opex_pct_revenue`, sometimes
  `capex_pct_revenue` or `payout_ratio`. **The team decides these.**
- **Mechanical drivers**: working-capital days, other current items, interest
  rates, minority share, lease payments. The assistant sets them from recent
  history and explains the choice in `rationale`.

## Every driver

| Driver | Meaning | How to anchor it | Watch out |
|---|---|---|---|
| `revenue_growth` | Revenue growth vs prior year | Market growth (industry.md) + share change + price/mix; guidance if any | Ignored when revenue segments are set |
| `gross_margin` | Gross profit / revenue | 3-5 year average; move it only with a reason (mix, pricing, input costs) | Above the historical best needs a pillar behind it |
| `opex_pct_revenue` | Operating expenses / revenue | Recent average; operating leverage if growth is strong | Cutting it without a plan is the most common judge challenge |
| `da_pct_revenue` | Total D&A / revenue | Recent average, rising if capex > D&A | Must stay consistent with capex over time |
| `amort_pct_revenue` | Amortization of intangibles / revenue (part of D&A) | Intangible amortization in the notes; 0 if not material | Keeps PP&E from absorbing intangible amortization |
| `capex_pct_revenue` | Capex / revenue | Guidance or history; maintenance capex ~ D&A, growth capex above | Capex below D&A for years means a shrinking asset base |
| `lease_principal_pct_revenue` | Lease principal paid / revenue (IFRS 16) | Recent average | Needed for lease-heavy companies (retail, restaurants, airlines) |
| `dso` | Receivable days | Recent average | Rising days eat cash |
| `dio` | Inventory days | Recent average | 0 for service companies |
| `dpo` | Payable days | Recent average | Rising payables flatter cash flow — don't assume it without evidence |
| `other_ca_pct_revenue` | Other current assets / revenue | Recent average | |
| `other_cl_pct_revenue` | Other current liabilities / revenue | Recent average | |
| `tax_rate` | Effective tax rate | Statutory rate (Mexico 30%, Brazil 34%, Chile 27%, Colombia 35%, Peru 29.5%) adjusted by recent history | Loss years distort the history |
| `interest_rate_debt` | Interest / opening total debt (incl. leases) | Recent history; debt costs note | |
| `interest_rate_cash` | Interest income / opening cash | Local short rates | |
| `payout_ratio` | Dividends / net income to shareholders | Dividend policy; recent history | |
| `nci_share` | Minority share of net income | Recent history | |
| `net_new_debt` | New long-term debt minus repayments (currency) | Debt maturity schedule in the notes; 0 if no plan | Repayments cannot exceed the balance (the engine floors debt at 0) |
| `shares_growth` | Change in diluted shares | 0 unless buybacks or issuance are announced | |
| `min_cash` | Minimum cash balance (currency) | Roughly last actual cash or a few weeks of costs | Below it, the model draws the revolver |

## Revenue by segment

When `financials.csv` has `seg_<key>` rows, set in `drivers.yaml`:

```yaml
revenue_segments:
  - {key: mexico, label: Mexico}
  - {key: usa, label: United States}
```

and one driver per segment: `seg_mexico_growth`, `seg_usa_growth` (same format as
other drivers). Segments must add up to revenue in history (include
eliminations as their own segment).

## Tags

`guidance` when management gave the number (cite where in `rationale`),
`assumption` for team or assistant judgment, `sourced` only for a figure copied
from a document (e.g. a statutory tax rate).

## Sanity rules the assistant checks before writing

- Margins beyond the historical best, or growth above market growth plus a
  credible share gain -> needs a pillar and a sentence in `rationale`.
- Capex below D&A for more than two years -> say why (asset-light shift?).
- Revenue growth converging towards long-term nominal GDP by the last year.
- Working-capital days moving more than 10 days -> evidence required.
```

- [ ] **Step 2: Create `skills/forecast/references/drivers-template.yaml`**

```yaml
# model/drivers.yaml - written by the forecast skill, read by the model engine.
# One value per forecast year. tag: guidance | assumption | sourced.
# pillar: the thesis pillar the driver supports ("1", "2", "3") or "".
forecast_years: 5
drivers:
  revenue_growth:              {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  gross_margin:                {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  opex_pct_revenue:            {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  da_pct_revenue:              {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  amort_pct_revenue:           {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  capex_pct_revenue:           {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  lease_principal_pct_revenue: {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  dso:                         {values: [0, 0, 0, 0, 0], tag: assumption, rationale: "", pillar: ""}
  dio:                         {values: [0, 0, 0, 0, 0], tag: assumption, rationale: "", pillar: ""}
  dpo:                         {values: [0, 0, 0, 0, 0], tag: assumption, rationale: "", pillar: ""}
  other_ca_pct_revenue:        {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  other_cl_pct_revenue:        {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  tax_rate:                    {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  interest_rate_debt:          {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  interest_rate_cash:          {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  payout_ratio:                {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  nci_share:                   {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  net_new_debt:                {values: [0, 0, 0, 0, 0], tag: assumption, rationale: "", pillar: ""}
  shares_growth:               {values: [0.0, 0.0, 0.0, 0.0, 0.0], tag: assumption, rationale: "", pillar: ""}
  min_cash:                    {values: [0, 0, 0, 0, 0], tag: assumption, rationale: "", pillar: ""}
# Optional, only when financials.csv has seg_<key> rows:
# revenue_segments:
#   - {key: mexico, label: Mexico}
# and add per segment:  seg_mexico_growth: {values: [...], tag: ..., rationale: ..., pillar: ...}
```

- [ ] **Step 3: Create `skills/forecast/SKILL.md`**

````markdown
---
name: forecast
description: Turn a CFA Research Challenge team's investment thesis into forecast drivers for the financial model - revenue growth or segment growth, margins, working-capital days, capex, leases, tax, payout - written to model/drivers.yaml with a rationale, tag and thesis pillar for every driver. Sets the mechanical drivers from history and coaches the team on the 3-5 assumptions that carry the story (what must be true, how far from history and guidance). Use whenever a student asks to forecast, project, "set the assumptions", "what growth should we use", build revenue by segment, or asks whether a margin or growth assumption is reasonable - even if they don't say drivers.
---

# forecast

## Purpose

Connect the story to the numbers. Mechanical assumptions are the assistant's
job; the 3-5 assumptions that carry the thesis belong to the team, and each one
must be defensible against history, guidance and the industry.

## Reads

- `data/financials.csv` — required. Missing: stop and suggest the financials skill.
- `data/adjustments.md` — one-off items to exclude from baselines.
- `research/thesis.md` — pillars. Missing: continue, leave `pillar` empty, add a
  `todo.md` item "link the forecast to the thesis".
- `research/industry.md` — market growth, share, pricing. Optional.
- `filings/` — management guidance (MD&A, earnings-call transcripts).
- `model/drivers.yaml` — if present, revise it instead of starting over.
- `references/drivers-guide.md`, `references/drivers-template.yaml`.

## Steps

1. **Baseline.** Run the engine once from the project folder (Python found as in
   init-skills) to get historical driver values:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project .`
   Read the `drivers` section of `model/model-summary.json`. If there is no
   `drivers.yaml` yet, this first workbook is the "engine-default baseline"; say so.
2. **Clean baselines.** For each driver compute the 3-5 year average and trend,
   excluding the one-off years listed in `adjustments.md`.
3. **Map pillars to drivers.** For each thesis pillar name the driver(s) that
   show it in numbers. Decide growth vs segments: use segments when
   `financials.csv` has `seg_` rows and a pillar is segment-specific.
4. **Draft every driver** per `references/drivers-guide.md`: mechanical drivers
   from recent history (say which years in `rationale`); story drivers as a
   *proposal* only. Tag `guidance` when management gave the number and cite it.
5. **Coach the story drivers** (see Coach moments) and write the team's choices.
6. **Sanity pass** with the guide's rules; flag any breach in one line each.
7. **Write `model/drivers.yaml`** from the template (all keys, `forecast_years`,
   `revenue_segments` if used) and run the engine again (same command). Read
   `status` in `model-summary.json`; fix input errors; explain any `WARN` in one
   plain sentence each.
8. **Close** with: the story drivers (history -> forecast), status, and the next
   step ("next: the model skill to review the build, or valuation").

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Which 3-5 drivers carry the story:** tie each to a pillar; drop drivers that
  no pillar needs from the discussion.
- **Each story driver's value:** show history, your proposal, guidance or
  consensus if known, and "what must be true" for the team's number.
- **Revenue vs the industry:** growth implies a market-share path — make the
  team say it out loud.

## Writes

- `model/drivers.yaml`; a new model version in `model/` (the engine never overwrites).
- Appends coach-moment answers to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — forecast — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | forecast | model/drivers.yaml | set mechanical drivers from history; team chose <story drivers>`
- `docs/context/memory.md`: `# decision: <driver> = <values> because <pillar/reason>` per story driver.
- `docs/context/todo.md`: evidence still needed for any story driver.
````

- [ ] **Step 4: Run the structural tests for this skill**

Run: `python -m pytest -q tests -k "forecast or drivers_guide"`
Expected: all selected tests pass.

- [ ] **Step 5: Commit**

```bash
git add skills/forecast/
git commit -m "feat(forecast): drivers skill with guide and template tied to the thesis"
```

---

### Task 5: `model` skill

**Files:**
- Create: `skills/model/references/reading-the-model.md`
- Create: `skills/model/references/model-summary.md`
- Create: `skills/model/SKILL.md`

- [ ] **Step 1: Create `skills/model/references/reading-the-model.md`**

```markdown
# Reading the model

## Never edit the workbook to change an assumption

Change `data/financials.csv`, `model/drivers.yaml` or `valuation/valuation.yaml`
and rebuild. Every build is a new file (`<TICKER>_model_v<N>.xlsx`); old versions
stay. If someone edits inputs in Excel, the parity checks turn to warnings
("stale — rebuild").

## Tabs

| Tab | What it shows |
|---|---|
| Cover | Status (live), how to read the model, engine warnings |
| Drivers | Every assumption: history (black) next to forecast inputs (blue on yellow), with tag, rationale, pillar |
| IS / BS / CF | Three statements; history in blue with the source in the cell comment |
| Schedules | Revenue build, PP&E and intangibles, working capital, debt and revolver, interest |
| Ratios | Margins, returns (ROE, ROIC), leverage, cash conversion cycle |
| WACC / DCF / Comps / Sensitivity / Football | Valuation (only when `valuation.yaml` exists) |
| Checks | Every integrity check by year; OK / ERROR / WARN |

Colors: blue = input or reported figure, black = formula, green = link to another tab.

## When a check is not met

| Check | Usually means | Fix | Where |
|---|---|---|---|
| Balance sheet balances (history) | A reported line was missed or double counted | Re-map the year; tie to reported totals | financials |
| Total assets / net income tie | Mapping differs from the reported total | Find the missing line | financials |
| Segments add up | Segments miss eliminations | Add `seg_eliminations` | financials |
| Balance sheet balances (forecast only) | Inherited from a history gap | Fix history first | financials |
| Cash at or above minimum / revolver not drawn | The plan burns cash: high payout, capex or working capital | Revisit story drivers or accept the borrowing and say so | forecast |
| PP&E stays at or above zero | D&A too high vs capex, or intangible amortization not split out | Set `amort_pct_revenue`, revisit capex/D&A | forecast |
| WACC above g, g below GDP, spread >= 2 pts | Terminal assumptions inconsistent | Lower g or revisit WACC inputs | valuation |
| Terminal value share, methods agree, positive values | Valuation depends on the terminal value or the two methods disagree | Revisit g, exit multiple, final-year margins | valuation |
| Excel matches Python (WARN) | Inputs were edited in Excel | Rebuild | model |
```

- [ ] **Step 2: Create `skills/model/references/model-summary.md`**

```markdown
# model/model-summary.json (read by valuation, report and pitch)

Written by every build. Numbers are in the profile's units; `null` means the
cell is blank (e.g. history of forecast-only lines) or not computable.

| Key | Content |
|---|---|
| `company`, `ticker`, `framework`, `currency`, `units` | From company-profile.yaml |
| `model_file`, `version`, `built_on` | The workbook this summary describes |
| `historical_years`, `forecast_years` | Lists of years |
| `status` | `ALL CHECKS OK`, `OK WITH WARNINGS` or `CHECKS FAILING` — the only failure signal (the engine exits 0 even when checks fail) |
| `lines` | Per year: revenue, gross_profit, ebitda, ebit, net_income_parent, eps, fcf, cash, revolver, net_debt, fcff (fcff only with valuation) |
| `ratios` | Per year: r_revenue_growth, r_gross_margin, r_ebitda_margin, r_ebit_margin, r_net_margin, r_fcf_margin, r_roe, r_roic, r_net_debt_ebitda, r_interest_cover, r_ccc |
| `drivers` | Per driver: `label`, `source` (`team` or `engine default`), `values` per year (history implied, forecast input) |
| `valuation` | Single values (only with valuation): wacc, terminal_growth, exit_multiple, ev_gordon, ev_exit, price_gordon, price_exit, share_price, upside_gordon, upside_exit, target_12m_gordon, dps_next, tv_ronic, de_market, tv_share_gordon, implied_exit_multiple, implied_g_exit, implied_g, price_comps_ev_ebitda, price_comps_pe (comps only with peers) |
| `checks` | List of `{check, year, status}`; `year` is null for single-value checks |
| `warnings` | Engine warnings (defaults used, unverified figures, missing files) |

Engine exit codes: 0 built (read `status`), 2 input error, 3 model definition
error, 4 file could not be written (close it in Excel / pause sync).
```

- [ ] **Step 3: Create `skills/model/SKILL.md`**

````markdown
---
name: model
description: Build, check and explain the CFA Research Challenge team's institutional-grade financial model - three statements, schedules, ratios, integrity checks and (when valuation inputs exist) the valuation tabs - by running the plugin's model engine on data/financials.csv, model/drivers.yaml and valuation/valuation.yaml. Reads model/model-summary.json, explains the status and every failed check in plain words, fixes mechanical problems, sends story problems back to the team, and writes a short model review. Use whenever a student asks to build, rebuild, run, update or check the model, asks what a tab or check means, asks why the model is red, or wants the Excel file - even if they don't say "model".
---

# model

## Purpose

Produce the workbook and make sure the team understands it. The engine does
the arithmetic; this skill runs it, reads the result, fixes what is mechanical
and explains the rest so any member can walk a judge through the model.

## Reads

- `data/financials.csv` — required. Missing: stop and suggest the financials skill.
- `model/drivers.yaml` — optional; without it every driver is held at its last
  actual value (say so and suggest the forecast skill).
- `valuation/valuation.yaml` — optional; without it no valuation tabs.
- `model/model-summary.json` — the result of each build.
- `references/reading-the-model.md`, `references/model-summary.md`.

## Steps

1. **Build.** Find Python as in init-skills (`python3`, `python`, then `py` on
   Windows); if Python, openpyxl or pyyaml is missing, give the install command
   from init-skills and stop. From the project folder run:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project .`
   Exit code 2: fix the listed inputs (mapping problems yourself; story drivers
   go to the team) and rerun. Exit 4: ask the team to close the file, rerun.
2. **Read** `model/model-summary.json`: `status`, every check that is not OK,
   `warnings`, and the `ratios` and `lines` sections.
3. **Resolve failed checks** with `references/reading-the-model.md`: fix
   mechanical causes directly (a mapping gap, a missing lease line), rebuild, and
   list story causes for the team with the driver involved.
4. **Review the forecast against history** (from `ratios`): revenue growth,
   EBITDA margin, ROIC, net debt / EBITDA, FCF margin. Flag any forecast year that
   breaks the historical range and name the driver responsible.
5. **Write `model/review.md`**: status, the ratio table (last 3 actual years and
   all forecast years), flags, fixes made, open questions for the team.
6. **Explain** in five lines or fewer: which file to open, status, the two most
   important things the model says, and one next step.

## Coach moments

One review checkpoint, not a decision: **"Does the model look like the business?"**
Show the three ratio trends that move most between history and forecast; ask the
team to explain the biggest change in one sentence and which pillar causes it.
If they can't, that driver goes back to the forecast skill.

## Writes

- `model/<TICKER>_model_v<N>.xlsx` and `model/model-summary.json` (via the engine)
- `model/review.md`
- Appends the checkpoint answer to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — model — does the model look like the business` + question, answer.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | model | model/<file>, model/review.md | built model v<N>; status <status>; <n> fixes`
- `docs/context/todo.md`: one item per open story issue, with the driver named.
````

- [ ] **Step 4: Run the structural tests for this skill**

Run: `python -m pytest -q tests -k "model"`
Expected: all selected tests pass.

- [ ] **Step 5: Commit**

```bash
git add skills/model/SKILL.md skills/model/references/
git commit -m "feat(model): build-and-explain skill with model reading guide and summary reference"
```

---

### Task 6: `valuation` skill

**Files:**
- Create: `skills/valuation/references/wacc-latam.md`
- Create: `skills/valuation/references/valuation-template.yaml`
- Create: `skills/valuation/references/recommendation-guide.md`
- Create: `skills/valuation/SKILL.md`

- [ ] **Step 1: Create `skills/valuation/references/wacc-latam.md`**

```markdown
# WACC and terminal value for LatAm companies

Values below are anchors to check, not data: always look up current figures and
cite the source and date in `rationale` / `valuation.md`.

## 1. Pick one currency and stay in it

The model is in the reporting currency (e.g. MXN nominal). The discount rate
must be in the same currency and in nominal terms.

- **Local route (preferred):** local 10-year government bond yield as risk-free
  (it already contains country risk and local inflation) + beta x mature-market
  ERP. No separate country risk premium (set it to 0).
- **USD route:** US 10-year Treasury + beta x ERP + country risk premium, then
  convert to local currency: `(1 + k_local) = (1 + k_usd) x (1 + inflation_local) / (1 + inflation_us)`.
  Enter the converted local rates in `valuation.yaml` and set the CRP line to 0,
  or keep the USD components and explain why the cash flows are in USD.

| Country | Local 10-year risk-free | Central-bank inflation target |
|---|---|---|
| Mexico | M Bono 10y (Banxico) | 3% |
| Brazil | NTN-F / DI curve 10y (BCB, Tesouro) | 3% |
| Chile | BCP / BTP 10y (Banco Central) | 3% |
| Colombia | TES 10y (Banco de la Republica) | 3% |
| Peru | Sovereign 10y in soles (BCRP) | 2% |

## 2. Equity risk premium and country risk

- ERP: a mature-market ERP (e.g. Damodaran's implied US ERP, updated monthly).
- Country risk premium: only on the USD route (e.g. Damodaran's country table).

## 3. Beta

Bottom-up: take peers' levered betas, unlever each
`beta_u = beta_l / (1 + (1 - tax) x D/E)` with D including leases, take the
median, and enter it as `beta_unlevered`; the model relevers it at the target D/E.

## 4. Capital structure and cost of debt

- `target_debt_to_equity`: market values, **debt including leases** (the model
  subtracts lease liabilities in net debt). Peer median or the company's own
  long-run target. The WACC tab shows the current market D/E next to it.
- `pre_tax_cost_of_debt`: yield on the company's bonds, or risk-free + a spread
  for its rating.
- `tax_rate`: statutory marginal rate (Mexico 30%, Brazil 34%, Chile 27%,
  Colombia 35%, Peru 29.5%).

## 5. Terminal value

- `growth` (g): at or below long-term **nominal** GDP growth in the model's
  currency (real growth of roughly 2-2.5% plus the inflation target). The model
  warns if WACC - g is under 2 points and fails if g is above `lt_nominal_gdp_growth`.
- `exit_ev_ebitda`: applied to final-year EBITDA. Anchor on peers' current EV /
  EBITDA, adjusted for where growth will be in the final year. The model shows the
  multiple implied by the Gordon value and warns if the two disagree by more than 2x.
- Check `tv_ronic` on the DCF tab: the return on new capital the terminal value
  assumes. Far above WACC forever needs a moat argument.
```

- [ ] **Step 2: Create `skills/valuation/references/valuation-template.yaml`**

```yaml
# valuation/valuation.yaml - written by the valuation skill, read by the model engine.
# Rates as decimals (0.095 = 9.5%). Money in the model's units (e.g. MXN millions).
share_price: 0.0                  # current price, source and date in valuation.md
price_52w_low: 0.0
price_52w_high: 0.0
mid_year: true                    # mid-year discounting convention
years_since_fiscal_year_end: 0.0  # e.g. 0.75 in late September for a December year-end
non_operating_assets: 0.0         # associates, investments, excess land (added to EV)
debt_like_items: 0.0              # pensions, provisions treated as debt (subtracted)
wacc:
  risk_free: 0.0                  # local 10y government bond (or US 10y on the USD route)
  equity_risk_premium: 0.0
  country_risk_premium: 0.0       # 0 on the local route
  beta_unlevered: 0.0             # median of peers' unlevered betas
  target_debt_to_equity: 0.0      # market values, debt incl. leases
  pre_tax_cost_of_debt: 0.0
  tax_rate: 0.0                   # statutory marginal rate
terminal:
  growth: 0.0                     # <= long-term nominal GDP growth
  exit_ev_ebitda: 0.0             # applied to final-year EBITDA
  lt_nominal_gdp_growth: 0.0
peers:                            # 4-8 peers from research/industry.md
  - name: ""
    ticker: ""
    price: 0.0
    shares: 0.0
    net_debt: 0.0                 # incl. leases + non-controlling interests
    ebitda_fwd: 0.0               # next-year EBITDA (must be > 0)
    eps_fwd: 0.0                  # next-year EPS (must be > 0)
target_price: null                # the TEAM's 12-month target; null until decided
```

- [ ] **Step 3: Create `skills/valuation/references/recommendation-guide.md`**

```markdown
# Target price and recommendation

The target price and the recommendation are the team's decision. The model
gives the evidence; the team chooses and defends.

## Evidence the model gives

- DCF value per share today (Gordon and exit multiple) and the 12-month target
  (Gordon value x (1 + cost of equity) - next dividend).
- Comps: value per share at the median peer EV / EBITDA and P / E.
- Sensitivity grid (WACC x g) and the football field (all methods, 52-week range,
  current price, the team's target once set).
- Reverse DCF: the terminal growth the market price implies.

## Choosing the target

- Pick a primary method and say why (usually the DCF for a company with visible
  cash flows; comps as the cross-check). Or weight methods and state the weights.
- If methods disagree by more than about 20%, explain why before choosing —
  judges ask.
- The target must sit inside the football-field ranges; if not, say why.

## Recommendation convention (state yours in the report)

The Challenge does not prescribe one. A common convention, measured as expected
12-month total return (price change + dividend yield):

| Expected return | Recommendation |
|---|---|
| 15% or more | BUY |
| between -10% and 15% | HOLD |
| -10% or less | SELL |

Whatever convention the team uses, the recommendation must follow the thesis
direction and the kill criteria in `research/thesis.md`, and name the catalyst
that closes the gap within 12 months.
```

- [ ] **Step 4: Create `skills/valuation/SKILL.md`**

````markdown
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
  `drivers.yaml`: run the model skill's build first and say the valuation rests on
  engine defaults until the forecast skill has run.
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
   risk-free, ERP, CRP (0 on the local route), bottom-up unlevered beta from
   peers, target D/E with leases, pre-tax cost of debt, marginal tax. Propose
   values with sources; the team confirms (Coach moments).
3. **Peers** from the industry peer set: price, shares, net debt incl. leases +
   NCI, next-year EBITDA and EPS (consensus if available, else say "trailing").
   Drop peers with non-positive EBITDA or EPS and say so.
4. **Bridge items**: `non_operating_assets`, `debt_like_items` from the notes.
5. **Terminal**: propose `growth`, `exit_ev_ebitda`, `lt_nominal_gdp_growth`.
6. **Write `valuation/valuation.yaml`** from the template with `target_price: null`
   and run from the project folder (Python found as in init-skills):
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project .`
   Read `valuation` and `checks` in `model/model-summary.json`; explain every
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
````

- [ ] **Step 5: Run the structural tests for this skill**

Run: `python -m pytest -q tests -k "valuation"`
Expected: all selected tests pass.

- [ ] **Step 6: Commit**

```bash
git add skills/valuation/
git commit -m "feat(valuation): valuation skill with LatAm WACC guide, input template and recommendation guide"
```

---

### Task 7: Integration — AGENTS template, README, manifests, evals, spec

**Files:**
- Modify: `skills/init-skills/templates/AGENTS.md` (skill table)
- Modify: `README.md` (skills table, "Coming next")
- Modify: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- Create: `evals/phase2.md`
- Modify: `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` (header status, §14)

- [ ] **Step 1: AGENTS.md template skill table**

In `skills/init-skills/templates/AGENTS.md`, replace the row
`| \`industry\` | Industry structure, competition, peers | \`research/industry.md\` |`
with these five rows (keep the rows before and after):

```markdown
| `industry` | Industry structure, competition, peers | `research/industry.md` |
| `financials` | Extract and map the statements from filings | `data/financials.csv`, `data/adjustments.md` |
| `forecast` | Set the drivers; the team picks the 3-5 that carry the story | `model/drivers.yaml` |
| `model` | Build, check and explain the Excel model | `model/<TICKER>_model_v<N>.xlsx`, `model/review.md` |
| `valuation` | WACC, DCF, comps, target price and recommendation | `valuation/valuation.yaml`, `valuation/valuation.md` |
```

and replace `Skills also trigger from plain requests ("roast our thesis", "analyze the industry").` with
`Skills also trigger from plain requests ("roast our thesis", "build the model", "what's our WACC").`

- [ ] **Step 2: README**

Replace the heading `## Skills (v0.1)` with `## Skills (v0.2)` and add these rows to its table after the `industry` row:

```markdown
| `financials` | Extracts the last 3-5 years from your filings, maps them and explains every adjustment | Nothing — but read `data/adjustments.md` before Q&A |
| `forecast` | Sets every driver from history; proposes the story drivers | The 3-5 assumptions that carry your thesis |
| `model` | Builds the Excel model (3 statements, schedules, ratios, checks, valuation) and explains it | Whether the model looks like the business |
| `valuation` | WACC, DCF, comps, sensitivity, football field | WACC calls, terminal value, target price, recommendation |
```

Replace the "Coming next" paragraph with:

```markdown
Coming next: `risks-esg`, `report`, `pitch`.

Typical order: `init-skills` -> `thesis` + `industry` -> `financials` -> `forecast`
-> `model` -> `valuation`. Each skill also works on its own.
```

- [ ] **Step 3: Manifests**

`.claude-plugin/plugin.json`: set `"version": "0.2.0"` and `"description"` to
`"Coaching skills for CFA Research Challenge teams: project setup with a LatAm specialist analyst persona, thesis coaching, industry analysis, statement extraction, forecasting, an institutional-grade Excel model and valuation. The assistant does the technical work; the team owns the story."`

`.claude-plugin/marketplace.json`: set the plugin entry's `"description"` to
`"From filings to a valued model: setup, thesis and industry coaching, financials, forecast, Excel model and valuation. The assistant does the technical work; the team owns the story."`

- [ ] **Step 4: Create `evals/phase2.md`**

```markdown
# Phase 2 manual evals

Run in a project set up with init-skills, with 3-5 annual reports of a real
BMV-listed company in `filings/`. Mark each expected behavior pass/fail.

## financials

1. Prompt: "pull the last five years of financials"
   - [ ] Lists the documents and years before extracting.
   - [ ] Writes `data/financials.csv` with a page for every sourced figure.
   - [ ] Runs the engine with `--check` and fixes input errors until `[ok]`.
   - [ ] Writes `data/adjustments.md` with three judge questions and answers.
2. Prompt (with `filings/` empty): "load the numbers"
   - [ ] Stops and lists which documents to download and where.

## forecast

1. Prompt: "set up the forecast"
   - [ ] Builds a baseline and reads historical drivers from `model-summary.json`.
   - [ ] Sets mechanical drivers itself with a rationale citing the years used.
   - [ ] Proposes the story drivers but asks the team to decide each one.
   - [ ] Writes `model/drivers.yaml` with tag, rationale and pillar for every driver.
2. Prompt: "is 12% growth reasonable?"
   - [ ] Compares with history, industry growth and guidance; asks what must be true.

## model

1. Prompt: "build the model"
   - [ ] Runs the engine, reports the file name and status.
   - [ ] Explains every failed check in plain words and names the fix.
   - [ ] Writes `model/review.md` with the ratio table and flags.
   - [ ] Asks whether the model looks like the business.
2. Prompt: "why is the model red?"
   - [ ] Reads the checks in `model-summary.json`, not the workbook.

## valuation

1. Prompt: "what's our WACC?"
   - [ ] Explains the currency route and proposes each input with a source and date.
   - [ ] Leaves the judgment calls (beta source, target D/E) to the team.
2. Prompt: "what's our target price?"
   - [ ] Shows DCF, comps and the football field; does not pick the target.
   - [ ] Writes the team's target into `valuation.yaml` and rebuilds.
   - [ ] Writes `valuation/valuation.md` with sources and the recommendation convention.
```

- [ ] **Step 5: Spec**

In `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md`: set the
header status line to `- **Status:** approved; phases 1, 2a and 2b implemented` and in
§14 add under item 2: `   (done: plans 2026-09-23-phase2a-model-engine.md, 2026-09-24-phase2b-model-skills.md)`.

- [ ] **Step 6: Run everything**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine; claude plugin validate .`
Expected: all tests pass; mypy `Success`; validation passes.

- [ ] **Step 7: Commit**

```bash
git add skills/init-skills/templates/AGENTS.md README.md .claude-plugin/ evals/phase2.md docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md
git commit -m "docs: integrate model skills into AGENTS template, README, manifests and evals"
```

After this task the branch `feat/phase2a-engine` is ready to merge into `main`
(engine and skills ship together).
