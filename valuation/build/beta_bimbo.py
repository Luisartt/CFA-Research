"""Grupo Bimbo beta against the S&P/BMV IPC from month-end closes.

  python -I valuation/build/beta_bimbo.py --project .
Reads data/market/bimbo_ipc_monthly_2021-11_2026-10.csv (sources and checks in data/market/README.md) and writes
valuation/inputs/beta_regression.json, which the WACC workbook shows as evidence for the beta choice.

Method: OLS of monthly returns (BIMBO A on IPC) over 60, 36 and 24 months, on price and on dividend-adjusted
(total return) closes; Blume adjustment 0.67 x beta + 0.33; Hamada unlevering at Bimbo's market D/E incl. leases
(0.7431) and the 30% statutory rate, the same convention as the rest of the WACC build.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics as st
from pathlib import Path

DE, TAX = 0.7431, 0.30


def returns(x: list[float]) -> list[float]:
    return [x[i] / x[i - 1] - 1 for i in range(1, len(x))]


def ols(y: list[float], x: list[float]) -> dict:
    n = len(y)
    mx, my = st.fmean(x), st.fmean(y)
    sxx = sum((a - mx) ** 2 for a in x)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    beta = sxy / sxx
    alpha = my - beta * mx
    sse = sum((b - (alpha + beta * a)) ** 2 for a, b in zip(x, y))
    sst = sum((b - my) ** 2 for b in y)
    se = math.sqrt(sse / (n - 2) / sxx)
    return {"n": n, "beta": beta, "r2": 1 - sse / sst, "se": se, "ci95_low": beta - 2.0 * se, "ci95_high": beta + 2.0 * se,
            "blume": 0.67 * beta + 0.33, "unlevered": beta / (1 + (1 - TAX) * DE),
            "blume_unlevered": (0.67 * beta + 0.33) / (1 + (1 - TAX) * DE)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", default=".")
    a = ap.parse_args()
    project = Path(a.project).resolve()
    src = project / "data" / "market" / "bimbo_ipc_monthly_2021-11_2026-10.csv"
    rows = list(csv.DictReader(src.open(encoding="utf-8")))
    px = [float(r["bimbo_close_mxn"]) for r in rows]
    adj = [float(r["bimbo_adjclose_mxn"]) for r in rows]
    ipc = [float(r["ipc_close"]) for r in rows]
    check = [(float(r["bimbo_close_mxn"]), float(r["ciq_close_mxn_check"])) for r in rows if r["ciq_close_mxn_check"]]
    max_diff = max(abs(p - c) for p, c in check)
    rx = returns(ipc)
    out = {"source": "data/market/bimbo_ipc_monthly_2021-11_2026-10.csv (Yahoo Finance BIMBOA.MX and ^MXX month-ends; "
                     "checked against Capital IQ, data/market/README.md)",
           "window_end": rows[-1]["month_end"], "de": DE, "tax": TAX,
           "ciq_check": {"months_compared": len(check), "max_abs_diff_mxn": max_diff}, "cases": {}}
    for name, series in (("price", px), ("total_return", adj)):
        ry = returns(series)
        for months in (60, 36, 24):
            k = max(0, len(ry) - months)
            out["cases"][f"{name}_{months}m"] = ols(ry[k:], rx[k:])
    base = out["cases"]["total_return_60m"]
    out["selected_evidence"] = {
        "case": "total_return_60m", "levered": base["beta"], "unlevered": base["unlevered"],
        "blume_unlevered": base["blume_unlevered"],
        "note": ("5-year monthly total-return regression on the IPC; 59 monthly returns (the 60 month-ends give 59 returns). "
                 "It corroborates the Damodaran global food-processing unlevered beta of 0.53; the 36- and 24-month windows "
                 "are higher (the 2023-24 de-rating) and less precise.")}
    dst = project / "valuation" / "inputs" / "beta_regression.json"
    dst.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"wrote {dst.relative_to(project)}; CIQ check max diff {max_diff:.2f} MXN over {len(check)} months")
    for k, v in out["cases"].items():
        print(f"  {k:18s} n={v['n']:2d} beta {v['beta']:.4f} R2 {v['r2']:.3f} se {v['se']:.3f} "
              f"Blume {v['blume']:.4f} unlevered {v['unlevered']:.4f} (Blume {v['blume_unlevered']:.4f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
