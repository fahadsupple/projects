---
capability: pre-launch-audit
description: Pre-launch on-page QA for new website builds — meta descriptions, H1/H2/title full audit (all pages via Screaming Frog + sense-check against URL), spelling, URL verification, company name consistency, mobile forms check
---

# Pre-Launch Audit Capability

**Capability name:** `pre-launch-audit`
**Deliverable path:** `seo/clients/[domain]/pre-launch-audit/on-page-audit-report.html`

---

## When This Capability Is Called

Run this capability when a new website is about to go live and the SEO PM needs to do a pre-launch on-page check. This is typically triggered after the web team has built the site and before the client email goes out confirming the launch.

---

## What to Ask For (If Not Provided)

Before starting, confirm you have all of the following:

1. **Screaming Frog CSV** — crawl of the staging/new website, HTML pages only, with these columns exported: Address, Title 1, Title 1 Length, Title 1 Pixel Width, Meta Description 1, Meta Description 1 Length, H1-1, H1-1 Length, H2-1, H2-2, Spelling Errors, Word Count, Status Code, Indexability
2. **Keyword-URL-Meta mapping sheet** (Excel or Google Sheet) — the approved URL structure, meta titles, and meta descriptions from the SEO plan
3. **Content document** (Google Doc or similar) — the approved content brief, if one exists, for content comparison
4. **Staging URL** — to crawl individual pages for content when writing meta descriptions
5. **Client memory file** — for business name, services, USPs, contact details, service areas

If any of these are missing, ask for them before proceeding.

---

## Full Checklist — Run Every Time

### 1. Meta Descriptions — All Pages (Must Do)
- Pull ALL pages from the CSV where Meta Description 1 Length = 0
- For each missing page, fetch the page content (use WebFetch or Playwright)
- Write a meta description: 150–160 characters, includes primary keyword, includes location (city / suburb as relevant), ends with a CTA (Free quote, Call us, Learn more, etc.)
- Do NOT write generic descriptions — base each one on the actual page content
- Also flag any existing meta description over 160 characters (not a blocker, but list them)

### 2. H1 Check — ALL Pages (via Screaming Frog CSV)
- Check every page in the CSV — do NOT sample randomly
- **Sense-check**: Does the H1 match what the URL says the page is about?
  - e.g. URL `/suspended-ceilings-richmond/` → H1 must mention Richmond and suspended ceilings
  - e.g. URL `/office-fitouts/` → H1 should not say "Partition Walls" or wrong suburb
- Flag: missing H1, H1 that doesn't match the URL topic, H1 that is a generic placeholder ("Home", "Services")
- Flag: H1 duplicated word-for-word with the meta title (not ideal but not a blocker)

### 3. H2 Check — ALL Pages (via Screaming Frog CSV)
- Check every page in the CSV — do NOT sample randomly
- **Sense-check**: Does the first H2 reflect actual page content, or is it just a form/widget label?
  - Flag if the only H2 visible in Screaming Frog is "Send us a message" or similar widget text — this indicates the page has no real content subheadings
- Flag: H2 that belongs to a different page/topic (e.g. Richmond page has H2 mentioning Preston)

### 4. Meta Title Check — ALL Pages (via Screaming Frog CSV)
- Check every page in the CSV — do NOT sample randomly
- **Sense-check**: Does the meta title match the URL topic?
  - e.g. URL `/partition-walls-geelong/` → title must mention Geelong and partition walls
  - Title format should be: `[Primary Keyword] | [Brand Name]` or `[Primary Keyword] [Location] | [Brand Name]`
- Flag: titles over 60 characters (suggest trim — usually remove a middle pipe segment)
- Flag: titles that don't match the page's URL topic (copy-paste errors)
- Flag: missing brand name in title

### 5. Meta Description Sense-Check — ALL Pages (via Screaming Frog CSV)
- For pages that already have a meta description, **sense-check** it against the URL:
  - Does the meta description mention the right suburb/location for the page?
  - Does it mention the right service for the page?
  - Flag any meta description that appears to be copied from a different page (wrong suburb, wrong service)
- Flag overlong descriptions (>160 chars) — list all of them

### 6. Spelling & Grammar — Full Site (Manual Crawl — NOT Screaming Frog)
- Do NOT rely on Screaming Frog for spelling/grammar — it misses most errors
- Manually fetch every page using WebFetch and read the content
- Check: body text, H1–H6, button labels, meta title, meta description, alt text
- Australian English standard: colour/honour/analyse/organise/minimise/travelling/centre
- Check for: wrong words (e.g. "amplify" instead of "improve", "stress-free" instead of "seamless"), grammar errors, US spellings, wrong content (wrong suburb in heading, wrong project count), redundant phrases (e.g. "Acoustic & Soundproofing"), colloquial language in professional copy
- Save results in the standard spelling-mistakes-finder HTML format at: `/home/invoi/fahad_projects/spelling-mistakes-finder/[staging-domain].html`

### 7. URL Verification — All Pages
- Extract all URLs from the Screaming Frog CSV
- Compare every URL against the approved keyword-URL mapping sheet
- Flag any URL that differs from the approved structure (slug changed, extra words added, different format)
- Escalate mismatches to web PM before go-live

### 8. Company Name Consistency — All Pages
- Determine the correct legal/trading name from the client memory file and homepage
- Check every page in the Screaming Frog CSV: title tag, H1, meta description
- Also spot-check body text on a sample of pages
- Flag any variation: missing letter, wrong capitalisation, wrong word order, abbreviated incorrectly

### 9. Content Comparison — If a Content Doc Exists
- If a Google Doc or content brief was provided, compare approved content against what is live on the site
- Check: H1 wording, H2 structure, body copy (is approved copy present?), FAQs (all questions and answers present?)
- Flag: missing sections, changed wording that has legal/liability implications, stub pages that haven't been built yet
- Save as a separate file: `seo/clients/[domain]/pre-launch-audit/content-comparison.html`

### 10. Content Random Check (3–4 pages, not every page)
- Even if a full content comparison is done, also spot-read 3–4 pages manually
- Check: placeholder text still present, inconsistencies in service descriptions, wrong suburb names in body copy
- Note findings in the audit report

### 11. Mobile Forms Check (Manual — Flag for Web PM)
- On mobile (or Chrome dev tools at 390px width), open location pages and homepage
- If the contact form appears above the fold, flag to web PM: replace form with a CTA button, keep form below the fold
- The ideal above-the-fold on any location page: H1, intro paragraph, CTA button — NOT a form
- This check cannot be done via Screaming Frog — requires browser or device

### 12. Final Email Items from On-Page Team
- If the on-page team has sent a final sign-off email with outstanding items, review each item
- Confirm each has been addressed or flag it as outstanding
- This audit covers SEO elements only — CRO, design, or content items remain the responsibility of the respective team member

### 13. Indexability Check
- Confirm staging site is set to noindex, nofollow — this is correct on staging
- Note clearly in the report: "Ensure noindex is removed and correct index directives are applied when the site goes live on the production domain"

---

## Deliverable Format

ALL deliverables must be saved under the client's pre-launch-audit folder: `seo/clients/[domain]/pre-launch-audit/`. Never save to tool folders or any other location.

### Main audit report: `seo/clients/[domain]/pre-launch-audit/on-page-audit-report.html`

Must include:
- Summary stat cards (issues found, URLs confirmed, etc.)
- Section 1: Meta descriptions written — table: URL (clickable link) | Meta Description to Add | Chars
- Section 2: Issues Found — 4-column table: Page | Element | Issue | Fix. Strip all pass rows — only include issues.
- Section 3: Spelling & Grammar — single table per page. No "recurring errors" sub-table — list every issue under the page URL it appears on. URLs must be clickable links. Priority issues (wrong facts, critical errors) at top.

Do NOT include a separate section per check type (H1 audit, H2 audit, etc.) unless the client specifically requests it. Keep the report concise — only flag issues, never include pass rows.

### Spelling/grammar report: `seo/clients/[domain]/pre-launch-audit/spelling-grammar-audit.html`

Incorporated directly into on-page-audit-report.html as Section 3. A separate file is no longer created.

### Content comparison (if content doc provided): `seo/clients/[domain]/pre-launch-audit/content-comparison.html`

---

## Standard Note — Always Include in Report

> **Note for Web PM:** Please inform the client about the new meta descriptions being added to the website as FYI — this can be included in the go-live email sent to the client. The client's approval is captured in that same communication. The SEO PM is not responsible for sending this notification, but Web PM should include it.

---

## Priority Levels

| Priority | Label | Meaning |
|---|---|---|
| Must Do | Red | Blocks launch or causes immediate SEO harm |
| Should Do | Amber | Should be done before launch if possible |
| Nice to Have | Blue | Low urgency, can be done post-launch |
| Communication | Purple | Not a technical task — just inform someone |

---

## Ownership

- **SEO PM:** Runs the audit, writes meta descriptions, flags issues to web PM
- **Web PM:** Implements all meta descriptions and technical fixes in the CMS, informs client of new meta descriptions
- **SEO PM does NOT:** Implement changes directly in the CMS, send the client communication about meta descriptions
