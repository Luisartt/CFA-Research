"""AUDIT-FIX COPY: build analisis-dcf-2026-10-26/proyecciones/BIMBOA_statements_2021-2030_v1_auditfix.xlsx (and _auditfix_ES).

Same as build_statements_workbook.py plus the five audit fixes H-01..H-05 proposed by the AI on 2026-10-26
(analisis-dcf-2026-10-26/notas/audit_fixes_v1_2026-10-26_ES.md, sheet Audit_fixes). The original builder and workbooks are not touched.

Original docstring: build model/BIMBOA_statements_2021-2030_v1.xlsx.

Full as-reported consolidated statements of Grupo Bimbo (MXN millions):
income statement, OCI, balance sheet, cash flow and equity roll-forward,
FY2021A-FY2025A typed from the audited filings and FY2026E-FY2030E linked to the
Assumptions sheet. Subtotals are live formulas in every column; the Checks sheet
tests that the statements tie to each other. The macro sheets of
data/macro/nominal_gdp_growth_2016-2030.xlsx (Capital IQ GDP, CPI and FX) are
copied in with their formulas, and Assumptions links to them live. The
Methodology sheet (rows in methodology_rows.py) explains every forecast line.

Sources (PDF page numbers):
  IA25 = filings/annual/IA25_GB_EEFF_V10.pdf  (FY2023-FY2025; BS p.12, IS p.13,
         OCI p.14, equity p.15, CF p.16)
  RA23 = filings/bmv/Reporte Anual 2023_XBRL_VF.PDF  (FY2021-FY2022; BS p.256,
         IS p.257, OCI p.258, equity p.259, CF p.260)
Rule (data/adjustments.md): the latest report that presents a year wins, so
FY2023 comes from IA25 and FY2021-FY2022 from RA23 (restated for Ricolino).
"""
import sys
from pathlib import Path

from copy import copy

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(1, str(Path(__file__).resolve().parents[2] / "model" / "build"))  # shared modules of the original builders
import glossary_rows
import macro_es
import methodology_rows
import statements_es

ROOT = Path(__file__).resolve().parents[2]
# Usage: python build_statements_workbook.py [--lang es]
LANG = "es" if "--lang" in sys.argv and sys.argv[sys.argv.index("--lang") + 1] == "es" else "en"
OUT = ROOT / "analisis-dcf-2026-10-26" / "proyecciones" / ("BIMBOA_estados_2021-2030_v1_auditfix_ES.xlsx" if LANG == "es"
                        else "BIMBOA_statements_2021-2030_v1_auditfix.xlsx")
import audit_fix_es  # Spanish strings and sheet name of the audit-fix copy (adds to statements_es)


def t(s):
    """Label in the build language; a missing Spanish label stops the build."""
    return s if LANG == "en" else macro_es.names(statements_es.ES[s])


def sn(name):
    """Sheet name in the build language."""
    return name if LANG == "en" else statements_es.SHEETS[name]


def yl(y):
    """Year column label in the build language."""
    return y if LANG == "en" else statements_es.YEARS[y]

HIST = ["FY2021A", "FY2022A", "FY2023A", "FY2024A", "FY2025A"]
FCST = ["FY2026E", "FY2027E", "FY2028E", "FY2029E", "FY2030E"]
YEARS = HIST + FCST
COLS = [get_column_letter(i) for i in range(2, 12)]  # B..K
HC, FC = COLS[:5], COLS[5:]
TAG_COL, SRC_COL = "L", "M"

SRC = {
    "IS": "RA23 p.257 (FY21-22); IA25 p.13 (FY23-25)",
    "OCI": "RA23 p.258 (FY21-22); IA25 p.14 (FY23-25)",
    "BS": "RA23 p.256 (FY21-22); IA25 p.12 (FY23-25)",
    "CF": "RA23 p.260 (FY21-22); IA25 p.16 (FY23-25)",
    "EQ": "RA23 p.259 (FY21-22); IA25 p.15 (FY23-25)",
    "SEG": "Segment note: RA23 p.359 (FY21), p.358 (FY22); IA25 p.86 (FY23-24), p.85 (FY25)",
}

# Forecast notes for lines held at 0 (team decisions 2026-10-25, memory.md)
N_BEN = ("Forecast = 0 (team 2026-10-25): the DCF bridge already deducts pensions, provisions and derivatives "
         "as debt-like; projecting these payments in FCFF would count them twice; the liability is held at Dec-25")
N_EMPB = "forecast held at Dec-25 (team 2026-10-25): deducted as debt-like in the DCF bridge"
N_INT = ("FY2026E = 0 because releases give net interest only (inside interest expense); FY2027E onward = 0 "
         "(team 2026-10-25): not operating; FCFF excludes it and cash enters at its balance in the DCF bridge; "
         "affects net income and EPS only")
N_INTG = ("Forecast = 0 (team 2026-10-25): immaterial (Assumptions: share of PP&E purchases FY2025 and 1H26); "
          "Bimbo's fixed-asset investment is PP&E only (RA25 BMV p.143), so the capex does not include them")


# Row spec: (key, label, kind, payload, note)
#   kind "h"   section header, "i" typed input (payload = 5 historical values),
#   "f"   formula in every year column (payload = template with {c} = column,
#         {p} = previous column, and {key} = row number of another line),
#   "fh"  formula in history only, forecast left as input (payload = template),
#   "b"   blank spacer.
IS_ROWS = [
    ("h1", "Continuing operations", "h", None, ""),
    ("sales", "Net sales", "i", [338792, 398706, 399879, 408335, 426952], ""),
    ("cogs", "Cost of sales", "i", [157703, 193325, 194369, 193407, 203465], "Positive = expense"),
    ("gp", "Gross profit", "f", "={c}{sales}-{c}{cogs}", ""),
    ("dist", "Distribution and selling expenses", "i", [124422, 140455, 139477, 147628, 154866], ""),
    ("admin", "Administrative expenses", "i", [23147, 26172, 25860, 27536, 29023], ""),
    ("integ", "Integration expenses", "i", [724, 367, 288, 317, 541], ""),
    ("oth", "Other (income) expenses, net", "i", [216, -15309, 4430, 6298, 4911],
     "FY2022 includes the non-cash gain on multi-employer pension plans (MEPP)"),
    ("opex", "Total general expenses", "f", "=SUM({c}{dist}:{c}{oth})", ""),
    ("ebit", "Operating income (EBIT)", "f", "={c}{gp}-{c}{opex}", ""),
    ("b1", "", "b", None, ""),
    ("h2", "Comprehensive financing result", "h", None, ""),
    ("intexp", "Interest expense", "i", [7823, 8049, 10006, 13100, 14464], "Includes IFRS 16 lease interest"),
    ("intinc", "Interest income", "i", [-363, -740, -809, -924, -897], "Negative = income (as in the filing); " + N_INT),
    ("fx", "Foreign exchange loss, net", "i", [538, 995, 1323, 506, 384], ""),
    ("mon", "Monetary position loss (gain)", "i", [-25, -34, -73, -103, 50], ""),
    ("cif", "Total comprehensive financing result", "f", "=SUM({c}{intexp}:{c}{mon})", ""),
    ("assoc", "Share of results of associates", "i", [247, 452, 316, 464, -2], ""),
    ("pbt", "Income before taxes, continuing operations", "f", "={c}{ebit}-{c}{cif}+{c}{assoc}", ""),
    ("tax", "Income taxes", "i", [8726, 14381, 8386, 6797, 7197], ""),
    ("nicont", "Net income from continuing operations", "f", "={c}{pbt}-{c}{tax}", ""),
    ("disc", "Net income from discontinued operations, after tax", "i", [1254, 16988, -16, -194, 0],
     "Ricolino (sold 1-Nov-2022)"),
    ("ni", "Consolidated net income", "f", "={c}{nicont}+{c}{disc}", ""),
    ("b2", "", "b", None, ""),
    ("h3", "Attribution", "h", None, ""),
    ("nci", "Non-controlling interest", "i", [1466, 1575, 1445, 1499, 1813],
     "FY21-22 include discontinued NCI (30; 402)"),
    ("nictrl", "Controlling interest", "f", "={c}{ni}-{c}{nci}", ""),
    ("shares", "Weighted-average shares (millions)", "i", [4487.268, 4448.693, 4418.137, 4357.250, 4310.531],
     "Filing reports thousands; basic = diluted"),
    ("eps", "Basic EPS (MXN)", "f", "=IFERROR({c}{nictrl}/{c}{shares},0)", ""),
    ("b3", "", "b", None, ""),
    ("h4", "Memo", "h", None, ""),
    ("da", "D&A, continuing (segment note)", "i", [16126, 18038, 18929, 23051, 24838],
     "RA23 p.358-359; IA25 p.85-86 (data/financials.csv)"),
    ("ebitda", "EBITDA (EBIT + D&A)", "f", "={c}{ebit}+{c}{da}", ""),
    ("othnc", "Impairment and other non-cash items (segment note)", "hf",
     ("={SEG}!{c}{seg_i_tot}+{SEG}!{c}{seg_n_tot}", "INPUT"),
     "Mainly multi-employer pension plan (MEPP) adjustments"),
    ("adjebitda", "Adjusted EBITDA (company definition)", "f", "={c}{ebit}+{c}{da}+{c}{othnc}",
     "Company definition; in history it ties to the segment note"),
]

OCI_ROWS = [
    ("ni", "Consolidated net income", "i", [17382, 48485, 16922, 14043, 12946], "Must equal IS consolidated net income"),
    ("b1", "", "b", None, ""),
    ("h1", "Items that will not be reclassified to profit or loss", "h", None, ""),
    ("eqv", "Valuation of equity financial instruments", "i", [-112, -32, -236, -43, -118], ""),
    ("act", "Actuarial gains (losses) on defined-benefit plans", "i", [1543, 800, -349, 802, -433], ""),
    ("tax1", "Income tax", "i", [-432, -207, 164, -540, 369], ""),
    ("sub1", "Subtotal", "f", "=SUM({c}{eqv}:{c}{tax1})", ""),
    ("h2", "Items that may be reclassified to profit or loss", "h", None, ""),
    ("nih", "Net investment hedge", "i", [-723, 667, 1100, -3407, 2096], ""),
    ("cta", "Translation of foreign operations", "i", [2114, -9862, -15635, 15551, -10811], ""),
    ("cfh", "Cash-flow hedges, net change", "i", [2988, -2213, 938, 287, -1800], ""),
    ("tax2", "Income tax", "i", [-937, 142, -772, 1164, -348], ""),
    ("sub2", "Subtotal", "f", "=SUM({c}{nih}:{c}{tax2})", ""),
    ("oci", "Total other comprehensive income", "f", "={c}{sub1}+{c}{sub2}", ""),
    ("ci", "Consolidated comprehensive income", "f", "={c}{ni}+{c}{oci}", ""),
    ("cinci", "  Attributable to non-controlling interest", "i", [1470, 1155, 1540, 1677, 2012], ""),
    ("cictrl", "  Attributable to controlling interest", "f", "={c}{ci}-{c}{cinci}", ""),
]

BS_ROWS = [
    ("h1", "Current assets", "h", None, ""),
    ("cash", "Cash and cash equivalents", "i", [8748, 12313, 6353, 8057, 8535], "Must equal CF ending cash"),
    ("ar", "Trade and other receivables, net", "i", [27170, 32185, 33269, 36659, 35782], ""),
    ("inv", "Inventories", "i", [13710, 16989, 16120, 18832, 17151], ""),
    ("prep", "Prepaid expenses", "i", [2296, 928, 1378, 1371, 1798], ""),
    ("derca", "Derivative financial instruments", "i", [1293, 38, 119, 1417, 60], ""),
    ("coll", "Collateral deposits on derivatives", "i", [0, 879, 1519, 577, 459], ""),
    ("hfs", "Assets held for sale", "i", [194, 138, 156, 267, 886], ""),
    ("tca", "Total current assets", "f", "=SUM({c}{cash}:{c}{hfs})", ""),
    ("ppe", "Property, plant and equipment, net", "i", [103891, 113505, 129156, 155376, 157423], ""),
    ("rou", "Right-of-use assets, net", "i", [30754, 28477, 25848, 34220, 32757], ""),
    ("assoc", "Investment in associates", "i", [3891, 4398, 5031, 7531, 7018], ""),
    ("dernca", "Derivative financial instruments", "i", [1962, 2005, 468, 784, 657], ""),
    ("dta", "Deferred income taxes", "i", [7861, 3962, 7313, 6884, 6908], ""),
    ("intang", "Intangible assets, net", "i", [56965, 59062, 55101, 65808, 62947], ""),
    ("gw", "Goodwill", "i", [74565, 68085, 62000, 75100, 72568], ""),
    ("otha", "Other assets, net", "i", [4340, 4800, 4271, 3921, 4856], ""),
    ("ta", "TOTAL ASSETS", "f", "={c}{tca}+SUM({c}{ppe}:{c}{otha})", ""),
    ("b1", "", "b", None, ""),
    ("h2", "Current liabilities", "h", None, ""),
    ("std", "Current portion of long-term debt", "i", [10625, 6435, 12932, 4862, 12635], ""),
    ("ap", "Trade payables", "i", [35752, 44058, 40409, 40815, 39074], ""),
    ("othp", "Other payables and accrued liabilities", "i", [24102, 24198, 22072, 27280, 26395], ""),
    ("leasec", "Lease liabilities", "i", [5793, 5930, 5751, 7140, 7076], ""),
    ("relp", "Payables to related parties", "i", [1527, 1240, 1412, 1260, 1154], ""),
    ("taxp", "Income taxes payable", "i", [708, 4604, 665, 1535, 1059], ""),
    ("ptu", "Employee profit sharing (PTU)", "i", [1692, 1811, 1787, 1752, 1592], ""),
    ("dercl", "Derivative financial instruments", "i", [169, 1458, 2164, 511, 1588], ""),
    ("othst", "Other short-term liabilities", "i", [392, 0, 0, 0, 0], ""),
    ("tcl", "Total current liabilities", "f", "=SUM({c}{std}:{c}{othst})", ""),
    ("ltd", "Long-term debt", "i", [82230, 77619, 97003, 146043, 141028], ""),
    ("leasenc", "Lease liabilities", "i", [25356, 23255, 21064, 28661, 27714], ""),
    ("derncl", "Derivative financial instruments", "i", [67, 590, 1888, 689, 2314], ""),
    ("empb", "Employee benefits", "i", [30712, 9382, 7217, 6635, 6507], "FY2022 drop = MEPP settlement; " + N_EMPB),
    ("dtl", "Deferred income taxes", "i", [7087, 7575, 9224, 8891, 8415], ""),
    ("othlt", "Other long-term liabilities", "i", [9822, 12007, 12886, 13032, 12999], ""),
    ("tl", "TOTAL LIABILITIES", "f", "={c}{tcl}+SUM({c}{ltd}:{c}{othlt})", ""),
    ("b2", "", "b", None, ""),
    ("h3", "Stockholders' equity", "h", None, ""),
    ("cap", "Capital stock", "i", [4021, 3984, 3946, 3887, 3866], ""),
    ("re", "Retained earnings", "i", [73384, 111486, 118718, 122763, 127596], ""),
    ("perp", "Other equity financial instrument (perpetual notes)", "i", [8867, 8098, 0, 0, 0],
     "Reclassified to debt in 2023"),
    ("ctab", "Cumulative translation adjustment", "i", [10297, 1132, -13832, -868, -10377], ""),
    ("actb", "Actuarial gains on defined-benefit plans", "i", [696, 1152, 734, 1315, 1008], ""),
    ("eqvb", "Valuation of equity financial instruments", "i", [-742, -690, -857, -1011, -1132], ""),
    ("cfhb", "Unrealized (losses) gains on cash-flow hedges", "i", [577, -1051, -387, -142, -1449], ""),
    ("ctrl", "Controlling interest", "f", "=SUM({c}{cap}:{c}{cfhb})", ""),
    ("ncib", "Non-controlling interest", "i", [4506, 3491, 3306, 1754, 743], ""),
    ("te", "TOTAL EQUITY", "f", "={c}{ctrl}+{c}{ncib}", ""),
    ("tle", "TOTAL LIABILITIES AND EQUITY", "f", "={c}{tl}+{c}{te}", ""),
    ("b3", "", "b", None, ""),
    ("chk", "Check: total assets - (liabilities + equity)", "f", "={c}{ta}-{c}{tle}", "Must be 0"),
]

CF_ROWS = [
    ("h1", "Operating activities", "h", None, ""),
    ("pbtc", "Income before taxes, continuing operations", "i", [24854, 45878, 25324, 21034, 20143], "Must equal IS"),
    ("pbtd", "Income (loss) before taxes, discontinued operations", "i", [1499, 23516, -23, -277, 0], ""),
    ("pbt", "Income before taxes", "f", "={c}{pbtc}+{c}{pbtd}", ""),
    ("h1a", "Adjustments for:", "h", None, ""),
    ("da", "Depreciation and amortization", "i", [16375, 18282, 18929, 23051, 24838],
     "FY21-22 include discontinued D&A (249; 244)"),
    ("ppel", "Loss (gain) on sale of property, plant and equipment", "i", [-157, 650, 751, -192, 68], ""),
    ("cas", "Write-off of PP&E due to casualty", "i", [379, 0, 0, 0, 0], ""),
    ("assoc", "Share of results of associates", "i", [-247, -452, -316, -464, 2], ""),
    ("imp", "Impairment of long-lived assets", "i", [694, 1046, 383, 249, 445], ""),
    ("dgain", "Gain on disposal of discontinued operation", "i", [0, -22038, 0, 277, 0], ""),
    ("mepp", "Multi-employer pension plans and other long-term liabilities", "i", [-2247, -19010, 0, -982, 27], ""),
    ("svc", "Current service cost", "i", [1128, 1013, 837, 942, 909], N_BEN),
    ("intexp", "Interest expense", "i", [7884, 8049, 10006, 13100, 14464], ""),
    ("intinc", "Interest income", "i", [-373, -740, -809, -924, -897], N_INT),
    ("stl", "Short-term and low-value lease expenses", "i", [2183, 2519, 3968, 4526, 4964], ""),
    ("h1b", "Changes in assets and liabilities:", "h", None, ""),
    ("dar", "Trade and other receivables", "i", [666, -6647, -4206, -319, 601], ""),
    ("dinv", "Inventories", "i", [-2320, -4163, -1078, -1104, 901], ""),
    ("dprep", "Prepaid expenses", "i", [-365, 1261, -625, 189, -594], ""),
    ("dap", "Trade payables", "i", [8286, 9920, -851, -2825, -1108], ""),
    ("doth", "Other payables and accrued liabilities", "i", [-1025, -3395, 390, -3827, -560], ""),
    ("drel", "Payables to related parties", "i", [209, 287, -172, 153, 105], ""),
    ("taxpd", "Income taxes paid", "i", [-7578, -11824, -13831, -6472, -8955], ""),
    ("dcoll", "Collateral deposits on derivatives", "i", [6, -1271, -640, 942, 118], ""),
    ("dptu", "Employee profit sharing (PTU)", "i", [675, 122, -21, -36, -159], ""),
    ("demp", "Employee benefits and social security", "i", [-2567, -754, -2637, -2608, -2595], N_BEN),
    ("ddisc", "Dividends receivable from discontinued operation", "i", [0, -879, 0, 0, 0], ""),
    ("stlp", "Short-term and low-value lease payments", "i", [-2183, -2519, -3968, -4526, -4964], ""),
    ("cfo", "Net cash from operating activities", "f", "=SUM({c}{pbt}:{c}{stlp})", ""),
    ("b1", "", "b", None, ""),
    ("h2", "Investing activities", "h", None, ""),
    ("capex", "Purchases of property, plant and equipment", "i", [-20671, -28669, -34754, -29402, -22530], ""),
    ("acq", "Business acquisitions and NCI, net of cash acquired", "i", [-10637, -6520, -6548, -5988, -11294], ""),
    ("divst", "Proceeds from sale of discontinued operation", "i", [0, 25797, 0, 0, 0], "Ricolino"),
    ("ppes", "Proceeds from sale of PP&E", "i", [882, 20, 152, 984, 824], ""),
    ("ins", "Insurance recoveries", "i", [201, 272, 0, 0, 0], ""),
    ("intg", "Purchases of intangible assets, net of disposals", "i", [-622, -798, -918, -772, -311], N_INTG),
    ("drights", "Increase in distribution rights in structured entities", "i", [-77, 3, -129, -705, -52], ""),
    ("otha", "Other assets", "i", [-1433, -794, -577, 455, -860], ""),
    ("divr", "Dividends received from associates and others", "i", [59, 954, 86, 207, 158], ""),
    ("intr", "Interest received", "i", [373, 740, 809, 924, 897], N_INT),
    ("ncip", "Purchase of non-controlling interest", "i", [0, 0, 0, 0, -1468], "Bimbo Colombia 40%"),
    ("assc", "Capital contributions to associates, net", "i", [-534, -127, -561, -1841, -16], ""),
    ("cfi", "Net cash used in investing activities", "f", "=SUM({c}{capex}:{c}{assc})", ""),
    ("b2", "", "b", None, ""),
    ("h3", "Financing activities", "h", None, ""),
    ("borr", "Proceeds from borrowings, net of issuance costs", "i", [38924, 51670, 136638, 79111, 69267], ""),
    ("repay", "Repayment of borrowings", "i", [-33535, -55542, -109847, -56495, -55477], ""),
    ("intp", "Interest paid", "i", [-6781, -6407, -7436, -8376, -11533], "Debt interest; lease interest is inside lease payments"),
    ("perpy", "Yield on perpetual notes (equity instrument)", "i", [-621, -649, -395, 0, 0], ""),
    ("perpr", "Repurchase of perpetual notes", "i", [0, -344, -78, 0, 0], ""),
    ("divp", "Dividends paid", "i", [-4636, -5885, -3549, -4234, -4451], "Parent + NCI"),
    ("sedist", "Distributions to US structured entities (NCI)", "i", [0, 0, 0, 0, 0],
     "Not reported separately in history; forecast = equity 'consolidation of structured entities'"),
    ("leasep", "Lease payments", "i", [-5372, -6385, -6278, -7072, -8060], "Principal + interest"),
    ("derp", "Payments on derivative financial instruments", "i", [-1690, 0, -1655, -1889, -1034], ""),
    ("derc", "Collections on derivative financial instruments", "i", [1496, 418, 2090, 692, 633], ""),
    ("buyb", "Share repurchases", "i", [-1901, -2568, -3586, -4433, -1253], ""),
    ("cff", "Net cash from (used in) financing activities", "f", "=SUM({c}{borr}:{c}{buyb})", ""),
    ("b3", "", "b", None, ""),
    ("fxadj", "Effect of exchange rates and inflation on cash", "i", [279, -472, -835, 631, -715], ""),
    ("net", "Net increase (decrease) in cash", "f", "={c}{cfo}+{c}{cfi}+{c}{cff}+{c}{fxadj}", ""),
    ("beg", "Cash at beginning of year", "beg", [9268, 8748, 12313, 6353, 8057],
     "FY2021 typed (FY2020 close); later years = prior-year ending cash"),
    ("end", "Cash at end of year", "f", "={c}{beg}+{c}{net}", "Must equal BS cash"),
]

EQ_ROWS = [
    ("h1", "Controlling interest", "h", None, ""),
    ("o1", "Opening balance", "open", [83713, 97100, 124111, 108322, 125944],
     "FY2021 typed (FY2020 close); later years = prior-year closing"),
    ("py", "Yield on perpetual notes", "i", [-621, -649, -395, 0, 0], ""),
    ("ptx", "Tax effect on perpetual notes", "i", [58, -229, -20, 0, 0], ""),
    ("prep", "Repurchase of perpetual notes", "i", [0, -377, -78, 0, 0], ""),
    ("prcl", "Reclassification of perpetual notes to debt", "i", [0, 0, -8844, 0, 0], ""),
    ("div1", "Dividends declared", "i", [-4502, -5791, -3458, -4125, -4316], ""),
    ("bb", "Share repurchases", "i", [-1901, -2568, -3586, -4433, -1253], ""),
    ("own", "Changes in ownership interest", "i", [0, 0, 0, 0, -752], "Colombia NCI purchase"),
    ("ni1", "Net income (controlling)", "i", [15916, 46910, 15477, 12544, 11133], "Must equal IS controlling NI"),
    ("oci1", "Other comprehensive income (controlling)", "i", [4437, -10285, -14885, 13636, -11244], ""),
    ("c1", "Closing balance, controlling", "f", "=SUM({c}{o1}:{c}{oci1})", "Must equal BS controlling interest"),
    ("b1", "", "b", None, ""),
    ("h2", "Non-controlling interest", "h", None, ""),
    ("o2", "Opening balance", "open", [4298, 4506, 3491, 3306, 1754],
     "FY2021 typed (FY2020 close); later years = prior-year closing"),
    ("se", "Consolidation of structured entities", "i", [-1099, -2011, -1851, -3120, -2240], ""),
    ("div2", "Dividends declared", "i", [-163, -94, -91, -109, -135], ""),
    ("own2", "Acquisitions, disposals and ownership changes", "i", [0, -65, 217, 0, -648],
     "FY22 discontinued (-65); FY23 acquisitions (+217); FY25 acquisitions 68 less decrease 716"),
    ("ni2", "Net income (NCI)", "i", [1466, 1575, 1445, 1499, 1813], "Must equal IS NCI"),
    ("oci2", "Other comprehensive income (NCI)", "i", [4, -420, 95, 178, 199], ""),
    ("c2", "Closing balance, NCI", "f", "=SUM({c}{o2}:{c}{oci2})", "Must equal BS NCI"),
    ("b2", "", "b", None, ""),
    ("tot", "Total equity, closing", "f", "={c}{c1}+{c}{c2}", "Must equal BS total equity"),
]

# Segment note (audited). Regional net sales are before intersegment eliminations;
# regional operating income excludes intercompany royalties, which sit in the
# eliminations column (segment note footnote 1).
REGIONS = [("mx", "Mexico"), ("na", "North America"), ("la", "Latin America"), ("eaa", "Europe, Asia and Africa (EAA)")]
SEG_DATA = {
    "s": {"mx": [109089, 130401, 145387, 151164, 154809], "na": [175369, 205674, 192534, 189330, 190211],
          "la": [31109, 38411, 36647, 39879, 44120], "eaa": [34195, 37536, 40545, 45044, 54214],
          "el": [-10970, -13316, -15234, -17082, -16402]},
    "o": {"mx": [16731, 18824, 21882, 23726, 23442], "na": [15171, 33263, 11175, 5920, 6272],
          "la": [78, 1087, 1294, 1191, 607], "eaa": [292, -486, 326, 1227, 2498],
          "el": [308, 1008, 778, 1085, 1327]},
    "d": {"mx": [3907, 4424, 5524, 6895, 7859], "na": [8470, 9248, 8946, 10878, 10793],
          "la": [1687, 2278, 2215, 2507, 2945], "eaa": [2062, 2088, 2244, 2772, 3241],
          "el": [0, 0, 0, -1, 0]},
    "i": {"mx": [133, 72, 78, 141, 329], "na": [57, -890, -79, -4, 25],
          "la": [142, 46, 22, -101, 0], "eaa": [350, 1024, 362, 213, 91], "el": [0, 0, 0, 0, 0]},
    "n": {"mx": [0, 0, 0, 0, 0], "na": [-2246, -19010, 175, -982, 27],
          "la": [19, 22, 0, 6, 0], "eaa": [0, 0, 0, 0, 0], "el": [211, 448, 0, 0, 0]},
}
# Reported Adjusted EBITDA by region (tie-out only).
SEG_EBITDA_REPORTED = {"mx": [20771, 23320, 27484, 30762, 31630], "na": [21452, 22611, 20217, 15812, 17117],
                       "la": [1926, 3433, 3531, 3603, 3552], "eaa": [2704, 2626, 2932, 4212, 5830],
                       "el": [519, 1456, 778, 1084, 1327], "tot": [47372, 53446, 54942, 55473, 59456]}


def _seg_rows():
    keys = [k for k, _ in REGIONS] + ["el"]
    first, last = keys[0], keys[-1]
    rows = [("h1", "Net sales by region (before intersegment eliminations)", "h", None, "")]
    for k, lab in REGIONS:
        rows.append((f"s_{k}", lab, "tf", (SEG_DATA["s"][k], None), ""))
    rows.append(("s_el", "Intersegment eliminations", "tf", (SEG_DATA["s"]["el"], None), ""))
    rows.append(("s_tot", "Consolidated net sales", "hf", ("=SUM({c}{s_%s}:{c}{s_%s})" % (first, last), None),
                 "Equals IS net sales"))
    rows.append(("b1", "", "b", None, ""))
    rows.append(("h2", "Net sales growth (in MXN, includes FX translation)", "h", None, ""))
    for k, lab in REGIONS:
        g = "=IFERROR({c}{s_%s}/{p}{s_%s}-1,0)" % (k, k)
        rows.append((f"g_{k}", lab, "hf", (g, g), ""))
    g = "=IFERROR({c}{s_tot}/{p}{s_tot}-1,0)"
    rows.append(("g_tot", "Consolidated net sales", "hf", (g, g), ""))
    rows.append(("b2", "", "b", None, ""))
    blocks = [("o", "Operating income by region", "Eliminations (intercompany royalties)",
               "Equals IS operating income"),
              ("d", "Depreciation and amortization by region", "Eliminations", "Equals IS memo D&A"),
              ("i", "Impairment (reversal) of long-lived assets by region", "Eliminations", ""),
              ("n", "Other non-cash items by region (mainly MEPP)", "Eliminations", "")]
    for b, head, ellab, totnote in blocks:
        rows.append((f"h_{b}", head, "h", None, ""))
        for k, lab in REGIONS + [("el", ellab)]:
            rows.append((f"{b}_{k}", lab, "tf", (SEG_DATA[b][k], None), ""))
        rows.append((f"{b}_tot", "Total", "hf",
                     ("=SUM({c}{%s_%s}:{c}{%s_%s})" % (b, first, b, last), None), totnote))
        rows.append((f"b_{b}", "", "b", None, ""))
    rows.append(("h_e", "Adjusted EBITDA by region (operating income + D&A + impairment + non-cash)", "h", None, ""))
    for k, lab in REGIONS:
        rows.append((f"e_{k}", lab, "hf",
                     ("={c}{o_%s}+{c}{d_%s}+{c}{i_%s}+{c}{n_%s}" % (k, k, k, k), None), ""))
    rows.append(("e_el", "Eliminations (intercompany royalties)", "hf",
                 ("={c}{o_el}+{c}{d_el}+{c}{i_el}+{c}{n_el}", None), ""))
    rows.append(("e_tot", "Total Adjusted EBITDA", "hf", ("=SUM({c}{e_%s}:{c}{e_el})" % first, None),
                 "Equals IS Adjusted EBITDA (EBIT + D&A + non-cash)"))
    rows.append(("b3", "", "b", None, ""))
    rows.append(("h_m", "Adjusted EBITDA margin on regional net sales", "h", None, ""))
    for k, lab in REGIONS:
        rows.append((f"m_{k}", lab, "hf", ("=IFERROR({c}{e_%s}/{c}{s_%s},0)" % (k, k), None),
                     "Same basis as the quarterly releases"))
    rows.append(("m_tot", "Consolidated", "hf", ("=IFERROR({c}{e_tot}/{c}{s_tot},0)", None), ""))
    return rows


BS_ROWNUM = {key: 5 + i for i, (key, *_) in enumerate(BS_ROWS)}
SEG_ROWS = _seg_rows()
SEG_ROWNUM = {key: 5 + i for i, (key, *_) in enumerate(SEG_ROWS)}
CF_ROWNUM = {key: 5 + i for i, (key, *_) in enumerate(CF_ROWS)}

BLUE = Font(name="Arial", size=9, color="0000FF")
BLACK = Font(name="Arial", size=9, color="000000")
BOLD = Font(name="Arial", size=9, bold=True)
HDR = Font(name="Arial", size=9, bold=True, color="FFFFFF")
TITLE = Font(name="Arial", size=12, bold=True)
NOTE = Font(name="Arial", size=8, italic=True, color="595959")
FILL_HDR = PatternFill("solid", fgColor="1F3864")
FILL_HIST = PatternFill("solid", fgColor="D9E1F2")
FILL_FCST = PatternFill("solid", fgColor="FCE4D6")
FILL_IN = PatternFill("solid", fgColor="FFF2CC")
FILL_SEC = PatternFill("solid", fgColor="F2F2F2")
FILL_ALAN = PatternFill("solid", fgColor="C6EFCE")     # applies the advisor's feedback (Alan): every row of the section
FILL_ALAN_H = PatternFill("solid", fgColor="70AD47")   # header row of such a section
ALAN_FONT = Font(name="Arial", size=9, bold=True, color="FFFFFF")
MACRO_TAB = "BF8F00"
ALAN_H = {"h_f", "h_f3", "h_t", "h_i"}
TOP = Border(top=Side(style="thin"))
NUM = '#,##0;(#,##0);"-"'
NUM2 = '#,##0.00;(#,##0.00);"-"'
TOTAL_KEYS = {"gp", "ebit", "pbt", "ni", "nicont", "ta", "tl", "te", "tle", "tca", "tcl", "ctrl",
              "cfo", "cfi", "cff", "end", "oci", "ci", "c1", "c2", "tot", "opex", "cif", "sub1", "sub2", "net",
              "adjebitda", "s_tot", "o_tot", "d_tot", "i_tot", "n_tot", "e_tot", "m_tot", "g_tot"}
PCT_PREFIX = ("g_", "m_")


def build_sheet(wb, name, title, subtitle, rows, src, ext=None, fcst_label="Forecast (team assumptions, sheet Assumptions)"):
    ext = ext or {}
    ws = wb.create_sheet(sn(name))
    ws["A1"] = t(title)
    ws["A1"].font = TITLE
    ws["A2"] = t(subtitle)
    ws["A2"].font = NOTE
    hdr = 4
    ws.cell(hdr, 1, t("MXN millions")).font = HDR
    for j, y in enumerate(YEARS):
        c = ws.cell(hdr, 2 + j, yl(y))
        c.font = HDR
        c.alignment = Alignment(horizontal="center")
    ws[f"{TAG_COL}{hdr}"] = t("Tag")
    ws[f"{SRC_COL}{hdr}"] = t("Source / note")
    for col in ["A"] + COLS + [TAG_COL, SRC_COL]:
        ws[f"{col}{hdr}"].fill = FILL_HDR
        ws[f"{col}{hdr}"].font = HDR
    ws.cell(hdr - 1, 2, t("Actual (audited)")).fill = FILL_HIST
    ws.merge_cells(start_row=hdr - 1, start_column=2, end_row=hdr - 1, end_column=6)
    ws.cell(hdr - 1, 7, t(fcst_label)).fill = FILL_FCST
    ws.merge_cells(start_row=hdr - 1, start_column=7, end_row=hdr - 1, end_column=11)
    for c in (ws.cell(hdr - 1, 2), ws.cell(hdr - 1, 7)):
        c.font = BOLD
        c.alignment = Alignment(horizontal="center")

    rownum = {}
    r = hdr + 1
    for key, *_ in rows:
        rownum[key] = r
        r += 1

    for key, label, kind, payload, note in rows:
        r = rownum[key]
        a = ws.cell(r, 1, t(label))
        if kind == "h":
            a.font = BOLD
            for col in ["A"] + COLS:
                ws[f"{col}{r}"].fill = FILL_SEC
            continue
        if kind == "b":
            continue
        a.font = BOLD if key in TOTAL_KEYS else BLACK
        fmt = NUM2 if key == "eps" else ('#,##0.000' if key == "shares" else NUM)
        if name == "Segments" and key.startswith(PCT_PREFIX):
            fmt = '0.0%;(0.0%);"-"'
        for j, col in enumerate(COLS):
            cell = ws[f"{col}{r}"]
            prev = COLS[j - 1] if j else None
            if kind == "i":
                if j < 5:
                    cell.value = payload[j]
                    cell.font = BLUE
                else:
                    cell.fill = FILL_IN
            elif kind in ("beg", "open"):
                if j == 0:
                    cell.value = payload[0]
                    cell.font = BLUE
                else:
                    close_key = "end" if kind == "beg" else ("c1" if key == "o1" else "c2")
                    cell.value = f"={prev}{rownum[close_key]}"
                    cell.font = BLACK
            elif kind == "f":
                if prev is None and "{p}" in payload:
                    continue
                cell.value = payload.format(c=col, p=prev, **rownum, **ext)
                cell.font = BOLD if key in TOTAL_KEYS else BLACK
            elif kind in ("tf", "hf"):
                hist, fcst = payload
                tpl = fcst if j >= 5 else hist
                if j < 5 and kind == "tf":
                    cell.value = hist[j]
                    cell.font = BLUE
                elif tpl == "INPUT":
                    cell.fill = FILL_IN
                elif tpl is None or (prev is None and "{p}" in tpl):
                    pass
                else:
                    cell.value = tpl.format(c=col, p=prev, **rownum, **ext)
                    cell.font = BOLD if key in TOTAL_KEYS else BLACK
            cell.number_format = fmt
            if key in TOTAL_KEYS:
                cell.border = TOP
        if kind in ("i", "tf"):
            tag = "[sourced]"
        elif kind in ("beg", "open"):
            tag = "[sourced] FY21; [calc] after"
        else:
            tag = "[calc]"
        if key in ("da",) and name == "IS":
            srcnote = t(note)
        else:
            srcnote = (t(src) + ("; " + t(note) if note else "")) if kind in ("i", "tf", "beg", "open") else t(note)
        ws[f"{TAG_COL}{r}"] = t(tag)
        ws[f"{SRC_COL}{r}"] = srcnote
        ws[f"{TAG_COL}{r}"].font = NOTE
        ws[f"{SRC_COL}{r}"].font = NOTE

    ws.column_dimensions["A"].width = 52
    for col in COLS:
        ws.column_dimensions[col].width = 11
    ws.column_dimensions[TAG_COL].width = 12
    ws.column_dimensions[SRC_COL].width = 70
    return ws, rownum


def validate_segments():
    """Segment note ties to the income statement in every historical year (build-time check)."""
    is_vals = {key: payload for key, _, kind, payload, _ in IS_ROWS if kind == "i"}
    keys = [k for k, _ in REGIONS] + ["el"]
    for j in range(5):
        sales = sum(SEG_DATA["s"][k][j] for k in keys)
        assert sales == is_vals["sales"][j], ("sales", j)
        ebit = (is_vals["sales"][j] - is_vals["cogs"][j]
                - sum(is_vals[x][j] for x in ("dist", "admin", "integ", "oth")))
        assert sum(SEG_DATA["o"][k][j] for k in keys) == ebit, ("ebit", j)
        assert sum(SEG_DATA["d"][k][j] for k in keys) == is_vals["da"][j], ("da", j)
        nc = sum(SEG_DATA[b][k][j] for b in ("i", "n") for k in keys)
        for k in keys:
            e = sum(SEG_DATA[b][k][j] for b in ("o", "d", "i", "n"))
            assert e == SEG_EBITDA_REPORTED[k][j], ("ebitda", k, j)
        assert ebit + is_vals["da"][j] + nc == SEG_EBITDA_REPORTED["tot"][j], ("total ebitda", j)


# FY2026E drivers (team decisions 2026-10-22/23, docs/context/memory.md).
FX_CSV = ROOT / "data" / "market" / "usdmxn_daily_2025-01_2026-10.csv"
REL = {"q1": "1T26 rel. p.9", "q2": "2T26 rel. p.8", "q3": "3T26 rel. p.8"}
Q_SRC = "Earnings releases, filings/quarterly: 1T26 p.9, 2T26 p.8, 3T26 p.8 (income statement)"

# FY2027E net sales by region (team decisions 2026-10-25, docs/context/memory.md). Ratios and GDP growth come
# from data/macro/nominal_gdp_growth_2016-2030.xlsx (built by model/build/build_macro_gdp.py), 4 decimals.
MACRO = "analisis-dcf-2026-10-26/datos/nominal_gdp_growth_2016-2030_auditfix.xlsx"  # H-02: built by build_macro_gdp_auditfix.py
audit_fix_es.remap_macro("data/macro/nominal_gdp_growth_2016-2030.xlsx", MACRO)
REG27 = [("na", "North America"), ("mx", "Mexico"), ("la", "Latin America"), ("eaa", "EAA")]
R9 = {"na": [40533, 44368, 44241], "mx": [39726, 40279, 40905],
      "la": [11545, 11620, 12047], "eaa": [12631, 13188, 13371]}
RATIO27 = {"na": 0.1678, "mx": 0.7747, "la": 0.6688, "eaa": 0.6307}  # H-02: was 0.5611
GDP27 = {"na": 0.0544, "mx": 0.0669, "la": 0.0795, "eaa": 0.0622}
GDPSRC = {"na": "sheet Data (USA, team choice: US only)", "mx": "sheet Data (MEX)",
          "la": "sheet Regional_agg (prior-year FX weights)", "eaa": "sheet Regional_agg (prior-year FX weights)"}
# Local currency -> USD factor FY2027E per region, sheet Regional_FX of MACRO (4 decimals) [calc]
FXL27 = {"na": 1.0, "mx": 1.0, "la": 0.9749, "eaa": 0.9917}
FXLSRC = {"na": "USA only (team choice for GDP): earned in USD", "mx": "Peso business: no translation",
          "la": MACRO + ", sheet Regional_FX", "eaa": MACRO + ", sheet Regional_FX"}
# FY2028E-FY2030E (same method, ratios held; team 2026-10-25) and the terminal growth g. GDP growth and the
# local currency -> USD factors from MACRO (4 decimals) [calc]; USD/MXN annual averages from MACRO sheet FX
# (Capital IQ forecast, BIMBOA/research/Informacion_BIMBO_macro.txt L1128) [sourced].
YRS3 = (2028, 2029, 2030)
GDP3 = {"na": (0.0475, 0.0418, 0.0413), "mx": (0.0601, 0.0580, 0.0488),
        "la": (0.0633, 0.0664, 0.0706), "eaa": (0.0594, 0.0605, 0.0600)}
FXL3 = {"na": (1.0, 1.0, 1.0), "mx": (1.0, 1.0, 1.0),
        "la": (0.9710, 0.9813, 0.9826), "eaa": (0.9945, 1.0035, 1.0012)}
MXN_CIQ = {2027: 18.21, 2028: 18.67, 2029: 19.03, 2030: 19.24}
# Mexico CPI annual average 2028-2030, Capital IQ consumerPriceInflation (MACRO sheet IAS29_test) [sourced]
INFL3 = {2028: 0.0372, 2029: 0.0321, 2030: 0.0255}
# Next-year maturity (US$ millions), maturity ladder 2Q26 investor presentation p.17 [sourced]
MAT3 = {2029: (1081, "USD bonds 900 + bank loans 181"), 2030: (396, "MXN bonds 237 + bank loans 159"),
        2031: (0, "no maturity shown for 2031")}
N_EXT = "Team 2026-10-25: FY2027E rule extended to FY2028E-FY2030E"

# Live links to the macro sheets copied in from MACRO (no pasted values). The 4-decimal constants above are kept
# only as a build-time check that each link points at the intended cell (embed_macro asserts it).
MCELL = {("rt", "na"): "Organic_pass!D17", ("rt", "mx"): "Organic_pass!D18", ("rt", "la"): "Organic_pass!D19",
         ("rt", "eaa"): "Organic_pass!D20", ("ppp", "la"): "PPP_terminal!D48", ("ppp", "eaa"): "PPP_terminal!D49"}
for _y, _gv, _ra, _fx, _cpi in ((2027, "N", "P", "D", "O"), (2028, "O", "Q", "E", "P"),
                                (2029, "P", "R", "F", "Q"), (2030, "Q", "S", "G", "R")):
    MCELL.update({("gd", _y, "na"): "Growth_view!%s3" % _gv, ("gd", _y, "mx"): "Growth_view!%s2" % _gv,
                  ("gd", _y, "la"): "Regional_agg!%s91" % _ra, ("gd", _y, "eaa"): "Regional_agg!%s92" % _ra,
                  ("fxl", _y, "la"): "Regional_FX!%s48" % _fx, ("fxl", _y, "eaa"): "Regional_FX!%s49" % _fx,
                  ("cq", _y): "FX!%s20" % _gv, ("cpi", _y, "mx"): "IAS29_test!%s3" % _cpi,
                  ("cpi", _y, "us"): "IAS29_test!%s4" % _cpi})
MCHECK = {}


def ml(key, expect):
    """Formula linking a macro cell; records the value the cell must hold."""
    MCHECK[MCELL[key]] = expect
    return "=" + (MCELL[key] if LANG == "en" else macro_es.ref(MCELL[key]))


def fxl_row(key, label, k, y, expect, note):
    """FX factor row: 1 for the USD and peso businesses, a live link for Latin America and EAA."""
    if k in ("na", "mx"):
        return (key, label, "v", 1.0, "[calc]", note)
    return (key, label, "vf", ml(("fxl", y, k), expect), "[calc]", note)


def fx_quarter_averages():
    """4Q25 average, 4Q26 average (October closes plus the last quote held to year-end) and 9M26 average."""
    import csv
    import datetime
    rows = [(datetime.date.fromisoformat(r["date"]), float(r["usdmxn_close"]))
            for r in csv.DictReader(open(FX_CSV, encoding="utf-8"))]
    q4_25 = [v for d, v in rows if d.year == 2025 and d.month >= 10]
    q4_26 = [v for d, v in rows if d.year == 2026 and d.month >= 10]
    m9_26 = [v for d, v in rows if d.year == 2026 and d.month <= 9]
    last_d, spot = rows[-1]
    rem = sum(1 for i in range(1, 80)
              if (last_d + datetime.timedelta(i)).year == 2026 and (last_d + datetime.timedelta(i)).weekday() < 5)
    return (round(sum(q4_25) / len(q4_25), 4), round((sum(q4_26) + rem * spot) / (len(q4_26) + rem), 4),
            round(sum(m9_26) / len(m9_26), 4))


def sales_2028_2030_rows():
    """FY2028E-FY2030E net sales by region and the terminal growth g in MXN (team decisions 2026-10-25)."""
    ciq = MACRO + ", sheet FX (Capital IQ forecast)"
    rows = [("bl6b", "", "b", None, "", ""),
            ("h_f3", "FY2028E-FY2030E net sales by region: organic ratios held, same method as FY2027E (team decisions 2026-10-25)",
             "h", None, "", ""),
            ("cq2027", "USD/MXN average 2027, Capital IQ forecast", "vf", ml(("cq", 2027), MXN_CIQ[2027]), "[sourced]", ciq)]
    for i, y in enumerate(YRS3):
        py = y - 1
        fxp = "fx27" if y == 2028 else "fx%d" % (py % 100)
        sp = "s27" if y == 2028 else "s%d" % py
        rows += [("cq%d" % y, "USD/MXN average %d, Capital IQ forecast" % y, "vf", ml(("cq", y), MXN_CIQ[y]), "[sourced]", ciq),
                 ("fx%d" % (y % 100), "USD/MXN average FY%dE" % y, "vf", "=B{cq%d}" % y, "[assumption]",
                  "Team 2026-10-25: Capital IQ forecast for every year FY2027E-FY2030E (same source as GDP and regional FX)")]
        for k, lab in REG27:
            rows += [
                ("gd%d_%s" % (y, k), "Nominal GDP growth %d in local currency, %s" % (y, lab), "vf",
                 ml(("gd", y, k), GDP3[k][i]), "[calc]", "Capital IQ levels; %s, %s" % (MACRO, GDPSRC[k])),
                fxl_row("fxl%d_%s" % (y, k), "FX factor local currency to USD FY%dE, %s" % (y, lab), k, y, FXL3[k][i],
                        FXLSRC[k]),
                ("fxm%d_%s" % (y, k), "FX factor to MXN FY%dE, %s" % (y, lab), "vf",
                 "=1" if k == "mx" else "=B{fxl%d_%s}*B{fx%d}/B{%s}" % (y, k, y % 100, fxp), "[calc]",
                 "Peso business" if k == "mx" else "Local currency to USD x USD/MXN average, year on year"),
                ("s%d_%s" % (y, k), "Net sales FY%dE, %s" % (y, lab), "vf",
                 "=B{%s_%s}*(1+B{rt_%s}*B{gd%d_%s})*B{fxm%d_%s}" % (sp, k, k, y, k, y, k), "[calc]",
                 "Prior year x (1 + organic ratio x GDP growth in local currency) x FX factor to MXN")]
        rows += [
            ("s%d" % y, "Net sales FY%dE (sum of regions)" % y, "vf",
             "=" + "+".join("B{s%d_%s}" % (y, k) for k, _ in REG27), "[calc]",
             "Feeds the IS"),
            ("g%dm" % y, "Net sales growth FY%dE in MXN" % y, "vf", "=B{s%d}/B{%s}-1" % (y, sp), "[calc]",
             "Reported-currency growth"),
            ("g%db" % y, "  of which business growth (organic, excluding FX)", "vf",
             "=(" + "+".join("B{%s_%s}*B{rt_%s}*B{gd%d_%s}" % (sp, k, k, y, k) for k, _ in REG27) + ")/B{%s}" % sp,
             "[calc]", "Advisor: split business vs FX"),
            ("g%df" % y, "  of which FX effect", "vf", "=B{g%dm}-B{g%db}" % (y, y), "[calc]",
             "Growth in MXN less growth excluding FX, the way Bimbo reports it")]
    rows += [
        ("bl6c", "", "b", None, "", ""),
        ("h_t", "Terminal growth g (Gordon) in MXN: FY2030E ratios x long-run nominal GDP, purchasing power parity for every currency (team decisions 2026-10-25)",
         "h", None, "", ""),
        ("cpiT_mx", "CPI inflation 2030, Mexico", "vf", ml(("cpi", 2030, "mx"), 0.0255), "[sourced]",
         "Capital IQ consumerPriceInflation; %s, sheet IAS29_test" % MACRO),
        ("cpiT_us", "CPI inflation 2030, United States", "vf", ml(("cpi", 2030, "us"), 0.0206), "[sourced]",
         "Capital IQ consumerPriceInflation; %s, sheet IAS29_test" % MACRO),
        ("drT", "USD/MXN long-run change (purchasing power parity)", "vf", "=(1+B{cpiT_mx})/(1+B{cpiT_us})", "[calc]",
         "Team 2026-10-25: (1 + Mexico CPI) / (1 + US CPI), 2030; above 1 = the peso loses vs the USD"),
        ("fxlT_la", "Long-run FX factor local currency to USD (purchasing power parity), Latin America", "vf",
         ml(("ppp", "la"), 0.9851), "[calc]",
         "Team 2026-10-25: (1 + US CPI) / (1 + currency CPI) 2030 by country, aggregated as Regional_FX; %s, sheet PPP_terminal" % MACRO),
        ("fxlT_eaa", "Long-run FX factor local currency to USD (purchasing power parity), EAA", "vf",
         ml(("ppp", "eaa"), 0.9943), "[calc]",
         "Team 2026-10-25: (1 + US CPI) / (1 + currency CPI) 2030 by country, euro = GDP-weighted euro CPI, aggregated as Regional_FX; "
         "%s, sheet PPP_terminal" % MACRO),
    ]
    for k, lab in REG27:
        rows += [
            ("rtT_" + k, "Terminal ratio, %s" % lab, "vf", "=B{rt_%s}" % k, "[assumption]",
             "Team 2026-10-25 (option A): the FY2030E organic ratio held in perpetuity, so g continues FY2030E with no jump"),
            ("wT_" + k, "Weight in FY2030E net sales, %s" % lab, "vf", "=B{s2030_%s}/B{s2030}" % k, "[calc]",
             "Team 2026-10-25: FY2030E regional mix"),
            ("gT_" + k, "Long-run growth in MXN, %s" % lab, "vf",
             "=B{rtT_mx}*B{gd2030_mx}" if k == "mx" else "=(1+B{rtT_%s}*B{gd2030_%s})*B{%s}*B{drT}-1" % (
                 k, k, "fxl2030_na" if k == "na" else "fxlT_" + k),
             "[calc]", "Ratio x Mexico GDP growth 2030; peso business" if k == "mx" else
             "(1 + ratio x GDP growth 2030 in local currency) x FX factor 2030 to USD x USD/MXN change - 1"
             + ("" if k == "na" else "; local currency to USD by purchasing power parity"))]
    rows += [
        ("gT", "Terminal growth g in MXN", "vf", "=" + "+".join("B{wT_%s}*B{gT_%s}" % (k, k) for k, _ in REG27), "[calc]",
         "Regions weighted by FY2030E sales; replaces the v3 proposal 4.25% (0.36 x 3% + 0.64 x 5%, valuation.md)"),
        ("gTb", "  of which business growth (local currency, FY2030E ratios)", "vf",
         "=" + "+".join("B{wT_%s}*B{rtT_%s}*B{gd2030_%s}" % (k, k, k) for k, _ in REG27), "[calc]",
         "Advisor: split business vs FX"),
        ("gTf", "  of which FX effect", "vf", "=B{gT}-B{gTb}", "[calc]",
         "Translation of USD, EUR and other sales into MXN"),
        ("gT30", "Check: g less FY2030E net sales growth in MXN", "vf", "=B{gT}-B{g2030m}", "[calc]",
         "Near 0 = no jump between the last forecast year and the perpetuity"),
        ("gTmx", "Check: Mexico long-run nominal GDP growth (2030)", "vf", "=B{gd2030_mx}", "[calc]", "Capital IQ levels"),
        ("gTd", "Check: g less Mexico GDP growth", "vf", "=B{gT}-B{gTmx}", "[calc]", "Equals the two rows below"),
        ("gTmix", "  from the regional ratios and economies vs Mexico", "vf", "=B{gTb}-B{gTmx}", "[calc]",
         "Business growth less Mexico GDP growth"),
        ("gTfx", "  from FX translation into MXN", "vf", "=B{gTf}", "[calc]", ""),
        ("gTr", "Check: implied ratio g / Mexico GDP growth", "vf", "=B{gT}/B{gTmx}", "[calc]",
         "Explained by the two rows above"),
    ]
    return rows


def fcst_2028_2030_rows(is_r, opex):
    """FY2028E-FY2030E drivers: the FY2027E methods year by year (team decisions 2026-10-25)."""
    isn, bsn = sn("IS"), sn("BS")
    rows = []
    for i, y in enumerate(YRS3, 2):
        yy, pp = y % 100, (y - 1) % 100
        sy, sp = "s%d" % y, ("s27" if y == 2028 else "s%d" % (y - 1))
        pcol = FC[i - 1]
        rows += [("bl_y%d" % yy, "", "b", None, "", ""),
                 ("h_y%d" % yy, "FY%dE drivers: FY2027E methods (team decisions 2026-10-25)" % y, "h", None, "", "")]
        if y == 2028:
            rows += [
                ("cxr", "Capex / net sales FY2027E", "vf", "=B{cx27}/B{s27}", "[calc]",
                 "US$1.3bn = FY2026E + deferred projects = Bimbo's original 2026 plan (4Q25 deck p.17)"),
                ("etr3", "Effective tax rate FY2028E-FY2030E", "vf",
                 "=AVERAGE(%s!D%d/%s!D%d,%s!E%d/%s!E%d)" % (isn, is_r["tax"], isn, is_r["pbt"], isn, is_r["tax"], isn, is_r["pbt"]),
                 "[assumption]", "Team 2026-10-23: average of FY2023 and FY2024, the years without the unrecognized "
                 "tax-loss effect (EEFF25 p.57)")]
        # cost of sales
        rows += [
            ("w%d" % pp, "Wheat price %d (US$/t, annual average)" % (y - 1), "vf", "=B{w%d}" % ((y - 2) % 100), "[assumption]",
             "Team 2026-10-25: held at the 2026E level (no forecast of our own); CBOT futures as a sensitivity only"),
            ("rr%d" % yy, "Raw materials / net sales FY%dE" % y, "vf",
             "=B{rr%d}*(B{w%d}/B{w%d})^B{el}" % (pp, pp, (y - 2) % 100), "[calc]",
             "Prior-year ratio moved by the prior-year wheat change (one-year lag), as FY2027E"),
            ("rm%d" % yy, "Raw materials FY%dE" % y, "vf", "=B{%s}*B{rr%d}" % (sy, yy), "[calc]", "")]
        for k, lab in (("wg", "Wages and benefits"), ("fr", "Freight, fuel and maintenance"), ("ot", "Other cost of sales")):
            rows.append(("%s%d" % (k, yy), "%s FY%dE" % (lab, y), "vf", "=B{%s%d}/B{%s}*B{%s}" % (k, pp, sp, sy),
                         "[assumption]", N_EXT + "; prior-year ratio to net sales"))
        rows += [
            ("dp%d" % yy, "Depreciation FY%dE" % y, "vf", "=B{dp%d}*B{ppd%d}/B{ppd%d}" % (pp, yy, pp), "[calc]",
             "Prior-year line moved with PP&E depreciation"),
            ("c%d" % yy, "Cost of sales FY%dE" % y, "vf", "=B{rm%d}+B{wg%d}+B{fr%d}+B{dp%d}+B{ot%d}" % ((yy,) * 5), "[calc]",
             "Feeds the IS"),
            ("gm%d" % yy, "Gross margin FY%dE" % y, "vf", "=1-B{c%d}/B{%s}" % (yy, sy), "[calc]", "Result, not a target"),
            # capex and PP&E depreciation
            ("cx%d" % yy, "Capex FY%dE" % y, "vf", "=B{cxr}*B{%s}" % sy, "[assumption]",
             "Team 2026-10-25: capex / net sales held at FY2027E; purchases of PP&E in the cash flow"),
            ("ppd%d" % yy, "PP&E depreciation FY%dE" % y, "vf", "=B{dr}*%s!%s%d" % (bsn, pcol, BS_ROWNUM["ppe"]), "[calc]",
             "Rate x net PP&E at the prior year-end")]
        # general and other expenses by nature
        for k, label, _, m in opex:
            if m == "n":
                rows.append(("q%d_%s" % (yy, k), "%s FY%dE" % (label, y), "v", 0, "[assumption]",
                             "Non-recurring: not projected (team 2026-10-25, advisor feedback: organic, no non-recurring items)"))
            else:
                rows.append(("q%d_%s" % (yy, k), "%s FY%dE" % (label, y), "vf", "=B{q%d_%s}/B{%s}*B{%s}" % (pp, k, sp, sy),
                             "[assumption]", N_EXT + "; prior-year ratio to net sales"))
        rows += [
            ("q%d_da" % yy, "Depreciation and amortization in expenses FY%dE" % y, "vf",
             "=B{rou%d}+B{amort}+(B{oda26}-B{rou_d}-B{amort})/B{ppe_d}*B{ppd%d}" % (yy, yy), "[calc]",
             "Audit fixes H-03, H-05: right-of-use depreciation grows with net sales; amortization held at FY2025; PP&E part = its FY2026E share x PP&E depreciation"),
            ("x%d" % yy, "General and other expenses FY%dE" % y, "vf",
             "=B{q%d_da}+" % yy + "+".join("B{q%d_%s}" % (yy, k) for k, *_ in opex), "[calc]", "Feeds the IS"),
            ("x%d_o" % yy, "  Other (income) expenses, net", "vf", "=B{x%d_o}/B{%s}*B{%s}" % (pp, sp, sy), "[calc]",
             "Prior-year ratio to net sales, recurring part only"),
            ("x%d_i" % yy, "  Integration", "vf", "=B{q%d_ig}" % yy, "[calc]", ""),
            ("x%d_d" % yy, "  Distribution and selling", "vf",
             "=(B{x%d}-B{x%d_o}-B{x%d_i})*%s!F%d/(%s!F%d+%s!F%d)" % (yy, yy, yy, isn, is_r["dist"], isn, is_r["dist"], isn, is_r["admin"]),
             "[calc]", "FY2025 split of distribution and administration"),
            ("x%d_a" % yy, "  Administrative", "vf", "=B{x%d}-B{x%d_o}-B{x%d_i}-B{x%d_d}" % ((yy,) * 4), "[calc]", ""),
            ("da%d" % yy, "D&A FY%dE (IS memo)" % y, "vf", "=B{dp%d}+B{q%d_da}" % (yy, yy), "[calc]",
             "Cost-of-sales depreciation + expenses D&A"),
            ("x%d_r" % yy, "General and other expenses / net sales FY%dE" % y, "vf", "=B{x%d}/B{%s}" % (yy, sy), "[calc]", ""),
            ("ebit%d" % yy, "Operating income FY%dE" % y, "vf", "=B{%s}-B{c%d}-B{x%d}" % (sy, yy, yy), "[calc]", ""),
            ("em%d" % yy, "Adjusted EBITDA margin FY%dE" % y, "vf", "=(B{ebit%d}+B{da%d})/B{%s}" % (yy, yy, sy), "[calc]",
             "Result, not a target")]
        # below operating income
        nx = y + 1
        mv, msrc = MAT3[nx]
        rows += [
            ("refi%d" % yy, "New borrowing FY%dE (refinancing of the %d maturity)" % (y, y), "vf", "=B{mat%d}" % yy, "[assumption]",
             N_EXT + ": refinanced in full; net debt is the same either way"),
            ("mat%d_usd" % (nx % 100), "Debt maturing in %d (US$ millions)" % nx, "v", mv, "[sourced]",
             "Maturity ladder, 2Q26 investor presentation p.17 (%s)" % msrc),
            ("mat%d" % (nx % 100), "%d maturity, current portion at 31-Dec-%dE" % (nx, y), "vf",
             "=B{mat%d_usd}*B{mat_fx}" % (nx % 100), "[calc]",
             "Reclassified from long-term to current debt: due within 12 months of the balance date"),
            ("debt%d" % yy, "Gross debt at 31-Dec-%dE" % y, "vf", "=B{debt%d}-B{mat%d}+B{refi%d}" % (pp, yy, yy), "[calc]",
             "Carried in MXN at 17.84 (team): translation of the hedged balance goes to OCI"),
            ("fxf%d" % yy, "FX factor on interest FY%dE" % y, "vf", "=(1-B{fxsh})+B{fxsh}*B{fx%d}/B{mat_fx}" % yy, "[calc]",
             "USD/MXN average of the year vs the 17.84 balance rate"),
            ("rou%d" % yy, "Right-of-use depreciation FY%dE" % y, "vf", "=B{rou_d}*B{%s}/B{s26}" % sy, "[calc]",
             "Audit fix H-05: FY2025 level x net sales of the year / FY2026E"),
            ("li%d" % yy, "Lease interest FY%dE" % y, "vf", "=B{l_int}*B{%s}/B{s26}" % sy, "[calc]",
             "Audit fix H-05: FY2025 level x net sales of the year / FY2026E"),
            ("int%d" % yy, "Interest expense FY%dE" % y, "vf",
             "=(B{debt%d}+B{debt%d})/2*B{kd}*B{fxf%d}+B{li%d}" % (pp, yy, yy, yy), "[calc]",
             "Audit fixes H-04, H-05: average gross debt x cost of debt (FY2026E run-rate) x FX factor + lease interest growing with net sales"),
            ("mon%d" % yy, "Monetary position loss (gain) FY%dE" % y, "vf", "=B{c_mon}", "[assumption]", "Held at FY2026E"),
            ("as%d" % yy, "Share of results of associates FY%dE" % y, "vf", "=B{c_as}", "[assumption]", "Held at FY2026E"),
            ("nci%d" % yy, "Non-controlling interest FY%dE" % y, "vf", "=B{c_nci}/B{s26}*B{%s}" % sy, "[calc]",
             "FY2026E ratio to net sales: the US distributors earn on sales, not on Bimbo's interest or taxes"),
            # balance sheet and cash flow
            ("infl%d" % yy, "Mexico consumer inflation %d (annual average)" % y, "vf", ml(("cpi", y, "mx"), INFL3[y]), "[sourced]",
             "Capital IQ consumerPriceInflation; %s, sheet IAS29_test" % MACRO),
            ("dps%d" % yy, "Dividend per share %d (MXN)" % y, "vf", "=B{dps%d}*(1+B{infl%d})" % (pp, yy), "[assumption]",
             N_EXT + ": dividend grows at inflation"),
            ("div%d" % yy, "Dividends declared FY%dE, controlling" % y, "vf", "=B{dps%d}*B{c_sh}" % yy, "[calc]",
             "Same share count as FY2026E"),
            ("divn%d" % yy, "Dividends to non-controlling interest FY%dE" % y, "vf", "=B{divn}", "[assumption]",
             "Held at FY2026E (FY2025)"),
            ("bb%d" % yy, "Share repurchases FY%dE" % y, "vf", "=B{bb27}", "[assumption]",
             N_EXT + ": average FY2021-FY2025 (cash flow statement)")]
    # Reinvestment test of the terminal g: return on the capital the forecast adds (RONIC)
    icl = ("ppe", "rou", "intang", "gw", "ar", "inv")
    rows += [
        ("bl_r", "", "b", None, "", ""),
        ("h_r", "Reinvestment test of g: return on new invested capital (RONIC), FY2028E-FY2030E", "h", None, "", ""),
        ("rT_tax", "Operating tax rate on EBIT", "vf", "=B{etr3}", "[assumption]",
         "FY2028E-FY2030E rate in every year, so the 2028 tax step-down does not enter the return"),
        ("waccR", "WACC (v3 route B proposal, reference)", "v", 0.1032327567, "[calc]",
         "valuation/valuation-outputs.yaml (BIMBOA_WACC_v3.xlsx); team confirms")]
    for i, y in enumerate((2027, 2028, 2029, 2030), 1):
        col, yy = FC[i], y % 100
        rows += [
            ("nop%d" % yy, "NOPAT FY%dE = EBIT x (1 - tax)" % y, "vf", "=%s!%s%d*(1-B{rT_tax})" % (isn, col, is_r["ebit"]),
             "[calc]", ""),
            ("ic%d" % yy, "Operating invested capital at 31-Dec-%dE" % y, "vf",
             "=" + "+".join("%s!%s%d" % (bsn, col, BS_ROWNUM[k]) for k in icl) + "-%s!%s%d" % (bsn, col, BS_ROWNUM["ap"]),
             "[calc]", "Net PP&E + right-of-use + intangibles + goodwill + receivables + inventories - trade payables")]
        if y > 2027:
            rows.append(("roic%d" % yy, "ROIC FY%dE (NOPAT / opening invested capital)" % y, "vf",
                         "=B{nop%d}/B{ic%d}" % (yy, yy - 1), "[calc]", "Compare with the WACC"))
    rows += [
        ("ronic", "RONIC FY2028E-FY2030E", "vf", "=(B{nop30}-B{nop27})/(B{ic30}-B{ic27})", "[calc]",
         "(NOPAT FY2030E - FY2027E) / (invested capital Dec-30 - Dec-27). Overstated: NOPAT is translated at a weaker peso "
         "while the invested capital is carried at historical pesos"),
        ("rvr30", "Net reinvestment rate FY2030E", "vf", "=(B{ic30}-B{ic29})/B{nop30}", "[calc]",
         "(Invested capital Dec-30 - Dec-29) / NOPAT FY2030E"),
        ("ronicT", "RONIC implied by a Gordon value that keeps the FY2030E reinvestment rate", "vf", "=B{gT}/B{rvr30}", "[calc]",
         "g / reinvestment rate"),
        ("rvT", "Reinvestment rate that g needs at the forecast RONIC", "vf", "=B{gT}/B{ronic}", "[calc]", "g / RONIC"),
        ("roicW", "Check: ROIC FY2030E less WACC", "vf", "=B{roic30}-B{waccR}", "[calc]",
         "Below 0 = the average return on Bimbo's capital is below its cost"),
        ("ronicW", "Check: RONIC less WACC", "vf", "=B{ronic}-B{waccR}", "[calc]",
         "Above 0 = growth adds value; at 0 the Gordon value equals NOPAT / WACC"),
    ]
    return rows


def build_assumptions(wb, is_r):
    """Assumptions sheet: 2026 actual by quarter, FY2026E drivers, option A (feeds the IS) and option B check."""
    fx25, fx26, fx9m = fx_quarter_averages()
    ws = wb.create_sheet(sn("Assumptions"))
    bsn = sn("BS")
    ws["A1"] = t("Grupo Bimbo - Assumptions FY2026E-FY2030E and terminal growth")
    ws["A1"].font = TITLE
    ws["A2"] = t("First block: 2026 actual by quarter (columns B-E). Every section below it: one value per row in column B, with its tag and source.")
    ws["A2"].font = NOTE
    hdr = 4
    for j, txt in enumerate(["MXN millions", "1Q26", "2Q26", "3Q26", "9M26", "Tag", "Source / note"]):
        c = ws.cell(hdr, 1 + j, t(txt))
        c.font = HDR
        c.fill = FILL_HDR
    isn = sn("IS")
    rows = [
        ("h_q", "2026 actual by quarter (earnings releases)", "h", None, "", ""),
        ("q_s", "Net sales", "q", [100319, 105026, 106061], "[sourced]", Q_SRC),
        ("q_c", "Cost of sales", "q", [47662, 49771, 49762], "[sourced]", Q_SRC),
        ("q_gp", "Gross profit", "qf", "={c}{q_s}-{c}{q_c}", "[calc]", ""),
        ("q_g", "General expenses", "q", [44282, 45378, 45052], "[sourced]",
         Q_SRC + "; distribution and selling + administration + integration"),
        ("q_o", "Other (income) expenses, net", "q", [463, 1049, 857], "[sourced]", Q_SRC),
        ("q_ebit", "Operating income", "qf", "={c}{q_gp}-{c}{q_g}-{c}{q_o}", "[calc]",
         "Sum of lines; the releases print 7,911 / 8,827 / 10,390 (rounding)"),
        ("q_e", "Adjusted EBITDA", "q", [14036, 15113, 16644], "[sourced]", Q_SRC),
        ("q_dn", "D&A, impairment and non-cash items (EBITDA - EBIT)", "qf", "={c}{q_e}-{c}{q_ebit}", "[calc]", ""),
        ("q_s25", "Net sales, same quarter 2025", "q", [103448, 107389, 107427], "[sourced]",
         "Comparatives: 1T26 p.3, 2T26 p.3, 3T26 p.3 (3Q25 restated from 107,421)"),
        ("q_e25", "Adjusted EBITDA, same quarter 2025", "q", [12797, 14890, 15776], "[sourced]",
         "Comparatives in the 2026 releases (income statement page)"),
        ("q_gm", "Gross margin", "qf", "={c}{q_gp}/{c}{q_s}", "[calc]", ""),
        ("q_gr", "General expenses / net sales", "qf", "={c}{q_g}/{c}{q_s}", "[calc]", ""),
        ("q_or", "Other expenses / net sales", "qf", "={c}{q_o}/{c}{q_s}", "[calc]", ""),
        ("q_dr", "D&A and non-cash / net sales", "qf", "={c}{q_dn}/{c}{q_s}", "[calc]", ""),
        ("q_em", "Adjusted EBITDA margin", "qf", "={c}{q_e}/{c}{q_s}", "[calc]", ""),
        ("q_gx", "Net sales growth in MXN", "qf", "={c}{q_s}/{c}{q_s25}-1", "[calc]", ""),
        ("q_int", "Net interest expense", "q", [3273, 3292, 2829], "[sourced]", Q_SRC),
        ("q_fx", "Foreign exchange loss (gain), net", "q", [189, 227, 194], "[sourced]", Q_SRC),
        ("q_mon", "Monetary position loss (gain)", "q", [0, -56, 119], "[sourced]", Q_SRC),
        ("q_as", "Share of results of associates", "q", [-7, 42, 1], "[sourced]", Q_SRC),
        ("q_pbt", "Income before taxes (as reported)", "q", [4443, 5406, 7249], "[sourced]", Q_SRC),
        ("q_pbtc", "Income before taxes, sum of lines", "qf",
         "={c}{q_ebit}-{c}{q_int}-{c}{q_fx}-{c}{q_mon}+{c}{q_as}", "[calc]", "Differs from the release by rounding"),
        ("q_tax", "Income taxes", "q", [1644, 2000, 2682], "[sourced]", Q_SRC),
        ("q_etr", "Effective tax rate", "qf", "={c}{q_tax}/{c}{q_pbt}", "[calc]", ""),
        ("q_nci", "Non-controlling interest", "q", [437, 471, 458], "[sourced]", Q_SRC),
    ] + [("r9_" + k, "Net sales by quarter, %s" % lab, "q", R9[k], "[sourced]",
          "1T26 p.3, 2T26 p.3, 3T26 p.3 (before intersegment eliminations)") for k, lab in REG27] + [
        ("bl1", "", "b", None, "", ""),
        ("h_d", "FY2026E drivers (value in column B)", "h", None, "", ""),
        ("s25", "Net sales FY2025", "vf", "=%s!F%d" % (isn, is_r["sales"]), "[sourced]", "Income statement"),
        ("s4q25", "Net sales 4Q25", "v", 108688, "[sourced]", "4T25 rel. p.4"),
        ("e4q25", "Adjusted EBITDA 4Q25", "vf", "=%s!F%d-E{q_e25}" % (isn, is_r["adjebitda"]), "[calc]",
         "FY2025 less 9M25"),
        ("g4q", "4Q26 net sales growth excluding FX", "v", 0.05, "[assumption]",
         "Team: guide 'mid-single digit' taken literally for the last quarter (3Q26 deck p.26)"),
        ("mx25", "Mexico net sales FY2025 (after intersegment eliminations)", "v", 140360, "[sourced]",
         "Segment note, IA25 p.85"),
        ("mxsh", "Mexico share of net sales", "vf", "=B{mx25}/B{s25}", "[calc]",
         "Earned in MXN; the rest is translated (about 2/3 abroad, call 2026-02-25 p.7)"),
        ("fx25", "USD/MXN average 4Q25", "v", fx25, "[calc]",
         "Average of daily closes Oct-Dec 2025, data/market/usdmxn_daily_2025-01_2026-10.csv"),
        ("fx26", "USD/MXN average 4Q26", "v", fx26, "[assumption]",
         "October 2026 closes to 23-Oct plus the 23-Oct quote held for the remaining business days (market FX, team decision)"),
        ("fac", "FX translation factor 4Q26 vs 4Q25", "vf", "=B{mxsh}+(1-B{mxsh})*B{fx26}/B{fx25}", "[calc]",
         "USD/MXN as proxy for every foreign currency, as in Bimbo's own guidance"),
        ("s4q26", "Net sales 4Q26", "vf", "=B{s4q25}*(1+B{g4q})*B{fac}", "[calc]", ""),
        ("s26", "Net sales FY2026E", "vf", "=E{q_s}+B{s4q26}", "[calc]", "9M26 actual + 4Q26"),
        ("gs26", "Net sales growth FY2026E in MXN", "vf", "=B{s26}/B{s25}-1", "[calc]",
         "Guide: flat to low-single-digit decline in MXN"),
        ("m25", "Adjusted EBITDA margin FY2025", "vf", "=%s!F%d/%s!F%d" % (isn, is_r["adjebitda"], isn, is_r["sales"]),
         "[calc]", ""),
        ("bp", "Margin expansion, midpoint of the guide", "v", 0.01025, "[guidance]",
         "+85 to +120 bp; filings/quarterly/GB_Investor_PPT_3Q26.pdf p.26"),
        ("one", "Less one-off gain on the La Moderna stake", "v", -0.00115, "[guidance]",
         "10-13 bp of FY2026 margin, midpoint; call 2026-04-29 p.7 (excluded by team decision)"),
        ("m26", "Adjusted EBITDA margin FY2026E", "vf", "=B{m25}+B{bp}+B{one}", "[calc]", ""),
        ("e26", "Adjusted EBITDA FY2026E", "vf", "=B{s26}*B{m26}", "[calc]", ""),
        ("e4q26m", "Implied 4Q26 Adjusted EBITDA margin", "vf", "=(B{e26}-E{q_e})/B{s4q26}", "[calc]",
         "Compare with 4Q25"),
        ("e4q25m", "4Q25 Adjusted EBITDA margin", "vf", "=B{e4q25}/B{s4q25}", "[calc]", ""),
        ("bl2", "", "b", None, "", ""),
        ("h_a", "Option A: FY2026E income statement (9M26 gross margin; general expenses close to the guide)", "h",
         None, "", ""),
        ("a_c", "Cost of sales", "vf", "=B{s26}*(1-E{q_gm})", "[calc]", "9M26 gross margin"),
        ("a_da", "D&A and non-cash items", "vf", "=B{s26}*E{q_dr}", "[calc]",
         "9M26 ratio of (EBITDA - EBIT); goes to the IS D&A memo line"),
        ("a_o", "Other (income) expenses, net", "vf", "=B{s26}*E{q_or}", "[calc]", "9M26 ratio"),
        ("a_ebit", "Operating income", "vf", "=B{e26}-B{a_da}", "[calc]", ""),
        ("a_g", "General expenses (closing line)", "vf", "=B{s26}-B{a_c}-B{a_o}-B{a_ebit}", "[calc]", ""),
        ("a_gr", "General expenses / net sales", "vf", "=B{a_g}/B{s26}", "[calc]", "Compare with 9M26"),
        ("a_dist", "  Distribution and selling", "vf",
         "=(B{a_g}-B{a_int})*%s!F%d/(%s!F%d+%s!F%d)" % (isn, is_r["dist"], isn, is_r["dist"], isn, is_r["admin"]),
         "[calc]", "FY2025 split of distribution and administration"),
        ("a_adm", "  Administrative", "vf", "=B{a_g}-B{a_int}-B{a_dist}", "[calc]", ""),
        ("a_int", "  Integration", "vf", "=B{p_ig}", "[calc]",
         "Audit fix H-01: integration by nature FY2026E (1H26 x 2), so the IS and the expenses by nature agree"),
        ("bl4", "", "b", None, "", ""),
        ("h_c", "FY2026E below operating income (team decisions 2026-10-23)", "h", None, "", ""),
        ("c_int", "Net interest expense", "vf", "=E{q_int}+D{q_int}", "[assumption]",
         "9M26 actual + 4Q26 = 3Q26; the CFO said the 3Q26 level may not hold (3Q26 call). "
         "Releases give net interest only: IS interest income FY2026E = 0"),
        ("c_fx", "Foreign exchange loss (gain), net", "vf", "=E{q_fx}*4/3", "[assumption]",
         "9M26 actual + 4Q26 at the 9M26 quarterly average"),
        ("c_mon", "Monetary position loss (gain)", "vf", "=E{q_mon}*4/3", "[assumption]",
         "9M26 actual + 4Q26 at the 9M26 quarterly average"),
        ("c_as", "Share of results of associates", "vf", "=E{q_as}*4/3", "[assumption]",
         "9M26 actual + 4Q26 at the 9M26 quarterly average"),
        ("c_etr", "Effective tax rate", "v", 0.37, "[assumption]",
         "9M26 = 37.0%, Bimbo's estimate of its annual rate (IAS 34); the lower 4Q rate of 2024-25 is not projected"),
        ("c_nci", "Non-controlling interest", "vf", "=E{q_nci}*4/3", "[assumption]",
         "9M26 actual + 4Q26 at the 9M26 quarterly average"),
        ("c_sh", "Weighted-average shares (millions)", "v", 4304.744119, "[assumption]",
         "Shares outstanding at 31-Dec-2025, 4,304,744,119 (EEFF25 p.80): the 2026 starting count; "
         "2026 buybacks (20m shares in 3Q26, 3Q26 call) not deducted"),
        ("bl5", "", "b", None, "", ""),
        ("h_e", "FY2026E balance sheet and cash flow (team decisions 2026-10-23)", "h", None, "", ""),
        ("fx9m", "USD/MXN average 9M26", "v", fx9m, "[calc]",
         "Average of daily closes Jan-Sep 2026, data/market/usdmxn_daily_2025-01_2026-10.csv"),
        ("fxy", "USD/MXN average FY2026E", "vf", "=(3*B{fx9m}+B{fx26})/4", "[calc]", "Three quarters at 9M26, one at 4Q26"),
        ("cx_usd", "Capex FY2026E (US$ millions)", "v", 1050, "[guidance]",
         "Midpoint of the CFO's US$1.0-1.1bn (3Q26 call); deck US$1.0-1.2bn (GB_Investor_PPT_3Q26 p.26)"),
        ("cx", "Capex FY2026E", "vf", "=B{cx_usd}*B{fxy}", "[calc]", "Purchases of PP&E in the cash flow"),
        ("rou_d", "Right-of-use depreciation", "v", 6142, "[assumption]",
         "FY2025 (EEFF25 p.41); held in FY2026E; audit fix H-05: from FY2027E right-of-use assets, lease liabilities, their depreciation and interest grow with net sales"),
        ("l_int", "Lease interest", "v", 2137, "[assumption]", "FY2025 (EEFF25 p.43); paid inside lease payments"),
        ("amort", "Intangible amortization", "v", 2175, "[assumption]", "FY2025 (EEFF25 p.45); intangible purchases = 0 (immaterial, see below)"),
        ("ig25", "Intangible purchases / PP&E purchases FY2025", "vf",
         "=%s!F%d/%s!F%d" % (sn("CF"), CF_ROWNUM["intg"], sn("CF"), CF_ROWNUM["capex"]), "[calc]",
         "Cash flow FY2025 (EEFF25)"),
        ("ig1h", "Purchases of intangible assets 1H26", "v", 50.161, "[sourced]", "BMV Jun-26 p.17"),
        ("cx1h", "Purchases of PP&E 1H26", "v", 6892.373, "[sourced]", "BMV Jun-26 p.17"),
        ("ig1hr", "Intangible purchases / PP&E purchases 1H26", "vf", "=B{ig1h}/B{cx1h}", "[calc]",
         "Team 2026-10-25: intangible purchases = 0 in FY2026E-FY2030E because they are immaterial (this row and FY2025)"),
        ("ppe_d", "PP&E depreciation and other non-cash items", "vf", "=B{a_da}-B{rou_d}-B{amort}", "[calc]",
         "IS D&A less right-of-use depreciation and amortization"),
        ("d_ar", "Receivable days (average FY2021-FY2025, on net sales)", "vf",
         "=AVERAGE(" + ",".join("%s!%s%d/%s!%s%d*365" % (bsn, c, BS_ROWNUM["ar"], isn, c, is_r["sales"]) for c in "BCDEF") + ")",
         "[calc]", "Team 2026-10-25: stable 29-33 days in FY2021-FY2025, average used"),
        ("d_inv", "Inventory days (FY2025, on cost of sales)", "vf",
         "=%s!F%d/%s!F%d*365" % (bsn, BS_ROWNUM["inv"], isn, is_r["cogs"]), "[calc]", "Held at FY2025"),
        ("d_ap", "Payable days (FY2025, on cost of sales)", "vf",
         "=%s!F%d/%s!F%d*365" % (bsn, BS_ROWNUM["ap"], isn, is_r["cogs"]), "[calc]", "Held at FY2025"),
        ("std_sep", "Current portion of debt at 30-Sep-2026", "v", 13636, "[sourced]", "3T26 rel. p.8"),
        ("ltd_sep", "Long-term debt at 30-Sep-2026", "v", 139166, "[sourced]", "3T26 rel. p.8"),
        ("mat_usd", "Bank loans maturing in the rest of 2026 (US$ millions)", "v", 87, "[sourced]",
         "Amortization profile, 3T26 rel. p.6"),
        ("mat_fx", "USD/MXN of the amortization profile", "v", 17.84, "[sourced]", "3T26 rel. p.6, note 11"),
        ("mat", "2026 maturity repaid in 4Q26", "vf", "=B{mat_usd}*B{mat_fx}", "[assumption]",
         "Only the contractual maturity; no prepayment, no new borrowing; cash is the result"),
        ("dps", "Dividend per share 2026 (MXN)", "v", 1.075, "[sourced]",
         "BMV notice 30-Apr-2026 (bmv.com.mx/docs-pub/derechos/derechos_1554405_1.pdf), paid 13-May-2026"),
        ("div", "Dividends declared, controlling", "vf", "=B{dps}*B{c_sh}", "[calc]", "On shares outstanding at 31-Dec-2025"),
        ("divn", "Dividends to non-controlling interest", "v", 135, "[assumption]", "FY2025 (equity statement)"),
        ("ret9", "Returned to shareholders 9M26 (dividends + buybacks)", "v", 6000, "[guidance]",
         "CFO: 'returning 6 billion pesos' (3Q26 call, approximate)"),
        ("bb3q", "Share repurchases 3Q26", "v", 1200, "[guidance]",
         "CFO: 20 million shares, about 1.2 billion pesos in the quarter (3Q26 call)"),
        ("bb", "Share repurchases FY2026E", "vf", "=B{ret9}-B{div}+B{bb3q}", "[assumption]",
         "Team 2026-10-25: 9M26 implied + 4Q26 at the 3Q26 pace (CFO: the program continues, 3Q26 call)"),
        ("bl3", "", "b", None, "", ""),
        ("h_b", "Option B check: every ratio from 9M26", "h", None, "", ""),
        ("b_ebit", "Operating income", "vf", "=B{s26}*(E{q_gm}-E{q_gr}-E{q_or})", "[calc]", ""),
        ("b_e", "Adjusted EBITDA", "vf", "=B{b_ebit}+B{a_da}", "[calc]", ""),
        ("b_m", "Adjusted EBITDA margin", "vf", "=B{b_e}/B{s26}", "[calc]", ""),
        ("b_d", "Difference B - A", "vf", "=B{b_e}-B{e26}", "[calc]", ""),
        ("b_dbp", "Difference B - A (bp of net sales)", "vf", "=B{b_d}/B{s26}*10000", "[calc]",
         "A small difference means the guide is consistent with 9M26"),
        ("bl6", "", "b", None, "", ""),
        ("h_f", "FY2027E net sales by region: organic growth = ratio x nominal GDP growth (team decisions 2026-10-25)",
         "h", None, "", ""),
    ] + [
        x for k, lab in REG27 for x in (
            ("rt_" + k, "Organic ratio, %s" % lab, "vf", ml(("rt", k), RATIO27[k]), "[assumption]",
             "Team: organic 9M26 ex-FX growth / nominal GDP growth 2026; " + MACRO + ", sheet Organic_pass"),
            ("gd_" + k, "Nominal GDP growth 2027 in local currency, %s" % lab, "vf", ml(("gd", 2027, k), GDP27[k]), "[calc]",
             "Capital IQ levels; %s, %s" % (MACRO, GDPSRC[k])),
            ("go_" + k, "Organic net sales growth FY2027E excluding FX, %s" % lab, "vf", "=B{rt_%s}*B{gd_%s}" % (k, k),
             "[calc]", "Ratio x GDP growth"),
            ("wt_" + k, "Weight in 9M26 regional sales, %s" % lab, "vf",
             "=E{r9_%s}/(E{r9_na}+E{r9_mx}+E{r9_la}+E{r9_eaa})" % k, "[calc]", ""))] + [
        ("g27x", "Net sales growth FY2027E excluding FX", "vf",
         "=B{go_na}*B{wt_na}+B{go_mx}*B{wt_mx}+B{go_la}*B{wt_la}+B{go_eaa}*B{wt_eaa}", "[calc]",
         "Regions weighted by 9M26 sales; intersegment eliminations move with the total"),
    ] + [
        x for k, lab in REG27 for x in (
            fxl_row("fxl_" + k, "FX factor local currency to USD FY2027E, %s" % lab, k, 2027, FXL27[k], FXLSRC[k]),
            ("fxm_" + k, "FX factor to MXN FY2027E, %s" % lab, "vf",
             "=1" if k == "mx" else "=B{fxl_%s}*B{fx27}/B{fxy}" % k, "[calc]",
             "Peso business" if k == "mx" else "Local currency to USD x USD/MXN average FY2027E / FY2026E"),
            ("s26_" + k, "Net sales FY2026E, %s" % lab, "vf", "=B{s26}*B{wt_%s}" % k, "[calc]",
             "FY2026E split with the 9M26 regional mix (team 2026-10-25: no 4Q seasonality); eliminations pro rata"),
            ("s27_" + k, "Net sales FY2027E, %s" % lab, "vf", "=B{s26_%s}*(1+B{go_%s})*B{fxm_%s}" % (k, k, k), "[calc]",
             "FY2026E x (1 + organic growth in local currency) x FX factor to MXN"))] + [
        ("s27", "Net sales FY2027E", "vf", "=B{s27_na}+B{s27_mx}+B{s27_la}+B{s27_eaa}", "[calc]",
         "Sum of regions; replaces the FY2022-FY2026E CAGR (advisor's feedback, memory.md 2026-10-24)"),
        ("g27m", "Net sales growth FY2027E in MXN", "vf", "=B{s27}/B{s26}-1", "[calc]", "Reported-currency growth"),
        ("g27b", "  of which business growth (organic, excluding FX)", "vf", "=B{g27x}", "[calc]", "Advisor: split business vs FX"),
        ("g27f", "  of which FX effect", "vf", "=B{g27m}-B{g27b}", "[calc]",
         "Growth in MXN less growth excluding FX, the way Bimbo reports it"),
        ("elf", "Regional sales before intersegment eliminations / consolidated net sales, 9M26", "vf",
         "=(E{r9_na}+E{r9_mx}+E{r9_la}+E{r9_eaa})/E{q_s}", "[calc]",
         "Shows the forecast regions in sheet Segments on the same basis as the history (before eliminations)"),
    ] + sales_2028_2030_rows() + [
        ("bl7", "", "b", None, "", ""),
        ("h_g", "FY2027E cost of sales by nature (team decisions 2026-10-23)", "h", None, "", ""),
        ("n_rm", "Raw materials FY2025", "v", 129712, "[sourced]", "Costs by nature, EEFF25 p.82"),
        ("n_wg", "Wages and benefits FY2025", "v", 40113, "[sourced]", "Costs by nature, EEFF25 p.82"),
        ("n_fr", "Freight, fuel and maintenance FY2025", "v", 18374, "[sourced]", "Costs by nature, EEFF25 p.82"),
        ("n_dp", "Depreciation FY2025", "v", 10070, "[sourced]", "Costs by nature, EEFF25 p.82"),
        ("n_ot", "Other cost of sales FY2025", "v", 5196, "[sourced]",
         "EEFF25 p.82: professional services 1,607 + low-value leases 1,634 + indirect taxes 1,391 + travel 230 + other 334"),
        ("n_chk", "Check: lines less IS cost of sales FY2025 (must be 0)", "vf",
         "=B{n_rm}+B{n_wg}+B{n_fr}+B{n_dp}+B{n_ot}-%s!F%d" % (isn, is_r["cogs"]), "[calc]", ""),
        ("el", "Elasticity of raw materials / net sales to prior-year wheat", "v", 0.109, "[assumption]",
         "Team-approved log-log fit FY2018-FY2025, one-year lag, R2 0.70 (same-year 0.099, R2 0.48); "
         "costs-by-nature notes RA BMV 2020 p.283, RA 2022 p.308, RA 2024 p.317, EEFF25 p.82"),
        ("w24", "Wheat price 2024 (US$/t, annual average)", "v", 201.1949, "[sourced]",
         "IMF global price of wheat, FRED PWHEAMTUSDM"),
        ("w25", "Wheat price 2025 (US$/t, annual average)", "v", 173.0919, "[sourced]",
         "IMF global price of wheat, FRED PWHEAMTUSDM"),
        ("w9m", "Wheat price Jan-Sep 2026 (US$/t, average)", "v", 208.2778, "[sourced]",
         "Average of the nine monthly values, FRED PWHEAMTUSDM"),
        ("wsep", "Wheat price Sep-2026 (US$/t)", "v", 246.8518, "[sourced]", "FRED PWHEAMTUSDM"),
        ("w26", "Wheat price 2026E (US$/t, annual average)", "vf", "=(9*B{w9m}+3*B{wsep})/12", "[assumption]",
         "Team: nine actual months + Oct-Dec held at the Sep-2026 level; replace with actuals as FRED publishes them"),
        ("rr25", "Raw materials / net sales FY2025", "vf", "=B{n_rm}/B{s25}", "[calc]", ""),
        ("rr26", "Raw materials / net sales FY2026E", "vf", "=B{rr25}*(B{w25}/B{w24})^B{el}", "[calc]",
         "FY2025 ratio moved by the 2025 wheat change (one-year lag)"),
        ("rm26", "Raw materials FY2026E", "vf", "=B{s26}*B{rr26}", "[calc]", ""),
        ("nr26", "Other cost of sales lines FY2026E (total less raw materials)", "vf", "=B{a_c}-B{rm26}", "[calc]",
         "FY2026E cost of sales (option A) less raw materials"),
        ("wg26", "  Wages and benefits FY2026E", "vf", "=B{nr26}*B{n_wg}/(B{n_wg}+B{n_fr}+B{n_dp}+B{n_ot})", "[calc]",
         "FY2025 mix of the non-raw-material lines"),
        ("fr26", "  Freight, fuel and maintenance FY2026E", "vf", "=B{nr26}*B{n_fr}/(B{n_wg}+B{n_fr}+B{n_dp}+B{n_ot})",
         "[calc]", "FY2025 mix of the non-raw-material lines"),
        ("dp26", "  Depreciation FY2026E", "vf", "=B{nr26}*B{n_dp}/(B{n_wg}+B{n_fr}+B{n_dp}+B{n_ot})", "[calc]",
         "FY2025 mix of the non-raw-material lines"),
        ("ot26", "  Other FY2026E", "vf", "=B{nr26}*B{n_ot}/(B{n_wg}+B{n_fr}+B{n_dp}+B{n_ot})", "[calc]",
         "FY2025 mix of the non-raw-material lines"),
        ("rr27", "Raw materials / net sales FY2027E", "vf", "=B{rr26}*(B{w26}/B{w25})^B{el}", "[calc]",
         "FY2026E ratio moved by the 2026E wheat change (one-year lag)"),
        ("rm27", "Raw materials FY2027E", "vf", "=B{s27}*B{rr27}", "[calc]", ""),
        ("wg27", "Wages and benefits FY2027E", "vf", "=B{wg26}/B{s26}*B{s27}", "[assumption]",
         "Team: no specific adjustment (minimum wage, 46-hour week are risks only); FY2026E ratio to net sales"),
        ("fr27", "Freight, fuel and maintenance FY2027E", "vf", "=B{fr26}/B{s26}*B{s27}", "[assumption]",
         "Team: FY2026E ratio to net sales; the fuel share of this line is not disclosed (GRI 302-1 gives group fuel only, "
         "two-thirds of diesel burnt by third-party carriers), so diesel stays a risk and sensitivity"),
        ("dp27", "Depreciation FY2027E", "vf", "=B{dp26}/B{ppe_d}*B{ppd27}", "[calc]",
         "Audit fix H-03: FY2026E share of the PP&E part x PP&E depreciation (rate x opening PP&E); the 9M26 non-cash items are not projected"),
        ("ot27", "Other cost of sales FY2027E", "vf", "=B{ot26}/B{s26}*B{s27}", "[assumption]", "FY2026E ratio to net sales"),
        ("c27", "Cost of sales FY2027E", "vf", "=B{rm27}+B{wg27}+B{fr27}+B{dp27}+B{ot27}", "[calc]", "Feeds the IS"),
        ("gm27", "Gross margin FY2027E", "vf", "=1-B{c27}/B{s27}", "[calc]",
         "Result, not a target; consensus 52.0% (CIQ, 20-Sep-2026) for reference only"),
        ("bl8", "", "b", None, "", ""),
        ("h_h", "FY2027E capex and PP&E depreciation (team decisions 2026-10-23)", "h", None, "", ""),
        ("cx26g", "Capex FY2026 original guide, midpoint (US$ millions)", "v", 1300, "[guidance]",
         "US$1.2-1.4bn, 4Q25 deck p.17 (26-Feb-2026); cut to US$1.0-1.2bn in July (2Q26 deck) after deferring projects"),
        ("dfr", "Projects deferred from 2026 to 2027 (US$ millions)", "vf", "=B{cx26g}-B{cx_usd}", "[calc]",
         "Original guide midpoint less FY2026E capex"),
        ("cx27_usd", "Capex FY2027E (US$ millions)", "vf", "=B{cx_usd}+B{dfr}", "[assumption]",
         "Team: FY2026E level + every deferred project lands in 2027 (prudent: more cash out); "
         "CFO said 'a little bit higher' than 2026 (3Q26 call)"),
        ("fx27", "USD/MXN average FY2027E", "vf", "=B{cq2027}", "[assumption]",
         "Team 2026-10-25: Capital IQ forecast for every year FY2027E-FY2030E (same source as GDP and regional FX); replaces the Banxico survey average (17.50 + 18.04) / 2 = 17.77"),
        ("cx27", "Capex FY2027E", "vf", "=B{cx27_usd}*B{fx27}", "[calc]", "Purchases of PP&E in the cash flow"),
        ("ppd25", "PP&E depreciation FY2025", "v", 16375, "[sourced]", "PP&E roll-forward, EEFF25 p.38"),
        ("ppe24", "Net PP&E at 31-Dec-2024", "v", 155376, "[sourced]", "PP&E roll-forward, EEFF25 p.38"),
        ("dr", "PP&E depreciation rate (on opening net PP&E)", "vf", "=B{ppd25}/B{ppe24}", "[calc]",
         "FY2025; straight-line, useful lives EEFF25 p.28"),
        ("ppd26", "PP&E depreciation FY2026E at that rate", "vf", "=B{dr}*%s!F%d" % (bsn, BS_ROWNUM["ppe"]), "[calc]",
         "Rate x net PP&E Dec-25"),
        ("ppd27", "PP&E depreciation FY2027E", "vf", "=B{dr}*%s!G%d" % (bsn, BS_ROWNUM["ppe"]), "[calc]",
         "Rate x net PP&E Dec-26: 2026 capex depreciates in 2027; 2027 capex mostly from 2028"),
        ("bl9", "", "b", None, "", ""),
        ("h_i", "FY2027E general and other expenses by nature (team decisions 2026-10-23)", "h", None, "", ""),
    ]
    # FY2025 expenses by nature (EEFF25 p.82): key, label, FY2025, FY2027E method
    opex = [
        ("wg", "Wages and benefits", 84493, "r"),
        ("fr", "Freight, fuel and maintenance", 42263, "r"),
        ("ad", "Advertising and promotion", 15637, "r"),
        ("ps", "Professional services and consulting", 12180, "r"),
        ("lg", "Logistics costs", 6109, "r"),
        ("mp", "Multi-employer pension plan cancellation and revaluation", 27, "n"),
        ("ig", "Integration expenses", 541, "n"),
        ("tx", "Indirect taxes", 1759, "r"),
        ("rs", "Restructuring expenses", 3908, "n"),
        ("ls", "Low-value and short-term leases", 3330, "r"),
        ("tv", "Travel expenses", 1842, "r"),
        ("ot", "Other", 2484, "o"),
    ]
    nda = "+".join("B{o_%s}" % k for k, *_ in opex)
    for k, label, v25, _ in opex:
        rows.append(("o_" + k, label + " FY2025", "v", v25, "[sourced]", "Expenses by nature, EEFF25 p.82"))
    rows += [
        ("o_da", "Depreciation and amortization FY2025", "v", 14768, "[sourced]", "Expenses by nature, EEFF25 p.82"),
        ("o_chk", "Check: lines less IS general and other expenses FY2025 (must be 0)", "vf",
         "=B{o_da}+" + nda + "-SUM(%s!F%d:F%d)" % (isn, is_r["dist"], is_r["oth"]), "[calc]", ""),
        ("n22_nr", "Non-recurring items inside Other FY2025 (brand impairment 67, gain on PP&E sale -6)", "v", 61,
         "[sourced]", "Other expenses, net, EEFF25 p.83 (note 22)"),
        ("n22_tot", "Other (income) expenses, net FY2025", "v", 4911, "[sourced]", "EEFF25 p.83 (note 22)"),
        ("n22_rec", "Recurring part of other expenses, net FY2025 (amortization 146 + labor provision 1 + other 768)",
         "v", 915, "[sourced]", "EEFF25 p.83 (note 22); restructuring, MEPP, impairments and gains excluded"),
        ("oda26", "Depreciation and amortization in expenses FY2026E", "vf", "=B{a_da}-B{dp26}", "[calc]",
         "IS D&A FY2026E less cost-of-sales depreciation"),
        ("ond26", "Other expense lines FY2026E (total less D&A)", "vf", "=B{a_g}+B{a_o}-B{oda26}", "[calc]",
         "Audit fix H-01: FY2026E general + other expenses (option A) less D&A; non-recurring lines from 1H26 x 2, the rest by the FY2025 mix of the recurring lines"),
        ("h1_mp", "Multi-employer pension plan revaluation 1H26", "v", -14.032, "[sourced]",
         "Audit fix H-01: BMV Jun-26 p.81, expenses by nature (MXN thousands -14,032)"),
        ("h1_ig", "Integration expenses 1H26", "v", 366.681, "[sourced]",
         "Audit fix H-01: BMV Jun-26 p.81, expenses by nature (MXN thousands 366,681)"),
        ("h1_rs", "Restructuring expenses 1H26", "v", 1708.999, "[sourced]",
         "Audit fix H-01: BMV Jun-26 p.82, expenses by nature (MXN thousands 1,708,999; 1H25 1,763,831)"),
    ]
    nrs = "".join("-B{p_%s}" % k for k, _, _, m in opex if m == "n")
    rda = "+".join("B{o_%s}" % k for k, _, _, m in opex if m != "n")
    for k, label, _, m in opex:
        if m == "n":
            rows.append(("p_" + k, "  %s FY2026E" % label, "vf", "=2*B{h1_%s}" % k, "[assumption]",
                         "Audit fix H-01: 1H26 actual x 2 (second half = first half); replaces the FY2025 mix"))
        else:
            rows.append(("p_" + k, "  %s FY2026E" % label, "vf", "=(B{ond26}%s)*B{o_%s}/(%s)" % (nrs, k, rda), "[calc]",
                         "Audit fix H-01: non-D&A lines less the non-recurring lines, by the FY2025 mix of the recurring lines"))
    method = {
        "r": ("vf", "=B{p_%s}/B{s26}*B{s27}", "[assumption]", "FY2026E ratio to net sales"),
        "z": ("v", 0, "[assumption]", "Revaluation with no pattern (175 / -982 / 27 in 2023-2025, EEFF25 p.82); not projected"),
        "n": ("v", 0, "[assumption]", "Non-recurring: not projected (team 2026-10-25, advisor feedback: organic, no non-recurring items)"),
        "o": ("vf", "=B{p_%s}/B{s26}*B{s27}*(1-B{n22_nr}/B{o_%s})", "[assumption]",
              "FY2026E ratio to net sales, less the FY2025 non-recurring share (impairment, PP&E gain)"),
    }
    notes = {
        "wg": "Team: no specific adjustment (minimum wage, 46-hour week are risks only); FY2026E ratio to net sales",
        "fr": "Team: FY2026E ratio to net sales; diesel stays a risk (fuel share not disclosed)",
    }
    for k, label, _, m in opex:
        kind, formula, tag, note = method[m]
        payload = formula.replace("%s", k) if isinstance(formula, str) else formula
        rows.append(("q27_" + k, "%s FY2027E" % label, kind, payload, tag, notes.get(k, note)))
    rows += [
        ("q27_da", "Depreciation and amortization in expenses FY2027E", "vf",
         "=B{rou27}+B{amort}+(B{oda26}-B{rou_d}-B{amort})/B{ppe_d}*B{ppd27}", "[calc]",
         "Audit fixes H-03, H-05: right-of-use depreciation grows with net sales; amortization held at FY2025; PP&E part = its FY2026E share x PP&E depreciation"),
        ("x27", "General and other expenses FY2027E", "vf", "=B{q27_da}+" + "+".join("B{q27_%s}" % k for k, *_ in opex),
         "[calc]", "Feeds the IS"),
        ("x27_o", "  Other (income) expenses, net", "vf", "=B{a_o}*B{n22_rec}/B{n22_tot}/B{s26}*B{s27}", "[calc]",
         "FY2026E ratio to net sales, recurring part only (FY2025 mix, EEFF25 p.83): restructuring, MEPP, impairments, gains out"),
        ("x27_i", "  Integration", "vf", "=B{q27_ig}", "[calc]", ""),
        ("x27_d", "  Distribution and selling", "vf",
         "=(B{x27}-B{x27_o}-B{x27_i})*%s!F%d/(%s!F%d+%s!F%d)" % (isn, is_r["dist"], isn, is_r["dist"], isn, is_r["admin"]),
         "[calc]", "FY2025 split of distribution and administration"),
        ("x27_a", "  Administrative", "vf", "=B{x27}-B{x27_o}-B{x27_i}-B{x27_d}", "[calc]", ""),
        ("da27", "D&A FY2027E (IS memo)", "vf", "=B{dp27}+B{q27_da}", "[calc]", "Cost-of-sales depreciation + expenses D&A"),
        ("x27_r", "General and other expenses / net sales FY2027E", "vf", "=B{x27}/B{s27}", "[calc]", "Compare with FY2026E"),
        ("x26_r", "General and other expenses / net sales FY2026E", "vf", "=(B{a_g}+B{a_o})/B{s26}", "[calc]", ""),
        ("ebit27", "Operating income FY2027E", "vf", "=B{s27}-B{c27}-B{x27}", "[calc]", ""),
        ("em27", "Adjusted EBITDA margin FY2027E", "vf", "=(B{ebit27}+B{da27})/B{s27}", "[calc]",
         "Result, not a target; compare with FY2026E excluding restructuring"),
        ("em26x", "Adjusted EBITDA margin FY2026E excluding restructuring (comparison only)", "vf",
         "=(B{e26}+B{p_rs})/B{s26}", "[calc]",
         "FY2026E keeps the 9M26 restructuring actually booked; FY2027E has none, so compare FY2027E with this line"),
        ("bl10", "", "b", None, "", ""),
        ("h_j", "FY2027E below operating income (team decisions 2026-10-23)", "h", None, "", ""),
        ("debt26", "Gross debt at 31-Dec-2026E", "vf", "=%s!G%d+%s!G%d" % (bsn, BS_ROWNUM["std"], bsn, BS_ROWNUM["ltd"]),
         "[calc]", "Balance sheet FY2026E"),
        ("mat27_usd", "Debt maturing in 2027 (US$ millions)", "v", 677, "[sourced]", "Amortization profile, 3T26 rel. p.6"),
        ("mat27", "2027 maturity repaid", "vf", "=B{mat27_usd}*B{mat_fx}", "[sourced]",
         "Contractual maturity at the profile's USD/MXN 17.84 (mostly Bimbo 17, MXN 9,633, due 24-Sep-2027)"),
        ("refi27", "New borrowing FY2027E (refinancing of the 2027 maturity)", "vf", "=B{mat27}", "[assumption]",
         "Team 2026-10-25: refinanced in full, as Bimbo did in 2025 (MXN 15bn) and 2026 (MXN 12bn, Bimbo 16 prepaid 10-Feb-2026); "
         "net debt is the same either way"),
        ("mat28_usd", "Debt maturing in 2028 (US$ millions)", "v", 833, "[sourced]",
         "Maturity ladder, 2Q26 investor presentation p.17 (latest ladder with 2028; the 3T26 profile shows 2027 only in the files)"),
        ("mat28", "2028 maturity, current portion at 31-Dec-2027E", "vf", "=B{mat28_usd}*B{mat_fx}", "[calc]",
         "Reclassified from long-term to current debt: due within 12 months of the balance date"),
        ("debt27", "Gross debt at 31-Dec-2027E", "vf", "=B{debt26}-B{mat27}+B{refi27}", "[calc]",
         "Carried in MXN at 17.84 (team): translation of the hedged balance goes to OCI"),
        ("kd_rep", "Average cost of debt reported by Bimbo (incl. derivatives), reference", "v", 0.065, "[sourced]", "3T26 rel. p.6"),
        ("debt25", "Gross debt at 31-Dec-2025", "vf", "=%s!F%d+%s!F%d" % (bsn, BS_ROWNUM["std"], bsn, BS_ROWNUM["ltd"]),
         "[sourced]", "Balance sheet FY2025 (EEFF25)"),
        ("fxf26", "FX factor on interest FY2026E", "vf", "=(1-B{fxsh})+B{fxsh}*B{fxy}/B{mat_fx}", "[calc]",
         "Same formula as FY2027E, with the FY2026E USD/MXN average"),
        ("kd", "Cost of debt applied FY2027E-FY2030E (FY2026E run-rate, all-in net)", "vf",
         "=(B{c_int}-B{l_int})/((B{debt25}+B{debt26})/2)/B{fxf26}", "[calc]",
         "Audit fix H-04: the rate that, in the FY2027E formula, reproduces FY2026E net interest (9M26 + 4Q26 = 3Q26) less lease interest; "
         "net of interest income, which the IS sets to 0 from FY2026E"),
        ("fxsh", "Share of debt outside MXN", "v", 0.60, "[sourced]", "43% USD, 12% EUR, 3% CAD, 2% GBP; 3T26 rel. p.6"),
        ("fxf", "FX factor on interest", "vf", "=(1-B{fxsh})+B{fxsh}*B{fx27}/B{mat_fx}", "[calc]",
         "Team: FX enters through interest; USD/MXN average FY2027E vs the 17.84 balance rate"),
        ("rou27", "Right-of-use depreciation FY2027E", "vf", "=B{rou_d}*B{s27}/B{s26}", "[calc]",
         "Audit fix H-05: FY2025 level x net sales FY2027E / FY2026E (leases grow with sales, valuation basis v2 2026-10-17)"),
        ("li27", "Lease interest FY2027E", "vf", "=B{l_int}*B{s27}/B{s26}", "[calc]",
         "Audit fix H-05: FY2025 level x net sales FY2027E / FY2026E (leases grow with sales, valuation basis v2 2026-10-17)"),
        ("int27", "Interest expense FY2027E", "vf", "=(B{debt26}+B{debt27})/2*B{kd}*B{fxf}+B{li27}", "[calc]",
         "Audit fixes H-04, H-05: average gross debt x cost of debt (FY2026E run-rate) x FX factor + lease interest growing with net sales"),
        ("mon27", "Monetary position loss (gain) FY2027E", "vf", "=B{c_mon}", "[assumption]", "Held at FY2026E"),
        ("as27", "Share of results of associates FY2027E", "vf", "=B{c_as}", "[assumption]", "Held at FY2026E"),
        ("etr27", "Effective tax rate FY2027E", "v", 0.37, "[assumption]",
         "Team 2026-10-23: FY2026E 9M rate held; Brazil matures only in 3Q27, so the unrecognized tax-loss effect "
         "(+4.18 pp in FY2025, EEFF25 p.57) stays all year"),
        ("nci27", "Non-controlling interest FY2027E", "vf", "=B{c_nci}/B{s26}*B{s27}", "[calc]",
         "FY2026E ratio to net sales: the US distributors earn on sales, not on Bimbo's interest or taxes"),
        ("bl11", "", "b", None, "", ""),
        ("h_k", "FY2027E balance sheet and cash flow (same methods as FY2026E)", "h", None, "", ""),
        ("infl27", "Mexico consumer inflation 2027 (annual average)", "vf", ml(("cpi", 2027, "mx"), 0.039), "[sourced]",
         "Capital IQ consumerPriceInflation, data/capitaliq/capiq-sales-drivers-M1_2026-10-24.md; " + MACRO + ", sheet IAS29_test"),
        ("dps27", "Dividend per share 2027 (MXN)", "vf", "=B{dps}*(1+B{infl27})", "[assumption]",
         "CFO: grow the dividend 'slightly above inflation' (3Q26 call); 'slightly' is not quantified, so at inflation"),
        ("div27", "Dividends declared FY2027E, controlling", "vf", "=B{dps27}*B{c_sh}", "[calc]",
         "Same share count as FY2026E"),
        ("divn27", "Dividends to non-controlling interest FY2027E", "vf", "=B{divn}", "[assumption]", "Held at FY2026E (FY2025)"),
        ("bb27", "Share repurchases FY2027E", "vf",
         "=-AVERAGE(%s!B%d:F%d)" % (sn("CF"), CF_ROWNUM["buyb"], CF_ROWNUM["buyb"]), "[assumption]",
         "Team 2026-10-25: average FY2021-FY2025 (cash flow statement); CFO: the program continues, no amount given (3Q26 call)"),
    ]
    rows += fcst_2028_2030_rows(is_r, opex)
    pct = {"q_gm", "q_gr", "q_or", "q_dr", "q_em", "q_gx", "g4q", "mxsh", "gs26", "m25", "bp", "one", "m26",
           "e4q26m", "e4q25m", "a_gr", "b_m", "q_etr", "c_etr", "rr25", "rr26", "rr27", "gm27", "dr", "x27_r", "x26_r", "em27", "kd", "kd_rep", "fxsh", "etr27",
           "g27x", "g27m", "g27b", "g27f", "infl27", "em26x", "ig25", "ig1hr",
           "gT", "gTb", "gTf", "gTmx", "gTd", "gTmix", "gTfx", "gT30", "cpiT_mx", "cpiT_us", "cxr", "etr3", "rT_tax", "waccR", "ronic", "rvr30", "ronicT", "rvT", "roicW", "ronicW"} | {
           "roic%d" % yy for yy in (28, 29, 30)} | {
           p % yy for p in ("gm%d", "x%d_r", "em%d", "infl%d") for yy in (28, 29, 30)} | {"g%d%s" % (y, x) for y in YRS3 for x in "mbf"} | {
           "gd%d_%s" % (y, k) for y in YRS3 for k, _ in REG27} | {p + k for p in ("wT_", "gT_") for k, _ in REG27} | {p + k for p in ("gd_", "go_", "wt_") for k, _ in REG27}
    ratio_keys = {p + k for p in ("rt_", "fxl_", "fxm_") for k, _ in REG27} | {
        p % (y, k) for p in ("fxl%d_%s", "fxm%d_%s") for y in YRS3 for k, _ in REG27} | {
        "fx28", "fx29", "fx30", "cq2027", "cq2028", "cq2029", "cq2030", "drT", "gTr", "fxlT_la", "fxlT_eaa"} | {"fxf%d" % yy for yy in (28, 29, 30)} | {"elf", "fxf26"} | {"rtT_" + k for k, _ in REG27}
    rn = {key: hdr + 1 + i for i, (key, *_) in enumerate(rows)}
    alan = False
    for key, label, kind, payload, tag, note in rows:
        r = rn[key]
        a = ws.cell(r, 1, t(label))
        if kind == "h":
            alan = key in ALAN_H
            a.font = BOLD
            for col in "ABCDE":
                ws[f"{col}{r}"].fill = FILL_SEC
            if key != "h_q":
                ws[f"B{r}"] = t("Value")
                ws[f"B{r}"].font = BOLD
            if alan:
                for col in "ABCDEFG":
                    ws[f"{col}{r}"].fill = FILL_ALAN_H
                    ws[f"{col}{r}"].font = ALAN_FONT
                ws[f"G{r}"] = t("Applies the advisor's feedback (Alan): see sheet Methodology")
            continue
        if kind == "b":
            continue
        a.font = BLACK
        fmt = '0.00%;(0.00%);"-"' if key in ("rr25", "rr26", "rr27", "rr28", "rr29", "rr30") else ('0.0%;(0.0%);"-"' if key in pct else ('0.0000' if key in ("fx25", "fx26", "fac", "fx9m", "fxy", "mat_fx", "el", "fx27", "fxf", "fac27") or key in ratio_keys else
                                                 ('0.00' if key in ("w24", "w25", "w9m", "wsep", "w26", "w27", "w28", "w29") else
                                                 ('0.0;(0.0)' if key in ("b_dbp", "d_ar", "d_inv", "d_ap") else
                                                  ('#,##0.000' if key in ("c_sh", "dps", "dps27", "dps28", "dps29", "dps30") else NUM)))))
        cells = []
        if kind == "q":
            for j, col in enumerate("BCD"):
                ws[f"{col}{r}"] = payload[j]
                ws[f"{col}{r}"].font = BLUE
                cells.append(ws[f"{col}{r}"])
            ws[f"E{r}"] = f"=SUM(B{r}:D{r})"
            cells.append(ws[f"E{r}"])
        elif kind == "qf":
            for col in "BCDE":
                ws[f"{col}{r}"] = payload.format(c=col, **rn)
                cells.append(ws[f"{col}{r}"])
        elif kind == "v":
            ws[f"B{r}"] = payload
            ws[f"B{r}"].font = BLUE
            if tag == "[assumption]":
                ws[f"B{r}"].fill = FILL_IN
            cells.append(ws[f"B{r}"])
        elif kind == "vf":
            ws[f"B{r}"] = payload.format(**rn)
            cells.append(ws[f"B{r}"])
        for c in cells:
            c.number_format = fmt
        ws[f"F{r}"] = t(tag)
        ws[f"G{r}"] = t(note)
        ws[f"F{r}"].font = NOTE
        ws[f"G{r}"].font = NOTE
        if alan:
            for col in "AFG":
                ws[f"{col}{r}"].fill = FILL_ALAN
    ws.column_dimensions["A"].width = 60
    for col in "BCDE":
        ws.column_dimensions[col].width = 12
    ws.column_dimensions["F"].width = 13
    ws.column_dimensions["G"].width = 90
    return rn


def link_is_2026(wb, is_r, rn):
    """FY2026E income statement from the Assumptions sheet: option A down to EBIT, then the lines below it."""
    ws = wb[sn("IS")]
    an = sn("Assumptions")
    links = {"sales": "s26", "cogs": "a_c", "dist": "a_dist", "admin": "a_adm", "integ": "a_int",
             "oth": "a_o", "da": "a_da", "intexp": "c_int", "fx": "c_fx", "mon": "c_mon", "assoc": "c_as",
             "nci": "c_nci", "shares": "c_sh"}
    col = FC[0]
    for is_key, a_key in links.items():
        c = ws[f"{col}{is_r[is_key]}"]
        c.value = f"={an}!B{rn[a_key]}"
        c.font = BLACK
        c.fill = PatternFill(fill_type=None)
    c = ws[f"{col}{is_r['tax']}"]
    c.value = f"={col}{is_r['pbt']}*{an}!B{rn['c_etr']}"
    c.font = BLACK
    c.fill = PatternFill(fill_type=None)
    for key in ("othnc", "intinc", "disc"):
        c = ws[f"{col}{is_r[key]}"]
        c.value = 0
        c.font = BLUE
        c.fill = PatternFill(fill_type=None)
    for is_key, a_key in {"sales": "s27", "cogs": "c27", "dist": "x27_d", "admin": "x27_a", "integ": "x27_i",
                          "oth": "x27_o", "da": "da27", "intexp": "int27", "mon": "mon27", "assoc": "as27",
                          "nci": "nci27", "shares": "c_sh"}.items():
        c = ws[f"{FC[1]}{is_r[is_key]}"]
        c.value = f"={an}!B{rn[a_key]}"
        c.font = BLACK
        c.fill = PatternFill(fill_type=None)
    c = ws[f"{FC[1]}{is_r['tax']}"]
    c.value = f"={FC[1]}{is_r['pbt']}*{an}!B{rn['etr27']}"
    c.font = BLACK
    c.fill = PatternFill(fill_type=None)
    # Interest income = 0 (team 2026-10-25: not operating; FCFF excludes it, cash enters in the DCF bridge); FX result 0 (sign not forecastable, as the VPPA)
    for key in ("othnc", "intinc", "fx", "disc"):
        c = ws[f"{FC[1]}{is_r[key]}"]
        c.value = 0
        c.font = BLUE
        c.fill = PatternFill(fill_type=None)


def link_segments(wb, seg_r, is_r, rn):
    """FY2026E-FY2030E net sales by region from Assumptions, shown before intersegment eliminations like the history.

    The Assumptions regions carry the eliminations pro rata (9M26 mix); each one is grossed up by the 9M26 ratio of
    regional sales before eliminations to consolidated sales, and the eliminations line closes to IS net sales.
    """
    ws = wb[sn("Segments")]
    an, isn = sn("Assumptions"), sn("IS")
    for i, y in enumerate((2026, 2027, 2028, 2029, 2030)):
        col = FC[i]
        for k, _ in REGIONS:
            a_key = ("s%d_%s" % (y % 100, k)) if y < 2028 else ("s%d_%s" % (y, k))
            c = ws[f"{col}{seg_r['s_' + k]}"]
            c.value = f"={an}!B{rn[a_key]}*{an}!B{rn['elf']}"
            c.font = BLACK
            c.number_format = NUM
        c = ws[f"{col}{seg_r['s_el']}"]
        c.value = f"={isn}!{col}{is_r['sales']}-SUM({col}{seg_r['s_' + REGIONS[0][0]]}:{col}{seg_r['s_' + REGIONS[-1][0]]})"
        c.font = BLACK
        c.number_format = NUM
        c = ws[f"{col}{seg_r['s_tot']}"]
        c.value = f"=SUM({col}{seg_r['s_' + REGIONS[0][0]]}:{col}{seg_r['s_el']})"
        c.font = BOLD
        c.number_format = NUM
        c.border = TOP


def link_is_2028_2030(wb, is_r, rn):
    """FY2028E-FY2030E income statement from the Assumptions sheet, as FY2027E."""
    ws = wb[sn("IS")]
    an = sn("Assumptions")
    for i, y in enumerate(YRS3, 2):
        col, yy = FC[i], y % 100
        links = {"sales": "s%d" % y, "cogs": "c%d" % yy, "dist": "x%d_d" % yy, "admin": "x%d_a" % yy,
                 "integ": "x%d_i" % yy, "oth": "x%d_o" % yy, "da": "da%d" % yy, "intexp": "int%d" % yy,
                 "mon": "mon%d" % yy, "assoc": "as%d" % yy, "nci": "nci%d" % yy, "shares": "c_sh"}
        for is_key, a_key in links.items():
            c = ws[f"{col}{is_r[is_key]}"]
            c.value = f"={an}!B{rn[a_key]}"
            c.font = BLACK
            c.fill = PatternFill(fill_type=None)
        c = ws[f"{col}{is_r['tax']}"]
        c.value = f"={col}{is_r['pbt']}*{an}!B{rn['etr3']}"
        c.font = BLACK
        c.fill = PatternFill(fill_type=None)
        # interest income, FX result and the other lines = 0, as FY2027E (team 2026-10-25)
        for key in ("othnc", "intinc", "fx", "disc"):
            c = ws[f"{col}{is_r[key]}"]
            c.value = 0
            c.font = BLUE
            c.fill = PatternFill(fill_type=None)


def link_bs_cf_2026(wb, is_r, bs_r, cf_r, eq_r, oci_r, rn):
    """FY2026E balance sheet, cash flow, equity and OCI from the Assumptions sheet.

    Lines without a driver are held at FY2025 (BS) or set to 0 (flows), so every
    balance-sheet change has its cash-flow or equity counterpart and Checks closes.
    """
    col, prev = FC[0], COLS[4]
    an, isn, bsn, cfn, eqn = sn("Assumptions"), sn("IS"), sn("BS"), sn("CF"), sn("Equity")
    a = {k: f"{an}!B{v}" for k, v in rn.items()}

    def put(sheet, rows, values):
        ws = wb[sn(sheet)]
        for key, r in rows.items():
            if key not in values:
                continue
            c = ws[f"{col}{r}"]
            c.value = values[key]
            c.font = BLUE if values[key] == 0 else BLACK
            c.fill = PatternFill(fill_type=None)

    bs = {k: f"={prev}{r}" for k, (r, kind) in
          {k: (bs_r[k], kind) for k, _, kind, *_ in BS_ROWS}.items() if kind == "i"}
    bs.update({
        "cash": f"={cfn}!{col}{cf_r['end']}",
        "ar": f"={isn}!{col}{is_r['sales']}*{a['d_ar']}/365",
        "inv": f"={isn}!{col}{is_r['cogs']}*{a['d_inv']}/365",
        "ap": f"={isn}!{col}{is_r['cogs']}*{a['d_ap']}/365",
        "ppe": f"={prev}{bs_r['ppe']}+{a['cx']}-{a['ppe_d']}",
        "intang": f"={prev}{bs_r['intang']}-{a['amort']}",
        "assoc": f"={prev}{bs_r['assoc']}+{isn}!{col}{is_r['assoc']}",
        "std": f"={a['std_sep']}-{a['mat']}",
        "ltd": f"={a['ltd_sep']}",
        "re": f"={prev}{bs_r['re']}+SUM({eqn}!{col}{eq_r['py']}:{eqn}!{col}{eq_r['ni1']})",
        "ncib": f"={eqn}!{col}{eq_r['c2']}",
    })
    put("BS", bs_r, bs)

    cf = {k: 0 for k, _, kind, *_ in CF_ROWS if kind == "i"}
    cf.update({
        "pbtc": f"={isn}!{col}{is_r['pbt']}",
        "da": f"={isn}!{col}{is_r['da']}",
        "assoc": f"=-{isn}!{col}{is_r['assoc']}",
        "intexp": f"={isn}!{col}{is_r['intexp']}",
        "intinc": f"={isn}!{col}{is_r['intinc']}",
        "dar": f"={bsn}!{prev}{bs_r['ar']}-{bsn}!{col}{bs_r['ar']}",
        "dinv": f"={bsn}!{prev}{bs_r['inv']}-{bsn}!{col}{bs_r['inv']}",
        "dap": f"={bsn}!{col}{bs_r['ap']}-{bsn}!{prev}{bs_r['ap']}",
        "taxpd": f"=-{isn}!{col}{is_r['tax']}",
        "capex": f"=-{a['cx']}",
        "intr": f"=-{isn}!{col}{is_r['intinc']}",
        "repay": f"={bsn}!{col}{bs_r['std']}+{bsn}!{col}{bs_r['ltd']}-{bsn}!{prev}{bs_r['std']}-{bsn}!{prev}{bs_r['ltd']}",
        "intp": f"=-({isn}!{col}{is_r['intexp']}-{a['l_int']})",
        "divp": f"=-({a['div']}+{a['divn']})",
        "leasep": f"=-({a['rou_d']}+{a['l_int']})",
        "buyb": f"=-{a['bb']}",
        "sedist": f"={eqn}!{col}{eq_r['se']}",
    })
    put("CF", cf_r, cf)

    eq = {k: 0 for k, _, kind, *_ in EQ_ROWS if kind == "i"}
    eq.update({
        "div1": f"=-{a['div']}",
        "bb": f"=-{a['bb']}",
        "ni1": f"={isn}!{col}{is_r['nictrl']}",
        "div2": f"=-{a['divn']}",
        "ni2": f"={isn}!{col}{is_r['nci']}",
        # NCI owners take out what they earn: NCI equity stays at its FY2025 level (team, 2026-10-23)
        "se": f"=-({col}{eq_r['ni2']}+{col}{eq_r['div2']})",
    })
    put("Equity", eq_r, eq)

    oci = {k: 0 for k, _, kind, *_ in OCI_ROWS if kind == "i"}
    oci.update({"ni": f"={isn}!{col}{is_r['ni']}", "cinci": f"={isn}!{col}{is_r['nci']}"})
    put("OCI", oci_r, oci)


def link_bs_cf_fcst(wb, is_r, bs_r, cf_r, eq_r, oci_r, rn, i, k):
    """FY2027E-FY2030E balance sheet, cash flow, equity and OCI: the FY2026E methods with each year's drivers.

    k maps the year's Assumptions keys: cx (capex), mat (maturity repaid), refi (new borrowing),
    matn (next year's maturity, current at year-end), div, divn, bb.
    """
    col, prev = FC[i], FC[i - 1]
    an, isn, bsn, cfn, eqn = sn("Assumptions"), sn("IS"), sn("BS"), sn("CF"), sn("Equity")
    a = {k: f"{an}!B{v}" for k, v in rn.items()}

    def put(sheet, rows, values):
        ws = wb[sn(sheet)]
        for key, r in rows.items():
            if key not in values:
                continue
            c = ws[f"{col}{r}"]
            c.value = values[key]
            c.font = BLUE if values[key] == 0 else BLACK
            c.fill = PatternFill(fill_type=None)

    bs = {k: f"={prev}{r}" for k, (r, kind) in
          {k: (bs_r[k], kind) for k, _, kind, *_ in BS_ROWS}.items() if kind == "i"}
    bs.update({
        "cash": f"={cfn}!{col}{cf_r['end']}",
        "ar": f"={isn}!{col}{is_r['sales']}*{a['d_ar']}/365",
        "inv": f"={isn}!{col}{is_r['cogs']}*{a['d_inv']}/365",
        "ap": f"={isn}!{col}{is_r['cogs']}*{a['d_ap']}/365",
        # PP&E depreciation = IS D&A less right-of-use depreciation and amortization, as in FY2026E
        "ppe": f"={prev}{bs_r['ppe']}+{a[k['cx']]}-({isn}!{col}{is_r['da']}-{a[k['rou']]}-{a['amort']})",
        # audit fix H-05: right-of-use assets and lease liabilities grow with net sales (new leases are non-cash)
        "rou": f"={prev}{bs_r['rou']}*{isn}!{col}{is_r['sales']}/{isn}!{prev}{is_r['sales']}",
        "leasec": f"={prev}{bs_r['leasec']}*{isn}!{col}{is_r['sales']}/{isn}!{prev}{is_r['sales']}",
        "leasenc": f"={prev}{bs_r['leasenc']}*{isn}!{col}{is_r['sales']}/{isn}!{prev}{is_r['sales']}",
        "intang": f"={prev}{bs_r['intang']}-{a['amort']}",
        "assoc": f"={prev}{bs_r['assoc']}+{isn}!{col}{is_r['assoc']}",
        # the year's maturity is repaid from the current portion; next year's maturity moves from long-term to current
        "std": f"={a[k['matn']]}",
        "ltd": f"={prev}{bs_r['std']}+{prev}{bs_r['ltd']}-{a[k['mat']]}+{a[k['refi']]}-{a[k['matn']]}",
        "re": f"={prev}{bs_r['re']}+SUM({eqn}!{col}{eq_r['py']}:{eqn}!{col}{eq_r['ni1']})",
        "ncib": f"={eqn}!{col}{eq_r['c2']}",
    })
    put("BS", bs_r, bs)

    cf = {k: 0 for k, _, kind, *_ in CF_ROWS if kind == "i"}
    cf.update({
        "pbtc": f"={isn}!{col}{is_r['pbt']}",
        "da": f"={isn}!{col}{is_r['da']}",
        "assoc": f"=-{isn}!{col}{is_r['assoc']}",
        "intexp": f"={isn}!{col}{is_r['intexp']}",
        "intinc": f"={isn}!{col}{is_r['intinc']}",
        "dar": f"={bsn}!{prev}{bs_r['ar']}-{bsn}!{col}{bs_r['ar']}",
        "dinv": f"={bsn}!{prev}{bs_r['inv']}-{bsn}!{col}{bs_r['inv']}",
        "dap": f"={bsn}!{col}{bs_r['ap']}-{bsn}!{prev}{bs_r['ap']}",
        "taxpd": f"=-{isn}!{col}{is_r['tax']}",
        "capex": f"=-{a[k['cx']]}",
        "intr": f"=-{isn}!{col}{is_r['intinc']}",
        "borr": f"={a[k['refi']]}",
        "repay": f"={bsn}!{col}{bs_r['std']}+{bsn}!{col}{bs_r['ltd']}-{bsn}!{prev}{bs_r['std']}-{bsn}!{prev}{bs_r['ltd']}-{a[k['refi']]}",
        "intp": f"=-({isn}!{col}{is_r['intexp']}-{a[k['li']]})",
        "divp": f"=-({a[k['div']]}+{a[k['divn']]})",
        # audit fix H-05: depreciation + interest, less the asset growth not matched by liability growth (closes Checks)
        "leasep": f"=-({a[k['rou']]}+{a[k['li']]})-({bsn}!{col}{bs_r['rou']}-{bsn}!{prev}{bs_r['rou']})"
                  f"+({bsn}!{col}{bs_r['leasec']}+{bsn}!{col}{bs_r['leasenc']}-{bsn}!{prev}{bs_r['leasec']}-{bsn}!{prev}{bs_r['leasenc']})",
        "buyb": f"=-{a[k['bb']]}",
        "sedist": f"={eqn}!{col}{eq_r['se']}",
    })
    put("CF", cf_r, cf)

    eq = {k: 0 for k, _, kind, *_ in EQ_ROWS if kind == "i"}
    eq.update({
        "div1": f"=-{a[k['div']]}",
        "bb": f"=-{a[k['bb']]}",
        "ni1": f"={isn}!{col}{is_r['nictrl']}",
        "div2": f"=-{a[k['divn']]}",
        "ni2": f"={isn}!{col}{is_r['nci']}",
        "se": f"=-({col}{eq_r['ni2']}+{col}{eq_r['div2']})",
    })
    put("Equity", eq_r, eq)

    oci = {k: 0 for k, _, kind, *_ in OCI_ROWS if kind == "i"}
    oci.update({"ni": f"={isn}!{col}{is_r['ni']}", "cinci": f"={isn}!{col}{is_r['nci']}"})
    put("OCI", oci_r, oci)


def build_methodology(wb, rn):
    """One row per forecast line: formula, driver (live link to Assumptions), why, source, advisor feedback."""
    i = 0 if LANG == "en" else 1
    an = sn("Assumptions")
    wa = wb[an]
    ws = wb.create_sheet(sn("Methodology"), 1)
    ws["A1"] = t("Grupo Bimbo - Forecast methodology: formula, driver and reason for every projected line")
    ws["A1"].font = TITLE
    ws["A2"] = t("Driver and value link live to sheet Assumptions. Green rows apply the advisor's feedback (Alan).")
    ws["A2"].font = NOTE
    for j, h in enumerate(methodology_rows.HEADERS, 1):
        c = ws.cell(4, j, h[i])
        c.font = HDR
        c.fill = FILL_HDR
    wrap = Alignment(wrap_text=True, vertical="top")
    for r, (blk, line, meth, key, why, src, alan) in enumerate(methodology_rows.ROWS, 5):
        for j, v in enumerate((blk[i], line[i], meth[i], None, None, why[i], src[i], alan[i]), 1):
            c = ws.cell(r, j, macro_es.names(v) if v and i else v)
            c.font = BOLD if j == 2 else BLACK
            c.alignment = wrap
            if alan[0]:
                c.fill = FILL_ALAN_H if j == 8 else FILL_ALAN
                if j == 8:
                    c.font = ALAN_FONT
        if key:
            ws.cell(r, 4, f"={an}!A{rn[key]}")
            ws.cell(r, 5, f"={an}!B{rn[key]}").number_format = wa[f"B{rn[key]}"].number_format
    for col, w in zip("ABCDEFGH", (16, 30, 62, 40, 12, 52, 30, 30)):
        ws.column_dimensions[col].width = w


def build_glossary(wb):
    """Abbreviations and terms used in the workbook, next to Methodology, to share with the team."""
    i = 0 if LANG == "en" else 1
    ws = wb.create_sheet(sn("Glossary"), 2)
    ws["A1"] = t("Grupo Bimbo - Glossary: abbreviations and terms used in this workbook")
    ws["A1"].font = TITLE
    ws["A2"] = t("Plain-words meaning of every abbreviation, and the sheets where it appears.")
    ws["A2"].font = NOTE
    for j, h in enumerate(glossary_rows.HEADERS, 1):
        c = ws.cell(4, j, h[i])
        c.font = HDR
        c.fill = FILL_HDR
    wrap = Alignment(wrap_text=True, vertical="top")
    for r, row in enumerate(glossary_rows.ROWS, 5):
        for j, v in enumerate(row, 1):
            c = ws.cell(r, j, v[i])
            c.font = BOLD if j == 2 else BLACK
            c.alignment = wrap
    for col, w in zip("ABCDE", (14, 28, 40, 80, 38)):
        ws.column_dimensions[col].width = w


def embed_macro(wb):
    """Copy every sheet of MACRO (values, live formulas, formats) so Assumptions links to it inside this workbook."""
    src = load_workbook(ROOT / MACRO)
    cached = load_workbook(ROOT / MACRO, data_only=True)
    for addr, exp in MCHECK.items():
        sh, cell = addr.split("!")
        val = cached[sh][cell].value
        assert isinstance(val, (int, float)) and abs(val - exp) < 5e-5, \
            ("macro link moved or MACRO not recalculated in Excel", addr, val, exp)
    for s in src.worksheets:
        d = wb.create_sheet(("Macro_Notes" if s.title == "Notes" else s.title) if LANG == "en" else macro_es.SHEETS[s.title])
        d.sheet_properties.tabColor = MACRO_TAB
        for row in s.iter_rows():
            for c in row:
                if c.value is None and not c.has_style:
                    continue
                v = c.value
                if LANG == "es" and isinstance(v, str):
                    v = macro_es.formula(v) if v.startswith("=") else macro_es.text(v)
                n = d.cell(c.row, c.column, v)
                if c.has_style:
                    n.font, n.fill, n.border = copy(c.font), copy(c.fill), copy(c.border)
                    n.alignment, n.number_format = copy(c.alignment), c.number_format
        for k, dim in s.column_dimensions.items():
            d.column_dimensions[k].width = dim.width
        for rng in s.merged_cells.ranges:
            d.merge_cells(str(rng))
        for cf in s.conditional_formatting:
            for rule in cf.rules:
                d.conditional_formatting.add(str(cf.sqref), rule)


def sheet_refs(formula):
    """Rename sheet references in a check formula to the build language."""
    for name in ("Segments", "Equity", "OCI", "IS", "BS", "CF"):
        formula = formula.replace(f"{name}!", f"{sn(name)}!")
    return formula


def main():
    wb = Workbook()
    readme = wb.active
    readme.title = sn("README")

    seg_ext = {"SEG": sn("Segments"), "seg_s_tot": SEG_ROWNUM["s_tot"],
               "seg_i_tot": SEG_ROWNUM["i_tot"], "seg_n_tot": SEG_ROWNUM["n_tot"]}
    _, is_r = build_sheet(wb, "IS", "Grupo Bimbo - Consolidated income statement",
                          "Continuing operations; FY2021 restated for Ricolino (discontinued from 2022). Costs by function, as reported.",
                          IS_ROWS, SRC["IS"], seg_ext)
    a_rn = build_assumptions(wb, is_r)
    link_is_2026(wb, is_r, a_rn)
    link_is_2028_2030(wb, is_r, a_rn)
    _, seg_r = build_sheet(wb, "Segments", "Grupo Bimbo - Net sales by region (history and forecast) and Adjusted EBITDA by region (history)",
                           "History: audited segment note. Forecast: net sales by region from Assumptions; Adjusted EBITDA by region "
                           "is not forecast (the forecast is consolidated below net sales).",
                           SEG_ROWS, SRC["SEG"], fcst_label="Forecast: net sales only (sheet Assumptions)")
    assert seg_r == SEG_ROWNUM
    link_segments(wb, seg_r, is_r, a_rn)
    validate_segments()
    _, oci_r = build_sheet(wb, "OCI", "Grupo Bimbo - Consolidated statement of other comprehensive income",
                           "As reported. Positive = gain.", OCI_ROWS, SRC["OCI"])
    _, bs_r = build_sheet(wb, "BS", "Grupo Bimbo - Consolidated balance sheet (31 December)",
                          "As reported, every line of the face of the statement.", BS_ROWS, SRC["BS"])
    _, cf_r = build_sheet(wb, "CF", "Grupo Bimbo - Consolidated cash flow statement",
                          "Indirect method, as reported. Sign as in the filing: negative = cash outflow. FY2021-22 include Ricolino until its sale.",
                          CF_ROWS, SRC["CF"])
    _, eq_r = build_sheet(wb, "Equity", "Grupo Bimbo - Equity roll-forward (statement of changes in equity)",
                          "Columns of the statement of changes in equity condensed to controlling and non-controlling totals.",
                          EQ_ROWS, SRC["EQ"])
    assert bs_r == BS_ROWNUM
    assert cf_r == CF_ROWNUM
    link_bs_cf_2026(wb, is_r, bs_r, cf_r, eq_r, oci_r, a_rn)
    for i, yy in enumerate((27, 28, 29, 30), 1):
        link_bs_cf_fcst(wb, is_r, bs_r, cf_r, eq_r, oci_r, a_rn, i,
                        {"cx": "cx%d" % yy, "mat": "mat%d" % yy, "refi": "refi%d" % yy, "matn": "mat%d" % (yy + 1),
                         "div": "div%d" % yy, "divn": "divn%d" % yy, "bb": "bb%d" % yy,
                         "rou": "rou%d" % yy, "li": "li%d" % yy})

    build_methodology(wb, a_rn)
    build_glossary(wb)
    audit_fix_es.build_fix_sheet(wb, a_rn, LANG, sn, t, TITLE, NOTE, HDR, FILL_HDR, BOLD, BLACK)

    # Checks sheet
    ck = wb.create_sheet(sn("Checks"))
    ck["A1"] = t("Integrity checks - every line must be 0 in every year")
    ck["A1"].font = TITLE
    ck["A2"] = t("Historical columns tie to the filing. In any year, a non-zero value points to a broken link.")
    ck["A2"].font = NOTE
    ck.cell(4, 1, t("Check (difference, MXN m)")).font = HDR
    ck.cell(4, 1).fill = FILL_HDR
    for j, y in enumerate(YEARS):
        c = ck.cell(4, 2 + j, yl(y))
        c.font = HDR
        c.fill = FILL_HDR
        c.alignment = Alignment(horizontal="center")
    checks = [
        ("BS: total assets - (liabilities + equity)", "=BS!{c}%d-BS!{c}%d" % (bs_r["ta"], bs_r["tle"])),
        ("CF ending cash - BS cash", "=CF!{c}%d-BS!{c}%d" % (cf_r["end"], bs_r["cash"])),
        ("CF income before taxes (continuing) - IS", "=CF!{c}%d-IS!{c}%d" % (cf_r["pbtc"], is_r["pbt"])),
        ("OCI net income - IS consolidated net income", "=OCI!{c}%d-IS!{c}%d" % (oci_r["ni"], is_r["ni"])),
        ("Equity: controlling net income - IS", "=Equity!{c}%d-IS!{c}%d" % (eq_r["ni1"], is_r["nictrl"])),
        ("Equity: NCI net income - IS", "=Equity!{c}%d-IS!{c}%d" % (eq_r["ni2"], is_r["nci"])),
        ("Equity: OCI (controlling + NCI) - OCI statement", "=Equity!{c}%d+Equity!{c}%d-OCI!{c}%d" % (eq_r["oci1"], eq_r["oci2"], oci_r["oci"])),
        ("Equity: OCI to NCI - OCI statement", "=Equity!{c}%d-(OCI!{c}%d-IS!{c}%d)" % (eq_r["oci2"], oci_r["cinci"], is_r["nci"])),
        ("Equity: closing controlling - BS", "=Equity!{c}%d-BS!{c}%d" % (eq_r["c1"], bs_r["ctrl"])),
        ("Equity: closing NCI - BS", "=Equity!{c}%d-BS!{c}%d" % (eq_r["c2"], bs_r["ncib"])),
        ("Equity: share repurchases - CF", "=Equity!{c}%d-CF!{c}%d" % (eq_r["bb"], cf_r["buyb"])),
    ]
    tie_outs = [
        ("IS net sales vs filing", is_r["sales"], [338792, 398706, 399879, 408335, 426952]),
        ("IS gross profit vs filing", is_r["gp"], [181089, 205381, 205510, 214928, 223487]),
        ("IS operating income vs filing", is_r["ebit"], [32580, 53696, 35455, 33149, 34146]),
        ("IS income before taxes vs filing", is_r["pbt"], [24854, 45878, 25324, 21034, 20143]),
        ("IS consolidated net income vs filing", is_r["ni"], [17382, 48485, 16922, 14043, 12946]),
        ("IS controlling net income vs filing", is_r["nictrl"], [15916, 46910, 15477, 12544, 11133]),
    ]
    tie_bs = [
        ("BS total current assets vs filing", "tca", [53411, 63470, 58914, 67180, 64671]),
        ("BS total assets vs filing", "ta", [337640, 347764, 348102, 416804, 409805]),
        ("BS total current liabilities vs filing", "tcl", [80760, 89734, 87192, 85155, 90573]),
        ("BS total liabilities vs filing", "tl", [236034, 220162, 236474, 289106, 289550]),
        ("BS total equity vs filing", "te", [101606, 127602, 111628, 127698, 120255]),
    ]
    tie_cf = [
        ("CF operating vs filing", "cfo", [45776, 38851, 31411, 39907, 47753]),
        ("CF investing vs filing", "cfi", [-32459, -9122, -42440, -36138, -34652]),
        ("CF financing vs filing", "cff", [-14116, -25692, 5904, -2696, -11908]),
        ("OCI total vs filing", "oci", [4441, -10705, -14790, 13814, -11045]),
    ]
    r = 5
    ck.cell(r, 1, t("Links between statements (all years)")).font = BOLD
    r += 1
    first_check = r
    for label, f in checks:
        ck.cell(r, 1, t(label)).font = BLACK
        for j, col in enumerate(COLS):
            c = ck[f"{col}{r}"]
            c.value = sheet_refs(f.format(c=col))
            c.number_format = NUM
        r += 1
    r += 1
    ck.cell(r, 1, t("Subtotals vs the audited filing (history only)")).font = BOLD
    r += 1
    rows_hist = [(l, "IS", row, v) for l, row, v in tie_outs]
    rows_hist += [(l, "BS", bs_r[k], v) for l, k, v in tie_bs]
    rows_hist += [(l, "CF", cf_r[k], v) for l, k, v in tie_cf[:3]]
    rows_hist += [(tie_cf[3][0], "OCI", oci_r["oci"], tie_cf[3][2])]

    for label, sh, row, vals in rows_hist:
        ck.cell(r, 1, t(label)).font = BLACK
        for j, col in enumerate(HC):
            c = ck[f"{col}{r}"]
            ref = vals[j] if isinstance(vals, list) else sheet_refs(vals.format(col=col))
            c.value = f"={sn(sh)}!{col}{row}-{ref}"
            c.number_format = NUM
        r += 1
    last_check = r - 1
    r += 1
    ck.cell(r, 1, t("Sum of absolute differences")).font = BOLD
    for col in COLS:
        c = ck[f"{col}{r}"]
        c.value = f"=SUMPRODUCT(ABS({col}{first_check}:{col}{last_check}))"
        c.number_format = NUM
        c.font = BOLD
    r += 1
    ck.cell(r, 1, t("Status")).font = BOLD
    for col in COLS:
        c = ck[f"{col}{r}"]
        c.value = f'=IF(ROUND({col}{r-1},0)=0,"OK","{t('CHECK')}")'
        c.font = BOLD
        c.alignment = Alignment(horizontal="center")
    ck.column_dimensions["A"].width = 52
    for col in COLS:
        ck.column_dimensions[col].width = 11

    # README
    lines = [
        ("Grupo Bimbo (BIMBOA) - Consolidated financial statements FY2021A-FY2030E", TITLE),
        ("MXN millions. AUDIT-FIX COPY built by analisis-dcf-2026-10-26/build/build_statements_workbook_auditfix.py; the macro sheets are copied from "
         "analisis-dcf-2026-10-26/datos/nominal_gdp_growth_2016-2030_auditfix.xlsx (built by analisis-dcf-2026-10-26/build/build_macro_gdp_auditfix.py).", NOTE),
        ("Audit fixes H-01 to H-05 applied (sheet Audit_fixes). The team's original workbook is BIMBOA_statements_2021-2030_v1.xlsx; "
         "the Methodology sheet still describes the original methods where Audit_fixes says otherwise.", BOLD),
        ("", None),
        ("Sheets", BOLD),
        ("Methodology: one row per forecast line - formula, driver (live link), why, source and whether it applies the advisor's feedback.", None),
        ("IS, OCI, BS, CF and Equity: every line of the face of the audited statements. FY2021A-FY2025A as reported; "
         "FY2026E-FY2030E linked to Assumptions.", None),
        ("Assumptions: every forecast driver, one value per row with its tag and source. First block: 2026 actual by quarter.", None),
        ("Segments: net sales by region (history and forecast); Adjusted EBITDA by region (history only).", None),
        ("Checks: links between the statements in every year and tie-outs to the filing in history. Every line must be 0.", None),
        ("Glossary: every abbreviation and term (PPP, g, perpetuity, ex-FX, RONIC...) in plain words, with the sheets where it appears.", None),
        ("Macro sheets (gold tabs): Capital IQ GDP, CPI and FX with live formulas - Macro_Notes, Data, Growth_view, "
         "IAS29_test, FX, Regional_agg, Ratio_history, Ratio_NA, Evidence_MEX, Ratios_9M26, Organic_pass, Cross_check_history, "
         "Regional_FX, PPP_terminal. Assumptions links to them directly.", None),
        ("", None),
        ("Advisor feedback (Alan)", BOLD),
        ("No historical CAGR; growth = team ratio x economy (nominal GDP); organic only; no non-recurring items; growth in local "
         "currency, consolidated in pesos, with business growth and FX effect shown separately.", None),
        ("Where it applies: green sections in Assumptions (dark green header, light green rows) and green rows in Methodology.", None),
        ("", None),
        ("Sources (PDF page numbers)", BOLD),
        ("FY2023-FY2025: filings/annual/IA25_GB_EEFF_V10.pdf - BS p.12, IS p.13, OCI p.14, equity p.15, CF p.16.", None),
        ("FY2021-FY2022: filings/bmv/Reporte Anual 2023_XBRL_VF.PDF - BS p.256, IS p.257, OCI p.258, equity p.259, CF p.260.", None),
        ("Rule: the latest report that presents a year wins (data/adjustments.md). FY2021 is restated for the Ricolino disposal.", None),
        ("", None),
        ("Colour code", BOLD),
        ("Blue number = typed from a filing or source [sourced]. Black = formula [calc]. Yellow = team assumption typed as a value. "
         "Green = applies the advisor's feedback.", None),
        ("", None),
        ("Notes", BOLD),
        ("Signs follow each filing: IS expenses positive; interest income negative inside the financing result; CF outflows negative.", None),
        ("Lease interest is paid inside the CF line 'Lease payments' (data/adjustments.md, adjustment 6).", None),
        ("The condensed model inputs (data/financials.csv) group these lines; totals agree with this workbook.", None),
    ]
    for i, (txt, f) in enumerate(lines, start=1):
        c = readme.cell(i, 1, t(txt))
        if f:
            c.font = f
    readme.column_dimensions["A"].width = 130
    embed_macro(wb)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
