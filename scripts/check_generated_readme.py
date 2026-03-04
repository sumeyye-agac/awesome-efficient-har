#!/usr/bin/env python3
"""Fail if README.md is not in sync with data/entries.yaml generation."""

from __future__ import annotations

from difflib import unified_diff
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.generate_readme import ENTRIES_PATH, README_PATH, load_entries, render_readme


def main() -> int:
    entries = load_entries(ENTRIES_PATH)
    expected = render_readme(entries)
    actual = README_PATH.read_text(encoding="utf-8")

    if actual == expected:
        print("README.md is up-to-date with data/entries.yaml.")
        return 0

    diff = "\n".join(
        unified_diff(
            actual.splitlines(),
            expected.splitlines(),
            fromfile="README.md",
            tofile="generated README",
            lineterm="",
        )
    )
    print("README.md drift detected.")
    print("Run: python scripts/generate_readme.py")
    print("Diff preview:")
    print(diff)
    return 1


if __name__ == "__main__":
    sys.exit(main())
