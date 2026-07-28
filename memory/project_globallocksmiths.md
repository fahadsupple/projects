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

## The thing that will bite — sole operator vs plural-team copy
Form 2 Q1 says **"Only have 1 employee"**, but both forms are written throughout in
plural-team voice ("our team of expert locksmiths", "our entire expert team"). This
is unresolved with the client. Any generated page using plural-staff language is a
credibility claim the business may not be able to support. Recorded in
`client-profile.json _conflicts[0]` and in `client-notes.md` (which reaches
`client-context.md`, the file every downstream agent loads). Same pattern for tenure
(2002 vs "25+ years" vs "around 20 years") and hours (Mon–Fri 9–5 is OFFICE hours;
the mobile service is 24/7 — never state one without the other).

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
