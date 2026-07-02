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
