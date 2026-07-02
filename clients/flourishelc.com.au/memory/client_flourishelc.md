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

## Recurring technical issue found (2 Jul 2026 review)
FAQ content is built as a Beaver Builder accordion module PAIRED with a separate,
manually-written FAQPage JSON-LD `<script>` block. When the developer edits/removes an
accordion question, the paired JSON-LD script is NOT automatically updated — it has to
be edited by hand separately. This has caused stale/mismatched schema at least 4 times
(bateman-wa, areas-we-serve, mulgrave-nsw, shelley-wa, preschool-oakville-nsw). **When
reviewing any future content change on this site, always diff the visible accordion
question list against the FAQPage JSON-LD question list — don't assume schema was
updated just because the visible content was.**

## Review history
- 3 Jun 2026 — Approved doc vs live: 29 pages, strong match, few heading variations
  (see review-work/review-approved-doc-vs-live-03-Jun-2026.txt)
- 16 Jun 2026 — "Before and after school care" removal audit, 36 pages checked, 2 pages
  needed fixes (areas-we-serve, daycare-childcare-bateman-wa) — both visible AND schema
  removal required (see content-audit/basc-removal-audit.md)
- 2 Jul 2026 — Staging verification of "Adding CTAs & other requests" docx (5 tasks) +
  "Approved" docx corrections (Hawkesbury/council reference removal on mulgrave-nsw).
  Result: contact/CTA blocks and images correctly added to 27/28 silo pages (1 bug on
  leeming-wa enquiry icon), visible FAQ removal and Hawkesbury text corrections both
  done correctly, BUT FAQ JSON-LD schema not updated to match on 3 pages (bateman-wa,
  areas-we-serve, mulgrave-nsw) — recurring defect per above. areas-we-serve images
  are Oakville-only, not neutral as briefed. Full findings + dev action list at
  review-work/staging-verification-02-Jul-2026.txt

## Working method notes
- No pandoc/docx2txt on this machine — use `python3 -c "import docx"` (python-docx is
  installed) to extract paragraph text, and `python3 -c "import zipfile"` to extract
  embedded images from .docx (unzip CLI not available in this environment).
- Staging site is plain-HTML reachable via curl (no auth wall) — for multi-page
  content/schema verification, bulk `curl` download + grep/python is much faster than
  driving Playwright page by page, and is sufficient when no JS-rendered content is
  involved (this WordPress/Beaver Builder site renders everything server-side).
