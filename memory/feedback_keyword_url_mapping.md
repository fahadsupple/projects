---
name: Keyword → URL Mapping — Standard Approach
description: How to map keywords to pages for all SEO projects — primary/secondary pairing, URL patterns, separate vs combined pages, and SERP matching rules
type: feedback
---

Keywords are mapped to URLs using a structured approach that applies across all clients and projects.

**Why:** Established during wslegal.com.au (Apr 2026) as the confirmed method for presenting and executing keyword-to-page mapping.

**How to apply:** Follow this approach for every client keyword plan, from initial mapping through to deliverable output.

---

## The Mapping Rules

### One primary keyword per page
Every page has exactly one primary (P) keyword — the term the page is primarily optimised for. A page cannot have two primaries.

### Secondary keywords on the same page only if SERP matches
A secondary keyword can sit on the same page as the primary only if:
- The SERP composition for both keywords shows the same page type (e.g., both show law firm service pages)
- The search intent is the same or closely overlapping
- The secondary is not a linguistic subset of the primary (non-subset pairing rule still applies)

If SERP differs — mixed vs clean, informational vs commercial — the secondary keyword needs its own page.

### Service/city-level keywords: separate pages per topic
At a city level (e.g., "X lawyer melbourne"), each distinct service area gets its own page. You cannot combine different service topics on one page even if related:
- "probate lawyer melbourne" + "deceased estate lawyer melbourne" → same page (same intent, same SERP)
- "wills and estates lawyer melbourne" + "probate lawyer melbourne" → separate pages (different service areas; wills ≠ probate)
- "business lawyer melbourne" + "commercial lawyer melbourne" → same page (interchangeable terms, same SERP)

### Location keywords: separate pages per root
At suburb level, when there are multiple keyword roots (e.g., property lawyer, commercial lawyer, deceased estate lawyer), create separate pages per root — not one combined page.

**Reason:** Conversion suffers when a visitor searching "deceased estate lawyer berwick" lands on a page primarily about property conveyancing. Each root serves a different client need and emotional context. Separate pages = targeted message = better conversion.

Each location page is keyword-matched in the URL:
- `/property-lawyer-berwick/`
- `/commercial-lawyer-berwick/`
- `/deceased-estate-lawyer-berwick/`

Exception: If suburbs are very small (population <2,000, near-zero search demand across all roots), a single combined location page may be justified to avoid thin content.

---

## Deliverable Format

All keyword mappings are presented as a single table with three columns:

| Primary Keyword | Secondary Keywords | Status |
|---|---|---|
| [primary keyword] | [secondary keyword(s), comma-separated or —] | New `/suggested-url/` or Existing (page title + URL) |

- One row per page
- All secondary keywords for that page in one cell
- Status column includes both New/Existing AND the recommended URL
- No separate tables for service vs location — one unified table

---

## URL Pattern Rules

- Use the exact keyword phrase in the URL, hyphenated: `property-lawyer-berwick`
- No trailing brand name in URL slugs (e.g., not `/property-lawyer-berwick-wollerman-shacklock-lawyers`)
- Follow the client's existing URL pattern conventions where one exists
- Location pages follow `[keyword]-[suburb]` pattern matching the primary keyword
- Service pages follow `[service]-[city]` pattern (e.g., `/business-lawyer-melbourne/`)
