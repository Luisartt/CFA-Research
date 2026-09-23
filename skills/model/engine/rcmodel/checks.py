"""Integrity checks, written to the Checks sheet as Excel formulas and evaluated in Python.

Parity checks compare an Excel formula with the value Python computed at build
time, which the writer puts next to the result. They only warn: once a student
edits an input in Excel the build-time value is stale, and that is not an error.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum

from .engine import Model
from .expr import At, Context, Expr, Ref, cmp, fn
from .inputs import ModelInputs
from .spec import Fmt

R = Ref
TOLERANCE = 0.5  # half a unit of the model currency (e.g. MXN 0.5 million)
TV_SHARE_LIMIT = 0.75
WACC_G_SPREAD_LIMIT = 0.02
REFERENCE_KEY = "__reference_value__"  # the address a Context resolves for a check's own reference cell


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
    reference_value: float | None = None  # the Python value at build, shown next to a single-value result
    reference_fmt: Fmt = Fmt.NUMBER


@dataclass(frozen=True)
class ReferenceValue(Expr):
    """A check's build-time Python value: evaluates to the number, renders as the cell the writer puts it in."""

    v: float

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return self.v

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return ctx.address(REFERENCE_KEY, None, sheet)


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
        Check("ppe_non_negative", "PP&E stays at or above zero", Severity.ERROR,
              cmp(R("ppe_net"), ">=", -0.001), all_years),
        Check("debt_non_negative", "Long-term debt stays at or above zero", Severity.ERROR,
              cmp(R("debt_long"), ">=", -0.001), all_years),
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
            Check("wacc_g_spread", "WACC exceeds terminal growth by at least 2 points", Severity.WARN,
                  cmp(R("wacc") - R("terminal_growth"), ">=", WACC_G_SPREAD_LIMIT), None),
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
        line = model.line(key)
        label = (f"Excel matches the Python value at build: {line.label} "
                 "(stale if inputs are edited in Excel - rebuild)")
        checks.append(Check(f"parity_{key}", label, Severity.WARN, _close(ref, ReferenceValue(value), tolerance),
                            None, reference_value=value, reference_fmt=line.fmt))
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
