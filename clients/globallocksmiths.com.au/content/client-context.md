# globallocksmiths.com.au — Content Plugin Context

_Rebuilt: 2026-07-31T06:04:41Z_

## 1. Who this client is

- **Domain:** globallocksmiths.com.au
- **Brand voice:** CORPUS-DERIVED (not client-stated) — measured across the 6 approved pages, 7,295 words, 2026-07-30. Second person and direct: 'you/your' 33x per 1k words, outpacing 'we/our' at 24x — the copy talks to the customer about their property, not about the company. Plain-English explanatory register: defines the technology before selling it, benefit-led rather than spec-led, moderate 18-word average sentence. Contractions are normal (14x per 1k). Reassurance is the recurring note — 'peace of mind' appears 19 times, 'worry' 10 — paired with 'quality' (40) and 'trusted' (33). Occasional light exclamation on location pages. Practitioner authority is claimed by experience, not credentials-first ('As a trusted locksmith service in Melbourne, we've worked with countless homeowners'). Australian English. The free no-obligation quote is the standing CTA (25 mentions).
- **Audience:** Our ideal customers span a broad range of situations and needs. We serve residential homeowners who need lock installations, repairs, rekeying after moving into a new home, or lockout assistance. We also work with commercial property owners and businesses — including office and corporate buildings, retail shops, supermarkets and shopping centres, medical centres and aged care facilities, schools and TAFE centres, and government buildings. Additionally, we work with architects, builders and trades professionals. Our customers are typically Melbourne and Geelong residents and businesses who value security, reliability, and quality workmanship, and who want a licensed, insured, and accredited locksmith they can trust.
- **Services:** Advanced Locking Solutions, Commercial Door Locks, Deadlocks, Digital Locks, General Locks, Hardware, Key Replacement & Repair, Lock Bumping, Lock Change & Installation, Lock Fitting and Servicing, Lock Maintenance, Lock Repairs, Mobile Locksmith Services, Rekeying & Key Systems, Safe Installation, Safes & Security Solutions, Smart Lock Installation, Specialty Locks & Security
- **Locations served:** Melbourne, South Melbourne, South Yarra, Port Melbourne, Docklands, Richmond, Toorak, Prahran, St Kilda, Brighton, Hawthorn, Kew, Essendon, Moonee Ponds, Ascot Vale, Kensington, Flemington, Footscray, Yarraville, Seddon, Kingsville, Spotswood, Newport, Williamstown, Altona, Altona North, Maribyrnong, Maidstone, Braybrook, Sunshine, Sunshine West, Deer Park, St Albans, Caroline Springs, Point Cook, Williams Landing, Truganina, Tarneit, Hoppers Crossing, Werribee, Wyndham Vale

## 2. Notes from the analyst

## Content Restrictions

_All three items below were RESOLVED by the analyst on 2026-07-28. These are now
binding instructions, not open questions. Full trail in `client-profile.json`
`_conflicts[]`._

**NO 24/7. NO emergency service. NO response-time claims.** The business operates
**Monday to Friday, 9am to 5pm** — that is the whole offer. Form 2 (Q9, Q19, Q21)
claimed 24/7 mobile availability and a 30–60 minute response; the analyst has
confirmed that is wrong. Never write "24/7", "around the clock", "any time of day
or night", "after hours", "emergency locksmith", "emergency callout", or any
arrival-time promise. Lockout work itself is still a service the business
performs — write it without urgency framing. The 24/7 USP was deleted from the
profile and "emergency lockout assistance" was trimmed to "lockout assistance" in
`brand.audience`, because that field arms the honesty gate's capability tokens.

**Tenure — write "since 2002", never a year-count.** Established 2002 (form 1 Q3)
is the single approved fact. Do NOT write "over 25 years", "around 20 years",
"24 years of experience", or any other duration — a hardcoded year-count is correct
the day it ships and wrong a year later. `years_of_combined_experience` was removed
from the profile so it cannot be picked up.

**Team language is APPROVED.** Form 2 Q1's "Only have 1 employee" counts staff
besides the owner. The business is founder Shane Tipping plus 1 employee — two
people, which is a team. Plural-team phrasing ("our team", "our locksmiths") is
cleared for use. Do not inflate beyond that: no claims implying a large crew,
multiple simultaneous jobs, or depth of staffing.

**NO physical presence anywhere. No branch, depot, office, showroom or local base.**
Analyst-confirmed 2026-07-29: the business is not physically present in Altona
North, Camberwell, Hoppers Crossing, or any of the 41 target suburbs. Form 2 Q21's
"three locations across Melbourne" does not mean premises — that USP was deleted
and those three localities were removed from `signature_data_patterns`. This is a
**mobile service** (`operating_model: mobile_service_area`): locksmiths travel to
the customer. `business_address` is deliberately absent from the profile — it is
not a data gap to be filled. Never write "our Brighton branch", "based in
Richmond", "visit us in Werribee", "your local Toorak workshop", or any phrasing
that implies a fixed presence in a target suburb. Proximity language must describe
travel to the customer, not a location the business occupies.

## Content Preferences

**`smart lock installation melbourne` is the SERVICE HUB, not a suburb page.**
Analyst decision 2026-07-29. That entry is now `page_type: service` in cluster
`service-hubs`; the other 40 remain `service-location` in
`service-location-smart-lock-installation`. Write it as the metro-wide pillar the
40 suburb pages link up to — broader scope, covers the service end-to-end, not a
41st near-identical local page.

## Raw Notes

**Intake data gaps — 2026-07-28, recorded at `/content:init`.** Neither form supplied
these; they were left empty rather than guessed (Cardinal rule):

- ~~No street address or postcode.~~ **SUPERSEDED 2026-07-29 — see Content
  Restrictions. `business_address` is deliberately absent, not a gap. Do not chase
  an address; there isn't one to find.**
- **No brand voice or tone.** Neither form asked. `brand.voice` and `brand.tone` are
  absent, so `voice-profile.md` stays thin until approved content is ingested via
  `/content:ingest-approved`.
- **No banned terms** stated by the client.
- **No competitors** named.
- **No review count.** Only the 5-star average (form 2 Q20) — "thousands of satisfied
  customers" is not a countable review figure.
- **Only 3 of 5 customer questions** supplied (form 2 Q17). Useful FAQ seed but short
  of the requested five.

**The live site contradicts the client's own corrections — 2026-07-29.** Six pages
were fetched for voice corpus. The homepage and both sampled suburb pages
(`/brighton/`, `/richmond/`) advertise "24 hours a day, 7 days a week", "an
emergency lockout in the middle of the night", "we typically arrive within 30 to 60
minutes", and "over fifteen years" — every one of which the analyst has ruled out.
Brighton's title tag is "Locksmith Brighton | Fast 24/7 Mobile", so the claim looks
templated across the site's ~90 suburb pages (2 sampled, not verified site-wide).

**RESOLVED 2026-07-30 — scrubbed then ingested (analyst option 1).** 21 sentences
and list items were dropped across the six pages: every unit asserting 24/7
availability, emergency service, an arrival-time promise, or a tenure year-count.
Whole units were removed rather than edited, so all 7,295 remaining words are
verbatim client copy. Residual scan: zero hits. `corpus_operational_truth.json`
carries no banned assertion. The scrub is recorded in the event log with per-file
counts.

**The live site is still wrong, by design of the client's timeline.** The 24/7 and
emergency claims remain published; the client will correct them at the next website
update. So: our 41 new pages must not carry those claims, while the existing ~90
suburb pages still do. Expect a temporary inconsistency between old and new pages,
and re-check the live copy before any future corpus refresh — a re-ingest from an
uncorrected site would re-import the same claims.

**37 of the 41 target suburbs already have a root-level page** (`/brighton/`,
`/richmond/`, …) targeting general locksmith intent. The 4 without one are
`altona-north`, `sunshine-west`, `williams-landing` and `melbourne`. The new
`/smart-lock-installation-<suburb>/` pages will sit alongside these, so the two
sets need distinct angles and should interlink rather than compete.

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

