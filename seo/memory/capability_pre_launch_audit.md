---
name: pre-launch-audit capability
description: Pre-launch on-page QA process — what to check, what to ask for, what to deliver, owner responsibilities
type: feedback
---

# Capability: pre-launch-audit

**When triggered:** Any new website about to go live that needs an SEO pre-launch on-page check.

**Full instructions:** `seo/tools/pre-launch-audit/instructions.md`

**Deliverable:** `seo/clients/[domain]/pre-launch-audit/on-page-audit-report.html`

---

## What this capability covers

1. Meta descriptions — write for ALL pages missing them (150–160 chars, keyword + location + CTA)
2. H1 check — ALL pages via Screaming Frog CSV + **sense-check**: does the H1 match what the URL says the page is about?
3. H2 check — ALL pages via Screaming Frog CSV + sense-check: does H2 reflect actual content or just a widget label?
4. Meta title check — ALL pages via Screaming Frog CSV + sense-check: does title match URL topic? Flag over 60 chars.
5. Meta description sense-check — ALL pages: right suburb? right service? copied from wrong page?
6. Spelling & grammar — full manual crawl of every page (NOT Screaming Frog — it misses most errors)
7. URL verification — every URL compared against approved keyword-URL mapping sheet
8. Company name consistency — all pages
9. Content comparison — if a content doc was provided, compare approved copy vs what's live (saved as separate file)
10. Content random check (3–4 pages, grammar and consistency)
11. Mobile forms check (manual — flag for web PM if form is above fold on location pages)
12. Final email items from on-page team — confirm each has been addressed
13. Indexability — confirm noindex on staging, confirm it's removed on go-live

**Key rule updated (Apr 2026):** Do NOT check H1/H2/titles/meta descriptions randomly — check EVERY page. Use Screaming Frog CSV for bulk checks. Sense-check means: does the data on the page match what the URL says the page is about?

## What to ask for before starting

- Screaming Frog CSV (HTML pages only)
- Keyword-URL-Meta mapping sheet (Excel or Google Sheet)
- List of pages with missing meta descriptions (or derive from CSV)
- Staging URL
- Client memory file

## Standard note — always include in report

"Note for Web PM: Please inform the client about the new meta descriptions being added to the website as FYI — include in go-live email. SEO PM is not responsible for this communication."

## Ownership

- SEO PM: runs audit, writes meta descriptions, flags issues
- Web PM: implements changes in CMS, informs client about new meta descriptions
- SEO PM does NOT send the client communication about meta descriptions

**Why:** Established during Danton Developments pre-launch audit (April 2026). Rules confirmed by Fahad.
**How to apply:** Every time a client website is about to go live, run this capability in full before confirming launch readiness.
