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
    "share_price", "upside_gordon", "upside_exit", "target_12m_gordon", "dps_next", "tv_ronic", "de_market",
    "tv_share_gordon", "implied_exit_multiple",
    "implied_g_exit", "implied_g", "price_comps_ev_ebitda", "price_comps_pe",
)
SUMMARY_RATIOS: tuple[str, ...] = (
    "r_revenue_growth", "r_gross_margin", "r_ebitda_margin", "r_ebit_margin", "r_net_margin",
    "r_fcf_margin", "r_roe", "r_roic", "r_net_debt_ebitda", "r_interest_cover", "r_ccc",
)


def _clean(value: float) -> float | None:
    return round(value, 6) if math.isfinite(value) else None


def _series(model: Model, key: str) -> dict[str, float | None]:
    return {
        str(year): None if isinstance(model.cell(key, t), BlankCell) else _clean(model.value(key, t))
        for t, year in enumerate(model.inputs.years)
    }


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
        "football": _football(model),
        "sensitivity": _sensitivity(model),
        "checks": [
            {"check": r.label, "year": None if r.period is None else inputs.years[r.period], "status": r.status}
            for r in results
        ],
        "warnings": list(inputs.warnings),
    }
