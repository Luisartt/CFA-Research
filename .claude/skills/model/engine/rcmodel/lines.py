"""Model definition for Drivers, IS, BS, CF, Schedules and Ratios.

Sign convention: costs, capex, taxes and dividends are positive and formulas
subtract them. Interest is charged on opening balances, so there are no
circular references. A revolver keeps cash at or above the minimum balance.

Total D&A splits into amortization (reduces intangibles, never below zero) and
depreciation (reduces PP&E). Leases follow IFRS 16: principal repaid is a
financing outflow, and the leases renewed each year (assumed equal to the
principal repaid) are a non-cash addition to right-of-use assets, so the lease
liability stays flat and stays in net debt. Other non-current items and
short-term debt are held flat; long-term debt never goes below zero. Dividends
are never negative.

Historical ratios whose denominator can be zero read 0 instead of #DIV/0!;
the tax rate and payout ratio also read 0 in a loss year.
"""

from __future__ import annotations

from dataclasses import dataclass

from .chart import DEFAULT_FROM_LAST_ACTUAL, SEGMENT_PREFIX, ZERO_DEFAULT_DRIVERS
from .expr import At, Expr, Num, Ref, cmp, fn, iff
from .inputs import ModelInputs
from .spec import OBSERVED, CellSpec, Fmt, Header, Inputs, LayoutItem, Line, Style

R = Ref
DRV, IS, BS, CF, SCH, RAT = "Drivers", "IS", "BS", "CF", "Schedules", "Ratios"
DAYS_IN_YEAR = 365


def _growth(key: str) -> Expr:
    return R(key) / R(key, 1) - 1


def _safe_ratio(numerator: Expr, denominator: Expr, *, positive_only: bool = False) -> Expr:
    """numerator / denominator, or 0 when the denominator is 0 (or not positive, if `positive_only`)."""
    return iff(cmp(denominator, ">" if positive_only else "<>", 0), numerator / denominator, 0)


@dataclass(frozen=True)
class DriverDef:
    key: str
    label: str
    fmt: Fmt
    hist: Expr | None  # the historical value shown next to the forecast inputs; None = no history (blank)


DRIVER_DEFS: tuple[DriverDef, ...] = (
    DriverDef("revenue_growth", "Revenue growth", Fmt.PCT, _growth("revenue")),
    DriverDef("gross_margin", "Gross margin", Fmt.PCT, R("gross_profit") / R("revenue")),
    DriverDef("opex_pct_revenue", "Operating expenses / revenue", Fmt.PCT, R("opex") / R("revenue")),
    DriverDef("da_pct_revenue", "D&A / revenue", Fmt.PCT, R("da") / R("revenue")),
    DriverDef("amort_pct_revenue", "Amortization of intangibles / revenue (part of D&A)", Fmt.PCT, None),
    DriverDef("capex_pct_revenue", "Capex / revenue", Fmt.PCT, R("capex") / R("revenue")),
    DriverDef("lease_principal_pct_revenue", "Lease principal paid / revenue", Fmt.PCT,
              _safe_ratio(R("lease_principal_paid"), R("revenue"))),
    DriverDef("dso", "Receivable days (DSO)", Fmt.DAYS, R("receivables") / R("revenue") * DAYS_IN_YEAR),
    DriverDef("dio", "Inventory days (DIO)", Fmt.DAYS, _safe_ratio(R("inventory") * DAYS_IN_YEAR, R("cogs"))),
    DriverDef("dpo", "Payable days (DPO)", Fmt.DAYS, _safe_ratio(R("payables") * DAYS_IN_YEAR, R("cogs"))),
    DriverDef("other_ca_pct_revenue", "Other current assets / revenue", Fmt.PCT, R("other_current_assets") / R("revenue")),
    DriverDef("other_cl_pct_revenue", "Other current liabilities / revenue", Fmt.PCT, R("other_current_liabilities") / R("revenue")),
    DriverDef("tax_rate", "Effective tax rate", Fmt.PCT, _safe_ratio(R("income_tax"), R("ebt"), positive_only=True)),
    DriverDef("interest_rate_debt", "Interest rate on opening debt", Fmt.PCT,
              _safe_ratio(R("interest_expense"), R("total_debt", 1))),
    DriverDef("interest_rate_cash", "Interest rate on opening cash", Fmt.PCT,
              _safe_ratio(R("interest_income"), R("cash", 1))),
    DriverDef("payout_ratio", "Dividend payout ratio", Fmt.PCT,
              _safe_ratio(R("dividends_paid"), R("net_income_parent"), positive_only=True)),
    DriverDef("nci_share", "Non-controlling share of net income", Fmt.PCT, _safe_ratio(R("nci_income"), R("net_income"))),
    DriverDef("net_new_debt", "Net new long-term debt", Fmt.MONEY, R("debt_long") - R("debt_long", 1)),
    DriverDef("shares_growth", "Diluted share count growth", Fmt.PCT, _growth("shares_diluted")),
    DriverDef("min_cash", "Minimum cash balance", Fmt.MONEY, None),
)


def model_layout(inputs: ModelInputs) -> list[LayoutItem]:
    return [
        *driver_layout(inputs),
        *income_statement(inputs),
        *balance_sheet(inputs),
        *cash_flow(),
        *schedules(inputs),
        *ratios(),
    ]


def _driver_line(key: str, label: str, fmt: Fmt, hist: Expr | None, inputs: ModelInputs) -> Line:
    given = inputs.drivers.get(key)
    fcst: CellSpec
    if given is not None:
        fcst = Inputs(given.values)
        notes = (given.tag, given.rationale, _pillar(given.pillar))
    elif key in ZERO_DEFAULT_DRIVERS:
        fcst = Inputs(tuple(0.0 for _ in inputs.fcst_years))
        notes = ("assumption", "engine default: zero", "")
    elif key in DEFAULT_FROM_LAST_ACTUAL:
        source = DEFAULT_FROM_LAST_ACTUAL[key]
        fcst = At(source, inputs.h - 1)
        notes = ("assumption", f"engine default: last actual {source}", "")
    else:
        fcst = At(key, inputs.h - 1)
        notes = ("assumption", "engine default: held at last actual", "")
    return Line(key, label, DRV, fmt, hist=hist, fcst=fcst, notes=notes)


def _pillar(text: str) -> str:
    """'1' -> 'Pillar 1', so Excel shows a label rather than a number stored as text."""
    stripped = text.strip()
    if not stripped or stripped.lower().startswith("pillar"):
        return stripped
    return f"Pillar {stripped}"


def driver_layout(inputs: ModelInputs) -> list[LayoutItem]:
    n = inputs.n
    columns = ((3 + n, "Tag"), (4 + n, "Rationale"), (5 + n, "Thesis pillar"))
    items: list[LayoutItem] = [Header(DRV, "Operating drivers", columns=columns)]
    items += [_driver_line(d.key, d.label, d.fmt, d.hist, inputs) for d in DRIVER_DEFS]
    if inputs.segments:
        items.append(Header(DRV, "Revenue segments"))
        for segment in inputs.segments:
            line = f"{SEGMENT_PREFIX}{segment.key}"
            items.append(_driver_line(f"{line}_growth", f"{segment.label} growth", Fmt.PCT, _growth(line), inputs))
    return items


def _both(key: str, label: str, sheet: str, expr: Expr, fmt: Fmt = Fmt.MONEY, style: Style = Style.NORMAL) -> Line:
    return Line(key, label, sheet, fmt, style=style, hist=expr, fcst=expr)


def income_statement(inputs: ModelInputs) -> list[LayoutItem]:
    revenue_fcst: Expr
    if inputs.segments:
        revenue_fcst = fn("SUM", *[R(f"{SEGMENT_PREFIX}{s.key}") for s in inputs.segments])
    else:
        revenue_fcst = R("revenue", 1) * (1 + R("revenue_growth"))
    zeros = Inputs(tuple(0.0 for _ in inputs.fcst_years))
    items: list[LayoutItem] = [
        Header(IS, "Income statement"),
        Line("revenue", "Revenue", IS, style=Style.SUBTOTAL, hist=OBSERVED, fcst=revenue_fcst),
        Line("cogs", "Cost of sales", IS, hist=OBSERVED, fcst=R("revenue") * (1 - R("gross_margin"))),
        _both("gross_profit", "Gross profit", IS, R("revenue") - R("cogs"), style=Style.SUBTOTAL),
        Line("opex", "Operating expenses (net)", IS, hist=OBSERVED, fcst=R("revenue") * R("opex_pct_revenue")),
        _both("ebit", "EBIT", IS, R("gross_profit") - R("opex"), style=Style.SUBTOTAL),
        Line("interest_expense", "Interest expense", IS, hist=OBSERVED, fcst=R("sch_interest_expense")),
        Line("interest_income", "Interest income", IS, hist=OBSERVED, fcst=R("interest_rate_cash") * R("cash", 1)),
        Line("other_financial_net", "Other financial result, net", IS, hist=OBSERVED, fcst=zeros,
             notes=("assumption: held at zero",)),
        _both("ebt", "Pre-tax income", IS,
              R("ebit") - R("interest_expense") + R("interest_income") + R("other_financial_net"), style=Style.SUBTOTAL),
        Line("income_tax", "Income tax", IS, hist=OBSERVED, fcst=R("ebt") * R("tax_rate")),
        _both("net_income", "Net income", IS, R("ebt") - R("income_tax"), style=Style.TOTAL),
        Line("nci_income", "Attributable to non-controlling interests", IS, hist=OBSERVED,
             fcst=R("net_income") * R("nci_share")),
        _both("net_income_parent", "Net income to shareholders", IS, R("net_income") - R("nci_income"), style=Style.TOTAL),
        Header(IS, "Per share and memo"),
        Line("shares_diluted", "Diluted shares", IS, Fmt.SHARES, hist=OBSERVED,
             fcst=R("shares_diluted", 1) * (1 + R("shares_growth"))),
        _both("eps", "Diluted EPS", IS, R("net_income_parent") / R("shares_diluted"), fmt=Fmt.PRICE),
        Line("da", "D&A (included in costs above)", IS, hist=OBSERVED, fcst=R("revenue") * R("da_pct_revenue")),
        _both("ebitda", "EBITDA (post-IFRS 16)", IS, R("ebit") + R("da"), style=Style.SUBTOTAL),
    ]
    if "net_income_reported" in inputs.history:
        items.append(Line("net_income_reported", "Net income as reported (check)", IS, hist=OBSERVED))
    return items


def balance_sheet(inputs: ModelInputs) -> list[LayoutItem]:
    items: list[LayoutItem] = [
        Header(BS, "Assets"),
        Line("cash", "Cash and equivalents", BS, hist=OBSERVED, fcst=R("cash_end")),
        Line("receivables", "Accounts receivable", BS, hist=OBSERVED, fcst=R("sch_receivables")),
        Line("inventory", "Inventories", BS, hist=OBSERVED, fcst=R("sch_inventory")),
        Line("other_current_assets", "Other current assets", BS, hist=OBSERVED,
             fcst=R("revenue") * R("other_ca_pct_revenue")),
        _both("total_current_assets", "Total current assets", BS,
              R("cash") + R("receivables") + R("inventory") + R("other_current_assets"), style=Style.SUBTOTAL),
        Line("ppe_net", "PP&E and right-of-use assets, net", BS, hist=OBSERVED, fcst=R("sch_ppe_end")),
        Line("intangibles_goodwill", "Intangibles and goodwill", BS, hist=OBSERVED,
             fcst=R("intangibles_goodwill", 1) - R("sch_amort")),
        Line("other_noncurrent_assets", "Other non-current assets", BS, hist=OBSERVED,
             fcst=R("other_noncurrent_assets", 1)),
        _both("total_assets", "Total assets", BS,
              R("total_current_assets") + R("ppe_net") + R("intangibles_goodwill") + R("other_noncurrent_assets"),
              style=Style.TOTAL),
        Header(BS, "Liabilities and equity"),
        Line("payables", "Accounts payable", BS, hist=OBSERVED, fcst=R("sch_payables")),
        Line("other_current_liabilities", "Other current liabilities", BS, hist=OBSERVED,
             fcst=R("revenue") * R("other_cl_pct_revenue")),
        Line("debt_short", "Short-term debt", BS, hist=OBSERVED, fcst=R("debt_short", 1)),
        Line("revolver", "Revolving credit facility", BS, hist=Num(0.0), fcst=R("sch_revolver_end")),
        _both("total_current_liabilities", "Total current liabilities", BS,
              R("payables") + R("other_current_liabilities") + R("debt_short") + R("revolver"), style=Style.SUBTOTAL),
        Line("debt_long", "Long-term debt", BS, hist=OBSERVED, fcst=R("sch_debt_long_end")),
        Line("lease_liabilities", "Lease liabilities", BS, hist=OBSERVED, fcst=R("lease_liabilities", 1)),
        Line("other_noncurrent_liabilities", "Other non-current liabilities", BS, hist=OBSERVED,
             fcst=R("other_noncurrent_liabilities", 1)),
        _both("total_liabilities", "Total liabilities", BS,
              R("total_current_liabilities") + R("debt_long") + R("lease_liabilities") + R("other_noncurrent_liabilities"),
              style=Style.SUBTOTAL),
        Line("equity_parent", "Shareholders' equity", BS, hist=OBSERVED,
             fcst=R("equity_parent", 1) + R("net_income_parent") - R("dividends_paid")),
        Line("nci_equity", "Non-controlling interests", BS, hist=OBSERVED,
             fcst=R("nci_equity", 1) + R("nci_income") - R("nci_dividends")),
        _both("total_equity", "Total equity", BS, R("equity_parent") + R("nci_equity"), style=Style.SUBTOTAL),
        _both("total_liabilities_equity", "Total liabilities and equity", BS,
              R("total_liabilities") + R("total_equity"), style=Style.TOTAL),
        Header(BS, "Memo"),
        _both("total_debt", "Total debt incl. leases and revolver", BS,
              R("debt_short") + R("revolver") + R("debt_long") + R("lease_liabilities")),
        _both("net_debt", "Net debt", BS, R("total_debt") - R("cash")),
    ]
    if "total_assets_reported" in inputs.history:
        items.append(Line("total_assets_reported", "Total assets as reported (check)", BS, hist=OBSERVED))
    return items


def cash_flow() -> list[LayoutItem]:
    def change(key: str) -> Expr:
        return R(key) - R(key, 1)

    nwc = -(change("receivables") + change("inventory") + change("other_current_assets")
            - change("payables") - change("other_current_liabilities"))
    return [
        Header(CF, "Operating activities"),
        Line("cf_net_income", "Net income", CF, fcst=R("net_income")),
        Line("cf_da", "D&A", CF, fcst=R("da")),
        _both("change_nwc", "Change in working capital", CF, nwc),
        Line("cfo", "Cash flow from operations", CF, style=Style.SUBTOTAL, hist=OBSERVED,
             fcst=R("cf_net_income") + R("cf_da") + R("change_nwc")),
        Header(CF, "Investing activities"),
        Line("capex", "Capital expenditures", CF, hist=OBSERVED, fcst=R("revenue") * R("capex_pct_revenue")),
        Line("cfi", "Cash flow from investing", CF, style=Style.SUBTOTAL, fcst=-R("capex")),
        Header(CF, "Financing activities"),
        Line("cf_net_new_debt", "Net debt issued / (repaid)", CF, fcst=R("sch_net_new_debt")),
        Line("dividends_paid", "Dividends paid", CF, hist=OBSERVED,
             fcst=fn("MAX", 0, R("net_income_parent") * R("payout_ratio"))),
        Line("lease_principal_paid", "Lease principal paid (IFRS 16)", CF, hist=OBSERVED,
             fcst=R("revenue") * R("lease_principal_pct_revenue")),
        Line("nci_dividends", "Dividends to non-controlling interests", CF,
             fcst=fn("MAX", 0, R("nci_income") * R("payout_ratio"))),
        Line("cff_before_revolver", "Cash flow from financing before revolver", CF, style=Style.SUBTOTAL,
             fcst=R("cf_net_new_debt") - R("dividends_paid") - R("lease_principal_paid") - R("nci_dividends")),
        Header(CF, "Cash and revolver"),
        Line("cash_begin", "Opening cash", CF, fcst=R("cash", 1)),
        Line("cash_before_revolver", "Cash before revolver", CF,
             fcst=R("cash_begin") + R("cfo") + R("cfi") + R("cff_before_revolver")),
        Line("revolver_draw", "Revolver draw / (repayment)", CF,
             fcst=fn("MAX", R("min_cash") - R("cash_before_revolver"), -R("revolver", 1))),
        Line("cash_end", "Closing cash", CF, style=Style.TOTAL, fcst=R("cash_before_revolver") + R("revolver_draw")),
        Header(CF, "Memo"),
        _both("fcf", "Free cash flow (CFO - capex - lease principal)", CF,
              R("cfo") - R("capex") - R("lease_principal_paid")),
    ]


def schedules(inputs: ModelInputs) -> list[LayoutItem]:
    items: list[LayoutItem] = []
    if inputs.segments:
        items.append(Header(SCH, "Revenue build"))
        for segment in inputs.segments:
            line = f"{SEGMENT_PREFIX}{segment.key}"
            items.append(Line(line, segment.label, SCH, hist=OBSERVED, fcst=R(line, 1) * (1 + R(f"{line}_growth"))))
        items.append(_both("sch_revenue_total", "Total revenue (links to IS)", SCH, R("revenue"), style=Style.SUBTOTAL))
    items += [
        Header(SCH, "Intangibles"),
        Line("sch_amort", "Amortization of intangibles", SCH,
             fcst=fn("MIN", R("revenue") * R("amort_pct_revenue"), R("intangibles_goodwill", 1))),
        Header(SCH, "PP&E and right-of-use roll-forward"),
        Line("sch_ppe_begin", "Opening PP&E", SCH, fcst=R("ppe_net", 1)),
        Line("sch_capex", "Plus: capex", SCH, fcst=R("capex")),
        Line("sch_new_leases", "Plus: new leases (non-cash, = lease principal repaid)", SCH,
             fcst=R("lease_principal_paid")),
        Line("sch_da_ppe", "Less: depreciation of PP&E", SCH, fcst=R("da") - R("sch_amort")),
        Line("sch_ppe_end", "Closing PP&E", SCH, style=Style.TOTAL,
             fcst=R("sch_ppe_begin") + R("sch_capex") + R("sch_new_leases") - R("sch_da_ppe")),
        Header(SCH, "Working capital"),
        Line("sch_receivables", "Receivables = revenue x DSO / 365", SCH, fcst=R("revenue") * R("dso") / DAYS_IN_YEAR),
        Line("sch_inventory", "Inventories = cost of sales x DIO / 365", SCH, fcst=R("cogs") * R("dio") / DAYS_IN_YEAR),
        Line("sch_payables", "Payables = cost of sales x DPO / 365", SCH, fcst=R("cogs") * R("dpo") / DAYS_IN_YEAR),
        Header(SCH, "Debt and interest"),
        Line("sch_debt_long_begin", "Opening long-term debt", SCH, fcst=R("debt_long", 1)),
        Line("sch_net_new_debt", "Plus: net new debt (repayment capped at opening balance)", SCH,
             fcst=fn("MAX", R("net_new_debt"), -R("debt_long", 1))),
        Line("sch_debt_long_end", "Closing long-term debt", SCH, style=Style.TOTAL,
             fcst=R("sch_debt_long_begin") + R("sch_net_new_debt")),
        Line("sch_revolver_begin", "Opening revolver", SCH, fcst=R("revolver", 1)),
        Line("sch_revolver_draw", "Plus: draw / (repayment)", SCH, fcst=R("revolver_draw")),
        Line("sch_revolver_end", "Closing revolver", SCH, style=Style.TOTAL,
             fcst=R("sch_revolver_begin") + R("sch_revolver_draw")),
        Line("sch_interest_expense", "Interest expense = rate x opening total debt", SCH,
             fcst=R("interest_rate_debt") * R("total_debt", 1)),
    ]
    return items


def ratios() -> list[LayoutItem]:
    average_equity = (R("equity_parent") + R("equity_parent", 1)) / 2
    return [
        Header(RAT, "Growth and margins"),
        _both("r_revenue_growth", "Revenue growth", RAT, _growth("revenue"), fmt=Fmt.PCT),
        _both("r_gross_margin", "Gross margin", RAT, R("gross_profit") / R("revenue"), fmt=Fmt.PCT),
        _both("r_ebitda_margin", "EBITDA margin", RAT, R("ebitda") / R("revenue"), fmt=Fmt.PCT),
        _both("r_ebit_margin", "EBIT margin", RAT, R("ebit") / R("revenue"), fmt=Fmt.PCT),
        _both("r_net_margin", "Net margin", RAT, R("net_income_parent") / R("revenue"), fmt=Fmt.PCT),
        _both("r_fcf_margin", "Free cash flow margin", RAT, R("fcf") / R("revenue"), fmt=Fmt.PCT),
        Header(RAT, "Returns"),
        _both("r_roe", "Return on average equity", RAT, R("net_income_parent") / average_equity, fmt=Fmt.PCT),
        _both("r_roic", "ROIC = EBIT x (1 - tax rate) / opening (equity + net debt)", RAT,
              R("ebit") * (1 - R("tax_rate")) / (R("total_equity", 1) + R("net_debt", 1)), fmt=Fmt.PCT),
        Header(RAT, "Leverage and working capital"),
        _both("r_net_debt_ebitda", "Net debt / EBITDA", RAT, R("net_debt") / R("ebitda"), fmt=Fmt.MULT),
        _both("r_interest_cover", "EBIT / interest expense", RAT, R("ebit") / R("interest_expense"), fmt=Fmt.MULT),
        _both("r_ccc", "Cash conversion cycle (days) = DSO + DIO - DPO", RAT, R("dso") + R("dio") - R("dpo"),
              fmt=Fmt.DAYS),
    ]
