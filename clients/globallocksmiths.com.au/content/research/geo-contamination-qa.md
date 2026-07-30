# Geo-contamination QA — keyword research fixtures

**Client:** globallocksmiths.com.au · **Cluster scope:** all 41 entries
**Run date:** 2026-07-30 · **Fixtures scanned:** 246 (41 entries × 6 endpoints)
**Result:** 31 entries clean · **10 flagged**

## Why this file exists

The 41 target keywords are bare `smart lock installation <suburb>` strings with no city
qualifier, and several suburb names collide with places outside Melbourne. The plugin's
own `research_completeness` manifest records only whether a fixture **file exists** — so a
fixture that is present, well-formed and about the wrong country reads as `present` with
`absent_endpoints: []`. Nothing in the pipeline flags it. This file is that flag.

**A flagged fixture's prices, competitors and citations are not Melbourne ground truth.**

## Three distinct failure modes

| Mode | Cause | Fixable by location param? |
|---|---|---|
| **International homonym** | Brighton/Sussex, Maidstone/Kent, St Albans/Herts | Mostly — but `checkatrade.com` survives |
| **Interstate homonym** | "Sunshine" → Sunshine Coast QLD | **No** — competing entity is stronger nationally |
| **AI-probe country ceiling** | `chat_gpt_scraper` takes country-level location only | **No** — cannot be city-scoped at all |

SERP calls use `location_name: "Melbourne,Victoria,Australia"` (analyst-approved
2026-07-30). The DataForSEO Labs endpoints and the ChatGPT scraper accept country format
only, so they run on `"Australia"` and cannot be narrowed.

## Flagged entries

### Severe — do not use these fixtures for the stated purpose

**`maidstone` — `ai-overview` fixture is entirely UK (Kent).**
GBP pricing ×2, UK TLDs ×8, Checkatrade references ×9, **zero** Victoria/Melbourne
mentions. All four brand entities are `.co.uk`; both citations are UK. The SERP fixture
for this entry is fine (Melbourne local pack, Airtasker `maidstone-vic`) — it is
specifically the AI fixture that is unusable. Its £100–280 range must never appear as an
Australian price, and its `sources` are not citation slots this client can claim.

**`sunshine` — SERP organic is majority Sunshine Coast QLD.**
QLD signals ×15 against only 9 VIC mentions, plus an `(07)` phone number. Six of nine
organic results are QLD/Brisbane businesses (`lockmaster.com.au`, `avidlocksmiths.com.au`,
`astillselectrical.com.au`, `coastlocks.com.au`, `localsearch.com.au/…/sunshine-coast-qld`),
and Google's own `related_searches` echo "sunshine coast" and "Brisbane". City scoping
repaired the **local pack** (correctly Sunshine VIC) but could not repair organic.
→ For this entry, weight competitor signal to the **local pack + Airtasker only**. The
`ai-overview` fixture resolved correctly to Sunshine VIC and is the better source here.

### Moderate — one bad result each, rest of fixture usable

| Entry | Flag | Detail |
|---|---|---|
| `brighton` | intl-organic, gbp-pricing | `checkatrade.com` organic #5 — £102–£281 (Sussex) |
| `st-albans` | intl-organic, gbp-pricing | `checkatrade.com` — £108–£274 (Hertfordshire) |
| `sunshine-west` | interstate-present | QLD ×5 vs VIC ×11 |

### Minor — interstate mentions present but VIC clearly dominant

`flemington` (QLD 3 / NSW 1 vs VIC 18) · `kensington` (QLD 2 / NSW 4 vs VIC 15) ·
`kingsville` (QLD 3 vs VIC 10) · `newport` (NSW 2 / WA 2 vs VIC 18) ·
`seddon` (QLD 2 / NSW 1 vs VIC 12)

These are national-brand pages and directory cross-links, not geographic misresolution.
Usable; no action needed.

## The Checkatrade leak — recurring, cross-cutting

`checkatrade.com` is a UK trade directory that **survives Melbourne city scoping** because
it is a `.com` domain, so it evades any `.co.uk`/`.uk` TLD filter. Confirmed on four
entries — `brighton`, `maidstone`, `st-albans`, `williamstown`.

On `williamstown` it appears inside a **`people_also_ask` answer**, not the organic list.
That matters beyond competitor analysis: PAA questions feed FAQ generation
(`/content:faq` reads PAA + related searches), so a UK answer can reach an FAQ block.
Its "as little as 15 minutes" install timing and all £ figures must not be repeated as
Australian service claims.

## Local-pack coverage (separate data condition)

| local_pack items | Entries |
|---|---|
| 3 | 31 entries |
| 2 | `hoppers-crossing`, `tarneit`, `toorak`, `truganina`, `williams-landing`, `wyndham-vale` |
| **0** | **`deer-park`** |

`deer-park` returned `ai_overview` + `knowledge_graph` + `google_reviews` in place of a
local pack, and no VIC-suburb local businesses. Local-pack-derived signal is empty for
that entry by fact, not by collection failure — do not retry it expecting a different
shape.

## Volume data — absent, project-wide

40 of the 41 keywords are **absent from the DataForSEO keyword database** (not zero
volume — no record at all). Verified on direct single-keyword probes, not just the bulk
call. `keyword-overview`, `keyword-suggestions` and `related-keywords` return `items: []`
(117-byte fixtures) for all 40. Only the hub carries data:

| Keyword | Volume | Intent | Competition | CPC |
|---|---|---|---|---|
| `smart lock installation melbourne` | 90/mo | commercial | 0.93 HIGH | $6.07 |
| the other 40 | absent | — | — | — |

`search-intent` **does** return data for all 41 — it is a classifier, not a database
lookup. Reference points that do have volume: `smart lock installation` (national)
590/mo · `smart locks melbourne` 90/mo · `locksmith brighton` 320/mo (navigational — the
general-locksmith intent the client's existing root-level suburb pages already target).

## Suburb re-query — 7 bundles, 2026-07-30 (analyst-approved)

The first suburb pass used the bare query `<suburb> smart lock installation`. On homonym
suburbs it returned mostly the wrong place, agents correctly discarded those records, and
the bundles came back honestly thin. Seven were re-queried with an explicit disambiguator
(`smart lock installation <Suburb> Melbourne Victoria <postcode>`), `country: "AU"`.

This is legitimate for *suburb* research and would not be for keyword research: a keyword
must match what the page targets, but a suburb query is only an instrument for reaching
ground truth about a place, so naming the state and city is a fix rather than a cheat.
Every re-queried bundle carries `synthesis._requery` with the exact query, date, reason
and discard count.

### Geo integrity: 7 of 7 fixed

| Suburb | Wrong-geo discards, pass 1 → pass 2 | What pass 1 resolved to |
|---|---|---|
| kensington | 10/10 → **0/10** | London borough + Kensington laptop-lock brand |
| st-albans | 8/10 → **0/10** | Hertfordshire, incl. both Checkatrade listings + St Albans **Park** (Geelong) |
| brighton | 7/10 → **0/10** | Sussex/Hove (`01273`), Brisbane, Brighton **Colorado** |
| newport | 7/10 → **0/10** | Wales (`01633`, SA42), Oregon, NSW, QLD |
| sunshine | 7/10 → **0/10** | Sunshine Coast QLD |
| maidstone | 6/10 → **0/10** | Kent (LockRite ×3, Checkatrade ×2) |
| richmond | 6/10 → **0/10** | Richmond BC Canada ×3, Richmond Virginia ×3 |

The uPVC / anti-snap door vocabulary that contaminated st-albans is gone from the set.

### Depth: mixed, and the trade-off is real

**Disambiguation trades contamination for dilution.** Appending "Melbourne Victoria"
reliably kills wrong-place records but also pulls Melbourne-wide vendor and directory
pages that are geographically valid and locally useless.

- **Gained integrity AND depth** — `kensington` (synthesis 401 → 5,841 bytes, 4 of 5 keys
  now filled), `maidstone` (4 → 9 usable records), `st-albans` (4,993 → 9,241 bytes),
  `richmond` (2 → 5 records with suburb-specific detail).
- **Gained integrity, lost depth** — `brighton` (8 of 10 records are Melbourne-wide rolls;
  3 keys still insufficient) and `newport` (8 of 10 diluted; still only 2 load-bearing
  records, though both stronger and one states "Newport VIC 3015" outright).
- **Net trade** — `sunshine` gained geo confidence but lost two pieces of first-pass
  customer language (a pre-bored door needing the old cut-out filled; install-only demand
  where the customer already owns the hardware).

### Overwriting the fixtures cost some complementary evidence

Re-queries overwrote `brave-local-<suburb>-…json` in place, because the Python loader
derives that filename from the canonical `<suburb> <service>` string and will not find a
renamed file. Brave returned *different excerpts of the same URLs* across the two passes,
so some first-pass detail is no longer on disk for `sunshine`, `newport`, `brighton` and
`maidstone`. It is preserved in the commit prior to the re-query and can be merged back if
a page needs that depth. Agents dropped rather than carried those claims, which is correct
under the traceability rule — an unsourced claim is worse than a missing one.

### Brighton — one open judgement call

Pass 1's Brighton texture came from **Brighton East** (3187), a separate suburb. Pass 2
treated that as a wrong-suburb discard, so the bundle is now thinner but strictly sourced.
Brighton East is arguably a fair proxy for bayside building stock *if labelled as
adjacent*; the stricter reading was kept. Analyst may prefer to reinstate it as explicitly
adjacent context.

### Not re-queried, deliberately

Seven further bundles are thin only on `demographic_skew`, and `climate_context` is
insufficient in **all 40** — climate barely bears on indoor door hardware, so that is the
honest answer, not a defect. No query disambiguation makes Brave return resident
demographics, so re-running those would spend quota to reproduce the same result.

### Two competitive facts surfaced, for the cluster plan

- **Smart-lock specialists do not cover the west.** `smartlocksmelbourne.au` publishes ~45
  serviced suburbs running Albert Park → Windsor — bayside and inner south-east, no
  western suburb at all — while general north-west mobile locksmiths do cover 3021.
  Specialisation clusters on the opposite side of the city from St Albans, Sunshine,
  Braybrook, Maidstone and the rest of the western grid.
- **Sunshine's incumbent competes on what this client lacks.** `auslock.com.au` runs a
  "Local Sunshine North Base" leading with 24/7, 35 years and SCEC approval — exactly the
  availability and tenure axes Global Locksmiths cannot claim. Do not meet them there.

Admissible Australian door vocabulary to replace the rejected British terms, from
`thesmartlockshop.com.au` and `smartlockinstallation.com.au`: smart **mortice** locks,
**deadbolts**, fire-rated smart locks for unit doors, and the incumbent hardware brands a
retrofit must mate with — **Lockwood, Lane, Lemaar**.

## Reproduce

```bash
python3 qa_geo_contamination.py <client_dir> --json geo-qa.json
```

Machine-readable output: `geo-qa.json` (per-entry signal counts and verdicts). Note this
scanner reads the **keyword-research** fixtures (`serp-organic-*`, `ai-overview-*`); the
suburb re-query above concerns the `brave-local-*` fixtures and is not reflected in its
counts.
