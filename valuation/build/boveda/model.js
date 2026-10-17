/* Boveda Vision - DCF engine for the page (mirrors valuation/build/dcf_core.py, engine and published bases). */
(function (root) {
  "use strict";
  var DAYS = 365;

  function defaults(D) {
    var w = D.valuation.wacc;
    return {
      route: D.valuation.base_route || "A", beta: w.beta_u, de: w.de, kd: w.kd, erp: w.erp,
      g: D.valuation.g, exitMultiple: D.valuation.exit_multiple,
      capexShift: 0, gmShift: 0, opexShift: 0, growthShift: 0,
      lease: "published", exitClaims: "peer", nci: "g3", provisions: true,
      tvMethod: "fcff", ronic: 0.15, weightGordon: 0.5
    };
  }

  function costOfCapital(D, o) {
    var route = D.options.route[o.route] || D.options.route.A;
    var t = D.valuation.wacc.tax;
    var betaL = o.beta * (1 + (1 - t) * o.de);
    var ke = route.rf + betaL * o.erp + route.crp;
    var kdA = o.kd * (1 - t);
    var we = 1 / (1 + o.de), wd = o.de / (1 + o.de);
    return { rf: route.rf, crp: route.crp, betaL: betaL, ke: ke, kdA: kdA, we: we, wd: wd, wacc: we * ke + wd * kdA };
  }

  function forecast(D, o) {
    var n = D.years.fcst.length, dr = D.drivers, f0 = D.fy_last;
    var segs = D.segments.map(function (s) { return s.fy_last; });
    var prevRev = f0.revenue, leasePrev = f0.lease_liabilities;
    var prev = { ar: f0.receivables, inv: f0.inventory, oca: f0.other_current_assets,
                 ap: f0.payables, ocl: f0.other_current_liabilities };
    var L = { revenue: [], ebit: [], ebitda: [], nopat: [], capex: [], fcff: [], fcffPub: [], leaseLiab: [], leaseGrowth: [] };
    for (var i = 0; i < n; i++) {
      var rev = 0;
      for (var j = 0; j < D.segments.length; j++) {
        segs[j] = segs[j] * (1 + D.segments[j].growth[i] + o.growthShift);
        rev += segs[j];
      }
      var gm = dr.gross_margin[i] + o.gmShift;
      var cogs = rev * (1 - gm);
      var ebit = rev - cogs - rev * (dr.opex_pct_revenue[i] + o.opexShift);
      var da = rev * dr.da_pct_revenue[i];
      var nopat = ebit - ebit * dr.tax_rate[i];
      var capex = rev * (dr.capex_pct_revenue[i] + o.capexShift);
      var newLeases = rev * dr.lease_principal_pct_revenue[i];
      var bal = { ar: rev * dr.dso[i] / DAYS, inv: cogs * dr.dio[i] / DAYS, oca: rev * dr.other_ca_pct_revenue[i],
                  ap: cogs * dr.dpo[i] / DAYS, ocl: rev * dr.other_cl_pct_revenue[i] };
      var dnwc = -((bal.ar - prev.ar) + (bal.inv - prev.inv) + (bal.oca - prev.oca) - (bal.ap - prev.ap) - (bal.ocl - prev.ocl));
      var fcff = nopat + da - capex - newLeases + dnwc;
      var leaseLiab = leasePrev * rev / prevRev;
      var lg = leaseLiab - leasePrev;
      L.revenue.push(rev); L.ebit.push(ebit); L.ebitda.push(ebit + da); L.nopat.push(nopat); L.capex.push(capex);
      L.fcff.push(fcff); L.fcffPub.push(fcff - lg); L.leaseLiab.push(leaseLiab); L.leaseGrowth.push(lg);
      prev = bal; leasePrev = leaseLiab; prevRev = rev;
    }
    return L;
  }

  /* ov: {wacc, g, m} overrides for grids; the roll-forward factor and the NCI claim stay at the scenario's ke. */
  function value(D, o, ov) {
    ov = ov || {};
    var cc = costOfCapital(D, o);
    var r = ov.wacc != null ? ov.wacc : cc.wacc;
    var g = ov.g != null ? ov.g : o.g;
    var m = ov.m != null ? ov.m : o.exitMultiple;
    var ke = cc.ke;
    var f = forecast(D, o);
    var n = f.fcff.length, off = D.valuation.mid_year ? 0.5 : 0;
    var pub = o.lease === "published";
    var flows = pub ? f.fcffPub : f.fcff;
    var sumPv = 0;
    for (var t = 1; t <= n; t++) sumPv += flows[t - 1] / Math.pow(1 + r, t - off);
    var fN = f.fcff[n - 1], nopN = f.nopat[n - 1], ebN = f.ebitda[n - 1], LN = f.leaseLiab[n - 1];
    var fcffNext = pub ? fN * (1 + g) - g * LN : fN * (1 + g);
    var nopNext = nopN * (1 + g);
    var ronicUsed = null, tvG;
    if (o.tvMethod === "ronic") {
      ronicUsed = o.ronic === "wacc" ? r : o.ronic;
      tvG = nopNext * (1 - g / ronicUsed) / (r - g);
    } else {
      tvG = fcffNext / (r - g);
    }
    var pvTvG = tvG / Math.pow(1 + r, n - off);
    var tvX = ebN * m, pvTvX = tvX / Math.pow(1 + r, n);
    var evG = sumPv + pvTvG, evX = sumPv + pvTvX;

    var f0 = D.fy_last;
    var netDebt = f0.debt_short + f0.debt_long + f0.lease_liabilities - f0.cash;
    var nciBook = f0.nci_equity, inc = D.nci_claim.income, gr = D.nci_claim.growth;
    var uplift = 0;
    if (o.nci === "g3") uplift = inc / (ke - gr) - nciBook;
    else if (o.nci === "g0") uplift = inc / ke - nciBook;
    var items = [], other = 0;
    D.bridge_items.forEach(function (it) {
      var on = it.key === "nci_uplift" ? o.nci !== "book" : (it.key === "provisions" ? !!o.provisions : true);
      var v = it.key === "nci_uplift" ? uplift : it.value;
      items.push({ key: it.key, label: it.label, value: v, on: on, inExit: it.key === "nci_uplift" || o.exitClaims === "full" });
      if (on && it.key !== "nci_uplift") other += v;
    });
    var dlG = other + uplift;
    var dlX = o.exitClaims === "peer" ? uplift : dlG;
    var shares = f0.shares_diluted, roll = Math.pow(1 + ke, D.valuation.stub), nonOp = D.valuation.non_op;
    var vG = (evG + nonOp - netDebt - nciBook - dlG) / shares * roll;
    var vX = (evX + nonOp - netDebt - nciBook - dlX) / shares * roll;
    var price = D.valuation.price, div = D.valuation.next_div;
    var wG = o.weightGordon;
    var blend = wG * vG + (1 - wG) * vX;
    var tgt = blend * (1 + ke) - div;
    var gFrom = function (tv) { return pub ? (tv * r - fN) / (tv + fN - LN) : (tv * r - fN) / (tv + fN); };
    var marketEv = price / roll * shares + netDebt + nciBook + dlG - nonOp;
    var impliedTv = (marketEv - sumPv) * Math.pow(1 + r, n - off);
    var ronicImplied = ronicUsed != null ? ronicUsed : (fcffNext < nopNext ? g / (1 - fcffNext / nopNext) : null);
    return {
      cc: cc, wacc: r, ke: ke, g: g, m: m, sumPv: sumPv, tvG: tvG, pvTvG: pvTvG, tvX: tvX, pvTvX: pvTvX, evG: evG, evX: evX,
      gordon: vG, exit: vX, blend: blend, target12: tgt, expReturn: tgt / price - 1 + div / price,
      premG: vG / price - 1, premX: vX / price - 1, tvShareG: pvTvG / evG, tvShareX: pvTvX / evX,
      ronic: ronicImplied, reinvest: 1 - (o.tvMethod === "ronic" ? (1 - g / ronicUsed) : fcffNext / nopNext),
      impliedMultiple: tvG * Math.pow(1 + r, off) / ebN, impliedGExit: gFrom(tvX / Math.pow(1 + r, off)),
      marketImpliedG: marketEv > sumPv ? gFrom(impliedTv) : null,
      netDebt: netDebt, nciBook: nciBook, uplift: uplift, dlG: dlG, dlX: dlX, items: items, perShare: roll / shares,
      roll: roll, lines: f, disagreement: vX !== 0 ? Math.abs(vG - vX) / Math.min(Math.abs(vG), Math.abs(vX)) : 0
    };
  }

  function rating(expReturn) {
    if (expReturn >= 0.15) return "BUY";
    if (expReturn <= -0.10) return "SELL";
    return "HOLD";
  }

  var api = { defaults: defaults, costOfCapital: costOfCapital, forecast: forecast, value: value, rating: rating };
  root.BovedaModel = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
})(typeof window !== "undefined" ? window : this);
