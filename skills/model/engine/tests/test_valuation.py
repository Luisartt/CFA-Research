from __future__ import annotations

import copy
from pathlib import Path

import pytest

from conftest import DRIVERS, VALUATION, write_project
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
                    - m.value("capex", t) - m.value("lease_principal_paid", t) + m.value("change_nwc", t))
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


def test_new_leases_reduce_price_gordon(tmp_path: Path) -> None:
    """IFRS 16: lease liability stays in net debt, so new leases must be treated like capex in
    FCFF. Turning on lease renewals (lease_principal_pct_revenue > 0) should lower price_gordon
    relative to the base fixture, where it is held at zero."""
    base, _ = _full(write_project(tmp_path / "base"))
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"]["lease_principal_pct_revenue"] = {"values": [0.02] * 5, "tag": "assumption"}
    leased, _ = _full(write_project(tmp_path / "leased", drivers=drivers))
    assert leased.value("price_gordon", None) < base.value("price_gordon", None)
