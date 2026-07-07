#!/usr/bin/env python3
"""Pull heat-pump records from the MCS Product Directory.

MCS figures are the source of truth for SCOP on crog.uk, so this tool fetches
the live directory and reconciles it against _data/heat_pumps.yml.

It uses the directory's official JSON API (discovered from the site's WordPress
REST index) rather than scraping rendered HTML:

    GET https://mcscertified.com/wp-json/custom/v1/products
        ?search=<kw>&page=<n>&per_page=<n>

Observed API quirks (2026-07), which drive the design below:
  * `technology_type` is accepted but DOES NOT filter - the endpoint returns the
    whole directory (~264k products across all technologies). We therefore filter
    to Air Source Heat Pump client-side on the `TechnologyType` field.
  * `total_items` / `total_pages` are the global directory totals, not the
    filtered count, so we page until an empty batch instead of trusting them.
  * `search` matches a single token in the product Name only (e.g. `aroTHERM`,
    `Ecodan`); model numbers, multiword terms and certificate codes return
    nothing. Good for ad-hoc lookups, useless for reconcile.
  * SCOP lives in a `SCOPValues` map keyed by flow temperature; `Code` holds the
    certificate (often prefixed `MCS `, e.g. `MCS HP0002/47`).

Because of the above, `--reconcile` works against a locally cached full pull of
the ASHP set (build/refresh it with `--refresh-cache`).

Coverage caveat (verified 2026-07): the endpoint only serves ~130k of its claimed
264k rows before returning empty pages, and that slice skews to OLDER
certifications (~1,550 ASHP, mostly legacy models). Many current 2023-2025 models
are not reachable this way, so `--reconcile` reports how many certificates it
actually matched -- "Matched 0/N" means nothing was verified, not that our figures
are correct. Verify such models manually on the website.

Typical use:
    python tools/fetch_mcs.py --raw --search aroTHERM     # inspect JSON shape
    python tools/fetch_mcs.py --search aroTHERM           # ad-hoc name lookup
    python tools/fetch_mcs.py --refresh-cache             # pull all ASHP -> cache
    python tools/fetch_mcs.py --reconcile                 # diff cache vs dataset

Nothing is written back to _data automatically; the operator stays in the loop.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any, Iterable

import requests

try:
    import yaml
except ImportError:  # pragma: no cover - guidance only
    yaml = None

API_URL = "https://mcscertified.com/wp-json/custom/v1/products"
ASHP_TECHNOLOGY = "Air Source Heat Pump"  # value of the TechnologyType field
USER_AGENT = "crog.uk-heatpump-tool/1.0 (+https://crog.uk; contact croguk-contact@crog.uk)"
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "heat_pumps.yml"
CACHE_FILE = Path(__file__).resolve().parent / ".mcs_cache.json"

# Candidate JSON keys for each logical field, in priority order. The MCS API
# (custom/v1/products) currently uses the PascalCase names below; earlier aliases
# are kept as fallbacks in case the schema shifts. SCOP figures live in a nested
# `SCOPValues` map keyed by flow temperature (see _scop() below), not here.
FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "manufacturer": ("Manufacturer", "manufacturer", "company", "brand"),
    "model": ("ModelNumber", "Name", "model", "model_number", "title"),
    "certificate": ("Code", "certificate", "certificate_number", "cert_number"),
    "technology": ("TechnologyType", "technology", "type"),
    "technology_subtype": ("TechnologySubType", "technology_subtype"),
    "certified_from": ("CertifiedFrom", "certified_from", "valid_from"),
    "certified_to": ("CertifiedTo", "certified_to", "valid_to"),
    "period": ("CertificationPeriod", "certification_period"),
    "description": ("Description", "description"),
    "peak_power": ("PeakPowerOutput", "peak_power"),
    "url": ("Website", "url", "permalink", "link"),
}

# SCOP flow temperatures we surface (MCS reports every degree 35..65).
SCOP_TEMPS = ("35", "45", "55")


def _pick(record: dict[str, Any], logical: str) -> Any:
    """Return the first present alias value for a logical field (case-insensitive)."""
    lowered = {k.lower(): v for k, v in record.items()}
    for alias in FIELD_ALIASES[logical]:
        if alias in record and record[alias] not in (None, ""):
            return record[alias]
        if alias in lowered and lowered[alias] not in (None, ""):
            return lowered[alias]
    return None


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
    return s


def fetch_products(
    session: requests.Session,
    *,
    search: str | None = None,
    per_page: int = 200,
    max_pages: int = 50,
    delay: float = 0.3,
    ashp_only: bool = False,
    progress: bool = False,
) -> list[dict[str, Any]]:
    """Page through the products endpoint and return raw records.

    Pages until an empty batch (the API's total_pages is unreliable). With
    ``ashp_only`` the results are filtered client-side to Air Source Heat Pump,
    since the server-side technology filter does not work.
    """
    results: list[dict[str, Any]] = []
    for page in range(1, max_pages + 1):
        params: dict[str, Any] = {"page": page, "per_page": per_page}
        if search:
            params["search"] = search
        resp = session.get(API_URL, params=params, timeout=60)
        resp.raise_for_status()
        batch = _extract_records(resp.json())
        # Stop only on an empty page: this API returns variable-size pages, so a
        # short page is NOT a reliable end-of-data signal.
        if not batch:
            break
        results.extend(r for r in batch if not ashp_only or _is_ashp(r))
        if progress and page % 25 == 0:
            print(f"  ...page {page}: {len(results)} kept so far", file=sys.stderr)
        time.sleep(delay)
    return results


def _is_ashp(record: dict[str, Any]) -> bool:
    return str(record.get("TechnologyType", "")).strip().lower() == ASHP_TECHNOLOGY.lower()


def _extract_records(payload: Any) -> list[dict[str, Any]]:
    """The API may wrap the list (e.g. {"data": [...]}) or return a bare list."""
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    if isinstance(payload, dict):
        for key in ("data", "results", "products", "items"):
            value = payload.get(key)
            if isinstance(value, list):
                return [r for r in value if isinstance(r, dict)]
    return []


def _scop(record: dict[str, Any], temp: str) -> float | None:
    """Read SCOP at a flow temperature from the nested SCOPValues map."""
    values = record.get("SCOPValues") or record.get("scop_values")
    if isinstance(values, dict):
        raw = values.get(temp) or values.get(int(temp) if temp.isdigit() else temp)
        try:
            num = float(raw)
        except (TypeError, ValueError):
            return None
        return num if num > 0 else None  # MCS uses 0 as "not measured"
    return None


def normalise(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for r in records:
        out.append(
            {
                "manufacturer": _pick(r, "manufacturer"),
                "model": _pick(r, "model"),
                "certificate": _pick(r, "certificate"),
                "scop_35": _scop(r, "35"),
                "scop_45": _scop(r, "45"),
                "scop_55": _scop(r, "55"),
                "certified_from": _pick(r, "certified_from"),
                "certified_to": _pick(r, "certified_to"),
                "period": _pick(r, "period"),
                "description": _pick(r, "description"),
                "url": _pick(r, "url"),
            }
        )
    return out


def load_dataset() -> list[dict[str, Any]]:
    if yaml is None:
        raise SystemExit("PyYAML is required: pip install -r tools/requirements.txt")
    if not DATA_FILE.exists():
        raise SystemExit(f"Dataset not found: {DATA_FILE}")
    with DATA_FILE.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or []


def build_cache(session: requests.Session, *, per_page: int, max_pages: int, delay: float) -> list[dict[str, Any]]:
    """Pull the whole directory, keep Air Source Heat Pumps, cache normalised rows."""
    print("Refreshing MCS ASHP cache (full-directory pull, this takes a few minutes)...", file=sys.stderr)
    records = fetch_products(
        session, per_page=per_page, max_pages=max_pages, delay=delay, ashp_only=True, progress=True
    )
    rows = normalise(records)
    CACHE_FILE.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Cached {len(rows)} ASHP record(s) to {CACHE_FILE}", file=sys.stderr)
    return rows


def load_cache() -> list[dict[str, Any]] | None:
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    return None


def _norm_cert(value: Any) -> str:
    return "".join(str(value or "").split()).upper().replace("MCS", "")


def reconcile(mcs_rows: list[dict[str, Any]]) -> int:
    """Diff MCS SCOP figures against our dataset by certificate number.

    Also reports how many of our certificates were actually found in the MCS
    data, because the API cannot surface every product (see module docstring):
    a "0 matched" result means the reconcile could not verify anything, NOT that
    our figures are correct.
    """
    dataset = load_dataset()
    by_cert = {_norm_cert(e.get("mcs_cert")): e for e in dataset if e.get("mcs_cert")}
    mcs_by_cert = {_norm_cert(r.get("certificate")): r for r in mcs_rows if r.get("certificate")}

    matched: list[str] = []
    findings = 0
    for cert, ours in by_cert.items():
        row = mcs_by_cert.get(cert)
        if row is None:
            continue
        matched.append(ours.get("mcs_cert"))
        for temp in ("35", "45", "55"):
            mcs_val = row.get(f"scop_{temp}")
            our_val = ours.get(f"scop_{temp}")
            if mcs_val is None:
                continue
            try:
                if our_val is None or abs(float(mcs_val) - float(our_val)) > 0.001:
                    findings += 1
                    print(
                        f"[DIFF] {ours['manufacturer']} {ours['model']} "
                        f"SCOP@{temp}: ours={our_val} MCS={mcs_val} (cert {ours['mcs_cert']})"
                    )
            except (TypeError, ValueError):
                continue

    total = len(by_cert)
    print(
        f"\nMatched {len(matched)}/{total} dataset certificate(s) against "
        f"{len(mcs_by_cert)} cached MCS record(s).",
        file=sys.stderr,
    )
    if not matched:
        print(
            "WARNING: no certificates matched. The MCS API could not surface our "
            "models (its crawl/search does not reach every product), so nothing was "
            "verified. Check specific products manually at "
            "https://mcscertified.com/product-directory/ .",
            file=sys.stderr,
        )
    elif findings == 0:
        print("No SCOP discrepancies among matched certificates.")
    else:
        print(f"{findings} discrepancy field(s) found. Review and update _data/heat_pumps.yml.")
    return findings


def search_keys(session: requests.Session, *, per_page: int, delay: float) -> int:
    """Use each entry's `mcs_search` key to pull candidate MCS records for review.

    The API cannot address a product by certificate, so for models that carry a
    search key this lists the candidates the token returns (flagging an exact
    certificate match when present) for manual confirmation.
    """
    dataset = load_dataset()
    entries = [e for e in dataset if e.get("mcs_search")]
    missing = [e for e in dataset if e.get("mcs_cert") and not e.get("mcs_search")]
    print(f"Querying {len(entries)} model(s) with an mcs_search key...\n", file=sys.stderr)
    for e in entries:
        term = e["mcs_search"]
        recs = normalise(
            fetch_products(session, search=term, per_page=per_page, max_pages=3, delay=delay)
        )
        ncert = _norm_cert(e.get("mcs_cert"))
        exact = [r for r in recs if _norm_cert(r.get("certificate")) == ncert]
        flag = "EXACT cert match" if exact else f"{len(recs)} candidate(s), no exact cert"
        print(f'{e["manufacturer"]} {e["model"]}  (search="{term}", cert={e.get("mcs_cert")}): {flag}')
        for r in (exact or recs)[:4]:
            print(
                f'    {str(r.get("certificate")):22} {str(r.get("model"))[:34]:34} '
                f'SCOP={r["scop_35"]}/{r["scop_45"]}/{r["scop_55"]}'
            )
    if missing:
        print(f"\n{len(missing)} MCS model(s) have no search key (not surfaced by the API):", file=sys.stderr)
        for e in missing:
            print(f'  - {e["manufacturer"]} {e["model"]} (cert {e["mcs_cert"]})', file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--search", default=None, help="ad-hoc name lookup (single token, e.g. aroTHERM)")
    parser.add_argument("--per-page", type=int, default=200, help="page size (default 200)")
    parser.add_argument("--max-pages", type=int, default=2000, help="safety cap on pages for a full pull")
    parser.add_argument("--delay", type=float, default=0.3, help="seconds between page requests")
    parser.add_argument("--raw", action="store_true", help="print raw JSON of the first page and exit")
    parser.add_argument("--refresh-cache", action="store_true", help="pull all ASHP records into the local cache")
    parser.add_argument("--reconcile", action="store_true", help="diff cached MCS SCOP vs _data/heat_pumps.yml")
    parser.add_argument("--search-keys", action="store_true", help="pull candidates per model using each entry's mcs_search key")
    args = parser.parse_args(argv)

    session = _session()

    if args.raw:
        params: dict[str, Any] = {"page": 1, "per_page": args.per_page}
        if args.search:
            params["search"] = args.search
        resp = session.get(API_URL, params=params, timeout=30)
        resp.raise_for_status()
        print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
        return 0

    if args.search_keys:
        return search_keys(session, per_page=50, delay=args.delay)

    if args.refresh_cache:
        build_cache(session, per_page=args.per_page, max_pages=args.max_pages, delay=args.delay)
        if not args.reconcile:
            return 0

    if args.reconcile:
        rows = load_cache()
        if rows is None:
            rows = build_cache(session, per_page=args.per_page, max_pages=args.max_pages, delay=args.delay)
        return 1 if reconcile(rows) else 0

    # Default / --search: ad-hoc listing (name search is the only working filter).
    # Kept to a small sample of pages; use --refresh-cache for a full pull.
    rows = normalise(
        fetch_products(
            session,
            search=args.search,
            per_page=args.per_page,
            max_pages=5,
            delay=args.delay,
            ashp_only=True,
        )
    )
    print(f"Fetched {len(rows)} ASHP record(s).", file=sys.stderr)
    for row in rows:
        print(
            f"{row['manufacturer'] or '?':30} {row['model'] or '?':30} "
            f"cert={row['certificate'] or '-':20} "
            f"SCOP={row['scop_35']}/{row['scop_45']}/{row['scop_55']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
