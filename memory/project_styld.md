---
name: styldmelbourne.com.au project
description: STYLD Melbourne — home staging & property styling, Melbourne-wide, 20 general keywords, kwr:init complete 30 Apr 2026
type: project
---

# styldmelbourne.com.au — Project Status

**Why:** Keyword research engagement. STYLD Melbourne is a new (March 2025) home staging and property styling business targeting Melbourne property vendors and real estate agents.

**How to apply:** Local Melbourne service business. Melbourne modifier on all keywords. Home staging = for-sale staging, NOT interior decorating. Check SERP intent carefully for "home styling" (may bleed into decorating searches). BDM spec is 20 general keywords.

## Key Facts
- Domain: styldmelbourne.com.au (WIX site — very limited current pages)
- Business: STYLD MELBOURNE, West Melbourne, founded 2025
- Founders: Joshua Choi & Maureen Lim
- Scope: Melbourne metro only
- Customers: Vendors selling residential property, real estate agents, property developers
- Packages: Market Ready / Signature / Premium
- 42 jobs completed since March 2025 — brand new

## Status
- kwr:init: ✅ Complete (30 Apr 2026)
- GKP data: ✅ Complete — DataForSEO AU (30 Apr 2026)
- SERP analysis: ✅ Complete (30 Apr 2026)
- HTML deliverable: ✅ Complete — v1.0 (30 Apr 2026)
- Content implementation audit (headings): ✅ 19 Jun, 22 Jun 2026 — see below
- Approved content vs live full audit: ✅ 3 Jul 2026 — see below

## Content Implementation Audits (21-page content deliverable)
Note: WIX is server-side rendered — `curl -sL` fetches full content, no Playwright needed for content diffing.

- **19 Jun 2026:** heading audit — 7 pass / 14 partial, FAQ H2 rendered as H1 on 11 pages, heading level errors on 4 pages.
- **22 Jun 2026:** re-check — 6 pass / 15 partial (worse due to page-count mix), FAQ→H1 bug still on 12 pages, heading swaps on 5 pages.
- **3 Jul 2026 (approved-vs-live-content-audit-2026-07-03.md):** full content diff (not just headings) against `styldmelbourne.com.au (Approved).docx`:
  - Meta titles: 21/21 match. Meta descriptions: 21/21 match.
  - **FAQ H2→H1 bug still unresolved on 11 pages** (same defect since 19 Jun, ~2 weeks unfixed) — home-staging, property-styling, prahran, st-kilda, richmond, middle-park, port-melbourne, south-melbourne, windsor, brighton, areas-we-serve. Fixed on 10 other pages.
  - **4 of 5 heading level swaps still unresolved**: home-staging ("Thoughtful Home Styling in Melbourne" H3→H2), full-property-styling ("How We Work" H3→H2 and "Styling Packages for Every Property and Budget" H2→H3, swapped with each other), luxury-property-styling ("Our Luxury Styling Process" H3→H2), st-kilda ("Cutting Through Apartment Market Saturation" H3→H2). Caulfield's swap was fixed.
  - **New bug found:** `/full-property-styling/` FAQ — "How long does the styling stay in place?" question dropped from accordion; its answer got merged onto the previous answer which now duplicates itself. Needs a CMS/dev fix, not a copy fix.
  - **Missing paragraph:** `/property-styling/` — intro sentence under "Pre-Sale Property Styling for Melbourne Homes" H2 ("No two listings call for the same approach...") entirely absent on live.
  - **Minor/low priority:** word "artwork" added into several sentences beyond approved copy (Prahran, Albert Park, Full/Partial Property Styling FAQs, Port Melbourne, Luxury Property Styling) — reads fine, not urgent. Grammar slip on `/real-estate-staging/` FAQ ("highlight" should be "highlights"). A few Oxford-comma-only differences, cosmetic.
  - Packages sections (intro + Market Ready/Signature/Premium bullets) intentionally excluded from diffing — confirmed replaced site-wide by the live 3-card package widget, not a bug.
  - Full report: `clients/styldmelbourne.com.au/content-review/approved-vs-live-content-audit-2026-07-03.md`

## File Paths
- Questionnaire: `clients/styldmelbourne.com.au/keyword-research/questionnaire.md`
- HTML plan (when built): `clients/styldmelbourne.com.au/keyword-research/keyword-plan.html`
- Content review audits: `clients/styldmelbourne.com.au/content-review/`
