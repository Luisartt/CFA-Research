"""Compare the team's DCF models and value the consolidated input set.

The teammates' workbooks (valuation/team-models/) use the S&P Capital IQ "DCF Analysis"
template: FY2026E-FY2030E, a stub for the rest of 2026, mid-period discounting and an exit
EV/EBITDA multiple on FY2030 EBITDA. Alejandro's copy carries the v3 inputs; Diego's carries
his own. This script
  1. reads each workbook's inputs and results (cached values, nothing is recalculated there),
  2. replicates the template mechanics and checks the replica against each workbook,
  3. walks Alejandro's value to Diego's, one change at a time (exit method),
  4. values the consolidated set: judgments averaged, facts and mechanics reconciled,
  5. writes valuation/inputs/consolidated_results.json for the workbook builder and the write-up.

Usage (from the project folder): python -I valuation/build/consolidate_models.py --project .
"""

from __future__ import annotations

import argparse
import copy
import json
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path

import openpyxl
import yaml

FCST = ["N", "O", "P", "Q", "R"]  # FY2026E..FY2030E in the S&P template
YEARS = [2026, 2027, 2028, 2029, 2030]
DAYS = 365.0
ALE_FILE = "valuation/team-models/Bimbo_DCF_Alejandro.xlsm"
DIEGO_FILE = "valuation/team-models/SPG_DCF_independent_Diego.xlsm"
OUT_FILE = "valuation/inputs/consolidated_results.json"
CORE_FOUR = ["FLO", "GRUMA", "YMZ", "ARYN"]  # Diego's core group (his Multiples_Summary rows 4-7)
PRICE = 58.60
DPS_NEXT = 1.05  # consensus DPS FY2027E (valuation-outputs.yaml); the FY2026 dividend was paid 13-May-2026
TOL = 0.005  # MXN per share: replica must match each workbook to half a centavo
CIQ_DERIVATIVES = 2658.4  # hedging and derivative adjustments inside CIQ total debt 189,679.4 at Jun-26
#                           (wiki/Valuation/ciq-debt-stack-and-maturity-ladder.md, reconciliation table)


@dataclass
class State:
    label: str
    rev0: float
    growth: list
    ebitda_m: list
    da_pct: list
    capex_pct: list  # capex excluding new leases / revenue
    lease_mode: str  # "liability": principal + growth in the lease liability (v3); "given": lease_pct
    lease_pct: list
    lease_principal: float
    lease_liab: float
    wc_pct: list  # change in working capital / revenue, + = releases cash
    tax_ebit: float
    rf: float
    erp: float
    crp: float
    beta_u: float
    de: float
    kd: float
    tax_marg: float
    exit_mult: float
    g: float
    stub_days: int
    roll_days: int
    debt: float  # financial debt + lease liabilities
    cash: float
    nci_mode: str  # "market" = NCI income / (ke - growth); "book"
    nci_book: float
    nci_income: float
    nci_growth: float
    assoc_net: float  # associates - seasonal income tax payable
    other_claims: float  # pensions, provisions, derivatives: Gordon only (peer EVs exclude them)
    shares: float  # millions
    ronic: float | None = None  # terminal return on new capital for the consistent Gordon
    wacc_fixed: float | None = None  # replica of a workbook: use its own WACC cell
    ke_fixed: float | None = None


def ke_wacc(s: State) -> tuple[float, float, float]:
    beta_l = s.beta_u * (1 + (1 - s.tax_marg) * s.de)
    ke = s.rf + beta_l * s.erp + s.crp
    wd = s.de / (1 + s.de)
    wacc = (1 - wd) * ke + wd * s.kd * (1 - s.tax_marg)
    if s.ke_fixed is not None:
        ke = s.ke_fixed
    if s.wacc_fixed is not None:
        wacc = s.wacc_fixed
    return ke, wacc, beta_l


def run(s: State, wacc_shift: float = 0.0) -> dict:
    rev, prev = [], s.rev0
    for gr in s.growth:
        prev *= 1 + gr
        rev.append(prev)
    prevs = [s.rev0] + rev[:-1]
    ebitda = [r * m for r, m in zip(rev, s.ebitda_m)]
    da = [r * p for r, p in zip(rev, s.da_pct)]
    ebit = [e - d for e, d in zip(ebitda, da)]
    tax = [s.tax_ebit * e for e in ebit]
    nopat = [e - t for e, t in zip(ebit, tax)]
    capex = [r * c for r, c in zip(rev, s.capex_pct)]
    if s.lease_mode == "liability":
        leases = [s.lease_principal * r + s.lease_liab * (r - p) for r, p in zip(rev, prevs)]
    else:
        leases = [r * lp for r, lp in zip(rev, s.lease_pct)]
    dwc = [r * w for r, w in zip(rev, s.wc_pct)]
    fcff = [n + d - c - l_ + w for n, d, c, l_, w in zip(nopat, da, capex, leases, dwc)]

    ke, wacc, beta_l = ke_wacc(s)
    wacc += wacc_shift
    t0 = s.stub_days / DAYS
    expo = [t0 / 2] + [t0 + 0.5 + k for k in range(4)]
    pv = [fcff[0] * t0 / (1 + wacc) ** expo[0]] + [fcff[k] / (1 + wacc) ** expo[k] for k in range(1, 5)]
    t_tv = t0 + 4
    df_tv = (1 + wacc) ** t_tv
    pv_explicit = sum(pv)

    tv_exit = ebitda[-1] * s.exit_mult
    ev_exit = pv_explicit + tv_exit / df_tv
    implied_g_exit = (tv_exit * wacc - fcff[-1]) / (tv_exit + fcff[-1])

    tv_naive = fcff[-1] * (1 + s.g) / (wacc - s.g)
    ev_naive = pv_explicit + tv_naive / df_tv
    reinvest = capex[-1] + leases[-1] - da[-1] - dwc[-1]
    reinvest_rate = reinvest / nopat[-1]
    ronic_naive = s.g / reinvest_rate if reinvest_rate > 0 else None

    def ev_ronic(ronic: float) -> float:
        fcff_next = nopat[-1] * (1 + s.g) * (1 - s.g / ronic)
        return pv_explicit + fcff_next / (wacc - s.g) / df_tv

    nci = s.nci_book if s.nci_mode == "book" else s.nci_income / (ke - s.nci_growth)
    claims_exit = -s.debt + s.cash - nci + s.assoc_net
    claims_gordon = claims_exit - s.other_claims
    roll = (1 + ke) ** (s.roll_days / DAYS)

    def ps(ev: float, claims: float) -> float:
        return (ev + claims) / s.shares * roll

    out = {
        "rev": rev, "ebitda": ebitda, "da": da, "ebit": ebit, "tax": tax, "nopat": nopat, "capex": capex,
        "leases": leases, "dwc": dwc, "fcff": fcff, "pv": pv,
        "ke": ke, "wacc": wacc, "beta_l": beta_l, "nci": nci, "roll": roll,
        "pv_explicit": pv_explicit, "pv_tv_exit": tv_exit / df_tv, "ev_exit": ev_exit,
        "tv_share_exit": (tv_exit / df_tv) / ev_exit, "implied_g_exit": implied_g_exit,
        "equity_exit_anchor": ev_exit + claims_exit, "ps_anchor_exit": (ev_exit + claims_exit) / s.shares,
        "ps_exit": ps(ev_exit, claims_exit),
        "ev_gordon_naive": ev_naive, "ps_gordon_naive": ps(ev_naive, claims_gordon),
        "ronic_naive": ronic_naive, "reinvest_rate_2030": reinvest_rate,
        "implied_mult_gordon_naive": tv_naive / ebitda[-1],
        "claims_exit": claims_exit, "claims_gordon": claims_gordon,
    }
    if s.ronic:
        ev_r = ev_ronic(s.ronic)
        out["ev_gordon_ronic"] = ev_r
        out["ps_gordon_ronic"] = ps(ev_r, claims_gordon)
    out["ps_gordon_ronic_wacc"] = ps(ev_ronic(wacc), claims_gordon)
    for key in ("ps_exit", "ps_gordon_naive", "ps_gordon_ronic"):
        if key in out:
            target = out[key] * (1 + ke) - DPS_NEXT
            out[key.replace("ps_", "target12m_")] = target
            out[key.replace("ps_", "exp_return_")] = target / PRICE - 1 + DPS_NEXT / PRICE
    return out


# ---------------------------------------------------------------- readers


def _v(ws, addr: str):
    return ws[addr].value


def _row(ws, r: int) -> list:
    return [ws[f"{c}{r}"].value for c in FCST]


def read_template(path: Path) -> dict:
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb["DCF"]
    rev = _row(ws, 105)
    d = {
        "rev0": _v(ws, "M105"), "rev": rev, "growth": _row(ws, 106), "ebitda_m": _row(ws, 111),
        "da": _row(ws, 112), "ebit": _row(ws, 114), "tax": [-t for t in _row(ws, 117)],
        "capex_lease": [-c for c in _row(ws, 120)], "dwc": _row(ws, 123), "fcff": _row(ws, 133),
        "rf": _v(ws, "F52"), "rm": _v(ws, "F54"), "wd": _v(ws, "F55"), "de": _v(ws, "F56"), "crp": _v(ws, "F58"),
        "kd": _v(ws, "F60"), "tax_marg": _v(ws, "F50"), "beta_l": _v(ws, "F73"), "ke": _v(ws, "F77"),
        "wacc": _v(ws, "F91"), "exit_mult": _v(ws, "R144"), "implied_g": _v(ws, "R146"), "stub_days": _v(ws, "AA156"),
        "pv_stub": _v(ws, "I142"), "pv_mid": _v(ws, "I143"), "pv_tv": _v(ws, "I144"), "ev": _v(ws, "I145"),
        "bridge_debt": _v(ws, "I147"), "bridge_nci": _v(ws, "I149"), "bridge_plus": _v(ws, "I150"),
        "bridge_cash": _v(ws, "I151"), "equity": _v(ws, "I152"), "shares": _v(ws, "I154"), "ps_anchor": _v(ws, "I155"),
    }
    d["da_pct"] = [a / r for a, r in zip(d["da"], rev)]
    d["capex_lease_pct"] = [c / r for c, r in zip(d["capex_lease"], rev)]
    d["wc_pct"] = [w / r for w, r in zip(d["dwc"], rev)]
    d["tax_ebit"] = [t / e for t, e in zip(d["tax"], d["ebit"])]
    return d, wb


def read_ale(project: Path) -> dict:
    d, wb = read_template(project / ALE_FILE)
    su, dat = wb["Supuestos_DCF"], wb["Datos_Bimbo"]
    d.update({
        "capex_pct": [su[f"{c}50"].value for c in "CDEFG"],
        "lease_pct_sheet": [su[f"{c}51"].value for c in "CDEFG"],
        "beta_u": su["B20"].value, "g": su["B10"].value, "nci_growth": su["B12"].value,
        "roll": su["B64"].value, "ps_exit": su["B65"].value, "ps_gordon": su["B85"].value,
        "ronic_gordon": su["B90"].value, "nci_market": su["B26"].value, "assoc_net": su["B27"].value,
        "other_claims": -su["B81"].value, "fcff_v3": [su[f"{c}56"].value for c in "CDEFG"],
        "price": dat["D9"].value, "shares_m": dat["D10"].value, "fin_debt": dat["D13"].value,
        "leases_bs": dat["D14"].value, "total_debt": dat["D15"].value, "cash": dat["D16"].value,
        "nci_book": dat["D17"].value, "nci_income": dat["D18"].value, "assoc": dat["D19"].value,
        "tax_seasonal": dat["D20"].value, "debt_like": dat["D21"].value,
        "v3_gordon_ref": su["B114"].value, "v3_exit_ref": su["B115"].value,
    })
    d["lease_pct"] = [cl - c for cl, c in zip(d["capex_lease_pct"], d["capex_pct"])]
    return d


def read_diego(project: Path) -> dict:
    d, wb = read_template(project / DIEGO_FILE)
    ins = wb["Independent_DCF_Inputs"]
    d.update({
        "capex_pct": [ins[f"{c}27"].value for c in "BCDEF"], "lease_principal": ins["B20"].value,
        "beta_u": ins["B11"].value, "g": ins["B19"].value, "market_cap": ins["B12"].value,
        "debt_ciq": ins["B13"].value, "cash_ciq": ins["B14"].value, "nci_book": ins["B15"].value,
        "shares_m": ins["B16"].value / 1e6, "exit_note": ins["D18"].value,
    })
    d["lease_pct"] = [cl - c for cl, c in zip(d["capex_lease_pct"], d["capex_pct"])]
    return d


def read_peers(project: Path) -> dict:
    y = yaml.safe_load((project / "valuation/inputs/peers.yaml").read_text(encoding="utf-8"))
    by = {p["key"]: p for p in y["peers"]}
    clean = {k: by[k]["ev"] / by[k]["ebitda_ltm"] for k in CORE_FOUR}
    return {"clean_ltm": clean, "clean_median": statistics.median(clean.values()),
            "diego_raw": {"FLO": 6.67632, "GRUMA": 6.013367, "YMZ": 6.064346, "ARYN": 8.333201},
            "diego_raw_median": 6.370333}


def read_v3(project: Path) -> dict:
    y = yaml.safe_load((project / "valuation/valuation-outputs.yaml").read_text(encoding="utf-8"))
    p = y["published"]
    return {"gordon": p["value_today_gordon"]["value"], "exit": p["value_today_exit"]["value"],
            "gordon_12m": p["value_12m_gordon"]["value"], "wacc": p["wacc"], "ke": p["cost_of_equity"],
            "ronic": p["tv_ronic"]["value"], "g": p["terminal_growth"], "exit_mult": p["exit_multiple"],
            "comps_core": p["comps_indicative"]["core_bakery_5_53x"],
            "comps_all": p["comps_indicative"]["all_eligible_8_27x"]}


# ---------------------------------------------------------------- states


def ale_state(a: dict) -> State:
    return State(
        label="Alejandro (v3 inputs, S&P template)", rev0=a["rev0"], growth=a["growth"], ebitda_m=a["ebitda_m"],
        da_pct=a["da_pct"], capex_pct=a["capex_pct"], lease_mode="given", lease_pct=a["lease_pct"],
        lease_principal=0.0139, lease_liab=0.0, wc_pct=a["wc_pct"], tax_ebit=a["tax_ebit"][0],
        rf=a["rf"], erp=a["rm"] - a["rf"], crp=a["crp"], beta_u=a["beta_u"], de=a["de"], kd=a["kd"],
        tax_marg=a["tax_marg"], exit_mult=a["exit_mult"], g=a["g"], stub_days=a["stub_days"], roll_days=108,
        debt=-a["bridge_debt"], cash=a["bridge_cash"], nci_mode="market", nci_book=a["nci_book"],
        nci_income=a["nci_income"], nci_growth=a["nci_growth"], assoc_net=a["bridge_plus"],
        other_claims=a["other_claims"], shares=a["shares"], wacc_fixed=a["wacc"], ke_fixed=a["ke"])


def diego_state(d: dict) -> State:
    return State(
        label="Diego (independent, S&P template)", rev0=d["rev0"], growth=d["growth"], ebitda_m=d["ebitda_m"],
        da_pct=d["da_pct"], capex_pct=d["capex_pct"], lease_mode="given", lease_pct=d["lease_pct"],
        lease_principal=d["lease_principal"], lease_liab=0.0, wc_pct=d["wc_pct"], tax_ebit=d["tax_ebit"][0],
        rf=d["rf"], erp=d["rm"] - d["rf"], crp=d["crp"], beta_u=d["beta_u"], de=d["de"], kd=d["kd"],
        tax_marg=d["tax_marg"], exit_mult=d["exit_mult"], g=d["g"], stub_days=d["stub_days"], roll_days=0,
        debt=-d["bridge_debt"], cash=d["bridge_cash"], nci_mode="book", nci_book=-d["bridge_nci"],
        nci_income=1814.0, nci_growth=0.03, assoc_net=0.0, other_claims=0.0, shares=d["shares"],
        wacc_fixed=d["wacc"], ke_fixed=d["ke"])


def lease_liability_ratio(a: dict) -> float:
    """Back out the v3 lease-liability share of revenue from Alejandro's FY2027-30 new-lease path."""
    ratios = []
    rev = a["rev"]
    for k in range(1, 5):
        ratios.append((a["lease_pct"][k] - 0.0139) * rev[k] / (rev[k] - rev[k - 1]))
    return statistics.mean(ratios), max(ratios) - min(ratios)


def blend(x_v3, x_diego, w: float):
    if isinstance(x_v3, list):
        return [w * a + (1 - w) * b for a, b in zip(x_v3, x_diego)]
    return w * x_v3 + (1 - w) * x_diego


def consolidated_state(a: dict, d: dict, peers: dict, v3: dict, *, w: float = 0.5, multiple_basis: str = "clean",
                       nci_mode: str = "market", tax_ebit: float | None = None) -> State:
    liab, _ = lease_liability_ratio(a)
    diego_mult = peers["clean_median"] if multiple_basis == "clean" else d["exit_mult"]
    de_fact = a["total_debt"] / (a["price"] * a["shares_m"])
    return State(
        label=f"Consolidated (w_v3={w:.4f}, multiple={multiple_basis}, NCI={nci_mode})",
        rev0=a["rev0"], growth=blend(a["growth"], d["growth"], w), ebitda_m=blend(a["ebitda_m"], d["ebitda_m"], w),
        # D&A is a mechanic, not a judgment: Diego's path is the template's (D&A rising to 100% of capex + leases by
        # FY2030, i.e. no net investment while revenue grows ~4%), so the v3 path (share of revenue) is used for all w.
        da_pct=list(a["da_pct"]), capex_pct=blend(a["capex_pct"], d["capex_pct"], w),
        lease_mode="liability", lease_pct=[0.0] * 5, lease_principal=0.0139, lease_liab=liab,
        wc_pct=blend(a["wc_pct"], d["wc_pct"], w),
        tax_ebit=blend(a["tax_ebit"][0], d["tax_ebit"][0], w) if tax_ebit is None else tax_ebit,
        rf=a["rf"], erp=a["rm"] - a["rf"], crp=a["crp"], beta_u=blend(a["beta_u"], d["beta_u"], w), de=de_fact,
        kd=a["kd"], tax_marg=a["tax_marg"], exit_mult=blend(v3["exit_mult"], diego_mult, w),
        g=blend(a["g"], d["g"], w), stub_days=a["stub_days"], roll_days=108,
        debt=a["total_debt"], cash=a["cash"], nci_mode=nci_mode, nci_book=a["nci_book"], nci_income=a["nci_income"],
        nci_growth=a["nci_growth"], assoc_net=a["assoc"] - a["tax_seasonal"], other_claims=a["debt_like"],
        shares=a["shares_m"], ronic=v3["ronic"])


# ---------------------------------------------------------------- walk Alejandro -> Diego


def walk(a: dict, d: dict) -> list[dict]:
    s = ale_state(a)
    steps = [("Alejandro: v3 inputs on the S&P template (30-Jun anchor, rolled to 16-Oct at ke)", None)]

    def timing(x):
        x.stub_days, x.roll_days = d["stub_days"], 0

    def fx_debt(x):
        x.debt, x.cash = d["debt_ciq"], d["cash_ciq"]

    def derivatives(x):
        x.debt = a["total_debt"] + CIQ_DERIVATIVES

    def shares(x):
        x.shares = d["shares"]

    def assoc(x):
        x.assoc_net = 0.0

    def nci(x):
        x.nci_mode, x.nci_book = "book", -d["bridge_nci"]

    def wacc(x):
        x.wacc_fixed, x.ke_fixed, x.beta_u, x.de = d["wacc"], d["ke"], d["beta_u"], d["de"]

    def growth(x):
        x.growth = d["growth"]

    def margin(x):
        x.ebitda_m = d["ebitda_m"]

    def da(x):
        x.da_pct = d["da_pct"]

    def capex(x):
        x.capex_pct = d["capex_pct"]

    def leases(x):
        x.lease_pct = d["lease_pct"]

    def wc(x):
        x.wc_pct = d["wc_pct"]

    def tax(x):
        x.tax_ebit = d["tax_ebit"][0]

    def mult(x):
        x.exit_mult = d["exit_mult"]

    plan = [
        ("Valuation date: 76-day stub discounted from 16-Oct, balance sheet still 30-Jun (no roll-forward)", timing),
        ("Debt: add derivative liabilities that sit inside Capital IQ total debt (+2,658)", derivatives),
        ("Debt and cash: US$ figures reconverted at 17.96 MXN/US$; CIQ's own peso and dollar figures imply 17.47", fx_debt),
        ("Shares: Capital IQ 4,296.3m instead of the BMV notice 4,294.9m", shares),
        ("Bridge: drop associates (+6,498) and the seasonal tax payable (-4,538)", assoc),
        ("NCI at book (743) instead of market value (18,243)", nci),
        ("WACC 10.32% -> 10.40% (unlevered beta 0.53 -> 0.56; D/E 0.743 -> 0.774)", wacc),
        ("Revenue path: v3 regional build -> Capital IQ consensus + fade", growth),
        ("EBITDA margin path: v3 (to 15.3%) -> consensus (held at 14.7%)", margin),
        ("D&A path: v3 (5.85-5.9% of sales) -> template mechanics (D&A rises to 100% of capex + leases)", da),
        ("Capex excluding leases: v3 (4.6% -> 5.5%) -> consensus (5.2% -> 4.8%)", capex),
        ("New leases: principal + growth in the liability -> principal only (1.39%)", leases),
        ("Working capital path", wc),
        ("Tax on EBIT 34% (effective) -> 30% (statutory)", tax),
        ("Exit multiple 6.0x -> 6.4x", mult),
    ]
    rows = []
    prev = run(s)["ps_exit"]
    rows.append({"step": steps[0][0], "value": prev, "delta": None})
    for label, fn in plan:
        fn(s)
        v = run(s)["ps_exit"]
        rows.append({"step": label, "value": v, "delta": v - prev})
        prev = v
    return rows


def judgment_walk(a: dict, d: dict, peers: dict, v3: dict) -> list[dict]:
    """v3 set -> Diego set on the same facts and mechanics: where the two analysts really differ."""
    s = consolidated_state(a, d, peers, v3, w=1.0)
    end = consolidated_state(a, d, peers, v3, w=0.0)
    plan = [
        ("Unlevered beta 0.53 -> 0.56 (WACC 10.32% -> 10.43%)", ["beta_u"]),
        ("Revenue path: v3 regional build -> consensus + fade", ["growth"]),
        ("EBITDA margin path: v3 (to 15.3%) -> consensus (held at 14.7%)", ["ebitda_m"]),
        ("Capex excluding leases: v3 (4.6% -> 5.5%) -> consensus (5.2% -> 4.8%)", ["capex_pct"]),
        ("Working capital path", ["wc_pct"]),
        ("Tax on EBIT 34% -> 30%", ["tax_ebit"]),
        ("Exit multiple 6.0x -> 5.83x (Diego's core-median rule on lease-consistent peer data)", ["exit_mult"]),
        ("Terminal growth 4.25% -> 4.00% (Gordon only)", ["g"]),
    ]
    rows = []
    r0 = run(s)
    rows.append({"step": "v3 set on reconciled facts and mechanics (= Alejandro)", "exit": r0["ps_exit"],
                 "gordon_ronic": r0["ps_gordon_ronic"], "d_exit": None, "d_gordon": None})
    for label, fields in plan:
        for f in fields:
            setattr(s, f, copy.deepcopy(getattr(end, f)))
        r = run(s)
        rows.append({"step": label, "exit": r["ps_exit"], "gordon_ronic": r["ps_gordon_ronic"],
                     "d_exit": r["ps_exit"] - rows[-1]["exit"], "d_gordon": r["ps_gordon_ronic"] - rows[-1]["gordon_ronic"]})
    return rows


# ---------------------------------------------------------------- reverse DCF helpers


def solve(fn, lo: float, hi: float, target: float, tol: float = 1e-9) -> float | None:
    flo, fhi = fn(lo) - target, fn(hi) - target
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = fn(mid) - target
        if abs(fm) < tol:
            return mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def reverse(base: State) -> dict:
    def with_mult(m):
        s = copy.deepcopy(base)
        s.exit_mult = m
        return run(s)["ps_exit"]

    def with_shift(dw):
        return run(base, wacc_shift=dw)["ps_exit"]

    def with_growth(dg):
        s = copy.deepcopy(base)
        s.growth = [x + dg for x in base.growth]
        return run(s)["ps_exit"]

    w0 = run(base)["wacc"]
    shift = solve(with_shift, -0.05, 0.05, PRICE)
    return {"exit_multiple_for_price": solve(with_mult, 3.0, 15.0, PRICE),
            "wacc_for_price_exit": None if shift is None else w0 + shift,
            "growth_shift_for_price_exit": solve(with_growth, -0.05, 0.10, PRICE)}


# ---------------------------------------------------------------- levers (risk and ESG)


def levers(base: State) -> list[dict]:
    b = run(base)
    rows = []

    def add(label, theme, s=None, wacc_shift=0.0, claim=0.0):
        r = run(s or base, wacc_shift=wacc_shift)
        ex = r["ps_exit"] - b["ps_exit"] - claim / base.shares * b["roll"]
        go = r.get("ps_gordon_ronic", 0) - b.get("ps_gordon_ronic", 0) - claim / base.shares * b["roll"]
        rows.append({"lever": label, "theme": theme, "d_exit": ex, "d_gordon_ronic": go})

    for label, theme, field_, delta in [
        ("EBITDA margin -50 bp every year", "Wheat and climate input costs (gross margin)", "ebitda_m", -0.005),
        ("EBITDA margin +50 bp every year", "Productivity plan delivers more", "ebitda_m", 0.005),
        ("Capex +50 bp of revenue every year", "Water stress and decarbonisation capex", "capex_pct", 0.005),
        ("Revenue growth -50 bp every year", "Front-of-pack labels, school-food rules, GLP-1 volumes", "growth", -0.005),
    ]:
        s = copy.deepcopy(base)
        setattr(s, field_, [x + delta for x in getattr(base, field_)])
        add(label, theme, s)
    s = copy.deepcopy(base)
    s.exit_mult -= 0.5
    add("Exit multiple -0.5x", "Controlled-company governance discount widens", s)
    add("WACC +50 bp", "Country and currency risk (not ESG)", wacc_shift=0.005)
    add("One-off claim of MXN 1bn", "Litigation (Canada Bread class actions) or tax disputes; per MXN 1bn", claim=1000.0)
    s = copy.deepcopy(base)
    rev, prev = [], base.rev0
    for gr in base.growth:
        prev *= 1 + gr
        rev.append(prev)
    cut = [0.0] + [1000.0 / r for r in rev[1:]]  # MXN 1bn a year from FY2027, as a share of revenue
    s.ebitda_m = [m - c for m, c in zip(base.ebitda_m, cut)]
    add("Recurring cost of MXN 1bn a year from FY2027 (pre-tax)", "Carbon price (Mexican ETS) or packaging EPR fees; per MXN 1bn a year", s)
    # Bimbo 23L step-up: +25 bp on MXN 12,000m from 21-Nov-2031 to 20-May-2033 (1.5 years), after tax, at Kd
    step = 12000 * 0.0025 * (1 - base.tax_marg)
    pv = sum(step / 2 / (1 + base.kd) ** t for t in (5.65, 6.15, 6.65))  # half-years after 30-Jun-2026
    rows.append({"lever": "Bimbo 23L coupon step-up (Scope 3 target missed in 2030)", "theme": "Scope 3 / SBTi",
                 "d_exit": -pv / base.shares * b["roll"], "d_gordon_ronic": -pv / base.shares * b["roll"]})
    return rows


# ---------------------------------------------------------------- sensitivity grids


def grids(base: State) -> dict:
    b = run(base)
    waccs = [-0.01, -0.005, 0.0, 0.005, 0.01]
    mults = [5.0, 5.5, base.exit_mult, 6.5, 7.0]
    exit_grid = []
    for dw in waccs:
        row = []
        for m in mults:
            s = copy.deepcopy(base)
            s.exit_mult = m
            row.append(run(s, wacc_shift=dw)["ps_exit"])
        exit_grid.append(row)
    gs = [base.g + x for x in (-0.01, -0.005, 0.0, 0.005, 0.01)]
    gordon_grid = []
    for dw in waccs:
        row = []
        for g in gs:
            s = copy.deepcopy(base)
            s.g = g
            row.append(run(s, wacc_shift=dw)["ps_gordon_ronic"])
        gordon_grid.append(row)
    return {"wacc": [b["wacc"] + x for x in waccs], "mults": mults, "exit": exit_grid, "g": gs, "gordon_ronic": gordon_grid,
            "note": "NCI claim and the 30-Jun -> 16-Oct roll factor held at the base cost of equity"}


# ---------------------------------------------------------------- main


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=".")
    args = ap.parse_args(argv)
    project = Path(args.project).resolve()

    a, d = read_ale(project), read_diego(project)
    peers, v3 = read_peers(project), read_v3(project)

    # 1. replica checks
    ra, rd = run(ale_state(a)), run(diego_state(d))
    sa = ale_state(a)
    sa.ronic = None
    checks = {
        "ale_exit": {"replica": ra["ps_exit"], "workbook": a["ps_exit"]},
        "ale_gordon": {"replica": ra["ps_gordon_naive"], "workbook": a["ps_gordon"]},
        "ale_ev": {"replica": ra["ev_exit"], "workbook": a["ev"]},
        "ale_fcff_sum": {"replica": sum(ra["fcff"]), "workbook": sum(a["fcff"])},
        "ale_fcff_vs_v3": {"replica": sum(a["fcff"]), "workbook": sum(a["fcff_v3"])},
        "diego_exit": {"replica": rd["ps_exit"], "workbook": d["ps_anchor"]},
        "diego_ev": {"replica": rd["ev_exit"], "workbook": d["ev"]},
        "diego_fcff_sum": {"replica": sum(rd["fcff"]), "workbook": sum(d["fcff"])},
    }
    wa_calc = ke_wacc(State(**{**asdict(sa), "wacc_fixed": None, "ke_fixed": None}))[1]
    sd = diego_state(d)
    wd_calc = ke_wacc(State(**{**asdict(sd), "wacc_fixed": None, "ke_fixed": None}))[1]
    checks["ale_wacc_from_inputs"] = {"replica": wa_calc, "workbook": a["wacc"]}
    checks["diego_wacc_from_inputs"] = {"replica": wd_calc, "workbook": d["wacc"]}
    liab, spread = lease_liability_ratio(a)
    lease_check = []
    prevs = [a["rev0"]] + a["rev"][:-1]
    for k in range(5):
        lease_check.append(0.0139 + liab * (a["rev"][k] - prevs[k]) / a["rev"][k] - a["lease_pct"][k])
    checks["v3_lease_mechanics_max_gap"] = {"replica": max(abs(x) for x in lease_check), "workbook": 0.0}
    failed = []
    for k, c in checks.items():
        c["diff"] = c["replica"] - c["workbook"]
        tol = TOL if k.endswith(("exit", "gordon")) else (1.0 if "ev" in k or "fcff" in k else 1e-6)
        c["ok"] = abs(c["diff"]) <= tol
        if not c["ok"]:
            failed.append(k)

    # 2. walk
    w_rows = walk(a, d)
    walk_gap = w_rows[-1]["value"] - d["ps_anchor"]

    # 3. consolidated
    base = consolidated_state(a, d, peers, v3)
    rb = run(base)
    variants = {}
    for key, kw in {
        "base": {},
        "three_model_weights": {"w": 2 / 3},
        "raw_multiple_6_2x": {"multiple_basis": "raw"},
        "nci_at_book": {"nci_mode": "book"},
        "tax_34pct": {"tax_ebit": a["tax_ebit"][0]},
        "tax_30pct": {"tax_ebit": d["tax_ebit"][0]},
        "v3_set_only": {"w": 1.0},
        "diego_set_reconciled": {"w": 0.0},
        "diego_set_reconciled_raw_multiple": {"w": 0.0, "multiple_basis": "raw"},
    }.items():
        st = consolidated_state(a, d, peers, v3, **kw)
        r = run(st)
        variants[key] = {"label": st.label, "exit_mult": st.exit_mult, "g": st.g, "beta_u": st.beta_u,
                         "tax_ebit": st.tax_ebit, "wacc": r["wacc"], "ke": r["ke"], "ps_exit": r["ps_exit"],
                         "ps_gordon_ronic": r["ps_gordon_ronic"], "ps_gordon_naive": r["ps_gordon_naive"],
                         "ps_gordon_ronic_wacc": r["ps_gordon_ronic_wacc"], "ronic_naive": r["ronic_naive"],
                         "implied_g_exit": r["implied_g_exit"], "target12m_exit": r["target12m_exit"],
                         "exp_return_exit": r["exp_return_exit"], "target12m_gordon_ronic": r["target12m_gordon_ronic"],
                         "exp_return_gordon_ronic": r["exp_return_gordon_ronic"]}

    result = {
        "as_of": "2026-10-19",
        "price": PRICE, "dps_next": DPS_NEXT,
        "sources": {"alejandro": ALE_FILE, "diego": DIEGO_FILE, "v3": "valuation/valuation-outputs.yaml",
                    "peers": "valuation/inputs/peers.yaml"},
        "checks": checks, "checks_failed": failed, "walk_closes_to_diego": walk_gap,
        "inputs": {
            "alejandro": {k: a[k] for k in ("growth", "ebitda_m", "da_pct", "capex_pct", "lease_pct", "wc_pct", "tax_ebit",
                                            "beta_u", "de", "wacc", "ke", "exit_mult", "g", "stub_days", "rev", "fcff",
                                            "rf", "rm", "crp", "kd", "tax_marg", "beta_l", "wd", "ebitda_m", "capex_lease_pct",
                                            "nci_market", "assoc_net", "other_claims", "shares", "bridge_debt", "bridge_cash",
                                            "roll", "ronic_gordon", "implied_g", "ev", "pv_tv")},
            "diego": {k: d[k] for k in ("growth", "ebitda_m", "da_pct", "capex_pct", "lease_pct", "wc_pct", "tax_ebit",
                                        "beta_u", "de", "wacc", "ke", "exit_mult", "g", "stub_days", "rev", "fcff",
                                        "debt_ciq", "cash_ciq", "shares_m", "nci_book", "rf", "rm", "crp", "kd", "tax_marg",
                                        "beta_l", "wd", "capex_lease_pct", "lease_principal", "implied_g", "ev", "pv_tv",
                                        "market_cap")},
            "facts": {k: a[k] for k in ("price", "shares_m", "fin_debt", "leases_bs", "total_debt", "cash", "nci_book",
                                        "nci_income", "assoc", "tax_seasonal", "debt_like", "rev0")},
            "lease_liability_ratio": liab, "lease_liability_ratio_spread": spread,
            "peers": peers, "v3": v3,
        },
        "results": {
            "alejandro": {"ps_exit": a["ps_exit"], "ps_gordon": a["ps_gordon"], "wacc": a["wacc"], "ke": a["ke"],
                          "ronic_gordon": a["ronic_gordon"], "implied_g_exit": a["implied_g"], "ev": a["ev"]},
            "diego": {"ps_exit": d["ps_anchor"], "wacc": d["wacc"], "ke": d["ke"], "implied_g_exit": d["implied_g"],
                      "ev": d["ev"]},
            "v3": v3,
        },
        "walk": w_rows,
        "judgment_walk": judgment_walk(a, d, peers, v3),
        "consolidated": {"state": asdict(base), "run": {k: v for k, v in rb.items()}, "variants": variants,
                         "reverse": reverse(base), "levers": levers(base), "grids": grids(base)},
    }
    out = project / OUT_FILE
    out.write_text(json.dumps(result, indent=1, default=float), encoding="utf-8")

    print("checks:", "all OK" if not failed else f"FAILED {failed}")
    for k, c in checks.items():
        print(f"  {k:<28} replica {c['replica']:>14.6f}  workbook {c['workbook']:>14.6f}  diff {c['diff']:+.2e}  {'OK' if c['ok'] else 'FAIL'}")
    print(f"walk Alejandro -> Diego closes with gap {walk_gap:+.2e}")
    for r in w_rows:
        dl = "" if r["delta"] is None else f"{r['delta']:+7.2f}"
        print(f"  {r['value']:7.2f} {dl:>8}  {r['step']}")
    print(f"consolidated: WACC {rb['wacc']:.4%} ke {rb['ke']:.4%} exit {base.exit_mult:.3f}x g {base.g:.3%}")
    for k, v in variants.items():
        print(f"  {k:<36} exit {v['ps_exit']:6.2f}  gordon@RONIC {v['ps_gordon_ronic']:6.2f}  naive {v['ps_gordon_naive']:6.2f}"
              f" (RONIC {v['ronic_naive']:.1%})  WACC {v['wacc']:.3%}  ER exit {v['exp_return_exit']:+.1%}")
    print("wrote", out)
    return 1 if failed or abs(walk_gap) > 1e-6 else 0


if __name__ == "__main__":
    raise SystemExit(main())
