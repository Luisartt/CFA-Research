# Phase 3a — Report (language fix, risks-esg, charts, docx, report skill) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give teams everything needed for the written report before the Mexico deadline (2026-11-05): an English-only report setting, a `risks-esg` skill, chart and Word-body tools, and a `report` skill that co-writes the seven graded sections within the 10-page budget.

**Architecture:** Two small pure-Python tools in `skills/report/tools/`: `charts.py` (matplotlib PNGs from `model/model-summary.json` and `research/risks.yaml`) and `build_docx.py` (python-docx A4 body from `report/header.yaml` + `report/sections/NN-*.md` + charts; `--check` prints the page budget and uncited paragraphs). Skills call them via `${CLAUDE_PLUGIN_ROOT}/skills/report/tools/...`. The model engine's summary gains the football-field rows and the sensitivity grid so charts need no workbook.

**Tech Stack:** Python 3.10+, matplotlib, python-docx, PyYAML; pytest + mypy strict; Markdown skills.

**Spec:** `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` §8 (rules facts from the 2026-2027 Official Rules).

**Branch:** `feat/phase3a-report` (exists; spec commit is on it).

**Rules this plan must respect (Official Rules 2026-2027):** report in English; max 10 A4 pages + appendix max 10; official CFA cover attached by the team (never generated or redistributed); first-page header with company, exchange, ticker, sector/industry, rating, price + date, target + % up/down; sections Business description, Industry overview & competitive positioning, Investment summary, Valuation, Financial analysis, Investment risks, ESG; recognized citation system (Harvard default); disclose material AI reliance.

---

## File map

| File | Responsibility |
|---|---|
| `skills/init-skills/templates/{company-profile.yaml,AGENTS.md}`, `skills/init-skills/SKILL.md` | English-only report, presentation-language question, install line |
| `skills/model/engine/rcmodel/summary.py` (+ test) | `football` rows and `sensitivity` grid in the summary |
| `pyproject.toml` | new deps, test path, mypy overrides |
| `skills/report/tools/charts.py` | 5 charts -> `report/charts/*.png` |
| `skills/report/tools/build_docx.py` | A4 report body; `--check` page budget + uncited paragraphs |
| `skills/report/tools/tests/` | conftest (fixture writer), `fixtures/model-summary.json`, tests |
| `skills/risks-esg/SKILL.md` + references | `research/risks.md`, `research/risks.yaml`, `research/esg.md` |
| `skills/report/SKILL.md` + references | co-write sections, header, charts, build, AI disclosure |
| `tests/test_plugin_structure.py`, AGENTS template, README, manifests, `evals/phase3a.md` | integration |

---

### Task 1: English-only report; presentation language; install line

**Files:**
- Modify: `skills/init-skills/templates/company-profile.yaml`
- Modify: `skills/init-skills/templates/AGENTS.md`
- Modify: `skills/init-skills/SKILL.md`

- [ ] **Step 1: `company-profile.yaml` template** — in the `report:` block replace the `language` line with these two lines:

```yaml
  language: "en"                    # always English (CFA Institute Official Rules 2.6c)
  presentation_language: "{{PRESENTATION_LANGUAGE}}"   # en | es | pt, local round only; English from sub-regional up
```

- [ ] **Step 2: `AGENTS.md` template** — in `## System Persona`, replace the sentence that starts `The report is written in {{REPORT_LANGUAGE}}` (through `coach in whatever language the student writes to you in.`) and the sentence `Write files under \`research/\` and \`report/\` in {{REPORT_LANGUAGE}}, translating template headings.` with:

```markdown
The report is written in English (the CFA Institute rules require it at every
round). The local presentation is in {{PRESENTATION_LANGUAGE}}; from the
sub-regional round up it is in English. Coach in whatever language the student
writes to you in, but write every file under `research/`, `report/` and `model/`
in English, and files under `pitch/` in the presentation language.
```

- [ ] **Step 3: `init-skills/SKILL.md`**

  - Interview question 4 becomes:
    `4. Presentation language for the local round: en / es / pt. (The report is always in English; from the sub-regional round up the presentation is too.)`
  - Token table: replace the `{{REPORT_LANGUAGE}}` row with `| \`{{PRESENTATION_LANGUAGE}}\` | Q4 |`.
  - Log section: `# decision: report language = <lang>` becomes `# decision: presentation language = <lang> (report always English)`.
  - Step 2 install lines: `python-docx` becomes `python-docx matplotlib python-pptx` in both the Windows and macOS commands.

- [ ] **Step 4: Run the structural tests**

Run: `python -m pytest -q tests`
Expected: all pass (the token test confirms every template token is documented).

- [ ] **Step 5: Commit**

```bash
git add skills/init-skills/
git commit -m "fix(init-skills): report always in English; ask presentation language; install chart and deck packages"
```

---

### Task 2: Football field and sensitivity grid in `model-summary.json`

**Files:**
- Modify: `skills/model/engine/rcmodel/summary.py`
- Test: `skills/model/engine/tests/test_cli.py`

- [ ] **Step 1: Write the failing test** — append to `skills/model/engine/tests/test_cli.py`

```python
def test_summary_has_football_and_sensitivity(project: Path) -> None:
    assert main(["--project", str(project)]) == 0
    summary = json.loads((project / "model" / "model-summary.json").read_text(encoding="utf-8"))
    methods = [row["method"] for row in summary["football"]]
    assert methods[0].startswith("DCF - Gordon")
    assert "Current share price" in methods
    for row in summary["football"]:
        assert row["low"] <= row["high"]
    grid = summary["sensitivity"]
    assert len(grid["wacc"]) == 5 and len(grid["growth"]) == 5
    assert len(grid["values"]) == 5 and all(len(r) == 5 for r in grid["values"])
    assert grid["values"][2][2] == pytest.approx(summary["valuation"]["price_gordon"], rel=1e-6)


def test_summary_without_valuation_has_empty_football(tmp_path: Path) -> None:
    write_project(tmp_path, valuation=None)
    assert main(["--project", str(tmp_path)]) == 0
    summary = json.loads((tmp_path / "model" / "model-summary.json").read_text(encoding="utf-8"))
    assert summary["football"] == []
    assert summary["sensitivity"] is None
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_cli.py -k "football"`
Expected: FAIL with `KeyError: 'football'`.

- [ ] **Step 3: Implement** — in `rcmodel/summary.py` add these helpers above `build_summary`:

```python
def _football(model: Model) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line, _ in model.placed.lines:
        if line.sheet == "Football" and line.key.startswith("ff_") and line.key.endswith("_low"):
            high_key = line.key[: -len("_low")] + "_high"
            rows.append({
                "method": line.label,
                "low": _clean(model.value(line.key, None)),
                "high": _clean(model.value(high_key, None)),
            })
    return rows


def _sensitivity(model: Model) -> dict[str, Any] | None:
    if not model.has("sens_0_0"):
        return None
    size = 5
    wacc = [_clean(model.value(f"sens_w_{i}", None)) for i in range(size)]
    growth = [_clean(model.value(f"sens_g_{j}", None)) for j in range(size)]
    values: list[list[float | None]] = []
    for i in range(size):
        row: list[float | None] = []
        for j in range(size):
            w, g = model.value(f"sens_w_{i}", None), model.value(f"sens_g_{j}", None)
            row.append(_clean(model.value(f"sens_{i}_{j}", None)) if w - g >= 0.01 else None)
        values.append(row)
    return {"wacc": wacc, "growth": growth, "values": values}
```

and add two keys to the dict returned by `build_summary`, right after `"valuation": valuation,`:

```python
        "football": _football(model),
        "sensitivity": _sensitivity(model),
```

(Grid cells where WACC - g < 1% are `null`: the workbook shows them as n.m.)

- [ ] **Step 4: Update the summary reference** — in `skills/model/references/model-summary.md` add two table rows after the `valuation` row:

```markdown
| `football` | List of `{method, low, high}` value-per-share ranges (empty without valuation) |
| `sensitivity` | `{wacc: [5], growth: [5], values: [5 x 5]}` Gordon value per share; `null` cells where WACC - g < 1%; `null` without valuation |
```

- [ ] **Step 5: Run tests and mypy**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine`
Expected: all pass; mypy `Success`.

- [ ] **Step 6: Commit**

```bash
git add skills/model/engine/rcmodel/summary.py skills/model/engine/tests/test_cli.py skills/model/references/model-summary.md
git commit -m "feat(engine): football-field rows and sensitivity grid in model-summary.json"
```

---

### Task 3: Tooling for the report tools

**Files:**
- Modify: `pyproject.toml`
- Create: `skills/report/tools/tests/conftest.py`
- Create: `skills/report/tools/tests/fixtures/model-summary.json` (generated)

- [ ] **Step 1: `pyproject.toml`**

  - `dependencies` becomes `["openpyxl>=3.1", "pyyaml>=6", "matplotlib>=3.8", "python-docx>=1.1"]`.
  - `testpaths` becomes `["tests", "skills/model/engine/tests", "skills/report/tools/tests"]`.
  - In `[[tool.mypy.overrides]]` `module`, add `"docx"` and `"docx.*"`.
  - `[tool.mypy]` `mypy_path` becomes `"skills/model/engine,skills/report/tools"` (the root structural tests import `charts` and `build_docx`). Run mypy on the report tools as a separate command (`python -m mypy skills/report/tools`): checking both `tests` folders in one run collides on the module name `conftest`.

- [ ] **Step 2: Install**

Run: `python -m pip install "matplotlib>=3.8" "python-docx>=1.1"`
Expected: success.

- [ ] **Step 3: Generate the summary fixture** (deterministic; from the engine's Acme fixture)

Create a throwaway script in the scratchpad (not in the repo) that does:

```python
import shutil, sys, tempfile
from pathlib import Path
repo = Path(r"C:\Proyectos\CFA-Research")
sys.path.insert(0, str(repo / "skills/model/engine"))
sys.path.insert(0, str(repo / "skills/model/engine/tests"))
from conftest import write_project
from rcmodel.cli import main
project = write_project(Path(tempfile.mkdtemp()))
assert main(["--project", str(project)]) == 0
target = repo / "skills/report/tools/tests/fixtures/model-summary.json"
target.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(project / "model" / "model-summary.json", target)
```

Run it. Then edit the copied JSON by hand in one place only: set `"built_on"` to `"2026-09-24"` so the fixture is stable. Confirm it has non-empty `football`, a `sensitivity` grid, and `valuation.price_gordon`.

- [ ] **Step 4: Create `skills/report/tools/tests/conftest.py`** (Implemented as `report_fixtures.py`, not `conftest.py`: two conftest modules in one pytest session collide.)

```python
"""Shared fixtures for the report tools: a project folder with a model summary, risks and sections."""

from __future__ import annotations

import json
import shutil
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest
import yaml

TOOLS_DIR = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

RISKS: dict[str, Any] = {
    "risks": [
        {"id": "R1", "risk": "Wheat price spike", "category": "market", "pillar": "2",
         "probability": 3, "impact": 4, "mitigation": "Hedging 6-9 months", "priced_in": "partly"},
        {"id": "R2", "risk": "Peso depreciation", "category": "financial", "pillar": "1",
         "probability": 2, "impact": 3, "mitigation": "USD revenue from US unit", "priced_in": "yes"},
        {"id": "R3", "risk": "Front-of-pack labeling rules", "category": "regulatory", "pillar": "3",
         "probability": 4, "impact": 2, "mitigation": "Reformulation plan", "priced_in": "no"},
    ]
}

HEADER: dict[str, Any] = {
    "company": "Acme Alimentos",
    "exchange": "BMV",
    "ticker": "ACME",
    "sector": "Consumer Staples",
    "industry": "Packaged Foods",
    "recommendation": "BUY",
    "price": 25.0,
    "price_date": "2026-10-14",
    "currency": "MXN",
    "target_price": 31.0,
    "report_date": "2026-11-05",
}

SECTIONS: dict[str, str] = {
    "01-investment-summary.md": (
        "# Investment summary\n\n"
        "We rate Acme a **BUY** with a target of MXN 31.0 (Acme 2025, p. 12).\n\n"
        "- Pillar one: volume recovery\n- Pillar two: *margin* expansion\n\n"
        "![Revenue and EBITDA margin](../charts/revenue-margin.png)\n"
    ),
    "02-business-description.md": "# Business description\n\nAcme sells bread in Mexico and the US.\n",
    "05-valuation.md": (
        "# Valuation\n\n"
        "| Method | Value |\n|---|---|\n| DCF | 31.0 |\n| Comps | 29.5 |\n\n"
        "Our DCF gives 31 per share with a WACC of 12.5%.\n"
    ),
    "99-appendix.md": "# Appendix\n\nAI-use disclosure: we used an AI assistant to extract statements.\n",
}


def write_report_project(root: Path, summary: bool = True, risks: Mapping[str, Any] | None = RISKS,
                         header: Mapping[str, Any] | None = HEADER,
                         sections: Mapping[str, str] | None = SECTIONS) -> Path:
    for folder in ("model", "research", "report/sections", "report/charts"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    if summary:
        shutil.copy(FIXTURES / "model-summary.json", root / "model" / "model-summary.json")
    if risks is not None:
        (root / "research" / "risks.yaml").write_text(yaml.safe_dump(dict(risks), sort_keys=False), encoding="utf-8")
    if header is not None:
        (root / "report" / "header.yaml").write_text(yaml.safe_dump(dict(header), sort_keys=False), encoding="utf-8")
    for name, text in (sections or {}).items():
        (root / "report" / "sections" / name).write_text(text, encoding="utf-8")
    return root


def load_fixture_summary() -> dict[str, Any]:
    data: dict[str, Any] = json.loads((FIXTURES / "model-summary.json").read_text(encoding="utf-8"))
    return data


@pytest.fixture
def report_project(tmp_path: Path) -> Path:
    return write_report_project(tmp_path)
```

- [ ] **Step 5: Verify collection**

Run: `python -m pytest -q skills/report/tools/tests`
Expected: `no tests ran` (collection succeeds, exit code 5 is fine here).

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml skills/report/tools/tests/
git commit -m "test(report): tooling, summary fixture and report project fixture"
```

---

### Task 4: Charts (`charts.py`)

**Files:**
- Create: `skills/report/tools/charts.py`
- Test: `skills/report/tools/tests/test_charts.py`

- [ ] **Step 1: Write the failing tests** — `skills/report/tools/tests/test_charts.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

import matplotlib.image as mpimg
import pytest

from charts import CHARTS, ChartError, load_risks, main
from conftest import RISKS, write_report_project

EXPECTED = {"revenue-margin", "free-cash-flow", "football-field", "sensitivity", "risk-matrix"}


def test_all_charts_are_drawn(report_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(report_project)]) == 0
    written = {p.stem for p in (report_project / "report" / "charts").glob("*.png")}
    assert written == EXPECTED
    out = capsys.readouterr().out
    assert out.isascii() and "[ok] report/charts/football-field.png" in out


def test_chart_sizes_fit_the_page(report_project: Path) -> None:
    main(["--project", str(report_project)])
    for name in EXPECTED:
        height, width = mpimg.imread(report_project / "report" / "charts" / f"{name}.png").shape[:2]
        assert 500 <= width <= 1400, (name, width)
        assert height < width, name


def test_registry_names_match_files() -> None:
    assert {chart.name for chart in CHARTS} == EXPECTED


def test_missing_summary_still_draws_risks(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_report_project(tmp_path, summary=False)
    assert main(["--project", str(project)]) == 0
    written = {p.stem for p in (project / "report" / "charts").glob("*.png")}
    assert written == {"risk-matrix"}
    assert "[skip] revenue-margin" in capsys.readouterr().out


def test_nothing_to_draw_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_report_project(tmp_path, summary=False, risks=None)
    assert main(["--project", str(project)]) == 2
    assert "model-summary.json" in capsys.readouterr().out


def test_invalid_risk_scores_are_rejected(tmp_path: Path) -> None:
    risks = copy.deepcopy(RISKS)
    risks["risks"][0]["probability"] = 7
    project = write_report_project(tmp_path, risks=risks)
    with pytest.raises(ChartError, match="R1"):
        load_risks(project / "research" / "risks.yaml")


def test_summary_without_valuation_skips_valuation_charts(report_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    import json

    path = report_project / "model" / "model-summary.json"
    summary = json.loads(path.read_text(encoding="utf-8"))
    summary["football"], summary["sensitivity"], summary["valuation"] = [], None, {}
    path.write_text(json.dumps(summary), encoding="utf-8")
    assert main(["--project", str(report_project)]) == 0
    out = capsys.readouterr().out
    assert "[skip] football-field" in out and "[skip] sensitivity" in out
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest -q skills/report/tools/tests/test_charts.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'charts'`.

- [ ] **Step 3: Implement `skills/report/tools/charts.py`**

```python
"""Charts for the report and the deck.

Reads model/model-summary.json (written by the model engine) and
research/risks.yaml (written by the risks-esg skill); writes PNGs to
report/charts/. Console output is ASCII only.

Usage: python charts.py --project <team folder>
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import yaml  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

NAVY = "#1F4E79"
LIGHT = "#9DC3E6"
ACCENT = "#C55A11"
GREY = "#7F7F7F"
FULL_WIDTH_IN = 6.3
HALF_WIDTH_IN = 3.2
DPI = 200
SOURCE_NOTE = "A = actual, E = estimate. Source: team model."
EXIT_OK = 0
EXIT_NOTHING = 2

Summary = dict[str, Any]


class ChartError(Exception):
    """An input file is missing or invalid."""


@dataclass(frozen=True)
class Chart:
    name: str
    needs: str  # "summary", "valuation" or "risks"
    draw: Callable[[Summary, list[dict[str, Any]], Path], None]


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _year_labels(summary: Summary) -> list[str]:
    hist = [f"{y}A" for y in summary["historical_years"]]
    fcst = [f"{y}E" for y in summary["forecast_years"]]
    return hist + fcst


def _series(summary: Summary, section: str, key: str) -> list[float]:
    values = summary.get(section, {}).get(key, {})
    years = [str(y) for y in summary["historical_years"] + summary["forecast_years"]]
    return [math.nan if values.get(y) is None else float(values[y]) for y in years]


def _style(ax: Axes) -> None:
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.tick_params(labelsize=7)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.5)
    ax.set_axisbelow(True)


def _save(fig: Figure, path: Path, note: str = SOURCE_NOTE) -> None:
    fig.text(0.01, 0.01, note, fontsize=6, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=DPI)
    plt.close(fig)


def revenue_margin(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    labels = _year_labels(summary)
    h = len(summary["historical_years"])
    revenue = _series(summary, "lines", "revenue")
    margin = [m * 100 for m in _series(summary, "ratios", "r_ebitda_margin")]
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.3))
    ax.bar(labels, revenue, color=[NAVY if i < h else LIGHT for i in range(len(labels))])
    ax.set_ylabel(f"Revenue ({summary['currency']} {summary['units']})", fontsize=7)
    twin = ax.twinx()
    twin.plot(labels, margin, color=ACCENT, marker="o", linewidth=1.2, markersize=3)
    twin.set_ylabel("EBITDA margin (%)", fontsize=7)
    twin.tick_params(labelsize=7)
    ax.set_title("Revenue and EBITDA margin", fontsize=8)
    _style(ax)
    ax.tick_params(axis="x", rotation=45)
    _save(fig, path)


def free_cash_flow(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    labels = _year_labels(summary)
    fcf = _series(summary, "lines", "fcf")
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.3))
    ax.bar(labels, fcf, color=[ACCENT if (not math.isnan(v) and v < 0) else NAVY for v in fcf])
    ax.axhline(0, color=GREY, linewidth=0.6)
    ax.set_ylabel(f"{summary['currency']} {summary['units']}", fontsize=7)
    ax.set_title("Free cash flow (CFO - capex - lease principal)", fontsize=8)
    _style(ax)
    ax.tick_params(axis="x", rotation=45)
    _save(fig, path)


def football_field(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    rows = [r for r in summary["football"] if r["low"] is not None and r["high"] is not None]
    fig, ax = plt.subplots(figsize=(FULL_WIDTH_IN, 0.45 * len(rows) + 1.0))
    labels = [r["method"] for r in rows]
    for i, row in enumerate(rows):
        width = row["high"] - row["low"]
        if width > 0:
            ax.barh(i, width, left=row["low"], color=LIGHT, edgecolor=NAVY, height=0.5)
        else:
            ax.plot([row["low"]], [i], marker="D", color=NAVY)
    price = summary.get("valuation", {}).get("share_price")
    if price is not None:
        ax.axvline(price, color=ACCENT, linestyle="--", linewidth=1)
        ax.text(price, len(rows) - 0.4, f" price {price:,.2f}", color=ACCENT, fontsize=7)
    ax.set_yticks(range(len(rows)), labels=labels, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel(f"Value per share ({summary['currency']})", fontsize=7)
    ax.set_title("Valuation summary (football field)", fontsize=8)
    _style(ax)
    ax.grid(axis="x", color="#D9D9D9", linewidth=0.5)
    _save(fig, path, "Source: team model (DCF, comps, market data).")


def sensitivity(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    grid = summary["sensitivity"]
    values = [[math.nan if v is None else float(v) for v in row] for row in grid["values"]]
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.6))
    ax.imshow(values, cmap="Blues", aspect="auto")
    for i, row in enumerate(values):
        for j, v in enumerate(row):
            ax.text(j, i, "n.m." if math.isnan(v) else f"{v:,.1f}", ha="center", va="center", fontsize=6,
                    color="black")
    ax.set_xticks(range(len(grid["growth"])), labels=[f"{g * 100:.1f}%" for g in grid["growth"]], fontsize=7)
    ax.set_yticks(range(len(grid["wacc"])), labels=[f"{w * 100:.1f}%" for w in grid["wacc"]], fontsize=7)
    ax.set_xlabel("Terminal growth", fontsize=7)
    ax.set_ylabel("WACC", fontsize=7)
    ax.set_title("DCF value per share: sensitivity", fontsize=8)
    _save(fig, path, "Source: team model (Gordon growth DCF).")


def risk_matrix(_: Summary, risks: list[dict[str, Any]], path: Path) -> None:
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.8))
    for x in range(1, 6):
        for y in range(1, 6):
            score = x * y
            color = "#E2F0D9" if score <= 6 else ("#FFF2CC" if score <= 12 else "#F8CBAD")
            ax.add_patch(plt.Rectangle((x - 0.5, y - 0.5), 1, 1, color=color, zorder=0))
    for risk in risks:
        ax.scatter(risk["probability"], risk["impact"], color=NAVY, s=30, zorder=2)
        ax.annotate(risk["id"], (risk["probability"], risk["impact"]), textcoords="offset points",
                    xytext=(4, 4), fontsize=7)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.tick_params(labelsize=7)
    ax.set_xlabel("Probability (1 = low, 5 = high)", fontsize=7)
    ax.set_ylabel("Impact on value (1-5)", fontsize=7)
    ax.set_title("Investment risk matrix", fontsize=8)
    _save(fig, path, "Source: team analysis (research/risks.md).")


CHARTS: tuple[Chart, ...] = (
    Chart("revenue-margin", "summary", revenue_margin),
    Chart("free-cash-flow", "summary", free_cash_flow),
    Chart("football-field", "valuation", football_field),
    Chart("sensitivity", "valuation", sensitivity),
    Chart("risk-matrix", "risks", risk_matrix),
)


def load_summary(path: Path) -> Summary | None:
    if not path.is_file():
        return None
    try:
        data: Summary = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ChartError(f"{path.name} is not valid JSON: {exc}") from None
    return data


def load_risks(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except (yaml.YAMLError, UnicodeDecodeError) as exc:
        raise ChartError(f"{path.name} is not valid YAML: {exc}") from None
    risks = doc.get("risks") if isinstance(doc, dict) else None
    if not isinstance(risks, list):
        raise ChartError(f"{path.name} needs a 'risks:' list")
    problems: list[str] = []
    for n, risk in enumerate(risks, start=1):
        rid = risk.get("id", f"#{n}") if isinstance(risk, dict) else f"#{n}"
        if not isinstance(risk, dict):
            problems.append(f"risk {rid} must be a mapping")
            continue
        for field in ("probability", "impact"):
            value = risk.get(field)
            if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
                problems.append(f"risk {rid}: {field} must be a whole number from 1 to 5")
    if problems:
        raise ChartError("; ".join(problems))
    return risks


def _available(chart: Chart, summary: Summary | None, risks: Sequence[dict[str, Any]]) -> str:
    """Empty string if the chart can be drawn, else the reason it is skipped."""
    if chart.needs == "risks":
        return "" if risks else "research/risks.yaml not found or empty (run the risks-esg skill)"
    if summary is None:
        return "model/model-summary.json not found (run the model skill)"
    if chart.needs == "valuation":
        if chart.name == "football-field" and not summary.get("football"):
            return "no valuation in the model (run the valuation skill)"
        if chart.name == "sensitivity" and not summary.get("sensitivity"):
            return "no valuation in the model (run the valuation skill)"
    return ""


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Draw the report charts into report/charts/.")
    parser.add_argument("--project", default=".", help="Team project folder")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    try:
        summary = load_summary(project / "model" / "model-summary.json")
        risks = load_risks(project / "research" / "risks.yaml")
    except ChartError as exc:
        print("[x] " + ascii_safe(str(exc)))
        return EXIT_NOTHING
    out_dir = project / "report" / "charts"
    out_dir.mkdir(parents=True, exist_ok=True)
    drawn = 0
    for chart in CHARTS:
        reason = _available(chart, summary, risks)
        if reason:
            print(f"[skip] {chart.name}: {ascii_safe(reason)}")
            continue
        chart.draw(summary or {}, list(risks), out_dir / f"{chart.name}.png")
        print(f"[ok] report/charts/{chart.name}.png")
        drawn += 1
    if drawn == 0:
        print("[x] Nothing to draw: build the model (model-summary.json) or write research/risks.yaml first.")
        return EXIT_NOTHING
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest -q skills/report/tools/tests/test_charts.py`
Expected: `7 passed`

- [ ] **Step 5: mypy and commit**

Run: `python -m mypy skills/report/tools`
Expected: `Success` (fix typing-only issues if any; e.g. matplotlib stubs are bundled).

```bash
git add skills/report/tools/charts.py skills/report/tools/tests/test_charts.py
git commit -m "feat(report): chart builder for revenue, FCF, football field, sensitivity and risk matrix"
```

---

### Task 5: Report body builder (`build_docx.py`)

**Files:**
- Create: `skills/report/tools/build_docx.py`
- Test: `skills/report/tools/tests/test_build_docx.py`

- [ ] **Step 1: Write the failing tests** — `skills/report/tools/tests/test_build_docx.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

import pytest
from docx import Document
from docx.shared import Mm

from report_fixtures import HEADER, SECTIONS, report_project, write_report_project  # noqa: F401
from build_docx import BUDGET_PAGES, main, parse_markdown
from charts import main as draw_charts


def _build(project: Path) -> Path:
    draw_charts(["--project", str(project)])
    assert main(["--project", str(project)]) == 0
    return project / "report" / "ACME_report_v1.docx"


def test_builds_a4_body_with_header_sections_and_figures(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    section = doc.sections[0]
    assert abs(section.page_width - Mm(210)) < Mm(1) and abs(section.page_height - Mm(297)) < Mm(1)
    text = "\n".join(p.text for p in doc.paragraphs)
    for heading in ("Investment summary", "Business description", "Valuation", "Appendix"):
        assert heading in text
    assert "Figure 1: Revenue and EBITDA margin" in text
    assert len(doc.inline_shapes) == 1
    usable = section.page_width - section.left_margin - section.right_margin
    assert all(shape.width <= usable for shape in doc.inline_shapes)


def test_header_block_has_the_required_fields(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    header_text = " ".join(cell.text for row in doc.tables[0].rows for cell in row.cells)
    for expected in ("Acme Alimentos", "BMV: ACME", "Consumer Staples / Packaged Foods", "BUY",
                     "MXN 25.00 (2026-10-14)", "MXN 31.00 (+24.0%)"):
        assert expected in header_text, expected


def test_markdown_tables_and_inline_formatting(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    assert len(doc.tables) == 2  # header block + the valuation table
    assert doc.tables[1].rows[0].cells[0].text == "Method"
    bold_runs = [r.text for p in doc.paragraphs for r in p.runs if r.bold]
    assert "BUY" in bold_runs


def test_appendix_starts_on_a_new_page(report_project: Path) -> None:
    doc = Document(str(_build(report_project)))
    xml = doc.element.body.xml
    assert xml.index('w:type="page"') < xml.index(">Appendix<")


def test_versions_are_never_overwritten(report_project: Path) -> None:
    _build(report_project)
    assert main(["--project", str(report_project)]) == 0
    assert (report_project / "report" / "ACME_report_v1.docx").is_file()
    assert (report_project / "report" / "ACME_report_v2.docx").is_file()


def test_check_mode_reports_budget_and_uncited(report_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(report_project), "--check"]) == 0
    out = capsys.readouterr().out
    assert out.isascii()
    assert "investment-summary" in out and "pages" in out
    assert "uncited" in out and "Our DCF gives 31 per share" in out
    assert not list((report_project / "report").glob("*.docx"))


def test_check_mode_flags_over_budget(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    sections = copy.deepcopy(SECTIONS)
    sections["02-business-description.md"] = "# Business description\n\n" + ("word " * 600) + "\n"
    project = write_report_project(tmp_path, sections=sections)
    main(["--project", str(project), "--check"])
    assert "[over] business-description" in capsys.readouterr().out


def test_missing_header_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_report_project(tmp_path, header=None)
    assert main(["--project", str(project)]) == 2
    assert "header.yaml" in capsys.readouterr().out


def test_bad_recommendation_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    header = dict(HEADER)
    header["recommendation"] = "STRONG BUY"
    project = write_report_project(tmp_path, header=header)
    assert main(["--project", str(project)]) == 2
    assert "recommendation" in capsys.readouterr().out


def test_parser_blocks() -> None:
    blocks = parse_markdown("# Title\n\nPara one\nstill one.\n\n- a\n- b\n\n1. x\n\n![Cap](c.png)\n\n| A | B |\n|---|---|\n| 1 | 2 |\n")
    assert [b.kind for b in blocks] == ["heading", "paragraph", "bullet", "bullet", "number", "image", "table"]
    assert blocks[1].text == "Para one still one."
    assert blocks[6].rows == [["A", "B"], ["1", "2"]]


def test_budget_covers_the_seven_graded_sections() -> None:
    assert set(BUDGET_PAGES) == {"investment-summary", "business-description", "industry", "financial-analysis",
                                 "valuation", "risks", "esg"}
    assert sum(BUDGET_PAGES.values()) == 10
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest -q skills/report/tools/tests/test_build_docx.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'build_docx'`.

- [ ] **Step 3: Implement `skills/report/tools/build_docx.py`**

```python
"""Assemble the written report body as an A4 .docx.

Inputs (team project folder):
  report/header.yaml            first-page header fields
  report/sections/NN-slug.md    one file per section, sorted by NN; 99-appendix* starts the appendix
  report/charts/*.png           images referenced from the sections with ![caption](../charts/x.png)

The official CFA Institute cover page is NOT generated; the team puts it in front.
--check prints the page budget per section and paragraphs with numbers but no citation,
without writing a file. Console output is ASCII only.

Usage: python build_docx.py --project <team folder> [--check]
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_IO_ERROR = 4
PAGE_LIMIT = 10
WORDS_PER_PAGE = 500
PAGES_PER_FIGURE = 0.3
BUDGET_PAGES: dict[str, float] = {
    "investment-summary": 1.5,
    "business-description": 0.5,
    "industry": 1.0,
    "financial-analysis": 2.0,
    "valuation": 2.0,
    "risks": 1.5,
    "esg": 1.5,
}
RATINGS = {"BUY": "00B050", "HOLD": "BF8F00", "SELL": "C00000"}
HEADER_FIELDS = ("company", "exchange", "ticker", "sector", "industry", "recommendation", "price",
                 "price_date", "currency", "target_price", "report_date")
FONT = "Arial"
NAVY = RGBColor(0x1F, 0x4E, 0x79)
MARGIN = Mm(20)
CITATION = re.compile(r"\([^()]*\b(19|20)\d{2}\b[^()]*\)|Source:", re.IGNORECASE)
HAS_NUMBER = re.compile(r"\d")
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


class ReportInputError(Exception):
    def __init__(self, messages: list[str]) -> None:
        super().__init__("; ".join(messages))
        self.messages = messages


@dataclass
class Block:
    kind: str  # heading, paragraph, bullet, number, image, table
    text: str = ""
    level: int = 1
    path: str = ""
    rows: list[list[str]] = field(default_factory=list)


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def parse_markdown(source: str) -> list[Block]:
    """A small Markdown subset: #/##/### headings, paragraphs, - and 1. lists, images, pipe tables."""
    blocks: list[Block] = []
    paragraph: list[str] = []
    table: list[list[str]] = []

    def flush() -> None:
        if paragraph:
            blocks.append(Block("paragraph", " ".join(paragraph)))
            paragraph.clear()
        if table:
            blocks.append(Block("table", rows=[row[:] for row in table]))
            table.clear()

    for raw in source.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("|") and line.endswith("|"):
            if paragraph:
                flush()
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                table.append(cells)
            continue
        if table:
            flush()
        heading = re.match(r"^(#{1,3})\s+(.*)$", line)
        image = re.match(r"^!\[(.*)\]\((.+)\)$", line)
        bullet = re.match(r"^[-*]\s+(.*)$", line)
        number = re.match(r"^\d+\.\s+(.*)$", line)
        if heading:
            flush()
            blocks.append(Block("heading", heading.group(2), level=len(heading.group(1))))
        elif image:
            flush()
            blocks.append(Block("image", image.group(1), path=image.group(2)))
        elif bullet:
            flush()
            blocks.append(Block("bullet", bullet.group(1)))
        elif number:
            flush()
            blocks.append(Block("number", number.group(1)))
        else:
            paragraph.append(line)
    flush()
    return blocks


def _slug(path: Path) -> str:
    return re.sub(r"^\d+-", "", path.stem)


def load_header(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ReportInputError(["report/header.yaml not found: the report skill writes it (company, rating, price, target)"])
    doc = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    if not isinstance(doc, dict):
        raise ReportInputError(["report/header.yaml must be a mapping (key: value)"])
    problems = [f"report/header.yaml: {name} is missing" for name in HEADER_FIELDS if doc.get(name) in (None, "")]
    rating = str(doc.get("recommendation", "")).upper()
    if rating and rating not in RATINGS:
        problems.append("report/header.yaml: recommendation must be BUY, HOLD or SELL")
    for name in ("price", "target_price"):
        value = doc.get(name)
        if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0):
            problems.append(f"report/header.yaml: {name} must be a positive number")
    if problems:
        raise ReportInputError(problems)
    doc["recommendation"] = rating
    return doc


def load_sections(folder: Path) -> list[tuple[Path, list[Block]]]:
    files = sorted(folder.glob("*.md")) if folder.is_dir() else []
    if not files:
        raise ReportInputError(["report/sections/ has no .md files: write the sections first"])
    return [(path, parse_markdown(path.read_text(encoding="utf-8-sig"))) for path in files]


def _words(blocks: Sequence[Block]) -> int:
    count = 0
    for block in blocks:
        if block.kind == "table":
            count += sum(len(cell.split()) for row in block.rows for cell in row)
        elif block.kind != "image":
            count += len(block.text.split())
    return count


def budget_rows(sections: Sequence[tuple[Path, list[Block]]]) -> list[tuple[str, int, int, float, float | None]]:
    rows: list[tuple[str, int, int, float, float | None]] = []
    for path, blocks in sections:
        slug = _slug(path)
        if slug.startswith("appendix"):
            continue
        figures = sum(1 for b in blocks if b.kind == "image")
        pages = _words(blocks) / WORDS_PER_PAGE + figures * PAGES_PER_FIGURE
        rows.append((slug, _words(blocks), figures, round(pages, 2), BUDGET_PAGES.get(slug)))
    return rows


def uncited(sections: Sequence[tuple[Path, list[Block]]]) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for path, blocks in sections:
        for block in blocks:
            if block.kind in ("paragraph", "bullet", "number") and HAS_NUMBER.search(block.text) \
                    and not CITATION.search(block.text):
                found.append((_slug(path), block.text[:70]))
    return found


def _add_runs(paragraph: Any, text: str, size: float = 10) -> None:
    for part in INLINE.split(text):
        if not part:
            continue
        bold = part.startswith("**") and part.endswith("**")
        italic = not bold and part.startswith("*") and part.endswith("*")
        run = paragraph.add_run(part.strip("*") if (bold or italic) else part)
        run.bold, run.italic = bold, italic
        run.font.name, run.font.size = FONT, Pt(size)


def _shade(cell: Any, hex_color: str) -> None:
    shading = OxmlElement("w:shd")
    shading.set(qn("w:val"), "clear")
    shading.set(qn("w:color"), "auto")
    shading.set(qn("w:fill"), hex_color)
    cell._tc.get_or_add_tcPr().append(shading)


def _header_block(doc: Any, header: dict[str, Any]) -> None:
    upside = header["target_price"] / header["price"] - 1
    rows = (
        ("Company", str(header["company"])),
        ("Exchange: ticker", f"{header['exchange']}: {header['ticker']}"),
        ("Sector / industry", f"{header['sector']} / {header['industry']}"),
        ("Recommendation", header["recommendation"]),
        ("Price (date)", f"{header['currency']} {header['price']:,.2f} ({header['price_date']})"),
        ("Target price (upside)", f"{header['currency']} {header['target_price']:,.2f} ({upside:+.1%})"),
        ("Report date", str(header["report_date"])),
    )
    table = doc.add_table(rows=len(rows), cols=2)
    for (label, value), row in zip(rows, table.rows):
        _shade(row.cells[0], "DDEBF7")
        _add_runs(row.cells[0].paragraphs[0], f"**{label}**", 9)
        _add_runs(row.cells[1].paragraphs[0], f"**{value}**" if label == "Recommendation" else value, 9)
        if label == "Recommendation":
            row.cells[1].paragraphs[0].runs[0].font.color.rgb = RGBColor.from_string(RATINGS[value])
    doc.add_paragraph()


def _table(doc: Any, rows: list[list[str]]) -> None:
    width = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    for i, cells in enumerate(rows):
        for j in range(width):
            text = cells[j] if j < len(cells) else ""
            paragraph = table.rows[i].cells[j].paragraphs[0]
            _add_runs(paragraph, f"**{text}**" if i == 0 and text else text, 8)
            if i == 0:
                _shade(table.rows[i].cells[j], "DDEBF7")
    doc.add_paragraph()


def build(project: Path, header: dict[str, Any], sections: Sequence[tuple[Path, list[Block]]]) -> Path:
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Mm(210), Mm(297)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(section, side, MARGIN)
    usable = section.page_width - section.left_margin - section.right_margin
    doc.styles["Normal"].font.name = FONT
    doc.styles["Normal"].font.size = Pt(10)
    _header_block(doc, header)
    figure = 0
    for path, blocks in sections:
        if _slug(path).startswith("appendix"):
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        for block in blocks:
            if block.kind == "heading":
                heading = doc.add_heading(level=min(block.level, 3))
                _add_runs(heading, block.text, 14 if block.level == 1 else 11)
                for run in heading.runs:
                    run.font.color.rgb = NAVY
            elif block.kind == "paragraph":
                _add_runs(doc.add_paragraph(), block.text)
            elif block.kind in ("bullet", "number"):
                style = "List Bullet" if block.kind == "bullet" else "List Number"
                _add_runs(doc.add_paragraph(style=style), block.text)
            elif block.kind == "table":
                _table(doc, block.rows)
            elif block.kind == "image":
                image = (path.parent / block.path).resolve()
                if not image.is_file():
                    raise ReportInputError([f"{path.name}: image not found: {block.path} (run charts.py first)"])
                shape = doc.add_picture(str(image))
                if shape.width > usable:
                    shape.height = int(shape.height * usable / shape.width)
                    shape.width = usable
                figure += 1
                caption = doc.add_paragraph()
                _add_runs(caption, f"*Figure {figure}: {block.text}*", 8)
    out_dir = project / "report"
    ticker = re.sub(r"[^A-Za-z0-9]+", "-", str(header["ticker"])).strip("-") or "REPORT"
    pattern = re.compile(rf"^{re.escape(ticker)}_report_v(\d+)\.docx$")
    versions = [int(m.group(1)) for p in out_dir.glob("*.docx") if (m := pattern.match(p.name))]
    target = out_dir / f"{ticker}_report_v{max(versions, default=0) + 1}.docx"
    doc.save(str(target))
    return target


def _print_check(sections: Sequence[tuple[Path, list[Block]]]) -> None:
    rows = budget_rows(sections)
    print("section                 words  figures  pages  budget")
    for slug, words, figures, pages, budget in rows:
        flag = "[over]" if budget is not None and pages > budget * 1.1 else "      "
        budget_text = "-" if budget is None else f"{budget:.1f}"
        print(f"{flag} {ascii_safe(slug):<18} {words:>5}  {figures:>7}  {pages:>5.1f}  {budget_text:>6}")
    total = sum(r[3] for r in rows)
    print(f"total estimated pages: {total:.1f} of {PAGE_LIMIT} (appendix not counted)")
    if total > PAGE_LIMIT:
        print("[x] over the 10-page limit: cut before building")
    missing = [s for s in BUDGET_PAGES if s not in {r[0] for r in rows}]
    if missing:
        print("[warn] sections not written yet: " + ", ".join(missing))
    flagged = uncited(sections)
    print(f"uncited paragraphs with numbers: {len(flagged)}")
    for slug, text in flagged:
        print(f"  - [{ascii_safe(slug)}] {ascii_safe(text)}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the report body (A4 .docx) or check the page budget.")
    parser.add_argument("--project", default=".", help="Team project folder")
    parser.add_argument("--check", action="store_true", help="Print the page budget and uncited paragraphs only")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    try:
        sections = load_sections(project / "report" / "sections")
        if args.check:
            _print_check(sections)
            return EXIT_OK
        header = load_header(project / "report" / "header.yaml")
        target = build(project, header, sections)
    except ReportInputError as exc:
        print("[x] Cannot build the report. Fix these first:")
        for message in exc.messages:
            print("  - " + ascii_safe(message))
        return EXIT_INPUT_ERROR
    except OSError as exc:
        print(f"[x] Could not write the report: {ascii_safe(exc.strerror or str(exc))}. Close it in Word and run again.")
        return EXIT_IO_ERROR
    print(f"[ok] report -> report/{ascii_safe(target.name)}")
    print("Next: put the official CFA Institute cover page in front, then check the layout in Word.")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest -q skills/report/tools/tests/test_build_docx.py`
Expected: `11 passed`. If `test_appendix_starts_on_a_new_page` fails only because of how python-docx serializes the heading text, adjust the TEST's search string to the actual XML (not the builder).

- [ ] **Step 5: mypy and commit**

Run: `python -m mypy skills/report/tools`
Expected: `Success`.

```bash
git add skills/report/tools/build_docx.py skills/report/tools/tests/test_build_docx.py
git commit -m "feat(report): A4 report body builder with header block, figures, tables and page-budget check"
```

---

### Task 6: `risks-esg` skill

**Files:**
- Create: `skills/risks-esg/references/risk-framework.md`
- Create: `skills/risks-esg/references/risks-template.yaml`
- Create: `skills/risks-esg/references/esg-materiality-latam.md`
- Create: `skills/risks-esg/references/esg-template.md`
- Create: `skills/risks-esg/SKILL.md`

- [ ] **Step 1: Create `skills/risks-esg/references/risk-framework.md`**

```markdown
# Risk framework

Investment risks are worth 15 of 100 report points. Judges reward specific,
quantified risks tied to the thesis, and punish generic lists ("FX risk",
"competition").

## A good risk statement

cause -> effect on the business -> which model driver moves -> effect on value.
Example: "A 20% wheat price spike (cause) squeezes gross margin by ~150 bp
before prices adjust (effect; driver `gross_margin`), cutting our DCF value by
about 8% (value)."

## Scales (used in research/risks.yaml and the risk matrix)

| Score | Probability (next 12-24 months) | Impact on value per share |
|---|---|---|
| 1 | Rare, under 10% | Under 2% |
| 2 | Unlikely, 10-25% | 2-5% |
| 3 | Possible, 25-50% | 5-10% |
| 4 | Likely, 50-75% | 10-20% |
| 5 | Almost certain, over 75% | Over 20% |

## Categories

market (demand, prices, competition), operational (supply chain, execution,
capacity), financial (FX, rates, leverage, refinancing), regulatory (tax,
labeling, concessions, antitrust), ESG (environmental, social), governance
(controlling shareholder, related parties, succession).

## What to write

- 4-6 key risks in the body, each linked to a thesis pillar; the rest in a
  table in the appendix.
- For each: mitigation (what the company does) and whether it is priced in
  (already in the market price, in our forecast, or neither).
- One downside scenario: the risks that matter most, hitting together, with
  the value per share it implies (the valuation skill can run it).
- Every risk that could break a thesis pillar should match a kill criterion in
  `research/thesis.md`.
```

- [ ] **Step 2: Create `skills/risks-esg/references/risks-template.yaml`**

```yaml
# research/risks.yaml - written by the risks-esg skill, read by report/tools/charts.py.
# probability and impact: whole numbers 1-5 (see risk-framework.md).
risks:
  - id: R1
    risk: ""                 # one line: cause -> effect
    category: market         # market | operational | financial | regulatory | ESG | governance
    pillar: "1"              # thesis pillar it threatens
    driver: gross_margin     # model driver that moves
    probability: 3
    impact: 3
    mitigation: ""           # what the company does about it
    priced_in: "no"          # yes | partly | no, with one line of why
```

- [ ] **Step 3: Create `skills/risks-esg/references/esg-materiality-latam.md`**

```markdown
# ESG for LatAm equity research

ESG is worth 15 of 100 report points and 10 of 100 presentation points.
Judges want the few issues that are *material to value* for this industry,
evidence of how the company performs on them, and a link to the valuation —
not a generic sustainability summary.

## 1. Materiality first

Use industry-based materiality (the SASB standards, now part of the ISSB's
IFRS S1/S2 framework, list material issues by industry). Pick 3-5 issues for
the company's industry; explain in one sentence each why they affect cash flows
or risk.

| Industry | Usually material |
|---|---|
| Food and beverage | Packaging and waste, water use, sugar/health regulation (e.g. Mexico's front-of-pack warning labels), supply-chain sourcing, GHG from fleet and plants |
| Retail | Supply-chain labor, energy use, packaging, data privacy |
| Mining and metals | Tailings safety, water, community relations, GHG, closure costs |
| Cement and construction materials | GHG intensity and carbon pricing, energy mix, air quality |
| Banks and financials | Financial inclusion, data security, credit exposure to carbon-intensive sectors, governance |
| Telecom | Data privacy and security, network resilience, digital inclusion |
| Airlines and transport | Fuel and GHG, safety, labor relations |
| Energy and utilities | GHG, regulation and tariffs, water, community relations |
| Real estate (FIBRAs, REITs) | Energy efficiency, climate physical risk, tenant quality |

## 2. Governance checklist (often the most material ESG issue in LatAm)

- Controlling shareholder or family: stake, voting control, share classes.
- Board: size, share of independent directors (Mexican securities law requires
  at least 25%), independent audit committee, chair and CEO roles.
- Related-party transactions: size, disclosure quality (related-parties note).
- Minority protections: dividend policy, tag-along rights, free float and liquidity.
- Succession and key-person risk.
- Auditor and any qualified opinions or restatements.
- Sustainability reporting: standard used, external assurance, index membership
  (e.g. an S&P/BMV ESG index in Mexico).

## 3. Link ESG to value

Prefer explicit cash-flow effects over ad hoc discount-rate premiums:
- regulation or carbon-price scenario -> margin or capex driver;
- reformulation / packaging costs -> opex or capex;
- governance -> a justified discount to peer multiples, or a higher risk that
  shows in the risk matrix.
Say plainly when an issue is material but not quantifiable, and why.

## 4. Sources

Company sustainability/integrated report, annual report governance section,
related-parties note, proxy/assembly materials, regulators, and ESG ratings
(cite the provider and date; ratings disagree — do not rely on one).
```

- [ ] **Step 4: Create `skills/risks-esg/references/esg-template.md`**

```markdown
# ESG — <Company> (<TICKER>)

_Updated <YYYY-MM-DD>. Every figure cited._

## Material issues

| Issue | Why it matters for value | Company performance (data, trend) | Source |
|---|---|---|---|

## Environmental

## Social

## Governance

| Checklist item | Finding | Source |
|---|---|---|
| Controlling shareholder / share classes | | |
| Board independence | | |
| Audit committee | | |
| Related-party transactions | | |
| Minority protections, free float | | |
| Succession / key person | | |
| Auditor, restatements | | |
| Sustainability reporting and assurance | | |

## Link to valuation

- <issue> -> <driver or discount> -> <effect on value, or why not quantified>

## What a judge may ask

1. **Q:**  **A:**
2. **Q:**  **A:**
```

- [ ] **Step 5: Create `skills/risks-esg/SKILL.md`**

````markdown
---
name: risks-esg
description: Investment risks and ESG analysis for a CFA Research Challenge company - specific risks tied to the thesis pillars with probability x impact and a risk-matrix chart, plus industry-based ESG materiality with a LatAm governance checklist (controlling shareholder, board independence, related parties) and the link from ESG to value. Researches filings and sustainability reports and structures everything; coaches the team on which risks and ESG issues really matter and whether they are priced in. Use whenever a student asks about risks, downside, risk matrix, what could go wrong, ESG, sustainability, governance, controlling shareholders or materiality - even if they don't say risks-esg.
---

# risks-esg

## Purpose

Risks and ESG are 30 of 100 report points. Research and structure are the
assistant's job; the team decides which risks matter, how they are mitigated or
priced, which ESG issues are material and how they affect value.

## Reads

- `research/thesis.md` — pillars and kill criteria. Missing: continue, mark every
  risk's pillar as empty, add a `todo.md` item.
- `research/industry.md`, `data/adjustments.md`, `model/model-summary.json`
  (drivers and sensitivity, to size impacts). Optional.
- `filings/` — risk factors, governance section, related-parties note,
  sustainability or integrated report. Missing sustainability report: say so and
  add a `todo.md` item to download it.
- `company-profile.yaml` — sector, country.
- `research/risks.yaml`, `research/risks.md`, `research/esg.md` — if present, update them.
- `references/risk-framework.md`, `references/risks-template.yaml`,
  `references/esg-materiality-latam.md`, `references/esg-template.md`.

## Steps

1. **Collect candidate risks** from risk factors, the industry analysis, the
   thesis kill criteria, macro (FX, rates, commodities) and regulation. Write each
   as cause -> effect -> driver -> value (`references/risk-framework.md`).
2. **Size them**: probability and impact scores 1-5; use the model's drivers and
   sensitivity grid to estimate impact on value where possible. Propose, don't decide.
3. **ESG materiality**: pick 3-5 material issues for the industry from
   `references/esg-materiality-latam.md`; gather the company's data and trend for
   each; run the governance checklist.
4. **Run the coach moments** below and record the team's choices.
5. **Write** `research/risks.yaml` (template), `research/risks.md` (key-risks
   table, mitigation, priced in, downside scenario, appendix list) and
   `research/esg.md` (template). Cite every figure.
6. **Draw the risk matrix.** Find Python as in init-skills (3.10 or newer; install
   command there if matplotlib is missing) and run from the project folder:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py" --project .`
   (if `${CLAUDE_PLUGIN_ROOT}` does not resolve in the shell, use the absolute
   path of `skills/report/tools/charts.py` in the installed plugin, in quotes).
7. **Close** with the key risks, the material ESG issues, and one next step
   (usually: ask the valuation skill to run the downside scenario).

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Which 4-6 risks** truly threaten the thesis — cut the generic ones.
- **Mitigated, priced in, or neither** — for each key risk.
- **Material ESG issues** — why these 3-5 affect value for this industry.
- **Governance and value** — does the ownership structure justify a discount?

## Writes

- `research/risks.yaml`, `research/risks.md`, `research/esg.md`
- `report/charts/risk-matrix.png` (and any other chart the tool can draw)
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — risks-esg — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | risks-esg | research/risks.md, research/esg.md | researched risks and ESG; team chose key risks and material issues`
- `docs/context/memory.md`: `# decision: key risks = <ids>; material ESG = <issues>`.
- `docs/context/todo.md`: missing sustainability data, risks to quantify.
````

- [ ] **Step 6: Commit** (structural tests for this skill are added in Task 8)

```bash
git add skills/risks-esg/
git commit -m "feat(risks-esg): risks and ESG skill with risk framework, LatAm materiality guide and templates"
```

---

### Task 7: `report` skill

**Files:**
- Create: `skills/report/references/challenge-structure.md`
- Create: `skills/report/references/section-guide.md`
- Create: `skills/report/references/style-guide.md`
- Create: `skills/report/references/header-template.yaml`
- Create: `skills/report/references/ai-disclosure-template.md`
- Create: `skills/report/SKILL.md`

- [ ] **Step 1: Create `skills/report/references/challenge-structure.md`**

```markdown
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
| `99-appendix*.md` | Appendix (not graded separately; max 10 pages) | - | - |

The rules list the sections without mandating an order; putting the
investment summary first, under the header, is the common practice. File
numbers set the order — rename files to change it.

Budget rule of thumb: about 500 words per page; a half-width chart takes about
0.3 of a page. `build_docx.py --check` does this arithmetic.

## Appendix (suggested)

Income statement, balance sheet and cash flow (history + forecast), DCF summary
and WACC, comps table, sensitivity grid, full risk table, ESG data, references
(Harvard list), and the AI-use disclosure.
```

- [ ] **Step 2: Create `skills/report/references/section-guide.md`**

```markdown
# What each section must do

| Section | Judges look for | Built from | Common mistakes |
|---|---|---|---|
| Investment summary | Rating, target, 2-3 pillars, what the market misses, catalysts, key risk — readable alone | `research/thesis.md`, `valuation/valuation.md` | Restating the business description; no clear "why now" |
| Business description | What the company sells, to whom, how it makes money, segments, ownership | `filings/`, `research/industry.md` | History lessons; too long for 5 points |
| Industry and positioning | Market size and growth, structure, competitors, moat with evidence | `research/industry.md` | Generic five forces with no numbers |
| Financial analysis | Historical drivers, margins, returns, cash conversion, balance sheet, the forecast and why it differs from history | `model/review.md`, `model/model-summary.json`, `data/adjustments.md` | Tables without interpretation; forecast not tied to the thesis |
| Valuation | Methods and why, key inputs with sources, reconciliation, sensitivity, reverse DCF | `valuation/valuation.md`, charts | Black-box DCF; WACC inputs without sources; methods not reconciled |
| Investment risks | 4-6 specific risks tied to pillars, probability x impact, mitigation, downside scenario | `research/risks.md`, risk matrix | Generic list; no quantification |
| ESG | 3-5 material issues, evidence, governance, link to value | `research/esg.md` | Generic sustainability text; no valuation link |

Every section: lead with the conclusion, then the evidence. One idea per
paragraph. Each chart gets a caption and a source line.
```

- [ ] **Step 3: Create `skills/report/references/style-guide.md`**

```markdown
# Style guide

- **Language:** English, analyst register, "we" for the team. Short sentences.
  No hype ("amazing", "huge"), no hedging stacks.
- **Numbers:** currency and unit on first use (MXN 13,400 million); % with one
  decimal; margins changes in basis points; years as 2025A / 2026E.
- **Citations (Harvard):** in text `(Grupo Bimbo 2025, p. 45)`; a reference list
  in the appendix. Map the project's data tags:

| Tag in the research files | In the report |
|---|---|
| `[sourced]` | `(Author/Company Year, p. X)` |
| `[guidance]` | `(Company, 3Q25 earnings call)` |
| `[assumption]` | `(team estimate)` |
| `[calc]` | `(team model)` |
| `[unverified]` | not allowed in the report — resolve it first |

- **Figures:** Markdown image with a caption: `![Revenue and EBITDA margin](../charts/revenue-margin.png)`;
  the chart itself carries its source line.
- **Tables:** pipe tables; first row is the header; keep to 5-7 columns.
- **Rating words:** BUY / HOLD / SELL exactly as in the header.
```

- [ ] **Step 4: Create `skills/report/references/header-template.yaml`**

```yaml
# report/header.yaml - written by the report skill, read by report/tools/build_docx.py.
company: ""
exchange: ""            # e.g. BMV
ticker: ""
sector: ""
industry: ""
recommendation: ""      # BUY | HOLD | SELL - the team's decision
price: 0.0              # current price
price_date: ""          # YYYY-MM-DD
currency: ""            # e.g. MXN
target_price: 0.0       # the team's 12-month target
report_date: ""         # YYYY-MM-DD
```

- [ ] **Step 5: Create `skills/report/references/ai-disclosure-template.md`**

```markdown
# Use of AI tools

_(Appendix. Required by the Research Challenge rules when the team relied materially on AI.)_

**Tools.** <e.g. Claude (Anthropic) through Claude Code with the research-challenge plugin>.

**What we used them for.** <from docs/context/ai-use-log.md, grouped: statement
extraction and mapping; building the financial model; drafting and editing text;
charts; practice Q&A>.

**How we verified the output.** <tie-outs to reported totals; the model's
integrity checks; source citations checked by <member>; every number in this
report traced to a filing or the team model>.

**What the team decided.** <the thesis and its pillars, the key forecast
assumptions, WACC and terminal assumptions, the target price and the
recommendation, the material risks and ESG issues>.

**Reflection.** <one or two sentences: where AI helped most, where we did not
rely on it, and one limitation we noticed>.
```

- [ ] **Step 6: Create `skills/report/SKILL.md`**

````markdown
---
name: report
description: Co-write the CFA Research Challenge written report - the seven graded sections (investment summary, business description, industry and competitive positioning, financial analysis, valuation, investment risks, ESG) in English within the 10-page A4 budget, the first-page header, charts, appendix and AI-use disclosure - and assemble the report body as a Word file to put behind the official CFA Institute cover. Drafts from the team's research and model files with Harvard citations and checks page budget and uncited numbers; the team has the final say on every claim, the rating and the target. Use whenever a student asks to write, draft, edit, shorten or build the report or any section of it, or asks about page limits, citations or the AI disclosure - even if they don't say report.
---

# report

## Purpose

Turn the team's work into the graded document. Drafting, structure, charts,
citations and assembly are the assistant's job; the story, the rating, the
target and every claim belong to the team.

## Reads

- `company-profile.yaml`; `research/thesis.md`, `industry.md`, `risks.md`,
  `esg.md`; `data/adjustments.md`; `model/review.md`, `model/model-summary.json`;
  `valuation/valuation.md`, `valuation/valuation.yaml`; `docs/context/ai-use-log.md`
  and `memory.md` (team decisions). Any missing input: draft that section as a
  placeholder tagged `[assumption]`, name the skill that produces the input, add a
  `todo.md` item — never block.
- `report/sections/*.md`, `report/header.yaml` — if present, revise them.
- `references/challenge-structure.md`, `section-guide.md`, `style-guide.md`,
  `header-template.yaml`, `ai-disclosure-template.md`.

## Steps

1. **Inventory**: a table of the seven sections, the input each needs, and
   whether it exists. Say which sections can be written now.
2. **Header**: write `report/header.yaml` from the template. Recommendation and
   target price only from the team's decision (valuation.md / memory.md); if not
   decided, leave them empty and run that coach moment first.
3. **Charts**: find Python as in init-skills (3.10 or newer) and run
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py" --project .`
   (if `${CLAUDE_PLUGIN_ROOT}` does not resolve, use the absolute path of the
   installed plugin's `skills/report/tools/`, in quotes; missing packages: give the
   init-skills install command).
4. **Draft sections** in `report/sections/` with the file names in
   `references/challenge-structure.md`, in this order: financial analysis,
   valuation, risks, ESG, industry, business description, then the investment
   summary last. Follow `section-guide.md` and `style-guide.md`: English, the
   team's ideas only (never a claim they did not make), every number cited.
5. **Check**: `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/build_docx.py" --project . --check`.
   Fix uncited numbers; bring over-budget sections to the team (Coach moments).
6. **Appendix**: `99-appendix.md` (statements, DCF and WACC, comps, sensitivity
   figure, full risk table, ESG data, Harvard reference list) and
   `99-appendix-ai-use.md` from `references/ai-disclosure-template.md`, filled from
   `ai-use-log.md`; the team reviews and edits the reflection.
7. **Build**: `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/build_docx.py" --project .`
   Then tell the team: put the official CFA cover in front, check the layout and
   the 10-page count in Word, and export to PDF.
8. **Close** with: file name, estimated pages, open items, next step (pitch).

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Investment summary in three sentences**: thesis, valuation, catalyst — the
  team writes the first version; you tighten it.
- **Rating and target wording**: consistent with the valuation, the team's
  recommendation convention and the thesis kill criteria.
- **What to cut** when a section is over budget — propose the cut, the team chooses.

## Writes

- `report/header.yaml`, `report/sections/NN-*.md`, `report/charts/*.png`,
  `report/<TICKER>_report_v<N>.docx` (never overwritten)
- Appends coach-moment answers to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — report — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`, one line per section drafted or edited:
  `YYYY-MM-DD | <member> | report | report/sections/<file> | drafted from <inputs>; team edited <what>`
- `docs/context/todo.md`: placeholders, uncited numbers, missing inputs.
````

- [ ] **Step 7: Commit** (structural tests for this skill are added in Task 8)

```bash
git add skills/report/SKILL.md skills/report/references/
git commit -m "feat(report): report skill with rules-based structure, section and style guides, AI disclosure template"
```

---

### Task 8: Integration — structural tests, AGENTS template, README, manifests, evals

**Files:**
- Modify: `tests/test_plugin_structure.py`
- Modify: `skills/init-skills/templates/AGENTS.md`, `README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- Create: `evals/phase3a.md`
- Modify: spec header status

- [ ] **Step 1: Structural tests** — in `tests/test_plugin_structure.py`:

Add `"risks-esg", "report"` to the end of the `SKILLS` tuple, and append:

```python
REPORT_TOOLS = SKILLS_DIR / "report" / "tools"
TOOL_CALLS: dict[str, tuple[str, ...]] = {
    "risks-esg": ("${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py",),
    "report": ("${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py",
               "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/build_docx.py"),
}


@pytest.mark.parametrize("name", sorted(TOOL_CALLS))
def test_report_skills_call_the_tools_by_plugin_root(name: str) -> None:
    text = read_text(skill_md(name))
    for call in TOOL_CALLS[name]:
        assert call in text, call
        assert (ROOT / call.replace("${CLAUDE_PLUGIN_ROOT}/", "")).is_file(), call


def test_challenge_structure_matches_the_page_budget() -> None:
    import sys

    if str(REPORT_TOOLS) not in sys.path:
        sys.path.insert(0, str(REPORT_TOOLS))
    from build_docx import BUDGET_PAGES

    text = read_text(SKILLS_DIR / "report" / "references" / "challenge-structure.md")
    for slug, pages in BUDGET_PAGES.items():
        assert f"-{slug}.md`" in text, slug
        assert f"| {pages:.1f} |" in text, (slug, pages)


def test_risks_template_loads_in_the_chart_tool() -> None:
    import sys

    if str(REPORT_TOOLS) not in sys.path:
        sys.path.insert(0, str(REPORT_TOOLS))
    from charts import load_risks

    risks = load_risks(SKILLS_DIR / "risks-esg" / "references" / "risks-template.yaml")
    assert risks and risks[0]["id"] == "R1"
```

- [ ] **Step 2: AGENTS.md template** — add these rows after the `valuation` row of the skill table:

```markdown
| `risks-esg` | Key risks (probability x impact) and material ESG issues | `research/risks.md`, `research/esg.md` |
| `report` | Co-write the seven sections and build the Word body | `report/sections/`, `report/<TICKER>_report_v<N>.docx` |
```

- [ ] **Step 3: README**

  - Heading `## Skills (v0.2)` -> `## Skills (v0.3)`; add after the `valuation` row:

```markdown
| `risks-esg` | Specific risks with a risk matrix; ESG materiality and governance | Which risks and ESG issues matter, and how they affect value |
| `report` | Co-writes the 7 graded sections within 10 pages, charts, appendix, AI-use disclosure; builds the Word body | Every claim, the rating and the target |
```

  - "Coming next" line -> `Coming next: \`pitch\` and \`deck\` (presentation).`
  - Typical order line -> `` `init-skills` -> `thesis` + `industry` -> `financials` -> `forecast` -> `model` -> `valuation` -> `risks-esg` -> `report`. Each skill also works on its own. ``
  - Add a short section before "## Working as a team":

```markdown
## The written report

The report is always in English (CFA Institute rules). `report` builds the body
as a Word file; download the official CFA Institute cover page from the Research
Challenge student-preparation page, put it in front, check the layout and the
10-page limit in Word, and export to PDF.
```

  - Development install line: add `"matplotlib>=3.8" "python-docx>=1.1"`; mypy line becomes two commands: `python -m mypy tests skills/model/engine` and `python -m mypy skills/report/tools`.

- [ ] **Step 4: Manifests** — `plugin.json` `"version": "0.3.0"`; append to both descriptions (plugin.json and the marketplace plugin entry) the phrase `, risks and ESG, and the written report` before `. The assistant does`.

- [ ] **Step 5: Create `evals/phase3a.md`**

```markdown
# Phase 3a manual evals

Project with a built model and valuation (phase 2 evals done).

## init-skills

1. New folder, `/research-challenge:init-skills`
   - [ ] Does not ask for a report language; asks the presentation language.
   - [ ] `company-profile.yaml` has `language: "en"` and `presentation_language`.

## risks-esg

1. Prompt: "what are our key risks?"
   - [ ] Proposes specific cause -> effect -> driver -> value risks tied to pillars.
   - [ ] Asks the team to pick 4-6 and to say mitigated / priced in.
   - [ ] Writes `research/risks.yaml` and draws `report/charts/risk-matrix.png`.
2. Prompt: "do the ESG section"
   - [ ] Picks 3-5 industry-material issues, runs the governance checklist, links to value.

## report

1. Prompt: "draft the report"
   - [ ] Shows the section inventory first; placeholders for missing inputs.
   - [ ] Leaves rating/target empty until the team decides.
   - [ ] Writes sections in English with Harvard citations.
   - [ ] Runs `--check`, reports pages per section, flags uncited numbers.
2. Prompt: "build the Word file"
   - [ ] Produces `report/<TICKER>_report_v<N>.docx`, A4, header block, figures with captions.
   - [ ] Tells the team to add the official CFA cover and check 10 pages in Word.
   - [ ] Appendix includes the AI-use disclosure drafted from the log.
```

- [ ] **Step 6: Spec status** — header line -> `- **Status:** approved; phases 1, 2a, 2b and 3a implemented`.

- [ ] **Step 7: Run everything**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine; python -m mypy skills/report/tools; claude plugin validate .`
Expected: all pass; both mypy runs `Success`; validation passes.

- [ ] **Step 8: Commit**

```bash
git add tests/test_plugin_structure.py skills/init-skills/templates/AGENTS.md README.md .claude-plugin/ evals/phase3a.md docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md
git commit -m "docs: integrate risks-esg and report into tests, AGENTS template, README, manifests and evals"
```
