"""Consistency checks for the report draft: numbers quoted in the sections against the model data, forbidden tags,
figure keys and images, and the page count of the built PDF.

Usage: python check_report.py            (from report/build)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import report_data as D
from report_style import CHARTS, REPORT

SECTIONS = REPORT / "sections"
text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(SECTIONS.glob("*.md")))
L, R = D.LEV, D.RUN
ok = True


def need(label: str, s: str):
    global ok
    present = s in text
    if not present:
        ok = False
    print(f"  {'ok ' if present else 'MISSING'} {label:42s} {s}")


def f2(x):
    return f"{abs(x):.2f}"


print("Quoted values that must appear in the sections")
checks = {
    "price": f"{D.PRICE:.2f}", "DCF exit (today)": f"{R['ps_exit']:.2f}", "12-month value": f"{R['target12m_exit']:.2f}",
    "Gordon RONIC": f2(R["ps_gordon_ronic"]), "Gordon no link": f2(R["ps_gordon_naive"]), "WACC": f"{R['wacc'] * 100:.2f}%",
    "cost of equity": f"{R['ke'] * 100:.2f}%", "levered beta": f"{R['beta_l']:.3f}", "exit multiple": f"{D.STATE['exit_mult']:.2f}x",
    "reverse multiple": f"{L['reverse_multiple']:.2f}x", "HOLD low": f"{L['bands']['clean_low']['multiple']:.2f}x",
    "HOLD high": f"{L['bands']['clean_high']['multiple']:.2f}x", "BUY edge": f"{L['bands']['buy_edge']['multiple']:.2f}x",
    "CRP": f"{D.STATE['crp'] * 100:.2f}%", "rf": f"{D.STATE['rf'] * 100:.2f}%",
    "NA gap to Flowers": f2(L["levers"]["na_margin_gap_flowers_p150"]["exit"]), "NA +100 bp": f2(L["levers"]["na_margin_p100"]["exit"]),
    "wheat -50 bp from 2027": f2(L["levers"]["margin_m50_from27"]["exit"]), "wheat -100 bp from 2027": f2(L["levers"]["margin_m100_from27"]["exit"]),
    "one-year -100 bp": f2(L["levers"]["margin_m100_2027_only"]["exit"]), "NA growth -1 pp": f2(L["levers"]["na_growth_m1pp"]["exit"]),
    "Mexico growth -2 pp": f2(L["levers"]["mx_growth_m2pp"]["exit"]), "both growth": f2(L["levers"]["growth_both"]["exit"]),
    "all three": f2(L["scenario_all_three"]["exit"]), "value all three": f"{R['ps_exit'] + L['scenario_all_three']['exit']:.2f}",
    "Mexico margin -100 bp": f2(L["levers"]["mx_margin_m100"]["exit"]), "Mexico margin -150 bp": f2(L["levers"]["mx_margin_m150"]["exit"]),
    "core multiple value": f"{L['case_core_multiple_only']['value']:.2f}", "downside (ops)": f"{L['case_bear_base_multiple']['value']:.2f}",
    "downside (ops + core multiple)": f"{L['case_bear_core']['value']:.2f}", "upside case": f"{L['case_bull_hold_high']['value']:.2f}",
    "tornado: multiple 0.5x": f2(L["tornado"][0]["down"]), "tornado: margin 50 bp": f2(L["tornado"][1]["down"]),
    "tornado: capex": f2(L["tornado"][2]["down"]), "tornado: growth": f2(L["tornado"][3]["down"]), "tornado: WACC": f2(L["tornado"][4]["down"]),
    "terminal value PV (bn)": f"{R['pv_tv_exit'] / 1000:.1f}", "EV (bn)": f"{R['ev_exit'] / 1000:.1f}",
    "expected return": f"{R['exp_return_exit'] * 100:.1f}%".replace("-", ""),
}
for k, v in checks.items():
    need(k, v)

print("\nForbidden tags and leftovers")
bad = [t for t in ("[unverified]", "[assumption]", "[sourced]", "[calc]", "[guidance]", "TODO", "XXX") if t in text]
for t in bad:
    ok = False
    print("  FOUND", t)
if not bad:
    print("  none")
keys = set(re.findall(r"\{fig:([a-z_]+)\}", text)) | {k.strip() for m in re.findall(r"\[\[figs:\s*(.+?)\]\]", text) for k in m.split(",")}
import build_report_pdf as B  # noqa: E402

missing = [k for k in keys if k not in B.FIGS or not (CHARTS / f"{B.FIGS[k][0]}.png").exists()]
print("\nFigure keys without definition or image:", missing or "none")
ok = ok and not missing
unused = [k for k in B.FIGS if k not in keys]
print("Figures defined but not used in any section:", unused or "none")

pdf = REPORT / "BIMBOA_report_v1_draft.pdf"
if pdf.exists():
    import pymupdf

    n = pymupdf.open(pdf).page_count
    print(f"\nPDF pages: {n} (cover 1 + body + appendix); body limit 10, appendix limit 10")
print("\nRESULT:", "OK" if ok else "FIX THE ITEMS ABOVE")
sys.exit(0 if ok else 1)
