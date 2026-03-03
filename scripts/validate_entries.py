#!/usr/bin/env python3
"""Validate data/entries.yaml schema, categories, tags, and minimum coverage."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_PATH = ROOT / "data" / "entries.yaml"

ALLOWED_CATEGORIES = {
    "datasets",
    "lightweight_architectures",
    "attention_modules",
    "distillation",
    "quantization_pruning_compression",
    "on_device_benchmarking_tooling",
    "reproducible_benchmarks_leaderboards",
    "edge_har_starter_packs",
}

ALLOWED_TAGS = {
    "paper",
    "code",
    "dataset",
    "efficient",
    "on-device",
    "benchmark",
    "distillation",
    "attention",
    "quantization",
    "pruning",
    "tooling",
}

MIN_COUNTS = {
    "datasets": 12,
    "lightweight_architectures": 12,
    "distillation": 8,
    "quantization_pruning_compression": 8,
    "on_device_benchmarking_tooling": 6,
}

REQUIRED_KEYS = {"category", "title", "tags", "links", "description"}
OPTIONAL_KEYS = {"year", "notes"}
URL_RE = re.compile(r"^https?://")


def estimate_sentence_count(text: str) -> int:
    parts = re.split(r"[.!?]+", text.strip())
    return len([p for p in parts if p.strip()])


def main() -> int:
    errors: list[str] = []

    if not ENTRIES_PATH.exists():
        print(f"ERROR: missing file: {ENTRIES_PATH}")
        return 1

    try:
        payload = yaml.safe_load(ENTRIES_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - parser error path
        print(f"ERROR: failed to parse YAML: {exc}")
        return 1

    if not isinstance(payload, dict) or "entries" not in payload:
        errors.append("Top-level YAML must be a mapping containing key 'entries'.")
        payload = {"entries": []}

    entries = payload.get("entries")
    if not isinstance(entries, list):
        errors.append("'entries' must be a list.")
        entries = []

    category_counts: Counter[str] = Counter()
    seen_keys: set[tuple[str, str]] = set()

    for idx, entry in enumerate(entries, start=1):
        prefix = f"Entry #{idx}"

        if not isinstance(entry, dict):
            errors.append(f"{prefix}: must be a mapping.")
            continue

        keys = set(entry.keys())
        missing = REQUIRED_KEYS - keys
        extra = keys - REQUIRED_KEYS - OPTIONAL_KEYS
        if missing:
            errors.append(f"{prefix}: missing required keys: {sorted(missing)}")
        if extra:
            errors.append(f"{prefix}: unknown keys: {sorted(extra)}")

        category = entry.get("category")
        if category not in ALLOWED_CATEGORIES:
            errors.append(f"{prefix}: invalid category '{category}'.")
        else:
            category_counts[category] += 1

        title = entry.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{prefix}: title must be a non-empty string.")
        else:
            key = (category, title.strip().lower())
            if key in seen_keys:
                errors.append(f"{prefix}: duplicate title in category: '{title}'.")
            seen_keys.add(key)

        year = entry.get("year")
        if year is not None and not isinstance(year, int):
            errors.append(f"{prefix}: year must be an integer when present.")

        tags = entry.get("tags")
        if not isinstance(tags, list) or not tags:
            errors.append(f"{prefix}: tags must be a non-empty list.")
        else:
            if len(tags) != len(set(tags)):
                errors.append(f"{prefix}: tags list contains duplicates.")
            for tag in tags:
                if tag not in ALLOWED_TAGS:
                    errors.append(f"{prefix}: invalid tag '{tag}'.")

        links = entry.get("links")
        if not isinstance(links, dict) or not links:
            errors.append(f"{prefix}: links must be a non-empty mapping.")
        else:
            for link_name, link_value in links.items():
                if not isinstance(link_name, str) or not link_name.strip():
                    errors.append(f"{prefix}: link keys must be non-empty strings.")
                if not isinstance(link_value, str) or not link_value.strip():
                    errors.append(f"{prefix}: link '{link_name}' must be a non-empty string.")
                if isinstance(link_value, str) and link_name != "placeholder":
                    if not URL_RE.match(link_value.strip()):
                        errors.append(
                            f"{prefix}: link '{link_name}' should be http(s) URL or use key 'placeholder'."
                        )

        description = entry.get("description")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{prefix}: description must be a non-empty string.")
        else:
            sentences = estimate_sentence_count(description)
            if sentences > 2:
                errors.append(f"{prefix}: description should be 1-2 sentences (found {sentences}).")

        notes = entry.get("notes")
        if notes is not None and not isinstance(notes, str):
            errors.append(f"{prefix}: notes must be a string when present.")

    for category, minimum in MIN_COUNTS.items():
        found = category_counts.get(category, 0)
        if found < minimum:
            errors.append(
                f"Minimum count not met for '{category}': required {minimum}, found {found}."
            )

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Validation passed.")
    print(f"- Total entries: {len(entries)}")
    for category in sorted(category_counts):
        print(f"- {category}: {category_counts[category]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
