"""Build analisis-dcf-2026-10-26/puente/BIMBOA_bridge_3Q26_v1.xlsx: EV-to-equity claims at the latest balance (team, 2026-10-26).

Every line is at 30-Sep-2026. Debt, cash, leases and NCI book come from the 3T26 earnings release (condensed balance
sheet p.8). The debt-like items (employee benefits, provisions, derivatives, MEPP, deferred compensation), associates,
9M26 NCI income and shares come from the BMV 3Q26 XBRL report, with the same policy as Dec-25 and Jun-26
(valuation/inputs/spg_inputs.yaml dated_bridge). NCI is valued at market with 0% growth on the 9M26 run-rate (team,
2026-10-26).
Every typed value is [sourced] or a team [assumption]; every result is a live formula. The DCF is not run here.

Run from the worktree root:  python analisis-dcf-2026-10-26/build/build_bridge_3q26.py
then recalculate:            powershell -File valuation/build/recalc_excel.ps1 <Windows path of the workbook>
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "analisis-dcf-2026-10-26" / "puente" / "BIMBOA_bridge_3Q26_v1.xlsx"

TITLE = Font(name="Arial", size=12, bold=True)
BOLD = Font(name="Arial", size=9, bold=True)
BLACK = Font(name="Arial", size=9)
BLUE = Font(name="Arial", size=9, color="0000FF")
NOTE = Font(name="Arial", size=8, italic=True, color="595959")
HDR = Font(name="Arial", size=9, bold=True, color="FFFFFF")
FILL_HDR = PatternFill("solid", fgColor="1F4E78")
FILL_KEY = PatternFill("solid", fgColor="FFF2CC")
REL = "3T26 earnings release, filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%203T26.pdf"
XBRL = "BMV 3Q26 XBRL, analisis-dcf-2026-10-26/datos/bmv_3t26/Reporte_Definitivo_BMV_XBRL_Espanol_Sep_26.pdf"
XJUN = "BMV 2Q26 XBRL, filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Jun_26.pdf"
EEFF = "EEFF25 p.79-80 note 19 (" + "valuation/inputs/spg_inputs.yaml" + " cross_checks)"
DB = "valuation/inputs/spg_inputs.yaml dated_bridge"

# key, label, value or formula, tag, source, number format ("n", "p", "r"), highlight
ROWS = [
    ("h1", "1. Debt, leases, cash and NCI book at 30-Sep-2026 (MXN millions)", None, "", "", "", False),
    ("std", "Short-term debt", 13636, "[sourced]", REL + " p.8", "n", False),
    ("ltd", "Long-term debt", 139166, "[sourced]", REL + " p.8", "n", False),
    ("lsc", "Lease liabilities, short term", 7173, "[sourced]", REL + " p.8", "n", False),
    ("lsl", "Lease liabilities, long term", 26867, "[sourced]", REL + " p.8", "n", False),
    ("cash", "Cash and cash equivalents", 17459, "[sourced]", REL + " p.8", "n", False),
    ("ncib", "Non-controlling interest, book", 610, "[sourced]", REL + " p.8", "n", False),
    ("nd_rep", "Net debt reported by Bimbo (excludes leases), reference", 135343, "[sourced]", REL + " p.6", "n", False),
    ("debt", "Financial debt", "=B{std}+B{ltd}", "[calc]", "", "n", False),
    ("leases", "Lease liabilities (IFRS 16)", "=B{lsc}+B{lsl}", "[calc]", "In net debt because the FCFF deducts new leases", "n", False),
    ("nd", "Net debt including leases", "=B{debt}+B{leases}-B{cash}", "[calc]", "", "n", True),
    ("nd_chk", "Check: financial debt - cash - reported net debt (must be 0)", "=B{debt}-B{cash}-B{nd_rep}", "[calc]", "", "n", False),
    ("b1", "", None, "", "", "", False),
    ("h2", "2. Non-controlling interest at market value, 0% growth (team 2026-10-26)", None, "", "", "", False),
    ("n9m", "NCI net income 9M26", 1365.514, "[sourced]", XBRL + " [310000] p.13", "n", False),
    ("nq1", "NCI net income 1Q26, cross-check", 436, "[sourced]", "S&P Capital IQ quarterly; " + DB + " nci_claim", "n", False),
    ("nq2", "NCI net income 2Q26, cross-check", 471, "[sourced]", "S&P Capital IQ quarterly; " + DB + " nci_claim", "n", False),
    ("nq3", "NCI net income 3Q26, cross-check", 458, "[sourced]", REL + " p.8", "n", False),
    ("n_chk", "Check: 9M26 less the sum of the quarters (about 0, rounding)", "=B{n9m}-B{nq1}-B{nq2}-B{nq3}", "[calc]", "", "n", False),
    ("ninc", "NCI net income, annual run-rate = 9M26 x 4 / 3", "=B{n9m}*4/3", "[calc]",
     "Team 2026-10-26: 9M26 annualized (replaces 1H26 x 2 = 1,814)", "n", False),
    ("ke", "Cost of equity (v3 route B, reference)", 0.1294365113, "[calc]", "valuation/valuation-outputs.yaml cost_of_equity; team confirms the WACC", "p", False),
    ("gn", "NCI growth in perpetuity", 0.0, "[assumption]", "Team 2026-10-26: 0%, the NCI book base shrinks (3,306 Dec-23 to 743 Dec-25, EEFF25 p.12)", "p", False),
    ("ncim", "NCI claim at market value = income / (ke - g)", "=B{ninc}/(B{ke}-B{gn})", "[calc]", "", "n", True),
    ("nciu", "  of which uplift over book", "=B{ncim}-B{ncib}", "[calc]", "", "n", False),
    ("b2", "", None, "", "", "", False),
    ("h3", "3. Debt-like items, after tax, at 30-Sep-2026", None, "", "", "", False),
    ("eb", "Employee benefits liability, long term, 30-Sep-2026", 5697.178, "[sourced]", XBRL + " [210000] p.12", "n", False),
    ("eb_d25", "Dec-25 after-tax retirement + US welfare + LT bonuses", "=1515.25+2454.0+520.1", "[calc]",
     "valuation/inputs/spg_inputs.yaml bridge_items (EEFF25 notes 18-19)", "n", False),
    ("eb_bs25", "Employee benefits liability, Dec-25", 6507, "[sourced]", "EEFF25 p.12", "n", False),
    ("eb_at", "Employee benefits after tax = Sep-26 line x Dec-25 after-tax ratio", "=B{eb}*B{eb_d25}/B{eb_bs25}", "[calc]",
     "Same policy as Dec-25; the Sep-26 split by plan is not disclosed [assumption]", "n", False),
    ("utp", "Uncertain tax positions", 8296.701, "[sourced]", XBRL + " p.57; no tax shield", "n", False),
    ("ptax", "Tax provisions", 1367.570, "[sourced]", XBRL + " p.57; no tax shield", "n", False),
    ("plab", "Labour provisions", 514.830, "[sourced]", XBRL + " p.57", "n", False),
    ("pciv", "Civil provisions", 460.724, "[sourced]", XBRL + " p.58", "n", False),
    ("poth", "Other provisions", 0.378, "[sourced]", XBRL + " p.58", "n", False),
    ("ptot", "Total provisions reported", 10640.203, "[sourced]", XBRL + " p.58", "n", False),
    ("p_chk", "Check: sum of provisions less reported total (must be about 0)", "=B{utp}+B{ptax}+B{plab}+B{pciv}+B{poth}-B{ptot}", "[calc]", "", "n", False),
    ("tx", "Tax rate on deductible provisions and benefits (Mexico)", 0.30, "[assumption]", "Same as Dec-25 policy", "p", False),
    ("prov", "Provisions after tax", "=B{utp}+B{ptax}+(B{plab}+B{pciv})*(1-B{tx})+B{poth}", "[calc]", "", "n", False),
    ("dl1", "Derivative liabilities, current", 676.075, "[sourced]", XBRL + " p.63", "n", False),
    ("dl2", "Derivative liabilities, non-current", 2517.928, "[sourced]", XBRL + " p.64", "n", False),
    ("da1", "Derivative assets, current", 1753.547, "[sourced]", XBRL + " p.63", "n", False),
    ("da2", "Derivative assets, non-current", 954.916, "[sourced]", XBRL + " p.63", "n", False),
    ("der", "Net derivative liabilities", "=B{dl1}+B{dl2}-B{da1}-B{da2}", "[calc]",
     "Mostly cross-currency swaps on the USD debt. Margin-account deposits (asset 431.3) and withdrawals (liability 248.8, p.63) "
     "are left out, as the deposits were at Dec-25 and Jun-26", "n", False),
    ("olp", "Other long-term provisions line (provisions + MEPP + deferred compensation + other)", 12529.216, "[sourced]",
     XBRL + " [210000] p.12", "n", False),
    ("resid", "Residual beyond provisions", "=B{olp}-B{ptot}", "[calc]", "", "n", False),
    ("m25", "MEPP exit liabilities, Dec-25", 985, "[sourced]", EEFF, "n", False),
    ("c25", "Deferred compensation, Dec-25", 1060, "[sourced]", EEFF, "n", False),
    ("o25", "Other long-term liabilities in the residual, Dec-25", 270, "[sourced]", EEFF, "n", False),
    ("mepp", "MEPP exit liabilities, Sep-26 = residual x Dec-25 share", "=B{resid}*B{m25}/(B{m25}+B{c25}+B{o25})", "[calc]",
     "Not disclosed separately at Sep-26; split in the Dec-25 proportions [assumption], as at Jun-26", "n", False),
    ("dcomp", "Deferred compensation, Sep-26 = residual x Dec-25 share", "=B{resid}*B{c25}/(B{m25}+B{c25}+B{o25})", "[calc]",
     "Same split", "n", False),
    ("txus", "US tax rate on MEPP", 0.25, "[assumption]", "Same as Dec-25 policy", "p", False),
    ("other_dl", "MEPP and deferred compensation after tax", "=B{mepp}*(1-B{txus})+B{dcomp}*(1-B{tx})", "[calc]", "", "n", False),
    ("dl", "Debt-like items excluding NCI", "=B{eb_at}+B{prov}+B{der}+B{other_dl}", "[calc]", "", "n", True),
    ("dl_jun", "Debt-like items excluding NCI at 30-Jun-2026, reference", 18135.18, "[calc]",
     "Previous bridge, same policy (" + XJUN + "); " + DB + " debt_like_jun_ex_nci", "n", False),
    ("dl_chg", "Change from Jun-26", "=B{dl}-B{dl_jun}", "[calc]", "", "n", False),
    ("b3", "", None, "", "", "", False),
    ("h4", "4. Non-operating assets and shares at 30-Sep-2026", None, "", "", "", False),
    ("assoc", "Investments in associates (added to EV)", 6532.927, "[sourced]", XBRL + " [210000] p.11; 6,497.5 at Jun-26", "n", False),
    ("sh_is", "Issued shares (millions)", 4304.744119, "[sourced]", XBRL + " [700000] p.24 'acciones en circulación'", "n", False),
    ("sh_tr", "Repurchased shares held (millions)", 20.184108, "[sourced]", XBRL + " [700000] p.24 'acciones recompradas'", "n", False),
    ("sh", "Shares outstanding, net of repurchased (millions)", "=B{sh_is}-B{sh_tr}", "[calc]",
     "Same method at Jun-26 gives 4,296.284215, equal to the CIQ count; WACC uses 4,294.943715 (29-Jul-2026, wacc_inputs.yaml A8)", "n", False),
    ("b4", "", None, "", "", "", False),
    ("h5", "5. Claims to deduct from enterprise value (the DCF is not run here)", None, "", "", "", False),
    ("claims", "Net debt incl. leases + NCI at market + debt-like - associates", "=B{nd}+B{ncim}+B{dl}-B{assoc}", "[calc]",
     "Equity value = DCF enterprise value - this line", "n", True),
    ("claims_ps", "Per share", "=B{claims}/B{sh}", "[calc]", "MXN per share, before rolling to 16-Oct-2026", "r", True),
    ("dlps", "Debt-like items + NCI uplift per share (the v3 'Ps 8.60' measure)", "=(B{dl}+B{nciu})/B{sh}", "[calc]",
     "v3: 37,054 / 4,310.5 = 8.60 at Dec-25 with NCI at 3% growth", "r", True),
]


def main():
    wb = Workbook()
    rd = wb.active
    rd.title = "README"
    for i, (txt, f) in enumerate([
        ("Grupo Bimbo - equity bridge at the latest balance (30-Sep-2026), team decisions 2026-10-26", TITLE),
        ("Built by analisis-dcf-2026-10-26/build/build_bridge_3q26.py. Blue = typed from a source; black = live formula; yellow = key lines.", NOTE),
        ("Date: every line at 30-Sep-2026. Debt, leases, cash, NCI book from the 3T26 release p.8; debt-like items, associates, "
         "9M26 NCI income and shares from the BMV 3Q26 XBRL report.", None),
        ("NCI at market with 0% growth (team). The DCF is not run here: the claims line is what the DCF enterprise value must cover.", None),
    ], 1):
        c = rd.cell(i, 1, txt)
        if f:
            c.font = f
    rd.column_dimensions["A"].width = 140

    ws = wb.create_sheet("Bridge")
    ws["A1"] = "Equity bridge claims, MXN millions"
    ws["A1"].font = TITLE
    for j, (h, w) in enumerate((("Line", 72), ("Value", 13), ("Tag", 11), ("Source / note", 110)), 1):
        c = ws.cell(3, j, h)
        c.font, c.fill = HDR, FILL_HDR
        ws.column_dimensions[chr(64 + j)].width = w
    rn = {k: 4 + i for i, (k, *_) in enumerate(ROWS)}
    fmt = {"n": "#,##0.0;(#,##0.0)", "p": "0.00%", "r": "0.00"}
    for k, lab, v, tag, src, nf, key in ROWS:
        r = rn[k]
        ws.cell(r, 1, lab).font = BOLD if k.startswith("h") else BLACK
        if v is not None:
            c = ws.cell(r, 2, v.format(**rn) if isinstance(v, str) else v)
            c.font = BLACK if isinstance(v, str) else BLUE
            c.number_format = fmt[nf]
            if key:
                c.fill = FILL_KEY
        ws.cell(r, 3, tag).font = NOTE
        ws.cell(r, 4, src).font = NOTE
        ws.cell(r, 4).alignment = Alignment(wrap_text=False)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
