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
