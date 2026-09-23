"""Canonical line items the engine understands (annual, non-financial companies).

The financials skill maps every reported figure to one of these keys. Costs,
capex, taxes and dividends are positive numbers; formulas subtract them.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Statement(Enum):
    IS = "IS"
    BS = "BS"
    CF = "CF"
    CHECK = "CHECK"


@dataclass(frozen=True)
class ChartItem:
    key: str
    label: str
    statement: Statement
    required: bool
    meaning: str


CHART: tuple[ChartItem, ...] = (
    ChartItem("revenue", "Revenue", Statement.IS, True, "Net sales or total revenue"),
    ChartItem("cogs", "Cost of sales", Statement.IS, True, "Positive; includes D&A if the company reports it there"),
    ChartItem("opex", "Operating expenses (net)", Statement.IS, True, "SG&A plus other operating expenses, net of other operating income; positive"),
    ChartItem("da", "Depreciation and amortization", Statement.CF, True, "From the cash-flow statement; already inside cogs/opex"),
    ChartItem("interest_expense", "Interest expense", Statement.IS, True, "Positive; includes lease interest under IFRS 16"),
    ChartItem("interest_income", "Interest income", Statement.IS, False, "Positive"),
    ChartItem("other_financial_net", "Other financial result, net", Statement.IS, False, "FX, derivatives, associates; income positive, loss negative"),
    ChartItem("income_tax", "Income tax", Statement.IS, True, "Positive = expense"),
    ChartItem("nci_income", "Net income to non-controlling interests", Statement.IS, False, "Positive"),
    ChartItem("shares_diluted", "Diluted shares", Statement.IS, True, "Weighted-average diluted shares, same units as the model"),
    ChartItem("cash", "Cash and equivalents", Statement.BS, True, "Including short-term investments treated as cash"),
    ChartItem("receivables", "Accounts receivable", Statement.BS, True, "Trade receivables, net"),
    ChartItem("inventory", "Inventories", Statement.BS, False, "Net of allowances"),
    ChartItem("other_current_assets", "Other current assets", Statement.BS, False, "Everything else current"),
    ChartItem("ppe_net", "PP&E and right-of-use assets, net", Statement.BS, True, "Net of depreciation"),
    ChartItem("intangibles_goodwill", "Intangibles and goodwill", Statement.BS, False, "Net"),
    ChartItem("other_noncurrent_assets", "Other non-current assets", Statement.BS, False, "Deferred taxes, investments, other"),
    ChartItem("payables", "Accounts payable", Statement.BS, True, "Trade payables"),
    ChartItem("other_current_liabilities", "Other current liabilities", Statement.BS, False, "Excluding debt and leases"),
    ChartItem("debt_short", "Short-term debt", Statement.BS, False, "Including the current portion of long-term debt"),
    ChartItem("debt_long", "Long-term debt", Statement.BS, False, "Non-current borrowings"),
    ChartItem("lease_liabilities", "Lease liabilities", Statement.BS, False, "Current plus non-current"),
    ChartItem("other_noncurrent_liabilities", "Other non-current liabilities", Statement.BS, False, "Deferred taxes, provisions, other"),
    ChartItem("equity_parent", "Shareholders' equity", Statement.BS, True, "Attributable to the parent"),
    ChartItem("nci_equity", "Non-controlling interests (equity)", Statement.BS, False, "Minority interest in equity"),
    ChartItem("cfo", "Cash flow from operations", Statement.CF, True, "As reported"),
    ChartItem("capex", "Capital expenditures", Statement.CF, True, "Positive; PP&E plus intangible purchases"),
    ChartItem("dividends_paid", "Dividends paid", Statement.CF, False, "Positive; to parent shareholders"),
    ChartItem("lease_principal_paid", "Lease principal paid", Statement.CF, False,
              "Principal of lease liabilities paid (IFRS 16); positive"),
    ChartItem("total_assets_reported", "Total assets as reported", Statement.CHECK, False, "Used only to check the mapping"),
    ChartItem("net_income_reported", "Net income as reported", Statement.CHECK, False, "Used only to check the mapping"),
)

BY_KEY: dict[str, ChartItem] = {item.key: item for item in CHART}
REQUIRED_KEYS: frozenset[str] = frozenset(item.key for item in CHART if item.required)
TAGS: frozenset[str] = frozenset({"sourced", "guidance", "assumption", "calc", "unverified"})
SEGMENT_PREFIX = "seg_"

DRIVER_KEYS: tuple[str, ...] = (
    "revenue_growth",
    "gross_margin",
    "opex_pct_revenue",
    "da_pct_revenue",
    "amort_pct_revenue",
    "capex_pct_revenue",
    "lease_principal_pct_revenue",
    "dso",
    "dio",
    "dpo",
    "other_ca_pct_revenue",
    "other_cl_pct_revenue",
    "tax_rate",
    "interest_rate_debt",
    "interest_rate_cash",
    "payout_ratio",
    "nci_share",
    "net_new_debt",
    "shares_growth",
    "min_cash",
)
ZERO_DEFAULT_DRIVERS: frozenset[str] = frozenset(
    {"net_new_debt", "shares_growth", "amort_pct_revenue"}
)
