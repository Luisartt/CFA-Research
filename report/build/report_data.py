"""Numbers behind the report charts and tables, one place. Sources are in each block; nothing is typed twice.

Basis: the valuation is the CONSOLIDATED DCF (valuation/inputs/consolidated_results.json). The ratio table and the
appendix statements are the three-statement model v7 on v3 drivers ("engine basis", report/data/statements_v7.json).
"""

from __future__ import annotations

import json

from report_style import DATA, ROOT

CONS = json.loads((ROOT / "valuation" / "inputs" / "consolidated_results.json").read_text(encoding="utf-8"))
ST = json.loads((DATA / "statements_v7.json").read_text(encoding="utf-8"))
PEERS = json.loads((DATA / "peers_v3.json").read_text(encoding="utf-8"))
LEV = json.loads((DATA / "levers.json").read_text(encoding="utf-8"))

RUN = CONS["consolidated"]["run"]
STATE = CONS["consolidated"]["state"]

# ---- market data (16-Oct-2026) -------------------------------------------------------------------------------------
PRICE = 58.60                       # BMV official close 16-Oct-2026 (valuation/valuation-outputs.yaml)
PRICE_DATE = "16-Oct-2026"
SHARES_M = 4294.943715              # outstanding shares, million
DPS_LAST = 1.075                    # FY2026 dividend paid 13-May-2026
DPS_NEXT = 1.05                     # consensus DPS FY2027E
RANGE_52W = (53.03, 68.67)
TARGETS = {"mean": 70.17, "median": 69.50, "low": 51.0, "high": 87.0, "n": 12}   # S&P Capital IQ consensus
CONSENSUS_REC = 2.58                # 1 = Buy ... 5 = Sell
FREE_FLOAT = 27.63

# ---- segments FY2025 (MXN m): IA25-EEFF p.85-86; shares: 4T25 release p.4 and Celebramos p.17 --------------------
SEG_KEYS = ["na", "mx", "eaa", "latam"]
SEG_SALES = {"na": 190211, "mx": 154809, "eaa": 54214, "latam": 44120}
SEG_EBITDA = {"na": 17117, "mx": 31630, "eaa": 5830, "latam": 3552}
SHARE_SALES = {"na": 44.6, "mx": 32.4, "eaa": 12.7, "latam": 10.3}
SHARE_EBITDA = {"na": 28.8, "mx": 55.4, "eaa": 9.8, "latam": 6.0}
SEG_MARGIN = {"na": 9.0, "mx": 20.4, "eaa": 10.8, "latam": 8.1}
PLANTS = {"na": 77, "mx": 38, "eaa": 92, "latam": 42}

# ---- consolidated history (MXN m) ---------------------------------------------------------------------------------
YEARS_H = [2021, 2022, 2023, 2024, 2025]
REV_H = [338792, 398706, 399879, 408335, 426952]
ADJ_EBITDA_H = [47372, 53446, 54942, 55473, 59456]
ADJ_MARGIN_H = [e / r for e, r in zip(ADJ_EBITDA_H, REV_H)]
CAPEX_PPE_H = [20671, 28669, 34754, 29402, 22530]          # PP&E acquired, segment notes
CFO_H = [45776, 38851, 31411, 39907, 47753]                # cash flow from operations, statements
YEARS_F = [2026, 2027, 2028, 2029, 2030]
REV_F = RUN["rev"]
EBITDA_F = RUN["ebitda"]
MARGIN_F = [e / r for e, r in zip(EBITDA_F, REV_F)]
FCFF_F = RUN["fcff"]
CAPEX_F = RUN["capex"]

# ---- North America quarterly (wiki/Thesis/bimbo-north-america-turnaround-evidence.md, release tables) -------------
QUARTERS = ["1Q24", "2Q24", "3Q24", "4Q24", "1Q25", "2Q25", "3Q25", "4Q25", "1Q26", "2Q26"]
NA_MARGIN_Q = [8.7, 9.7, 9.5, 5.9, 7.4, 9.0, 10.4, 9.2, 8.6, 10.0]
NA_EXFX_Q = [-4.5, -3.4, -4.5, -5.7, -4.9, -4.6, -3.5, -2.9, 0.7, 1.3]
MX_GROWTH = {"FY24": 4.0, "FY25": 2.4, "1Q26": 4.5, "2Q26": 4.7}
NA_EXFX_FY = {"FY24": -4.6, "FY25": -4.0}

# ---- cost of sales by nature, FY2025 vs FY2024 (EEFF25 p.82, note 21; net sales p.13) -------------------------------
COST_LINES = [("Raw materials", 3.8), ("Salaries and benefits", 7.5), ("Freight, fuel, maintenance", 4.0),
              ("Depreciation", 13.3), ("Other five lines", 12.3)]
SALES_GROWTH_FY25 = 4.6
RAW_SHARE_SALES, RAW_SHARE_COGS = 30.4, 63.8

# ---- market (Global Data via RA25 p.107-111) -----------------------------------------------------------------------
MARKET = [("Global", 2.8, 4.7), ("North America", 4.1, 4.3), ("Latin America", 4.0, 5.5), ("Mexico", None, 3.5)]
MARKET_TYPE = {"Artisanal": 44.3, "Private label": 9.6}      # branded and other = remainder [calc]

# ---- ownership (RA25 p.181-182, register at 30-Apr-2026) -----------------------------------------------------------
OWNERS = [("Normaciel", 40.96), ("Promociones Monser", 12.78), ("Philae", 5.41), ("Grupo Valacci", 5.15),
          ("Banamex (trustee)", 3.99), ("Marlupag", 3.75)]
CONTROL_PCT = 72.03

# ---- ESG -----------------------------------------------------------------------------------------------------------
SP_YEARS = list(range(2013, 2027))
SP_TOTAL = [43, 43, 45, 45, 52, 39, 44, 50, 54, 55, 55, 61, 58, 59]
SP_E = [28, 37, 42, 44, 54, 53, 56, 58, 56, 67, 68, 72, 71, 69]
SP_S = [49, 40, 45, 42, 49, 30, 32, 44, 55, 52, 51, 61, 58, 63]
SP_G = [49, 50, 47, 49, 52, 36, 44, 49, 51, 46, 46, 46, 43, 46]
LSEG_PEERS = [("Danone", 90.82), ("Grupo Bimbo", 84.62), ("Nestle", 83.21), ("Hershey", 81.84), ("Mondelez", 79.43),
              ("Grupo Herdez", 76.87), ("General Mills", 76.10), ("Campbell's", 67.39), ("Kraft Heinz", 63.42),
              ("Flowers Foods", 59.48), ("Gruma", 50.45)]
GOV_BLOCKS = [("A Controlling shareholder", 5, 10), ("B Board independence", 10, 20), ("C Committees", 6, 8),
              ("D Related parties", 5, 8), ("E Takeover defences", 1, 10), ("F Pay, ethics, audit", 4, 8)]
SCOPE1_KT = [("2019 (restated)", 1224), ("2022", 1090), ("2023", 1141), ("2024", 1142), ("2025 prelim.", 1241)]
SCOPE3_KT = [("2019 (restated)", 11424), ("2022", 10072), ("2023", 8844), ("2024", 8131), ("2025 prelim.", 11764)]

# ---- risks (research/risks.yaml; probability and impact are team-estimate scores 1-5) --------------------------------
RISKS = [
    ("R1", "Wheat and climate input costs", 3, 4), ("R2", "North America turnaround stalls", 3, 4),
    ("R3", "Capital allocation breaks the debt hold", 3, 3), ("R4", "Mexico labour and health policy", 3, 4),
    ("R5", "Exit multiple compresses", 3, 3), ("R6", "Peso depreciates less than assumed", 3, 3),
    ("R7", "USMCA and tariffs", 3, 2), ("R8", "GLP-1 and health habits", 3, 2),
    ("R9", "Controlled-company governance", 4, 2), ("R10", "Canada Bread class actions", 2, 1),
    ("R11", "US multi-employer pensions", 2, 1), ("R12", "Water stress and packaging law", 4, 1),
    ("R13", "Cyber attack", 2, 2), ("R14", "Argentina and Venezuela", 2, 1),
]

# ---- statement helpers ---------------------------------------------------------------------------------------------
YEARS_ALL = ST["years"]


def stmt(sheet: str, label: str, year: int):
    return ST["sheets"][sheet][label][YEARS_ALL.index(year)]


def stmt_row(sheet: str, label: str, years):
    return [ST["sheets"][sheet][label][YEARS_ALL.index(y)] for y in years]


def f0(x) -> str:
    return "n/a" if x is None else f"{x:,.0f}"


def f1(x) -> str:
    return "n/a" if x is None else f"{x:,.1f}"


def f2(x) -> str:
    return "n/a" if x is None else f"{x:,.2f}"


def pct1(x) -> str:
    return "n/a" if x is None else f"{x * 100:.1f}%"


def mult(x) -> str:
    return "n/a" if x is None else f"{x:.2f}x"


# ---- key valuation numbers used in the prose (the fact-check script compares the sections against these) -----------
FACTS = {
    "price": f"{PRICE:.2f}",
    "wacc": f"{RUN['wacc'] * 100:.2f}%",
    "ke": f"{RUN['ke'] * 100:.2f}%",
    "beta": f"{RUN['beta_l']:.3f}",
    "dcf_exit": f"{RUN['ps_exit']:.2f}",
    "dcf_gordon": f"{RUN['ps_gordon_ronic']:.2f}",
    "dcf_gordon_naive": f"{RUN['ps_gordon_naive']:.2f}",
    "exit_mult": f"{STATE['exit_mult']:.2f}x",
    "tv_share": f"{RUN['tv_share_exit'] * 100:.0f}%",
    "exp_return": f"{RUN['exp_return_exit'] * 100:.1f}%",
    "target12m": f"{RUN['target12m_exit']:.2f}",
    "reverse_multiple": f"{LEV['reverse_multiple']:.2f}x",
    "hold_low_mult": f"{LEV['bands']['clean_low']['multiple']:.2f}x",
    "hold_high_mult": f"{LEV['bands']['clean_high']['multiple']:.2f}x",
    "crp": f"{STATE['crp'] * 100:.2f}%",
    "rf": f"{STATE['rf'] * 100:.2f}%",
}

if __name__ == "__main__":
    for k, v in FACTS.items():
        print(f"{k:18s} {v}")
