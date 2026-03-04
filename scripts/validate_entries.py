#!/usr/bin/env python3
"""Validate data/entries.yaml schema, quality gates, and ordering."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_PATH = ROOT / "data" / "entries.yaml"

CATEGORY_ORDER = [
    "datasets",
    "lightweight_architectures",
    "attention_modules",
    "distillation",
    "quantization_pruning_compression",
    "on_device_benchmarking_tooling",
    "reproducible_benchmarks_leaderboards",
    "edge_har_starter_packs",
]
ORDER_INDEX = {name: idx for idx, name in enumerate(CATEGORY_ORDER)}
ALLOWED_CATEGORIES = set(CATEGORY_ORDER)

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

REQUIRED_KEYS = {"category", "title", "year", "tags", "links", "description"}
OPTIONAL_KEYS = {"notes"}
URL_RE = re.compile(r"^https?://", re.IGNORECASE)
CURRENT_YEAR = datetime.now(timezone.utc).year


def estimate_sentence_count(text: str) -> int:
    parts = re.split(r"[.!?]+", text.strip())
    return len([p for p in parts if p.strip()])


def normalized_text(value: str) -> str:
    return value.strip()


def sort_key(entry: dict) -> tuple[int, int, str]:
    return (
        ORDER_INDEX.get(entry["category"], 10**9),
        -entry["year"],
        entry["title"].casefold(),
    )


def load_payload(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_payload(
    payload: dict,
    *,
    enforce_min_counts: bool = True,
    enforce_order: bool = True,
) -> list[str]:
    errors: list[str] = []

    if not isinstance(payload, dict) or "entries" not in payload:
        return ["Top-level YAML must be a mapping containing key 'entries'."]

    entries = payload.get("entries")
    if not isinstance(entries, list):
        return ["'entries' must be a list."]

    category_counts: Counter[str] = Counter()
    seen_titles: set[tuple[str, str]] = set()
    seen_links: dict[str, str] = {}
    order_candidates: list[dict] = []

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
        if not isinstance(category, str) or not category:
            errors.append(f"{prefix}: category must be a non-empty string.")
        else:
            if category != normalized_text(category) or category != category.lower():
                errors.append(f"{prefix}: category must be normalized (trimmed lowercase).")
            if category not in ALLOWED_CATEGORIES:
                errors.append(f"{prefix}: invalid category '{category}'.")
            else:
                category_counts[category] += 1

        title = entry.get("title")
        if not isinstance(title, str) or not normalized_text(title):
            errors.append(f"{prefix}: title must be a non-empty string.")
        else:
            if title != normalized_text(title):
                errors.append(f"{prefix}: title must not include leading/trailing whitespace.")
            title_key = ((category or ""), normalized_text(title).casefold())
            if title_key in seen_titles:
                errors.append(f"{prefix}: duplicate title in category: '{title}'.")
            seen_titles.add(title_key)

        year = entry.get("year")
        if not isinstance(year, int):
            errors.append(f"{prefix}: year must be an integer.")
        else:
            if year < 1900 or year > CURRENT_YEAR + 1:
                errors.append(
                    f"{prefix}: year must be between 1900 and {CURRENT_YEAR + 1} (got {year})."
                )

        tags = entry.get("tags")
        if not isinstance(tags, list) or not tags:
            errors.append(f"{prefix}: tags must be a non-empty list.")
        else:
            normalized_tags = []
            for raw_tag in tags:
                if not isinstance(raw_tag, str):
                    errors.append(f"{prefix}: tags must be strings.")
                    continue
                tag = normalized_text(raw_tag).lower()
                normalized_tags.append(tag)
                if raw_tag != tag:
                    errors.append(
                        f"{prefix}: tag '{raw_tag}' must be normalized (trimmed lowercase)."
                    )
                if tag not in ALLOWED_TAGS:
                    errors.append(f"{prefix}: invalid tag '{raw_tag}'.")
            if len(normalized_tags) != len(set(normalized_tags)):
                errors.append(f"{prefix}: tags list contains duplicates.")

        links = entry.get("links")
        if not isinstance(links, dict) or not links:
            errors.append(f"{prefix}: links must be a non-empty mapping.")
        else:
            for link_name, link_value in links.items():
                if not isinstance(link_name, str) or not normalized_text(link_name):
                    errors.append(f"{prefix}: link keys must be non-empty strings.")
                    continue
                if link_name != normalized_text(link_name).lower():
                    errors.append(
                        f"{prefix}: link key '{link_name}' must be normalized (trimmed lowercase)."
                    )
                if not isinstance(link_value, str) or not normalized_text(link_value):
                    errors.append(f"{prefix}: link '{link_name}' must be a non-empty string.")
                    continue

                value = normalized_text(link_value)
                if link_name != "placeholder" and not URL_RE.match(value):
                    errors.append(
                        f"{prefix}: link '{link_name}' should be an http(s) URL or use key 'placeholder'."
                    )

                canonical_link = value.rstrip("/")
                seen_at = seen_links.get(canonical_link)
                if seen_at:
                    errors.append(
                        f"{prefix}: duplicate link '{value}' already used in {seen_at}."
                    )
                else:
                    seen_links[canonical_link] = prefix

        description = entry.get("description")
        if not isinstance(description, str) or not normalized_text(description):
            errors.append(f"{prefix}: description must be a non-empty string.")
        else:
            if description != normalized_text(description):
                errors.append(
                    f"{prefix}: description must not include leading/trailing whitespace."
                )
            sentences = estimate_sentence_count(description)
            if sentences > 2:
                errors.append(f"{prefix}: description should be 1-2 sentences (found {sentences}).")

        notes = entry.get("notes")
        if notes is not None and not isinstance(notes, str):
            errors.append(f"{prefix}: notes must be a string when present.")

        if (
            isinstance(category, str)
            and category in ALLOWED_CATEGORIES
            and isinstance(year, int)
            and isinstance(title, str)
            and normalized_text(title)
        ):
            order_candidates.append(entry)

    if enforce_min_counts:
        for category, minimum in MIN_COUNTS.items():
            found = category_counts.get(category, 0)
            if found < minimum:
                errors.append(
                    f"Minimum count not met for '{category}': required {minimum}, found {found}."
                )

    if enforce_order and len(order_candidates) == len(entries):
        expected = sorted(order_candidates, key=sort_key)
        for idx, (current, wanted) in enumerate(zip(order_candidates, expected), start=1):
            if current is not wanted:
                errors.append(
                    "Entries must be ordered by category, then year (desc), then title. "
                    f"First mismatch at position {idx}: "
                    f"found '{current['title']}' but expected '{wanted['title']}'."
                )
                break

    return errors


def main() -> int:
    if not ENTRIES_PATH.exists():
        print(f"ERROR: missing file: {ENTRIES_PATH}")
        return 1

    try:
        payload = load_payload(ENTRIES_PATH)
    except Exception as exc:  # pragma: no cover - parser error path
        print(f"ERROR: failed to parse YAML: {exc}")
        return 1

    errors = validate_payload(payload)
    entries = payload.get("entries", []) if isinstance(payload, dict) else []

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Validation passed.")
    print(f"- Total entries: {len(entries)}")
    counts = Counter(entry["category"] for entry in entries)
    for category in CATEGORY_ORDER:
        if category in counts:
            print(f"- {category}: {counts[category]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
