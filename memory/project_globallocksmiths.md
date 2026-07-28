---
name: client-globallocksmiths
description: Global Locksmiths — mobile locksmith Melbourne/Geelong; content plugin intake complete 28 Jul 2026, 41 smart-lock suburb pages, sole-operator claim conflict
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
points", "easy access") will trip blocking findings during audit. Next phase:
`/content:research`.

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
