# Suburb re-query — disambiguated Brave search

Client folder: `/home/invoi/fahad_projects/clients/globallocksmiths.com.au/content`
Service (fixed): **smart lock installation**
`operating_model`: **`mobile_service_area`** → full physical contract, all five keys.

## Why you are re-running a suburb that was already done

The first pass used the bare query `<suburb> smart lock installation`. For your suburb it
returned mostly the **wrong place**, so the previous agent correctly discarded those
records and marked most keys `"Insufficient local data"`. A thin honest bundle was the
right call — but it leaves the page with no local intel, so we are retrying with an
explicit geographic disambiguator.

This is legitimate here and would **not** be legitimate in keyword research. A keyword
must match what the page targets. A *suburb research* query is only an instrument for
reaching ground truth about a place — so naming the state and city is a fix, not a cheat.

## Step 1 — one disambiguated Brave call

Call `mcp__plugin_content_brave-search__brave_local_search` with:

- `query`: **exactly the DISAMBIGUATED QUERY given in your dispatch prompt** (it names
  Melbourne and/or Victoria)
- `country`: **`"AU"`** — mandatory, it defaults to `US`
- `count`: `10`

Expect a plan-unavailable notice followed by a web-search fallback stream. That is the
normal verified shape for this account — not an error, do not retry for it. Brave's Free
plan allows **1 request/second** and sibling agents are running: on HTTP 429, back off
~20–30s and retry, up to 3 times.

Write the **full verbatim** response to — note this is the ORIGINAL undisambiguated
filename, and you are **overwriting** the existing file, which is intended and approved:

```
research/raw/brave-local-<suburb-slug>-smart-lock-installation.json
```

The Python loader derives that filename from the canonical `<suburb> <service>` string, so
it must not change even though the query you sent did. Do not rename it, do not add a
suffix, do not create a second file.

## Step 2 — synthesis

Overwrite `research/raw/_synthesis/<suburb-slug>-smart-lock-installation.json` with a JSON
object carrying the five physical-contract keys:

- `climate_context` — climate's bearing on smart lock installation. Usually marginal for
  indoor door hardware; if no record speaks to it, write
  `"Insufficient local data — recommend manual research"`. Do not invent a weather angle.
- `building_stock` — dominant building types and how they affect **this** service: door
  material and thickness, heritage timber, apartment/common-entrance doors, new-estate
  aluminium/composite, double-glazed sliders.
- `council_notes` — only what bears on changing door hardware (heritage overlays on
  street-facing doors, owners-corporation rules on common property, rental-provider
  obligations). `"None identified"` if nothing.
- `demographic_skew` — who lives there and how it shifts smart-lock demand (renters vs
  owners, families, professionals, short-stay turnover, downsizers).
- `common_concerns` — array of 2–4 concerns, each traceable to a returned record.

Plus one extra key, for the audit trail:

- `_requery` — object with `date`: `"2026-07-30"`, `query`: the exact disambiguated string
  you sent, `reason`: one line on what the first pass failed on, and
  `records_discarded_wrong_geo`: integer.

## The geo guard still applies — disambiguating reduces contamination, it does not remove it

Verified in the first pass: `checkatrade.com` (UK, £ pricing) survives even city-scoped
Google queries, and `st-albans-park` is Victorian but the **wrong suburb** (south-east
Geelong). So still check every record before you use it, and discard:

- **International** — £ or US$ pricing, `.co.uk`, Kent/Sussex/Hertfordshire/London/Wales,
  Checkatrade, US states, Canadian provinces
- **Interstate** — Sunshine Coast, Brisbane, QLD, Perth, Sydney, Adelaide, `(07)`, `(08)`,
  `(02)` numbers
- **Wrong Victorian suburb** — e.g. St Albans **Park** (Geelong) is not St Albans
- **Wrong entity** — a product model or brand that merely shares the suburb's name, or a
  business matched only on the word "lock" (bull-bars, vehicle alcohol interlocks)

**Every claim must trace to a record this call returned.** Your training knowledge about
Melbourne suburbs is not admissible. If disambiguation still leaves you thin, say so —
`"Insufficient local data — recommend manual research"` remains the correct answer, and a
second thin bundle is a legitimate result. Do not stretch a discarded record to fill a key,
and do not write generic filler ("residents value reliable service") that would not change
how a writer writes this specific page.

## Report

The two file paths with byte sizes, how many records Brave returned, how many you
discarded and why, which keys are still insufficient, and one line on whether the
disambiguated query actually improved on the first pass.
