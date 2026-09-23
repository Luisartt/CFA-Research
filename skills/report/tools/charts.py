"""Charts for the report and the deck.

Reads model/model-summary.json (written by the model engine) and
research/risks.yaml (written by the risks-esg skill); writes PNGs to
report/charts/. Console output is ASCII only.

Usage: python charts.py --project <team folder>
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import yaml  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

NAVY = "#1F4E79"
LIGHT = "#9DC3E6"
ACCENT = "#C55A11"
GREY = "#7F7F7F"
FULL_WIDTH_IN = 6.3
HALF_WIDTH_IN = 3.2
DPI = 200
SOURCE_NOTE = "A = actual, E = estimate. Source: team model."
EXIT_OK = 0
EXIT_NOTHING = 2

Summary = dict[str, Any]


class ChartError(Exception):
    """An input file is missing or invalid."""


@dataclass(frozen=True)
class Chart:
    name: str
    needs: str  # "summary", "valuation" or "risks"
    draw: Callable[[Summary, list[dict[str, Any]], Path], None]


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _year_labels(summary: Summary) -> list[str]:
    hist = [f"{y}A" for y in summary["historical_years"]]
    fcst = [f"{y}E" for y in summary["forecast_years"]]
    return hist + fcst


def _series(summary: Summary, section: str, key: str) -> list[float]:
    values = summary.get(section, {}).get(key, {})
    years = [str(y) for y in summary["historical_years"] + summary["forecast_years"]]
    return [math.nan if values.get(y) is None else float(values[y]) for y in years]


def _style(ax: Axes) -> None:
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.tick_params(labelsize=7)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.5)
    ax.set_axisbelow(True)


def _save(fig: Figure, path: Path, note: str = SOURCE_NOTE) -> None:
    fig.text(0.01, 0.01, note, fontsize=6, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=DPI)
    plt.close(fig)


def revenue_margin(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    labels = _year_labels(summary)
    h = len(summary["historical_years"])
    revenue = _series(summary, "lines", "revenue")
    margin = [m * 100 for m in _series(summary, "ratios", "r_ebitda_margin")]
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.3))
    ax.bar(labels, revenue, color=[NAVY if i < h else LIGHT for i in range(len(labels))])
    ax.set_ylabel(f"Revenue ({summary['currency']} {summary['units']})", fontsize=7)
    twin = ax.twinx()
    twin.plot(labels, margin, color=ACCENT, marker="o", linewidth=1.2, markersize=3)
    twin.set_ylabel("EBITDA margin (%)", fontsize=7)
    twin.tick_params(labelsize=7)
    ax.set_title("Revenue and EBITDA margin", fontsize=8)
    _style(ax)
    ax.tick_params(axis="x", rotation=45)
    _save(fig, path)


def free_cash_flow(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    labels = _year_labels(summary)
    fcf = _series(summary, "lines", "fcf")
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.3))
    ax.bar(labels, fcf, color=[ACCENT if (not math.isnan(v) and v < 0) else NAVY for v in fcf])
    ax.axhline(0, color=GREY, linewidth=0.6)
    ax.set_ylabel(f"{summary['currency']} {summary['units']}", fontsize=7)
    ax.set_title("Free cash flow (CFO - capex - lease principal)", fontsize=8)
    _style(ax)
    ax.tick_params(axis="x", rotation=45)
    _save(fig, path)


def football_field(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    rows = [r for r in summary["football"] if r["low"] is not None and r["high"] is not None]
    fig, ax = plt.subplots(figsize=(FULL_WIDTH_IN, 0.45 * len(rows) + 1.0))
    labels = [r["method"] for r in rows]
    for i, row in enumerate(rows):
        width = row["high"] - row["low"]
        if width > 0:
            ax.barh(i, width, left=row["low"], color=LIGHT, edgecolor=NAVY, height=0.5)
        else:
            ax.plot([row["low"]], [i], marker="D", color=NAVY)
    price = summary.get("valuation", {}).get("share_price")
    if price is not None:
        ax.axvline(price, color=ACCENT, linestyle="--", linewidth=1)
        ax.text(price, len(rows) - 0.4, f" price {price:,.2f}", color=ACCENT, fontsize=7)
    ax.set_yticks(range(len(rows)), labels=labels, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel(f"Value per share ({summary['currency']})", fontsize=7)
    ax.set_title("Valuation summary (football field)", fontsize=8)
    _style(ax)
    ax.grid(axis="x", color="#D9D9D9", linewidth=0.5)
    _save(fig, path, "Source: team model (DCF, comps, market data).")


def sensitivity(summary: Summary, _: list[dict[str, Any]], path: Path) -> None:
    grid = summary["sensitivity"]
    values = [[math.nan if v is None else float(v) for v in row] for row in grid["values"]]
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.6))
    ax.imshow(values, cmap="Blues", aspect="auto")
    for i, row in enumerate(values):
        for j, v in enumerate(row):
            ax.text(j, i, "n.m." if math.isnan(v) else f"{v:,.1f}", ha="center", va="center", fontsize=6,
                    color="black")
    ax.set_xticks(range(len(grid["growth"])), labels=[f"{g * 100:.1f}%" for g in grid["growth"]], fontsize=7)
    ax.set_yticks(range(len(grid["wacc"])), labels=[f"{w * 100:.1f}%" for w in grid["wacc"]], fontsize=7)
    ax.set_xlabel("Terminal growth", fontsize=7)
    ax.set_ylabel("WACC", fontsize=7)
    ax.set_title("DCF value per share: sensitivity", fontsize=8)
    _save(fig, path, "Source: team model (Gordon growth DCF).")


def risk_matrix(_: Summary, risks: list[dict[str, Any]], path: Path) -> None:
    fig, ax = plt.subplots(figsize=(HALF_WIDTH_IN, 2.8))
    for x in range(1, 6):
        for y in range(1, 6):
            score = x * y
            color = "#E2F0D9" if score <= 6 else ("#FFF2CC" if score <= 12 else "#F8CBAD")
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, color=color, zorder=0))
    for risk in risks:
        ax.scatter(risk["probability"], risk["impact"], color=NAVY, s=30, zorder=2)
        ax.annotate(risk["id"], (risk["probability"], risk["impact"]), textcoords="offset points",
                    xytext=(4, 4), fontsize=7)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.tick_params(labelsize=7)
    ax.set_xlabel("Probability (1 = low, 5 = high)", fontsize=7)
    ax.set_ylabel("Impact on value (1-5)", fontsize=7)
    ax.set_title("Investment risk matrix", fontsize=8)
    _save(fig, path, "Source: team analysis (research/risks.md).")


CHARTS: tuple[Chart, ...] = (
    Chart("revenue-margin", "summary", revenue_margin),
    Chart("free-cash-flow", "summary", free_cash_flow),
    Chart("football-field", "valuation", football_field),
    Chart("sensitivity", "valuation", sensitivity),
    Chart("risk-matrix", "risks", risk_matrix),
)


def load_summary(path: Path) -> Summary | None:
    if not path.is_file():
        return None
    try:
        data: Summary = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ChartError(f"{path.name} is not valid JSON: {exc}") from None
    return data


def load_risks(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except (yaml.YAMLError, UnicodeDecodeError) as exc:
        raise ChartError(f"{path.name} is not valid YAML: {exc}") from None
    risks = doc.get("risks") if isinstance(doc, dict) else None
    if not isinstance(risks, list):
        raise ChartError(f"{path.name} needs a 'risks:' list")
    problems: list[str] = []
    for n, risk in enumerate(risks, start=1):
        rid = risk.get("id", f"#{n}") if isinstance(risk, dict) else f"#{n}"
        if not isinstance(risk, dict):
            problems.append(f"risk {rid} must be a mapping")
            continue
        for field in ("probability", "impact"):
            value = risk.get(field)
            if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
                problems.append(f"risk {rid}: {field} must be a whole number from 1 to 5")
    if problems:
        raise ChartError("; ".join(problems))
    return risks


def _available(chart: Chart, summary: Summary | None, risks: Sequence[dict[str, Any]]) -> str:
    """Empty string if the chart can be drawn, else the reason it is skipped."""
    if chart.needs == "risks":
        return "" if risks else "research/risks.yaml not found or empty (run the risks-esg skill)"
    if summary is None:
        return "model/model-summary.json not found (run the model skill)"
    if chart.needs == "valuation":
        if chart.name == "football-field" and not summary.get("football"):
            return "no valuation in the model (run the valuation skill)"
        if chart.name == "sensitivity" and not summary.get("sensitivity"):
            return "no valuation in the model (run the valuation skill)"
    return ""


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Draw the report charts into report/charts/.")
    parser.add_argument("--project", default=".", help="Team project folder")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    try:
        summary = load_summary(project / "model" / "model-summary.json")
        risks = load_risks(project / "research" / "risks.yaml")
    except ChartError as exc:
        print("[x] " + ascii_safe(str(exc)))
        return EXIT_NOTHING
    out_dir = project / "report" / "charts"
    out_dir.mkdir(parents=True, exist_ok=True)
    drawn = 0
    for chart in CHARTS:
        reason = _available(chart, summary, risks)
        if reason:
            print(f"[skip] {chart.name}: {ascii_safe(reason)}")
            continue
        chart.draw(summary or {}, list(risks), out_dir / f"{chart.name}.png")
        print(f"[ok] report/charts/{chart.name}.png")
        drawn += 1
    if drawn == 0:
        print("[x] Nothing to draw: build the model (model-summary.json) or write research/risks.yaml first.")
        return EXIT_NOTHING
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
