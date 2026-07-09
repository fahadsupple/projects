# flourishelc.com.au — Flourish Early Learning Centre

**Business:** Early learning / childcare / preschool / kindergarten centres, NSW + WA.
**Live centres in scope:** Oakville NSW, Bull Creek WA. Watanobbi NSW is OUT OF SCOPE —
client instruction: "We are ONLY working on Oakville and Bull Creek and NOT Watanobbi."
**Staging site:** https://hardyd21.sg-host.com/ — all dev changes are made here first,
never directly on the live flourishelc.com.au site.

## Site structure
- Oakville NSW silo (14 pages): daycare-childcare-{oakville,box-hill,vineyard,gables,
  grantham-farm,riverstone,mulgrave}-nsw + preschool-{same 7 suburbs}-nsw
- Bull Creek WA silo (14 pages): daycare-childcare-{bull-creek,leeming,bateman,rossmoyne,
  shelley,willetton,brentwood}-wa + kindergarten-{same 7 suburbs}-wa
- Silo master/hub pages: flourish-early-learning-centre-oakville-nsw,
  flourish-early-learning-bull-creek-wa, flourish-early-learning-centre-watanobbi-nsw
- Other pages: areas-we-serve (all-3-centres landing page), homepage, philosophy,
  curriculum, join-the-team, terms-and-conditions, watanobbi-special-offer

## CRITICAL working method note — content docs use Word track changes
The client's content docs for this project (e.g. "flourishelc.com.au (Approved).docx")
are downloaded copies of a Google Doc that still has **open, unaccepted suggested edits**
(Word track changes: `<w:ins>`/`<w:del>` in word/document.xml). This is easy to miss and
caused a real error on 2 Jul 2026: `python-docx`'s default `paragraph.text` property only
reads direct child `<w:r>` runs of a paragraph — text wrapped inside `<w:ins>`/`<w:del>`
sits one level deeper and is SILENTLY DROPPED. A first-pass review using
`docx.Document(path)` + `paragraph.text` made a 37-change, 20-page document look like it
only had 5 corrected lines on one page.

**Rule for this client (and any doc that might have track changes): before trusting a
docx extraction, check `word/document.xml` for `<w:ins`/`<w:del` counts:**
```python
import zipfile
z = zipfile.ZipFile(path)
doc = z.read('word/document.xml').decode('utf-8')
print(doc.count('<w:ins '), doc.count('<w:del '))
```
If non-zero, parse the XML directly (iterate `w:p` → child `w:ins`/`w:del`/`w:r` elements,
pull `w:t` for inserted/plain text and `w:delText` for deleted text) to recover the true,
complete list of suggested changes before comparing against the live site.
Also: the user has directed that for this client, work from the LOCAL downloaded .docx
file in the client folder, not the live Google Doc link — the local file is confirmed to
be an accurate downloaded copy.

## Recurring technical issue found (2 Jul 2026 review)
FAQ content is built as a Beaver Builder accordion module PAIRED with a separate,
manually-written FAQPage JSON-LD `<script>` block. When the developer edits/removes an
accordion question or answer text, the paired JSON-LD script is NOT automatically
updated — it has to be edited by hand separately. Confirmed stale/mismatched schema on
12 pages after a full site check: bateman-wa, areas-we-serve (before/after school care
task), oakville-nsw, mulgrave-nsw, preschool-oakville-nsw, preschool-gables-nsw,
bull-creek-wa, leeming-wa, shelley-wa, kindergarten-bull-creek-wa,
kindergarten-rossmoyne-wa, kindergarten-willetton-wa (council-reference task). **When
reviewing any future content change on this site, always diff the visible accordion
question list against the FAQPage JSON-LD question list — don't assume schema was
updated just because the visible content was. This is a systemic, recurring defect in
this build, not a one-off.**

## Review history
- 3 Jun 2026 — Approved doc vs live: 29 pages, strong match, few heading variations
  (see review-work/review-approved-doc-vs-live-03-Jun-2026.txt)
- 16 Jun 2026 — "Before and after school care" removal audit, 36 pages checked, 2 pages
  needed fixes (areas-we-serve, daycare-childcare-bateman-wa) — both visible AND schema
  removal required (see content-audit/basc-removal-audit.md)
- 2 Jul 2026 — Staging verification of "Adding CTAs & other requests" docx (5 tasks) +
  "Approved" docx corrections (council/region reference removal — corrected scope: 37
  tracked-change blocks across 20 pages in both silos, not just Mulgrave as first
  reported). Result: contact/CTA blocks and images correctly added to 27/28 silo pages
  (1 bug on leeming-wa enquiry icon); ALL council/region corrections implemented
  correctly in visible content across all 20 pages (thorough work); FAQ JSON-LD schema
  left stale on 10 of those 20 pages plus the 2 before/after-school-care pages (12
  total) — same recurring schema-sync defect. areas-we-serve images are Oakville-only,
  not neutral as briefed. Full findings + dev action list at
  review-work/staging-verification-02-Jul-2026.txt
- 9 Jul 2026 — Full word-for-word check of the (new, much larger — 29-page) "Approved"
  docx against all 29 matching staging URLs. Meta titles/descriptions: 29/29 exact match.
  CRITICAL: 8 pages have their closing CTA H2 section (e.g. "Join the Flourish Family
  Today") misplaced BEFORE the FAQ section instead of after it (systemic build issue) —
  daycare-childcare-{box-hill,vineyard,gables,mulgrave}-nsw, preschool-{vineyard,
  riverstone,mulgrave}-nsw, daycare-childcare-bateman-wa. 4 genuine content bugs found:
  "wecome" typo (preschool-riverstone-nsw), "Kndergarten" typo in FAQ heading
  (kindergarten-rossmoyne-wa), missing "Cancer Council WA SunSmart guidelines" clause in
  both visible text AND JSON-LD (daycare-childcare-willetton-wa), and a rewritten
  (non-approved-wording) FAQ answer on daycare-childcare-bull-creek-wa. Also confirmed:
  docx itself still contains stale "before and after school care" copy on bull-creek-wa,
  bateman-wa, areas-we-serve that live correctly excludes per the 16 Jun 2026 removal
  instruction — docx is NOT the source of truth on this point, live is correct, no
  action needed. Several docx-side-only typos (live already correct): "Flourish Early
  Centre" missing "Learning" and double-period on daycare-childcare-riverstone-nsw,
  stray ":" on daycare-childcare-shelley-wa, "Proving"/"Providing" typo on
  kindergarten-brentwood-wa. Also flagged (likely intentional, not bugs): "Book a tour
  or enquiry today." CTA appended on ~24/29 pages, WA-page sidebar CTA block (Follow us
  on Facebook / Make an enquiry / Enrolment Form) on all 7 WA pages, and FAQ heading
  enhancement ("Frequently Asked Questions About X") on ~25/29 pages vs generic docx
  heading — both match the separate "Adding CTAs" task pattern from 2 Jul, needs
  analyst/client sign-off either way since it deviates from the Approved doc's literal
  text. Docx also has a URL typo: page 5 URL field says ".../grantham farm-nsw/" (space)
  instead of "grantham-farm-nsw". Full findings + dev priority list at
  review-work/approved-doc-vs-staging-09-Jul-2026.txt
- 9 Jul 2026 (same day) — Re-verified the "Adding CTAs & other requests" docx's 5 tasks
  against current staging (follow-up to 2 Jul review). 5 of 6 previously-flagged items
  now FIXED: Task 1 leeming-wa duplicate-icon bug resolved (all 28 silo pages pass CTA
  block check incl. correct Bull Creek "Follow us on Facebook" -> FlourishELCBullCreekWA
  link, verified against master pages); Task 3 areas-we-serve images swapped from
  Oakville-only to generic Flourish-ELC branding; Task 4 FAQ JSON-LD schema for
  before/after-school-care now clean on both bateman-wa and areas-we-serve; bonus
  Vineyard "Here's what sets..." phrasing tweak applied. Task 2 unchanged/still correct
  (Bull Creek silo reuses 1 image — source material limit, not a bug). ONE ITEM STILL
  OUTSTANDING, unchanged word-for-word since 2 Jul: Task 5's FAQ JSON-LD schema still has
  stale council/region references on the same 10 pages (oakville-nsw daycare+preschool,
  mulgrave-nsw, preschool-gables-nsw, bull-creek-wa daycare+kindergarten, leeming-wa,
  shelley-wa, rossmoyne-wa kindergarten, willetton-wa kindergarten) — visible content
  confirmed clean site-wide. Full report at
  review-work/adding-ctas-doc-vs-staging-09-Jul-2026.txt
- 9 Jul 2026 (same day) — Confirmed via full 37-page sitemap scan (visible + all JSON-LD
  scripts) that "before and after school care" no longer appears ANYWHERE on staging —
  client's original "verify if there are any other references" request from the Adding
  CTAs doc is now fully closed out, no other instances found.
- 9 Jul 2026 (same day) — Targeted compliance-statement scan (comply/regulation/NQF/EYLF/
  LEP/RFS/accreditation etc.) across all 29 location+areas-we-serve pages, visible +
  schema. Flagged 4 items for client verification (not confirmed wrong, just unverified
  specific claims, client OK with dev removing entirely if not quickly verifiable): (1)
  footer "Privacy-and-Confidentiality-Policy-NQF-NSW.pdf" linked site-wide incl. WA pages
  despite NSW-branded filename; (2) preschool-oakville-nsw cites a specific "Local
  Environmental Plan (LEP)" + "semi-rural (RU4)" zoning claim; (3) preschool-vineyard-nsw
  + preschool-gables-nsw cite NSW RFS "Bush Fire Prone Area" designation compliance; (4)
  kindergarten-shelley-wa claims formal "SunSmart accreditation" (stronger than the
  generic SunSmart-guidelines language used elsewhere). NQF/EYLF/National Law/Child Care
  Subsidy/Working with Children references elsewhere are standard Australia-wide
  language, not flagged. Dev handoff scoped to ONLY these compliance items (client
  explicitly asked to exclude CTA/FAQ items, those are separate handoffs) written to
  review-work/dev-instructions-09-Jul-2026.txt. Client then dropped item 1 (footer PDF)
  as not needed, and asked for surgical "replace X with Y" instructions instead of
  descriptive options for the remaining 3 (LEP/RU4, RFS bushfire x2 pages, SunSmart
  accreditation x2 mentions on 1 page) — file rewritten accordingly with exact current
  text + exact replacement text for each, specifying visible-content vs FAQ-schema scope
  per item.

## Working method notes
- No pandoc/docx2txt on this machine — use `python3 -c "import docx"` (python-docx is
  installed) to extract paragraph text, and `python3 -c "import zipfile"` to extract
  embedded images from .docx (unzip CLI not available in this environment). BUT see the
  track-changes warning above — check for `<w:ins`/`<w:del` before trusting python-docx
  output.
- Staging site is plain-HTML reachable via curl (no auth wall) — for multi-page
  content/schema verification, bulk `curl` download + grep/python is much faster than
  driving Playwright page by page, and is sufficient when no JS-rendered content is
  involved (this WordPress/Beaver Builder site renders everything server-side).
