"""Model definition for Drivers, IS, BS, CF, Schedules and Ratios.

Sign convention: costs, capex, taxes and dividends are positive and formulas
subtract them. Interest is charged on opening balances, so there are no
circular references. A revolver keeps cash at or above the minimum balance.
D&A reduces PP&E only; intangibles, other non-current items, short-term debt
and leases are held flat.
"""

from __future__ import annotations

from dataclasses import dataclass

from .chart import SEGMENT_PREFIX, ZERO_DEFAULT_DRIVERS
from .expr import At, Expr, Num, Ref, fn
from .inputs import ModelInputs
from .spec import OBSERVED, CellSpec, Fmt, Header, Inputs, LayoutItem, Line, Style

R = Ref
DRV, IS, BS, CF, SCH, RAT = "Drivers", "IS", "BS", "CF", "Schedules", "Ratios"
DAYS_IN_YEAR = 365


def _growth(key: str) -> Expr:
    return R(key) / R(key, 1) - 1


@dataclass(frozen=True)
class DriverDef:
    key: str
    label: str
    fmt: Fmt
    hist: Expr  # the historical value of the driver, shown next to the forecast inputs


DRIVER_DEFS: tuple[DriverDef, ...] = (
    DriverDef("revenue_growth", "Revenue growth", Fmt.PCT, _growth("revenue")),
    DriverDef("gross_margin", "Gross margin", Fmt.PCT, R("gross_profit") / R("revenue")),
    DriverDef("opex_pct_revenue", "Operating expenses / revenue", Fmt.PCT, R("opex") / R("revenue")),
    DriverDef("da_pct_revenue", "D&A / revenue", Fmt.PCT, R("da") / R("revenue")),
    DriverDef("capex_pct_revenue", "Capex / revenue", Fmt.PCT, R("capex") / R("revenue")),
    DriverDef("dso", "Receivable days (DSO)", Fmt.DAYS, R("receivables") / R("revenue") * DAYS_IN_YEAR),
    DriverDef("dio", "Inventory days (DIO)", Fmt.DAYS, R("inventory") / R("cogs") * DAYS_IN_YEAR),
    DriverDef("dpo", "Payable days (DPO)", Fmt.DAYS, R("payables") / R("cogs") * DAYS_IN_YEAR),
    DriverDef("other_ca_pct_revenue", "Other current assets / revenue", Fmt.PCT, R("other_current_assets") / R("revenue")),
    DriverDef("other_cl_pct_revenue", "Other current liabilities / revenue", Fmt.PCT, R("other_current_liabilities") / R("revenue")),
    DriverDef("tax_rate", "Effective tax rate", Fmt.PCT, R("income_tax") / R("ebt")),
    DriverDef("interest_rate_debt", "Interest rate on opening debt", Fmt.PCT, R("interest_expense") / R("total_debt", 1)),
    DriverDef("interest_rate_cash", "Interest rate on opening cash", Fmt.PCT, R("interest_income") / R("cash", 1)),
    DriverDef("payout_ratio", "Dividend payout ratio", Fmt.PCT, R("dividends_paid") / R("net_income_parent")),
    DriverDef("nci_share", "Non-controlling share of net income", Fmt.PCT, R("nci_income") / R("net_income")),
    DriverDef("net_new_debt", "Net new long-term debt", Fmt.MONEY, R("debt_long") - R("debt_long", 1)),
    DriverDef("shares_growth", "Diluted share count growth", Fmt.PCT, _growth("shares_diluted")),
    DriverDef("min_cash", "Minimum cash balance", Fmt.MONEY, R("cash")),
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


def _driver_line(key: str, label: str, fmt: Fmt, hist: Expr, inputs: ModelInputs) -> Line:
    given = inputs.drivers.get(key)
    fcst: CellSpec
    if given is not None:
        fcst = Inputs(given.values)
        notes = (given.tag, given.rationale, given.pillar)
    elif key in ZERO_DEFAULT_DRIVERS:
        fcst = Inputs(tuple(0.0 for _ in inputs.fcst_years))
        notes = ("assumption", "engine default: zero", "")
    else:
        fcst = At(key, inputs.h - 1)
        notes = ("assumption", "engine default: held at last actual", "")
    return Line(key, label, DRV, fmt, hist=hist, fcst=fcst, notes=notes)


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
        _both("ebitda", "EBITDA", IS, R("ebit") + R("da"), style=Style.SUBTOTAL),
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
        Line("intangibles_goodwill", "Intangibles and goodwill", BS, hist=OBSERVED, fcst=R("intangibles_goodwill", 1)),
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
        Line("nci_equity", "Non-controlling interests", BS, hist=OBSERVED, fcst=R("nci_equity", 1) + R("nci_income")),
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
        Line("cf_net_new_debt", "Net debt issued / (repaid)", CF, fcst=R("net_new_debt")),
        Line("dividends_paid", "Dividends paid", CF, hist=OBSERVED, fcst=R("net_income_parent") * R("payout_ratio")),
        Line("cff_before_revolver", "Cash flow from financing before revolver", CF, style=Style.SUBTOTAL,
             fcst=R("cf_net_new_debt") - R("dividends_paid")),
        Header(CF, "Cash and revolver"),
        Line("cash_begin", "Opening cash", CF, fcst=R("cash", 1)),
        Line("cash_before_revolver", "Cash before revolver", CF,
             fcst=R("cash_begin") + R("cfo") + R("cfi") + R("cff_before_revolver")),
        Line("revolver_draw", "Revolver draw / (repayment)", CF,
             fcst=fn("MAX", R("min_cash") - R("cash_before_revolver"), -R("revolver", 1))),
        Line("cash_end", "Closing cash", CF, style=Style.TOTAL, fcst=R("cash_before_revolver") + R("revolver_draw")),
        Header(CF, "Memo"),
        _both("fcf", "Free cash flow (CFO - capex)", CF, R("cfo") - R("capex")),
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
        Header(SCH, "PP&E roll-forward"),
        Line("sch_ppe_begin", "Opening PP&E", SCH, fcst=R("ppe_net", 1)),
        Line("sch_capex", "Plus: capex", SCH, fcst=R("capex")),
        Line("sch_da", "Less: D&A", SCH, fcst=R("da")),
        Line("sch_ppe_end", "Closing PP&E", SCH, style=Style.TOTAL,
             fcst=R("sch_ppe_begin") + R("sch_capex") - R("sch_da")),
        Header(SCH, "Working capital"),
        Line("sch_receivables", "Receivables = revenue x DSO / 365", SCH, fcst=R("revenue") * R("dso") / DAYS_IN_YEAR),
        Line("sch_inventory", "Inventories = cost of sales x DIO / 365", SCH, fcst=R("cogs") * R("dio") / DAYS_IN_YEAR),
        Line("sch_payables", "Payables = cost of sales x DPO / 365", SCH, fcst=R("cogs") * R("dpo") / DAYS_IN_YEAR),
        Header(SCH, "Debt and interest"),
        Line("sch_debt_long_begin", "Opening long-term debt", SCH, fcst=R("debt_long", 1)),
        Line("sch_net_new_debt", "Plus: net new debt", SCH, fcst=R("net_new_debt")),
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
        _both("r_roic", "ROIC = EBIT x (1 - tax rate) / (equity + net debt)", RAT,
              R("ebit") * (1 - R("tax_rate")) / (R("total_equity") + R("net_debt")), fmt=Fmt.PCT),
        Header(RAT, "Leverage and working capital"),
        _both("r_net_debt_ebitda", "Net debt / EBITDA", RAT, R("net_debt") / R("ebitda"), fmt=Fmt.MULT),
        _both("r_interest_cover", "EBIT / interest expense", RAT, R("ebit") / R("interest_expense"), fmt=Fmt.MULT),
        _both("r_ccc", "Cash conversion cycle (days) = DSO + DIO - DPO", RAT, R("dso") + R("dio") - R("dpo"),
              fmt=Fmt.DAYS),
    ]
