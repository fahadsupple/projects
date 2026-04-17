---
name: Keyword Research — Master Reference
description: Consolidated process, rules, business-type strategies, and industry-specific insights for all keyword research projects
type: feedback
originSessionId: fa00b4dd-c85a-421c-80a3-26bc8c56ac87
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
- GKP is the source of truth for volume — Ahrefs volumes are relative indicators only, never final
- Always save learnings and decisions to memory as the project progresses
- **Never assume or proceed without key data** — if search volume, client detail, or SERP result is missing and needed, ask for it. Tell the user exactly what's needed and why so they can pull it or check with the client in one go.

---

## 2. Process Steps

1. **Get client brief** — services, locations, target customers, BDM notes
2. **Define entity framework** — homepage entity, service page entities, location page entities
3. **Pull GKP data** — AU, correct date range (12 months), batch by topic
4. **Pull competitor Ahrefs exports** — identify what competitors rank for, traffic levels, keyword gaps
5. **Check current site rankings** — pull Ahrefs organic export for the client's own domain before building plan
6. **Ranking check at closing (existing sites only)** — once the keyword list is in final stages, ask the user to check current rankings for all selected keywords
   - Prompt: "Before we finalise — can you check current rankings for the keyword list? I'll give you the full list to check."
   - Do NOT ask earlier — only when keyword selection is near final
   - Existing positions may reveal: quick wins (page 2 terms), existing page URLs to 301, additional keyword ideas
   - Note any ranking URLs in the plan alongside the planned URL (e.g. "currently ranking at /old-url/ — 301 to new URL")
   - Are any commercial keywords already ranking? (Usually no for new SEO clients)
   - What blog/informational content is working? (Quick win opportunities)
   - Page-2 terms (pos 11–30, KD ≤ 15) = fast wins to flag alongside the plan
6. **Decide URL structure** — included in Keyword Research capability. Determine page slugs based on SERP research and keyword mapping. No city modifier in URLs — Melbourne goes in meta title and H1 only.
7. **Map keywords to pages** — primary + secondary per page, SERP-validated
8. **SERP check each keyword pair** — confirm page type, competitive set, intent
9. **Build HTML deliverable** — keyword plan with reasoning section
10. **Update memory** — save all decisions and learnings

> **Capability confirmation rule:** Before starting any keyword research task, confirm: "This looks like **Keyword Research** work — proceeding under that. Correct?" URL structure and keyword-to-page mapping are both part of this capability.

---

## 3. Keyword Rules & Standards

### Modifier rules
- All keywords must have a location or service modifier
- Melbourne modifier preferred for relevance and local intent
- **Melbourne modifier exception:** If Melbourne-modified version has 0 GKP volume but the national/unmodified term has volume AND: (a) client genuinely offers the service, (b) CPC is high, (c) no better Melbourne alternative exists, (d) term is not a subset of the primary — the unmodified term CAN be used as a secondary (entity signal value)
- **Always add Melbourne modifier for reporting:** Even when GKP shows 0 volume for the Melbourne version, add the modifier to the keyword. Reason: easier to track and present rankings to clients; easier to rank for a modified term than unmodified national term

### Non-subset pairing rule
- Two keywords on the same page must not be linguistic subsets of each other
- Test: does one keyword contain all the words of the other? If yes → reject
- Unmodified secondary keywords (modifier exception) still build entity signals even at low/0 volume

### Primary keyword must align with the URL slug
- The primary keyword on a page should always match (or be the closest match to) the URL slug
- The broader term is typically primary; the more specific/niche term is secondary
- Example: `/glass-partition-walls/` → primary = "glass partition walls melbourne", secondary = "glass office partitions melbourne" (office partitions = specific application of partition walls, not the other way)

### Root keyword variant testing
- At suburb level, different word forms can have significantly different volumes — always test both
- e.g., "conveyancer [suburb]" vs "conveyancing [suburb]" — check both in GKP; pick the higher volume and use it consistently across all location pages AND matching service page
- GKP groups singular/plural (property lawyer = property lawyers) but NOT always noun vs gerund forms
- **Consistency rule:** All keywords in a plan must use the same form — either "lawyer" or "lawyers" throughout, never mixed. Before finalising, do a final check across all keywords and standardise to whichever form the majority uses
- Once a root is chosen, apply it consistently everywhere (service page + all location pages)

### Mixed SERP = replace the keyword, don't patch
- If secondary keyword SERP shows government pages, Legal Aid, Wikipedia, or informational blog content mixed with commercial results → replace it entirely
- Adding "explanatory content" is only a partial fix — a mixed-intent secondary sends conflicting signals
- Standard: 8+ law firm / service business pages in SERP = clean commercial intent ✓
- Example: "probate melbourne" (mixed SERP with government + informational) → replaced with "deceased estate lawyer melbourne" (all law firm pages)

---

## 4. By Business Type

### Local Business (single location, suburb/LGA-focused)
- Homepage targets city-level primary service keyword + USP modifier as secondary
- Service pages target city-level service keywords for services deliverable remotely
- **Melbourne-level keywords — only for remote-delivery services:** wills, probate, business law, leases, professional advice → Melbourne modifier OK. Conveyancing, trades, proximity-dependent services → location pages only, no Melbourne service page
- Home suburb → homepage entity (see Location Page Strategy below)
- Location pages: target suburbs within realistic catchment (typically same LGA or 15–20km radius)
- Conversion test: would a client from the other side of the city realistically hire this business? If no → drop Melbourne keyword for that service, use location pages

### Service Business (city-wide or regional)
- Homepage: primary service + city
- Service pages: specific service + city, validated by SERP (inner pages vs homepages)
- Location pages: same service roots at suburb level if volume/intent supports it
- Melbourne modifier applies broadly — service businesses typically serve whole city

### Nationwide Business
- Homepage: primary service (no city modifier, or brand-only)
- Service pages: primary service + state/city combinations
- Location pages: city-level pages rather than suburb-level
- Root keyword selection: national volume matters; suburb-level pages less relevant

### Ecommerce
- Category pages: product category + modifiers (material, size, use case, brand)
- Product pages: specific product keywords, model numbers, brand + product
- Location pages: rarely needed unless delivery/pickup-focused
- Volume strategy: target higher-volume category terms on category pages; long-tail on product pages
- *(To be expanded as ecommerce projects are completed)*

### Franchise / Multi-Location
- *(To be expanded)*

---

## 5. Location Page Strategy

### When to use location pages
- When suburb-level GKP volume exists for the root keyword, OR
- When strategic presence in a suburb is justified (growth area, competitor location, client's office suburb)
- Never create location pages outside the client's realistic service catchment — they rank but don't convert

### Home suburb → homepage, not a location page
- The business's own address suburb should be anchored to the homepage via NAP, schema, and content
- Do NOT create a standalone location page for the home suburb — it competes with the homepage and wastes a budget slot
- Instead: incorporate the suburb into the homepage entity (address, schema, content) and reallocate the freed budget slots to a different suburb

### No directional suburb name modifiers
- Never use suburbs with directional words in the name: North, South, East, West (e.g., Cranbourne North, Narre Warren South, Hampton East)
- These are treated as separate suburbs by Google but create weak, confusing entity signals
- If the plain suburb is already in the plan, pick a different nearby suburb without a directional modifier
- This rule applies regardless of GKP volume — skip directional suburbs entirely

### Suburb selection criteria
- Same LGA or within realistic travel distance
- Active property/commercial activity (check development, population, market activity)
- At least some competition to validate that people search for services there
- Exclude suburbs in different LGAs with their own established service communities — pages rank but don't convert (e.g., Frankston, Dandenong for a Casey-based firm)

### Root keyword selection for location pages
- Must have suburb-level GKP volume, OR strong strategic justification (client's office, growth area, low competition)
- Test both noun forms (conveyancer vs conveyancing) — pick higher volume, use consistently
- "Near me" searches (very high volume) are local pack triggers — map to `/areas-we-serve/` page (see Non-SEO Entity Pages section), NOT to individual suburb pages or service pages. Also reinforce via GBP optimisation.

### When to use 2 roots for location pages
Two roots are justified when ALL of the following are true:
1. The two roots capture meaningfully different searcher intents
2. The second root reinforces a genuine brand differentiator (not just a synonym)
3. Competition for root 2 is low enough that 0-volume suburb pages are still worth creating
4. At least one suburb has confirmed volume for root 2 (proves the intent exists)
- Each suburb gets a SEPARATE PAGE per root — never combine both roots on one page (splits entity signal, typically wins neither term)
- Example: "conveyancer [suburb]" (transaction intent) + "property lawyer [suburb]" (legal advice intent + accredited specialist positioning)

### When to use 1 root only
- If root 2 is essentially a synonym with the same searcher intent
- If the client has no meaningful differentiator to justify the second root's positioning
- If root 2 volume is zero at suburb level AND no strategic rationale exists (compare: core drilling for a concrete contractor — rejected; property lawyer for an accredited property specialist — kept)

---

## 6. SERP Analysis Rules

### Page type matching (mandatory)
- If competitor HOMEPAGES rank for a keyword → client's homepage should target it
- If competitor INNER PAGES (/service-melbourne/) rank → client needs a dedicated inner page
- If competitor LOCATION PAGES rank → client needs location pages, not a city-level page
- Never map a city-level keyword to a location page or vice versa

### Competitive set check
- Check WHO ranks, not just what ranks
- If ranked sites are in a different business vertical → keyword has ambiguous intent, lower priority
- If ranked sites are government/informational → keyword has informational SERP, not suitable as commercial target
- Target keywords where your client's business type already dominates the SERP
- **One questionable result does not disqualify a keyword** — if a national chain or strong competitor appears at one position but the rest of the SERP is occupied by smaller/local vendors, assess the overall competitive set. A keyword is viable if the client has a realistic path to rank within the positions held by comparable businesses. Only reject if the questionable competitor dominates (e.g., holds multiple top positions, or the top 3 are all national chains).

### Local pack
- Presence of local pack = strong local commercial intent
- Local pack searches are also won through Google Business Profile optimisation (separate from page keyword strategy)
- "Near me" keywords almost always trigger local pack — map to `/areas-we-serve/` page on site, AND reinforce via GBP. Never put "near me" on a suburb page or service page.

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
- Competition levels (LOW/MED/HIGH) and CPC dollar values come from full GKP exports — NOT from stripped volume-only exports (which only have volume + % changes)
- Singular/plural are grouped by GKP — treat as same keyword
- Noun vs gerund forms (conveyancer vs conveyancing) are separate — test both
- When volume data is missing or insufficient to make a decision → ask for a specific GKP search rather than guessing

### Ahrefs
- Competitor exports: useful for discovering what competitors rank for and traffic levels
- Client's own export: always pull before building plan — reveals current commercial ranking gaps, blog quick wins
- Volumes: relative indicators only — verify everything with GKP
- UTF-16 TSV format typical for exports — parse accordingly

### SERP checking
- Search tool operates from US servers — append "australia" to queries to get Australian results
- Always note: page type (homepage/inner page/location page), business type (law firm/conveyancer/directory), intent (commercial/informational/government)

---

## 8. Modifier Strategy for Rankability

### Core principle
The goal of modifier testing is **not** to find high-volume variants — it is to find the **lowest-KD variant that still carries commercial intent**.

- Volume is a floor check only: if a term has any tracked volume (or appears in GSC data), it qualifies
- Ranking itself is the objective — a ranked page intercepts broader related traffic beyond the specific keyword's tracked volume figure
- The query that earned the ranking is a subset of the total traffic the page will receive once ranked
- **How to apply:** For any competitive head term, systematically test modifier variants → select the lowest-KD option that still has commercial intent → build the page around that variant

### Modifier testing hierarchy (city / service businesses)
Test in this order — stop when you find a KD level the site can win:

| Level | Pattern | Typical KD | Notes |
|---|---|---|---|
| 1 | [service] + [city] | High | Base term — usually most competitive |
| 2 | [service] + agency/company/services + [city] | Moderate | Often 3–7 points lower than base |
| 3 | [service] + [state] | Moderate | Useful when city term is heavily contested |
| 4 | [industry vertical] + [service] + [city] | Lower | More specific intent; e.g. "commercial debt collection sydney" |
| 5 | [service] + [suburb] | Near zero | Uncontested in most markets — highest rankability |

### Suburb-level modifier rule
- When SE Ranking returns **0 results** for a suburb-level term → near-zero KD confirmed — include it
- When the client has a **physical office** in that suburb → GBP address signals compound the rankability further
- Suburb pages rank quickly; business impact comes from the ranking, not from the keyword's tracked volume
- Include suburb-level pages even when SE Ranking has no data — absence of data = absence of competition

### How to run modifier testing in a project
1. Pull similar keywords from SE Ranking for the competitive head term (`DATA_getSimilarKeywords`, AU, vol_from=10)
2. Pull long-tail variants (`DATA_getLongTailKeywords`)
3. Sort results by KD ascending — identify the lowest-KD modifier with commercial SERP signals
4. Test suburb-level terms for any client with a physical office or strong local footprint
5. If suburb terms return 0 data → note "near-zero KD, no SE Ranking data" and include in plan
6. Document all modifier variants tested in the Eligible Candidates section

### What this does NOT mean
- Do not add meaningless modifiers that destroy commercial intent ("debt collection jobs sydney" = wrong intent — exclude)
- Do not use modifiers that push the term into a different business vertical ("debt collection lawyers sydney" = law firm SERP, not agency SERP — exclude)
- Low KD is only useful if the SERP is occupied by the same business type as the client

---

## 9. Non-SEO Entity Pages (Always Include in Every Keyword Plan)  <!-- was §8 -->

Every keyword research deliverable must include a set of non-SEO entity pages alongside the keyword-targeted pages. These are always required — they build authority, establish the entity, and are never optional.

### Standard non-SEO pages (always include)

| Page | URL | Purpose | Keywords to map |
|------|-----|---------|-----------------|
| Homepage | `/` | Brand entity — what the business does, where, for whom | Broad brand descriptor (e.g. "Suspended Ceilings & Partition Walls — Melbourne & Geelong"). Not an SEO keyword — entity signal only. |
| Services hub | `/services/` | Links to all service pages. Signals topical breadth. | No keyword target — navigation/entity page |
| Areas we serve | `/areas-we-serve/` | Geographic coverage signal. Links to all location pages. | Map "near me" keywords here — take each location keyword root + "near me". e.g. "suspended ceilings near me" + "partition walls near me" |
| About | `/about/` | Entity establishment — founder, experience, credentials, story | No keyword target — E-E-A-T and trust page |
| Contact | `/contact/` | NAP signal, local entity anchor | No keyword target |
| Gallery / Our Work | `/gallery/` or `/our-work/` | E-E-A-T proof — real projects, real outcomes. Especially critical for trades, fitout, construction. | No keyword target — conversion and trust page |
| Get a Quote | `/get-a-quote/` or `/free-quote/` | Conversion destination. Should be a dedicated page, not just a contact form. | No keyword target |
| Testimonials | `/testimonials/` | Social proof — real client feedback | No keyword target |

### GBP and website are mutually reinforcing — always treat together
Location pages on the website and Google Business Profile are not separate levers — they feed each other:
- Location pages signal to Google which suburbs the business serves → expands GBP visibility in those suburbs' map pack
- GBP authority in a suburb → reinforces organic location page ranking for that suburb
- A location page ranking below the map pack is still valuable — it feeds geographic service area signals back to GBP

**How to apply:** When recommending location pages, always note that GBP should be optimised in parallel — service area settings, suburb mentions in description, posts targeting those areas. The two compound each other. Never treat website SEO and GBP as independent workstreams for local businesses.

---

### Near me rule (mandatory for every project)
- `/areas-we-serve/` always gets "near me" keywords
- Take each location keyword root used in the plan and append "near me"
- Example (Danton Developments): location roots = "suspended ceilings" + "partition walls" → map "suspended ceilings near me" + "partition walls near me" to `/areas-we-serve/`
- If a project has only one location root, still create one "near me" keyword for the areas page
- These are the primary and secondary keywords for the `/areas-we-serve/` page

### When to include in the HTML deliverable
- Always list these pages in the deliverable as a separate section from the SEO keyword pages
- Label them clearly as "Entity / Authority Pages" so the client and manager understand they are structural, not keyword-targeted
- Include the "near me" keyword mapping for `/areas-we-serve/` explicitly

---

## 10. Reporting Standards

- Always add location modifier (e.g., "melbourne") to secondary keywords even when GKP shows 0 volume for that modifier
- Reason: easier to track and present rankings to client; location-modified terms are easier to rank for than unmodified national terms; avoids client confusion about what geography the ranking covers
- Quick wins from blog content (page 2 positions, low KD) should be flagged separately alongside the keyword plan — these are actionable without new pages

### HTML Deliverable — Required Sections (Mandatory)

Every keyword plan HTML must include the following sections. Sections 0–3 are in the strategy/reasoning area. The Eligible Candidates section is a separate block at the bottom, after all strategy notes.

#### Eligible Candidates — Additional Options (always include, always at bottom)
Every keyword plan HTML must include an **Eligible Candidates — Additional Options** section at the bottom of the page, after the Strategy Notes reasoning block.

- **Purpose:** Documents all keywords that passed initial filters but were not selected in the current plan. Provides a pre-validated pool for future swaps, expansions, or client-requested category additions. Prevents re-doing SERP/volume research for every future change.
- **Content:** Include all evaluated alternatives with: keyword, GKP volume, YoY trend (if available), category, SERP status (CLEAN / AMBER / REJECTED / NOT CHECKED), and a reason note explaining why not selected and what conditions would justify selecting it.
- **Group structure:** Group by outcome — e.g. "Previously Selected — Now Replaced", "Rejected — Declining Trend", "Rejected — National Chain SERP", "Pending Validation", "Category Alternatives"
- **SERP status colour coding:** CLEAN = green, AMBER = amber/orange, REJECTED = red, NOT CHECKED = grey
- **When a keyword is swapped out:** Add it to Eligible Candidates immediately, with a note explaining the replacement rationale and conditions for reinstatement
- **When a keyword is swapped in:** Move it from Eligible Candidates to the main table, note it was "selected" in the Eligible Candidates section with the date

**Why:** The candidate pool analysis work (often 1,000+ keywords) should never be lost. Future keyword additions, client requests, or SERP changes may require quick swaps — the Eligible Candidates section makes this instantaneous without re-research.

---

### HTML Deliverable — Required Reasoning Sections

Every keyword plan HTML must include the following sections in the strategy rationale/reasoning area. The brief and form sections always come first — before budget, strategy, and page rationale.

#### 0. Client Brief — BDM Notes + Onboarding Form (yellow block at top of page, always)
The client brief must appear as a **visually distinct yellow block at the very top of the HTML**, before the keyword table and before any other content. Not in the reasoning section — at the top of the page where it is immediately visible.

- **Styling:** Yellow background (`#fffbcc`), amber border (`#e6d800`), two-column layout (BDM Brief left, Onboarding Form right)
- **BDM Brief column (verbatim):** All BDM notes exactly as written — budget, services to target, locations, keyword preferences, any flags. Do not paraphrase. If a BDM flag was resolved during research, note the outcome inline with a flag indicator.
- **Onboarding Form column (verbatim, relevant fields only):** Include: location/address, services/products offered (Q12), SEO keyword preferences (Q13 — even if none provided), USPs (Q14), ideal customer (Q16). Omit purely administrative fields (ABN, phone, email, insurance) — only include what's strategically pertinent.
- **Why:** The manager reviewing the plan needs to see source requirements at a glance, without opening separate files, to verify alignment between brief and keyword selections.

#### 1. Entity Structure Being Built
Explain the full entity architecture the keyword plan creates — not just "here are the keywords" but what Google will understand about the business after the plan is executed:
- **Tier 1 — Homepage:** What business entity is being signalled. Brand + primary service + location. What credential or USP the secondary keyword anchors.
- **Tier 2 — Service pages:** What topic entities each service page builds and how they collectively expand the business's topical authority.
- **Tier 3 — Location pages:** What geographic entity associations the location pages create. How they cluster to build local authority in a specific area/LGA.
- **The overall picture:** What Google understands about the business after all pages are live — business type, topic authority, geographic reach.

#### 2. Supporting Entities Per Page (Content Signals — Not Keyword Targets)
For each page in the plan, list the related entities, subtopics, and terminology that should appear as headings and content — NOT as additional keyword targets, but as topical depth signals. These become the content brief for writers.
- Group by page type: homepage, each service page, location page root 1, location page root 2
- Include: related terminology, process steps, related services, named entities (people, organisations, legislation), FAQs, topics that should be covered as sections even if not searchable as standalone keywords
- Flag any out-of-scope services that should appear as content sections because clients ask about them even if they're not rankable (e.g., powers of attorney on a wills page)

#### 3. Beyond This Keyword Plan — What Else Is Needed
List all elements outside the keyword plan scope that are required to make the entity structure perform. This sets client/manager expectations and ensures the plan is not treated as the only thing needed:
- **Google Business Profile:** Service categories, service area, description content, review strategy, post frequency. "Near me" keywords are won through GBP, not service pages.
- **Schema markup:** Business type schema (LocalBusiness → LegalService / Contractor / etc.), page-level schema (FAQ, HowTo where relevant), employee/credential schema, areaServed. Specify what schema type is appropriate for the business.
- **NAP consistency:** Where it must match — website, GBP, all citation directories. Flag key directories relevant to the industry.
- **Internal linking:** Homepage → service pages → location pages. Blog → service pages. How entity signals should flow across the site.
- **Content production:** Note that the keyword plan defines targets; original, non-templated content built around supporting entities is required. Warn against thin/duplicate location pages.
- **Citation building:** Key directories for the industry. Why citations matter for local entity reinforcement.
- **Review strategy:** How reviews impact local rankings and trust signals.
- **Blog quick wins:** If any exist (page 2 positions, low KD), flag them separately as fast wins alongside the page build-out.

---

## 11. Industry-Specific Insights

### Legal / Law Firms
- **Competitive set:** Check if SERP shows generalist firms or specialist firms — specialist firms (e.g., leaselawyers.net.au) signal a mature market with clear intent
- **Accredited specialist angle:** If principal has an accreditation (e.g., LIV Accredited Property Specialist), this is a high-value USP secondary keyword — few competitors have it, and it signals authority
- **Service intent split:** Conveyancing (transactional, document-processing intent) vs property lawyer (legal advice intent) — these are meaningfully different and justify separate pages and roots
- **Powers of attorney SERP:** Government and public advocate bodies dominate — not a commercial keyword target. Cover as content section on wills/estate page
- **Probate SERP:** Primary ("probate lawyer melbourne") = all law firms ✓. Secondary choices with mixed government/informational SERPs → replace with "deceased estate lawyer [city]" or "probate solicitor [city]" (both clean commercial)
- **High-CPC signals:** Probate ($40+), commercial law ($70–$80), commercial lease ($26–$52) — high CPCs reflect high per-matter value. Low-volume + high-CPC = worth including even with small search volume
- **Conveyancing SERP:** Often dominated by specialist conveyancers (not law firms) — law firm positioning as "lawyer-backed conveyancing" is a genuine differentiator in this SERP
- **Will disputes / adverse possession / subdivisions:** Very low Melbourne-specific volume — cover as content topics on relevant pages, not as standalone keyword targets
- **Family law vs property law:** Check competitor traffic carefully — firms ranking for both can mislead. Duffy & Simon (Casey area) = mostly family law traffic, not a direct competitor for property/wills

### Trades & Contractors
- **Root keyword:** Usually the trade name + city/suburb (e.g., "concrete cutting melbourne")
- **Ambiguous terms:** Some trade terms have commercial + industrial meanings — check SERP to confirm business vertical
- **Suburb volume:** Suburb-level volume for trades can be very low — justify strategically (near job sites, industrial areas) if volume is 0
- **Second root:** Usually not justified for trades — searcher intent at suburb level is typically the same regardless of trade descriptor used

### Real Estate
- *(To be expanded)*

### Healthcare / Medical
- *(To be expanded)*

### Ecommerce / Retail
- *(To be expanded)*

### Hospitality / Accommodation
- *(To be expanded)*

### Education / Training
- *(To be expanded)*

---

## 11. Global Rule — Consolidated Project Memory Files

Every client project must have **one consolidated memory file** that serves as the single source of truth for future pickup. This applies to all project types (local business, service business, ecommerce, franchise, nationwide, etc.).

### What goes in it
- Business identity (name, address, contact, hours, ABN)
- Services offered and USPs
- Budget and split (general vs location units)
- All strategic decisions and the reasoning behind them
- Entity framework (homepage, service pages, location pages)
- Final keyword-to-page mapping with volumes and CPC
- SERP learnings (per keyword — what page type, what competitive set, what intent)
- Current site rankings summary (Ahrefs snapshot date, commercial vs informational, quick wins)
- Competitor map (names, niches, SEO strength)
- HTML deliverable file path and version
- Status and pending work (what's done, what's next)

### Naming convention
`client_[domain-without-tld].md` — e.g., `client_wslegal.md`, `client_australcontractors.md`

### Rules
- Create the file at project start; update it at every session where decisions are made
- Do NOT split client project info across multiple files — merge into one on first opportunity
- Always update the "Status & Pending" section so future sessions can resume without re-reading full history
- Add a pointer to the file in MEMORY.md under "Client Projects"

### Client folder structure — capability subfolders
All deliverables for a client go under `clients/[client-domain]/[capability]/`:
- `clients/wslegal.com.au/keyword-research/keyword-plan.html`
- `clients/wslegal.com.au/internal-links/report.html`
- Client-level assets (onboarding form, BDM brief) stay at `clients/[client-domain]/` root — shared across capabilities, not specific to one

### Always save raw briefs and onboarding forms
When a client brief, onboarding form, or any structured intake data is shared — save it immediately as a raw file in the client folder:
- File: `clients/[domain]/onboarding-form.md` or `clients/[domain]/client-brief.md`
- Save the full raw content — do not summarise or truncate
- This is the source of truth for all client context; the consolidated `client_[domain].md` is derived from it
- If anything in the consolidated file conflicts with the raw brief, the raw brief wins
- Applies to any intake data: onboarding forms, BDM notes, email briefs, call notes shared as text
