# Phase 2a — Model Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Python engine that turns `data/financials.csv` + `model/drivers.yaml` + `valuation/valuation.yaml` into an institutional-grade `.xlsx` with live formulas plus `model/model-summary.json`, with Python and Excel guaranteed to agree.

**Architecture:** Every model cell is defined once as an expression tree (`rcmodel.expr`). The same tree is evaluated in Python (source of truth for checks, valuation and the summary) and rendered as an Excel formula, so the two cannot drift. A layout (list of `Line`/`Header`) describes every row; `placement` assigns rows; `engine.Model` evaluates lazily with cycle detection; `writer` emits the workbook. Interest is charged on opening balances (no circularity); a revolver keeps cash at or above the minimum.

**Tech Stack:** Python 3.10+, openpyxl, PyYAML. Dev: pytest, mypy (strict), hypothesis, `formulas` (pure-Python Excel evaluator used only in tests as the parity oracle).

**Spec:** `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` §6-§7.

**Decisions taken after the spec (recorded in Task 10):**
- research_analyst has no calculation engine to borrow; the engine is new code. Only the style palette is adapted (attributed).
- No `Historical` tab: reported history sits directly in IS/BS/CF as blue cells with a source comment (document, page, tag).
- Valuation is as of the last fiscal year-end (no stub period). Sensitivity uses formula grids, not Excel data tables.
- D&A reduces PP&E only; intangibles, other non-current items, short-term debt and leases are held flat.
- Superseded during implementation: see spec §7 (stub roll-forward, intangible amortization, IFRS 16 lease renewals were added after reviews).

**Branch:** work on `feat/phase2a-engine`; merge after phase 2b adds the `model` skill that uses this engine.

---

## File map

All engine files live in `skills/model/engine/` (a skill may only rely on files inside its own directory).

| File | Responsibility |
|---|---|
| `rcmodel/__init__.py` | Package marker, version |
| `rcmodel/expr.py` | Expression tree: evaluate in Python, render as Excel |
| `rcmodel/chart.py` | Canonical line items, tags, driver keys |
| `rcmodel/inputs.py` | Load + validate profile, financials.csv, drivers.yaml, valuation.yaml |
| `rcmodel/spec.py` | `Line`, `Header`, `Fmt`, `Style`, `OBSERVED`, `Inputs` |
| `rcmodel/placement.py` | Row/column assignment |
| `rcmodel/engine.py` | `Model`: cell kinds, lazy evaluation, addresses |
| `rcmodel/lines.py` | Drivers, IS, BS, CF, Schedules, Ratios definitions |
| `rcmodel/valuation.py` | WACC, DCF, reverse DCF, Comps, Sensitivity, Football definitions |
| `rcmodel/assemble.py` | Build + evaluate the full model |
| `rcmodel/checks.py` | Integrity and parity checks |
| `rcmodel/styles.py` | Fonts, fills, borders (palette adapted from research_analyst) |
| `rcmodel/writer.py` | openpyxl workbook writer |
| `rcmodel/summary.py` | `model-summary.json` |
| `rcmodel/cli.py` | `build` + `main` (ASCII console output) |
| `build_model.py` | Launcher: `python <skill>/engine/build_model.py --project <folder>` |
| `tests/conftest.py` | Fictional balanced company "Acme Alimentos" written to a temp project |
| `tests/test_*.py` | One test module per engine module, plus Excel parity tests |

---

### Task 1: Branch, tooling and test fixture

**Files:**
- Modify: `pyproject.toml`
- Create: `skills/model/engine/rcmodel/__init__.py`
- Create: `skills/model/engine/tests/conftest.py`
- Create: `skills/model/engine/tests/test_fixture.py`

- [ ] **Step 1: Create the branch**

```bash
git checkout -b feat/phase2a-engine
```

- [ ] **Step 2: Replace `pyproject.toml`**

```toml
[project]
name = "research-challenge-plugin"
version = "0.2.0"
description = "Structural tests and model engine for the research-challenge Claude Code plugin"
requires-python = ">=3.10"
dependencies = ["openpyxl>=3.1", "pyyaml>=6"]

[project.optional-dependencies]
dev = ["pytest>=8", "mypy>=1.10", "hypothesis>=6", "formulas>=1.2"]

[tool.pytest.ini_options]
testpaths = ["tests", "skills/model/engine/tests"]

[tool.mypy]
strict = true
python_version = "3.10"
mypy_path = "skills/model/engine"

[[tool.mypy.overrides]]
module = ["openpyxl.*", "yaml", "formulas", "numpy"]
ignore_missing_imports = true
```

- [ ] **Step 3: Install dependencies**

Run: `python -m pip install "openpyxl>=3.1" "pyyaml>=6" "pytest>=8" "mypy>=1.10" "hypothesis>=6" "formulas>=1.2"`
Expected: installs succeed. If `formulas` fails to install, continue (its tests skip) and report it as a concern.

- [ ] **Step 4: Create `skills/model/engine/rcmodel/__init__.py`**

```python
"""research-challenge model engine: one definition per cell, Python values and Excel formulas."""

__version__ = "0.1.0"
```

- [ ] **Step 5: Create `skills/model/engine/tests/conftest.py`**

```python
"""Shared fixture: Acme Alimentos, a small balanced fictional company (MXN millions)."""

from __future__ import annotations

import csv
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

YEARS: tuple[int, ...] = (2021, 2022, 2023, 2024, 2025)

HISTORY: dict[str, tuple[float, ...]] = {
    "revenue": (10000, 10800, 11700, 12500, 13400),
    "cogs": (6000, 6450, 6950, 7400, 7900),
    "opex": (2600, 2800, 3000, 3250, 3500),
    "da": (500, 530, 560, 600, 640),
    "interest_expense": (300, 310, 320, 330, 340),
    "interest_income": (40, 45, 50, 55, 60),
    "other_financial_net": (-20, 10, -30, 0, 15),
    "income_tax": (336, 389, 435, 473, 521),
    "nci_income": (40, 45, 50, 55, 60),
    "shares_diluted": (1000, 1000, 1000, 995, 990),
    "cash": (1500, 1600, 1750, 1900, 2100),
    "receivables": (1200, 1300, 1400, 1500, 1600),
    "inventory": (900, 950, 1000, 1050, 1100),
    "other_current_assets": (300, 300, 300, 300, 300),
    "ppe_net": (6000, 6200, 6450, 6700, 6950),
    "intangibles_goodwill": (1500, 1500, 1500, 1500, 1500),
    "other_noncurrent_assets": (500, 500, 500, 500, 500),
    "payables": (1000, 1050, 1100, 1150, 1200),
    "other_current_liabilities": (400, 400, 400, 400, 400),
    "debt_short": (500, 500, 500, 500, 500),
    "debt_long": (3500, 3400, 3300, 3200, 3100),
    "lease_liabilities": (600, 600, 600, 600, 600),
    "other_noncurrent_liabilities": (300, 300, 300, 300, 300),
    "equity_parent": (5300, 5770, 6340, 6910, 7530),
    "nci_equity": (300, 330, 360, 390, 420),
    "cfo": (1200, 1300, 1450, 1550, 1700),
    "capex": (700, 750, 800, 850, 900),
    "dividends_paid": (300, 340, 380, 420, 460),
    "total_assets_reported": (11900, 12350, 12900, 13450, 14050),
    "net_income_reported": (784, 906, 1015, 1102, 1214),
}

SEGMENTS: dict[str, tuple[float, ...]] = {
    "seg_mx": (6000, 6500, 7000, 7500, 8000),
    "seg_us": (4000, 4300, 4700, 5000, 5400),
}

PROFILE: dict[str, Any] = {
    "company": {"name": "Acme Alimentos", "ticker": "ACME", "exchange": "BMV"},
    "accounting": {"framework": "ifrs", "reporting_currency": "MXN", "units": "millions"},
}


def _driver(values: Sequence[float]) -> dict[str, Any]:
    return {"values": list(values), "tag": "assumption", "rationale": "fixture", "pillar": "1"}


DRIVERS: dict[str, Any] = {
    "forecast_years": 5,
    "drivers": {
        "revenue_growth": _driver([0.07, 0.065, 0.06, 0.055, 0.05]),
        "gross_margin": _driver([0.41] * 5),
        "opex_pct_revenue": _driver([0.26] * 5),
        "da_pct_revenue": _driver([0.048] * 5),
        "capex_pct_revenue": _driver([0.065] * 5),
        "dso": _driver([43] * 5),
        "dio": _driver([50] * 5),
        "dpo": _driver([55] * 5),
        "other_ca_pct_revenue": _driver([0.022] * 5),
        "other_cl_pct_revenue": _driver([0.03] * 5),
        "tax_rate": _driver([0.30] * 5),
        "interest_rate_debt": _driver([0.075] * 5),
        "interest_rate_cash": _driver([0.03] * 5),
        "payout_ratio": _driver([0.40] * 5),
        "nci_share": _driver([0.05] * 5),
        "net_new_debt": _driver([-100] * 5),
        "shares_growth": _driver([0.0] * 5),
        "min_cash": _driver([1500] * 5),
    },
}

VALUATION: dict[str, Any] = {
    "share_price": 25.0,
    "price_52w_low": 20.0,
    "price_52w_high": 28.0,
    "mid_year": True,
    "wacc": {
        "risk_free": 0.09,
        "equity_risk_premium": 0.055,
        "country_risk_premium": 0.0,
        "beta_unlevered": 0.8,
        "target_debt_to_equity": 0.4,
        "pre_tax_cost_of_debt": 0.10,
        "tax_rate": 0.30,
    },
    "terminal": {"growth": 0.04, "exit_ev_ebitda": 7.0, "lt_nominal_gdp_growth": 0.07},
    "peers": [
        {"name": "Peer A", "ticker": "PA", "price": 50, "shares": 500, "net_debt": 3000, "ebitda_fwd": 4000, "eps_fwd": 4.0},
        {"name": "Peer B", "ticker": "PB", "price": 30, "shares": 800, "net_debt": 2000, "ebitda_fwd": 3800, "eps_fwd": 2.5},
        {"name": "Peer C", "ticker": "PC", "price": 80, "shares": 200, "net_debt": 1500, "ebitda_fwd": 2600, "eps_fwd": 6.0},
    ],
    "target_price": None,
}


def write_project(
    root: Path,
    history: Mapping[str, Sequence[float]] = HISTORY,
    drivers: Mapping[str, Any] | None = DRIVERS,
    valuation: Mapping[str, Any] | None = VALUATION,
    profile: Mapping[str, Any] = PROFILE,
    unverified: Sequence[str] = (),
    years: Sequence[int] = YEARS,
) -> Path:
    """Write a complete team project folder under `root` and return it."""
    for folder in ("data", "model", "valuation"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    (root / "company-profile.yaml").write_text(yaml.safe_dump(dict(profile), sort_keys=False), encoding="utf-8")
    with (root / "data" / "financials.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["line_item", "year", "value", "tag", "source_doc", "page", "note"])
        for key, values in history.items():
            tag = "unverified" if key in unverified else "sourced"
            for year, value in zip(years, values):
                writer.writerow([key, year, value, tag, "Annual report 2025", "45", ""])
    if drivers is not None:
        (root / "model" / "drivers.yaml").write_text(yaml.safe_dump(dict(drivers), sort_keys=False), encoding="utf-8")
    if valuation is not None:
        (root / "valuation" / "valuation.yaml").write_text(yaml.safe_dump(dict(valuation), sort_keys=False), encoding="utf-8")
    return root


@pytest.fixture
def project(tmp_path: Path) -> Path:
    return write_project(tmp_path)
```

- [ ] **Step 6: Create `skills/model/engine/tests/test_fixture.py`**

```python
"""The fixture itself must be internally consistent, or every other test is meaningless."""

from __future__ import annotations

from pathlib import Path

from conftest import HISTORY, SEGMENTS, YEARS


def _series(key: str) -> tuple[float, ...]:
    return HISTORY[key]


def test_fixture_balance_sheet_balances() -> None:
    assets = ("cash", "receivables", "inventory", "other_current_assets", "ppe_net", "intangibles_goodwill", "other_noncurrent_assets")
    claims = ("payables", "other_current_liabilities", "debt_short", "debt_long", "lease_liabilities",
              "other_noncurrent_liabilities", "equity_parent", "nci_equity")
    for i in range(len(YEARS)):
        total_assets = sum(_series(k)[i] for k in assets)
        assert total_assets == sum(_series(k)[i] for k in claims)
        assert total_assets == _series("total_assets_reported")[i]


def test_fixture_net_income_ties() -> None:
    for i in range(len(YEARS)):
        ebt = (_series("revenue")[i] - _series("cogs")[i] - _series("opex")[i] - _series("interest_expense")[i]
               + _series("interest_income")[i] + _series("other_financial_net")[i])
        assert ebt - _series("income_tax")[i] == _series("net_income_reported")[i]


def test_fixture_segments_add_up() -> None:
    for i in range(len(YEARS)):
        assert SEGMENTS["seg_mx"][i] + SEGMENTS["seg_us"][i] == _series("revenue")[i]


def test_project_files_written(project: Path) -> None:
    for relative in ("company-profile.yaml", "data/financials.csv", "model/drivers.yaml", "valuation/valuation.yaml"):
        assert (project / relative).is_file(), relative
```

- [ ] **Step 7: Run the fixture tests**

Run: `python -m pytest -q skills/model/engine/tests`
Expected: `4 passed`

- [ ] **Step 8: Run the whole suite and mypy**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine`
Expected: all tests pass (26 structural + 4 fixture); mypy `Success`.

- [ ] **Step 9: Commit**

```bash
git add pyproject.toml skills/model/engine/
git commit -m "test(engine): add tooling and balanced Acme fixture"
```

---

### Task 2: Expression tree (`expr.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/expr.py`
- Test: `skills/model/engine/tests/test_expr.py`
- Test: `skills/model/engine/tests/test_expr_excel_parity.py`

- [ ] **Step 1: Write the failing unit tests** — `tests/test_expr.py`

```python
from __future__ import annotations

import math

import pytest

from rcmodel.expr import At, Neg, Ref, Rng, cmp, fn, iff


class FakeCtx:
    """Values per (key, period); addresses are the key letter plus the period number."""

    def __init__(self, values: dict[tuple[str, int | None], float]) -> None:
        self.values = values

    def value(self, key: str, period: int | None) -> float:
        return self.values[(key, period)]

    def address(self, key: str, period: int | None, from_sheet: str) -> str:
        return f"{key.upper()}{'' if period is None else period}"

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str:
        return f"{key.upper()}{first}:{key.upper()}{last}"


CTX = FakeCtx({
    ("a", 2): 10.0, ("a", 1): 8.0, ("g", 2): 0.05, ("b", 2): 3.0, ("c", 2): 2.0,
    ("f", 1): 100.0, ("f", 2): 110.0, ("f", 3): 121.0, ("s", None): 7.0,
})


def test_growth_formula_evaluates_and_renders() -> None:
    e = Ref("a", 1) * (1 + Ref("g"))
    assert e.evaluate(CTX, 2) == pytest.approx(8.4)
    assert e.render(CTX, 2, "S") == "A1*(1+G2)"


def test_lag_sets_max_lag() -> None:
    assert (Ref("a") - Ref("a", 1)).max_lag() == 1
    assert Ref("a").max_lag() == 0


def test_subtraction_keeps_right_hand_grouping() -> None:
    assert (Ref("a") - (Ref("b") - Ref("c"))).render(CTX, 2, "S") == "A2-(B2-C2)"
    assert ((Ref("a") - Ref("b")) - Ref("c")).render(CTX, 2, "S") == "A2-B2-C2"
    assert (Ref("a") - (Ref("b") - Ref("c"))).evaluate(CTX, 2) == 9.0


def test_division_by_zero_is_nan() -> None:
    assert math.isnan((Ref("a") / (Ref("b") - 3)).evaluate(CTX, 2))


def test_negative_numbers_are_parenthesized() -> None:
    assert (Ref("a") * -2).render(CTX, 2, "S") == "A2*(-2)"


def test_negation_follows_excel_precedence() -> None:
    squared_of_negative = Neg(Ref("b")) ** 2
    assert squared_of_negative.render(CTX, 2, "S") == "-B2^2"  # Excel reads (-B2)^2
    assert squared_of_negative.evaluate(CTX, 2) == 9.0
    negative_of_square = Neg(Ref("b") ** 2)
    assert negative_of_square.render(CTX, 2, "S") == "-(B2^2)"
    assert negative_of_square.evaluate(CTX, 2) == -9.0


def test_npv_matches_manual_discounting() -> None:
    e = fn("NPV", 0.1, Rng("f", 1, 3))
    expected = 100 / 1.1 + 110 / 1.1**2 + 121 / 1.1**3
    assert e.evaluate(CTX, None) == pytest.approx(expected)
    assert e.render(CTX, None, "S") == "NPV(0.1,F1:F3)"


def test_if_with_comparison() -> None:
    e = iff(cmp(Ref("a"), ">", 5), Ref("b"), Ref("c"))
    assert e.evaluate(CTX, 2) == 3.0
    assert e.render(CTX, 2, "S") == "IF(A2>5,B2,C2)"


def test_aggregates() -> None:
    assert fn("SUM", Rng("f", 1, 3)).evaluate(CTX, None) == 331.0
    assert fn("MEDIAN", Ref("a"), Ref("b"), Ref("c")).evaluate(CTX, 2) == 3.0
    assert fn("MIN", Ref("a"), Ref("b")).evaluate(CTX, 2) == 3.0
    assert fn("MAX", Ref("a"), Ref("b")).evaluate(CTX, 2) == 10.0
    assert fn("ABS", Ref("b") - Ref("a")).evaluate(CTX, 2) == 7.0


def test_at_and_scalar_refs() -> None:
    assert At("a", 1).evaluate(CTX, None) == 8.0
    assert At("a", 1).render(CTX, None, "S") == "A1"
    assert Ref("s").evaluate(CTX, None) == 7.0


def test_unknown_function_rejected() -> None:
    with pytest.raises(ValueError):
        fn("VLOOKUP", Ref("a"))


def test_comparison_with_nan_is_false() -> None:
    assert cmp(Ref("a") / (Ref("b") - 3), "<=", 1).evaluate(CTX, 2) == 0.0
```

- [ ] **Step 2: Write the Excel-semantics oracle test** — `tests/test_expr_excel_parity.py`

```python
"""Rendered formulas must compute the same value in an Excel engine as in Python."""

from __future__ import annotations

import math

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from rcmodel.expr import Bin, Expr, Neg, Num, Ref

formulas = pytest.importorskip("formulas")

LEAVES: dict[str, float] = {"a": 1.5, "b": -2.25}


class LiteralCtx:
    """Renders every reference as its numeric literal, so the formula is self-contained."""

    def value(self, key: str, period: int | None) -> float:
        return LEAVES[key]

    def address(self, key: str, period: int | None, from_sheet: str) -> str:
        return f"({LEAVES[key]!r})"

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str:
        raise AssertionError("ranges are not generated here")


def _trees() -> st.SearchStrategy[Expr]:
    leaves: st.SearchStrategy[Expr] = st.one_of(
        st.sampled_from([Ref("a"), Ref("b")]),
        st.floats(min_value=-5, max_value=5, allow_nan=False).filter(lambda x: abs(x) > 1e-3).map(Num),
    )

    def extend(children: st.SearchStrategy[Expr]) -> st.SearchStrategy[Expr]:
        return st.one_of(
            st.tuples(st.sampled_from(["+", "-", "*", "/"]), children, children).map(lambda t: Bin(t[0], t[1], t[2])),
            children.map(Neg),
            st.tuples(children, st.sampled_from([2.0, 3.0])).map(lambda t: Bin("^", t[0], Num(t[1]))),
        )

    return st.recursive(leaves, extend, max_leaves=8)


def _to_float(result: object) -> float:
    try:
        import numpy as np

        return float(np.asarray(result, dtype=object).ravel()[0])
    except (TypeError, ValueError):
        return math.nan


@settings(max_examples=150, deadline=None)
@given(tree=_trees())
def test_rendered_formula_matches_python(tree: Expr) -> None:
    ctx = LiteralCtx()
    python_value = tree.evaluate(ctx, 0)
    compiled = formulas.Parser().ast("=" + tree.render(ctx, 0, "S"))[1].compile()
    excel_value = _to_float(compiled())
    if not math.isfinite(python_value):
        assert not math.isfinite(excel_value)
    else:
        assert excel_value == pytest.approx(python_value, rel=1e-9, abs=1e-9)
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_expr.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.expr'`.

- [ ] **Step 4: Implement `rcmodel/expr.py`**

```python
"""One definition, two renderings: a Python value and an Excel formula.

Every model cell is an ``Expr`` tree. The engine evaluates the tree in Python
(the source of truth for checks, valuation and model-summary.json) and renders
the same tree as an Excel formula, so the workbook and the Python numbers
cannot drift apart.
"""

from __future__ import annotations

import math
import statistics
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol, Union

ATOM = 9
UNARY = 4
COMPARISON = 0
BINARY_PRECEDENCE: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
COMPARE_OPS = frozenset({"<", "<=", ">", ">=", "=", "<>"})
FUNCTIONS = frozenset({"SUM", "MIN", "MAX", "MEDIAN", "ABS", "IF", "NPV"})


class Context(Protocol):
    """What an expression needs from the model to evaluate or render itself."""

    def value(self, key: str, period: int | None) -> float: ...

    def address(self, key: str, period: int | None, from_sheet: str) -> str: ...

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str: ...


class Expr:
    """Base node. Subclasses implement evaluate, render and (if they reference lines) max_lag."""

    @property
    def precedence(self) -> int:
        return ATOM

    def evaluate(self, ctx: Context, t: int | None) -> float:
        raise NotImplementedError

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        raise NotImplementedError

    def max_lag(self) -> int:
        return 0

    def __add__(self, other: Operand) -> Expr:
        return Bin("+", self, wrap(other))

    def __radd__(self, other: Operand) -> Expr:
        return Bin("+", wrap(other), self)

    def __sub__(self, other: Operand) -> Expr:
        return Bin("-", self, wrap(other))

    def __rsub__(self, other: Operand) -> Expr:
        return Bin("-", wrap(other), self)

    def __mul__(self, other: Operand) -> Expr:
        return Bin("*", self, wrap(other))

    def __rmul__(self, other: Operand) -> Expr:
        return Bin("*", wrap(other), self)

    def __truediv__(self, other: Operand) -> Expr:
        return Bin("/", self, wrap(other))

    def __rtruediv__(self, other: Operand) -> Expr:
        return Bin("/", wrap(other), self)

    def __pow__(self, other: Operand) -> Expr:
        return Bin("^", self, wrap(other))

    def __rpow__(self, other: Operand) -> Expr:
        return Bin("^", wrap(other), self)

    def __neg__(self) -> Expr:
        return Neg(self)


Operand = Union[Expr, int, float]


def wrap(x: Operand) -> Expr:
    """Turn a Python number into a Num node; pass expressions through."""
    return x if isinstance(x, Expr) else Num(float(x))


def _arith(op: str, x: float, y: float) -> float:
    try:
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y
        return math.pow(x, y)
    except (ZeroDivisionError, OverflowError, ValueError):
        return math.nan


@dataclass(frozen=True)
class Num(Expr):
    v: float

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return self.v

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        text = str(int(self.v)) if self.v.is_integer() and abs(self.v) < 1e15 else repr(self.v)
        return f"({text})" if self.v < 0 else text


@dataclass(frozen=True)
class Ref(Expr):
    """A line `lag` periods back (0 = this period). References to single values ignore the period."""

    key: str
    lag: int = 0

    def _period(self, t: int | None) -> int | None:
        return None if t is None else t - self.lag

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return ctx.value(self.key, self._period(t))

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return ctx.address(self.key, self._period(t), sheet)

    def max_lag(self) -> int:
        return self.lag


@dataclass(frozen=True)
class At(Expr):
    """A per-year line at a fixed period index (used from single-value cells)."""

    key: str
    period: int

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return ctx.value(self.key, self.period)

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return ctx.address(self.key, self.period, sheet)


@dataclass(frozen=True)
class Rng:
    """A run of periods of one line, for SUM / NPV / MEDIAN / MIN / MAX."""

    key: str
    first: int
    last: int

    def values(self, ctx: Context) -> list[float]:
        return [ctx.value(self.key, p) for p in range(self.first, self.last + 1)]

    def render(self, ctx: Context, sheet: str) -> str:
        return ctx.range_address(self.key, self.first, self.last, sheet)


@dataclass(frozen=True)
class Bin(Expr):
    op: str
    a: Expr
    b: Expr

    def __post_init__(self) -> None:
        if self.op not in BINARY_PRECEDENCE:
            raise ValueError(f"unsupported operator {self.op!r}")

    @property
    def precedence(self) -> int:
        return BINARY_PRECEDENCE[self.op]

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return _arith(self.op, self.a.evaluate(ctx, t), self.b.evaluate(ctx, t))

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        p = self.precedence
        left = self.a.render(ctx, t, sheet)
        if self.a.precedence < p:
            left = f"({left})"
        right = self.b.render(ctx, t, sheet)
        if self.b.precedence < p or (self.b.precedence == p and self.op in ("-", "/", "^")):
            right = f"({right})"
        return f"{left}{self.op}{right}"

    def max_lag(self) -> int:
        return max(self.a.max_lag(), self.b.max_lag())


@dataclass(frozen=True)
class Neg(Expr):
    """Unary minus. Excel binds it tighter than ^, and so does this tree: Neg(x)^2 = (-x)^2."""

    a: Expr

    @property
    def precedence(self) -> int:
        return UNARY

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return -self.a.evaluate(ctx, t)

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        inner = self.a.render(ctx, t, sheet)
        return f"-({inner})" if self.a.precedence < ATOM else f"-{inner}"

    def max_lag(self) -> int:
        return self.a.max_lag()


@dataclass(frozen=True)
class Cmp(Expr):
    """Comparison; evaluates to 1.0 (true) or 0.0 (false). Any NaN operand is false."""

    op: str
    a: Expr
    b: Expr

    def __post_init__(self) -> None:
        if self.op not in COMPARE_OPS:
            raise ValueError(f"unsupported comparison {self.op!r}")

    @property
    def precedence(self) -> int:
        return COMPARISON

    def evaluate(self, ctx: Context, t: int | None) -> float:
        x, y = self.a.evaluate(ctx, t), self.b.evaluate(ctx, t)
        if math.isnan(x) or math.isnan(y):
            return 0.0
        outcomes = {"<": x < y, "<=": x <= y, ">": x > y, ">=": x >= y, "=": x == y, "<>": x != y}
        return 1.0 if outcomes[self.op] else 0.0

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return f"{self.a.render(ctx, t, sheet)}{self.op}{self.b.render(ctx, t, sheet)}"

    def max_lag(self) -> int:
        return max(self.a.max_lag(), self.b.max_lag())


Arg = Union[Expr, Rng]


@dataclass(frozen=True)
class Func(Expr):
    name: str
    args: tuple[Arg, ...]

    def __post_init__(self) -> None:
        if self.name not in FUNCTIONS:
            raise ValueError(f"unsupported function {self.name!r}")
        if not self.args:
            raise ValueError(f"{self.name} needs arguments")
        if self.name == "IF" and len(self.args) != 3:
            raise ValueError("IF takes exactly 3 arguments")
        if self.name == "ABS" and len(self.args) != 1:
            raise ValueError("ABS takes exactly 1 argument")
        if self.name == "NPV" and (len(self.args) < 2 or isinstance(self.args[0], Rng)):
            raise ValueError("NPV takes a rate and then cash flows")
        if self.name in ("IF", "ABS") and any(isinstance(a, Rng) for a in self.args):
            raise ValueError(f"{self.name} does not take ranges")

    def evaluate(self, ctx: Context, t: int | None) -> float:
        if self.name == "IF":
            cond, yes, no = (_as_expr(a) for a in self.args)
            return yes.evaluate(ctx, t) if cond.evaluate(ctx, t) != 0.0 else no.evaluate(ctx, t)
        if self.name == "NPV":
            rate = _as_expr(self.args[0]).evaluate(ctx, t)
            total = 0.0
            for i, flow in enumerate(_collect(self.args[1:], ctx, t), start=1):
                total += _arith("/", flow, _arith("^", 1.0 + rate, float(i)))
            return total
        values = _collect(self.args, ctx, t)
        if any(math.isnan(v) for v in values):
            return math.nan
        if self.name == "SUM":
            return math.fsum(values)
        if self.name == "MIN":
            return min(values)
        if self.name == "MAX":
            return max(values)
        if self.name == "MEDIAN":
            return float(statistics.median(values))
        return abs(values[0])

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        parts = [a.render(ctx, sheet) if isinstance(a, Rng) else a.render(ctx, t, sheet) for a in self.args]
        return f"{self.name}({','.join(parts)})"

    def max_lag(self) -> int:
        return max((a.max_lag() for a in self.args if isinstance(a, Expr)), default=0)


def _as_expr(arg: Arg) -> Expr:
    if isinstance(arg, Rng):
        raise TypeError("a range is not allowed here")
    return arg


def _collect(args: Sequence[Arg], ctx: Context, t: int | None) -> list[float]:
    values: list[float] = []
    for arg in args:
        if isinstance(arg, Rng):
            values.extend(arg.values(ctx))
        else:
            values.append(arg.evaluate(ctx, t))
    return values


def fn(name: str, *args: Operand | Rng) -> Func:
    """Build a function node: fn("SUM", Rng("x", 5, 9)), fn("MAX", a, b)."""
    return Func(name, tuple(a if isinstance(a, Rng) else wrap(a) for a in args))


def cmp(a: Operand, op: str, b: Operand) -> Cmp:
    return Cmp(op, wrap(a), wrap(b))


def iff(cond: Expr, yes: Operand, no: Operand) -> Func:
    return Func("IF", (cond, wrap(yes), wrap(no)))
```

- [ ] **Step 5: Run the unit tests**

Run: `python -m pytest -q skills/model/engine/tests/test_expr.py`
Expected: `12 passed`

- [ ] **Step 6: Run the Excel oracle test**

Run: `python -m pytest -q skills/model/engine/tests/test_expr_excel_parity.py`
Expected: `1 passed` (or `1 skipped` if `formulas` is not installed). If it fails, do NOT change `Neg`/`Bin` precedence to make it pass — report the falsifying example as DONE_WITH_CONCERNS; it means either the renderer or the `formulas` library disagrees with Excel and a human must decide which.

- [ ] **Step 7: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/expr.py skills/model/engine/tests/test_expr.py skills/model/engine/tests/test_expr_excel_parity.py
git commit -m "feat(engine): expression tree evaluated in Python and rendered as Excel"
```

---

### Task 3: Canonical chart and input loading (`chart.py`, `inputs.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/chart.py`
- Create: `skills/model/engine/rcmodel/inputs.py`
- Test: `skills/model/engine/tests/test_inputs.py`

- [ ] **Step 1: Write the failing tests** — `tests/test_inputs.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

import pytest

from conftest import DRIVERS, HISTORY, PROFILE, VALUATION, YEARS, write_project
from rcmodel.inputs import InputError, load_inputs


def _messages(project: Path) -> list[str]:
    with pytest.raises(InputError) as caught:
        load_inputs(project)
    return caught.value.messages


def test_loads_the_fixture(project: Path) -> None:
    inputs = load_inputs(project)
    assert inputs.hist_years == YEARS
    assert inputs.fcst_years == (2026, 2027, 2028, 2029, 2030)
    assert inputs.history["revenue"][2025].value == 13400
    assert inputs.history["revenue"][2025].source_doc == "Annual report 2025"
    assert inputs.drivers["gross_margin"].values == (0.41,) * 5
    assert inputs.valuation is not None
    assert len(inputs.valuation.peers) == 3
    assert inputs.warnings == ()


def test_missing_required_line_is_reported(tmp_path: Path) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "cash"}
    messages = _messages(write_project(tmp_path, history=history))
    assert any("'cash'" in m for m in messages)


def test_unknown_line_item_and_bad_tag(tmp_path: Path) -> None:
    write_project(tmp_path)
    with (tmp_path / "data" / "financials.csv").open("a", encoding="utf-8") as handle:
        handle.write("ebitdaa,2025,1,sourced,AR,1,\n")
        handle.write("capex,2019,1,made_up,AR,1,\n")
    messages = _messages(tmp_path)
    assert any("unknown line_item 'ebitdaa'" in m for m in messages)
    assert any("tag 'made_up'" in m for m in messages)


def test_unverified_tag_warns(tmp_path: Path) -> None:
    inputs = load_inputs(write_project(tmp_path, unverified=("capex",)))
    assert any("capex 2025" in w and "unverified" in w for w in inputs.warnings)


def test_too_few_years(tmp_path: Path) -> None:
    history = {k: v[:2] for k, v in HISTORY.items()}
    messages = _messages(write_project(tmp_path, history=history, years=YEARS[:2]))
    assert any("at least 3 years" in m for m in messages)


def test_driver_length_mismatch(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"]["gross_margin"]["values"] = [0.4, 0.4]
    messages = _messages(write_project(tmp_path, drivers=drivers))
    assert any("'gross_margin' needs exactly 5 numeric values" in m for m in messages)


def test_unknown_driver(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"]["ebitda_margin"] = {"values": [0.2] * 5}
    messages = _messages(write_project(tmp_path, drivers=drivers))
    assert any("unknown driver 'ebitda_margin'" in m for m in messages)


def test_missing_drivers_file_uses_defaults(tmp_path: Path) -> None:
    inputs = load_inputs(write_project(tmp_path, drivers=None))
    assert inputs.drivers == {}
    assert inputs.fcst_years == (2026, 2027, 2028, 2029, 2030)
    assert any("drivers.yaml not found" in w for w in inputs.warnings)


def test_missing_driver_warns_with_its_default(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    del drivers["drivers"]["gross_margin"]
    del drivers["drivers"]["net_new_debt"]
    inputs = load_inputs(write_project(tmp_path, drivers=drivers))
    assert any("'gross_margin'" in w and "last actual" in w for w in inputs.warnings)
    assert any("'net_new_debt'" in w and "zero" in w for w in inputs.warnings)


def test_profile_with_placeholders_rejected(tmp_path: Path) -> None:
    profile = copy.deepcopy(PROFILE)
    profile["company"]["ticker"] = "{{TICKER}}"
    messages = _messages(write_project(tmp_path, profile=profile))
    assert any("init-skills" in m for m in messages)


def test_valuation_is_optional(tmp_path: Path) -> None:
    assert load_inputs(write_project(tmp_path, valuation=None)).valuation is None


def test_valuation_bad_number(tmp_path: Path) -> None:
    valuation = copy.deepcopy(VALUATION)
    valuation["wacc"]["risk_free"] = "high"
    messages = _messages(write_project(tmp_path, valuation=valuation))
    assert any("wacc.risk_free must be a number" in m for m in messages)


def test_segments_need_history(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["revenue_segments"] = [{"key": "mx", "label": "Mexico"}]
    messages = _messages(write_project(tmp_path, drivers=drivers))
    assert any("seg_mx" in m for m in messages)


def test_missing_financials_file(tmp_path: Path) -> None:
    write_project(tmp_path)
    (tmp_path / "data" / "financials.csv").unlink()
    messages = _messages(tmp_path)
    assert any("financials skill" in m for m in messages)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_inputs.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.inputs'`.

- [ ] **Step 3: Implement `rcmodel/chart.py`**

```python
"""Canonical line items the engine understands (annual, non-financial companies).

The financials skill maps every reported figure to one of these keys. Costs,
capex, taxes and dividends are positive numbers; formulas subtract them.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Statement(Enum):
    IS = "IS"
    BS = "BS"
    CF = "CF"
    CHECK = "CHECK"


@dataclass(frozen=True)
class ChartItem:
    key: str
    label: str
    statement: Statement
    required: bool
    meaning: str


CHART: tuple[ChartItem, ...] = (
    ChartItem("revenue", "Revenue", Statement.IS, True, "Net sales or total revenue"),
    ChartItem("cogs", "Cost of sales", Statement.IS, True, "Positive; includes D&A if the company reports it there"),
    ChartItem("opex", "Operating expenses (net)", Statement.IS, True, "SG&A plus other operating expenses, net of other operating income; positive"),
    ChartItem("da", "Depreciation and amortization", Statement.CF, True, "From the cash-flow statement; already inside cogs/opex"),
    ChartItem("interest_expense", "Interest expense", Statement.IS, True, "Positive; includes lease interest under IFRS 16"),
    ChartItem("interest_income", "Interest income", Statement.IS, False, "Positive"),
    ChartItem("other_financial_net", "Other financial result, net", Statement.IS, False, "FX, derivatives, associates; income positive, loss negative"),
    ChartItem("income_tax", "Income tax", Statement.IS, True, "Positive = expense"),
    ChartItem("nci_income", "Net income to non-controlling interests", Statement.IS, False, "Positive"),
    ChartItem("shares_diluted", "Diluted shares", Statement.IS, True, "Weighted-average diluted shares, same units as the model"),
    ChartItem("cash", "Cash and equivalents", Statement.BS, True, "Including short-term investments treated as cash"),
    ChartItem("receivables", "Accounts receivable", Statement.BS, True, "Trade receivables, net"),
    ChartItem("inventory", "Inventories", Statement.BS, False, "Net of allowances"),
    ChartItem("other_current_assets", "Other current assets", Statement.BS, False, "Everything else current"),
    ChartItem("ppe_net", "PP&E and right-of-use assets, net", Statement.BS, True, "Net of depreciation"),
    ChartItem("intangibles_goodwill", "Intangibles and goodwill", Statement.BS, False, "Net"),
    ChartItem("other_noncurrent_assets", "Other non-current assets", Statement.BS, False, "Deferred taxes, investments, other"),
    ChartItem("payables", "Accounts payable", Statement.BS, True, "Trade payables"),
    ChartItem("other_current_liabilities", "Other current liabilities", Statement.BS, False, "Excluding debt and leases"),
    ChartItem("debt_short", "Short-term debt", Statement.BS, False, "Including the current portion of long-term debt"),
    ChartItem("debt_long", "Long-term debt", Statement.BS, False, "Non-current borrowings"),
    ChartItem("lease_liabilities", "Lease liabilities", Statement.BS, False, "Current plus non-current"),
    ChartItem("other_noncurrent_liabilities", "Other non-current liabilities", Statement.BS, False, "Deferred taxes, provisions, other"),
    ChartItem("equity_parent", "Shareholders' equity", Statement.BS, True, "Attributable to the parent"),
    ChartItem("nci_equity", "Non-controlling interests (equity)", Statement.BS, False, "Minority interest in equity"),
    ChartItem("cfo", "Cash flow from operations", Statement.CF, True, "As reported"),
    ChartItem("capex", "Capital expenditures", Statement.CF, True, "Positive; PP&E plus intangible purchases"),
    ChartItem("dividends_paid", "Dividends paid", Statement.CF, False, "Positive; to parent shareholders"),
    ChartItem("total_assets_reported", "Total assets as reported", Statement.CHECK, False, "Used only to check the mapping"),
    ChartItem("net_income_reported", "Net income as reported", Statement.CHECK, False, "Used only to check the mapping"),
)

BY_KEY: dict[str, ChartItem] = {item.key: item for item in CHART}
REQUIRED_KEYS: frozenset[str] = frozenset(item.key for item in CHART if item.required)
TAGS: frozenset[str] = frozenset({"sourced", "guidance", "assumption", "calc", "unverified"})
SEGMENT_PREFIX = "seg_"

DRIVER_KEYS: tuple[str, ...] = (
    "revenue_growth",
    "gross_margin",
    "opex_pct_revenue",
    "da_pct_revenue",
    "capex_pct_revenue",
    "dso",
    "dio",
    "dpo",
    "other_ca_pct_revenue",
    "other_cl_pct_revenue",
    "tax_rate",
    "interest_rate_debt",
    "interest_rate_cash",
    "payout_ratio",
    "nci_share",
    "net_new_debt",
    "shares_growth",
    "min_cash",
)
ZERO_DEFAULT_DRIVERS: frozenset[str] = frozenset({"net_new_debt", "shares_growth"})
```

- [ ] **Step 4: Implement `rcmodel/inputs.py`**

```python
"""Load and validate the project files the engine reads.

- company-profile.yaml        written by init-skills
- data/financials.csv         written by the financials skill
- model/drivers.yaml          written by the forecast skill (optional)
- valuation/valuation.yaml    written by the valuation skill (optional)

Every problem is collected and raised together, so a student fixes them in one pass.
"""

from __future__ import annotations

import csv
import math
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypeVar

import yaml

from .chart import BY_KEY, DRIVER_KEYS, REQUIRED_KEYS, SEGMENT_PREFIX, TAGS, ZERO_DEFAULT_DRIVERS

MIN_HIST_YEARS = 3
MAX_HIST_YEARS = 5
DEFAULT_FCST_YEARS = 5
MAX_FCST_YEARS = 10
FIN_COLUMNS = ("line_item", "year", "value", "tag", "source_doc", "page")
WACC_FIELDS = ("risk_free", "equity_risk_premium", "country_risk_premium", "beta_unlevered",
               "target_debt_to_equity", "pre_tax_cost_of_debt", "tax_rate")
TERMINAL_FIELDS = ("growth", "exit_ev_ebitda", "lt_nominal_gdp_growth")

T = TypeVar("T")


class InputError(Exception):
    """One or more project files are missing or invalid; `messages` lists every problem."""

    def __init__(self, messages: list[str]) -> None:
        super().__init__("; ".join(messages))
        self.messages = messages


@dataclass(frozen=True)
class Profile:
    name: str
    ticker: str
    currency: str
    units: str
    framework: str


@dataclass(frozen=True)
class Observation:
    value: float
    tag: str
    source_doc: str
    page: str


@dataclass(frozen=True)
class DriverInput:
    values: tuple[float, ...]
    tag: str
    rationale: str
    pillar: str


@dataclass(frozen=True)
class Segment:
    key: str
    label: str


@dataclass(frozen=True)
class Peer:
    name: str
    ticker: str
    price: float
    shares: float
    net_debt: float
    ebitda_fwd: float
    eps_fwd: float


@dataclass(frozen=True)
class Valuation:
    share_price: float
    price_52w_low: float
    price_52w_high: float
    risk_free: float
    equity_risk_premium: float
    country_risk_premium: float
    beta_unlevered: float
    target_debt_to_equity: float
    pre_tax_cost_of_debt: float
    tax_rate: float
    terminal_growth: float
    exit_ev_ebitda: float
    lt_nominal_gdp_growth: float
    mid_year: bool
    peers: tuple[Peer, ...]
    target_price: float | None


@dataclass(frozen=True)
class ModelInputs:
    profile: Profile
    hist_years: tuple[int, ...]
    fcst_years: tuple[int, ...]
    history: dict[str, dict[int, Observation]]
    drivers: dict[str, DriverInput]
    segments: tuple[Segment, ...]
    valuation: Valuation | None
    warnings: tuple[str, ...]

    @property
    def years(self) -> tuple[int, ...]:
        return self.hist_years + self.fcst_years

    @property
    def h(self) -> int:
        return len(self.hist_years)

    @property
    def n(self) -> int:
        return len(self.years)


def load_inputs(project: Path) -> ModelInputs:
    errors: list[str] = []
    profile = _collect(errors, lambda: load_profile(project / "company-profile.yaml"))
    financials = _collect(errors, lambda: load_financials(project / "data" / "financials.csv"))
    if errors or profile is None or financials is None:
        raise InputError(errors)
    history, hist_years, warnings = financials
    drivers_result = _collect(errors, lambda: load_drivers(project / "model" / "drivers.yaml", history, hist_years))
    valuation = _collect(errors, lambda: load_valuation(project / "valuation" / "valuation.yaml"))
    if errors or drivers_result is None:
        raise InputError(errors)
    drivers, segments, n_fcst, driver_warnings = drivers_result
    last = hist_years[-1]
    return ModelInputs(
        profile=profile,
        hist_years=hist_years,
        fcst_years=tuple(range(last + 1, last + 1 + n_fcst)),
        history=history,
        drivers=drivers,
        segments=segments,
        valuation=valuation,
        warnings=tuple(warnings + driver_warnings),
    )


def load_profile(path: Path) -> Profile:
    if not path.is_file():
        raise InputError([f"{path.name} not found: run /research-challenge:init-skills first"])
    doc = _mapping(_read_yaml(path), path.name)
    company = _mapping(doc.get("company"), f"{path.name} > company")
    accounting = _mapping(doc.get("accounting"), f"{path.name} > accounting")
    fields: dict[str, object] = {
        "company.name": company.get("name"),
        "company.ticker": company.get("ticker"),
        "accounting.reporting_currency": accounting.get("reporting_currency"),
        "accounting.units": accounting.get("units"),
        "accounting.framework": accounting.get("framework"),
    }
    errors: list[str] = []
    clean: dict[str, str] = {}
    for name, value in fields.items():
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path.name}: {name} is missing")
        elif "{{" in value:
            errors.append(f"{path.name}: {name} still has a placeholder; finish /research-challenge:init-skills")
        else:
            clean[name] = value.strip()
    if errors:
        raise InputError(errors)
    return Profile(
        name=clean["company.name"],
        ticker=clean["company.ticker"],
        currency=clean["accounting.reporting_currency"],
        units=clean["accounting.units"],
        framework=clean["accounting.framework"],
    )


def load_financials(path: Path) -> tuple[dict[str, dict[int, Observation]], tuple[int, ...], list[str]]:
    if not path.is_file():
        raise InputError([f"data/{path.name} not found: run the financials skill first"])
    errors: list[str] = []
    warnings: list[str] = []
    raw: dict[str, dict[int, Observation]] = {}
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [c for c in FIN_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise InputError([f"financials.csv is missing columns: {', '.join(missing)}"])
        for number, row in enumerate(reader, start=2):
            _read_row(number, row, raw, errors, warnings)
    years = sorted({year for series in raw.values() for year in series})
    if len(years) < MIN_HIST_YEARS:
        errors.append(f"financials.csv needs at least {MIN_HIST_YEARS} years of history; found {len(years)}")
        raise InputError(errors)
    hist_years = tuple(years[-MAX_HIST_YEARS:])
    for key in sorted(REQUIRED_KEYS):
        absent = [str(y) for y in hist_years if y not in raw.get(key, {})]
        if absent:
            errors.append(f"required line '{key}' is missing for {', '.join(absent)}")
    if errors:
        raise InputError(errors)
    history = {key: {y: o for y, o in series.items() if y in hist_years} for key, series in raw.items()}
    return history, hist_years, warnings


def _read_row(number: int, row: Mapping[str, str | None], raw: dict[str, dict[int, Observation]],
              errors: list[str], warnings: list[str]) -> None:
    key = (row.get("line_item") or "").strip()
    if key not in BY_KEY and not key.startswith(SEGMENT_PREFIX):
        errors.append(f"row {number}: unknown line_item '{key}'")
        return
    try:
        year = int((row.get("year") or "").strip())
        value = float((row.get("value") or "").strip())
    except ValueError:
        errors.append(f"row {number}: year and value must be plain numbers (no thousands separators)")
        return
    if not math.isfinite(value):
        errors.append(f"row {number}: value must be a finite number")
        return
    tag = (row.get("tag") or "").strip()
    if tag not in TAGS:
        errors.append(f"row {number}: tag '{tag}' must be one of {', '.join(sorted(TAGS))}")
        return
    series = raw.setdefault(key, {})
    if year in series:
        errors.append(f"row {number}: duplicate {key} for {year}")
        return
    if tag == "unverified":
        warnings.append(f"{key} {year} is tagged [unverified]; resolve it before the report")
    series[year] = Observation(value, tag, (row.get("source_doc") or "").strip(), (row.get("page") or "").strip())


def load_drivers(path: Path, history: Mapping[str, Mapping[int, Observation]], hist_years: tuple[int, ...]
                 ) -> tuple[dict[str, DriverInput], tuple[Segment, ...], int, list[str]]:
    if not path.is_file():
        return {}, (), DEFAULT_FCST_YEARS, [
            "model/drivers.yaml not found: every driver held at its last actual value (run the forecast skill)"
        ]
    doc = _mapping(_read_yaml(path), "drivers.yaml")
    n_fcst = doc.get("forecast_years", DEFAULT_FCST_YEARS)
    if isinstance(n_fcst, bool) or not isinstance(n_fcst, int) or not 1 <= n_fcst <= MAX_FCST_YEARS:
        raise InputError([f"drivers.yaml: forecast_years must be a whole number from 1 to {MAX_FCST_YEARS}"])
    errors: list[str] = []
    warnings: list[str] = []
    segments = _read_segments(doc.get("revenue_segments"), history, hist_years, errors)
    allowed = set(DRIVER_KEYS) | {f"{SEGMENT_PREFIX}{s.key}_growth" for s in segments}
    drivers: dict[str, DriverInput] = {}
    for key, entry in _mapping(doc.get("drivers", {}), "drivers.yaml > drivers").items():
        if key not in allowed:
            errors.append(f"drivers.yaml: unknown driver '{key}'")
            continue
        parsed = _read_driver(key, entry, n_fcst, errors)
        if parsed is not None:
            drivers[key] = parsed
    if errors:
        raise InputError(errors)
    for key in sorted(allowed - drivers.keys()):
        if key == "revenue_growth" and segments:
            continue
        default = "zero" if key in ZERO_DEFAULT_DRIVERS else "held at last actual value"
        warnings.append(f"driver '{key}' not set: {default} (engine default)")
    if segments and "revenue_growth" in drivers:
        warnings.append("revenue_growth is ignored because revenue_segments are set")
    return drivers, segments, n_fcst, warnings


def _read_driver(key: str, entry: object, n_fcst: int, errors: list[str]) -> DriverInput | None:
    if not isinstance(entry, dict):
        errors.append(f"drivers.yaml: '{key}' must have values, tag, rationale")
        return None
    values = entry.get("values")
    if not isinstance(values, list) or len(values) != n_fcst or not all(_is_number(v) for v in values):
        errors.append(f"drivers.yaml: '{key}' needs exactly {n_fcst} numeric values")
        return None
    tag = str(entry.get("tag", "assumption"))
    if tag not in TAGS:
        errors.append(f"drivers.yaml: '{key}' tag '{tag}' must be one of {', '.join(sorted(TAGS))}")
        return None
    return DriverInput(tuple(float(v) for v in values), tag, str(entry.get("rationale", "")), str(entry.get("pillar", "")))


def _read_segments(raw: object, history: Mapping[str, Mapping[int, Observation]], hist_years: tuple[int, ...],
                   errors: list[str]) -> tuple[Segment, ...]:
    if raw is None:
        return ()
    if not isinstance(raw, list):
        errors.append("drivers.yaml: revenue_segments must be a list")
        return ()
    segments: list[Segment] = []
    for item in raw:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str):
            errors.append("drivers.yaml: each revenue segment needs a key and a label")
            continue
        key = item["key"].strip()
        if not key.replace("_", "").isalnum():
            errors.append(f"drivers.yaml: segment key '{key}' must use letters, digits or _")
            continue
        line = f"{SEGMENT_PREFIX}{key}"
        absent = [str(y) for y in hist_years if y not in history.get(line, {})]
        if absent:
            errors.append(f"financials.csv: segment line '{line}' is missing for {', '.join(absent)}")
            continue
        segments.append(Segment(key, str(item.get("label", key))))
    return tuple(segments)


def load_valuation(path: Path) -> Valuation | None:
    if not path.is_file():
        return None
    doc = _mapping(_read_yaml(path), "valuation.yaml")
    wacc = _mapping(doc.get("wacc"), "valuation.yaml > wacc")
    terminal = _mapping(doc.get("terminal"), "valuation.yaml > terminal")
    errors: list[str] = []

    def number(section: Mapping[str, Any], name: str, where: str) -> float:
        raw = section.get(name)
        if not _is_number(raw):
            errors.append(f"valuation.yaml: {where}{name} must be a number")
            return math.nan
        return float(raw)

    w = {f: number(wacc, f, "wacc.") for f in WACC_FIELDS}
    t = {f: number(terminal, f, "terminal.") for f in TERMINAL_FIELDS}
    price = number(doc, "share_price", "")
    low = number(doc, "price_52w_low", "")
    high = number(doc, "price_52w_high", "")
    peers: list[Peer] = []
    raw_peers = doc.get("peers") or []
    if not isinstance(raw_peers, list):
        errors.append("valuation.yaml: peers must be a list")
        raw_peers = []
    for i, entry in enumerate(raw_peers, start=1):
        if not isinstance(entry, dict):
            errors.append(f"valuation.yaml: peer {i} must be a mapping")
            continue
        where = f"peers[{i}]."
        peers.append(Peer(
            name=str(entry.get("name", f"Peer {i}")),
            ticker=str(entry.get("ticker", "")),
            price=number(entry, "price", where),
            shares=number(entry, "shares", where),
            net_debt=number(entry, "net_debt", where),
            ebitda_fwd=number(entry, "ebitda_fwd", where),
            eps_fwd=number(entry, "eps_fwd", where),
        ))
    target = doc.get("target_price")
    if target is not None and not _is_number(target):
        errors.append("valuation.yaml: target_price must be a number or null")
    mid_year = doc.get("mid_year", True)
    if not isinstance(mid_year, bool):
        errors.append("valuation.yaml: mid_year must be true or false")
    if errors:
        raise InputError(errors)
    return Valuation(
        share_price=price, price_52w_low=low, price_52w_high=high,
        risk_free=w["risk_free"], equity_risk_premium=w["equity_risk_premium"],
        country_risk_premium=w["country_risk_premium"], beta_unlevered=w["beta_unlevered"],
        target_debt_to_equity=w["target_debt_to_equity"], pre_tax_cost_of_debt=w["pre_tax_cost_of_debt"],
        tax_rate=w["tax_rate"], terminal_growth=t["growth"], exit_ev_ebitda=t["exit_ev_ebitda"],
        lt_nominal_gdp_growth=t["lt_nominal_gdp_growth"], mid_year=bool(mid_year), peers=tuple(peers),
        target_price=float(target) if _is_number(target) else None,
    )


def _collect(errors: list[str], load: Callable[[], T]) -> T | None:
    try:
        return load()
    except InputError as exc:
        errors.extend(exc.messages)
        return None


def _read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except yaml.YAMLError as exc:
        raise InputError([f"{path.name} is not valid YAML: {exc}"]) from None


def _mapping(obj: object, where: str) -> dict[str, Any]:
    if not isinstance(obj, dict):
        raise InputError([f"{where} must be a mapping (key: value)"])
    return obj


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)
```

- [ ] **Step 5: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests/test_inputs.py`
Expected: `14 passed`

- [ ] **Step 6: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/chart.py skills/model/engine/rcmodel/inputs.py skills/model/engine/tests/test_inputs.py
git commit -m "feat(engine): canonical chart and validated input loading"
```

---

### Task 4: Layout types, placement and the evaluator (`spec.py`, `placement.py`, `engine.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/spec.py`
- Create: `skills/model/engine/rcmodel/placement.py`
- Create: `skills/model/engine/rcmodel/engine.py`
- Test: `skills/model/engine/tests/test_engine.py`

- [ ] **Step 1: Write the failing tests** — `tests/test_engine.py`

```python
from __future__ import annotations

from pathlib import Path

import pytest

from rcmodel.engine import BlankCell, FormulaCell, InputCell, Model, ModelError, ObservedCell
from rcmodel.expr import At, Ref
from rcmodel.inputs import load_inputs
from rcmodel.placement import FIRST_ROW, LayoutError, place
from rcmodel.spec import OBSERVED, Header, Inputs, Line


def _tiny(project: Path, extra: list[Line] | None = None) -> Model:
    inputs = load_inputs(project)
    growth = tuple(0.1 for _ in inputs.fcst_years)
    layout = [
        Header("IS", "Tiny"),
        Line("revenue", "Revenue", "IS", hist=OBSERVED, fcst=Ref("revenue", 1) * (1 + Ref("g"))),
        Line("g", "Growth", "Drivers", hist=Ref("revenue") / Ref("revenue", 1) - 1, fcst=Inputs(growth)),
        Line("peak", "Peak revenue", "DCF", scalar=At("revenue", inputs.n - 1)),
        *(extra or []),
    ]
    return Model(layout, inputs)


def test_values_follow_the_formulas(project: Path) -> None:
    m = _tiny(project)
    assert m.value("revenue", 4) == 13400
    assert m.value("revenue", 5) == pytest.approx(13400 * 1.1)
    assert m.value("peak", None) == pytest.approx(13400 * 1.1**5)


def test_cells_by_kind(project: Path) -> None:
    m = _tiny(project)
    observed = m.cell("revenue", 0)
    assert isinstance(observed, ObservedCell)
    assert "sourced" in observed.comment and "p.45" in observed.comment
    assert isinstance(m.cell("g", 5), InputCell)
    assert isinstance(m.cell("g", 0), BlankCell)  # needs revenue of the year before the first
    assert isinstance(m.cell("g", 1), FormulaCell)


def test_addresses(project: Path) -> None:
    m = _tiny(project)
    row = m.row_of("revenue")
    assert row == FIRST_ROW + 1
    assert m.address("revenue", 0, "IS") == f"C{row}"
    assert m.address("revenue", 5, "Drivers") == f"IS!H{row}"
    assert m.range_address("revenue", 5, 9, "DCF") == f"IS!H{row}:L{row}"
    assert m.address("peak", None, "DCF") == f"C{m.row_of('peak')}"


def test_formula_renders_with_addresses(project: Path) -> None:
    m = _tiny(project)
    cell = m.cell("revenue", 5)
    assert isinstance(cell, FormulaCell)
    assert cell.expr.render(m, 5, "IS") == f"G{m.row_of('revenue')}*(1+Drivers!H{m.row_of('g')})"


def test_unknown_reference(project: Path) -> None:
    m = _tiny(project, [Line("bad", "Bad", "IS", fcst=Ref("nope"))])
    with pytest.raises(ModelError, match="unknown line 'nope'"):
        m.evaluate_all()


def test_circular_reference(project: Path) -> None:
    m = _tiny(project, [Line("x", "X", "IS", fcst=Ref("y")), Line("y", "Y", "IS", fcst=Ref("x"))])
    with pytest.raises(ModelError, match="circular"):
        m.evaluate_all()


def test_single_value_formulas_must_use_at(project: Path) -> None:
    m = _tiny(project, [Line("oops", "Oops", "DCF", scalar=Ref("revenue"))])
    with pytest.raises(ModelError, match="At"):
        m.evaluate_all()


def test_duplicate_keys_rejected() -> None:
    with pytest.raises(LayoutError):
        place([Line("a", "A", "IS"), Line("a", "A", "IS")])


def test_headers_leave_a_breathing_row() -> None:
    placed = place([Header("IS", "One"), Line("a", "A", "IS"), Header("IS", "Two"), Line("b", "B", "IS")])
    rows = {line.key: row for line, row in placed.lines}
    assert rows == {"a": FIRST_ROW + 1, "b": FIRST_ROW + 4}


def test_continuation_lines_share_a_row() -> None:
    placed = place([Line("a", "A", "Comps", scalar=1.0, col=3), Line("b", "", "Comps", scalar=2.0, col=4, new_row=False)])
    assert placed.placements["a"].row == placed.placements["b"].row
    assert placed.placements["b"].col == 4


def test_line_cannot_be_both_kinds() -> None:
    with pytest.raises(ValueError):
        Line("x", "X", "IS", scalar=1.0, fcst=Ref("y"))
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_engine.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.engine'`.

- [ ] **Step 3: Implement `rcmodel/spec.py`**

```python
"""Model definition types: lines, headers and how each cell is filled."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias, Union

from .expr import Expr


class Fmt(Enum):
    """Excel number formats."""

    MONEY = '#,##0.0_);(#,##0.0);"-"_)'
    PCT = "0.0%"
    MULT = '0.0"x"'
    DAYS = "0"
    PRICE = "#,##0.00"
    SHARES = "#,##0.0"
    NUMBER = "0.00"


class Style(Enum):
    NORMAL = "normal"
    SUBTOTAL = "subtotal"
    TOTAL = "total"


@dataclass(frozen=True)
class Observed:
    """Fill historical cells with the reported value from data/financials.csv."""


OBSERVED = Observed()


@dataclass(frozen=True)
class Inputs:
    """Hard-coded forecast inputs, one per forecast year (blue cells)."""

    values: tuple[float, ...]


CellSpec: TypeAlias = Union[Expr, Observed, Inputs, None]


@dataclass(frozen=True)
class Line:
    """One model row. Per-year lines fill one cell per year; scalar lines fill a single cell."""

    key: str
    label: str
    sheet: str
    fmt: Fmt = Fmt.MONEY
    style: Style = Style.NORMAL
    hist: CellSpec = None
    fcst: CellSpec = None
    scalar: Expr | float | None = None
    col: int = 3
    new_row: bool = True
    notes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.scalar is not None and (self.hist is not None or self.fcst is not None):
            raise ValueError(f"line '{self.key}' cannot be both a single value and per-year")
        if isinstance(self.hist, Inputs):
            raise ValueError(f"line '{self.key}': Inputs are for forecast years only")

    @property
    def is_scalar(self) -> bool:
        return self.scalar is not None


@dataclass(frozen=True)
class Header:
    """A section band. `columns` puts column titles in the band row: ((col, text), ...)."""

    sheet: str
    title: str
    columns: tuple[tuple[int, str], ...] = ()


LayoutItem: TypeAlias = Union[Line, Header]
```

- [ ] **Step 4: Implement `rcmodel/placement.py`**

```python
"""Assign every line a sheet row (and a column for single values)."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from .spec import Header, LayoutItem, Line

HEADER_ROW = 4
FIRST_ROW = 6
PERIOD_COL0 = 3


class LayoutError(Exception):
    """The model definition is inconsistent (duplicate keys, bad row flags)."""


@dataclass(frozen=True)
class Placement:
    sheet: str
    row: int
    col: int | None  # None = one column per year, starting at PERIOD_COL0


@dataclass(frozen=True)
class Placed:
    placements: dict[str, Placement]
    headers: tuple[tuple[str, int, Header], ...]
    lines: tuple[tuple[Line, int], ...]


def place(layout: Sequence[LayoutItem]) -> Placed:
    next_row: dict[str, int] = {}
    placements: dict[str, Placement] = {}
    headers: list[tuple[str, int, Header]] = []
    lines: list[tuple[Line, int]] = []
    for item in layout:
        row = next_row.get(item.sheet, FIRST_ROW)
        if isinstance(item, Header):
            if row > FIRST_ROW:
                row += 1
            headers.append((item.sheet, row, item))
            next_row[item.sheet] = row + 1
            continue
        if item.key in placements:
            raise LayoutError(f"duplicate line key '{item.key}'")
        if item.new_row:
            next_row[item.sheet] = row + 1
        else:
            if row == FIRST_ROW:
                raise LayoutError(f"line '{item.key}' continues a row but is first on {item.sheet}")
            row -= 1
        placements[item.key] = Placement(item.sheet, row, item.col if item.is_scalar else None)
        lines.append((item, row))
    return Placed(placements, tuple(headers), tuple(lines))
```

- [ ] **Step 5: Implement `rcmodel/engine.py`**

```python
"""Evaluate the model in Python and resolve cell addresses for Excel formulas."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import TypeAlias, Union

from openpyxl.utils import get_column_letter

from .expr import Expr
from .inputs import ModelInputs
from .placement import PERIOD_COL0, Placement, place
from .spec import Inputs, LayoutItem, Line, Observed


class ModelError(Exception):
    """A formula references something that does not exist or loops back on itself."""


@dataclass(frozen=True)
class ObservedCell:
    value: float
    comment: str


@dataclass(frozen=True)
class InputCell:
    value: float


@dataclass(frozen=True)
class FormulaCell:
    expr: Expr


@dataclass(frozen=True)
class BlankCell:
    pass


BLANK = BlankCell()
Cell: TypeAlias = Union[ObservedCell, InputCell, FormulaCell, BlankCell]


class Model:
    """The evaluated model; implements the expr.Context protocol."""

    def __init__(self, layout: Sequence[LayoutItem], inputs: ModelInputs) -> None:
        self.inputs = inputs
        self.placed = place(layout)
        self.lines: dict[str, Line] = {line.key: line for line, _ in self.placed.lines}
        self._cache: dict[tuple[str, int | None], float] = {}
        self._visiting: set[tuple[str, int | None]] = set()

    @property
    def h(self) -> int:
        return self.inputs.h

    @property
    def n(self) -> int:
        return self.inputs.n

    def has(self, key: str) -> bool:
        return key in self.lines

    def line(self, key: str) -> Line:
        try:
            return self.lines[key]
        except KeyError:
            raise ModelError(f"unknown line '{key}'") from None

    def sheet_of(self, key: str) -> str:
        return self._placement(key).sheet

    def row_of(self, key: str) -> int:
        return self._placement(key).row

    def cell(self, key: str, period: int | None) -> Cell:
        line = self.line(key)
        if line.scalar is not None:
            scalar = line.scalar
            return FormulaCell(scalar) if isinstance(scalar, Expr) else InputCell(float(scalar))
        if period is None:
            raise ModelError(f"'{key}' is a per-year line; a single-value formula must use At()")
        spec = line.hist if period < self.h else line.fcst
        if spec is None:
            return BLANK
        if isinstance(spec, Observed):
            return self._observed(key, period)
        if isinstance(spec, Inputs):
            return InputCell(spec.values[period - self.h])
        if period - spec.max_lag() < 0:
            return BLANK
        return FormulaCell(spec)

    def value(self, key: str, period: int | None) -> float:
        line = self.line(key)
        slot: int | None = None
        if line.scalar is None:
            if period is None:
                raise ModelError(f"'{key}' is a per-year line; a single-value formula must use At()")
            if not 0 <= period < self.n:
                raise ModelError(f"'{key}' referenced outside the model years (period {period})")
            slot = period
        cache_key = (key, slot)
        if cache_key in self._cache:
            return self._cache[cache_key]
        if cache_key in self._visiting:
            raise ModelError(f"circular reference through '{key}'")
        self._visiting.add(cache_key)
        try:
            result = self._compute(key, slot)
        finally:
            self._visiting.discard(cache_key)
        self._cache[cache_key] = result
        return result

    def address(self, key: str, period: int | None, from_sheet: str) -> str:
        placement = self._placement(key)
        if placement.col is not None:
            col = placement.col
        elif period is None:
            raise ModelError(f"'{key}' is a per-year line; a single-value formula must use At()")
        else:
            col = PERIOD_COL0 + period
        ref = f"{get_column_letter(col)}{placement.row}"
        return ref if placement.sheet == from_sheet else f"{placement.sheet}!{ref}"

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str:
        placement = self._placement(key)
        if placement.col is not None:
            raise ModelError(f"'{key}' is a single value, not a range")
        start = f"{get_column_letter(PERIOD_COL0 + first)}{placement.row}"
        end = f"{get_column_letter(PERIOD_COL0 + last)}{placement.row}"
        span = f"{start}:{end}"
        return span if placement.sheet == from_sheet else f"{placement.sheet}!{span}"

    def evaluate_all(self) -> None:
        """Evaluate every cell once, so broken references and cycles fail before writing."""
        for key, line in self.lines.items():
            periods: Sequence[int | None] = [None] if line.is_scalar else range(self.n)
            for period in periods:
                self.value(key, period)

    def _placement(self, key: str) -> Placement:
        try:
            return self.placed.placements[key]
        except KeyError:
            raise ModelError(f"unknown line '{key}'") from None

    def _observed(self, key: str, period: int) -> ObservedCell:
        year = self.inputs.hist_years[period]
        point = self.inputs.history.get(key, {}).get(year)
        if point is None:
            return ObservedCell(0.0, f"{key} {year}: not reported, set to 0")
        page = f" p.{point.page}" if point.page else ""
        return ObservedCell(point.value, f"[{point.tag}] {point.source_doc}{page}")

    def _compute(self, key: str, slot: int | None) -> float:
        cell = self.cell(key, slot)
        if isinstance(cell, (ObservedCell, InputCell)):
            return cell.value
        if isinstance(cell, FormulaCell):
            return cell.expr.evaluate(self, slot)
        return 0.0  # blank cells read as zero, exactly as in Excel
```

- [ ] **Step 6: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests/test_engine.py`
Expected: `11 passed`

- [ ] **Step 7: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/spec.py skills/model/engine/rcmodel/placement.py skills/model/engine/rcmodel/engine.py skills/model/engine/tests/test_engine.py
git commit -m "feat(engine): layout types, row placement and lazy evaluator with cycle detection"
```

---

### Task 5: Three statements, schedules, drivers and ratios (`lines.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/lines.py`
- Test: `skills/model/engine/tests/test_model.py`

- [ ] **Step 1: Write the failing tests** — `tests/test_model.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

import pytest

from conftest import DRIVERS, HISTORY, SEGMENTS, write_project
from rcmodel.chart import DRIVER_KEYS
from rcmodel.engine import BlankCell, FormulaCell, Model
from rcmodel.inputs import load_inputs
from rcmodel.lines import DRIVER_DEFS, model_layout


def _model(project: Path) -> Model:
    inputs = load_inputs(project)
    model = Model(model_layout(inputs), inputs)
    model.evaluate_all()
    return model


def _with_driver(tmp_path: Path, key: str, values: list[float]) -> Model:
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"][key]["values"] = values
    return _model(write_project(tmp_path, drivers=drivers))


def test_driver_definitions_cover_every_driver_key() -> None:
    assert tuple(d.key for d in DRIVER_DEFS) == DRIVER_KEYS


def test_balance_sheet_balances_every_year(project: Path) -> None:
    m = _model(project)
    for t in range(m.n):
        assert m.value("total_assets", t) == pytest.approx(m.value("total_liabilities_equity", t), abs=1e-6)


def test_history_matches_reported_totals(project: Path) -> None:
    m = _model(project)
    for t in range(m.h):
        assert m.value("total_assets", t) == HISTORY["total_assets_reported"][t]
        assert m.value("net_income", t) == HISTORY["net_income_reported"][t]


def test_forecast_cash_ties_to_cash_flow(project: Path) -> None:
    m = _model(project)
    for t in range(m.h, m.n):
        assert m.value("cash", t) == pytest.approx(m.value("cash_end", t))


def test_revenue_follows_growth_driver(project: Path) -> None:
    m = _model(project)
    assert m.value("revenue", m.h) == pytest.approx(13400 * 1.07)
    assert m.value("cogs", m.h) == pytest.approx(13400 * 1.07 * 0.59)


def test_interest_uses_opening_debt(project: Path) -> None:
    m = _model(project)
    opening_debt = m.value("total_debt", m.h - 1)
    assert m.value("interest_expense", m.h) == pytest.approx(0.075 * opening_debt)


def test_no_revolver_in_base_case(project: Path) -> None:
    m = _model(project)
    for t in range(m.h, m.n):
        assert m.value("revolver", t) == pytest.approx(0.0, abs=1e-9)
        assert m.value("cash", t) >= 1500


def test_revolver_funds_a_cash_shortfall(tmp_path: Path) -> None:
    m = _with_driver(tmp_path, "payout_ratio", [3.0] * 5)
    assert m.value("revolver", m.h) > 0
    for t in range(m.h, m.n):
        assert m.value("cash", t) == pytest.approx(1500)
        assert m.value("total_assets", t) == pytest.approx(m.value("total_liabilities_equity", t), abs=1e-6)


def test_revolver_is_repaid_when_cash_returns(tmp_path: Path) -> None:
    m = _with_driver(tmp_path, "payout_ratio", [3.0, 0.0, 0.0, 0.0, 0.0])
    assert m.value("revolver", m.n - 1) < m.value("revolver", m.h)
    assert m.value("revolver", m.n - 1) >= 0


def test_missing_driver_is_held_at_last_actual(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    del drivers["drivers"]["gross_margin"]
    m = _model(write_project(tmp_path, drivers=drivers))
    assert isinstance(m.cell("gross_margin", m.h), FormulaCell)
    assert m.value("gross_margin", m.h) == pytest.approx(5500 / 13400)


def test_segments_drive_revenue(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["revenue_segments"] = [{"key": "mx", "label": "Mexico"}, {"key": "us", "label": "United States"}]
    drivers["drivers"]["seg_mx_growth"] = {"values": [0.08] * 5, "tag": "assumption"}
    drivers["drivers"]["seg_us_growth"] = {"values": [0.04] * 5, "tag": "assumption"}
    m = _model(write_project(tmp_path, history={**HISTORY, **SEGMENTS}, drivers=drivers))
    assert m.value("revenue", m.h) == pytest.approx(8000 * 1.08 + 5400 * 1.04)


def test_first_year_lagged_formulas_are_blank(project: Path) -> None:
    m = _model(project)
    assert isinstance(m.cell("change_nwc", 0), BlankCell)
    assert isinstance(m.cell("interest_rate_debt", 0), BlankCell)


def test_ratios_are_computed(project: Path) -> None:
    m = _model(project)
    assert m.value("r_gross_margin", m.h - 1) == pytest.approx(5500 / 13400)
    assert m.value("r_ccc", m.h) == pytest.approx(43 + 50 - 55)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_model.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.lines'`.

- [ ] **Step 3: Implement `rcmodel/lines.py`**

```python
"""Model definition for Drivers, IS, BS, CF, Schedules and Ratios.

Sign convention: costs, capex, taxes and dividends are positive and formulas
subtract them. Interest is charged on opening balances, so there are no
circular references. A revolver keeps cash at or above the minimum balance.
D&A reduces PP&E only; intangibles, other non-current items, short-term debt
and leases are held flat.
"""

from __future__ import annotations

from dataclasses import dataclass

from .chart import SEGMENT_PREFIX, ZERO_DEFAULT_DRIVERS
from .expr import At, Expr, Num, Ref, fn
from .inputs import ModelInputs
from .spec import OBSERVED, CellSpec, Fmt, Header, Inputs, LayoutItem, Line, Style

R = Ref
DRV, IS, BS, CF, SCH, RAT = "Drivers", "IS", "BS", "CF", "Schedules", "Ratios"
DAYS_IN_YEAR = 365


def _growth(key: str) -> Expr:
    return R(key) / R(key, 1) - 1


@dataclass(frozen=True)
class DriverDef:
    key: str
    label: str
    fmt: Fmt
    hist: Expr  # the historical value of the driver, shown next to the forecast inputs


DRIVER_DEFS: tuple[DriverDef, ...] = (
    DriverDef("revenue_growth", "Revenue growth", Fmt.PCT, _growth("revenue")),
    DriverDef("gross_margin", "Gross margin", Fmt.PCT, R("gross_profit") / R("revenue")),
    DriverDef("opex_pct_revenue", "Operating expenses / revenue", Fmt.PCT, R("opex") / R("revenue")),
    DriverDef("da_pct_revenue", "D&A / revenue", Fmt.PCT, R("da") / R("revenue")),
    DriverDef("capex_pct_revenue", "Capex / revenue", Fmt.PCT, R("capex") / R("revenue")),
    DriverDef("dso", "Receivable days (DSO)", Fmt.DAYS, R("receivables") / R("revenue") * DAYS_IN_YEAR),
    DriverDef("dio", "Inventory days (DIO)", Fmt.DAYS, R("inventory") / R("cogs") * DAYS_IN_YEAR),
    DriverDef("dpo", "Payable days (DPO)", Fmt.DAYS, R("payables") / R("cogs") * DAYS_IN_YEAR),
    DriverDef("other_ca_pct_revenue", "Other current assets / revenue", Fmt.PCT, R("other_current_assets") / R("revenue")),
    DriverDef("other_cl_pct_revenue", "Other current liabilities / revenue", Fmt.PCT, R("other_current_liabilities") / R("revenue")),
    DriverDef("tax_rate", "Effective tax rate", Fmt.PCT, R("income_tax") / R("ebt")),
    DriverDef("interest_rate_debt", "Interest rate on opening debt", Fmt.PCT, R("interest_expense") / R("total_debt", 1)),
    DriverDef("interest_rate_cash", "Interest rate on opening cash", Fmt.PCT, R("interest_income") / R("cash", 1)),
    DriverDef("payout_ratio", "Dividend payout ratio", Fmt.PCT, R("dividends_paid") / R("net_income_parent")),
    DriverDef("nci_share", "Non-controlling share of net income", Fmt.PCT, R("nci_income") / R("net_income")),
    DriverDef("net_new_debt", "Net new long-term debt", Fmt.MONEY, R("debt_long") - R("debt_long", 1)),
    DriverDef("shares_growth", "Diluted share count growth", Fmt.PCT, _growth("shares_diluted")),
    DriverDef("min_cash", "Minimum cash balance", Fmt.MONEY, R("cash")),
)


def model_layout(inputs: ModelInputs) -> list[LayoutItem]:
    return [
        *driver_layout(inputs),
        *income_statement(inputs),
        *balance_sheet(inputs),
        *cash_flow(),
        *schedules(inputs),
        *ratios(),
    ]


def _driver_line(key: str, label: str, fmt: Fmt, hist: Expr, inputs: ModelInputs) -> Line:
    given = inputs.drivers.get(key)
    fcst: CellSpec
    if given is not None:
        fcst = Inputs(given.values)
        notes = (given.tag, given.rationale, given.pillar)
    elif key in ZERO_DEFAULT_DRIVERS:
        fcst = Inputs(tuple(0.0 for _ in inputs.fcst_years))
        notes = ("assumption", "engine default: zero", "")
    else:
        fcst = At(key, inputs.h - 1)
        notes = ("assumption", "engine default: held at last actual", "")
    return Line(key, label, DRV, fmt, hist=hist, fcst=fcst, notes=notes)


def driver_layout(inputs: ModelInputs) -> list[LayoutItem]:
    n = inputs.n
    columns = ((3 + n, "Tag"), (4 + n, "Rationale"), (5 + n, "Thesis pillar"))
    items: list[LayoutItem] = [Header(DRV, "Operating drivers", columns=columns)]
    items += [_driver_line(d.key, d.label, d.fmt, d.hist, inputs) for d in DRIVER_DEFS]
    if inputs.segments:
        items.append(Header(DRV, "Revenue segments"))
        for segment in inputs.segments:
            line = f"{SEGMENT_PREFIX}{segment.key}"
            items.append(_driver_line(f"{line}_growth", f"{segment.label} growth", Fmt.PCT, _growth(line), inputs))
    return items


def _both(key: str, label: str, sheet: str, expr: Expr, fmt: Fmt = Fmt.MONEY, style: Style = Style.NORMAL) -> Line:
    return Line(key, label, sheet, fmt, style=style, hist=expr, fcst=expr)


def income_statement(inputs: ModelInputs) -> list[LayoutItem]:
    revenue_fcst: Expr
    if inputs.segments:
        revenue_fcst = fn("SUM", *[R(f"{SEGMENT_PREFIX}{s.key}") for s in inputs.segments])
    else:
        revenue_fcst = R("revenue", 1) * (1 + R("revenue_growth"))
    zeros = Inputs(tuple(0.0 for _ in inputs.fcst_years))
    items: list[LayoutItem] = [
        Header(IS, "Income statement"),
        Line("revenue", "Revenue", IS, style=Style.SUBTOTAL, hist=OBSERVED, fcst=revenue_fcst),
        Line("cogs", "Cost of sales", IS, hist=OBSERVED, fcst=R("revenue") * (1 - R("gross_margin"))),
        _both("gross_profit", "Gross profit", IS, R("revenue") - R("cogs"), style=Style.SUBTOTAL),
        Line("opex", "Operating expenses (net)", IS, hist=OBSERVED, fcst=R("revenue") * R("opex_pct_revenue")),
        _both("ebit", "EBIT", IS, R("gross_profit") - R("opex"), style=Style.SUBTOTAL),
        Line("interest_expense", "Interest expense", IS, hist=OBSERVED, fcst=R("sch_interest_expense")),
        Line("interest_income", "Interest income", IS, hist=OBSERVED, fcst=R("interest_rate_cash") * R("cash", 1)),
        Line("other_financial_net", "Other financial result, net", IS, hist=OBSERVED, fcst=zeros,
             notes=("assumption: held at zero",)),
        _both("ebt", "Pre-tax income", IS,
              R("ebit") - R("interest_expense") + R("interest_income") + R("other_financial_net"), style=Style.SUBTOTAL),
        Line("income_tax", "Income tax", IS, hist=OBSERVED, fcst=R("ebt") * R("tax_rate")),
        _both("net_income", "Net income", IS, R("ebt") - R("income_tax"), style=Style.TOTAL),
        Line("nci_income", "Attributable to non-controlling interests", IS, hist=OBSERVED,
             fcst=R("net_income") * R("nci_share")),
        _both("net_income_parent", "Net income to shareholders", IS, R("net_income") - R("nci_income"), style=Style.TOTAL),
        Header(IS, "Per share and memo"),
        Line("shares_diluted", "Diluted shares", IS, Fmt.SHARES, hist=OBSERVED,
             fcst=R("shares_diluted", 1) * (1 + R("shares_growth"))),
        _both("eps", "Diluted EPS", IS, R("net_income_parent") / R("shares_diluted"), fmt=Fmt.PRICE),
        Line("da", "D&A (included in costs above)", IS, hist=OBSERVED, fcst=R("revenue") * R("da_pct_revenue")),
        _both("ebitda", "EBITDA", IS, R("ebit") + R("da"), style=Style.SUBTOTAL),
    ]
    if "net_income_reported" in inputs.history:
        items.append(Line("net_income_reported", "Net income as reported (check)", IS, hist=OBSERVED))
    return items


def balance_sheet(inputs: ModelInputs) -> list[LayoutItem]:
    items: list[LayoutItem] = [
        Header(BS, "Assets"),
        Line("cash", "Cash and equivalents", BS, hist=OBSERVED, fcst=R("cash_end")),
        Line("receivables", "Accounts receivable", BS, hist=OBSERVED, fcst=R("sch_receivables")),
        Line("inventory", "Inventories", BS, hist=OBSERVED, fcst=R("sch_inventory")),
        Line("other_current_assets", "Other current assets", BS, hist=OBSERVED,
             fcst=R("revenue") * R("other_ca_pct_revenue")),
        _both("total_current_assets", "Total current assets", BS,
              R("cash") + R("receivables") + R("inventory") + R("other_current_assets"), style=Style.SUBTOTAL),
        Line("ppe_net", "PP&E and right-of-use assets, net", BS, hist=OBSERVED, fcst=R("sch_ppe_end")),
        Line("intangibles_goodwill", "Intangibles and goodwill", BS, hist=OBSERVED, fcst=R("intangibles_goodwill", 1)),
        Line("other_noncurrent_assets", "Other non-current assets", BS, hist=OBSERVED,
             fcst=R("other_noncurrent_assets", 1)),
        _both("total_assets", "Total assets", BS,
              R("total_current_assets") + R("ppe_net") + R("intangibles_goodwill") + R("other_noncurrent_assets"),
              style=Style.TOTAL),
        Header(BS, "Liabilities and equity"),
        Line("payables", "Accounts payable", BS, hist=OBSERVED, fcst=R("sch_payables")),
        Line("other_current_liabilities", "Other current liabilities", BS, hist=OBSERVED,
             fcst=R("revenue") * R("other_cl_pct_revenue")),
        Line("debt_short", "Short-term debt", BS, hist=OBSERVED, fcst=R("debt_short", 1)),
        Line("revolver", "Revolving credit facility", BS, hist=Num(0.0), fcst=R("sch_revolver_end")),
        _both("total_current_liabilities", "Total current liabilities", BS,
              R("payables") + R("other_current_liabilities") + R("debt_short") + R("revolver"), style=Style.SUBTOTAL),
        Line("debt_long", "Long-term debt", BS, hist=OBSERVED, fcst=R("sch_debt_long_end")),
        Line("lease_liabilities", "Lease liabilities", BS, hist=OBSERVED, fcst=R("lease_liabilities", 1)),
        Line("other_noncurrent_liabilities", "Other non-current liabilities", BS, hist=OBSERVED,
             fcst=R("other_noncurrent_liabilities", 1)),
        _both("total_liabilities", "Total liabilities", BS,
              R("total_current_liabilities") + R("debt_long") + R("lease_liabilities") + R("other_noncurrent_liabilities"),
              style=Style.SUBTOTAL),
        Line("equity_parent", "Shareholders' equity", BS, hist=OBSERVED,
             fcst=R("equity_parent", 1) + R("net_income_parent") - R("dividends_paid")),
        Line("nci_equity", "Non-controlling interests", BS, hist=OBSERVED, fcst=R("nci_equity", 1) + R("nci_income")),
        _both("total_equity", "Total equity", BS, R("equity_parent") + R("nci_equity"), style=Style.SUBTOTAL),
        _both("total_liabilities_equity", "Total liabilities and equity", BS,
              R("total_liabilities") + R("total_equity"), style=Style.TOTAL),
        Header(BS, "Memo"),
        _both("total_debt", "Total debt incl. leases and revolver", BS,
              R("debt_short") + R("revolver") + R("debt_long") + R("lease_liabilities")),
        _both("net_debt", "Net debt", BS, R("total_debt") - R("cash")),
    ]
    if "total_assets_reported" in inputs.history:
        items.append(Line("total_assets_reported", "Total assets as reported (check)", BS, hist=OBSERVED))
    return items


def cash_flow() -> list[LayoutItem]:
    def change(key: str) -> Expr:
        return R(key) - R(key, 1)

    nwc = -(change("receivables") + change("inventory") + change("other_current_assets")
            - change("payables") - change("other_current_liabilities"))
    return [
        Header(CF, "Operating activities"),
        Line("cf_net_income", "Net income", CF, fcst=R("net_income")),
        Line("cf_da", "D&A", CF, fcst=R("da")),
        _both("change_nwc", "Change in working capital", CF, nwc),
        Line("cfo", "Cash flow from operations", CF, style=Style.SUBTOTAL, hist=OBSERVED,
             fcst=R("cf_net_income") + R("cf_da") + R("change_nwc")),
        Header(CF, "Investing activities"),
        Line("capex", "Capital expenditures", CF, hist=OBSERVED, fcst=R("revenue") * R("capex_pct_revenue")),
        Line("cfi", "Cash flow from investing", CF, style=Style.SUBTOTAL, fcst=-R("capex")),
        Header(CF, "Financing activities"),
        Line("cf_net_new_debt", "Net debt issued / (repaid)", CF, fcst=R("net_new_debt")),
        Line("dividends_paid", "Dividends paid", CF, hist=OBSERVED, fcst=R("net_income_parent") * R("payout_ratio")),
        Line("cff_before_revolver", "Cash flow from financing before revolver", CF, style=Style.SUBTOTAL,
             fcst=R("cf_net_new_debt") - R("dividends_paid")),
        Header(CF, "Cash and revolver"),
        Line("cash_begin", "Opening cash", CF, fcst=R("cash", 1)),
        Line("cash_before_revolver", "Cash before revolver", CF,
             fcst=R("cash_begin") + R("cfo") + R("cfi") + R("cff_before_revolver")),
        Line("revolver_draw", "Revolver draw / (repayment)", CF,
             fcst=fn("MAX", R("min_cash") - R("cash_before_revolver"), -R("revolver", 1))),
        Line("cash_end", "Closing cash", CF, style=Style.TOTAL, fcst=R("cash_before_revolver") + R("revolver_draw")),
        Header(CF, "Memo"),
        _both("fcf", "Free cash flow (CFO - capex)", CF, R("cfo") - R("capex")),
    ]


def schedules(inputs: ModelInputs) -> list[LayoutItem]:
    items: list[LayoutItem] = []
    if inputs.segments:
        items.append(Header(SCH, "Revenue build"))
        for segment in inputs.segments:
            line = f"{SEGMENT_PREFIX}{segment.key}"
            items.append(Line(line, segment.label, SCH, hist=OBSERVED, fcst=R(line, 1) * (1 + R(f"{line}_growth"))))
        items.append(_both("sch_revenue_total", "Total revenue (links to IS)", SCH, R("revenue"), style=Style.SUBTOTAL))
    items += [
        Header(SCH, "PP&E roll-forward"),
        Line("sch_ppe_begin", "Opening PP&E", SCH, fcst=R("ppe_net", 1)),
        Line("sch_capex", "Plus: capex", SCH, fcst=R("capex")),
        Line("sch_da", "Less: D&A", SCH, fcst=R("da")),
        Line("sch_ppe_end", "Closing PP&E", SCH, style=Style.TOTAL,
             fcst=R("sch_ppe_begin") + R("sch_capex") - R("sch_da")),
        Header(SCH, "Working capital"),
        Line("sch_receivables", "Receivables = revenue x DSO / 365", SCH, fcst=R("revenue") * R("dso") / DAYS_IN_YEAR),
        Line("sch_inventory", "Inventories = cost of sales x DIO / 365", SCH, fcst=R("cogs") * R("dio") / DAYS_IN_YEAR),
        Line("sch_payables", "Payables = cost of sales x DPO / 365", SCH, fcst=R("cogs") * R("dpo") / DAYS_IN_YEAR),
        Header(SCH, "Debt and interest"),
        Line("sch_debt_long_begin", "Opening long-term debt", SCH, fcst=R("debt_long", 1)),
        Line("sch_net_new_debt", "Plus: net new debt", SCH, fcst=R("net_new_debt")),
        Line("sch_debt_long_end", "Closing long-term debt", SCH, style=Style.TOTAL,
             fcst=R("sch_debt_long_begin") + R("sch_net_new_debt")),
        Line("sch_revolver_begin", "Opening revolver", SCH, fcst=R("revolver", 1)),
        Line("sch_revolver_draw", "Plus: draw / (repayment)", SCH, fcst=R("revolver_draw")),
        Line("sch_revolver_end", "Closing revolver", SCH, style=Style.TOTAL,
             fcst=R("sch_revolver_begin") + R("sch_revolver_draw")),
        Line("sch_interest_expense", "Interest expense = rate x opening total debt", SCH,
             fcst=R("interest_rate_debt") * R("total_debt", 1)),
    ]
    return items


def ratios() -> list[LayoutItem]:
    average_equity = (R("equity_parent") + R("equity_parent", 1)) / 2
    return [
        Header(RAT, "Growth and margins"),
        _both("r_revenue_growth", "Revenue growth", RAT, _growth("revenue"), fmt=Fmt.PCT),
        _both("r_gross_margin", "Gross margin", RAT, R("gross_profit") / R("revenue"), fmt=Fmt.PCT),
        _both("r_ebitda_margin", "EBITDA margin", RAT, R("ebitda") / R("revenue"), fmt=Fmt.PCT),
        _both("r_ebit_margin", "EBIT margin", RAT, R("ebit") / R("revenue"), fmt=Fmt.PCT),
        _both("r_net_margin", "Net margin", RAT, R("net_income_parent") / R("revenue"), fmt=Fmt.PCT),
        _both("r_fcf_margin", "Free cash flow margin", RAT, R("fcf") / R("revenue"), fmt=Fmt.PCT),
        Header(RAT, "Returns"),
        _both("r_roe", "Return on average equity", RAT, R("net_income_parent") / average_equity, fmt=Fmt.PCT),
        _both("r_roic", "ROIC = EBIT x (1 - tax rate) / (equity + net debt)", RAT,
              R("ebit") * (1 - R("tax_rate")) / (R("total_equity") + R("net_debt")), fmt=Fmt.PCT),
        Header(RAT, "Leverage and working capital"),
        _both("r_net_debt_ebitda", "Net debt / EBITDA", RAT, R("net_debt") / R("ebitda"), fmt=Fmt.MULT),
        _both("r_interest_cover", "EBIT / interest expense", RAT, R("ebit") / R("interest_expense"), fmt=Fmt.MULT),
        _both("r_ccc", "Cash conversion cycle (days) = DSO + DIO - DPO", RAT, R("dso") + R("dio") - R("dpo"),
              fmt=Fmt.DAYS),
    ]
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests/test_model.py`
Expected: `13 passed`

If `test_balance_sheet_balances_every_year` fails in forecast years only, compare the change in total assets with the change in liabilities plus equity for the first forecast year line by line; do not add a plug line.

- [ ] **Step 5: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/lines.py skills/model/engine/tests/test_model.py
git commit -m "feat(engine): three statements, schedules, drivers and ratios"
```

---

### Task 6: Valuation (`valuation.py`, `assemble.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/valuation.py`
- Create: `skills/model/engine/rcmodel/assemble.py`
- Test: `skills/model/engine/tests/test_valuation.py`

- [ ] **Step 1: Write the failing tests** — `tests/test_valuation.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

import pytest

from conftest import VALUATION, write_project
from rcmodel.assemble import assemble
from rcmodel.engine import Model
from rcmodel.inputs import load_inputs
from rcmodel.valuation import FootballSpec


def _full(project: Path) -> tuple[Model, FootballSpec | None]:
    return assemble(load_inputs(project))


def _with_valuation(tmp_path: Path, name: str, **changes: object) -> Model:
    valuation = copy.deepcopy(VALUATION)
    for dotted, value in changes.items():
        section, _, field = dotted.partition("__")
        if field:
            valuation[section][field] = value
        else:
            valuation[section] = value
    model, _ = _full(write_project(tmp_path / name, valuation=valuation))
    return model


def test_wacc_matches_hand_calculation(project: Path) -> None:
    m, _ = _full(project)
    beta_levered = 0.8 * (1 + (1 - 0.30) * 0.4)
    cost_of_equity = 0.09 + beta_levered * 0.055 + 0.0
    expected = cost_of_equity / 1.4 + 0.10 * (1 - 0.30) * 0.4 / 1.4
    assert m.value("wacc", None) == pytest.approx(expected)


def test_fcff_definition(project: Path) -> None:
    m, _ = _full(project)
    for t in range(m.h, m.n):
        expected = (m.value("ebit", t) * (1 - m.value("tax_rate", t)) + m.value("da", t)
                    - m.value("capex", t) + m.value("change_nwc", t))
        assert m.value("fcff", t) == pytest.approx(expected)


def test_gordon_price_matches_manual_dcf(project: Path) -> None:
    m, _ = _full(project)
    w, g = m.value("wacc", None), 0.04
    fcff = [m.value("fcff", t) for t in range(m.h, m.n)]
    present_value = sum(f / (1 + w) ** (i + 0.5) for i, f in enumerate(fcff))
    terminal = fcff[-1] * (1 + g) / (w - g) / (1 + w) ** len(fcff)
    equity = present_value + terminal - m.value("net_debt", m.h - 1) - m.value("nci_equity", m.h - 1)
    assert m.value("price_gordon", None) == pytest.approx(equity / m.value("shares_diluted", m.h - 1))


def test_sensitivity_center_equals_base_price(project: Path) -> None:
    m, _ = _full(project)
    assert m.value("sens_2_2", None) == pytest.approx(m.value("price_gordon", None), rel=1e-9)


def test_reverse_dcf_recovers_terminal_growth(tmp_path: Path) -> None:
    base, _ = _full(write_project(tmp_path / "base"))
    m = _with_valuation(tmp_path, "priced", share_price=base.value("price_gordon", None))
    assert m.value("implied_g", None) == pytest.approx(0.04, abs=1e-9)


def test_exit_at_implied_multiple_equals_gordon(tmp_path: Path) -> None:
    base, _ = _full(write_project(tmp_path / "base"))
    m = _with_valuation(tmp_path, "exit", terminal__exit_ev_ebitda=base.value("implied_exit_multiple", None))
    assert m.value("price_exit", None) == pytest.approx(m.value("price_gordon", None))


def test_comps_medians_and_prices(project: Path) -> None:
    m, _ = _full(project)
    assert m.value("comps_ev_ebitda_median", None) == pytest.approx(26000 / 3800)
    assert m.value("comps_pe_median", None) == pytest.approx(12.5)
    assert m.value("price_comps_pe", None) == pytest.approx(12.5 * m.value("eps", m.h))


def test_football_rows_bracket_the_dcf(project: Path) -> None:
    m, football = _full(project)
    assert football == FootballSpec("ff_dcf_low", "ff_price_low")
    assert m.value("ff_dcf_low", None) <= m.value("price_gordon", None) <= m.value("ff_dcf_high", None)


def test_target_price_row_when_set(tmp_path: Path) -> None:
    valuation = copy.deepcopy(VALUATION)
    valuation["target_price"] = 31.0
    m, football = _full(write_project(tmp_path, valuation=valuation))
    assert football is not None and football.last_row_key == "ff_target_low"
    assert m.value("ff_target_high", None) == 31.0


def test_no_valuation_file_means_no_valuation(tmp_path: Path) -> None:
    m, football = _full(write_project(tmp_path, valuation=None))
    assert not m.has("wacc")
    assert football is None


def test_no_peers_means_no_comps(tmp_path: Path) -> None:
    m = _with_valuation(tmp_path, "nopeers", peers=[])
    assert not m.has("comps_pe_median")
    assert not m.has("ff_pe_low")
    assert m.has("price_gordon")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_valuation.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.assemble'`.

- [ ] **Step 3: Implement `rcmodel/valuation.py`**

```python
"""Valuation sheets: WACC, DCF (Gordon and exit multiple), reverse DCF, comps,
sensitivity and football field. Valuation is as of the last fiscal year-end."""

from __future__ import annotations

from dataclasses import dataclass

from .expr import At, Expr, Ref, Rng, fn
from .inputs import ModelInputs, Valuation
from .spec import Fmt, Header, Inputs, LayoutItem, Line, Style

R = Ref
WACC_S, DCF_S, COMPS_S, SENS_S, FF_S = "WACC", "DCF", "Comps", "Sensitivity", "Football"
WACC_STEPS: tuple[float, ...] = (-0.02, -0.01, 0.0, 0.01, 0.02)
G_STEPS: tuple[float, ...] = (-0.01, -0.005, 0.0, 0.005, 0.01)
EXIT_STEP = 1.0
FROM_FILE = "input from valuation/valuation.yaml"


@dataclass(frozen=True)
class FootballSpec:
    """First and last 'low' cells of the football-field table (the chart's data range)."""

    first_row_key: str
    last_row_key: str


def _input(key: str, label: str, sheet: str, value: float, fmt: Fmt, note: str = FROM_FILE) -> Line:
    return Line(key, label, sheet, fmt, scalar=value, notes=(note,))


def _calc(key: str, label: str, sheet: str, expr: Expr, fmt: Fmt = Fmt.MONEY, style: Style = Style.NORMAL) -> Line:
    return Line(key, label, sheet, fmt, style=style, scalar=expr)


def valuation_layout(inputs: ModelInputs) -> tuple[list[LayoutItem], FootballSpec | None]:
    v = inputs.valuation
    if v is None:
        return [], None
    football_items, football = football_layout(inputs, v)
    items = [*wacc_layout(v), *dcf_layout(inputs, v), *comps_layout(inputs, v), *sensitivity_layout(inputs, v),
             *football_items]
    return items, football


def wacc_layout(v: Valuation) -> list[LayoutItem]:
    return [
        Header(WACC_S, "Cost of capital inputs"),
        _input("v_rf", "Risk-free rate", WACC_S, v.risk_free, Fmt.PCT),
        _input("v_erp", "Equity risk premium", WACC_S, v.equity_risk_premium, Fmt.PCT),
        _input("v_crp", "Country risk premium", WACC_S, v.country_risk_premium, Fmt.PCT),
        _input("v_beta_u", "Unlevered beta", WACC_S, v.beta_unlevered, Fmt.NUMBER),
        _input("v_de", "Target debt / equity", WACC_S, v.target_debt_to_equity, Fmt.NUMBER),
        _input("v_kd", "Pre-tax cost of debt", WACC_S, v.pre_tax_cost_of_debt, Fmt.PCT),
        _input("v_tax", "Marginal tax rate", WACC_S, v.tax_rate, Fmt.PCT),
        Header(WACC_S, "Cost of capital"),
        _calc("v_beta_l", "Relevered beta = unlevered x (1 + (1 - tax) x D/E)", WACC_S,
              R("v_beta_u") * (1 + (1 - R("v_tax")) * R("v_de")), Fmt.NUMBER),
        _calc("v_ke", "Cost of equity = rf + beta x ERP + CRP", WACC_S,
              R("v_rf") + R("v_beta_l") * R("v_erp") + R("v_crp"), Fmt.PCT),
        _calc("v_kd_after", "After-tax cost of debt", WACC_S, R("v_kd") * (1 - R("v_tax")), Fmt.PCT),
        _calc("v_we", "Equity weight = 1 / (1 + D/E)", WACC_S, 1 / (1 + R("v_de")), Fmt.PCT),
        _calc("v_wd", "Debt weight = D/E / (1 + D/E)", WACC_S, R("v_de") / (1 + R("v_de")), Fmt.PCT),
        _calc("wacc", "WACC", WACC_S, R("v_we") * R("v_ke") + R("v_wd") * R("v_kd_after"), Fmt.PCT, Style.TOTAL),
    ]


def dcf_layout(inputs: ModelInputs, v: Valuation) -> list[LayoutItem]:
    h, last = inputs.h, inputs.n - 1
    years = inputs.n - inputs.h
    offset = 0.5 if v.mid_year else 0.0
    periods = Inputs(tuple(float(i) - offset for i in range(1, years + 1)))
    period_label = "Discount period (years, mid-year)" if v.mid_year else "Discount period (years)"
    last_fcff, last_ebitda = At("fcff", last), At("ebitda", last)
    return [
        Header(DCF_S, "Free cash flow to the firm"),
        Line("dcf_ebit", "EBIT", DCF_S, fcst=R("ebit")),
        Line("dcf_tax", "Less: taxes on EBIT", DCF_S, fcst=R("dcf_ebit") * R("tax_rate")),
        Line("dcf_nopat", "NOPAT", DCF_S, style=Style.SUBTOTAL, fcst=R("dcf_ebit") - R("dcf_tax")),
        Line("dcf_da", "Plus: D&A", DCF_S, fcst=R("da")),
        Line("dcf_capex", "Less: capex", DCF_S, fcst=R("capex")),
        Line("dcf_nwc", "Plus: change in working capital", DCF_S, fcst=R("change_nwc")),
        Line("fcff", "Free cash flow to the firm", DCF_S, style=Style.TOTAL,
             fcst=R("dcf_nopat") + R("dcf_da") - R("dcf_capex") + R("dcf_nwc")),
        Line("dcf_period", period_label, DCF_S, Fmt.NUMBER, fcst=periods,
             notes=("mechanical: year number, minus 0.5 with the mid-year convention",)),
        Line("dcf_df", "Discount factor", DCF_S, Fmt.NUMBER, fcst=1 / (1 + R("wacc")) ** R("dcf_period")),
        Line("dcf_pv", "Present value of FCFF", DCF_S, fcst=R("fcff") * R("dcf_df")),
        Header(DCF_S, "Terminal value and enterprise value (single values in column C)"),
        _input("terminal_growth", "Terminal growth (g)", DCF_S, v.terminal_growth, Fmt.PCT),
        _input("exit_multiple", "Exit EV / EBITDA multiple", DCF_S, v.exit_ev_ebitda, Fmt.MULT),
        _input("lt_gdp", "Long-term nominal GDP growth (cap for g)", DCF_S, v.lt_nominal_gdp_growth, Fmt.PCT),
        _calc("sum_pv", "Sum of PV of FCFF", DCF_S, fn("SUM", Rng("dcf_pv", h, last))),
        _calc("tv_gordon", "Terminal value - Gordon growth", DCF_S,
              last_fcff * (1 + R("terminal_growth")) / (R("wacc") - R("terminal_growth"))),
        _calc("pv_tv_gordon", "PV of terminal value - Gordon", DCF_S, R("tv_gordon") / (1 + R("wacc")) ** years),
        _calc("ev_gordon", "Enterprise value - Gordon", DCF_S, R("sum_pv") + R("pv_tv_gordon"), style=Style.SUBTOTAL),
        _calc("tv_exit", "Terminal value - exit multiple", DCF_S, last_ebitda * R("exit_multiple")),
        _calc("pv_tv_exit", "PV of terminal value - exit multiple", DCF_S, R("tv_exit") / (1 + R("wacc")) ** years),
        _calc("ev_exit", "Enterprise value - exit multiple", DCF_S, R("sum_pv") + R("pv_tv_exit"), style=Style.SUBTOTAL),
        Header(DCF_S, "Equity value per share"),
        _calc("net_debt_val", "Net debt (last actual)", DCF_S, At("net_debt", h - 1)),
        _calc("nci_val", "Non-controlling interests (last actual)", DCF_S, At("nci_equity", h - 1)),
        _calc("shares_val", "Diluted shares (last actual)", DCF_S, At("shares_diluted", h - 1), Fmt.SHARES),
        _calc("price_gordon", "Value per share - Gordon", DCF_S,
              (R("ev_gordon") - R("net_debt_val") - R("nci_val")) / R("shares_val"), Fmt.PRICE, Style.TOTAL),
        _calc("price_exit", "Value per share - exit multiple", DCF_S,
              (R("ev_exit") - R("net_debt_val") - R("nci_val")) / R("shares_val"), Fmt.PRICE, Style.TOTAL),
        _input("share_price", "Current share price", DCF_S, v.share_price, Fmt.PRICE),
        _calc("upside_gordon", "Upside / (downside) - Gordon", DCF_S, R("price_gordon") / R("share_price") - 1, Fmt.PCT),
        _calc("upside_exit", "Upside / (downside) - exit multiple", DCF_S, R("price_exit") / R("share_price") - 1, Fmt.PCT),
        Header(DCF_S, "Cross-checks"),
        _calc("tv_share_gordon", "Terminal value share of EV - Gordon", DCF_S, R("pv_tv_gordon") / R("ev_gordon"), Fmt.PCT),
        _calc("implied_exit_multiple", "Exit multiple implied by Gordon", DCF_S, R("tv_gordon") / last_ebitda, Fmt.MULT),
        _calc("implied_g_exit", "Growth implied by the exit multiple", DCF_S,
              (R("tv_exit") * R("wacc") - last_fcff) / (R("tv_exit") + last_fcff), Fmt.PCT),
        Header(DCF_S, "Reverse DCF - what the market price implies"),
        _calc("market_ev", "Market EV = price x shares + net debt + NCI", DCF_S,
              R("share_price") * R("shares_val") + R("net_debt_val") + R("nci_val")),
        _calc("implied_tv", "Terminal value implied by the market", DCF_S,
              (R("market_ev") - R("sum_pv")) * (1 + R("wacc")) ** years),
        _calc("implied_g", "Terminal growth implied by the market price", DCF_S,
              (R("implied_tv") * R("wacc") - last_fcff) / (R("implied_tv") + last_fcff), Fmt.PCT),
    ]


def _ev_price(multiple: Expr) -> Expr:
    return (multiple * R("company_ebitda_next") - R("net_debt_val") - R("nci_val")) / R("shares_val")


def comps_layout(inputs: ModelInputs, v: Valuation) -> list[LayoutItem]:
    if not v.peers:
        return []
    columns = ((3, "Price"), (4, "Shares"), (5, "Net debt"), (6, "EBITDA next yr"), (7, "EPS next yr"),
               (8, "EV"), (9, "EV / EBITDA"), (10, "P / E"))
    items: list[LayoutItem] = [Header(COMPS_S, "Peer multiples", columns=columns)]
    for i, peer in enumerate(v.peers):
        k = f"peer_{i}"
        items += [
            Line(f"{k}_price", f"{peer.name} ({peer.ticker})", COMPS_S, Fmt.PRICE, scalar=peer.price, col=3),
            Line(f"{k}_shares", "", COMPS_S, Fmt.SHARES, scalar=peer.shares, col=4, new_row=False),
            Line(f"{k}_net_debt", "", COMPS_S, Fmt.MONEY, scalar=peer.net_debt, col=5, new_row=False),
            Line(f"{k}_ebitda", "", COMPS_S, Fmt.MONEY, scalar=peer.ebitda_fwd, col=6, new_row=False),
            Line(f"{k}_eps", "", COMPS_S, Fmt.PRICE, scalar=peer.eps_fwd, col=7, new_row=False),
            Line(f"{k}_ev", "", COMPS_S, Fmt.MONEY, col=8, new_row=False,
                 scalar=R(f"{k}_price") * R(f"{k}_shares") + R(f"{k}_net_debt")),
            Line(f"{k}_ev_ebitda", "", COMPS_S, Fmt.MULT, col=9, new_row=False, scalar=R(f"{k}_ev") / R(f"{k}_ebitda")),
            Line(f"{k}_pe", "", COMPS_S, Fmt.MULT, col=10, new_row=False, scalar=R(f"{k}_price") / R(f"{k}_eps")),
        ]
    ev_multiples = [R(f"peer_{i}_ev_ebitda") for i in range(len(v.peers))]
    pe_multiples = [R(f"peer_{i}_pe") for i in range(len(v.peers))]
    items += [
        Header(COMPS_S, "Implied value per share"),
        _calc("comps_ev_ebitda_median", "Median EV / EBITDA", COMPS_S, fn("MEDIAN", *ev_multiples), Fmt.MULT),
        _calc("comps_ev_ebitda_min", "Lowest EV / EBITDA", COMPS_S, fn("MIN", *ev_multiples), Fmt.MULT),
        _calc("comps_ev_ebitda_max", "Highest EV / EBITDA", COMPS_S, fn("MAX", *ev_multiples), Fmt.MULT),
        _calc("comps_pe_median", "Median P / E", COMPS_S, fn("MEDIAN", *pe_multiples), Fmt.MULT),
        _calc("comps_pe_min", "Lowest P / E", COMPS_S, fn("MIN", *pe_multiples), Fmt.MULT),
        _calc("comps_pe_max", "Highest P / E", COMPS_S, fn("MAX", *pe_multiples), Fmt.MULT),
        _calc("company_ebitda_next", "Company EBITDA next year", COMPS_S, At("ebitda", inputs.h)),
        _calc("company_eps_next", "Company EPS next year", COMPS_S, At("eps", inputs.h), Fmt.PRICE),
        _calc("price_comps_ev_ebitda", "Value per share at median EV / EBITDA", COMPS_S,
              _ev_price(R("comps_ev_ebitda_median")), Fmt.PRICE, Style.TOTAL),
        _calc("price_comps_pe", "Value per share at median P / E", COMPS_S,
              R("comps_pe_median") * R("company_eps_next"), Fmt.PRICE, Style.TOTAL),
    ]
    return items


def _price_at(w: Expr, g: Expr, first: int, last: int, years: int, mid_year: bool) -> Expr:
    """Gordon value per share at WACC w and growth g, written as one self-contained formula."""
    present_value: Expr = fn("NPV", w, Rng("fcff", first, last))
    if mid_year:
        present_value = present_value * (1 + w) ** 0.5
    terminal = At("fcff", last) * (1 + g) / (w - g) / (1 + w) ** years
    return (present_value + terminal - R("net_debt_val") - R("nci_val")) / R("shares_val")


def sensitivity_layout(inputs: ModelInputs, v: Valuation) -> list[LayoutItem]:
    first, last, years = inputs.h, inputs.n - 1, inputs.n - inputs.h
    items: list[LayoutItem] = [
        Header(SENS_S, "Value per share (Gordon): WACC down the side, terminal growth across")
    ]
    for j, step in enumerate(G_STEPS):
        items.append(Line(f"sens_g_{j}", "Terminal growth ->" if j == 0 else "", SENS_S, Fmt.PCT,
                          scalar=R("terminal_growth") + step, col=4 + j, new_row=(j == 0)))
    for i, step in enumerate(WACC_STEPS):
        items.append(Line(f"sens_w_{i}", "WACC" if i == 0 else "", SENS_S, Fmt.PCT, scalar=R("wacc") + step, col=3))
        for j in range(len(G_STEPS)):
            items.append(Line(f"sens_{i}_{j}", "", SENS_S, Fmt.PRICE, col=4 + j, new_row=False,
                              scalar=_price_at(R(f"sens_w_{i}"), R(f"sens_g_{j}"), first, last, years, v.mid_year)))
    return items


def _exit_price(multiple: Expr, last: int, years: int) -> Expr:
    terminal = At("ebitda", last) * multiple / (1 + R("wacc")) ** years
    return (R("sum_pv") + terminal - R("net_debt_val") - R("nci_val")) / R("shares_val")


def football_layout(inputs: ModelInputs, v: Valuation) -> tuple[list[LayoutItem], FootballSpec]:
    last, years = inputs.n - 1, inputs.n - inputs.h
    grid = [R(f"sens_{i}_{j}") for i in range(len(WACC_STEPS)) for j in range(len(G_STEPS))]
    rows: list[tuple[str, str, Expr | float, Expr | float]] = [
        ("dcf", "DCF - Gordon (sensitivity range)", fn("MIN", *grid), fn("MAX", *grid)),
        ("exit", "DCF - exit multiple +/- 1.0x",
         _exit_price(R("exit_multiple") - EXIT_STEP, last, years), _exit_price(R("exit_multiple") + EXIT_STEP, last, years)),
    ]
    if v.peers:
        rows += [
            ("ev_ebitda", "Comps - EV / EBITDA (peer range)",
             _ev_price(R("comps_ev_ebitda_min")), _ev_price(R("comps_ev_ebitda_max"))),
            ("pe", "Comps - P / E (peer range)",
             R("comps_pe_min") * R("company_eps_next"), R("comps_pe_max") * R("company_eps_next")),
        ]
    rows += [
        ("52w", "52-week trading range", v.price_52w_low, v.price_52w_high),
        ("price", "Current share price", R("share_price"), R("share_price")),
    ]
    if v.target_price is not None:
        rows.append(("target", "Team target price", v.target_price, v.target_price))
    items: list[LayoutItem] = [
        Header(FF_S, "Valuation summary (football field)", columns=((3, "Low"), (4, "High"), (5, "Spread")))
    ]
    for key, label, low, high in rows:
        items += [
            Line(f"ff_{key}_low", label, FF_S, Fmt.PRICE, scalar=low, col=3),
            Line(f"ff_{key}_high", "", FF_S, Fmt.PRICE, scalar=high, col=4, new_row=False),
            Line(f"ff_{key}_spread", "", FF_S, Fmt.PRICE, col=5, new_row=False,
                 scalar=R(f"ff_{key}_high") - R(f"ff_{key}_low")),
        ]
    return items, FootballSpec(f"ff_{rows[0][0]}_low", f"ff_{rows[-1][0]}_low")
```

- [ ] **Step 4: Implement `rcmodel/assemble.py`**

```python
"""Put the model together: statements plus the optional valuation, fully evaluated."""

from __future__ import annotations

from .engine import Model
from .inputs import ModelInputs
from .lines import model_layout
from .valuation import FootballSpec, valuation_layout


def assemble(inputs: ModelInputs) -> tuple[Model, FootballSpec | None]:
    valuation_items, football = valuation_layout(inputs)
    model = Model([*model_layout(inputs), *valuation_items], inputs)
    model.evaluate_all()
    return model, football
```

- [ ] **Step 5: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests/test_valuation.py`
Expected: `11 passed`

- [ ] **Step 6: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/valuation.py skills/model/engine/rcmodel/assemble.py skills/model/engine/tests/test_valuation.py
git commit -m "feat(engine): WACC, DCF with dual terminal value, reverse DCF, comps, sensitivity, football field"
```

---

### Task 7: Integrity and parity checks (`checks.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/checks.py`
- Test: `skills/model/engine/tests/test_checks.py`

- [ ] **Step 1: Write the failing tests** — `tests/test_checks.py`

```python
from __future__ import annotations

import copy
from pathlib import Path

from conftest import HISTORY, VALUATION, write_project
from rcmodel.assemble import assemble
from rcmodel.checks import CheckResult, build_checks, evaluate_checks, overall_status, parity_checks
from rcmodel.inputs import load_inputs


def _results(project: Path) -> list[CheckResult]:
    model, _ = assemble(load_inputs(project))
    return evaluate_checks(model, [*build_checks(model.inputs), *parity_checks(model)])


def _status(results: list[CheckResult], key: str, period: int | None) -> str:
    return next(r.status for r in results if r.key == key and r.period == period)


def test_fixture_has_no_errors(project: Path) -> None:
    results = _results(project)
    assert [r for r in results if r.status == "ERROR"] == []
    assert any(r.key == "parity_price_gordon" for r in results)


def test_reported_total_assets_mismatch_is_flagged(tmp_path: Path) -> None:
    history = dict(HISTORY)
    history["total_assets_reported"] = (11900, 12350, 12900, 13450, 14150)
    results = _results(write_project(tmp_path, history=history))
    assert _status(results, "tie_total_assets", 4) == "ERROR"
    assert _status(results, "tie_total_assets", 3) == "OK"


def test_unbalanced_history_is_flagged(tmp_path: Path) -> None:
    history = dict(HISTORY)
    history["cash"] = (1500, 1600, 1750, 1900, 2150)
    results = _results(write_project(tmp_path, history=history))
    assert _status(results, "bs_balances", 4) == "ERROR"
    assert _status(results, "bs_balances", 3) == "OK"


def test_terminal_value_share_warns(tmp_path: Path) -> None:
    valuation = copy.deepcopy(VALUATION)
    valuation["terminal"]["growth"] = 0.07
    results = _results(write_project(tmp_path, valuation=valuation))
    assert _status(results, "tv_share", None) == "WARN"
    assert overall_status(results) == "OK WITH WARNINGS"


def test_growth_above_gdp_is_an_error(tmp_path: Path) -> None:
    valuation = copy.deepcopy(VALUATION)
    valuation["terminal"]["lt_nominal_gdp_growth"] = 0.03
    results = _results(write_project(tmp_path, valuation=valuation))
    assert _status(results, "g_le_gdp", None) == "ERROR"
    assert overall_status(results) == "CHECKS FAILING"


def test_overall_status_all_ok() -> None:
    ok = CheckResult("a", "A", None, "OK")
    assert overall_status([ok]) == "ALL CHECKS OK"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_checks.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.checks'`.

- [ ] **Step 3: Implement `rcmodel/checks.py`**

```python
"""Integrity checks, written to the Checks sheet as Excel formulas and evaluated in Python.

Parity checks compare an Excel formula with the value Python computed at build
time; they can only fail inside Excel, which is exactly what they are for.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum

from .engine import Model
from .expr import At, Expr, Ref, cmp, fn, wrap
from .inputs import ModelInputs

R = Ref
TOLERANCE = 0.5  # half a unit of the model currency (e.g. MXN 0.5 million)
TV_SHARE_LIMIT = 0.75


class Severity(Enum):
    ERROR = "ERROR"
    WARN = "WARN"


@dataclass(frozen=True)
class Check:
    key: str
    label: str
    severity: Severity
    cond: Expr
    periods: tuple[int, ...] | None  # None = single-value check


@dataclass(frozen=True)
class CheckResult:
    key: str
    label: str
    period: int | None
    status: str  # "OK", "ERROR" or "WARN"


def _close(a: Expr, b: Expr, tolerance: float = TOLERANCE) -> Expr:
    return cmp(fn("ABS", a - b), "<=", tolerance)


def build_checks(inputs: ModelInputs) -> list[Check]:
    all_years = tuple(range(inputs.n))
    forecast = tuple(range(inputs.h, inputs.n))
    checks = [
        Check("bs_balances", "Balance sheet balances (assets = liabilities + equity)", Severity.ERROR,
              _close(R("total_assets"), R("total_liabilities_equity")), all_years),
        Check("cash_ties", "Cash-flow closing cash = balance-sheet cash", Severity.ERROR,
              _close(R("cash_end"), R("cash")), forecast),
        Check("equity_roll", "Equity roll-forward (opening + net income - dividends)", Severity.ERROR,
              _close(R("equity_parent"), R("equity_parent", 1) + R("net_income_parent") - R("dividends_paid")), forecast),
        Check("revolver_positive", "Revolver balance is not negative", Severity.ERROR,
              cmp(R("revolver"), ">=", -0.001), forecast),
        Check("min_cash", "Cash at or above the minimum balance", Severity.ERROR,
              cmp(R("cash"), ">=", R("min_cash") - TOLERANCE), forecast),
    ]
    for key, computed, label in (
        ("total_assets_reported", "total_assets", "Total assets tie to the reported figure"),
        ("net_income_reported", "net_income", "Net income ties to the reported figure"),
    ):
        series = inputs.history.get(key)
        if series:
            periods = tuple(i for i, year in enumerate(inputs.hist_years) if year in series)
            checks.append(Check(f"tie_{computed}", label, Severity.ERROR, _close(R(computed), R(key)), periods))
    if inputs.segments:
        segments = fn("SUM", *[R(f"seg_{s.key}") for s in inputs.segments])
        checks.append(Check("segments_tie", "Revenue segments add up to revenue", Severity.ERROR,
                            _close(segments, R("revenue")), tuple(range(inputs.h))))
    if inputs.valuation is not None:
        checks += [
            Check("wacc_gt_g", "WACC is above terminal growth", Severity.ERROR,
                  cmp(R("wacc"), ">", R("terminal_growth")), None),
            Check("g_le_gdp", "Terminal growth at or below long-term nominal GDP growth", Severity.ERROR,
                  cmp(R("terminal_growth"), "<=", R("lt_gdp")), None),
            Check("tv_share", "Terminal value is below 75% of enterprise value (Gordon)", Severity.WARN,
                  cmp(R("tv_share_gordon"), "<=", TV_SHARE_LIMIT), None),
        ]
    return checks


def parity_checks(model: Model) -> list[Check]:
    """Excel must reproduce the Python value of a few key cells."""
    last = model.n - 1
    targets: list[tuple[str, int | None]] = [("total_assets", last), ("net_income_parent", last), ("cash_end", last)]
    if model.has("price_gordon"):
        targets += [("wacc", None), ("price_gordon", None)]
    checks: list[Check] = []
    for key, period in targets:
        value = model.value(key, period)
        if not math.isfinite(value):
            continue
        ref: Expr = At(key, period) if period is not None else R(key)
        tolerance = 1e-6 * max(1.0, abs(value))
        checks.append(Check(f"parity_{key}", f"Excel matches the Python value: {model.line(key).label}",
                            Severity.ERROR, _close(ref, wrap(value), tolerance), None))
    return checks


def evaluate_checks(model: Model, checks: Sequence[Check]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for check in checks:
        for period in check.periods if check.periods is not None else (None,):
            ok = check.cond.evaluate(model, period) != 0.0
            results.append(CheckResult(check.key, check.label, period, "OK" if ok else check.severity.value))
    return results


def overall_status(results: Sequence[CheckResult]) -> str:
    statuses = {r.status for r in results}
    if "ERROR" in statuses:
        return "CHECKS FAILING"
    if "WARN" in statuses:
        return "OK WITH WARNINGS"
    return "ALL CHECKS OK"
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests/test_checks.py`
Expected: `6 passed`

- [ ] **Step 5: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/checks.py skills/model/engine/tests/test_checks.py
git commit -m "feat(engine): integrity and Excel-parity checks"
```

---

### Task 8: Workbook writer (`styles.py`, `writer.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/styles.py`
- Create: `skills/model/engine/rcmodel/writer.py`
- Test: `skills/model/engine/tests/test_writer.py`
- Test: `skills/model/engine/tests/test_workbook_parity.py`

- [ ] **Step 1: Write the failing writer tests** — `tests/test_writer.py`

```python
from __future__ import annotations

import zipfile
from datetime import date
from pathlib import Path

from openpyxl import load_workbook

from conftest import write_project
from rcmodel.assemble import assemble
from rcmodel.checks import build_checks, evaluate_checks, parity_checks
from rcmodel.engine import Model
from rcmodel.inputs import load_inputs
from rcmodel.writer import BuildInfo, write_workbook


def build_file(project: Path) -> tuple[Path, Model]:
    model, football = assemble(load_inputs(project))
    checks = [*build_checks(model.inputs), *parity_checks(model)]
    path = project / "model" / "TEST.xlsx"
    write_workbook(path, model, checks, evaluate_checks(model, checks), football,
                   BuildInfo(1, path.name, date(2026, 9, 23)))
    return path, model


def test_sheets_in_order(project: Path) -> None:
    path, _ = build_file(project)
    assert load_workbook(path).sheetnames == [
        "Cover", "Drivers", "IS", "BS", "CF", "Schedules", "Ratios",
        "WACC", "DCF", "Comps", "Sensitivity", "Football", "Checks",
    ]


def test_history_is_values_forecast_is_formulas(project: Path) -> None:
    path, model = build_file(project)
    ws = load_workbook(path)["IS"]
    row = model.row_of("revenue")
    assert ws.cell(row, 3 + model.h - 1).value == 13400
    forecast = ws.cell(row, 3 + model.h).value
    assert isinstance(forecast, str) and forecast.startswith("=") and "Drivers!" in forecast
    assert "sourced" in ws.cell(row, 3).comment.text


def test_inputs_are_blue_on_yellow(project: Path) -> None:
    path, model = build_file(project)
    cell = load_workbook(path)["Drivers"].cell(model.row_of("gross_margin"), 3 + model.h)
    assert cell.value == 0.41
    assert cell.font.color.rgb == "FF0000FF"
    assert cell.fill.fgColor.rgb == "FFFFF2CC"


def test_links_to_other_sheets_are_green(project: Path) -> None:
    path, model = build_file(project)
    cell = load_workbook(path)["BS"].cell(model.row_of("cash"), 3 + model.h)
    assert str(cell.value).startswith("=CF!")
    assert cell.font.color.rgb == "FF008000"


def test_checks_and_cover_formulas(project: Path) -> None:
    path, _ = build_file(project)
    workbook = load_workbook(path)
    check_formulas = [c.value for row in workbook["Checks"].iter_rows() for c in row
                      if isinstance(c.value, str) and c.value.startswith("=IF(")]
    assert check_formulas
    cover_text = [c.value for row in workbook["Cover"].iter_rows() for c in row if isinstance(c.value, str)]
    assert any("COUNTIF(Checks!" in text for text in cover_text)
    assert "ALL CHECKS OK" in cover_text or "OK WITH WARNINGS" in cover_text


def test_workbook_recalculates_on_open(project: Path) -> None:
    path, _ = build_file(project)
    assert load_workbook(path).calculation.fullCalcOnLoad is True


def test_football_chart_is_embedded(project: Path) -> None:
    path, _ = build_file(project)
    with zipfile.ZipFile(path) as archive:
        assert any(name.startswith("xl/charts/chart") for name in archive.namelist())


def test_no_valuation_sheets_without_valuation(tmp_path: Path) -> None:
    path, _ = build_file(write_project(tmp_path, valuation=None))
    assert load_workbook(path).sheetnames == ["Cover", "Drivers", "IS", "BS", "CF", "Schedules", "Ratios", "Checks"]
```

- [ ] **Step 2: Write the workbook parity test** — `tests/test_workbook_parity.py`

```python
"""Recalculate the written workbook with an Excel engine and compare every formula with Python."""

from __future__ import annotations

import math
import re
from pathlib import Path

import pytest

from rcmodel.engine import FormulaCell
from rcmodel.placement import PERIOD_COL0
from test_writer import build_file

formulas = pytest.importorskip("formulas")

KEY = re.compile(r"^'\[(?P<book>[^\]]+)\](?P<sheet>[^']+)'!(?P<cell>[A-Z]+[0-9]+)$")


def _to_float(result: object) -> float:
    try:
        import numpy as np

        return float(np.asarray(result, dtype=object).ravel()[0])
    except (TypeError, ValueError):
        return math.nan


def test_excel_values_match_python(project: Path) -> None:
    from openpyxl.utils import get_column_letter

    path, model = build_file(project)
    solution = formulas.ExcelModel().loads(str(path)).finish().calculate()
    excel: dict[tuple[str, str], float] = {}
    for name, ranges in solution.items():
        match = KEY.match(str(name).upper())
        if match:
            excel[(match["sheet"], match["cell"])] = _to_float(getattr(ranges, "value", ranges))
    compared = 0
    for line, row in model.placed.lines:
        periods = [None] if line.is_scalar else list(range(model.n))
        for period in periods:
            if not isinstance(model.cell(line.key, period), FormulaCell):
                continue
            col = line.col if period is None else PERIOD_COL0 + period
            key = (line.sheet.upper(), f"{get_column_letter(col)}{row}")
            python_value = model.value(line.key, period)
            if key not in excel or not math.isfinite(python_value):
                continue
            assert excel[key] == pytest.approx(python_value, rel=1e-9, abs=1e-6), f"{line.key} {period}"
            compared += 1
    assert compared > 300
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_writer.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.writer'`.

- [ ] **Step 4: Implement `rcmodel/styles.py`**

```python
"""Cell styles for the model workbook.

Palette and number-format conventions adapted from research_analyst
tools/xlsx_builder.py (MIT License, Copyright (c) 2026 CFA Society Mexico -
AI for Finance): blue inputs, black formulas, green links.
"""

from __future__ import annotations

from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

FONT_NAME = "Aptos Narrow"
BLUE = "FF0000FF"
BLACK = "FF000000"
GREEN = "FF008000"
WHITE = "FFFFFFFF"
GREY = "FF7F7F7F"


def font(color: str, bold: bool = False) -> Font:
    return Font(name=FONT_NAME, color=color, bold=bold)


BAND_FILL = PatternFill("solid", fgColor="FF1F4E79")
SECTION_FILL = PatternFill("solid", fgColor="FFBDD7EE")
INPUT_FILL = PatternFill("solid", fgColor="FFFFF2CC")
ERROR_FILL = PatternFill("solid", fgColor="FFC00000")
WARN_FILL = PatternFill("solid", fgColor="FFFFC000")
BAND_FONT = Font(name=FONT_NAME, color=WHITE, bold=True, size=12)
SECTION_FONT = Font(name=FONT_NAME, color=BLACK, bold=True)
BOLD_FONT = Font(name=FONT_NAME, bold=True)
TITLE_FONT = Font(name=FONT_NAME, bold=True, size=14)
NOTE_FONT = Font(name=FONT_NAME, color=GREY, italic=True)
WHITE_BOLD = Font(name=FONT_NAME, color=WHITE, bold=True)
TOP_BORDER = Border(top=Side(style="thin"))
RIGHT = Alignment(horizontal="right")
```

- [ ] **Step 5: Implement `rcmodel/writer.py`**

```python
"""Write the evaluated model to an .xlsx with live formulas (openpyxl)."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

from . import styles
from .checks import Check, CheckResult, Severity, overall_status
from .engine import BlankCell, Cell, InputCell, Model, ObservedCell
from .expr import At, Expr, Ref
from .placement import FIRST_ROW, HEADER_ROW, PERIOD_COL0
from .spec import Header, Line, Style
from .valuation import FootballSpec

SHEET_TITLES: dict[str, str] = {
    "Cover": "Model cover",
    "Drivers": "Drivers and assumptions",
    "IS": "Income statement",
    "BS": "Balance sheet",
    "CF": "Cash flow statement",
    "Schedules": "Supporting schedules",
    "Ratios": "Ratios",
    "WACC": "Cost of capital",
    "DCF": "Discounted cash flow",
    "Comps": "Comparable companies",
    "Sensitivity": "Sensitivity (value per share)",
    "Football": "Football field",
    "Checks": "Integrity checks",
}
SHEET_ORDER: tuple[str, ...] = tuple(SHEET_TITLES)
PERIOD_SHEETS = frozenset({"Drivers", "IS", "BS", "CF", "Schedules", "Ratios", "DCF", "Checks"})
AUTHOR = "research-challenge"
COVER_NOTES = (
    "Blue = input or reported figure (hover a reported figure for its source); black = formula; "
    "green = link to another sheet.",
    "Interest is charged on opening balances, so the model has no circular references.",
    "A revolving credit line keeps cash at or above the minimum cash balance.",
    "Valuation is as of the last fiscal year-end (no stub-period adjustment).",
)


@dataclass(frozen=True)
class BuildInfo:
    version: int
    filename: str
    built_on: date


def write_workbook(path: Path, model: Model, checks: Sequence[Check], results: Sequence[CheckResult],
                   football: FootballSpec | None, info: BuildInfo) -> None:
    workbook = Workbook()
    cover = workbook.active
    cover.title = "Cover"
    used = {placement.sheet for placement in model.placed.placements.values()} | {"Checks"}
    sheets: dict[str, Any] = {}
    for name in SHEET_ORDER[1:]:
        if name in used:
            sheets[name] = workbook.create_sheet(name)
            _frame(sheets[name], model, name)
    for sheet, row, header in model.placed.headers:
        _header(sheets[sheet], row, header, model)
    for line, row in model.placed.lines:
        _write_line(sheets[line.sheet], line, row, model)
    last_check_row = _write_checks(sheets["Checks"], model, checks)
    if football is not None:
        _football_chart(sheets["Football"], model, football)
    _cover(cover, model, info, results, last_check_row)
    workbook.calculation.fullCalcOnLoad = True
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(path)


def _last_col(model: Model) -> int:
    return PERIOD_COL0 + model.n + 2


def _frame(ws: Any, model: Model, name: str) -> None:
    profile = model.inputs.profile
    last_col = _last_col(model)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 52
    for col in range(PERIOD_COL0, last_col + 1):
        ws.column_dimensions[get_column_letter(col)].width = 13
    if name == "Drivers":
        ws.column_dimensions[get_column_letter(PERIOD_COL0 + model.n + 1)].width = 48
    for col in range(2, last_col + 1):
        ws.cell(1, col).fill = styles.BAND_FILL
    ws.cell(1, 2, f"{profile.name} ({profile.ticker}) - {SHEET_TITLES[name]}").font = styles.BAND_FONT
    ws.cell(2, 2, f"{profile.currency} {profile.units} | A = actual, E = estimate | "
                  "blue = input, black = formula, green = link to another sheet").font = styles.NOTE_FONT
    if name in PERIOD_SHEETS:
        for period, year in enumerate(model.inputs.years):
            cell = ws.cell(HEADER_ROW, PERIOD_COL0 + period, year)
            cell.number_format = '0"A"' if period < model.h else '0"E"'
            cell.font = styles.BOLD_FONT
            cell.alignment = styles.RIGHT
        ws.freeze_panes = ws.cell(HEADER_ROW + 1, PERIOD_COL0)


def _header(ws: Any, row: int, header: Header, model: Model) -> None:
    for col in range(2, _last_col(model) + 1):
        ws.cell(row, col).fill = styles.SECTION_FILL
    ws.cell(row, 2, header.title).font = styles.SECTION_FONT
    for col, text in header.columns:
        cell = ws.cell(row, col, text)
        cell.font = styles.SECTION_FONT
        cell.alignment = styles.RIGHT


def _write_line(ws: Any, line: Line, row: int, model: Model) -> None:
    if line.new_row and line.label:
        ws.cell(row, 2, line.label).font = styles.font(styles.BLACK, bold=line.style is not Style.NORMAL)
    periods: Sequence[int | None] = [None] if line.is_scalar else range(model.n)
    for period in periods:
        col = line.col if period is None else PERIOD_COL0 + period
        _write_cell(ws, row, col, line, model.cell(line.key, period), model, period)
    if line.notes:
        start = line.col + 1 if line.is_scalar else PERIOD_COL0 + model.n
        for offset, text in enumerate(line.notes):
            if text:
                ws.cell(row, start + offset, text).font = styles.NOTE_FONT


def _write_cell(ws: Any, row: int, col: int, line: Line, cell: Cell, model: Model, period: int | None) -> None:
    if isinstance(cell, BlankCell):
        return
    target = ws.cell(row, col)
    color = styles.BLACK
    if isinstance(cell, ObservedCell):
        target.value = cell.value
        target.comment = Comment(cell.comment, AUTHOR)
        color = styles.BLUE
    elif isinstance(cell, InputCell):
        target.value = cell.value
        target.fill = styles.INPUT_FILL
        color = styles.BLUE
    else:
        target.value = "=" + cell.expr.render(model, period, ws.title)
        if _is_link(cell.expr, ws.title, model):
            color = styles.GREEN
    target.font = styles.font(color, bold=line.style is not Style.NORMAL)
    target.number_format = line.fmt.value
    if line.style is Style.TOTAL:
        target.border = styles.TOP_BORDER


def _is_link(expr: Expr, sheet: str, model: Model) -> bool:
    return isinstance(expr, (Ref, At)) and model.sheet_of(expr.key) != sheet


def _write_checks(ws: Any, model: Model, checks: Sequence[Check]) -> int:
    row = FIRST_ROW
    groups = (
        ("Checks by year", [c for c in checks if c.periods is not None]),
        ("Single-value checks (result in column C)", [c for c in checks if c.periods is None]),
    )
    for title, group in groups:
        if not group:
            continue
        if row > FIRST_ROW:
            row += 1
        _header(ws, row, Header("Checks", title), model)
        row += 1
        for check in group:
            suffix = " (warning only)" if check.severity is Severity.WARN else ""
            ws.cell(row, 2, check.label + suffix)
            for period in check.periods if check.periods is not None else (None,):
                col = PERIOD_COL0 if period is None else PERIOD_COL0 + period
                condition = check.cond.render(model, period, ws.title)
                ws.cell(row, col, f'=IF({condition},"OK","{check.severity.value}")').alignment = styles.RIGHT
            row += 1
    last = max(row - 1, FIRST_ROW)
    span = f"C{FIRST_ROW}:{get_column_letter(PERIOD_COL0 + model.n - 1)}{last}"
    ws.conditional_formatting.add(span, CellIsRule(operator="equal", formula=['"ERROR"'],
                                                   fill=styles.ERROR_FILL, font=styles.WHITE_BOLD))
    ws.conditional_formatting.add(span, CellIsRule(operator="equal", formula=['"WARN"'], fill=styles.WARN_FILL))
    return last


def _football_chart(ws: Any, model: Model, spec: FootballSpec) -> None:
    first, last = model.row_of(spec.first_row_key), model.row_of(spec.last_row_key)
    chart = BarChart()
    chart.type = "bar"
    chart.grouping = "stacked"
    chart.overlap = 100
    chart.title = "Value per share by method"
    chart.add_data(Reference(ws, min_col=3, min_row=first, max_row=last), titles_from_data=False)
    chart.add_data(Reference(ws, min_col=5, min_row=first, max_row=last), titles_from_data=False)
    chart.set_categories(Reference(ws, min_col=2, min_row=first, max_row=last))
    chart.series[0].graphicalProperties.noFill = True
    chart.series[0].graphicalProperties.line.noFill = True
    chart.legend = None
    chart.height = 9
    chart.width = 18
    ws.add_chart(chart, f"G{FIRST_ROW}")


def _cover(ws: Any, model: Model, info: BuildInfo, results: Sequence[CheckResult], last_check_row: int) -> None:
    profile, years = model.inputs.profile, model.inputs.years
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 36
    ws.column_dimensions["C"].width = 90
    ws.cell(2, 2, f"{profile.name} ({profile.ticker})").font = styles.TITLE_FONT
    facts = (
        ("Accounting framework", profile.framework),
        ("Currency and units", f"{profile.currency} {profile.units}"),
        ("Historical years", f"{years[0]}-{years[model.h - 1]}"),
        ("Forecast years", f"{years[model.h]}-{years[-1]}"),
        ("Model file", info.filename),
        ("Version", str(info.version)),
        ("Built on", info.built_on.isoformat()),
    )
    row = 4
    for label, value in facts:
        ws.cell(row, 2, label).font = styles.BOLD_FONT
        ws.cell(row, 3, value)
        row += 1
    row += 1
    span = f"Checks!$C${FIRST_ROW}:${get_column_letter(PERIOD_COL0 + model.n - 1)}${last_check_row}"
    ws.cell(row, 2, "Model status (live)").font = styles.BOLD_FONT
    status = ws.cell(row, 3, f'=IF(COUNTIF({span},"ERROR")>0,"CHECKS FAILING",'
                             f'IF(COUNTIF({span},"WARN")>0,"OK WITH WARNINGS","ALL CHECKS OK"))')
    status.font = styles.TITLE_FONT
    ws.conditional_formatting.add(f"C{row}", FormulaRule(formula=[f'$C${row}="CHECKS FAILING"'],
                                                         fill=styles.ERROR_FILL, font=styles.WHITE_BOLD))
    row += 1
    ws.cell(row, 2, "Status computed by Python at build").font = styles.BOLD_FONT
    ws.cell(row, 3, overall_status(results))
    row += 2
    ws.cell(row, 2, "How to read this model").font = styles.BOLD_FONT
    for note in COVER_NOTES:
        ws.cell(row, 3, note)
        row += 1
    if model.inputs.warnings:
        row += 1
        ws.cell(row, 2, "Engine warnings").font = styles.BOLD_FONT
        for warning in model.inputs.warnings:
            ws.cell(row, 3, warning)
            row += 1
```

- [ ] **Step 6: Run the writer tests**

Run: `python -m pytest -q skills/model/engine/tests/test_writer.py`
Expected: `8 passed`

- [ ] **Step 7: Run the workbook parity test**

Run: `python -m pytest -q skills/model/engine/tests/test_workbook_parity.py`
Expected: `1 passed` (or skipped without `formulas`). If specific cells disagree, report the line keys and both values as DONE_WITH_CONCERNS; do not loosen the tolerance.

- [ ] **Step 8: mypy and commit**

Run: `python -m mypy tests skills/model/engine`
Expected: `Success`.

```bash
git add skills/model/engine/rcmodel/styles.py skills/model/engine/rcmodel/writer.py skills/model/engine/tests/test_writer.py skills/model/engine/tests/test_workbook_parity.py
git commit -m "feat(engine): xlsx writer with live formulas, checks sheet, cover status and football chart"
```

---

### Task 9: Summary, CLI and launcher (`summary.py`, `cli.py`, `build_model.py`)

**Files:**
- Create: `skills/model/engine/rcmodel/summary.py`
- Create: `skills/model/engine/rcmodel/cli.py`
- Create: `skills/model/engine/build_model.py`
- Test: `skills/model/engine/tests/test_cli.py`

- [ ] **Step 1: Write the failing tests** — `tests/test_cli.py`

```python
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import ENGINE_DIR, HISTORY, write_project
from rcmodel.cli import main, next_version_path


def test_build_writes_workbook_and_summary(project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(project)]) == 0
    assert (project / "model" / "ACME_model_v1.xlsx").is_file()
    summary = json.loads((project / "model" / "model-summary.json").read_text(encoding="utf-8"))
    assert summary["status"] in {"ALL CHECKS OK", "OK WITH WARNINGS"}
    assert summary["lines"]["revenue"]["2026"] == pytest.approx(13400 * 1.07)
    assert summary["lines"]["fcff"]["2021"] is None
    assert "price_gordon" in summary["valuation"]
    assert summary["model_file"] == "ACME_model_v1.xlsx"
    out = capsys.readouterr().out
    assert out.isascii()
    assert "[ok] workbook -> model/ACME_model_v1.xlsx" in out


def test_second_build_bumps_the_version(project: Path) -> None:
    assert main(["--project", str(project)]) == 0
    assert main(["--project", str(project)]) == 0
    assert (project / "model" / "ACME_model_v1.xlsx").is_file()
    assert (project / "model" / "ACME_model_v2.xlsx").is_file()


def test_input_errors_exit_2_with_ascii_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "cash"}
    write_project(tmp_path, history=history)
    assert main(["--project", str(tmp_path)]) == 2
    out = capsys.readouterr().out
    assert out.isascii() and "cash" in out


def test_next_version_ignores_other_files(tmp_path: Path) -> None:
    (tmp_path / "ACME_model_v3.xlsx").write_bytes(b"")
    (tmp_path / "notes.xlsx").write_bytes(b"")
    path, version = next_version_path(tmp_path, "ACME")
    assert (path.name, version) == ("ACME_model_v4.xlsx", 4)


def test_ticker_is_made_filename_safe(tmp_path: Path) -> None:
    path, _ = next_version_path(tmp_path, "GFNORTE O")
    assert path.name == "GFNORTE-O_model_v1.xlsx"


def test_launcher_runs(project: Path) -> None:
    completed = subprocess.run(
        [sys.executable, str(ENGINE_DIR / "build_model.py"), "--project", str(project)],
        capture_output=True, text=True, check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert (project / "model" / "ACME_model_v1.xlsx").is_file()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest -q skills/model/engine/tests/test_cli.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'rcmodel.cli'`.

- [ ] **Step 3: Implement `rcmodel/summary.py`**

```python
"""model/model-summary.json: the numbers the valuation, report and pitch skills read."""

from __future__ import annotations

import math
from collections.abc import Sequence
from typing import Any

from .checks import CheckResult, overall_status
from .engine import BlankCell, Model
from .writer import BuildInfo

SUMMARY_LINES: tuple[str, ...] = (
    "revenue", "gross_profit", "ebitda", "ebit", "net_income_parent", "eps",
    "fcf", "cash", "revolver", "net_debt", "fcff",
)
SUMMARY_VALUES: tuple[str, ...] = (
    "wacc", "terminal_growth", "exit_multiple", "ev_gordon", "ev_exit", "price_gordon", "price_exit",
    "share_price", "upside_gordon", "upside_exit", "tv_share_gordon", "implied_exit_multiple",
    "implied_g_exit", "implied_g", "price_comps_ev_ebitda", "price_comps_pe",
)


def _clean(value: float) -> float | None:
    return round(value, 6) if math.isfinite(value) else None


def build_summary(model: Model, results: Sequence[CheckResult], info: BuildInfo) -> dict[str, Any]:
    inputs = model.inputs
    lines: dict[str, dict[str, float | None]] = {}
    for key in SUMMARY_LINES:
        if not model.has(key):
            continue
        lines[key] = {
            str(year): None if isinstance(model.cell(key, t), BlankCell) else _clean(model.value(key, t))
            for t, year in enumerate(inputs.years)
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
        "valuation": valuation,
        "checks": [
            {"check": r.label, "year": None if r.period is None else inputs.years[r.period], "status": r.status}
            for r in results
        ],
        "warnings": list(inputs.warnings),
    }
```

- [ ] **Step 4: Implement `rcmodel/cli.py`**

```python
"""Command line: python build_model.py --project <team folder>. Console output is ASCII only."""

from __future__ import annotations

import argparse
import json
import re
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .assemble import assemble
from .checks import CheckResult, build_checks, evaluate_checks, overall_status, parity_checks
from .engine import ModelError
from .inputs import InputError, load_inputs
from .summary import build_summary
from .writer import BuildInfo, write_workbook

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_MODEL_ERROR = 3


@dataclass(frozen=True)
class BuildResult:
    workbook: Path
    summary: Path
    results: tuple[CheckResult, ...]
    warnings: tuple[str, ...]
    status: str
    years: tuple[int, ...]


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def next_version_path(model_dir: Path, ticker: str) -> tuple[Path, int]:
    """Next unused <TICKER>_model_v<N>.xlsx; earlier versions are never overwritten."""
    safe = re.sub(r"[^A-Za-z0-9]+", "-", ticker).strip("-") or "MODEL"
    pattern = re.compile(rf"^{re.escape(safe)}_model_v(\d+)\.xlsx$")
    versions = [int(m.group(1)) for p in model_dir.glob("*.xlsx") if (m := pattern.match(p.name))]
    version = max(versions, default=0) + 1
    return model_dir / f"{safe}_model_v{version}.xlsx", version


def build(project: Path, today: date) -> BuildResult:
    inputs = load_inputs(project)
    model, football = assemble(inputs)
    checks = [*build_checks(inputs), *parity_checks(model)]
    results = evaluate_checks(model, checks)
    model_dir = project / "model"
    model_dir.mkdir(parents=True, exist_ok=True)
    path, version = next_version_path(model_dir, inputs.profile.ticker)
    info = BuildInfo(version, path.name, today)
    write_workbook(path, model, checks, results, football, info)
    summary_path = model_dir / "model-summary.json"
    summary = build_summary(model, results, info)
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return BuildResult(path, summary_path, tuple(results), inputs.warnings, overall_status(results), inputs.years)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the research-challenge financial model (xlsx + model-summary.json).")
    parser.add_argument("--project", default=".", help="Team project folder (the one with company-profile.yaml)")
    args = parser.parse_args(argv)
    try:
        result = build(Path(args.project).resolve(), date.today())
    except InputError as exc:
        print("[x] Cannot build the model. Fix these inputs first:")
        for message in exc.messages:
            print("  - " + ascii_safe(message))
        return EXIT_INPUT_ERROR
    except ModelError as exc:
        print("[x] Model definition error: " + ascii_safe(str(exc)))
        return EXIT_MODEL_ERROR
    counts = {status: sum(1 for r in result.results if r.status == status) for status in ("OK", "ERROR", "WARN")}
    print(f"[ok] workbook -> model/{ascii_safe(result.workbook.name)}")
    print("[ok] summary  -> model/model-summary.json")
    print(f"checks: {counts['OK']} OK, {counts['ERROR']} ERROR, {counts['WARN']} WARN")
    for r in result.results:
        if r.status != "OK":
            year = "" if r.period is None else f" ({result.years[r.period]})"
            marker = "[x]" if r.status == "ERROR" else "[warn]"
            print(f"{marker} {ascii_safe(r.label)}{year}")
    for warning in result.warnings:
        print("[warn] " + ascii_safe(warning))
    print(f"status: {result.status}")
    return EXIT_OK
```

- [ ] **Step 5: Implement `skills/model/engine/build_model.py`**

```python
"""Launcher for the model engine.

Usage (from the team project folder):
    python <path-to-skill>/engine/build_model.py --project .
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcmodel.cli import main  # noqa: E402

raise SystemExit(main())
```

- [ ] **Step 6: Run the tests**

Run: `python -m pytest -q skills/model/engine/tests/test_cli.py`
Expected: `6 passed`

- [ ] **Step 7: Run the whole suite and mypy**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine`
Expected: every test passes (parity tests may skip if `formulas` is missing); mypy `Success`.

- [ ] **Step 8: Commit**

```bash
git add skills/model/engine/rcmodel/summary.py skills/model/engine/rcmodel/cli.py skills/model/engine/build_model.py skills/model/engine/tests/test_cli.py
git commit -m "feat(engine): model-summary.json, CLI with versioned output and launcher"
```

---

### Task 10: Integration — dependencies, docs, attribution, spec

**Files:**
- Modify: `skills/init-skills/SKILL.md` (Step 2 environment check)
- Modify: `README.md` (requirements, development)
- Modify: `NOTICE`
- Modify: `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` (§7, §11)

- [ ] **Step 1: `skills/init-skills/SKILL.md` — require PyYAML too**

In Step 2, replace `<cmd> -c "import openpyxl"` with `<cmd> -c "import openpyxl, yaml"`, and replace the `openpyxl missing` bullet with:

```markdown
- openpyxl or PyYAML missing -> Windows: `py -m pip install openpyxl pyyaml python-docx`; macOS: `python3 -m pip install openpyxl pyyaml python-docx`
```

- [ ] **Step 2: `README.md`**

Replace the Requirements paragraph with:

```markdown
**Requirements:** Claude Code. The model skills need Python 3 with `openpyxl`
and `pyyaml`; `init-skills` checks and tells you the exact install command.
```

Replace the Development code block with:

```
python -m pip install "openpyxl>=3.1" "pyyaml>=6" "pytest>=8" "mypy>=1.10" "hypothesis>=6" "formulas>=1.2"
python -m pytest -q
python -m mypy tests skills/model/engine
```

- [ ] **Step 3: `NOTICE` — append**

```
The model engine (skills/model/engine) is original code. Its cell palette and
number formats (blue inputs, black formulas, green links) are adapted from
research_analyst tools/xlsx_builder.py, and its valuation conventions (dual
terminal value with implied cross-checks, closed-form reverse DCF, Hamada
beta relevering, working capital in days, interest on opening balances)
follow research_analyst's model-standards references.
```

- [ ] **Step 4: Spec §7 — record what was built**

In `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md`, replace the §7 opening line
`Adapted from research_analyst \`tools/xlsx_builder.py\` (MIT, attributed in NOTICE).`
with:

```markdown
New code in `skills/model/engine/` (research_analyst has no calculation engine;
only its style palette is adapted, attributed in NOTICE). Every cell is defined
once as an expression tree that is both evaluated in Python and rendered as an
Excel formula, so the two cannot drift; tests recalculate the workbook with the
`formulas` library as an Excel oracle. Plan:
`docs/superpowers/plans/2026-09-23-phase2a-model-engine.md`.
```

In the §7 tab list, remove `Historical,` and add after the tab list:

```markdown
- Reported history sits directly in IS/BS/CF as blue cells with a comment
  giving document, page and tag (no separate Historical tab).
- Sensitivity uses formula grids (no Excel data tables, which need Excel to recalculate).
- D&A reduces PP&E only; intangibles, other non-current items, short-term debt
  and leases are held flat. Engine defaults: a missing driver is held at its
  last actual value (net new debt and share growth default to zero) and flagged.
- Runtime dependencies: `openpyxl`, `pyyaml`.
```

In §11, replace `skills/model/engine/            model builder (adapted) + tests/ (phase 2)` with `skills/model/engine/            model engine (rcmodel package, build_model.py) + tests/`.

- [ ] **Step 5: Run everything**

Run: `python -m pytest -q; python -m mypy tests skills/model/engine; claude plugin validate .`
Expected: all tests pass; mypy `Success`; validation passes.

- [ ] **Step 6: End-to-end manual check (by the user, optional)**

Open the newest `ACME_model_v*.xlsx` produced by `test_cli` in a temp folder (or run
`python skills/model/engine/build_model.py --project <a folder written with the fixture>`)
in Excel or LibreOffice and confirm the Cover shows `ALL CHECKS OK` or `OK WITH WARNINGS`
and the Checks sheet has no `ERROR`.

- [ ] **Step 7: Commit**

```bash
git add skills/init-skills/SKILL.md README.md NOTICE docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md
git commit -m "docs: record model engine design, dependencies and attribution"
```

Do not merge `feat/phase2a-engine` into `main` yet: phase 2b adds the `financials`, `forecast`, `model` and `valuation` skills that use this engine.
