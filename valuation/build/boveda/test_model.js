/* node test_model.js <data.json> : compares the page engine with the Python reference cases. */
const fs = require("fs");
const path = require("path");
const M = require(path.join(__dirname, "model.js"));
const D = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
let fails = 0, n = 0;
for (const [name, c] of Object.entries(D.reference.cases)) {
  const o = Object.assign(M.defaults(D), c.opts);
  const v = M.value(D, o);
  for (const k of ["gordon", "exit", "ronic", "implied_g", "wacc", "ke"]) {
    if (c[k] == null) continue;
    const got = { gordon: v.gordon, exit: v.exit, ronic: v.ronic, implied_g: v.marketImpliedG, wacc: v.wacc, ke: v.ke }[k];
    const rel = Math.abs(got / c[k] - 1);
    n++;
    const ok = rel < 1e-6;
    if (!ok) fails++;
    console.log(`${ok ? "OK  " : "FAIL"} ${name.padEnd(12)} ${k.padEnd(9)} js ${got.toFixed(6)}  py ${c[k].toFixed(6)}  rel ${rel.toExponential(2)}`);
  }
}
const base = M.value(D, M.defaults(D));
const ref = D.reference.published;
for (const [k, got] of [["ev_gordon", base.evG], ["ev_exit", base.evX], ["tv_share_gordon", base.tvShareG],
                        ["implied_exit_multiple", base.impliedMultiple], ["implied_g_exit", base.impliedGExit], ["tgt12", null]]) {
  const want = ref[k];
  const g = k === "tgt12" ? base.gordon * (1 + base.ke) - D.valuation.next_div : got;
  const rel = Math.abs(g / want - 1); n++;
  if (rel >= 1e-6) fails++;
  console.log(`${rel < 1e-6 ? "OK  " : "FAIL"} base         ${k.padEnd(22)} js ${g.toFixed(6)}  py ${want.toFixed(6)}`);
}
console.log(`\n${n - fails}/${n} OK`);
process.exit(fails ? 1 : 0);
