#!/usr/bin/env python3
"""Check external links in README.md and data/entries.yaml."""

from __future__ import annotations

from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

import yaml

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
ENTRIES_PATH = ROOT / "data" / "entries.yaml"

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
HTTP_RE = re.compile(r"^https?://")
ALLOWED_HTTP_ERRORS = {401, 403, 405, 429}
TIMEOUT_SECONDS = 15


def load_markdown_urls(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(MARKDOWN_LINK_RE.findall(text))


def load_yaml_urls(path: Path) -> set[str]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    entries = payload.get("entries", []) if isinstance(payload, dict) else []
    urls: set[str] = set()
    for entry in entries:
        links = entry.get("links", {}) if isinstance(entry, dict) else {}
        if not isinstance(links, dict):
            continue
        for value in links.values():
            if isinstance(value, str) and HTTP_RE.match(value):
                urls.add(value)
    return urls


def check_url(url: str) -> tuple[bool, str]:
    headers = {"User-Agent": "awesome-efficient-har-link-check/1.0"}

    methods = ["HEAD", "GET"]
    last_error = "unknown error"
    for method in methods:
        request = urllib.request.Request(url=url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                status = response.status
                if 200 <= status < 400:
                    return True, f"HTTP {status}"
                last_error = f"HTTP {status}"
        except urllib.error.HTTPError as exc:
            if exc.code in ALLOWED_HTTP_ERRORS:
                return True, f"HTTP {exc.code} (allowed)"
            last_error = f"HTTP {exc.code}"
        except urllib.error.URLError as exc:
            last_error = f"URL error: {exc.reason}"
        except Exception as exc:  # pragma: no cover
            last_error = f"Error: {exc}"
    return False, last_error


def main() -> int:
    urls = set()
    urls |= load_markdown_urls(README_PATH)
    urls |= load_yaml_urls(ENTRIES_PATH)

    if not urls:
        print("No URLs found to check.")
        return 0

    failures: list[tuple[str, str]] = []
    print(f"Checking {len(urls)} URLs...")
    for url in sorted(urls):
        ok, detail = check_url(url)
        status_text = "OK" if ok else "FAIL"
        print(f"[{status_text}] {url} -> {detail}")
        if not ok:
            failures.append((url, detail))

    if failures:
        print("\nLink check failed for the following URLs:")
        for url, detail in failures:
            print(f"- {url}: {detail}")
        return 1

    print("All checked URLs are reachable (or blocked with allowed status codes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
