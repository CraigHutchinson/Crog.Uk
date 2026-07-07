#!/usr/bin/env python3
"""Check the heat-pump dataset (and optionally posts) for dead links.

Reads every URL in _data/heat_pumps.yml (site / datasheet / brochure / mcs) and,
with --posts, any Markdown links in _posts/. Each URL is requested concurrently
and classified OK / REDIRECT / BROKEN. A summary report is printed and, with
--report, written to a Markdown file for follow-up.

Exit code is non-zero when broken links are found, so this can gate CI later.

Usage:
    python tools/check_links.py                     # dataset links only
    python tools/check_links.py --posts             # also scan _posts/*.md
    python tools/check_links.py --report links-report.md
"""
from __future__ import annotations

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

import requests

try:
    import yaml
except ImportError:  # pragma: no cover - guidance only
    yaml = None

USER_AGENT = (
    "Mozilla/5.0 (compatible; crog.uk-linkcheck/1.0; +https://crog.uk)"
)
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "heat_pumps.yml"
POSTS_DIR = REPO_ROOT / "_posts"
LINK_KEYS = ("site", "datasheet", "brochure", "mcs")
MD_LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)")


@dataclass
class LinkResult:
    url: str
    source: str
    status: int | None
    note: str

    @property
    def state(self) -> str:
        if self.status is None:
            return "BROKEN"
        if self.status >= 400:
            return "BROKEN"
        if 300 <= self.status < 400:
            return "REDIRECT"
        return "OK"


def collect_dataset_links() -> dict[str, set[str]]:
    """Map url -> set of 'Manufacturer Model (key)' sources."""
    if yaml is None:
        raise SystemExit("PyYAML is required: pip install -r tools/requirements.txt")
    with DATA_FILE.open(encoding="utf-8") as fh:
        entries = yaml.safe_load(fh) or []
    links: dict[str, set[str]] = {}
    for entry in entries:
        label = f"{entry.get('manufacturer', '?')} {entry.get('model', '?')}"
        for key in LINK_KEYS:
            url = (entry.get("links") or {}).get(key)
            if url:
                links.setdefault(url, set()).add(f"{label} [{key}]")
    return links


def collect_post_links() -> dict[str, set[str]]:
    links: dict[str, set[str]] = {}
    for md in sorted(POSTS_DIR.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for url in MD_LINK_RE.findall(text):
            links.setdefault(url, set()).add(md.name)
    return links


def check_url(url: str, source: str, timeout: float) -> LinkResult:
    headers = {"User-Agent": USER_AGENT}
    try:
        # HEAD first; many servers reject it, so fall back to a ranged GET.
        resp = requests.head(url, headers=headers, allow_redirects=True, timeout=timeout)
        if resp.status_code >= 400 or resp.status_code == 405:
            resp = requests.get(
                url, headers={**headers, "Range": "bytes=0-0"},
                allow_redirects=True, timeout=timeout, stream=True,
            )
            resp.close()
        note = "" if not resp.history else f"-> {resp.url}"
        return LinkResult(url, source, resp.status_code, note)
    except requests.RequestException as exc:
        return LinkResult(url, source, None, type(exc).__name__)


def run(links: dict[str, set[str]], workers: int, timeout: float) -> list[LinkResult]:
    results: list[LinkResult] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(check_url, url, "; ".join(sorted(src)), timeout): url
            for url, src in links.items()
        }
        for fut in as_completed(futures):
            results.append(fut.result())
    return sorted(results, key=lambda r: (r.state != "BROKEN", r.url))


def render_report(results: list[LinkResult]) -> str:
    broken = [r for r in results if r.state == "BROKEN"]
    redirects = [r for r in results if r.state == "REDIRECT"]
    lines = ["# Link check report", ""]
    lines.append(f"- Total: {len(results)}")
    lines.append(f"- Broken: {len(broken)}")
    lines.append(f"- Redirects: {len(redirects)}")
    lines.append("")
    if broken:
        lines += ["## Broken", "", "| Status | URL | Used by |", "| --- | --- | --- |"]
        for r in broken:
            lines.append(f"| {r.status or r.note} | {r.url} | {r.source} |")
        lines.append("")
    if redirects:
        lines += ["## Redirects", "", "| Status | URL | Used by | Note |", "| --- | --- | --- | --- |"]
        for r in redirects:
            lines.append(f"| {r.status} | {r.url} | {r.source} | {r.note} |")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--posts", action="store_true", help="also scan _posts/*.md for links")
    parser.add_argument("--workers", type=int, default=12, help="concurrent requests (default 12)")
    parser.add_argument("--timeout", type=float, default=20.0, help="per-request timeout seconds")
    parser.add_argument("--report", type=Path, default=None, help="write a Markdown report to this path")
    args = parser.parse_args(argv)

    links = collect_dataset_links()
    if args.posts:
        for url, src in collect_post_links().items():
            links.setdefault(url, set()).update(src)

    if not links:
        print("No links found.")
        return 0

    print(f"Checking {len(links)} unique URL(s)...", file=sys.stderr)
    results = run(links, args.workers, args.timeout)

    for r in results:
        print(f"[{r.state:8}] {r.status or r.note:>18}  {r.url}")

    report = render_report(results)
    if args.report:
        args.report.write_text(report, encoding="utf-8")
        print(f"\nReport written to {args.report}", file=sys.stderr)

    broken = sum(1 for r in results if r.state == "BROKEN")
    print(f"\n{broken} broken / {len(results)} total.", file=sys.stderr)
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
