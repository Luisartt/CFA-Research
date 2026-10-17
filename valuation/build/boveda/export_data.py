"""Export the BIMBOA DCF inputs and reference results for the Boveda Vision page.

Run from the project root:  python -I <this file> --project . --out <data.json>
Reads only; never writes inside the project.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import statistics
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=".")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    project = Path(a.project).resolve()
    sys.path.insert(0, str(project / "valuation" / "build"))
    import dcf_core as core  # noqa: E402

    c = core.build_case(project)
    ex = c.extra
    last = c.last
    seg_labels = {s["key"]: s.get("label", s["key"]) for s in (core.load_yaml(project / "model" / "drivers.yaml")
                                                              .get("revenue_segments") or [])}
    drv = {k: c.drivers[k] for k in ("gross_margin", "opex_pct_revenue", "da_pct_revenue", "capex_pct_revenue",
                                     "lease_principal_pct_revenue", "dso", "dio", "dpo", "other_ca_pct_revenue",
                                     "other_cl_pct_revenue", "tax_rate")}
    seg_growth = {s: c.drivers[f"seg_{s}_growth"] for s in c.segments}

    # WACC options
    va = ex.get("wacc_variants") or {}
    rf_a = float(va["rf"]["mbono10"]["value"])
    def_spread = float(va["rf"]["def_spread"]["value"])
    crp_co = core.crp_from_countries(ex)["company"]      # the one validated country -> region -> company build
    crp_ebitda, crp_rev = crp_co["ebitda_fy25"], crp_co["revenue_fy25"]
    unlev = []
    for p in ex.get("beta_peers") or []:
        if p.get("include", True):
            de = float(p["debt_incl_leases"]) / float(p["market_equity"])
            unlev.append(float(p["beta_levered"]) / (1 + (1 - float(p["tax"])) * de))
    beta_med, beta_mean = statistics.median(unlev), statistics.fmean(unlev)
    cs = ex.get("capital_structure") or {}
    kd = ex.get("kd_candidates") or []

    b = core.bridge(c)
    items_cfg = ex.get("bridge_items") or {}
    short = {"retirement": "Retiro y post-retiro (neto)", "us_welfare": "Previsión social EUA (LP)",
             "lt_bonuses": "Bonos LP a colaboradores", "mepp": "Salida de planes MEPP",
             "deferred_comp": "Compensaciones diferidas", "provisions": "Provisiones: posiciones fiscales inciertas y juicios",
             "derivatives": "Derivados (pasivo neto)", "nci_uplift": "Prima de mercado del NCI (operadores BBU)"}
    bridge_items = [{"key": k, "label": short.get(k, k), "value": float(v.get("value", 0.0)),
                     "source": str(v.get("source", ""))[:220]} for k, v in items_cfg.items()]

    # base route: B when valuation.yaml holds the default-free MXN rate (M-Bono - default spread)
    base_route = "B1" if abs(c.wacc_in["risk_free"] - (rf_a - def_spread)) < 1e-9 else "A"
    # peer medians from the v3 peer workbook spec; comps value per share on the Jun-26 bridge with peer-EV claims
    import yaml as _yaml
    pe_path = project / "valuation" / "inputs" / "peer_extras_v3.yaml"
    pe = _yaml.safe_load(pe_path.read_text(encoding="utf-8")) if pe_path.is_file() else {}
    meds = ((pe.get("expected") or {}).get("medians") or {})
    m_core = float(meds.get("core_ev_ltm", 5.641458))
    m_all = float(meds.get("all_ev_ltm", 8.269323))
    m_ntm = float(meds.get("all_ev_ntm", 9.215747))
    LTM_EBITDA = 60919.0
    dbj = ex.get("dated_bridge") or {}
    rec = lambda k: float(dbj[k]["value"] if isinstance(dbj[k], dict) else dbj[k])  # noqa: E731  (records or numbers)
    ke0 = core.value(c, basis="published")["ke"]
    nci_mkt = core.nci_claim(c, ke0)["market"]
    claims_jun = rec("debt_jun") + rec("leases_jun") - rec("cash_jun") + nci_mkt - rec("non_op_jun")
    shares_jun = rec("shares_out")

    def comps_v(m):
        return (m * LTM_EBITDA - claims_jun) / shares_jun

    bimbo_mult = (c.price * shares_jun + claims_jun) / LTM_EBITDA
    names = {"FLO": "Flowers", "GRUMA": "Gruma", "YMZ": "Yamazaki", "ARYN": "Aryzta", "SJM": "Smucker", "CPB": "Campbell's",
             "MDLZ": "Mondelez", "AC": "Arca", "PEP": "PepsiCo"}
    elig = {e["key"]: e for e in (pe.get("eligibility") or [])}
    peer_pts = sorted([{"name": names.get(k, k), "m": float(d["ev_ebitda_ltm"])}
                       for k, d in ((pe.get("expected") or {}).get("per_company") or {}).items()
                       if isinstance(d.get("ev_ebitda_ltm"), (int, float)) and elig.get(k, {}).get("in_median") == "yes"],
                      key=lambda x: x["m"])
    data = {
        "meta": {"company": "Grupo Bimbo, S.A.B. de C.V.", "ticker": "BMV: BIMBO A", "valuation_date": "2026-10-16",
                 "as_of": "2026-10-17", "currency": "MXN", "units": "millones de MXN"},
        "years": {"hist_last": last, "fcst": c.fcst_years},
        "segments": [{"key": s, "label": seg_labels.get(s, s), "fy_last": c.h("seg_" + s), "growth": seg_growth[s]}
                     for s in c.segments],
        "drivers": drv,
        "fy_last": {k: c.h(k) for k in ("revenue", "receivables", "inventory", "other_current_assets", "payables",
                                         "other_current_liabilities", "lease_liabilities", "debt_short", "debt_long",
                                         "cash", "nci_equity", "shares_diluted")},
        "valuation": {"price": c.price, "w52_low": 53.03, "w52_high": 68.67, "stub": c.stub, "mid_year": c.mid_year,
                      "non_op": c.non_op, "debt_like_engine": c.debt_like, "g": c.g, "exit_multiple": c.exit_multiple,
                      "lt_gdp": 0.05, "next_div": 1.05,
                      "wacc": {"rf": c.wacc_in["risk_free"], "erp": c.wacc_in["equity_risk_premium"],
                               "crp": c.wacc_in["country_risk_premium"], "beta_u": c.wacc_in["beta_unlevered"],
                               "de": c.wacc_in["target_debt_to_equity"], "kd": c.wacc_in["pre_tax_cost_of_debt"],
                               "tax": c.wacc_in["tax_rate"]}},
        "bridge_items": bridge_items,
        "nci_claim": {"income": float(ex["nci_claim"]["income"]), "growth": float(ex["nci_claim"]["growth"])},
        "options": {
            "route": {"A": {"rf": rf_a, "crp": 0.0, "label": f"A · local: M-Bono 10a {rf_a:.2%}, sin prima país"},
                      "B1": {"rf": rf_a - def_spread, "crp": crp_ebitda,
                             "label": f"B · Damodaran: rf {rf_a - def_spread:.2%} + prima país {crp_ebitda:.2%} "
                                      "(ponderada por EBITDA)"},
                      "B2": {"rf": rf_a - def_spread, "crp": crp_rev,
                             "label": f"B · Damodaran: rf {rf_a - def_spread:.2%} + prima país {crp_rev:.2%} "
                                      "(ponderada por ventas)"}},
            "beta": [{"id": "g053", "value": 0.53, "label": "Damodaran Food Processing, global"},
                     {"id": "u046", "value": 0.46, "label": "Damodaran Food Processing, EUA"},
                     {"id": "bum", "value": beta_med, "label": "Pares, mediana desapalancada"},
                     {"id": "bua", "value": beta_mean, "label": "Pares, promedio desapalancado"}],
            "de": [{"id": "cur", "value": float(cs["de_current"]["value"]), "label": "Bimbo hoy (mercado, con arrendamientos)"},
                   {"id": "mgmt", "value": float(cs["de_mgmt"]["value"]), "label": "Rango de la administración 2.0–2.5x"},
                   {"id": "peer", "value": float(cs["de_peer_median"]["value"]), "label": "Mediana de pares"}],
            "kd": [{"id": f"k{i}", "value": float(k["value"]), "label": str(k["label"])} for i, k in enumerate(kd)],
            "exit_presets": [{"value": m_core, "label": f"Panificadoras {m_core:.2f}x"}, {"value": 6.0, "label": "Propuesta 6.0x"},
                             {"value": bimbo_mult, "label": f"Bimbo hoy {bimbo_mult:.2f}x"},
                             {"value": m_all, "label": f"Todos los pares {m_all:.2f}x"},
                             {"value": m_ntm, "label": f"Pares NTM {m_ntm:.2f}x"}],
        },
        "comps": {"ltm_ebitda": LTM_EBITDA, "bimbo_multiple_peer_claims": bimbo_mult,
                  "points": [{"m": m_core, "v": comps_v(m_core)}, {"m": 6.0, "v": comps_v(6.0)}, {"m": m_all, "v": comps_v(m_all)}],
                  "peers": peer_pts},
    }
    data["valuation"]["base_route"] = base_route

    # ---------------- reference results (Python, valuation/build/dcf_core.py) for the JS test
    def pub(cc):
        return core.value(cc, basis="published")

    def with_wacc(**kw):
        w = dict(c.wacc_in)
        w.update(kw)
        return dataclasses.replace(c, wacc_in=w)

    def with_opex(shift):
        d = dict(c.drivers)
        d["opex_pct_revenue"] = [x + shift for x in d["opex_pct_revenue"]]
        return dataclasses.replace(c, drivers=d)

    p0, e0 = pub(c), core.value(c)
    ps = p0["roll_factor"] / p0["bridge"]["shares"]
    n = p0["nci"]
    prov = next(i["value"] for i in bridge_items if i["key"] == "provisions")
    outside = sum(i["value"] for i in bridge_items if i["key"] != "nci_uplift")
    cases = {
        "published": {"opts": {}, "gordon": p0["price_gordon"], "exit": p0["price_exit"], "ronic": p0["tv_ronic"],
                      "implied_g": p0["implied_g"], "wacc": p0["wacc"], "ke": p0["ke"]},
        "engine": {"opts": {"lease": "engine", "exitClaims": "full"}, "gordon": e0["price_gordon"],
                   "exit": e0["price_exit"], "ronic": e0["tv_ronic"], "implied_g": e0["implied_g"]},
        "beta046": {"opts": {"beta": 0.46}, "gordon": pub(with_wacc(beta_unlevered=0.46))["price_gordon"],
                    "exit": pub(with_wacc(beta_unlevered=0.46))["price_exit"]},
        "routeA": {"opts": {"route": "A"},
                   "gordon": pub(with_wacc(risk_free=rf_a, country_risk_premium=0.0))["price_gordon"],
                   "exit": pub(with_wacc(risk_free=rf_a, country_risk_premium=0.0))["price_exit"]},
        "routeB2": {"opts": {"route": "B2"},
                    "gordon": pub(with_wacc(risk_free=rf_a - def_spread, country_risk_premium=crp_rev))["price_gordon"],
                    "exit": pub(with_wacc(risk_free=rf_a - def_spread, country_risk_premium=crp_rev))["price_exit"]},
        "capexm05": {"opts": {"capexShift": -0.005},
                     "gordon": pub(core.build_case(project, capex_shift=-0.005))["price_gordon"],
                     "exit": pub(core.build_case(project, capex_shift=-0.005))["price_exit"]},
        "gmp05": {"opts": {"gmShift": 0.005}, "gordon": pub(core.build_case(project, gm_shift=0.005))["price_gordon"],
                  "exit": pub(core.build_case(project, gm_shift=0.005))["price_exit"]},
        "growthp05": {"opts": {"growthShift": 0.005},
                      "gordon": pub(core.build_case(project, growth_shift=0.005))["price_gordon"],
                      "exit": pub(core.build_case(project, growth_shift=0.005))["price_exit"]},
        "opexm05": {"opts": {"opexShift": -0.005}, "gordon": pub(with_opex(-0.005))["price_gordon"],
                    "exit": pub(with_opex(-0.005))["price_exit"]},
        "ronicWacc": {"opts": {"tvMethod": "ronic", "ronic": "wacc"}, "gordon": core.ronic_case(c, p0, p0["wacc"])},
        "ronic125": {"opts": {"tvMethod": "ronic", "ronic": 0.125}, "gordon": core.ronic_case(c, p0, 0.125)},
        "nciG0": {"opts": {"nci": "g0"}, "gordon": p0["price_gordon"] + (n["uplift"] - n["uplift_g0"]) * ps,
                  "exit": p0["price_exit"] + (n["uplift"] - n["uplift_g0"]) * ps},
        "nciBook": {"opts": {"nci": "book"}, "gordon": p0["price_gordon"] + n["uplift"] * ps,
                    "exit": p0["price_exit"] + n["uplift"] * ps},
        "noProvisions": {"opts": {"provisions": False}, "gordon": p0["price_gordon"] + prov * ps, "exit": p0["price_exit"]},
        "exitFull": {"opts": {"exitClaims": "full"}, "exit": p0["price_exit"] - outside * ps},
    }
    data["reference"] = {"cases": cases, "published": {
        "ev_gordon": p0["ev_gordon"], "ev_exit": p0["ev_exit"], "tv_share_gordon": p0["tv_share_gordon"],
        "implied_exit_multiple": p0["implied_exit_multiple"], "implied_g_exit": p0["implied_g_exit"],
        "tgt12": p0["price_gordon"] * (1 + p0["ke"]) - 1.05}}
    Path(a.out).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", a.out)
    for k, v in cases.items():
        print(f"  {k:12s} G {v.get('gordon', float('nan')):.6f}  X {v.get('exit', float('nan')):.6f}")
    print("  beta median/mean", round(beta_med, 6), round(beta_mean, 6), "crp", round(crp_ebitda, 6), round(crp_rev, 6))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
