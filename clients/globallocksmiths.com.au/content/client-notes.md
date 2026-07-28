## Content Restrictions

**Team-size language — UNRESOLVED, treat as restrictive until the client confirms.**
Form 2 Q1 states "Only have 1 employee". Both forms elsewhere use plural-team
language ("our team of expert locksmiths", "our entire expert team", "our
locksmiths", "technical and management staff"). Until the analyst confirms actual
headcount, do NOT write plural-staff claims — no "our team of locksmiths", no "our
technicians", no "our staff". Attribute expertise to the named licensed Master
Locksmith (Shane Tipping) or to the business, not to an unverified team.
Source: client-profile.json `_conflicts[0]`.

**Tenure — use one figure only.** Three tenures appear across the forms: established
2002 (form 1 Q3), "25+ years" (form 1 Q7, form 2 Q2), and "around 20 years" (form 2
Q13, Q21). 2002 is the only hard date and is the retained value. Derive tenure from
2002 alone; never let two different year counts appear across the 41 pages.
Source: client-profile.json `_conflicts[1]`.

**Operating hours — never state the office hours alone.** "Monday to Friday 9am to
5pm" is OFFICE hours. The mobile locksmith service runs 24/7 with a typical 30–60
minute response (form 2 Q9, Q19). Any mention of the 9–5 window must be paired with
the 24/7 mobile availability, or the page implies the business is unreachable after
5pm — the exact defect flagged in the 21 May 2026 content-additions document.
Source: client-profile.json `_conflicts[2]`.

## Raw Notes

**Intake data gaps — 2026-07-28, recorded at `/content:init`.** Neither form supplied
these; they were left empty rather than guessed (Cardinal rule):

- **No street address or postcode.** `business_address` is omitted from
  client-profile.json, so the `business_address_integrity` audit gate has no fixed
  NAP to protect. Form 2 Q21 names three Melbourne locations — Altona North,
  Camberwell, Hoppers Crossing — but with no street address or postcode for any of
  them. Note that Altona North and Hoppers Crossing are themselves two of the 41
  target suburbs; those two pages can legitimately claim a local base once the
  addresses are confirmed.
- **No brand voice or tone.** Neither form asked. `brand.voice` and `brand.tone` are
  absent, so `voice-profile.md` stays thin until approved content is ingested via
  `/content:ingest-approved`.
- **No banned terms** stated by the client.
- **No competitors** named.
- **No review count.** Only the 5-star average (form 2 Q20) — "thousands of satisfied
  customers" is not a countable review figure.
- **Only 3 of 5 customer questions** supplied (form 2 Q17). Useful FAQ seed but short
  of the requested five.

**Existing smart-lock article.** Form 2 Q5 supplies
`https://globallocksmiths.com.au/are-smart-locks-worth-it-a-local-locksmiths-honest-take/`
— an existing published piece on the exact topic of this 41-page cluster. Strong
candidate as a voice-corpus seed (`/content:ingest-approved`) and as an internal-link
target for every page in the cluster.

**Cluster scope vs client keyword brief.** Form 1 Q11 names three target services —
"locksmiths", "mobile locksmith", "smart lock installation" — and asks for Melbourne
and Geelong. The Meta File supplied for this run covers only `smart lock installation`
across 41 Melbourne suburbs, with no Geelong URLs. The other two service roots and
Geelong are out of scope for this intake.
