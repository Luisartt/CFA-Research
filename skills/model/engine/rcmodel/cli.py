"""Command line: python build_model.py --project <team folder>. Console output is ASCII only."""

from __future__ import annotations

import argparse
import json
import re
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .assemble import assemble
from .checks import CheckResult, build_checks, evaluate_checks, overall_status, parity_checks
from .engine import ModelError
from .inputs import InputError, load_inputs
from .summary import build_summary
from .writer import BuildInfo, write_workbook

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_MODEL_ERROR = 3
EXIT_IO_ERROR = 4
EXIT_CODES_HELP = "exit codes: 0 built, 2 input error, 3 model definition error, 4 file could not be written"


@dataclass(frozen=True)
class BuildResult:
    workbook: Path
    summary: Path
    results: tuple[CheckResult, ...]
    warnings: tuple[str, ...]
    status: str
    years: tuple[int, ...]


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def next_version_path(model_dir: Path, ticker: str) -> tuple[Path, int]:
    """Next unused <TICKER>_model_v<N>.xlsx; earlier versions are never overwritten."""
    safe = re.sub(r"[^A-Za-z0-9]+", "-", ticker).strip("-") or "MODEL"
    pattern = re.compile(rf"^{re.escape(safe)}_model_v(\d+)\.xlsx$")
    versions = [int(m.group(1)) for p in model_dir.glob("*.xlsx") if (m := pattern.match(p.name))]
    version = max(versions, default=0) + 1
    return model_dir / f"{safe}_model_v{version}.xlsx", version


def build(project: Path, today: date) -> BuildResult:
    inputs = load_inputs(project)
    model, football = assemble(inputs)
    checks = [*build_checks(inputs), *parity_checks(model)]
    results = evaluate_checks(model, checks)
    model_dir = project / "model"
    model_dir.mkdir(parents=True, exist_ok=True)
    path, version = next_version_path(model_dir, inputs.profile.ticker)
    info = BuildInfo(version, path.name, today)
    write_workbook(path, model, checks, results, football, info)
    summary_path = model_dir / "model-summary.json"
    summary = build_summary(model, results, info)
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return BuildResult(path, summary_path, tuple(results), inputs.warnings, overall_status(results), inputs.years)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the research-challenge financial model (xlsx + model-summary.json).",
        epilog=EXIT_CODES_HELP,
    )
    parser.add_argument("--project", default=".", help="Team project folder (the one with company-profile.yaml)")
    args = parser.parse_args(argv)
    try:
        result = build(Path(args.project).resolve(), date.today())
    except InputError as exc:
        print("[x] Cannot build the model. Fix these inputs first:")
        for message in exc.messages:
            print("  - " + ascii_safe(message))
        return EXIT_INPUT_ERROR
    except ModelError as exc:
        print("[x] Model definition error: " + ascii_safe(str(exc)))
        return EXIT_MODEL_ERROR
    except OSError as exc:
        target = Path(exc.filename).name if exc.filename else "a file in model/"
        print(f"[x] Could not write {ascii_safe(target)}: {ascii_safe(exc.strerror or str(exc))}.")
        print("    Close it if it is open in Excel or another program (or pause OneDrive sync), then run again.")
        return EXIT_IO_ERROR
    counts = {status: sum(1 for r in result.results if r.status == status) for status in ("OK", "ERROR", "WARN")}
    print(f"[ok] workbook -> model/{ascii_safe(result.workbook.name)}")
    print("[ok] summary  -> model/model-summary.json")
    print(f"checks: {counts['OK']} OK, {counts['ERROR']} ERROR, {counts['WARN']} WARN")
    for r in result.results:
        if r.status != "OK":
            year = "" if r.period is None else f" ({result.years[r.period]})"
            marker = "[x]" if r.status == "ERROR" else "[warn]"
            print(f"{marker} Not met: {ascii_safe(r.label)}{year}")
    for warning in result.warnings:
        print("[warn] " + ascii_safe(warning))
    print(f"status: {result.status}")
    return EXIT_OK
