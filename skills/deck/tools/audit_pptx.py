"""Audit a pitch deck against the Challenge rules and basic presentation hygiene.

Structural checks only (no rendering): slide count for a 10-minute talk, a source on
every slide but the title, speaker notes, leftover placeholder text, shapes off the
slide, small fonts, too many font families, likely text overflow, dense slides, and
numbers that disagree with model/model-summary.json and report/header.yaml.
--fix saves a NEW version with mechanical fixes only (empty placeholders removed,
off-palette fonts set to the deck's main font); everything else is reported.
Writes pitch/deck-audit.md. Console output is ASCII only.

Usage: python audit_pptx.py --project <team folder> [--deck <file>] [--fix]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from pptx import Presentation
from pptx.exc import PackageNotFoundError

EXIT_OK = 0
EXIT_NO_DECK = 2
EXIT_IO_ERROR = 4
MIN_SLIDES, MAX_SLIDES = 6, 14
MIN_FONT_PT, MIN_FOOTER_PT = 10, 8
MAX_WORDS = 60
MAX_FONT_FAMILIES = 2
DEFAULT_FONT_PT = 18
EMU_PER_PT = 12700
LEFTOVERS = ("click to add", "lorem ipsum", "todo", "[insert", "xx.x", "tbd")
TARGET_RE = re.compile(r"target(?:\s+price)?\D{0,15}?(\d[\d,]*\.?\d*)", re.IGNORECASE)
WACC_RE = re.compile(r"WACC\D{0,15}?(\d+(?:\.\d+)?)\s*%", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    slide: int  # 0 = whole deck
    severity: str  # ERROR or WARN
    code: str
    message: str


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _texts(slide: Any) -> Iterator[tuple[Any, str]]:
    for shape in slide.shapes:
        if shape.has_text_frame:
            yield shape, shape.text_frame.text


def _load_reference(project: Path) -> dict[str, float]:
    ref: dict[str, float] = {}
    header = project / "report" / "header.yaml"
    if header.is_file():
        doc = yaml.safe_load(header.read_text(encoding="utf-8-sig"))
        if isinstance(doc, dict) and isinstance(doc.get("target_price"), (int, float)):
            ref["target"] = float(doc["target_price"])
    summary = project / "model" / "model-summary.json"
    if summary.is_file():
        data = json.loads(summary.read_text(encoding="utf-8"))
        wacc = data.get("valuation", {}).get("wacc")
        if isinstance(wacc, (int, float)):
            ref["wacc_pct"] = float(wacc) * 100
    return ref


def _overflow(shape: Any, text: str) -> bool:
    if shape.width is None or shape.height is None or not text.strip():
        return False
    sizes = [r.font.size.pt for p in shape.text_frame.paragraphs for r in p.runs if r.font.size is not None]
    size = min(sizes) if sizes else DEFAULT_FONT_PT
    chars_per_line = max(1.0, (shape.width / EMU_PER_PT) / (size * 0.5))
    lines = sum(max(1, -(-len(p.text) // int(chars_per_line))) for p in shape.text_frame.paragraphs)
    capacity = (shape.height / EMU_PER_PT) / (size * 1.2)
    return bool(lines > capacity + 0.5)


def audit(path: Path, project: Path) -> list[Finding]:
    prs = Presentation(str(path))
    reference = _load_reference(project)
    findings: list[Finding] = []
    count = len(prs.slides)
    if not MIN_SLIDES <= count <= MAX_SLIDES:
        findings.append(Finding(0, "WARN", "slide-count",
                                f"{count} slides; a 10-minute talk usually needs {MIN_SLIDES}-{MAX_SLIDES}"))
    families: Counter[str] = Counter()
    for n, slide in enumerate(prs.slides, start=1):
        texts = list(_texts(slide))
        all_text = " ".join(t for _, t in texts)
        if n > 1 and not any(t.strip().lower().startswith("source") for _, t in texts):
            findings.append(Finding(n, "ERROR", "no-sources", "no 'Source:' line (Challenge rule: slides show sources)"))
        notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
        if not notes.strip():
            findings.append(Finding(n, "WARN", "no-notes", "no speaker notes"))
        lowered = all_text.lower()
        for marker in LEFTOVERS:
            if marker in lowered:
                findings.append(Finding(n, "ERROR", "leftover", f"placeholder text left: '{marker}'"))
        if len(all_text.split()) > MAX_WORDS:
            findings.append(Finding(n, "WARN", "dense", f"{len(all_text.split())} words; aim for under {MAX_WORDS}"))
        for shape in slide.shapes:
            if None not in (shape.left, shape.top, shape.width, shape.height) and (
                    shape.left < 0 or shape.top < 0 or shape.left + shape.width > prs.slide_width
                    or shape.top + shape.height > prs.slide_height):
                findings.append(Finding(n, "ERROR", "off-slide", f"'{shape.name}' extends beyond the slide"))
        for shape, text in texts:
            is_footer = text.strip().lower().startswith("source")
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.font.name:
                        families[run.font.name] += len(run.text)
                    size = run.font.size or paragraph.font.size
                    if size is not None and size.pt < (MIN_FOOTER_PT if is_footer else MIN_FONT_PT):
                        findings.append(Finding(n, "WARN", "small-font", f"{size.pt:g} pt text in '{shape.name}'"))
            if _overflow(shape, text):
                findings.append(Finding(n, "WARN", "overflow", f"text may not fit in '{shape.name}'"))
        if "target" in reference:
            for match in TARGET_RE.finditer(all_text):
                value = float(match.group(1).replace(",", ""))
                if abs(value - reference["target"]) > 0.01 * reference["target"]:
                    findings.append(Finding(n, "WARN", "stale-target",
                                            f"target {value:g} differs from report/header.yaml ({reference['target']:g})"))
        if "wacc_pct" in reference:
            for match in WACC_RE.finditer(all_text):
                if abs(float(match.group(1)) - reference["wacc_pct"]) > 0.1:
                    findings.append(Finding(n, "WARN", "stale-wacc",
                                            f"WACC {match.group(1)}% differs from the model ({reference['wacc_pct']:.1f}%)"))
    if len(families) > MAX_FONT_FAMILIES:
        findings.append(Finding(0, "WARN", "fonts", "fonts used: " + ", ".join(sorted(families))))
    return findings


RARE_FONT_SHARE = 0.2


def fix(path: Path, target: Path) -> int:
    """Mechanical fixes only; returns the number of changes. Saves to `target`.

    - removes empty placeholders;
    - a font used for less than 20% of the deck's text is reset to the template's
      theme font (explicit font removed), so stray pasted fonts disappear while
      the team's main font is never touched.
    """
    prs = Presentation(str(path))
    families: Counter[str] = Counter()
    total = 0
    for slide in prs.slides:
        for shape, _ in _texts(slide):
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    total += len(run.text)
                    if run.font.name:
                        families[run.font.name] += len(run.text)
    rare = {name for name, chars in families.items() if chars < RARE_FONT_SHARE * total}
    changes = 0
    for slide in prs.slides:
        for ph in list(slide.placeholders):
            if ph.has_text_frame and not ph.text_frame.text.strip():
                ph._element.getparent().remove(ph._element)
                changes += 1
        for shape, _ in _texts(slide):
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.font.name in rare:
                        run.font.name = None
                        changes += 1
    prs.save(str(target))
    return changes


def _latest_deck(pitch: Path) -> Path | None:
    decks = sorted(pitch.glob("*_deck_v*.pptx"),
                   key=lambda p: int(m.group(1)) if (m := re.search(r"_v(\d+)\.pptx$", p.name)) else 0)
    return decks[-1] if decks else None


def _next_version(path: Path) -> Path:
    match = re.match(r"^(.*_deck_v)(\d+)\.pptx$", path.name)
    if not match:
        return path.with_name(path.stem + "_fixed.pptx")
    stem = match.group(1)
    versions = [int(m.group(1)) for p in path.parent.glob(f"{stem}*.pptx")
                if (m := re.search(r"_v(\d+)\.pptx$", p.name))]
    return path.with_name(f"{stem}{max(versions) + 1}.pptx")


def write_report(project: Path, deck: Path, findings: Sequence[Finding]) -> Path:
    lines = [f"# Deck audit - {deck.name}", "",
             f"{sum(f.severity == 'ERROR' for f in findings)} errors, {sum(f.severity == 'WARN' for f in findings)} warnings.",
             "", "| Slide | Severity | Check | Finding |", "|---|---|---|---|"]
    lines += [f"| {f.slide or 'deck'} | {f.severity} | {f.code} | {f.message} |" for f in findings]
    lines += ["", "Structural checks only: open the deck in PowerPoint and look at every slide before presenting."]
    report = project / "pitch" / "deck-audit.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the pitch deck (and optionally apply mechanical fixes).")
    parser.add_argument("--project", default=".", help="Team project folder")
    parser.add_argument("--deck", help="Deck to audit (default: newest pitch/<TICKER>_deck_v<N>.pptx)")
    parser.add_argument("--fix", action="store_true", help="Save a new version with mechanical fixes")
    args = parser.parse_args(argv)
    project = Path(args.project).resolve()
    deck = Path(args.deck).resolve() if args.deck else _latest_deck(project / "pitch")
    if deck is None or not deck.is_file():
        print("[x] no deck found: build it with build_pptx.py or pass --deck <file>")
        return EXIT_NO_DECK
    try:
        if args.fix:
            fixed = _next_version(deck)
            changes = fix(deck, fixed)
            print(f"[ok] {changes} mechanical fixes -> pitch/{ascii_safe(fixed.name)}")
            deck = fixed
        findings = audit(deck, project)
        report = write_report(project, deck, findings)
    except PackageNotFoundError:
        print(f"[x] {ascii_safe(deck.name)} is not a valid .pptx file")
        return EXIT_NO_DECK
    except OSError as exc:
        print(f"[x] Could not write: {ascii_safe(exc.strerror or str(exc))}. Close the file and run again.")
        return EXIT_IO_ERROR
    errors = sum(f.severity == "ERROR" for f in findings)
    print(f"audited {ascii_safe(deck.name)}: {errors} errors, {len(findings) - errors} warnings")
    for f in findings:
        where = "deck" if f.slide == 0 else f"slide {f.slide}"
        print(f"[{'x' if f.severity == 'ERROR' else 'warn'}] {where}: {ascii_safe(f.message)}")
    print(f"[ok] report -> pitch/{report.name}")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
