# Keyword-research fixture collection — agent instructions

Client folder (all write paths are relative to it): `/home/invoi/fahad_projects/clients/globallocksmiths.com.au/content`
It already exists and already contains `research/raw/`. Write there. Do **not** create a
`clients/` subdirectory, do not create `research/raw/` yourself.

Your dispatch prompt gives you three variables: **ENTRY**, **KEYWORD**, **SLUG**.

## Call these 6 tools, in order, ONE AT A TIME

Never call them in parallel — parallel calls close the shared MCP connection mid-response
and lose fixtures. Write each raw response to disk **before** making the next call.

| # | Tool | Arguments | Write to |
|---|---|---|---|
| 1 | `mcp__plugin_content_dataforseo__serp_organic_live_advanced` | `keyword` KEYWORD, `location_name` **`"Melbourne,Victoria,Australia"`**, `language_code` `"en"`, `depth` 10 | `research/raw/serp-organic-SLUG.json` |
| 2 | `mcp__plugin_content_dataforseo__dataforseo_labs_google_keyword_overview` | `keywords` `[KEYWORD]`, `location_name` `"Australia"`, `language_code` `"en"` | `research/raw/keyword-overview-SLUG.json` |
| 3 | `mcp__plugin_content_dataforseo__dataforseo_labs_search_intent` | `keywords` `[KEYWORD]`, `language_code` `"en"` — **ONLY these two**; this endpoint has NO `location_name` parameter and sending one errors | `research/raw/search-intent-SLUG.json` |
| 4 | `mcp__plugin_content_dataforseo__ai_optimization_chat_gpt_scraper` | `keyword` KEYWORD, `language_code` `"en"`, `location_name` `"Australia"` | `research/raw/ai-overview-SLUG.json` |
| 5 | `mcp__plugin_content_dataforseo__dataforseo_labs_google_keyword_suggestions` | `keyword` KEYWORD, `location_name` `"Australia"`, `language_code` `"en"`, `limit` 30 — higher limits blow the harness token ceiling and the call is rejected | `research/raw/keyword-suggestions-SLUG.json` |
| 6 | `mcp__plugin_content_dataforseo__dataforseo_labs_google_related_keywords` | `keyword` KEYWORD, `location_name` `"Australia"`, `language_code` `"en"` | `research/raw/related-keywords-SLUG.json` |

Calls **1–4 are REQUIRED**. Calls 5–6 are best-effort: attempt them, tolerate per-call
failure. Do **not** call brave-local — it is not part of keyword research.

### Why only call 1 gets the city-scoped location

Call 1 (`serp_organic_live_advanced`) is the **only** endpoint here that accepts a
hierarchical `City,Region,Country` location, and it **must** get
`"Melbourne,Victoria,Australia"`. Analyst-approved 2026-07-30: with a bare `"Australia"`,
UK-homonym suburbs return UK businesses — `smart lock installation brighton` pulled
`bn-locksmith.co.uk` ("Brighton, Hove & Sussex"), `lockrite.org`, and Checkatrade pricing
in **£**. City scoping replaced those with the real Melbourne local pack. About 15 of these
41 suburbs are UK/US homonyms, so this is not optional.

Calls 2, 5 and 6 are DataForSEO Labs endpoints whose `location_name` is documented as
**country format only** ("not City or Region") — passing a city there errors or silently
misbehaves. Call 4's scraper is likewise country-level. So those four keep
`"Australia"` exactly as written in the table. Do not "helpfully" propagate the city
to them.

Call 4 is the ChatGPT scraper, **not** Google's AI Overview. Treat `sources` as that
engine's citations only, and an empty `sources` list as "engine cited nothing" — never as
an open citation slot that content can claim.

## Known data condition — expected, not an error

Every suburb keyword in this project is **absent from the DataForSEO keyword database**
(orchestrator-verified on direct probes). Confirmed live on the first two entries:

- call 2 `keyword-overview` → `items: []`
- call 5 `keyword-suggestions` → `items: []`
- call 6 `related-keywords` → `items: []`
- call 3 `search-intent` → **populated** (it is a classifier, not a database lookup)
- call 1 `serp-organic` and call 4 `ai-overview` → **populated with real data**

Write the empty responses **verbatim anyway** and move on. An empty result is a real
measured signal. Do **not** retry in a loop, do **not** widen the location, and above all
do **not** substitute a shorter or different keyword to force a non-empty result —
silently researching a keyword the page does not target is worse than an empty fixture.

## Write verbatim

Full MCP response JSON. No reformatting, no partial extraction, no hand-wrapping, no
dropping fields. The Python synthesizer reads these back through `FixtureDataProvider`;
deviations break synthesis **silently** and produce zero-signal output that looks fine.

Do not invoke synthesis yourself — the orchestrator runs `scripts.run_synthesis` after all
dispatches.

## Cardinal rule

Full persona: `/home/invoi/.claude/plugins/cache/colana-mp/content/0.17.0/agents/research-agent.md`
(ignore its YAML frontmatter). The rule that governs everything: **every signal must come
from a real API response.** Never estimate a search volume, never invent a PAA question,
never fabricate a competitor structure. If a call fails, record the failure and move on —
do not fill the gap from training data. Missing data is a finding; fabricated data is a lie
that ships to a real client's live page.

Quota exhausted → HALT immediately and report which quota. Transient network error →
retry 3× with backoff (2s/8s/30s). Persistent failure of one call → skip it, continue.

## Report

Exactly this, nothing else: the 6 filenames with byte sizes, and for calls 2/3/5/6 whether
`items` was populated or empty.
