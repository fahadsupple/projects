---
name: capability-review-work
description: "Review Work capability — compare a client-approved content doc + dev task doc + annotated task screenshots against the live site (desktop AND mobile), output 4-part findings report"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9107e663-1871-4a85-b951-aab1649354f6
  modified: 2026-07-28T04:26:02.978Z
---

# Capability: Review Work

## What it does
Compares an approved content document (DOCX) — and, when supplied, the developer **Daily Tasks** doc that told the dev what to build — against the live website. Checks:
1. **Content matching** — meta titles, meta descriptions, H1/H2/H3, body text
2. **Content issues** — wrong suburb/location on wrong pages, spelling, AU English
3. **Coding / SEO issues** — noindex, canonical, schema, OG tags, H1 count, HTTP status
4. **Mobile rendering** — the mobile version is a first-class check, not an afterthought (see below)
5. **Heading structure** — level order, skips, duplicates, one-H1 rule
6. **HTML code quality** — duplicate IDs, malformed links, alt text, accessible names

## How it works
1. Extract DOCX text via `zipfile` + `ElementTree` (walk `w:body`; handle `w:tbl` separately so table cells aren't lost)
2. Parse into structured pages (URL, meta title, meta description, H1, H2s, H3s, body)
3. Fetch all live URLs **twice** — once with a desktop UA, once with a mobile UA — and diff them (title, desc, headings, body length). Identical HTML means a responsive build; any difference is a finding in its own right.
3b. If annotated screenshots are supplied (Trello cards, marked-up page grabs), split each tall PNG into ~1500px vertical slices at ~1200px wide and read every slice. Each red callout is a separate task line — catalogue them all before touching the site, and check them one by one alongside the doc tasks.
4. Compare doc vs live per page — **paragraph-level containment**, not just headings
5. Flag discrepancies, spelling issues, coding problems

## Output format — 4 sections in this order
- **Part 1 — Content Matching** (what matches, what varies)
- **Part 2 — Content Issues** (spelling, AU English, wrong content, contamination)
- **Part 3 — Coding/SEO Issues**, in four sub-blocks:
  - 3A High priority, 3B Mobile, 3C Headings, 3D HTML code
- **Part 4 — Task compliance checklist** — one row per Daily Task line AND one row
  per screenshot annotation, marked DONE / PARTIAL / NOT DONE. This is the part
  the client and the dev actually read; never skip it.
- **Summary table** — action items with PRIORITY + OWNER columns

## Output file location
`clients/[domain]/review/review-[doc-description]-[date].txt`
(or `review-work/` if that's the existing folder — keep the report beside the source docs the analyst dropped in)

## Key checks run
- Meta title/desc match doc vs live
- Exactly 1 H1 per page
- Every doc body paragraph present in live HTML (normalise smart quotes, nbsp, en/em dashes before comparing)
- Wrong suburb/location in headings (cross-page contamination)
- Duplicate meta titles/descriptions across the reviewed set
- AU English: enrol, organise, recognise, flavour, colour, catalogue, centre, fulfil, analyse
- Canonical present and self-referencing; noindex not set; OG tags; FAQPage/Product schema; HTTP 200
- XML sitemap coverage for every newly created URL
- Internal links the approved copy explicitly promises ("follow the X link through to…")

## When a Daily Tasks doc is in scope — check the structural work too
The content can be 100% correct while the build is incomplete. Always verify separately:
- **Product/item assignment on new category pages.** Count product tiles or `add-to-cart=` IDs per page. A new ecommerce category with 0 products renders "No products were found which match your selection" — highest-priority defect, and content matching will never catch it. Then grep the product sitemap for how many matching items already exist, so the fix is quantified for the client rather than vague.
- **Nav/menu instructions, including ordering.** Parse the menu `<ul id="menu-…">` and walk `<li>`/`<ul>` depth. Items are usually appended in task-doc order even when the doc said "insert alphabetically" — check order, not just presence. Worst case it breaks an existing alphabetical submenu.
- **"Parent must stay clickable" dropdown instructions** — confirm `href` is the real category URL, not `#`.
- **Hub page links** (e.g. Areas We Serve) — strip header/footer before counting so nav links don't create false positives.
- **Footer/secondary menus** — new pages added to the main nav are often missed in the footer menu. Not usually a task-doc line item; report as a consistency gap.
- **Hub/index pages excluded from the content brief** — their own meta often goes stale once the site's scope expands (e.g. "areas of Sydney and NSW" on a site now covering 7 cities). Flag as a gap in the brief, not a dev error.

## Mobile version — always check it, it is where the defects hide
Run a real headless browser at **390x844, isMobile, hasTouch** over every page in
scope (Python Playwright; ~20s/page, run it backgrounded). Desktop-only review will
pass a page that is broken on the phone, and for local-service clients most traffic
is mobile. Check per page:
- **Hidden-on-mobile sections.** The single highest-value check. Page builders let a
  section be hidden per breakpoint — Elementor uses `elementor-hidden-mobile`. Walk
  every `<form>`'s ancestors looking for it, and measure the form's
  `getBoundingClientRect()` at both viewports. A form that is 410x378 on desktop and
  0x0 on mobile is the primary conversion path deleted on most of the traffic. Found
  on 46 naztech pages. Also check CTAs, phone blocks and maps the same way.
- **Horizontal overflow.** `document.documentElement.scrollWidth > innerWidth`, then
  list the offending elements by `getBoundingClientRect().right > vw`.
- **Tap targets.** Flag any `a[href]`/`button` under ~32px tall (Google wants 48px).
  In-content card CTAs are the usual offender and repeat hundreds of times.
- **Font sizes.** Flag rendered `font-size < 12px` on elements with real text.
- **Broken images.** `img.naturalWidth === 0`. IMPORTANT: scroll to the bottom and
  wait ~2s first, then **re-verify every hit with an HTTP request** — lazy-loading
  produces mass false positives. On naztech 8 URLs looked broken; only 1 was a real
  404 (an Elementor `/thumbs/` derivative that 404s while the source image is 200).
- **Empty vertical gaps.** Sort visible leaf text nodes by top offset and report gaps
  >160px. Large runs usually mean a hidden section or an unconstrained image.
- **Mobile vs desktop parity.** Title, description, H1 set, full heading list, body
  character count. >2% body divergence means content is being withheld from one.
- Take a 390px-wide screenshot per page and eyeball the hero and the pre-footer.

## Headings — check structure, not just text
- Exactly one H1 per page (assert on the live DOM, not the doc).
- **Level skips**: walk H1-H6 in document order and flag any jump of more than one
  (H1 → H3 on 48/49 naztech pages, caused by hero USP labels marked up as H3).
- **Duplicate heading text on the same page** — this is how you catch a section whose
  heading was copy-pasted and never edited. On naztech it surfaced a wrong FAQ H2
  (the previous section's heading repeated) and a doubled "Nearby Suburbs We Cover".
- Mind the doc-to-page level mapping: in Supple approved docs, **Heading 1 = meta
  title, the URL and meta description follow it, Heading 2 = the page H1, Heading 3 =
  the on-page H2s.** Compare on that mapping or every page will look wrong.

## HTML code checks
- **Duplicate element IDs** — pages with two instances of the same form emit the same
  `form-field-*` IDs twice. Invalid HTML; `<label for>` binds to the first field only.
- **tel: link formats** — grep every `tel:` and count variants. naztech had four
  (`tel:0449%20992%20695` x403, `tel:+61449992695` x123, `tel:0449992695` x110,
  and `tel:0449 992 695` x61 with a raw space, which is a malformed URI).
  Standardise on E.164.
- **Anchors with no accessible name** — `<a>` with no text, no `<img>`, no aria-label
  (header phone-icon links are the classic).
- **`target="_blank"` without `rel="noopener"`**, especially on internal links where
  it is almost always accidental.
- **Image alt** — report per page and name the file; one templated image with no alt
  will repeat across a whole silo.
- **Image weight** — flag any image over ~300 KB and check whether a resized variant
  already exists in the media library.
- **Link targets vs card titles** — a card whose title links correctly while its
  "Learn More" button points at a generic hub page is a real, easily-missed defect.
- **Footer vs main nav parity** — the nav gets updated and the footer never does.
  Check the footer menu for the new pages, and for plain-text items that should be
  links.

## Sitewide find-and-replace tasks — verify with a regex sweep, per page
When a task says "across the website, change X to Y", never spot-check. Regex every
page for the old string and report the count per page. On naztech the rename was done
in page bodies but missed in the footer, so it survived on all 49 pages twice over,
plus 5 extra instances on the homepage that no other page had. The homepage is the
usual straggler because it is built differently from the templated pages.
Also sweep for *near-miss* variants the task did not literally name
("Across Victoria", "regional Victoria", "Melbourne or Victoria", "34 Reviews") and
report them as consistency gaps rather than task failures.

## Body-copy matching — sentence level, not paragraph level
Split approved paragraphs into sentences (>40 chars) and containment-test each one
against the live page text. Paragraph-level matching produced 791 false "missing" on
naztech because the builder splits paragraphs across widgets and inlines links;
sentence-level reduced it to 3 real findings out of 2,752 sentences.
Normalise before comparing: smart quotes, en/em dashes, nbsp, `4x4` vs `4×4`.
**Watch the normaliser bug**: if the corpus key strips spaces but the needle key
keeps them (or vice versa) every check fails. Sanity-check with one paragraph you can
see on the page before trusting a mass "missing" result.

## Verification discipline — confirm before you report
Two classes of false positive burned time on naztech and will recur:
- **AU English regexes**: `licensed` is correct as a verb/adjective (ARC licensed);
  `meter` is correct for a multimeter; `tires` is correct as a verb. Only `licence`
  as a *noun* matters. Read the surrounding sentence before reporting a spelling hit.
- **Cross-suburb "contamination"**: check the approved doc first. Location pages
  legitimately name the home base ("Working out of Pakenham...") and FAQ questions
  often name a second suburb by design.

## Keyword coverage — match with filler tolerance
Phrase-match every keyword in the Meta File against title + description + body, allowing up to ~3 connector words (`in the a an to for and of across is are our your we that you`) between terms. A strict contiguous match produced 24 false "missing" on foodistribute; the filler-tolerant match produced 1 real one. Also read the Keywords column's **bold** formatting to separate the current upgrade's keywords from earlier ones.

## False positives to avoid
- Footer links to other locations — expected, not contamination
- Product-tile titles marked up as `<h2>` by the theme — carousel noise, not page headings; skip the first N before comparing to the doc
- "enrolled" / "enrolling", "waitlist" — same in AU English
- "program" — correct AU spelling for a business/menu/educational program (e.g. "a baking program"); **not** an error
- A missing FAQPage schema is only a defect if the approved copy for that page actually has FAQs — check the doc before reporting it
- An intentional cross-city mention in approved copy (e.g. "the Sydney supplier already on the Newcastle run" on the Newcastle page)
- Missing image `alt` with an identical count on every page = pre-existing theme issue, not introduced by the upload
- `img.naturalWidth === 0` before the page has finished lazy-loading — always re-verify with an HTTP request
- Meta titles over 65 chars that **match the approved doc exactly** — that is our copy decision, not a dev error. Flag it to ourselves, not to the developer
- Template section headings that were never in the approved doc (e.g. "Trusted by Commercial Operators Across Melbourne") — report as a consistency gap, not a task failure

## Also check the pre-publish fix list, if one exists
If `content/keyword-coverage-fixes.md` (or similar) was written before delivery, verify each fix landed live. Wording often differs from the fixes doc while still achieving the keyword adjacency — judge on the adjacency, not on the literal sentence.

## Uses
- flourishelc.com.au — 3 June 2026 (29 location pages, NSW + WA). Found: Rossmoyne kindergarten with wrong suburb in FAQ H2, "Enroll" US spelling on Mulgrave page, brand name truncation on Riverstone page, kindergarten pages using "Childcare" in FAQ headings
- foodistribute.com.au — 28 July 2026 (30 pages + Daily Tasks doc). Content 100% accurate; the real findings were structural — 10 new category pages with 0 products assigned, and nav items appended instead of inserted alphabetically. See [[project-foodistribute]].
- naztech.com.au — 31 July 2026 (49 pages: approved copy + Daily Tasks doc + 4 annotated Trello screenshots). Content 99.9% accurate (2,749/2,752 sentences verbatim); nav, redirects, sitemap, canonicals and internal linking all clean. The real findings were everywhere *except* the body copy: homepage H1 never swapped, enquiry form hidden on mobile across 46 pages via `elementor-hidden-mobile`, the sitewide "Melbourne & Victoria" rename missed in the footer on all 49 pages, a 404 Elementor thumbnail on 22 pages, four different `tel:` formats, and duplicate form IDs on 45 pages. First run of this capability with the mobile / headings / HTML checks added. See [[project-naztech]].
