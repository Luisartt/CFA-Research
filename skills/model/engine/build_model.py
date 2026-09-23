"""Launcher for the model engine.

Usage (from the team project folder):
    python <path-to-skill>/engine/build_model.py --project .
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcmodel.cli import main  # noqa: E402

raise SystemExit(main())
