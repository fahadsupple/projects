---
name: SEO Keyword Research — Master Reference
description: Consolidated process, rules, business-type strategies, SERP rules, and industry-specific insights for all keyword research projects
type: feedback
originSessionId: 81e50042-3c9e-4c29-91de-238cd6a73314
---
# Keyword Research — Master Reference

---

## 1. Core Principles (Always Apply)

- Every keyword requires a modifier — never use bare root keywords (e.g., never "concrete cutting", always "concrete cutting melbourne")
- Minimum 2 keywords per page: 1 primary + 1 secondary — exceptions allowed when a page is added at client direction and no budget slot remains for a secondary
- Non-subset pairing rule: the two keywords on a page must NOT be linguistic subsets of each other
  - BAD: "property lawyer" + "property lawyer melbourne" (one contains the other)
  - GOOD: "property lawyer melbourne" + "property law specialist melbourne"
- SERP validation is mandatory before finalising any keyword — check page type, intent, competitive set
- **Use site: queries to verify client product/service offerings:** Before finalising a keyword, run `site:[client-domain] [product/style]` in Google to confirm the client actually stocks or offers what the keyword targets. E.g. `site:triplejfurniture.com.au hamptons` confirms they carry Hamptons-style pieces. Faster than asking the client for every detail.
- GKP is the source of truth for volume — Ahrefs volumes are relative indicators only, never final
- Always save learnings and decisions to memory as the project progresses
- **Never assume or proceed without key data** — if search volume, client detail, or SERP result is missing and needed, ask for it

---

## 2. Process Steps

1. **Get client brief** — services, locations, target customers, BDM notes
2. **Define entity framework** — homepage entity, service page entities, location page entities
3. **Pull GKP data** — AU, correct date range (12 months), batch by topic
4. **Pull competitor Ahrefs exports** — identify what competitors rank for, traffic levels, keyword gaps
5. **Check current site rankings** — pull Ahrefs organic export for the client's own domain before building plan
6. **Ranking check at closing (existing sites only)** — once the keyword list is in final stages, ask user to check current rankings for all selected keywords
   - Prompt: "Before we finalise — can you check current rankings for the keyword list?"
   - Do NOT ask earlier — only when keyword selection is near final
   - Existing positions may reveal: quick wins (page 2 terms), existing page URLs to 301, additional keyword ideas
   - Are any commercial keywords already ranking? (Usually no for new SEO clients)
   - Page-2 terms (pos 11–30, KD ≤ 15) = fast wins to flag alongside the plan
7. **Decide URL structure** — included in Keyword Research capability. No city modifier in URLs — Melbourne goes in meta title and H1 only.
8. **Map keywords to pages** — primary + secondary per page, SERP-validated
9. **SERP check each keyword pair** — confirm page type, competitive set, intent
10. **Build HTML deliverable** — keyword plan with reasoning section
11. **Update memory** — save all decisions and learnings

---

## 3. Keyword Rules & Standards

### Modifier rules
- All keywords must have a location or service modifier
- Melbourne modifier preferred for relevance and local intent
- **Melbourne modifier exception:** If Melbourne-modified version has 0 GKP volume but the national/unmodified term has volume AND: (a) client genuinely offers the service, (b) CPC is high, (c) no better Melbourne alternative exists, (d) term is not a subset of the primary — the unmodified term CAN be used as a secondary (entity signal value)
- **Always add Melbourne modifier for reporting:** Even when GKP shows 0 volume for the Melbourne version, add the modifier to the keyword. Reason: easier to track and present rankings to clients; easier to rank for a modified term than unmodified national term
- **City modifier rule — all 3 or none:** If a city modifier is used, it must cover ALL target cities as a cluster group (e.g. Sydney + Melbourne + Brisbane), not just 1 or 2 cities. If a keyword can't support all 3 city versions, use a national modifier (australia, services, etc.) instead. This prevents lopsided geographic coverage.

### Non-subset pairing rule
- Two keywords on the same page must not be linguistic subsets of each other
- Test: does one keyword contain all the words of the other? If yes → reject
- Unmodified secondary keywords (modifier exception) still build entity signals even at low/0 volume

### Primary keyword must align with the URL slug
- The primary keyword on a page should always match (or be the closest match to) the URL slug
- The broader term is typically primary; the more specific/niche term is secondary
- Example: `/glass-partition-walls/` → primary = "glass partition walls melbourne", secondary = "glass office partitions melbourne"

### Root keyword variant testing
- At suburb level, different word forms can have significantly different volumes — always test both
- e.g., "conveyancer [suburb]" vs "conveyancing [suburb]" — check both in GKP; pick the higher volume
- GKP groups singular/plural but NOT always noun vs gerund forms
- **Consistency rule:** All keywords in a plan must use the same form — never mixed. Standardise to whichever form the majority uses

### Mixed SERP = replace the keyword, don't patch
- If secondary keyword SERP shows government pages, Legal Aid, Wikipedia, or informational blog content mixed with commercial results → replace it entirely
- Standard: 8+ law firm / service business pages in SERP = clean commercial intent ✓
- Example: "probate melbourne" (mixed SERP) → replaced with "deceased estate lawyer melbourne" (all law firm pages)

---

## 4. By Business Type

### Local Business (single location, suburb/LGA-focused)
- Homepage targets city-level primary service keyword + USP modifier as secondary
- **Melbourne-level keywords — only for remote-delivery services:** wills, probate, business law, leases → Melbourne modifier OK. Conveyancing, trades, proximity-dependent services → location pages only, no Melbourne service page
- Home suburb → homepage entity (see Location Page Strategy below)
- Location pages: target suburbs within realistic catchment (typically same LGA or 15–20km radius)
- Conversion test: would a client from the other side of the city realistically hire this business? If no → drop Melbourne keyword for that service

### Service Business (city-wide or regional)
- Homepage: primary service + city
- Service pages: specific service + city, validated by SERP
- Location pages: same service roots at suburb level if volume/intent supports it
- Melbourne modifier applies broadly

### Nationwide Business
- Homepage: primary service (no city modifier, or brand-only)
- Service pages: primary service + state/city combinations
- Location pages: city-level pages rather than suburb-level

### Ecommerce
- Category pages: product category + modifiers (material, size, use case, brand)
- Product pages: specific product keywords, model numbers, brand + product
- Volume strategy: target higher-volume category terms on category pages; long-tail on product pages
- Volume ceiling: keep all keywords at ≤ 1,000 monthly searches per keyword for new/weak domains (DR < 20), except homepage
- BDM priority category should dominate the keyword plan — allocate majority of page slots to that category

---

## 5. Location Page Strategy

### When to use location pages
- When suburb-level GKP volume exists for the root keyword, OR
- When strategic presence in a suburb is justified (growth area, competitor location, client's office suburb)
- Never create location pages outside the client's realistic service catchment

### Home suburb → homepage, not a location page
- The business's own address suburb should be anchored to the homepage via NAP, schema, and content
- Do NOT create a standalone location page for the home suburb
- Instead: incorporate the suburb into homepage entity and reallocate freed budget slots to a different suburb

### No directional suburb name modifiers
- Never use suburbs with directional words: North, South, East, West (e.g., Cranbourne North, Narre Warren South, Hampton East)
- These create weak, confusing entity signals
- Skip directional suburbs entirely regardless of GKP volume

### When to use 2 roots for location pages
Two roots are justified when ALL of the following are true:
1. The two roots capture meaningfully different searcher intents
2. The second root reinforces a genuine brand differentiator (not just a synonym)
3. Competition for root 2 is low enough that 0-volume suburb pages are still worth creating
4. At least one suburb has confirmed volume for root 2 (proves the intent exists)
- Each suburb gets a SEPARATE PAGE per root — never combine both roots on one page

### When to use 1 root only
- If root 2 is essentially a synonym with the same searcher intent
- If the client has no meaningful differentiator to justify the second root's positioning
- If root 2 volume is zero at suburb level AND no strategic rationale exists

---

## 6. SERP Analysis Rules

### Page type matching (mandatory)
- If competitor HOMEPAGES rank → client's homepage should target it
- If competitor INNER PAGES rank → client needs a dedicated inner page
- If competitor LOCATION PAGES rank → client needs location pages, not a city-level page
- Never map a city-level keyword to a location page or vice versa

### Competitive set check
- Check WHO ranks, not just what ranks
- If ranked sites are government/informational → keyword has informational SERP, not suitable as commercial target
- Target keywords where your client's business type already dominates the SERP
- **One questionable result does not disqualify a keyword** — assess the overall competitive set. A keyword is viable if the client has a realistic path to rank within positions held by comparable businesses.

### Local pack
- Presence of local pack = strong local commercial intent
- "Near me" keywords almost always trigger local pack — map to `/areas-we-serve/` page, AND reinforce via GBP. Never put "near me" on a suburb page or service page.

### Intent signals
- "How to", "what is", "difference between" in top results = informational SERP
- Law firm / service business pages dominating = commercial intent ✓
- Government, Legal Aid, Wikipedia = informational/authoritative SERP — not a commercial keyword target
- Mixed informational + commercial = conflicting intent — replace the keyword

---

## 7. Data & Tools

### Google Keyword Planner
- Always AU, correct 12-month date range
- Files often UTF-16 encoded — decode accordingly before parsing
- Two header rows typical: row 0 = export metadata, row 1 = date range, row 2 = actual column headers
- Competition levels (LOW/MED/HIGH) and CPC dollar values come from full GKP exports — NOT from stripped volume-only exports
- Singular/plural are grouped by GKP — treat as same keyword
- Noun vs gerund forms (conveyancer vs conveyancing) are separate — test both
- When volume data is missing → ask for a specific GKP search rather than guessing

### Ahrefs
- Competitor exports: useful for discovering what competitors rank for and traffic levels
- Client's own export: always pull before building plan
- Volumes: relative indicators only — verify everything with GKP
- UTF-16 TSV format typical for exports

### SERP checking
- Search tool operates from US servers — append "australia" to queries to get Australian results
- Always note: page type, business type, intent (commercial/informational/government)

---

## 8. Non-SEO Entity Pages (Always Include in Every Keyword Plan)

Every keyword research deliverable must include a set of non-SEO entity pages. These are always required.

### Standard non-SEO pages (always include)

| Page | URL | Purpose | Keywords to map |
|------|-----|---------|-----------------|
| Homepage | `/` | Brand entity | Broad brand descriptor (entity signal only, not SEO keyword) |
| Services hub | `/services/` | Links to all service pages | No keyword target — navigation/entity page |
| Areas we serve | `/areas-we-serve/` | Geographic coverage signal | Map "near me" keywords here |
| About | `/about/` | Entity establishment | No keyword target |
| Contact | `/contact/` | NAP signal | No keyword target |
| Gallery / Our Work | `/gallery/` | E-E-A-T proof | No keyword target |
| Get a Quote | `/get-a-quote/` | Conversion destination | No keyword target |
| Testimonials | `/testimonials/` | Social proof | No keyword target |

### Near me rule (mandatory for every project)
- `/areas-we-serve/` always gets "near me" keywords
- Take each location keyword root used in the plan and append "near me"
- Example (Danton Developments): roots = "suspended ceilings" + "partition walls" → "suspended ceilings near me" + "partition walls near me"

---

## 9. Reporting Standards

- Always add location modifier to secondary keywords even when GKP shows 0 volume for that modifier
- Quick wins from blog content (page 2 positions, low KD) should be flagged separately

### HTML Deliverable — Required Reasoning Sections

Every keyword plan HTML must include these sections (brief and form sections always come first):

#### 0. Client Brief — BDM Notes + Onboarding Form (yellow block at top, always)
- **Styling:** Yellow background (`#fffbcc`), amber border (`#e6d800`), two-column layout (BDM Brief left, Onboarding Form right)
- **BDM Brief column (verbatim):** All BDM notes exactly as written
- **Onboarding Form column (verbatim, relevant fields only):** location/address, services offered, SEO keyword preferences, USPs, ideal customer. Omit purely administrative fields.

#### 1. Entity Structure Being Built
- Tier 1 — Homepage: brand entity signal
- Tier 2 — Service pages: topic entities
- Tier 3 — Location pages: geographic entity associations
- The overall picture: what Google understands about the business after all pages are live

#### 2. Supporting Entities Per Page (Content Signals — Not Keyword Targets)
- Related terminology, process steps, related services, named entities, FAQs
- These become the content brief for writers

#### 3. Beyond This Keyword Plan — What Else Is Needed
- GBP, schema markup, NAP consistency, internal linking, content production, citation building, review strategy, blog quick wins

---

## 10. Industry-Specific Insights

### Legal / Law Firms
- **Accredited specialist angle:** If principal has an accreditation, this is a high-value USP secondary keyword
- **Service intent split:** Conveyancing (transactional) vs property lawyer (legal advice) — meaningfully different, justify separate pages and roots
- **Powers of attorney SERP:** Government and public advocate bodies dominate — not a commercial keyword target. Cover as content section.
- **Probate SERP:** "probate lawyer melbourne" = clean. "probate melbourne" = mixed → replace with "deceased estate lawyer [city]"
- **High-CPC signals:** Probate ($40+), commercial law ($70–$80), commercial lease ($26–$52) — high CPCs = worth including even with small volume
- **Conveyancing SERP:** Often dominated by specialist conveyancers — law firm positioning as "lawyer-backed conveyancing" is a genuine differentiator

### Trades & Contractors
- **Root keyword:** Usually the trade name + city/suburb
- **Ambiguous terms:** Some trade terms have commercial + industrial meanings — check SERP to confirm business vertical
- **Second root:** Usually not justified for trades — searcher intent at suburb level is typically the same

### Ecommerce / Furniture
- **"Bedroom suite" + city modifier pulls hotel SERPs** — never use as a furniture keyword
- **"For sale" + location modifier** — consistently pulls classified/clearance SERPs. Do not use.
- **Size-specific sofa keywords** (3 seater, 2 seater) dominated by national chains — skip for DR < 20 domains
- **Bedroom piece keywords** at meaningful volume almost always have national chains
- **National chain presence threshold:** Reject if chain at positions 1–4. Amber (evaluate) if at positions 5–8.
- **"Kitchen furniture"** = renovation/cabinet SERP, not furniture retailers
- **"Lighting"** = designer specialist SERP, wrong competitive set
- QA process — run SERP checks on ALL keyword pairs before finalising any plan

---

## 11. Global Rule — Consolidated Project Memory Files

Every client project must have **one consolidated memory file** as the single source of truth.

### What goes in it
- Business identity, services, USPs
- Budget and split (general vs location units)
- All strategic decisions and reasoning
- Entity framework (homepage, service pages, location pages)
- Final keyword-to-page mapping with volumes and CPC
- SERP learnings per keyword
- Current site rankings summary
- Competitor map
- HTML deliverable file path and version
- Status and pending work

### Naming convention
`client_[domain-without-tld].md` — e.g., `client_wslegal.md`

### Always save raw briefs and onboarding forms
When a client brief, onboarding form, or any structured intake data is shared — save it immediately as a raw file in the client folder. This is the source of truth; the consolidated file is derived from it.
