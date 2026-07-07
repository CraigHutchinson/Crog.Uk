# crog.uk heat-pump tooling

Utilities that keep the SCOP dataset ([`_data/heat_pumps.yml`](../_data/heat_pumps.yml))
accurate. Both scripts are read-only against the site — they never write back to
`_data` automatically, so a human stays in the loop.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r tools/requirements.txt
```

## `fetch_mcs.py` — pull the latest MCS figures

MCS Product Directory figures are the source of truth for SCOP. This tool queries
the directory's official JSON API
(`https://mcscertified.com/wp-json/custom/v1/products`) and reconciles it with our
dataset.

```powershell
# 1. Inspect the raw JSON shape (confirm field names if the API changes)
python tools/fetch_mcs.py --raw --search aroTHERM

# 2. Ad-hoc lookup by product name (single token, e.g. aroTHERM / Ecodan)
python tools/fetch_mcs.py --search aroTHERM

# 3. Refresh the local ASHP cache, then diff SCOP vs our dataset
python tools/fetch_mcs.py --refresh-cache
python tools/fetch_mcs.py --reconcile

# 4. Pull candidates per model using each entry's mcs_search key
python tools/fetch_mcs.py --search-keys
```

Each dataset entry carries an `mcs_search` key — the token that finds its product
line via the API `search` (e.g. `aroTHERM`, `Therma V`, `Ecodan`). `--search-keys`
runs those searches and lists the candidate records (flagging an exact certificate
match when present) so figures can be confirmed by hand. Five current models
(EBac, Aira, Bosch, Ideal, Octopus) have `mcs_search: null` because the API does
not surface them at all — verify those on the website. Extend keys in
`_data/heat_pumps.yml` as new working tokens are found.

`--reconcile` prints `[DIFF]` lines for any SCOP value that differs from MCS
(matched by certificate number); update `_data/heat_pumps.yml` accordingly and
re-run. SCOP comes as a `SCOPValues` map keyed by flow temperature 35–65 °C; the
tool surfaces 35/45/55 and treats `0` as "not measured". Certificates live in the
`Code` field, often prefixed `MCS ` (normalised away when matching).

> **Why a cache?** The MCS API has three quirks that shape this workflow:
> 1. `technology_type` is accepted but does **not** filter — the endpoint returns
>    the whole ~264k-product directory, so the tool filters to Air Source Heat
>    Pump client-side on `TechnologyType`.
> 2. `total_items` / `total_pages` are global totals, so the tool pages until an
>    empty batch rather than trusting them.
> 3. `search` matches a single token in the product **Name** only (`aroTHERM`,
>    `Ecodan`); model numbers, multiword and certificate codes return nothing.
>
> Because of (1)–(3) there is no cheap server-side way to fetch just "our" models,
> so `--refresh-cache` does a full-directory pull (a few minutes) into
> `tools/.mcs_cache.json` and `--reconcile` diffs against that cache.
>
> **Known coverage limit (verified 2026-07):** the endpoint only serves ~130k of
> its claimed 264k rows before returning empty pages, and that reachable slice is
> skewed to **older** certifications. A full crawl currently yields ~1,550 ASHP
> records that are mostly legacy models (e.g. Vaillant aroTHERM `/2`, Samsung
> AE090, Mitsubishi PUHZ) — most of our **current** 2023–2025 models are not in
> it. `--reconcile` therefore prints how many certificates it actually matched;
> **`Matched 0/N` means nothing was verified**, not that figures are correct. For
> those models, confirm SCOP manually via
> <https://mcscertified.com/product-directory/> (search by model on the site) and
> update `_data/heat_pumps.yml` by hand.

## `check_links.py` — find dead links

```powershell
# Dataset links only
python tools/check_links.py

# Also scan Markdown links in _posts/, and write a report
python tools/check_links.py --posts --report links-report.md
```

Exit code is non-zero when broken links are found (suitable for a future CI gate).
`REDIRECT` rows show the final URL so you can update `_data/heat_pumps.yml` to the
canonical target where appropriate.

## Workflow to refresh the table

1. `python tools/fetch_mcs.py --refresh-cache` then `--reconcile` — apply any MCS SCOP changes to the dataset.
2. Add newly certified models to `_data/heat_pumps.yml` (set `status: mcs`).
3. `python tools/check_links.py --posts` — fix or update any broken/redirected links.
4. Rebuild the site (`bundle exec jekyll serve`) and review the rendered table.
