"""Every sensitivity quoted in the report, computed on the consolidated DCF (replica in valuation/build/consolidate_models.py).

Writes report/data/levers.json. Run after valuation/inputs/consolidated_results.json changes.
Timing rule for thesis levers: they start in FY2027E (FY2026E is mostly reported: 1H26 actual).
Segment mapping: a segment shock moves consolidated revenue by that segment's share of consolidated revenue in the
three-statement model (report/data/statements_v7.json, 'Schedules'); a segment margin shock moves the consolidated
EBITDA margin by the same share. Both are [calc] approximations, stated in the report.
"""

from __future__ import annotations

import copy
import json
import sys

from report_style import DATA, ROOT

sys.path.insert(0, str(ROOT / "valuation" / "build"))
import consolidate_models as cm  # noqa: E402

CONS = json.loads((ROOT / "valuation" / "inputs" / "consolidated_results.json").read_text(encoding="utf-8"))
ST = json.loads((DATA / "statements_v7.json").read_text(encoding="utf-8"))

PRICE = cm.PRICE
DPS = cm.DPS_NEXT


def base_state() -> cm.State:
    return cm.State(**CONS["consolidated"]["state"])


def segment_paths() -> dict:
    """Engine segment revenue FY2026-FY2030 and growth, from the three-statement model."""
    yrs = ST["years"]
    idx = [yrs.index(y) for y in (2025, 2026, 2027, 2028, 2029, 2030)]
    sch = ST["sheets"]["Schedules"]
    out = {}
    for key, lab in (("na", "North America"), ("mx", "Mexico")):
        vals = [sch[lab][i] for i in idx]
        out[key] = {"rev": vals[1:], "g": [vals[k + 1] / vals[k] - 1 for k in range(5)]}
    total = [ST["sheets"]["IS"]["Revenue"][i] for i in idx]
    out["total"] = total[1:]
    return out


SEG = segment_paths()


def ps(s: cm.State, **kw) -> dict:
    return cm.run(s, **kw)


def growth_from_rev(rev0: float, rev: list) -> list:
    out, prev = [], rev0
    for r in rev:
        out.append(r / prev - 1)
        prev = r
    return out


def shock_growth(base: cm.State, seg: str, d_g: float, start: int = 1) -> cm.State:
    """Lower one segment's growth by d_g (decimal) from forecast index `start` (1 = FY2027E)."""
    b = ps(base)
    rev = list(b["rev"])
    seg_g = SEG[seg]["g"]
    share = [SEG[seg]["rev"][k] / SEG["total"][k] for k in range(5)]
    factor, f = [], 1.0
    for k in range(5):
        if k >= start:
            f *= (1 + seg_g[k] + d_g) / (1 + seg_g[k])
        factor.append(f - 1.0)
    new_rev = [rev[k] * (1 + share[k] * factor[k]) for k in range(5)]
    s = copy.deepcopy(base)
    s.growth = growth_from_rev(base.rev0, new_rev)
    return s


def shock_margin(base: cm.State, d_m: float, weight: list | None = None, start: int = 1, only: int | None = None) -> cm.State:
    s = copy.deepcopy(base)
    m = []
    for k, x in enumerate(base.ebitda_m):
        w = 1.0 if weight is None else weight[k]
        hit = (k >= start) if only is None else (k == only)
        m.append(x + (d_m * w if hit else 0.0))
    s.ebitda_m = m
    return s


def exit_value(base: cm.State, mult: float) -> float:
    s = copy.deepcopy(base)
    s.exit_mult = mult
    return ps(s)["ps_exit"]


def exp_return(value_today: float, ke: float) -> float:
    return value_today * (1 + ke) / PRICE - 1.0


def main() -> None:
    base = base_state()
    b = ps(base)
    ke = b["ke"]
    out: dict = {"price": PRICE, "dps": DPS, "ke": ke, "wacc": b["wacc"], "base_exit": b["ps_exit"],
                 "base_gordon_ronic": b["ps_gordon_ronic"], "base_gordon_naive": b["ps_gordon_naive"],
                 "base_exp_return": b["exp_return_exit"]}

    # ---- rating bands (project convention, references/recommendation-guide.md) -------------------------------------
    def v_for(er: float) -> float:
        return (1 + er) * PRICE / (1 + ke)

    slope = (exit_value(base, base.exit_mult + 1.0) - exit_value(base, base.exit_mult)) / 1.0

    def mult_for(v: float) -> float:
        return base.exit_mult + (v - b["ps_exit"]) / slope

    bands = {}
    for name, er in (("sell_edge", -0.10), ("clean_low", -0.05), ("clean_high", 0.10), ("buy_edge", 0.15)):
        v = v_for(er)
        bands[name] = {"exp_return": er, "value": v, "multiple": mult_for(v)}
    out["bands"] = bands
    out["slope_per_turn"] = slope
    out["reverse_multiple"] = mult_for(PRICE)

    # ---- exit multiple table --------------------------------------------------------------------------------------
    rows = []
    for m in (5.0, 5.526, base.exit_mult, 6.0, 6.2, 6.5, 6.8, 7.0):
        v = exit_value(base, m)
        rows.append({"multiple": m, "value": v, "exp_return": exp_return(v, ke)})
    out["multiple_table"] = rows
    out["curve"] = [{"multiple": m / 10, "value": exit_value(base, m / 10), "exp_return": exp_return(exit_value(base, m / 10), ke)}
                    for m in range(48, 76, 2)]

    # ---- thesis levers (start FY2027E) ---------------------------------------------------------------------------
    share_na = [SEG["na"]["rev"][k] / SEG["total"][k] for k in range(5)]
    share_mx = [SEG["mx"]["rev"][k] / SEG["total"][k] for k in range(5)]
    out["share_na"], out["share_mx"] = share_na, share_mx

    def d(s: cm.State) -> dict:
        r = ps(s)
        return {"exit": r["ps_exit"] - b["ps_exit"], "gordon_ronic": r["ps_gordon_ronic"] - b["ps_gordon_ronic"]}

    L = {}
    L["margin_m50_from27"] = d(shock_margin(base, -0.005))
    L["margin_m100_from27"] = d(shock_margin(base, -0.010))
    L["margin_m100_2027_only"] = d(shock_margin(base, -0.010, only=1))
    L["margin_m50_all_years"] = d(shock_margin(base, -0.005, start=0))
    L["margin_p50_all_years"] = d(shock_margin(base, +0.005, start=0))
    L["na_margin_p100"] = d(shock_margin(base, +0.010, weight=share_na))
    L["na_margin_gap_flowers_p150"] = d(shock_margin(base, +0.015, weight=share_na))
    L["mx_margin_m100"] = d(shock_margin(base, -0.010, weight=share_mx))
    L["mx_margin_m150"] = d(shock_margin(base, -0.015, weight=share_mx))
    L["na_growth_m1pp"] = d(shock_growth(base, "na", -0.01))
    L["mx_growth_m2pp"] = d(shock_growth(base, "mx", -0.02))
    both = shock_growth(shock_growth(base, "na", -0.01), "mx", -0.02)
    # the second shock re-uses the base revenue path; combine by adding the two revenue deltas
    rev0 = b["rev"]
    r_na = ps(shock_growth(base, "na", -0.01))["rev"]
    r_mx = ps(shock_growth(base, "mx", -0.02))["rev"]
    comb = [rev0[k] + (r_na[k] - rev0[k]) + (r_mx[k] - rev0[k]) for k in range(5)]
    both = copy.deepcopy(base)
    both.growth = growth_from_rev(base.rev0, comb)
    L["growth_both"] = d(both)
    out["levers"] = L
    out["levers_consolidated"] = CONS["consolidated"]["levers"]

    # ---- three-thesis scenario: combined sensitivities (not additive: run jointly) -----------------------------------
    bear = shock_margin(base, -0.005)
    bear.growth = both.growth
    out["scenario_bear_ops"] = d(bear)                      # wheat -50 bp persistent + growth shortfall, base multiple
    bull = shock_margin(base, +0.015, weight=share_na)
    out["scenario_bull_ops"] = d(bull)                      # NA margin closes the gap to Flowers
    s_all = shock_margin(base, +0.015, weight=share_na)
    s_all = shock_margin(s_all, -0.005)
    s_all.growth = both.growth
    out["scenario_all_three"] = d(s_all)                    # all three theses at once

    # ---- downside and upside cases including the multiple ----------------------------------------------------------
    def case(s: cm.State, m: float) -> dict:
        t = copy.deepcopy(s)
        t.exit_mult = m
        r = ps(t)
        return {"value": r["ps_exit"], "exp_return": r["exp_return_exit"], "multiple": m}

    peers = json.loads((DATA / "peers_v3.json").read_text(encoding="utf-8"))
    core_m = peers["medians"]["core_median"]["ev_ebitda_ltm"]     # core-baker median on the claim basis (peer workbook v3)
    out["case_bear_core"] = case(bear, core_m)                      # wheat -50 bp + growth shortfall + 5.53x
    out["case_bear_base_multiple"] = case(bear, base.exit_mult)
    out["case_bull_hold_high"] = case(bull, 6.82)                   # NA gap closes + 6.82x
    out["case_all_three_base_multiple"] = case(s_all, base.exit_mult)
    out["case_core_multiple_only"] = case(base, core_m)

    # ---- football-field rows (MXN per share) -----------------------------------------------------------------------
    g = CONS["consolidated"]["grids"]
    exit_grid, mults, waccs = g["exit"], g["mults"], g["wacc"]
    gr_grid, gs = g["gordon_ronic"], g["g"]
    out["football"] = {
        "dcf_exit_multiple": {"low": exit_grid[2][0], "mid": b["ps_exit"], "high": exit_grid[2][4],
                              "note": f"{mults[0]:.1f}x-{mults[4]:.1f}x on FY2030E EBITDA"},
        "dcf_exit_wacc": {"low": exit_grid[4][2], "mid": b["ps_exit"], "high": exit_grid[0][2],
                          "note": f"WACC {waccs[0]*100:.1f}%-{waccs[4]*100:.1f}%"},
        "dcf_gordon_ronic": {"low": gr_grid[2][0], "mid": b["ps_gordon_ronic"], "high": gr_grid[2][4],
                             "note": f"g {gs[0]*100:.1f}%-{gs[4]*100:.1f}%, RONIC 14.6%"},
    }
    # ---- tornado, exit method, every year from FY2026E (both directions computed, not mirrored) ---------------------
    def v_exit(s: cm.State, **kw) -> float:
        return ps(s, **kw)["ps_exit"] - b["ps_exit"]

    def with_field(field: str, delta: float) -> cm.State:
        s = copy.deepcopy(base)
        setattr(s, field, [x + delta for x in getattr(base, field)])
        return s

    def with_mult(delta: float) -> cm.State:
        s = copy.deepcopy(base)
        s.exit_mult += delta
        return s

    out["tornado"] = [
        {"label": "Exit multiple +/-0.5x", "down": v_exit(with_mult(-0.5)), "up": v_exit(with_mult(+0.5))},
        {"label": "EBITDA margin +/-50 bp", "down": v_exit(with_field("ebitda_m", -0.005)), "up": v_exit(with_field("ebitda_m", +0.005))},
        {"label": "Capex +/-50 bp of sales", "down": v_exit(with_field("capex_pct", +0.005)), "up": v_exit(with_field("capex_pct", -0.005))},
        {"label": "Revenue growth +/-50 bp", "down": v_exit(with_field("growth", -0.005)), "up": v_exit(with_field("growth", +0.005))},
        {"label": "WACC +/-50 bp", "down": v_exit(base, wacc_shift=+0.005), "up": v_exit(base, wacc_shift=-0.005)},
    ]

    # ---- exit multiple by regional mix (evidence for the exit-multiple decision; NOT used in the DCF) -------------------
    # Rest of the group at the core-baker median; Mexico at a reference multiple. Weights: FY2025 Adj. EBITDA shares
    # (Celebramos p.17; Mexico includes eliminations) [assumption: FY2025 mix applied to the FY2030E terminal year].
    mult = {p["name"]: p["ev_ebitda_ltm"] for p in peers["peers"]}
    gruma, arca = mult["Gruma, S.A.B. de C.V."], mult["Arca Continental, S.A.B. de C.V."]
    today = mult["Grupo Bimbo, S.A.B. de C.V. (subject)"]
    w_mx = 0.554

    def blend(x: float) -> float:
        return (1 - w_mx) * core_m + w_mx * x

    def mex_for(m: float) -> float:
        return (m - (1 - w_mx) * core_m) / w_mx

    def at(m: float) -> dict:
        v = exit_value(base, m)
        return {"multiple": m, "value": v, "exp_return": exp_return(v, ke)}

    out["mix"] = {
        "w_mx": w_mx, "rest_multiple": core_m, "gruma": gruma, "arca": arca, "bimbo_today": today,
        "group_if_gruma": at(blend(gruma)), "group_if_arca": at(blend(arca)), "group_if_mid": at(blend(6.6)),
        "mexico_for_today": mex_for(today), "mexico_for_base": mex_for(base.exit_mult),
        "mexico_for_clean_low": mex_for(bands["clean_low"]["multiple"]), "mexico_for_clean_high": mex_for(bands["clean_high"]["multiple"]),
        "mexico_for_buy": mex_for(bands["buy_edge"]["multiple"]),
    }
    (DATA / "levers.json").write_text(json.dumps(out, indent=1), encoding="utf-8")

    m_ = out["mix"]
    print("MIX  rest of group at %.2fx; Gruma %.2fx, Arca %.2fx, Bimbo today %.2fx" % (core_m, gruma, arca, today))
    for k in ("group_if_gruma", "group_if_arca", "group_if_mid"):
        print("  %-15s group multiple %.2fx -> value %.2f, expected return %+.1f%%" % (k, m_[k]["multiple"], m_[k]["value"], m_[k]["exp_return"] * 100))
    print("  Mexico multiple implied: today %.2fx | base %.2fx | clean HOLD %.2fx-%.2fx | BUY %.2fx" % (
        m_["mexico_for_today"], m_["mexico_for_base"], m_["mexico_for_clean_low"], m_["mexico_for_clean_high"], m_["mexico_for_buy"]))

    print("base exit", round(b["ps_exit"], 2), "ER", round(b["exp_return_exit"], 4), "slope/turn", round(slope, 3))
    for k, v in bands.items():
        print(f"  {k:11s} ER {v['exp_return']:+.0%}  value {v['value']:.2f}  multiple {v['multiple']:.2f}x")
    print("  reverse multiple", round(out["reverse_multiple"], 3))
    for k, v in L.items():
        print(f"  {k:28s} exit {v['exit']:+.2f}  gordon {v['gordon_ronic']:+.2f}")
    for k in ("scenario_bear_ops", "scenario_bull_ops", "scenario_all_three"):
        print(" ", k, {a: round(x, 2) for a, x in out[k].items()})
    for r in rows:
        print(f"  mult {r['multiple']:.3f} value {r['value']:.2f} ER {r['exp_return']:+.1%}")
    print("  football", {k: {a: (round(x, 2) if isinstance(x, float) else x) for a, x in v.items()} for k, v in out["football"].items()})
    print("  NA share", [round(x, 3) for x in share_na], "MX share", [round(x, 3) for x in share_mx])


if __name__ == "__main__":
    main()
