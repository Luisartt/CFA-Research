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
        Line("dcf_new_leases", "Less: new leases (IFRS 16, = lease principal repaid)", DCF_S,
             fcst=R("lease_principal_paid")),
        Line("dcf_nwc", "Plus: change in working capital", DCF_S, fcst=R("change_nwc")),
        Line("fcff", "Free cash flow to the firm", DCF_S, style=Style.TOTAL,
             fcst=R("dcf_nopat") + R("dcf_da") - R("dcf_capex") - R("dcf_new_leases") + R("dcf_nwc")),
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
