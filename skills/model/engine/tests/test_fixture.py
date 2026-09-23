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
