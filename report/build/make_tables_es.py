"""Spanish copy of the report tables: the numbers of report/tables/*.md are carried into the existing Spanish tables cell by cell.

Cells that are pure numbers are copied; cells that mix text and numbers keep the Spanish wording and take the new numbers in order;
labels listed in LABELS are replaced. Run after make_tables.py. Prints what it could not merge.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "report/tables_es"  # Spanish tables to take the wording from
LABELS = {"NOPAT (tax 32.7%)": "NOPAT (impuesto 32.7%)",
          "Non-controlling interests (income capitalised at ke less g)": "Participación no controladora (ingreso capitalizado a ke menos g)"}
NUM = re.compile(r"[-+]?\(?\d[\d,]*\.?\d*\)?%?x?")
PURE = re.compile(r"^[\s*()\-+0-9.,%x]*$")
bad = []
for f in sorted((ROOT / "report/tables").glob("*.md")):
    new = f.read_text(encoding="utf-8").split("\n")
    old = (SRC / f.name).read_text(encoding="utf-8").split("\n")
    out = []
    for ln, (n, o) in enumerate(zip(new, old)):
        if not n.startswith("|") or re.match(r"^\|[-| ]+\|$", n):
            out.append(n); continue
        nc, oc = n.strip("|").split("|"), o.strip("|").split("|")
        if len(nc) != len(oc):
            bad.append((f.name, ln, "columns")); out.append(o); continue
        cells = []
        for a, b in zip(nc, oc):
            a_, b_ = a.strip(), b.strip()
            if a_ in LABELS:
                cells.append(" " + LABELS[a_] + " ")
            elif PURE.match(a_) or not re.search(r"[A-Za-z]", b_):
                cells.append(" " + a_ + " ")
            elif re.search(r"\d", a_):
                na, nb = NUM.findall(a_), NUM.findall(b_)
                if len(na) == len(nb):
                    it = iter(na)
                    cells.append(" " + NUM.sub(lambda m: next(it), b_) + " ")
                else:
                    bad.append((f.name, ln, a_[:60], b_[:60])); cells.append(" " + b_ + " ")
            else:
                cells.append(" " + b_ + " ")
        out.append("|" + "|".join(cells) + "|")
    (ROOT / "report/tables_es" / f.name).write_text("\n".join(out), encoding="utf-8")
print("tables_es written;", len(bad), "cells to check")
for b in bad: print("  ", b)
