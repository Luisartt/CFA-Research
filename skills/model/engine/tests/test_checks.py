from __future__ import annotations

import copy
from pathlib import Path

from conftest import DRIVERS, HISTORY, VALUATION, write_project
from rcmodel.assemble import assemble
from rcmodel.checks import CheckResult, Severity, build_checks, evaluate_checks, overall_status, parity_checks
from rcmodel.inputs import load_inputs

DRIVER_ENTRY_DEFAULTS = {"tag": "assumption", "rationale": "test", "pillar": "1"}


def _driver(values: list[float]) -> dict[str, object]:
    return {"values": values, **DRIVER_ENTRY_DEFAULTS}


def _results(project: Path) -> list[CheckResult]:
    model, _ = assemble(load_inputs(project))
    return evaluate_checks(model, [*build_checks(model.inputs), *parity_checks(model)])


def _status(results: list[CheckResult], key: str, period: int | None) -> str:
    return next(r.status for r in results if r.key == key and r.period == period)


def test_fixture_has_no_errors(project: Path) -> None:
    results = _results(project)
    assert [r for r in results if r.status == "ERROR"] == []
    assert any(r.key == "parity_price_gordon" for r in results)


def test_parity_checks_warn_and_carry_the_python_value(project: Path) -> None:
    model, _ = assemble(load_inputs(project))
    checks = parity_checks(model)
    assert {c.key for c in checks} == {"parity_total_assets", "parity_net_income_parent", "parity_cash_end",
                                       "parity_wacc", "parity_price_gordon"}
    for check in checks:
        assert check.severity is Severity.WARN
        assert check.label.startswith("Excel matches the Python value at build: ")
        assert check.label.endswith("(stale if inputs are edited in Excel - rebuild)")
    price = next(c for c in checks if c.key == "parity_price_gordon")
    assert price.reference_value == model.value("price_gordon", None)
    assert "Value per share today - Gordon" in price.label
    assert all(c.reference_value is None for c in build_checks(model.inputs))
    assert overall_status(evaluate_checks(model, checks)) == "ALL CHECKS OK"


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


def test_ppe_non_negative_check_fires(tmp_path: Path) -> None:
    # A tiny opening PP&E balance plus an outsized D&A / revenue assumption (amortization held at
    # zero, so it is all depreciation) drives the schedule's PP&E roll-forward below zero.
    history = dict(HISTORY)
    history["ppe_net"] = (6000, 6200, 6450, 6700, 50)
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"]["da_pct_revenue"] = _driver([0.5] * 5)
    results = _results(write_project(tmp_path, history=history, drivers=drivers))
    assert _status(results, "ppe_non_negative", 4) == "OK"
    assert _status(results, "ppe_non_negative", 5) == "ERROR"


def test_debt_non_negative_check_fires(tmp_path: Path) -> None:
    # The forecast schedule already caps repayment at the opening balance (Task 6), so long-term
    # debt can only go negative from a bad historical figure, which this check should still catch.
    history = dict(HISTORY)
    history["debt_long"] = (3500, 3400, 3300, 3200, -100)
    results = _results(write_project(tmp_path, history=history))
    assert _status(results, "debt_non_negative", 3) == "OK"
    assert _status(results, "debt_non_negative", 4) == "ERROR"


def test_wacc_g_spread_warns(tmp_path: Path) -> None:
    # Lowering the risk-free rate pulls WACC down close to (but still above) terminal growth,
    # so the spread falls under the 2-point warning threshold without tripping wacc_gt_g.
    valuation = copy.deepcopy(VALUATION)
    valuation["wacc"]["risk_free"] = -0.02
    results = _results(write_project(tmp_path, valuation=valuation))
    assert _status(results, "wacc_gt_g", None) == "OK"
    assert _status(results, "wacc_g_spread", None) == "WARN"
    assert overall_status(results) == "OK WITH WARNINGS"
