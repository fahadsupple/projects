---
capability: pre-launch-audit
description: Pre-launch on-page QA for new website builds — meta descriptions, H1/H2/title spot checks, spelling, URL verification, company name consistency, mobile forms check
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

1. **Screaming Frog CSV** — crawl of the staging/new website, HTML pages only, with these columns exported: Address, Title 1, Title 1 Length, Meta Description 1, Meta Description 1 Length, H1-1, H1-1 Length, H2-1, H2-2, Spelling Errors, Word Count, Status Code, Indexability
2. **Keyword-URL-Meta mapping sheet** (Excel or Google Sheet) — the approved URL structure and meta titles from the SEO plan
3. **List of pages with missing meta descriptions** — or derive from the Screaming Frog CSV (Meta Description 1 Length = 0)
4. **Staging URL** — to crawl individual pages for content when writing meta descriptions
5. **Client memory file** — for business name, services, USPs, contact details, service areas

If any of these are missing, ask for them before proceeding.

---

## Full Checklist — Run Every Time

### 1. Meta Descriptions (Must Do)
- Pull all pages from the CSV where Meta Description 1 Length = 0
- For each missing page, fetch the page content (use WebFetch or Playwright)
- Write a meta description: 150–160 characters, includes primary keyword, includes location (Melbourne / suburb / Geelong as relevant), ends with a CTA (Free quote, Call us, Learn more, etc.)
- Do NOT write generic descriptions — base each one on the actual page content

### 2. H1 Spot Check (Sample 6–8 pages randomly)
- H1 should include the primary keyword and location
- H1 should not duplicate the meta title word-for-word (close is fine, identical is not ideal)
- No page should have more than one H1 (Screaming Frog will flag duplicate H1s)
- Flag any H1 that is just a brand name, "Home", "Services", or other non-keyword placeholder

### 3. H2 Spot Check (Same sample as H1)
- Check that real content sections have H2 headings
- Flag if H2 is only contact/form widget text (e.g., "Send us a message") with no other H2s — this means content lacks subheadings
- Note this as an observation, not a blocker

### 4. Meta Title Spot Check (Same sample + any flagged by length)
- Recommended: under 60 characters (580px pixel width)
- If over: flag URL and suggest trim (usually remove a middle pipe segment)
- Check that the brand name appears at the end: "[Keyword] | [Brand]"

### 5. Meta Description Quality Check (Existing descriptions)
- Flag any existing meta description over 160 characters — list the URL and current length
- These are not blockers but should be trimmed post-launch or before launch if time allows

### 6. Spelling Errors
- Pull Screaming Frog "Spelling Errors" column — list any pages with reported errors
- If Screaming Frog shows none, note "No spelling errors detected by Screaming Frog"
- Additionally, spot-check content on 3–4 pages manually (read the page during meta description research)

### 7. Company Name Consistency
- Check that the company name is used identically across all pages (exact legal name or the agreed shortened name)
- Common error: "Danton Development" vs "Danton Developments" (missing 's')
- Source of truth: client memory file

### 8. URL Verification
- Compare all URLs in the Screaming Frog crawl against the keyword-URL mapping sheet
- Flag any URL that differs from the approved structure
- Escalate mismatches to web PM before go-live

### 9. Content Random Check
- Open 3–4 pages and read the main body content
- Check for: grammar issues, inconsistencies in service names, wrong suburb names, placeholder text still present
- Note any issues in the audit report

### 10. Mobile Forms Check (Manual — Flag for Web PM)
- On mobile (or Chrome dev tools at 390px), open location pages and homepage
- If the contact form appears above the fold, flag to web PM: replace form with a CTA button, keep form below the fold
- The ideal above-the-fold on any location page is: H1, intro paragraph, CTA button — not a form
- This check cannot be done from Screaming Frog — must be done via browser or device

### 11. Indexability Check
- Staging sites should be noindex, nofollow — confirm this is set correctly on staging
- Flag clearly in the report: "Ensure noindex is removed when site goes live on the production domain"

---

## Deliverable Format

Create an HTML report at: `seo/clients/[domain]/pre-launch-audit/on-page-audit-report.html`

The report should include:
- Summary cards (missing meta descs, title length issues, spelling errors, meta desc length issues)
- Section 1: Meta descriptions written (table: URL + H1 | meta description to add | char count)
- Section 2: H1 / H2 / Title spot check (sample table)
- Section 3: Issues found (meta titles too long, meta descs too long)
- Section 4: Checks passed
- Section 5: Checks requiring manual verification (mobile forms, URL sheet comparison, noindex)
- Section 6: Recommended actions table (action | priority | owner)

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
