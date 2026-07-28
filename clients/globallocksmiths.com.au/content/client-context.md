# globallocksmiths.com.au — Content Plugin Context

_Rebuilt: 2026-07-28T04:24:47Z_

## 1. Who this client is

- **Domain:** globallocksmiths.com.au
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

