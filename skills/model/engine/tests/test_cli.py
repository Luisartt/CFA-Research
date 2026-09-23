from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import ENGINE_DIR, HISTORY, write_project
from rcmodel.cli import main, next_version_path


def test_build_writes_workbook_and_summary(project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(project)]) == 0
    assert (project / "model" / "ACME_model_v1.xlsx").is_file()
    summary = json.loads((project / "model" / "model-summary.json").read_text(encoding="utf-8"))
    assert summary["status"] in {"ALL CHECKS OK", "OK WITH WARNINGS"}
    assert summary["lines"]["revenue"]["2026"] == pytest.approx(13400 * 1.07)
    assert summary["lines"]["fcff"]["2021"] is None
    assert "price_gordon" in summary["valuation"]
    assert "target_12m_gordon" in summary["valuation"]
    assert summary["model_file"] == "ACME_model_v1.xlsx"
    out = capsys.readouterr().out
    assert out.isascii()
    assert "[ok] workbook -> model/ACME_model_v1.xlsx" in out


def test_second_build_bumps_the_version(project: Path) -> None:
    assert main(["--project", str(project)]) == 0
    assert main(["--project", str(project)]) == 0
    assert (project / "model" / "ACME_model_v1.xlsx").is_file()
    assert (project / "model" / "ACME_model_v2.xlsx").is_file()


def test_input_errors_exit_2_with_ascii_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "cash"}
    write_project(tmp_path, history=history)
    assert main(["--project", str(tmp_path)]) == 2
    out = capsys.readouterr().out
    assert out.isascii() and "cash" in out


def test_next_version_ignores_other_files(tmp_path: Path) -> None:
    (tmp_path / "ACME_model_v3.xlsx").write_bytes(b"")
    (tmp_path / "notes.xlsx").write_bytes(b"")
    path, version = next_version_path(tmp_path, "ACME")
    assert (path.name, version) == ("ACME_model_v4.xlsx", 4)


def test_ticker_is_made_filename_safe(tmp_path: Path) -> None:
    path, _ = next_version_path(tmp_path, "GFNORTE O")
    assert path.name == "GFNORTE-O_model_v1.xlsx"


def test_launcher_runs(project: Path) -> None:
    completed = subprocess.run(
        [sys.executable, str(ENGINE_DIR / "build_model.py"), "--project", str(project)],
        capture_output=True, text=True, check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert (project / "model" / "ACME_model_v1.xlsx").is_file()
