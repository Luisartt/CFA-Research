from __future__ import annotations

import copy
import math
from pathlib import Path
from typing import Any

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


OVERRIDE_TAG = "assumption"


def _drivers_with(**overrides: list[float]) -> dict[str, Any]:
    drivers = copy.deepcopy(DRIVERS)
    for key, values in overrides.items():
        drivers["drivers"][key] = {"values": values, "tag": OVERRIDE_TAG}
    return drivers


def _assert_balances(m: Model) -> None:
    for t in range(m.n):
        assert m.value("total_assets", t) == pytest.approx(m.value("total_liabilities_equity", t), abs=1e-6)


def test_lease_principal_is_financing_and_renews_right_of_use_assets(tmp_path: Path) -> None:
    base = _model(write_project(tmp_path / "base"))
    m = _model(write_project(tmp_path / "lease", drivers=_drivers_with(lease_principal_pct_revenue=[0.02] * 5)))
    _assert_balances(m)
    cumulative = 0.0
    for t in range(m.h, m.n):
        principal = m.value("lease_principal_paid", t)
        assert principal == pytest.approx(0.02 * m.value("revenue", t))
        cumulative += principal
        assert m.value("sch_new_leases", t) == pytest.approx(principal)
        assert m.value("lease_liabilities", t) == pytest.approx(600)
        assert m.value("revolver", t) == pytest.approx(0.0, abs=1e-9)
        assert m.value("ppe_net", t) - base.value("ppe_net", t) == pytest.approx(cumulative)
        shortfall = base.value("cash", t) - m.value("cash", t)
        assert shortfall == pytest.approx(cumulative, rel=0.05)
        assert shortfall >= cumulative  # lost interest income only widens the gap
        assert m.value("fcf", t) == pytest.approx(m.value("cfo", t) - m.value("capex", t) - principal)


def test_lease_principal_history_is_observed(tmp_path: Path) -> None:
    history = {**HISTORY, "lease_principal_paid": (100, 110, 120, 125, 134)}
    m = _model(write_project(tmp_path, history=history))
    last = m.h - 1
    assert m.value("lease_principal_pct_revenue", last) == pytest.approx(134 / 13400)
    assert m.value("fcf", last) == pytest.approx(1700 - 900 - 134)


def _asset_light_history() -> dict[str, tuple[float, ...]]:
    history = dict(HISTORY)
    history["intangibles_goodwill"] = tuple(
        i + p - 500 for i, p in zip(HISTORY["intangibles_goodwill"], HISTORY["ppe_net"])
    )
    history["ppe_net"] = (500.0,) * len(HISTORY["ppe_net"])
    return history


def test_amortization_runs_off_intangibles_not_ppe(tmp_path: Path) -> None:
    history = _asset_light_history()
    before = _model(write_project(tmp_path / "before", history=history,
                                  drivers=_drivers_with(capex_pct_revenue=[0.02] * 5)))
    assert min(before.value("ppe_net", t) for t in range(before.h, before.n)) < 0
    m = _model(write_project(tmp_path / "after", history=history,
                             drivers=_drivers_with(capex_pct_revenue=[0.02] * 5, amort_pct_revenue=[0.035] * 5)))
    _assert_balances(m)
    for t in range(m.h, m.n):
        amortization = 0.035 * m.value("revenue", t)
        assert m.value("sch_amort", t) == pytest.approx(amortization)
        assert m.value("sch_da_ppe", t) == pytest.approx(m.value("da", t) - amortization)
        assert m.value("da", t) == pytest.approx(before.value("da", t))
        assert m.value("intangibles_goodwill", t) == pytest.approx(m.value("intangibles_goodwill", t - 1) - amortization)
        assert m.value("ppe_net", t) >= 0


def test_amortization_is_capped_at_opening_intangibles(tmp_path: Path) -> None:
    history = {**HISTORY, "intangibles_goodwill": (0.0,) * 5,
               "equity_parent": tuple(e - 1500 for e in HISTORY["equity_parent"])}
    m = _model(write_project(tmp_path, history=history, drivers=_drivers_with(amort_pct_revenue=[0.01] * 5)))
    _assert_balances(m)
    for t in range(m.h, m.n):
        assert m.value("sch_amort", t) == pytest.approx(0.0)
        assert m.value("intangibles_goodwill", t) == pytest.approx(0.0)


def test_loss_years_pay_no_dividends(tmp_path: Path) -> None:
    m = _with_driver(tmp_path, "gross_margin", [0.25] * 5)
    _assert_balances(m)
    for t in range(m.h, m.n):
        assert m.value("net_income_parent", t) < 0
        assert m.value("dividends_paid", t) == 0.0
        assert m.value("nci_dividends", t) == 0.0


def test_nci_dividends_reduce_nci_equity_and_cash(project: Path) -> None:
    m = _model(project)
    t = m.h
    nci_dividends = m.value("nci_income", t) * 0.40
    assert m.value("nci_dividends", t) == pytest.approx(nci_dividends)
    assert m.value("nci_equity", t) == pytest.approx(420 + m.value("nci_income", t) - nci_dividends)
    assert m.value("cff_before_revolver", t) == pytest.approx(
        m.value("cf_net_new_debt", t) - m.value("dividends_paid", t) - m.value("lease_principal_paid", t) - nci_dividends
    )


def test_debt_repayment_stops_at_zero(tmp_path: Path) -> None:
    m = _with_driver(tmp_path, "net_new_debt", [-1000.0] * 5)
    _assert_balances(m)
    for t, expected in zip(range(m.h, m.n), (2100, 1100, 100, 0, 0)):
        assert m.value("debt_long", t) == pytest.approx(expected)
        assert m.value("cf_net_new_debt", t) == pytest.approx(m.value("sch_net_new_debt", t))


def test_debt_free_company_builds_without_nan(tmp_path: Path) -> None:
    zeros = (0.0,) * 5
    history = {k: v for k, v in HISTORY.items() if k != "net_income_reported"}
    history.update(debt_short=zeros, debt_long=zeros, lease_liabilities=zeros, interest_expense=zeros)
    history["equity_parent"] = tuple(
        e + s + d + le for e, s, d, le in zip(HISTORY["equity_parent"], HISTORY["debt_short"],
                                             HISTORY["debt_long"], HISTORY["lease_liabilities"])
    )
    drivers = copy.deepcopy(DRIVERS)
    del drivers["drivers"]["interest_rate_debt"]
    m = _model(write_project(tmp_path, history=history, drivers=drivers))
    assert m.value("interest_rate_debt", m.h - 1) == 0.0
    _assert_balances(m)
    for key, line in m.lines.items():
        if line.is_scalar or m.sheet_of(key) == "Ratios":
            continue
        for t in range(m.n):
            assert not math.isnan(m.value(key, t)), f"{key}[{t}] is NaN"


def test_loss_year_history_gives_zero_tax_rate_and_payout(tmp_path: Path) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "net_income_reported"}
    history["opex"] = (*HISTORY["opex"][:-1], 6000)
    drivers = copy.deepcopy(DRIVERS)
    del drivers["drivers"]["tax_rate"]
    del drivers["drivers"]["payout_ratio"]
    m = _model(write_project(tmp_path, history=history, drivers=drivers))
    last = m.h - 1
    assert m.value("ebt", last) < 0
    assert m.value("tax_rate", last) == 0.0
    assert m.value("payout_ratio", last) == 0.0
    assert m.value("tax_rate", m.h) == 0.0
    assert m.value("payout_ratio", m.h) == 0.0


def test_roic_uses_opening_capital(project: Path) -> None:
    m = _model(project)
    t = m.h
    opening_capital = m.value("total_equity", t - 1) + m.value("net_debt", t - 1)
    assert m.value("r_roic", t) == pytest.approx(m.value("ebit", t) * (1 - 0.30) / opening_capital)
    assert isinstance(m.cell("r_roic", 0), BlankCell)
    assert m.line("r_roic").label == "ROIC = EBIT x (1 - tax rate) / opening (equity + net debt)"
    assert m.line("ebitda").label == "EBITDA (post-IFRS 16)"
