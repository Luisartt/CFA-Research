"""Load and validate the project files the engine reads.

- company-profile.yaml        written by init-skills
- data/financials.csv         written by the financials skill
- model/drivers.yaml          written by the forecast skill (optional)
- valuation/valuation.yaml    written by the valuation skill (optional)

Every problem is collected and raised together, so a student fixes them in one pass.
"""

from __future__ import annotations

import csv
import math
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypeGuard, TypeVar

import yaml

from .chart import BY_KEY, DRIVER_KEYS, REQUIRED_KEYS, SEGMENT_PREFIX, TAGS, ZERO_DEFAULT_DRIVERS

MIN_HIST_YEARS = 3
MAX_HIST_YEARS = 5
DEFAULT_FCST_YEARS = 5
MAX_FCST_YEARS = 10
FIN_COLUMNS = ("line_item", "year", "value", "tag", "source_doc", "page")
WACC_FIELDS = ("risk_free", "equity_risk_premium", "country_risk_premium", "beta_unlevered",
               "target_debt_to_equity", "pre_tax_cost_of_debt", "tax_rate")
TERMINAL_FIELDS = ("growth", "exit_ev_ebitda", "lt_nominal_gdp_growth")

T = TypeVar("T")


class InputError(Exception):
    """One or more project files are missing or invalid; `messages` lists every problem."""

    def __init__(self, messages: list[str]) -> None:
        super().__init__("; ".join(messages))
        self.messages = messages


@dataclass(frozen=True)
class Profile:
    name: str
    ticker: str
    currency: str
    units: str
    framework: str


@dataclass(frozen=True)
class Observation:
    value: float
    tag: str
    source_doc: str
    page: str


@dataclass(frozen=True)
class DriverInput:
    values: tuple[float, ...]
    tag: str
    rationale: str
    pillar: str


@dataclass(frozen=True)
class Segment:
    key: str
    label: str


@dataclass(frozen=True)
class Peer:
    name: str
    ticker: str
    price: float
    shares: float
    net_debt: float
    ebitda_fwd: float
    eps_fwd: float


@dataclass(frozen=True)
class Valuation:
    share_price: float
    price_52w_low: float
    price_52w_high: float
    risk_free: float
    equity_risk_premium: float
    country_risk_premium: float
    beta_unlevered: float
    target_debt_to_equity: float
    pre_tax_cost_of_debt: float
    tax_rate: float
    terminal_growth: float
    exit_ev_ebitda: float
    lt_nominal_gdp_growth: float
    mid_year: bool
    peers: tuple[Peer, ...]
    target_price: float | None


@dataclass(frozen=True)
class ModelInputs:
    profile: Profile
    hist_years: tuple[int, ...]
    fcst_years: tuple[int, ...]
    history: dict[str, dict[int, Observation]]
    drivers: dict[str, DriverInput]
    segments: tuple[Segment, ...]
    valuation: Valuation | None
    warnings: tuple[str, ...]

    @property
    def years(self) -> tuple[int, ...]:
        return self.hist_years + self.fcst_years

    @property
    def h(self) -> int:
        return len(self.hist_years)

    @property
    def n(self) -> int:
        return len(self.years)


def load_inputs(project: Path) -> ModelInputs:
    errors: list[str] = []
    profile = _collect(errors, lambda: load_profile(project / "company-profile.yaml"))
    financials = _collect(errors, lambda: load_financials(project / "data" / "financials.csv"))
    valuation = _collect(errors, lambda: load_valuation(project / "valuation" / "valuation.yaml"))
    if errors or profile is None or financials is None:
        raise InputError(errors)
    history, hist_years, warnings = financials
    drivers_result = _collect(errors, lambda: load_drivers(project / "model" / "drivers.yaml", history, hist_years))
    if errors or drivers_result is None:
        raise InputError(errors)
    drivers, segments, n_fcst, driver_warnings = drivers_result
    last = hist_years[-1]
    return ModelInputs(
        profile=profile,
        hist_years=hist_years,
        fcst_years=tuple(range(last + 1, last + 1 + n_fcst)),
        history=history,
        drivers=drivers,
        segments=segments,
        valuation=valuation,
        warnings=tuple(warnings + driver_warnings),
    )


def load_profile(path: Path) -> Profile:
    if not path.is_file():
        raise InputError([f"{path.name} not found: run /research-challenge:init-skills first"])
    doc = _mapping(_read_yaml(path), path.name)
    company = _mapping(doc.get("company"), f"{path.name} > company")
    accounting = _mapping(doc.get("accounting"), f"{path.name} > accounting")
    fields: dict[str, object] = {
        "company.name": company.get("name"),
        "company.ticker": company.get("ticker"),
        "accounting.reporting_currency": accounting.get("reporting_currency"),
        "accounting.units": accounting.get("units"),
        "accounting.framework": accounting.get("framework"),
    }
    errors: list[str] = []
    clean: dict[str, str] = {}
    for name, value in fields.items():
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path.name}: {name} is missing")
        elif "{{" in value:
            errors.append(f"{path.name}: {name} still has a placeholder; finish /research-challenge:init-skills")
        else:
            clean[name] = value.strip()
    if errors:
        raise InputError(errors)
    return Profile(
        name=clean["company.name"],
        ticker=clean["company.ticker"],
        currency=clean["accounting.reporting_currency"],
        units=clean["accounting.units"],
        framework=clean["accounting.framework"],
    )


def load_financials(path: Path) -> tuple[dict[str, dict[int, Observation]], tuple[int, ...], list[str]]:
    if not path.is_file():
        raise InputError([f"data/{path.name} not found: run the financials skill first"])
    errors: list[str] = []
    warnings: list[str] = []
    raw: dict[str, dict[int, Observation]] = {}
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            missing = [c for c in FIN_COLUMNS if c not in (reader.fieldnames or [])]
            if missing:
                raise InputError([f"financials.csv is missing columns: {', '.join(missing)}"])
            for number, row in enumerate(reader, start=2):
                _read_row(number, row, raw, errors, warnings)
    except UnicodeDecodeError:
        raise InputError([
            f"{path.name} is not saved as UTF-8. In Excel use File > Save As > "
            "'CSV UTF-8 (Comma delimited)'; in a text editor choose encoding UTF-8. Then run again."
        ]) from None
    years = sorted({year for series in raw.values() for year in series})
    if len(years) < MIN_HIST_YEARS:
        errors.append(f"financials.csv needs at least {MIN_HIST_YEARS} years of history; found {len(years)}")
        raise InputError(errors)
    hist_years = tuple(years[-MAX_HIST_YEARS:])
    for key in sorted(REQUIRED_KEYS):
        absent = [str(y) for y in hist_years if y not in raw.get(key, {})]
        if absent:
            errors.append(f"financials.csv: required line '{key}' is missing for {', '.join(absent)}")
    if errors:
        raise InputError(errors)
    history = {key: {y: o for y, o in series.items() if y in hist_years} for key, series in raw.items()}
    return history, hist_years, warnings


def _read_row(number: int, row: Mapping[str, str | None], raw: dict[str, dict[int, Observation]],
              errors: list[str], warnings: list[str]) -> None:
    key = (row.get("line_item") or "").strip()
    if key not in BY_KEY and not key.startswith(SEGMENT_PREFIX):
        errors.append(f"financials.csv row {number}: unknown line_item '{key}'")
        return
    try:
        year = int((row.get("year") or "").strip())
        value = float((row.get("value") or "").strip())
    except ValueError:
        errors.append(f"financials.csv row {number}: year and value must be plain numbers (no thousands separators)")
        return
    if not math.isfinite(value):
        errors.append(f"financials.csv row {number}: value must be a finite number")
        return
    tag = (row.get("tag") or "").strip()
    if tag not in TAGS:
        errors.append(f"financials.csv row {number}: tag '{tag}' must be one of {', '.join(sorted(TAGS))}")
        return
    series = raw.setdefault(key, {})
    if year in series:
        errors.append(f"financials.csv row {number}: duplicate {key} for {year}")
        return
    if tag == "unverified":
        warnings.append(f"{key} {year} is tagged [unverified]; resolve it before the report")
    series[year] = Observation(value, tag, (row.get("source_doc") or "").strip(), (row.get("page") or "").strip())


def load_drivers(path: Path, history: Mapping[str, Mapping[int, Observation]], hist_years: tuple[int, ...]
                 ) -> tuple[dict[str, DriverInput], tuple[Segment, ...], int, list[str]]:
    if not path.is_file():
        return {}, (), DEFAULT_FCST_YEARS, [
            "model/drivers.yaml not found: every driver held at its last actual value (run the forecast skill)"
        ]
    doc = _mapping(_read_yaml(path), "drivers.yaml")
    n_fcst = doc.get("forecast_years", DEFAULT_FCST_YEARS)
    if isinstance(n_fcst, bool) or not isinstance(n_fcst, int) or not 1 <= n_fcst <= MAX_FCST_YEARS:
        raise InputError([f"drivers.yaml: forecast_years must be a whole number from 1 to {MAX_FCST_YEARS}"])
    errors: list[str] = []
    warnings: list[str] = []
    segments = _read_segments(doc.get("revenue_segments"), history, hist_years, errors)
    allowed = set(DRIVER_KEYS) | {f"{SEGMENT_PREFIX}{s.key}_growth" for s in segments}
    drivers: dict[str, DriverInput] = {}
    for key, entry in _mapping(doc.get("drivers", {}), "drivers.yaml > drivers").items():
        if key not in allowed:
            errors.append(f"drivers.yaml: unknown driver '{key}'")
            continue
        parsed = _read_driver(key, entry, n_fcst, errors)
        if parsed is not None:
            drivers[key] = parsed
    if errors:
        raise InputError(errors)
    for key in sorted(allowed - drivers.keys()):
        if key == "revenue_growth" and segments:
            continue
        default = "zero" if key in ZERO_DEFAULT_DRIVERS else "held at last actual value"
        warnings.append(f"driver '{key}' not set: {default} (engine default)")
    if segments and "revenue_growth" in drivers:
        warnings.append("revenue_growth is ignored because revenue_segments are set")
    return drivers, segments, n_fcst, warnings


def _read_driver(key: str, entry: object, n_fcst: int, errors: list[str]) -> DriverInput | None:
    if not isinstance(entry, dict):
        errors.append(f"drivers.yaml: '{key}' must have values, tag, rationale")
        return None
    values = entry.get("values")
    if not isinstance(values, list) or len(values) != n_fcst or not all(_is_number(v) for v in values):
        errors.append(f"drivers.yaml: '{key}' needs exactly {n_fcst} numeric values")
        return None
    tag = str(entry.get("tag", "assumption"))
    if tag not in TAGS:
        errors.append(f"drivers.yaml: '{key}' tag '{tag}' must be one of {', '.join(sorted(TAGS))}")
        return None
    return DriverInput(tuple(float(v) for v in values), tag, str(entry.get("rationale", "")), str(entry.get("pillar", "")))


def _read_segments(raw: object, history: Mapping[str, Mapping[int, Observation]], hist_years: tuple[int, ...],
                   errors: list[str]) -> tuple[Segment, ...]:
    if raw is None:
        return ()
    if not isinstance(raw, list):
        errors.append("drivers.yaml: revenue_segments must be a list")
        return ()
    segments: list[Segment] = []
    for item in raw:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str):
            errors.append("drivers.yaml: each revenue segment needs a key and a label")
            continue
        key = item["key"].strip()
        if not key.replace("_", "").isalnum():
            errors.append(f"drivers.yaml: segment key '{key}' must use letters, digits or _")
            continue
        line = f"{SEGMENT_PREFIX}{key}"
        absent = [str(y) for y in hist_years if y not in history.get(line, {})]
        if absent:
            errors.append(f"financials.csv: segment line '{line}' is missing for {', '.join(absent)}")
            continue
        segments.append(Segment(key, str(item.get("label", key))))
    return tuple(segments)


def load_valuation(path: Path) -> Valuation | None:
    if not path.is_file():
        return None
    doc = _mapping(_read_yaml(path), "valuation.yaml")
    wacc = _mapping(doc.get("wacc"), "valuation.yaml > wacc")
    terminal = _mapping(doc.get("terminal"), "valuation.yaml > terminal")
    errors: list[str] = []

    def number(section: Mapping[str, Any], name: str, where: str) -> float:
        raw = section.get(name)
        if not _is_number(raw):
            errors.append(f"valuation.yaml: {where}{name} must be a number")
            return math.nan
        return float(raw)

    w = {f: number(wacc, f, "wacc.") for f in WACC_FIELDS}
    t = {f: number(terminal, f, "terminal.") for f in TERMINAL_FIELDS}
    price = number(doc, "share_price", "")
    low = number(doc, "price_52w_low", "")
    high = number(doc, "price_52w_high", "")
    peers: list[Peer] = []
    raw_peers = doc.get("peers") or []
    if not isinstance(raw_peers, list):
        errors.append("valuation.yaml: peers must be a list")
        raw_peers = []
    for i, entry in enumerate(raw_peers, start=1):
        if not isinstance(entry, dict):
            errors.append(f"valuation.yaml: peer {i} must be a mapping")
            continue
        where = f"peers[{i}]."
        peers.append(Peer(
            name=str(entry.get("name", f"Peer {i}")),
            ticker=str(entry.get("ticker", "")),
            price=number(entry, "price", where),
            shares=number(entry, "shares", where),
            net_debt=number(entry, "net_debt", where),
            ebitda_fwd=number(entry, "ebitda_fwd", where),
            eps_fwd=number(entry, "eps_fwd", where),
        ))
    target = doc.get("target_price")
    if target is not None and not _is_number(target):
        errors.append("valuation.yaml: target_price must be a number or null")
    mid_year = doc.get("mid_year", True)
    if not isinstance(mid_year, bool):
        errors.append("valuation.yaml: mid_year must be true or false")
    if errors:
        raise InputError(errors)
    return Valuation(
        share_price=price, price_52w_low=low, price_52w_high=high,
        risk_free=w["risk_free"], equity_risk_premium=w["equity_risk_premium"],
        country_risk_premium=w["country_risk_premium"], beta_unlevered=w["beta_unlevered"],
        target_debt_to_equity=w["target_debt_to_equity"], pre_tax_cost_of_debt=w["pre_tax_cost_of_debt"],
        tax_rate=w["tax_rate"], terminal_growth=t["growth"], exit_ev_ebitda=t["exit_ev_ebitda"],
        lt_nominal_gdp_growth=t["lt_nominal_gdp_growth"], mid_year=bool(mid_year), peers=tuple(peers),
        target_price=float(target) if _is_number(target) else None,
    )


def _collect(errors: list[str], load: Callable[[], T]) -> T | None:
    try:
        return load()
    except InputError as exc:
        errors.extend(exc.messages)
        return None


def _read_yaml(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        raise InputError([f"{path.name} is not saved as UTF-8; re-save it with UTF-8 encoding and run again."]) from None
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise InputError([f"{path.name} is not valid YAML: {exc}"]) from None


def _mapping(obj: object, where: str) -> dict[str, Any]:
    if not isinstance(obj, dict):
        raise InputError([f"{where} must be a mapping (key: value)"])
    return obj


def _is_number(value: object) -> TypeGuard[int | float]:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
