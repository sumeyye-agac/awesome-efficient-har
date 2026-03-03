#!/usr/bin/env python3
"""Generate README.md from data/entries.yaml deterministically."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_PATH = ROOT / "data" / "entries.yaml"
README_PATH = ROOT / "README.md"

TAG_LABELS = {
    "paper": "[📄 paper]",
    "code": "[💻 code]",
    "dataset": "[📦 dataset]",
    "efficient": "[⚡ efficient]",
    "on-device": "[📱 on-device]",
    "benchmark": "[🧪 benchmark]",
    "distillation": "[🧠 distillation]",
    "attention": "[🧩 attention]",
    "quantization": "[🔧 quantization]",
    "pruning": "[🪓 pruning]",
    "tooling": "[🧰 tooling]",
}

CATEGORY_SECTIONS = [
    ("datasets", "1) Datasets (wearable/IMU/multimodal)"),
    ("lightweight_architectures", "2) Lightweight architectures for time-series"),
    ("attention_modules", "3) Attention modules for sensor/time-series"),
    ("distillation", "4) Knowledge distillation for HAR/time-series"),
    ("quantization_pruning_compression", "5) Quantization/pruning/compression"),
    ("on_device_benchmarking_tooling", "6) On-device benchmarking and tooling"),
    ("reproducible_benchmarks_leaderboards", "7) Reproducible benchmarks/leaderboards"),
]

def load_entries(path: Path) -> list[dict]:
    content = yaml.safe_load(path.read_text(encoding="utf-8"))
    entries = content.get("entries", []) if isinstance(content, dict) else []
    if not isinstance(entries, list):
        raise ValueError("entries.yaml must contain a top-level 'entries' list")
    return entries


def select_link(links: dict) -> tuple[str | None, str | None]:
    if not isinstance(links, dict) or not links:
        return None, None

    priority = [
        "official",
        "paper",
        "dataset",
        "code",
        "docs",
        "benchmark",
        "leaderboard",
        "template",
        "placeholder",
    ]
    for key in priority:
        if key in links:
            return key, links[key]

    first_key = sorted(links.keys())[0]
    return first_key, links[first_key]


def format_entry(entry: dict) -> str:
    title = entry["title"].strip()
    year = entry.get("year")
    description = entry["description"].strip()
    notes = entry.get("notes")

    link_key, link_value = select_link(entry.get("links", {}))
    if isinstance(link_value, str) and link_value.startswith(("http://", "https://")):
        title_part = f"[{title}]({link_value})"
    elif isinstance(link_value, str) and link_value:
        title_part = f"`{title}` ({link_value})"
    else:
        title_part = title

    if year is not None:
        title_part += f" ({year})"

    tags = entry.get("tags", [])
    tag_str = " ".join(TAG_LABELS[tag] for tag in tags if tag in TAG_LABELS)

    suffix = "" if description.endswith((".", "!", "?")) else "."
    line = f"- {title_part} - {description}{suffix}"
    if notes:
        line += f" ({notes})"
    if tag_str:
        line += f" `{tag_str}`"
    return line


def render_readme(entries: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        grouped[entry["category"]].append(entry)

    lines: list[str] = []
    lines.append("# awesome-efficient-har")
    lines.append("")
    lines.append("A curated list of resources for **efficient, edge, and wearable Human Activity Recognition (HAR)**.")
    lines.append("")
    lines.append("Focus areas:")
    lines.append("- wearable and smartphone sensor data (IMU, multimodal)")
    lines.append("- compact models for time-series HAR")
    lines.append("- on-device deployment and reliable benchmarking")
    lines.append("")
    lines.append("This README is generated from `data/entries.yaml` via `scripts/generate_readme.py`.")
    lines.append("")
    lines.append("## Legend")
    lines.append("")
    lines.append("`[📄 paper]` `[💻 code]` `[📦 dataset]` `[⚡ efficient]` `[📱 on-device]` `[🧪 benchmark]` `[🧠 distillation]` `[🧩 attention]` `[🔧 quantization]` `[🪓 pruning]` `[🧰 tooling]`")
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    lines.append("1. [Datasets (wearable/IMU/multimodal)](#1-datasets-wearableimumultimodal)")
    lines.append("2. [Lightweight architectures for time-series](#2-lightweight-architectures-for-time-series)")
    lines.append("3. [Attention modules for sensor/time-series](#3-attention-modules-for-sensortime-series)")
    lines.append("4. [Knowledge distillation for HAR/time-series](#4-knowledge-distillation-for-hartime-series)")
    lines.append("5. [Quantization/pruning/compression](#5-quantizationpruningcompression)")
    lines.append("6. [On-device benchmarking and tooling](#6-on-device-benchmarking-and-tooling)")
    lines.append("7. [Reproducible benchmarks/leaderboards](#7-reproducible-benchmarksleaderboards)")
    lines.append("8. [Deployment patterns (windowing/streaming/personalization)](#8-deployment-patterns-windowingstreamingpersonalization)")
    lines.append("9. [Efficiency reporting checklist for HAR papers](#efficiency-reporting-checklist-for-har-papers)")
    lines.append("10. [Edge HAR starter packs](#edge-har-starter-packs)")
    lines.append("")

    for category, heading in CATEGORY_SECTIONS:
        lines.append(f"## {heading}")
        lines.append("")
        for entry in grouped.get(category, []):
            lines.append(format_entry(entry))
        lines.append("")

    lines.append("## 8) Deployment patterns (windowing/streaming/personalization)")
    lines.append("")
    lines.append("- **Windowing policy**: Report window length, stride, overlap, and label-assignment rule; avoid hidden overlap leakage between train and test.")
    lines.append("- **Streaming inference**: Prefer causal feature extraction and stateful models for low-latency online HAR.")
    lines.append("- **Subject split discipline**: Always separate users across train/val/test when claiming generalization.")
    lines.append("- **Personalization track**: Report both cold-start (no user fine-tune) and adaptation (few-shot or calibration) metrics.")
    lines.append("- **Fallback behavior**: Define unknown/transition states and confidence thresholds for real-world deployment.")
    lines.append("- **Battery-accuracy tradeoff**: Jointly report duty cycle, sampling rate, and latency.")
    lines.append("")
    lines.append("## Efficiency reporting checklist for HAR papers")
    lines.append("")
    lines.append("Report these metrics together:")
    lines.append("- Parameter count")
    lines.append("- MACs/FLOPs (for stated input window)")
    lines.append("- End-to-end latency on target hardware")
    lines.append("- Peak memory (RAM and model size)")
    lines.append("- Energy proxy (power draw, battery drain rate, or joules/inference)")
    lines.append("")
    lines.append("Common pitfalls to document and avoid:")
    lines.append("- Window leakage from overlap across data splits")
    lines.append("- Subject split mistakes (random split instead of subject-wise split)")
    lines.append("- Personalization evaluation without clear adaptation budget or protocol")
    lines.append("")
    lines.append("## Edge HAR starter packs")
    lines.append("")
    for entry in grouped.get("edge_har_starter_packs", []):
        lines.append(format_entry(entry))
    lines.append("")
    lines.append("## Related recipes")
    lines.append("")
    lines.append("- [Knowledge distillation recipe](recipes/knowledge_distillation.md)")
    lines.append("- [TFLite int8 export recipe](recipes/tflite_int8_export.md)")
    lines.append("- [Android latency benchmark recipe](recipes/android_latency_benchmark.md)")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("List content is released under [CC0-1.0](LICENSE).")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    entries = load_entries(ENTRIES_PATH)
    readme = render_readme(entries)
    README_PATH.write_text(readme, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
