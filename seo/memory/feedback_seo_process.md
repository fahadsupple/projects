---
name: SEO Keyword Research Process & Standards
description: How to approach keyword research, entity mapping, SERP validation, and page-to-keyword mapping for client projects
type: feedback
---

## Process learned from australcontractors.com.au project

### General vs Location keyword distinction
- "General" keywords = city-level (e.g., Melbourne) or no-location service terms — target main service pages / homepage
- "Location" keywords = suburb-level targets — need dedicated location pages
- 1 general keyword = 2 location keywords in pricing
- Always aim for minimum 2 keywords per page

### Entity framework (must define before keyword mapping)
1. Homepage: Brand + primary service + city. Should match what homepages rank for in the SERP.
2. Service pages: Specific service entity + city. Check if competitors use homepage or inner pages for this SERP.
3. Location pages: Service entity + suburb entity. URL pattern: /[service]-[suburb]/

### SERP validation steps (mandatory for keyword mapping)
For each pair of keywords proposed for the same page:
1. Check what PAGE TYPE dominates the SERP (homepages vs service pages vs location pages vs ecommerce vs informational)
2. Check if local pack appears (confirms local commercial intent)
3. Compare SERPs of co-mapped keywords — are they similar/overlapping? If not, they may need separate pages.
4. Check competitor types — are competitors in the same business vertical? If not, the keyword may not convert well for this client.

### Key SERP insight: homepage vs inner page
- If competitor HOMEPAGES rank for a keyword → map to CLIENT's homepage
- If competitor INNER PAGES (/service-melbourne/) rank for a keyword → client needs a dedicated inner page for that URL
- Do NOT put a city-level keyword on a generic service page if competitors use dedicated /service-city/ pages

### Mixed intent warning
- If keyword SERP shows informational results mixed in (blog posts, "what is X") → include an explanatory section on the page
- If keyword SERP shows ecommerce (eBay, product pages) → the term has product-purchase intent, may not convert well for service businesses

### Competitive set awareness
- Always check WHO ranks, not just what ranks
- If ranked sites are in a different business vertical (e.g., mining companies for "core drilling") → the keyword has ambiguous intent, lower priority
- If ranked sites are broader than the client's niche (e.g., demolition companies + concreters for "concrete removal") → content must differentiate the client's specialized approach

### Keyword modifier rules (critical)
- NEVER use bare root keywords like "concrete cutting" — always require a modifier
- Modifier types: city ("concrete cutting melbourne"), service-type ("concrete cutting services"), action, sector
- This prevents targeting overly broad national traffic that won't convert for a local service business

### Non-subset pairing rule (critical)
- When mapping 2+ keywords to the same page, they must NOT be subsets of each other
- BAD: "concrete cutting" + "concrete cutting melbourne" — one is a subset of the other
- BAD: "ring sawing" + "ring sawing melbourne" — one is a subset of the other
- GOOD: "concrete cutting melbourne" + "concrete cutting services" — neither contains the other
- GOOD: "ring sawing melbourne" + "wall sawing melbourne" — genuinely different terms
- This ensures each keyword represents a meaningfully different search intent, not just a variation

### Ahrefs data
- Ahrefs volumes are NOT accurate — treat as relative indicators only
- Always verify with Google Keyword Planner before finalizing keyword list
- Ahrefs is useful for: finding what competitors rank for, relative volume comparison, discovering keyword ideas

### learning.xlsx pattern
- Keywords are grouped by service topic, then assigned to a page
- 2+ keywords per page is the standard (primary + secondary)
- Location keywords follow: [root keyword] + [suburb/city]
- Root keywords should have confirmed suburb-level search volume before being selected

### Mixed SERP = replace the keyword, don't patch it
- If a secondary keyword's SERP shows government pages, legal aid, Wikipedia, or informational blog content mixed in → replace it with a different keyword that has a clean commercial SERP
- Adding "explanatory content" is only a partial fix — a mixed-intent secondary creates a conflicting page signal
- Test: does the SERP show 8+ law firm / service business pages? If not, find an alternative
- Example: "probate melbourne" (mixed SERP) → replaced with "deceased estate lawyer melbourne" (clean all-law-firm SERP)

### Always check current site rankings before building keyword plan
- Pull Ahrefs organic keywords export for the client's domain before finalising any keyword targets
- Key things to check: (1) Are any commercial keywords already ranking? (2) What blog/informational content is working? (3) Are there page-2 quick wins?
- A site with zero commercial rankings needs the keyword plan to build the commercial layer from scratch — don't assume any existing pages are optimised
- Quick wins (pos 11–30, KD ≤ 15) = blog content optimisation opportunities to report alongside the keyword plan

### Root keyword variant testing (conveyancer vs conveyancing)
- At suburb level, "conveyancer [suburb]" and "conveyancing [suburb]" can have significantly different volumes — always check both
- GKP groups singular/plural (e.g., "property lawyer" = "property lawyers") but does NOT always group noun vs gerund forms
- Example: "conveyancer narre warren" = 170/mo vs "conveyancing narre warren" = 110/mo — 55% volume difference
- Pick the form with higher volume; make it consistent across all location pages and matching service pages

### Separate pages per root per suburb (never combine)
- Each suburb × root combination gets its own dedicated page
- "conveyancer berwick" and "property lawyer berwick" are separate pages, not one combined page
- Reason: different searcher intent, different entity signal, two independent ranking opportunities
- Combining them splits the relevance signal and typically wins neither term
