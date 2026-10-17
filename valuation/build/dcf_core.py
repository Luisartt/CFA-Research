"""Pure-Python replica of the valuation mechanics used by the project's model engine.

It mirrors rcmodel/valuation.py and rcmodel/lines.py (FCFF, discounting, terminal values,
bridge, roll-forward, sensitivity) so the generated workbooks can be checked against an
independent calculation, and it solves the reverse-DCF growth shift by bisection.
It never writes files.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path

import yaml

DAYS = 365.0
SEG = "seg_"


# ----------------------------------------------------------------------------- loading

def load_financials(path: Path) -> dict[str, dict[int, float]]:
    out: dict[str, dict[int, float]] = {}
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            key = row["line_item"].strip()
            try:
                year, value = int(row["year"]), float(row["value"])
            except (TypeError, ValueError):
                continue
            out.setdefault(key, {})[year] = value
    return out


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def load_summary(path: Path) -> dict | None:
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


@dataclass
class Case:
    """Everything the DCF needs, in the model's units (MXN millions)."""

    hist_years: list[int]
    fin: dict[str, dict[int, float]]
    fcst_years: list[int]
    drivers: dict[str, list[float]]
    segments: list[str]                      # segment keys (without the seg_ prefix), may be empty
    wacc_in: dict[str, float]                # risk_free, equity_risk_premium, country_risk_premium, beta_unlevered,
                                             # target_debt_to_equity, pre_tax_cost_of_debt, tax_rate
    g: float
    exit_multiple: float
    mid_year: bool
    stub: float
    non_op: float
    debt_like: float
    price: float
    lease_method: str = "principal"          # "intensity" = lease liability held at the FY share of revenue
    growth_shift: float = 0.0
    gm_shift: float = 0.0
    capex_shift: float = 0.0
    extra: dict = field(default_factory=dict)

    @property
    def last(self) -> int:
        return self.hist_years[-1]

    def h(self, key: str, year: int | None = None, default: float = 0.0) -> float:
        return self.fin.get(key, {}).get(self.last if year is None else year, default)


def build_case(project: Path, *, growth_shift: float = 0.0, gm_shift: float = 0.0, capex_shift: float = 0.0) -> Case:
    fin = load_financials(project / "data" / "financials.csv")
    drv_doc = load_yaml(project / "model" / "drivers.yaml")
    val = load_yaml(project / "valuation" / "valuation.yaml")
    years = sorted(fin["revenue"])
    n = int(drv_doc.get("forecast_years", 5))
    drivers = {k: [float(x) for x in v["values"]] for k, v in drv_doc["drivers"].items()}
    segments = [s["key"] for s in (drv_doc.get("revenue_segments") or [])]
    extras_path = project / "valuation" / "inputs" / "spg_inputs.yaml"
    extras = load_yaml(extras_path) if extras_path.is_file() else {}
    lease_method = str((extras.get("lease_schedule") or {}).get("method", "principal"))
    return Case(
        hist_years=years, fin=fin, fcst_years=[years[-1] + i for i in range(1, n + 1)], drivers=drivers,
        segments=segments, wacc_in={k: float(v) for k, v in val["wacc"].items()},
        g=float(val["terminal"]["growth"]), exit_multiple=float(val["terminal"]["exit_ev_ebitda"]),
        mid_year=bool(val.get("mid_year", True)), stub=float(val.get("years_since_fiscal_year_end") or 0.0),
        non_op=float(val.get("non_operating_assets") or 0.0), debt_like=float(val.get("debt_like_items") or 0.0),
        price=float(val["share_price"]), lease_method=lease_method,
        growth_shift=growth_shift, gm_shift=gm_shift, capex_shift=capex_shift, extra=extras,
    )


# ----------------------------------------------------------------------------- mechanics

def wacc(c: Case) -> dict[str, float]:
    w = c.wacc_in
    beta_l = w["beta_unlevered"] * (1 + (1 - w["tax_rate"]) * w["target_debt_to_equity"])
    ke = w["risk_free"] + beta_l * w["equity_risk_premium"] + w["country_risk_premium"]
    kd_after = w["pre_tax_cost_of_debt"] * (1 - w["tax_rate"])
    we = 1 / (1 + w["target_debt_to_equity"])
    wd = w["target_debt_to_equity"] / (1 + w["target_debt_to_equity"])
    return {"beta_l": beta_l, "ke": ke, "kd_after": kd_after, "we": we, "wd": wd, "wacc": we * ke + wd * kd_after}


def _drv(c: Case, key: str, i: int) -> float:
    vals = c.drivers.get(key)
    if vals is None:
        raise KeyError(f"driver {key} missing from drivers.yaml")
    return vals[i]


def forecast(c: Case) -> dict[str, list[float]]:
    """Forecast lines for the DCF, mirroring the engine (plus optional scenario shifts).

    Also returns the published-basis lease lines: the lease liability is held at its last
    actual share of revenue, so new leases = principal repaid + growth in the liability, and
    fcff_pub = engine FCFF - growth in the lease liability.
    """
    n = len(c.fcst_years)
    rev: list[float] = []
    seg_vals = {s: c.h(SEG + s) for s in c.segments}
    prev_rev = c.h("revenue")
    for i in range(n):
        if c.segments:
            total = 0.0
            for s in c.segments:
                seg_vals[s] = seg_vals[s] * (1 + _drv(c, f"{SEG}{s}_growth", i) + c.growth_shift)
                total += seg_vals[s]
            rev.append(total)
        else:
            rev.append(prev_rev * (1 + _drv(c, "revenue_growth", i) + c.growth_shift))
        prev_rev = rev[-1]
    out: dict[str, list[float]] = {k: [] for k in (
        "revenue", "cogs", "gross_profit", "opex", "ebit", "da", "ebitda", "tax", "nopat", "capex",
        "new_leases", "receivables", "inventory", "other_ca", "payables", "other_cl",
        "change_nwc", "fcff", "lease_liab", "lease_growth", "lease_additions", "fcff_pub")}
    prev = {
        "receivables": c.h("receivables"), "inventory": c.h("inventory"),
        "other_ca": c.h("other_current_assets"), "payables": c.h("payables"),
        "other_cl": c.h("other_current_liabilities"),
    }
    lease_prev, rev_prev = c.h("lease_liabilities"), c.h("revenue")
    for i in range(n):
        r = rev[i]
        gm = _drv(c, "gross_margin", i) + c.gm_shift
        cogs = r * (1 - gm)
        gp = r - cogs
        opex = r * _drv(c, "opex_pct_revenue", i)
        ebit = gp - opex
        da = r * _drv(c, "da_pct_revenue", i)
        tax = ebit * _drv(c, "tax_rate", i)
        nopat = ebit - tax
        capex = r * (_drv(c, "capex_pct_revenue", i) + c.capex_shift)
        new_leases = r * _drv(c, "lease_principal_pct_revenue", i)
        bal = {
            "receivables": r * _drv(c, "dso", i) / DAYS,
            "inventory": cogs * _drv(c, "dio", i) / DAYS,
            "other_ca": r * _drv(c, "other_ca_pct_revenue", i),
            "payables": cogs * _drv(c, "dpo", i) / DAYS,
            "other_cl": r * _drv(c, "other_cl_pct_revenue", i),
        }
        dnwc = -((bal["receivables"] - prev["receivables"]) + (bal["inventory"] - prev["inventory"])
                 + (bal["other_ca"] - prev["other_ca"]) - (bal["payables"] - prev["payables"])
                 - (bal["other_cl"] - prev["other_cl"]))
        fcff = nopat + da - capex - new_leases + dnwc
        lease_liab = lease_prev * r / rev_prev
        lease_growth = lease_liab - lease_prev
        for k, v in (("revenue", r), ("cogs", cogs), ("gross_profit", gp), ("opex", opex), ("ebit", ebit),
                     ("da", da), ("ebitda", ebit + da), ("tax", tax), ("nopat", nopat), ("capex", capex),
                     ("new_leases", new_leases), ("change_nwc", dnwc), ("fcff", fcff),
                     ("lease_liab", lease_liab), ("lease_growth", lease_growth),
                     ("lease_additions", new_leases + lease_growth), ("fcff_pub", fcff - lease_growth)):
            out[k].append(v)
        for k, v in bal.items():
            out[k].append(v)
        prev = bal
        lease_prev, rev_prev = lease_liab, r
    return out


CRP_REGION_CODES = {"North America (US + Canada)": "North America", "Mexico": "Mexico",
                    "Europe, Asia & Africa": "EAA", "Latin America": "Latin America"}
CRP_BASES = {"ebitda_fy25": "ebitda_weight", "revenue_fy25": "revenue_weight", "ebitda_3y": "ebitda_weight_3y",
             "revenue_3y": "revenue_weight_3y"}


def crp_from_countries(extra: dict, tol: float = 1e-9) -> dict:
    """One calculation layer for the route-B country risk premium: countries -> regions (plant-weighted, included
    countries) -> company (region weights). Validates the inputs and that the stored region CRPs in crp_exposure equal
    the country build, so the WACC workbook, the DCF scenarios and the page cannot drift apart."""
    import math
    va = extra.get("wacc_variants") or {}
    countries = va.get("crp_countries") or []
    regions = va.get("crp_exposure") or []
    if not countries or not regions:
        raise ValueError("crp_countries and crp_exposure are required for route B")
    labels = [str(r.get("region")) for r in regions]
    if sorted(labels) != sorted(CRP_REGION_CODES) or len(set(labels)) != len(labels):
        raise ValueError(f"crp_exposure must hold each region exactly once: {labels}")
    codes = set(CRP_REGION_CODES.values())
    seen = set()
    for c in countries:
        if c.get("region") not in codes:
            raise ValueError(f"country {c.get('country')} has an unknown region code {c.get('region')!r}")
        cid = (c.get("region"), c.get("country"))
        if cid in seen:
            raise ValueError(f"duplicate country row {cid}")
        seen.add(cid)
        for fld in ("plants", "crp"):
            x = c.get(fld)
            if not isinstance(x, (int, float)) or not math.isfinite(float(x)) or float(x) < 0:
                raise ValueError(f"country {c.get('country')}: {fld} must be a finite non-negative number, got {x!r}")
    for r in regions:
        for wk in ("crp",) + tuple(CRP_BASES.values()):
            x = r.get(wk)
            if not isinstance(x, (int, float)) or not math.isfinite(float(x)) or float(x) < 0:
                raise ValueError(f"crp_exposure {r.get('region')}: {wk} must be a finite non-negative number, got {x!r}")
    out = {"regions": {}, "company": {}}
    for r in regions:
        label = str(r.get("region"))
        code = CRP_REGION_CODES[label]
        res = {}
        for key, ex_arg in (("crp", False), ("crp_ex_argentina", True)):
            inc = [c for c in countries if c.get("region") == code and c.get("include", True)
                   and not (ex_arg and c.get("country") == "Argentina")]
            plants = sum(float(c.get("plants") or 0) for c in inc)
            if plants <= 0:
                raise ValueError(f"no included plants in region {code}")
            res[key] = sum(float(c.get("plants") or 0) * float(c["crp"]) for c in inc) / plants
            if key == "crp":
                res["plants"] = plants
        if abs(res["crp"] - float(r.get("crp", -1))) > tol:
            raise ValueError(f"crp_exposure {label}: stored {r.get('crp')} != country build {res['crp']}")
        out["regions"][label] = {**res, **{wk: float(r.get(wk, r.get("ebitda_weight", 0.0))) for wk in CRP_BASES.values()}}
    for base, wk in CRP_BASES.items():
        ws = [v[wk] for v in out["regions"].values()]
        if abs(sum(ws) - 1.0) > 1e-6 or min(ws) < 0:
            raise ValueError(f"CRP weights for {base} do not sum to 1: {sum(ws)}")
        out["company"][base] = sum(v[wk] * v["crp"] for v in out["regions"].values())
        out["company"][base + "_xar"] = sum(v[wk] * v["crp_ex_argentina"] for v in out["regions"].values())
    return out


def nci_claim(c: Case, ke: float) -> dict[str, float]:
    """Market value of the NCI claim = annual NCI income / (ke - g); uplift = market value - book."""
    n = c.extra.get("nci_claim") or {}
    income, growth = float(n.get("income", 0.0)), float(n.get("growth", 0.0))
    if income and not ke > growth:
        raise ValueError(f"NCI claim needs ke > g (ke {ke}, g {growth})")
    book = c.h("nci_equity")
    market = income / (ke - growth) if income else book
    market_g0 = income / ke if income else book
    return {"income": income, "growth": growth, "book": book, "market": market, "uplift": market - book,
            "uplift_g0": market_g0 - book}


def bridge_items(c: Case, ke: float) -> dict[str, float]:
    """Debt-like components (after tax) with the NCI uplift computed live at ke."""
    items = {}
    for k, item in (c.extra.get("bridge_items") or {}).items():
        items[k] = nci_claim(c, ke)["uplift"] if k == "nci_uplift" else float(item.get("value", 0.0))
    return items


def bridge(c: Case) -> dict[str, float]:
    debt = c.h("debt_short") + c.h("debt_long") + c.h("lease_liabilities")
    return {
        "debt_short": c.h("debt_short"), "debt_long": c.h("debt_long"), "lease_liabilities": c.h("lease_liabilities"),
        "cash": c.h("cash"), "total_debt": debt, "net_debt": debt - c.h("cash"), "nci": c.h("nci_equity"),
        "shares": c.h("shares_diluted"),
    }


def value(c: Case, *, basis: str = "engine") -> dict:
    """Valuation on one of two bases.

    engine    - mirrors the model engine exactly: FCFF deducts new leases = principal; one bridge
                (valuation.yaml debt_like_items) for both methods.
    published - FCFF also deducts the growth in the lease liability (liability held at the last actual
                share of revenue); Gordon TV = (FCFF_N x (1 + g) - g x L_N) / (WACC - g); Gordon uses
                the full bridge with the NCI uplift live at ke; exit uses peer-EV-consistent claims
                (net debt, NCI at market) because peer EVs exclude pensions, provisions and derivatives.
    """
    import math
    f = forecast(c)
    w = wacc(c)
    r, ke = w["wacc"], w["ke"]
    if not all(math.isfinite(x) for x in (r, ke, c.g, c.exit_multiple)):
        raise ValueError(f"non-finite valuation input: WACC {r}, ke {ke}, g {c.g}, exit {c.exit_multiple}")
    if not r > c.g:
        raise ValueError(f"WACC {r:.4%} must exceed terminal growth {c.g:.4%}")
    if not c.h("shares_diluted") > 0:
        raise ValueError("shares must be positive")
    off = 0.5 if c.mid_year else 0.0
    n = len(c.fcst_years)
    pub = basis == "published"
    flows = f["fcff_pub"] if pub else f["fcff"]
    periods = [t - off for t in range(1, n + 1)]
    dfs = [1 / (1 + r) ** p for p in periods]
    pvs = [x * d for x, d in zip(flows, dfs)]
    sum_pv = sum(pvs)
    fcff_n, ebitda_n, nopat_n = flows[-1], f["ebitda"][-1], f["nopat"][-1]
    lease_n = f["lease_liab"][-1]
    if pub:
        fcff_next = f["fcff"][-1] * (1 + c.g) - c.g * lease_n
    else:
        fcff_next = fcff_n * (1 + c.g)
    nopat_next = nopat_n * (1 + c.g)
    tv_g = fcff_next / (r - c.g)
    pv_tv_g = tv_g / (1 + r) ** (n - off)
    tv_x = ebitda_n * c.exit_multiple
    pv_tv_x = tv_x / (1 + r) ** n
    b = bridge(c)
    roll = (1 + ke) ** c.stub
    items = bridge_items(c, ke)
    nci = nci_claim(c, ke)
    debt_like_full = sum(items.values()) if pub else c.debt_like
    debt_like_exit = items.get("nci_uplift", 0.0) if pub else c.debt_like

    def per_share(ev: float, dl: float) -> float:
        return (ev + c.non_op - b["net_debt"] - b["nci"] - dl) / b["shares"] * roll

    ev_g, ev_x = sum_pv + pv_tv_g, sum_pv + pv_tv_x
    tv_x_adj = tv_x / (1 + r) ** off
    market_ev = c.price / roll * b["shares"] + b["net_debt"] + b["nci"] + debt_like_full - c.non_op
    implied_tv = (market_ev - sum_pv) * (1 + r) ** (n - off)
    base_n = f["fcff"][-1]
    if pub:     # TV = (F (1 + g) - g L) / (r - g)  ->  g = (TV r - F) / (TV + F - L)
        g_from_tv = lambda tv: (tv * r - base_n) / (tv + base_n - lease_n)  # noqa: E731
    else:
        g_from_tv = lambda tv: (tv * r - fcff_n) / (tv + fcff_n)  # noqa: E731
    out = {
        **w, "basis": basis, "periods": periods, "dfs": dfs, "pvs": pvs, "sum_pv": sum_pv, "tv_gordon": tv_g,
        "pv_tv_gordon": pv_tv_g, "ev_gordon": ev_g, "tv_exit": tv_x, "pv_tv_exit": pv_tv_x, "ev_exit": ev_x,
        "roll_factor": roll, "price_gordon": per_share(ev_g, debt_like_full),
        "price_exit": per_share(ev_x, debt_like_exit),
        "equity_gordon": ev_g + c.non_op - b["net_debt"] - b["nci"] - debt_like_full,
        "equity_exit": ev_x + c.non_op - b["net_debt"] - b["nci"] - debt_like_exit,
        "debt_like_gordon": debt_like_full, "debt_like_exit": debt_like_exit, "bridge_items": items, "nci": nci,
        "tv_share_gordon": pv_tv_g / ev_g, "implied_exit_multiple": tv_g * (1 + r) ** off / ebitda_n,
        "implied_g_exit": g_from_tv(tv_x_adj),
        "tv_ronic": (c.g / (1 - fcff_next / nopat_next) if nopat_next > 0 and fcff_next < nopat_next else None),
        "fcff_next": fcff_next, "nopat_next": nopat_next, "lease_n": lease_n,
        "market_ev": market_ev, "implied_tv": implied_tv,
        "implied_g": g_from_tv(implied_tv) if market_ev > sum_pv else None,
        "bridge": b, "lines": f,
    }
    return out


def per_share_with_tv(c: Case, v: dict, tv_gordon: float) -> float:
    """Gordon value per share today for a given terminal value (same explicit PV and bridge as v)."""
    r, n, off = v["wacc"], len(c.fcst_years), (0.5 if c.mid_year else 0.0)
    b = v["bridge"]
    ev = v["sum_pv"] + tv_gordon / (1 + r) ** (n - off)
    return (ev + c.non_op - b["net_debt"] - b["nci"] - v["debt_like_gordon"]) / b["shares"] * v["roll_factor"]


def ronic_case(c: Case, v: dict, ronic: float) -> float:
    """Value-driver terminal value: TV = NOPAT_N+1 x (1 - g / RONIC) / (WACC - g); returns value per share."""
    tv = v["nopat_next"] * (1 - c.g / ronic) / (v["wacc"] - c.g)
    return per_share_with_tv(c, v, tv)


def price_at(c: Case, w_: float, g_: float) -> float | None:
    """Gordon value per share today at WACC w_ and growth g_ (engine sensitivity convention: roll factor fixed)."""
    if w_ - g_ < 0.01:
        return None
    f = forecast(c)
    off = 0.5 if c.mid_year else 0.0
    n = len(c.fcst_years)
    pv = sum(x / (1 + w_) ** (t - off) for t, x in enumerate(f["fcff"], start=1))
    tv = f["fcff"][-1] * (1 + g_) / (w_ - g_) / (1 + w_) ** (n - off)
    b = bridge(c)
    roll = (1 + wacc(c)["ke"]) ** c.stub
    return (pv + tv + c.non_op - b["net_debt"] - b["nci"] - c.debt_like) / b["shares"] * roll


def solve_growth_shift(project: Path, target_price: float, method: str = "gordon",
                       lo: float = -0.10, hi: float = 0.10, tol: float = 1e-7, basis: str = "engine") -> float | None:
    """Uniform revenue-growth shift (added to every forecast growth driver) that makes the DCF equal the price."""
    def f(shift: float) -> float:
        v = value(build_case(project, growth_shift=shift), basis=basis)
        return v["price_gordon" if method == "gordon" else "price_exit"] - target_price
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = f(mid)
        if abs(fm) < tol:
            return mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2
