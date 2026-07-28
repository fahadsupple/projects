---
name: capability-review-work
description: "Review Work capability — compare a client-approved content doc + dev task doc against the live site, output 3-part findings report"
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

## How it works
1. Extract DOCX text via `zipfile` + `ElementTree` (walk `w:body`; handle `w:tbl` separately so table cells aren't lost)
2. Parse into structured pages (URL, meta title, meta description, H1, H2s, H3s, body)
3. Fetch all live URLs (`urllib` + regex parsing is sufficient; send a real UA and handle gzip)
4. Compare doc vs live per page — **paragraph-level containment**, not just headings
5. Flag discrepancies, spelling issues, coding problems

## Output format — 3 sections in this order
- **Part 1 — Content Matching** (what matches, what varies)
- **Part 2 — Content Issues** (spelling, AU English, wrong content, contamination)
- **Part 3 — Coding/SEO Issues** (noindex, canonical, schema, OG, H1 count)
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

## Also check the pre-publish fix list, if one exists
If `content/keyword-coverage-fixes.md` (or similar) was written before delivery, verify each fix landed live. Wording often differs from the fixes doc while still achieving the keyword adjacency — judge on the adjacency, not on the literal sentence.

## Uses
- flourishelc.com.au — 3 June 2026 (29 location pages, NSW + WA). Found: Rossmoyne kindergarten with wrong suburb in FAQ H2, "Enroll" US spelling on Mulgrave page, brand name truncation on Riverstone page, kindergarten pages using "Childcare" in FAQ headings
- foodistribute.com.au — 28 July 2026 (30 pages + Daily Tasks doc). Content 100% accurate; the real findings were structural — 10 new category pages with 0 products assigned, and nav items appended instead of inserted alphabetically. See [[project-foodistribute]].
