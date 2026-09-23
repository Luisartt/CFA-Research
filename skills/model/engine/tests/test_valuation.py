from __future__ import annotations

import copy
import math
from pathlib import Path

import pytest

from conftest import DRIVERS, VALUATION, write_project
from rcmodel.assemble import assemble
from rcmodel.engine import Model
from rcmodel.inputs import load_inputs
from rcmodel.spec import Fmt, Header
from rcmodel.valuation import COMPS_S, G_STEPS, WACC_STEPS, FootballSpec, comps_layout


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
    w, g, ke = m.value("wacc", None), 0.04, m.value("v_ke", None)
    fcff = [m.value("fcff", t) for t in range(m.h, m.n)]
    present_value = sum(f / (1 + w) ** (i + 0.5) for i, f in enumerate(fcff))
    terminal = fcff[-1] * (1 + g) / (w - g) / (1 + w) ** (len(fcff) - 0.5)
    non_operating, debt_like, stub = 0.0, 0.0, 0.0  # fixture defaults
    equity = (present_value + terminal + non_operating - m.value("net_debt", m.h - 1)
              - m.value("nci_equity", m.h - 1) - debt_like)
    roll = (1 + ke) ** stub
    assert m.value("price_gordon", None) == pytest.approx(equity / m.value("shares_diluted", m.h - 1) * roll)


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


VALUATION_SHEETS = frozenset({"WACC", "DCF", "Comps", "Sensitivity", "Football"})


def test_wacc_close_to_growth_does_not_blow_up(tmp_path: Path) -> None:
    """risk_free 0.012 puts WACC near g: grid cells with WACC - g < 1% read 0 (shown n.m.), never NaN."""
    m = _with_valuation(tmp_path, "tight", wacc__risk_free=0.012)
    for key, line in m.lines.items():
        if line.sheet not in VALUATION_SHEETS:
            continue
        periods: list[int | None] = [None] if line.is_scalar else list(range(m.n))
        for t in periods:
            assert not math.isnan(m.value(key, t)), f"{key}[{t}] is NaN"
    guarded = 0
    for i in range(len(WACC_STEPS)):
        for j in range(len(G_STEPS)):
            assert m.line(f"sens_{i}_{j}").fmt == Fmt.PRICE_NM
            if m.value(f"sens_w_{i}", None) - m.value(f"sens_g_{j}", None) < 0.01:
                guarded += 1
                assert m.value(f"sens_{i}_{j}", None) == 0
    assert guarded > 0
    assert m.value("ff_dcf_low", None) > 0


def test_mid_year_discounts_gordon_terminal_value_half_a_year_less(tmp_path: Path) -> None:
    mid = _with_valuation(tmp_path, "mid", mid_year=True)
    end = _with_valuation(tmp_path, "end", mid_year=False)
    years = mid.n - mid.h
    for m, exponent in ((mid, years - 0.5), (end, float(years))):
        w = m.value("wacc", None)
        assert m.value("pv_tv_gordon", None) == pytest.approx(m.value("tv_gordon", None) / (1 + w) ** exponent)
        assert m.value("pv_tv_exit", None) == pytest.approx(m.value("tv_exit", None) / (1 + w) ** years)
        assert m.value("sens_2_2", None) == pytest.approx(m.value("price_gordon", None), rel=1e-9)


def test_exit_at_implied_multiple_equals_gordon_without_mid_year(tmp_path: Path) -> None:
    base = _with_valuation(tmp_path, "base", mid_year=False)
    m = _with_valuation(tmp_path, "exit", mid_year=False,
                        terminal__exit_ev_ebitda=base.value("implied_exit_multiple", None))
    assert m.value("price_exit", None) == pytest.approx(m.value("price_gordon", None))


def test_implied_growth_of_exit_multiple_reproduces_the_exit_price(tmp_path: Path) -> None:
    base = _with_valuation(tmp_path, "base")
    m = _with_valuation(tmp_path, "g", terminal__growth=base.value("implied_g_exit", None))
    assert m.value("price_gordon", None) == pytest.approx(base.value("price_exit", None))


def test_equity_bridge_adds_non_operating_assets_and_deducts_debt_like_items(tmp_path: Path) -> None:
    base = _with_valuation(tmp_path, "base")
    m = _with_valuation(tmp_path, "bridge", non_operating_assets=500.0, debt_like_items=200.0)
    shift = (500.0 - 200.0) / m.value("shares_val", None)
    assert m.value("non_op", None) == 500.0
    assert m.value("debt_like", None) == 200.0
    for key in ("price_gordon", "price_exit", "price_comps_ev_ebitda", "sens_2_2", "ff_exit_low", "ff_ev_ebitda_high"):
        assert m.value(key, None) == pytest.approx(base.value(key, None) + shift), key
    assert m.value("price_comps_pe", None) == pytest.approx(base.value("price_comps_pe", None))
    assert m.value("market_ev", None) == pytest.approx(base.value("market_ev", None) - 300.0)


def test_reverse_dcf_recovers_growth_with_bridge_items(tmp_path: Path) -> None:
    base = _with_valuation(tmp_path, "base", non_operating_assets=500.0, debt_like_items=200.0)
    m = _with_valuation(tmp_path, "priced", non_operating_assets=500.0, debt_like_items=200.0,
                        share_price=base.value("price_gordon", None))
    assert m.value("implied_g", None) == pytest.approx(0.04, abs=1e-9)


def test_reverse_dcf_recovers_growth_with_stub(tmp_path: Path) -> None:
    base = _with_valuation(tmp_path, "base", years_since_fiscal_year_end=0.75)
    m = _with_valuation(tmp_path, "priced", years_since_fiscal_year_end=0.75,
                        share_price=base.value("price_gordon", None))
    assert m.value("implied_g", None) == pytest.approx(m.value("terminal_growth", None), abs=1e-9)


def test_football_keeps_valid_negative_grid_values(tmp_path: Path) -> None:
    """A heavily indebted company can have genuinely negative values; only n.m. cells fall back."""
    m = _with_valuation(tmp_path, "indebted", debt_like_items=15000.0)
    grid = [m.value(f"sens_{i}_{j}", None) for i in range(len(WACC_STEPS)) for j in range(len(G_STEPS))]
    assert min(grid) < m.value("price_gordon", None) < 0 < max(grid)
    assert m.value("ff_dcf_low", None) == pytest.approx(min(grid))
    assert m.value("ff_dcf_high", None) == pytest.approx(max(grid))


def test_value_today_rolls_forward_from_fiscal_year_end(tmp_path: Path) -> None:
    base = _with_valuation(tmp_path, "base")
    m = _with_valuation(tmp_path, "stub", years_since_fiscal_year_end=0.75)
    ke = m.value("v_ke", None)
    assert m.value("stub", None) == 0.75
    assert m.value("roll_factor", None) == pytest.approx((1 + ke) ** 0.75)
    for key in ("price_gordon", "price_exit", "ff_exit_low", "ff_exit_high"):
        assert m.value(key, None) == pytest.approx(base.value(key, None) * (1 + ke) ** 0.75), key
    assert m.value("sens_2_2", None) == pytest.approx(m.value("price_gordon", None), rel=1e-9)
    assert m.value("price_comps_pe", None) == pytest.approx(base.value("price_comps_pe", None))


def test_twelve_month_target_and_upside(project: Path) -> None:
    m, _ = _full(project)
    dps = m.value("dividends_paid", m.h) / m.value("shares_diluted", m.h)
    assert m.value("dps_next", None) == pytest.approx(dps)
    target = m.value("price_gordon", None) * (1 + m.value("v_ke", None)) - dps
    assert m.value("target_12m_gordon", None) == pytest.approx(target)
    assert m.value("upside_gordon", None) == pytest.approx(target / 25.0 - 1)
    assert m.value("upside_exit", None) == pytest.approx(m.value("price_exit", None) / 25.0 - 1)
    assert m.line("upside_gordon").label == "Upside to 12-month target - Gordon"
    assert m.line("target_12m_gordon").label == (
        "12-month target price - Gordon (value today x (1 + cost of equity) - next dividend)")


def test_current_market_debt_to_equity(project: Path) -> None:
    m, _ = _full(project)
    expected = m.value("total_debt", m.h - 1) / (25.0 * m.value("shares_diluted", m.h - 1))
    assert m.value("de_market", None) == pytest.approx(expected)
    assert m.line("de_market").sheet == "WACC"
    assert m.row_of("de_market") > m.row_of("wacc")
    assert m.line("v_de").label == "Target debt / equity (debt incl. leases, at market value)"


def test_terminal_value_implied_return_on_new_capital(project: Path) -> None:
    m, _ = _full(project)
    last = m.n - 1
    reinvestment = 1 - m.value("fcff", last) / m.value("dcf_nopat", last)
    assert m.value("tv_ronic", None) == pytest.approx(0.04 / reinvestment)
    assert m.line("tv_ronic").fmt == Fmt.PCT
    assert m.line("exit_multiple").label == "Exit EV / EBITDA multiple (applied to final-year EBITDA)"


def test_comps_net_debt_column_includes_leases_and_nci(project: Path) -> None:
    inputs = load_inputs(project)
    assert inputs.valuation is not None
    header = comps_layout(inputs, inputs.valuation)[0]
    assert isinstance(header, Header) and header.sheet == COMPS_S
    assert (5, "Net debt incl. leases + NCI") in header.columns
