"""Spanish copies of the valuation workbooks.

  extract: python -I translate_workbook.py extract --out strings.json <book.xlsx> [...]
           collects every text cell that no formula reads (label, note, source), so a translation can never break
           a formula that compares text (e.g. ="yes", ="Core", COUNTIF(...,"OK")).
  apply:   python -I translate_workbook.py apply --dict es.json --src <book.xlsx> --dst <book_ES.xlsx>
           writes a copy with those cells translated; formulas, numbers, sheet names and formats are unchanged.
           Missing translations are reported and left in English. Recalculate the copy afterwards with
           recalc_excel.ps1 (openpyxl does not keep cached values) and scan it with scan_errors.py.
Never run it on the S&P templates (SPG_*): it refuses them.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.formula.tokenizer import Tokenizer
from openpyxl.utils.cell import range_boundaries

REF = re.compile(r"^(?:(?P<sheet>'[^']+'|[A-Za-z0-9_.]+)!)?(?P<rng>\$?[A-Z]{1,3}\$?\d+(?::\$?[A-Z]{1,3}\$?\d+)?)$")
KEEP = {"OK", "WARN", "FAIL", "CHECK", "FLAG", "n/a", "n.m.", "n.a.", "yes", "no", "x", "%", "-", "—"}


def referenced_cells(wb) -> set[tuple[str, int, int]]:
    """(sheet, row, col) of every cell any formula reads, ranges expanded."""
    out: set[tuple[str, int, int]] = set()
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if not (isinstance(v, str) and v.startswith("=")):
                    continue
                try:
                    toks = Tokenizer(v).items
                except Exception:
                    continue
                for t in toks:
                    if t.type != "OPERAND" or t.subtype != "RANGE":
                        continue
                    m = REF.match(t.value.replace(" ", ""))
                    if not m:
                        continue
                    sheet = (m.group("sheet") or ws.title).strip("'")
                    c1, r1, c2, r2 = range_boundaries(m.group("rng").replace("$", ""))
                    if (r2 - r1 + 1) * (c2 - c1 + 1) > 200:
                        # whole-sheet ranges (error scans such as SUMPRODUCT(--ISERROR(A1:T80))) only test for
                        # errors; text comparisons (="yes", ="Core", COUNTIF(...,"OK")) use small ranges
                        continue
                    for rr in range(r1, r2 + 1):
                        for cc in range(c1, c2 + 1):
                            out.add((sheet, rr, cc))
    return out


def translatable(wb):
    refs = referenced_cells(wb)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if not isinstance(v, str) or v.startswith("=") or not v.strip():
                    continue
                if (ws.title, c.row, c.column) in refs or v.strip() in KEEP:
                    continue
                if not re.search(r"[A-Za-z]{2,}", v):
                    continue
                yield ws, c, v


def guard(path: Path) -> None:
    if path.name.upper().startswith("SPG_"):
        raise SystemExit(f"refusing to touch an S&P template: {path.name}")


def cmd_extract(a) -> int:
    strings: dict[str, str] = {}
    for p in a.books:
        path = Path(p)
        guard(path)
        wb = load_workbook(path)
        for _, _, v in translatable(wb):
            strings.setdefault(v, "")
    Path(a.out).write_text(json.dumps(strings, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"{len(strings)} unique strings -> {a.out}")
    return 0


def cmd_apply(a) -> int:
    src, dst = Path(a.src), Path(a.dst)
    guard(src)
    guard(dst)
    tr = json.loads(Path(a.dict).read_text(encoding="utf-8"))
    wb = load_workbook(src)
    done = missing = 0
    miss: set[str] = set()
    for _, c, v in list(translatable(wb)):
        t = tr.get(v)
        if t:
            c.value = t
            done += 1
        else:
            missing += 1
            miss.add(v)
    wb.save(dst)
    print(f"{dst.name}: {done} cells translated, {missing} left in English ({len(miss)} unique)")
    for m in sorted(miss)[:20]:
        print("   missing:", m[:90])
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract")
    e.add_argument("--out", required=True)
    e.add_argument("books", nargs="+")
    p = sub.add_parser("apply")
    p.add_argument("--dict", required=True)
    p.add_argument("--src", required=True)
    p.add_argument("--dst", required=True)
    a = ap.parse_args(argv)
    return cmd_extract(a) if a.cmd == "extract" else cmd_apply(a)


if __name__ == "__main__":
    sys.exit(main())
