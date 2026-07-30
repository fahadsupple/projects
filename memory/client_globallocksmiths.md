---
name: client-globallocksmiths
description: Global Locksmiths — mobile locksmith Melbourne/Geelong; content research complete 30 Jul 2026 (41 entries, 40 suburb pairs); 40/41 keywords absent from volume DB, geo contamination on 10 entries, fetch_brave_local plugin defect
metadata:
  type: project
---

**Global Locksmiths Pty Ltd** (globallocksmiths.com.au) — mobile locksmith, Melbourne
Metro + Geelong. Founder Shane Tipping, established 2002, ABN 43 969 968 576,
1300 333 565. Formerly traded as Newmans Locksmiths. MLAA + ANZLA accredited.
Existing site ~163 pages.

## Content plugin state (as at 2026-07-28)
`/content:init` complete — greenfield, content plugin v0.17.0, folder
`clients/globallocksmiths.com.au/content/`. 41 entries, one cluster
`service-location-smart-lock-installation`, all `mode: new-page` (every target URL
returned 404 on the pre-intake probe). `operating_model: mobile_service_area`.
`business_type_tokens: [locksmith, safe_installation]` — the safety_critical +
audience_tone audit adapters are armed, so ordinary security phrasing ("weak
points", "easy access") will trip blocking findings during audit.

## `/content:research` complete — 2026-07-30
Both clusters done. Keyword leg: 246 raw fixtures (41 × 6 endpoints), 41 bundles,
`run_synthesis --all` exit 0, zero zero-signal failures. Suburb leg: 40 pairs,
`operating_model: mobile_service_area` → full physical 5-key contract, 10 local
signals per bundle. Next phase: `/content:plan`.

**Two settings that must not be reverted on any re-run.** SERP calls take
`location_name: "Melbourne,Victoria,Australia"` — the spec's task template hardcodes
bare `"Australia"`, which pulls UK businesses on the ~15 homonym suburbs. The Labs
endpoints (`keyword_overview`, `keyword_suggestions`, `related_keywords`) and the
ChatGPT scraper accept **country format only**, so those stay `"Australia"`; passing a
city errors. Brave needs `country: "AU"` (it defaults to `US`).

## The volume data does not exist, and the plugin says it does
**40 of the 41 keywords are absent from the DataForSEO keyword database** — no record,
not zero volume. Verified on single-keyword probes, not just the bulk call. Only
`smart lock installation melbourne` has data (90/mo, commercial, comp 0.93, CPC $6.07).
`search-intent` **is** populated for all 41 because it is a classifier, not a DB lookup.

The trap: `research_completeness` records whether a fixture **file exists**, so those
117-byte `items: []` fixtures report `present` with `absent_endpoints: []`. The
endpoint-aware layer cannot see this, and no WARN fires. **A bundle can be running on
no volume signal at all and still look complete.** Written up in
`content/research/geo-contamination-qa.md` because nothing in the tooling will say it.

## Geo contamination — three modes, only one fixable by parameters
10 of 41 entries flagged. See `content/research/geo-contamination-qa.md` and
`geo-qa.json`; reproduce with `research/qa_geo_contamination.py`.

1. **International homonym** — city scoping fixed most, but `checkatrade.com` (UK trade
   directory, £ pricing) **survives** it because it is a `.com`, so any `.co.uk` TLD
   filter misses it. Confirmed on brighton, maidstone, st-albans, williamstown. On
   williamstown it sits inside a **`people_also_ask` answer**, and PAA feeds
   `/content:faq` — so a UK answer can reach an FAQ block.
2. **Interstate homonym** — `sunshine` resolves largely to **Sunshine Coast QLD** (SERP
   organic 6 of 9 QLD; Google's own related_searches say "sunshine coast"). City scoping
   **cannot** fix this; the competing entity is stronger nationally. Use that entry's
   local pack + Airtasker only.
3. **AI-probe country ceiling** — `chat_gpt_scraper` cannot be city-scoped at all.
   `maidstone` came back 100% Kent UK: 0 VIC mentions, 8 UK TLDs, £ pricing. That
   fixture is unusable and its `sources` are not citation slots we can claim.

Also: **`deer-park` returned zero `local_pack`** (knowledge_graph instead) — a fact, not
a collection failure; don't retry expecting a different shape.

## Suburb research is legitimately thin on homonym suburbs
The geo guard told agents to discard wrong-place records, so several bundles are honestly
sparse rather than richly wrong. Worst: **kensington 10 of 10 discarded** (double
homonym — London borough *and* the Kensington laptop-lock brand), all five keys
insufficient; **st-albans 8 of 10**; **richmond 6 of 10** (Richmond BC + Virginia);
**newport 7 of 10**; **sunshine 7 of 10**. St-albans is the cautionary one — every
record describing door stock was UK (uPVC, anti-snap, Ultion/Nuki), copy that would read
as obviously foreign on a Melbourne page. **A thin honest bundle beats a rich wrong one**;
if these need filling, re-query with an explicit disambiguator (`kensington vic 3031 …`)
— for *suburb* research the query is an instrument, not a ranking target, so
disambiguating it is legitimate, unlike keyword research.

## Plugin defect — `fetch_brave_local` silently loses the evidence trail
Without the Brave Pro local plan, the MCP response is a prose notice **concatenated with
the JSON objects on one line**. `_coerce_json_stream`'s notice-plus-NDJSON branch splits
on newlines so it never matches, and whole-text `raw_decode` fails on the leading prose →
`fetch_brave_local` returns the empty stub. Effect is silent and nasty: bundles get
`local_signals: []` while `synthesis` stays fully populated, so the evidence vanishes and
the bundle still validates. Worked around in `content/research/run_suburb_bundles.py`
(`BraveNoticeSalvagingProvider`, scans from the first brace); the installed plugin was
**not** modified. Upstream fix would be to strip the non-JSON prefix before `raw_decode`.

## Unresolved — `globallocksmiths.net.au`
Surfaced repeatedly across suburb research with a full regional path structure
(`/western-suburbs/locksmiths-altona/`, `/northern-suburbs/locksmith-ascot-vale/`,
`/eastern-suburbs/…`, `/western-suburbs/locksmith-werribee`) and snippets advertising
"24/7 emergency lockout assistance" — a claim the client does not support. It is in **no**
client record, and the domain **does not resolve** from here. Ask the client whether it is
theirs: if it is, we are building 40 pages alongside a parallel site on the same suburbs.

## The forms overstate the offer — analyst corrections, 2026-07-28
All three intake conflicts are RESOLVED. The corrections matter more than the form
text, because **form 2 makes claims the business cannot support**:

- **No 24/7. No emergency service. No response-time promise.** Mon–Fri 9am–5pm is
  the whole offer. Form 2 Q9/Q19/Q21 claimed 24/7 mobile availability and 30–60 min
  arrival — wrong. The 24/7 USP was deleted and "emergency lockout assistance" was
  trimmed to "lockout assistance" in `brand.audience`, because that field arms
  `honesty_audit`'s capability-token pool: leaving the word there would have marked
  "emergency" as a *supported* claim and let it through the gate. Lockout work
  itself is still in scope, just without urgency framing.
- **Tenure: write "since 2002", never a year-count.** A hardcoded "over 25 years"
  ships correct and goes stale. `years_of_combined_experience` was removed from the
  profile so the writer can't emit it.
- **Team language is fine.** "Only have 1 employee" counts staff besides the owner,
  so it's Shane + 1 = 2 people = a team.

Trail lives in `client-profile.json _conflicts[]` (each with `resolution`) and in
`client-notes.md`, which is what reaches `client-context.md` — the file every
downstream agent loads. `_conflicts` itself is analyst-facing only; no agent reads it.

## The live site contradicts the client's own corrections
Fetched 6 pages for voice corpus on 2026-07-29. The homepage and the suburb pages
advertise "24 hours a day, 7 days a week", "emergency lockout in the middle of the
night", "arrive within 30 to 60 minutes" and "over fifteen years" — all four ruled
out by the analyst. Brighton's title tag is "Locksmith Brighton | Fast 24/7 Mobile",
so it looks templated site-wide. **The client is advertising a service they don't
provide** — they will fix it at the next website update, so the live pages stay wrong
in the meantime while our 41 new pages must not repeat the claims.

The trap worth remembering: `approved/*.md` isn't just a style reference —
`rebuild_corpus_operational_truth()` parses it into the writer's *operational ground
truth* and `rebuild_voice_profile()` builds the voice anchor from it. Ingesting a
site whose copy contradicts the client's own corrections silently re-arms every
banned claim across the whole run. **Always diff a client's live copy against their
stated corrections before ingesting voice**, and re-check before any corpus refresh.

Resolved 2026-07-30 by scrubbing then ingesting (analyst option 1): dropped 21 whole
sentences/list-items carrying a banned claim, so all 7,295 surviving words stay
verbatim. Zero residual hits. `brand.voice`/`brand.tone` were empty (no form question
covered them), so both are now **corpus-derived and labelled CORPUS-DERIVED** with
measured evidence — you/your 33x per 1k vs we/our 24x, "peace of mind" 19x, 18-word
average sentence, free-quote CTA 25x. Client-stated voice, if ever given, supersedes.

Also found: **37 of the 41 target suburbs already have a root-level page**
(`/brighton/` etc.) on general locksmith intent. Only altona-north, sunshine-west,
williams-landing and melbourne don't. New smart-lock pages sit alongside these.

## No physical presence
Analyst-confirmed 2026-07-29: no premises anywhere — not in Altona North,
Camberwell or Hoppers Crossing (form 2 Q21's "three locations" is not premises),
and not in any target suburb. `business_address` is deliberately absent, not a gap.
Mobile service only. No branch/depot/showroom/"based in X" language on any page.

## Cluster shape
`smart lock installation melbourne` = `page_type: service`, cluster `service-hubs`
(analyst decision 2026-07-29 — metro-wide pillar). The other 40 stay
`service-location` in `service-location-smart-lock-installation` and link up to it.

## Scope boundary
Form 1 Q11 asked for three service roots (locksmiths, mobile locksmith, smart lock
installation) across Melbourne **and Geelong**. The Meta File covers only smart lock
installation across 41 Melbourne suburbs — no Geelong, no other root. Expect the
client to ask for the rest later.

## Gaps the forms never filled
No street address or postcode (so `business_address` is omitted and the
business_address_integrity gate is inert) — but three locations are named: Altona
North, Camberwell, Hoppers Crossing, two of which are target suburbs. No brand
voice/tone, no banned terms, no competitors, no review count.
`client-facts.json` flags two `needs_confirmation` facts that are extractor noise,
not real data — `social-proof.clients` scraped digits out of the ABN and phone
number; do not confirm it.

Related: [[capability_keyword_url_mapping]], [[feedback_seo_location_page_rules]]
