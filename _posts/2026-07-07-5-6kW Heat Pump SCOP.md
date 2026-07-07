---
layout: post
title:  "Comparison of 5-6kW Heat Pumps (2026)"
date:   2026-07-07 09:00:00 +0000
modified_date: 2026-07-07 09:00:00 +0000
categories: HeatPump
datatable: true
pinned: true
---

This is the 2026 refresh of the heat-pump SCOP comparison. The current focus is the
**5&ndash;6kW** range (suitable for a well-insulated ~4&ndash;5kW-demand property), but the
table is now a single **filterable master table** driven from a shared dataset, so larger
outputs can be added over time &mdash; use the search box and the **kW** column to filter/sort.

The data now lives in [`_data/heat_pumps.yml`](https://github.com/CraigHutchinson/Crog.Uk/blob/main/_data/heat_pumps.yml) as a
clean single source of truth, so figures can be de-duplicated, re-ranked and checked by tooling
rather than hand-edited in the table.

Criteria / methodology (unchanged from the [2024 table]({% post_url 2024-02-15-5Kw Heat Pump SCOP %})):

- Target property demand ~4&ndash;5kW; units may cycle if oversized (8kW+).
- EN 14511/14825 Average Climate. Low temp = 35&deg;C, Medium = 45&deg;C, High = 55&deg;C.
- Ordered by SCOP@35&deg;C where higher is better; ambiguous ranks fall back to 45&deg;C then 55&deg;C
  (we prefer mild-weather performance which gives greater yearly SCOP).
- **MCS Product Database figures are the source of truth** and replace datasheet figures where they
  differ &mdash; see [MCS Product Directory](https://mcscertified.com/product-directory/).
- Where a model has **no MCS certification**, published manufacturer/datasheet figures are used
  instead and flagged &#128148; (unverified). Note many manufacturers publish only **COP**, not the
  SCOP@35/45/55 trio, so some newly launched models show no SCOP until they are MCS-certified.
- A `*` on SCOP@45&deg;C means it was estimated as mean(35,55) because the datasheet omitted it
  (a conservative underestimate).

**Status column legend**

| Badge | Meaning |
| :---- | :------ |
| &#128142; | Datasheet matches MCS-verified figures |
| &#128215; | MCS-only or a close match to datasheet |
| &#128216; | MCS present but **not** close to datasheet (MCS used) &mdash; hover the `ds&#8800;` marker for datasheet claims |
| &#128148; | Not validated / unknown &mdash; may be mis-ranked |

`MCS verified`, `Datasheet only` and `Rumoured / no data` in the Status column are searchable
terms &mdash; type one into the search box to isolate that confidence tier.

{% include scop-table.html %}

---

Notes:

- Figures are refreshed from the MCS Product Database using `tools/fetch_mcs.py`; links are
  validated with `tools/check_links.py` (see `tools/README.md`).
- The older [2024 5kW table]({% post_url 2024-02-15-5Kw Heat Pump SCOP %}) is retained for history.

ToDo / research backlog:

- Vaillant aroTHERM plus 2025/26 (improved-spec model expected to reach the UK market in 2026).
- Confirm SCOP + MCS certs for newly announced 2025/26 models and move them from
  `Rumoured / no data` up into a verified tier as figures are published.
