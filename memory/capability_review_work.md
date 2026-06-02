# Capability: Review Work

## What it does
Compares content in a client-approved document (Word/DOCX) against the live website. Checks for:
1. **Content matching** — meta titles, meta descriptions, H1/H2/H3 headings, body text
2. **Content issues** — wrong suburb/location names on wrong pages, spelling mistakes, AU English compliance
3. **Coding / SEO issues** — noindex, canonical, schema markup, OG tags, H1 count, HTTP status

## How it works
1. Extract full document text from DOCX using Python zipfile + ElementTree
2. Parse into structured pages (URL, meta title, meta description, H1, H2s, H3s, body)
3. Scrape all live URLs using requests + BeautifulSoup
4. Compare document vs live for each page
5. Flag discrepancies, spelling issues, and coding problems

## Output format — 3 sections in this order
- **Part 1 — Content Matching** (what matches, what varies)
- **Part 2 — Content Issues** (spelling, AU English, wrong content, contamination)
- **Part 3 — Coding/SEO Issues** (noindex, canonical, schema, OG, H1 count)
- **Summary table** — action items for developer with priority levels

## Output file location
`clients/[domain]/review-work/review-[doc-description]-[date].txt`

## Key checks run
- Meta title/desc match between doc and live
- Exactly 1 H1 per page
- H2 headings match document
- Wrong suburb/location in headings (cross-page contamination)
- AU English: enrol (not enroll), programme (arts only), organise, recognise, etc.
- "program" is correct AU spelling for educational/government programs — NOT an error
- Canonical tags present and self-referencing
- Noindex not set accidentally
- Schema markup present (WebPage + FAQPage)
- OG tags present
- HTTP 200 status

## False positive to avoid
- Footer links to other centre locations — expected, not contamination
- "enrolled" / "enrolling" — same spelling in AU and US English
- "program" — correct in AU English for educational programs
- "waitlist" — accepted in AU English

## First use
flourishelc.com.au — 3 June 2026 (29 location pages, NSW + WA)
Found: Rossmoyne kindergarten with wrong suburb in FAQ H2, "Enroll" US spelling on Mulgrave page, brand name truncation on Riverstone page, kindergarten pages using "Childcare" in FAQ headings
