"""Shared fixture: Acme Alimentos, a small fictional company (MXN millions).

The balance-sheet identity and the net-income tie hold every year; historical
cash, equity and PP&E roll-forwards are NOT consistent (not needed by any check).
"""

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
