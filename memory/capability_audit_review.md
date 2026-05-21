---
name: audit-review capability
description: Translating a completed SEO audit report into actionable deliverables — quick wins plan, client data checklist, and developer requirements doc
type: feedback
---

# Capability: audit-review

**When triggered:** A completed SEO audit report (by Hardy or another auditor) needs to be translated into
a prioritised action plan and developer brief.

**Deliverables (in order):**
1. `quick-wins-action-plan.html` — prioritised batches, styled HTML, for internal/client use
2. Developer requirements `.txt` — plain text, copy-paste ready, for handing directly to developers
3. Client data checklist — conversational or as a section inside the developer doc

---

## What this capability produces

### 1. Quick Wins Action Plan (HTML)

File: `clients/[domain]/quick-wins-action-plan.html`

A dark-theme styled HTML file with:
- Batch sections: Batch 1 (today), Batch 2 (week 1), Batch 3 (weeks 2–4),
  Batch 4 (months 1–3), Batch 5 (ongoing)
- Each item has: item ID (e.g. TITLE-001), priority badge (CRITICAL/HIGH/MEDIUM/LOW),
  effort estimate, and specific fix instruction
- Items assigned across SEO team, developer, and client

Batching logic:
- **Batch 1 (today):** Quick technical wins + title/H1 fixes + GBP immediate actions.
  Target: changes that take under 15 minutes and unlock ranking signals.
- **Batch 2 (week 1):** Systematic meta/title fixes, schema config, NAP standardisation.
- **Batch 3 (weeks 2–4):** Content rewrites, citation building, redirect clean-up.
- **Batch 4 (months 1–3):** Schema implementation, cannibalisation resolution, E-E-A-T content.
- **Batch 5 (ongoing):** Review acquisition, content gap, topical authority build.

---

### 2. Developer Requirements (.txt)

File: `clients/[domain]/developer-requirements.txt`

Format rules (established from group1linemarking + globallocksmiths):
- **Plain text** — not HTML, not markdown, so it can be pasted into any PM tool
- Numbered changes within lettered sections (A1, A2... B11, B12...)
- Each change contains only a precise description of WHAT needs to change
  (the exact URL, current value, new value/code). No CMS navigation instructions.
- No time estimates — do not include "Estimated time" on any change
- No priority labels — the section grouping itself communicates urgency.
  Section A = do first, Section B onwards = in order
- Always use full URLs — `https://[domain]/path/` not URI paths like `/path/`
- Changes with visual impact: include a DESIGN NOTE explaining existing design patterns
  so the developer matches the site's current look without guessing
- Include actual copy-paste-ready code (JSON-LD blocks, corrected text, regex patterns)
- Summary table at end: #, Change, Who

Section structure (use this every time):
```
SECTION A — EMERGENCY FIXES           (do first, most under 15 mins)
SECTION B — ANALYTICS + TECHNICAL     (tracking, crawl, performance)
SECTION C — PHONE, NAP + META FIXES   (contact data consistency)
SECTION D — TITLES, META + H1 FIXES   (SERP appearance)
SCHEMA                                 (JSON-LD implementation)
INTERNAL LINKING                       (PageRank distribution)
SECTION E — CLIENT TO ACTION           (GBP — never assign to developer)
SECTION F — BLOCKED — AWAITING DATA   (can't start without client info)
```

**Critical rules:**
- GBP changes ALWAYS go in Section E (client to action) — never assign to dev
- Blocked items go in Section F — never mix with actionable dev tasks
- If access is already confirmed (WP, GSC, GA4), note it at the top so devs
  know they don't need to request access
- Total time estimate at the top and bottom of the doc

---

### 3. Client Data Checklist

When reviewing an audit, identify what can't be done without client input:
- **Authority building form covers:** ABN, certifications, insurance, awards, social URLs
- **Additional items typically needed:** canonical phone number, founding year,
  owner name + bio + headshot, GBP URL (g.page link), confirmation of which
  states/cities are genuinely serviced, office status for each listed address,
  project records for gallery photos (suburb, sector, year)
- **Visual assets needed:** project photos, team photos, premises exterior,
  headshots, accreditation/association logos

Present this as a two-part list:
1. What the authority form already collects (client doesn't need to be asked twice)
2. What's extra — specific items the form doesn't cover

---

## Audit phases to check (standard Hardy audit structure)

When reviewing an audit file, extract and process all 6 phases:

1. **Technical SEO** — robots.txt, sitemap, crawl errors, redirects, broken links,
   page speed, Core Web Vitals, viewport meta, duplicate content flags
2. **On-Page SEO** — title lengths, meta description coverage, H1 presence/duplicates,
   keyword cannibalisation, WooCommerce CMS title templates ("Archives" default)
3. **Content & E-E-A-T** — word count, named authors, About Us quality, trust signals,
   templated/thin content risk, gallery alt text, establishment claims consistency
4. **Local SEO** — NAP consistency, postcode accuracy, GBP photo count,
   review count vs competitors, Local Pack appearance, citation directories
5. **Keywords & SERP** — title mismatches (copy-paste errors between pages),
   suburb/service H1 template errors, meta description phone number typos
6. **Competitors & Backlinks** — PBN/toxic links, competitor schema tactics,
   competitor FAQ/review schema, disavow candidates

---

## Common findings and fixes (reference patterns)

### Schema issues
| Finding | Fix |
|---------|-----|
| No LocalBusiness JSON-LD anywhere | Add to homepage `<head>`. Include address, phone, areaServed, openingHours, aggregateRating, sameAs |
| CreativeWorkSeries schema with AggregateRating | REMOVE immediately — Google classifies this as review snippet spam, manual action risk |
| BreadcrumbList emitted by both theme and Yoast | Disable the theme-side breadcrumb JSON-LD — Yoast is the single source |
| No Service JSON-LD on service pages | Add Service block to each service page `<head>`, reference homepage @id as provider |
| No FAQPage schema | Add FAQ accordion section (visible) + FAQPage JSON-LD. Use existing accordion component if present |
| Location page schema missing areaServed | Add area-scoped Service JSON-LD at template level — auto-generates for all location pages |

### LocalBusiness JSON-LD template (standard — adapt per client)
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://[domain]/#localbusiness",
  "name": "[Business Name]",
  "url": "https://[domain]/",
  "telephone": "[canonical phone]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[street]",
    "addressLocality": "[suburb]",
    "addressRegion": "[state]",
    "postalCode": "[postcode]",
    "addressCountry": "AU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": [lat],
    "longitude": [lng]
  },
  "areaServed": [{"@type": "Place", "name": "[suburb, state]"}],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "17:00"
  }],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[x.x]",
    "bestRating": "5",
    "ratingCount": "[n]",
    "itemReviewed": {"@id": "https://[domain]/#localbusiness"}
  },
  "sameAs": ["[GBP URL]", "[Facebook URL]", "[LinkedIn URL]"]
}
```

### Title/meta issues
| Finding | Fix |
|---------|-----|
| WooCommerce product-category pages show "X Archives ▷ Free Quote" | Update Yoast → Search Appearance → Taxonomies → Product Category title template |
| 50+ pages over 60 chars | Change global Yoast title suffix template (one change fixes all) |
| Paginated category pages have duplicate titles | Add %%page%% to Yoast title template |
| Copy-paste title error (e.g. page A's title on page B) | Fix manually in Yoast for that specific page |
| Missing meta on 20+ pages | Set Yoast global template per content type to generate baseline metas |
| Product variant pages share identical meta | Rewrite individually per WP Admin → Products — add size/feature in first sentence |

### Technical issues
| Finding | Fix |
|---------|-----|
| `Crawl-delay: 10` before any User-agent block | Delete that line from robots.txt (syntax error Bing/Yandex honour) |
| `user-scalable=no` in viewport meta | Remove from header.php — WCAG violation |
| Stale sitemap lastmod (years old) | Force regenerate via Yoast → Tools → File editor → Save |
| Broken internal link to 404 | Find in WP content search + set up 301 redirect as fallback |
| Duplicate suburb URLs (e.g. /plains/ and /browns-plains/) | 301 redirect the non-canonical to the canonical |
| GA4 not firing | Check analytics plugin activation + GTM container published + consent plugin default state |
| Competitor tabs auto-opening | Plugin/widget injecting JS — deactivate plugins one by one to identify source |
| Slow location page template | Run Lighthouse, identify bottleneck (usually Maps iframe or unoptimised image in template) |

### H1 issues
| Finding | Fix |
|---------|-----|
| H1 missing entirely | Add to page content area, before first H2. Match existing H1 design class |
| Sub-service pages show only suburb name as H1 (e.g. "Mackay" on /areas-we-serve/mackay/bollards/) | Template-level fix — update to pull both {service} and {suburb} tokens |
| Homepage H1 has keyword stuffing or brand repetition | Rewrite to clean single version |
| Pagination pages share H1 with page 1 | Add "— Page 2" suffix |

### NAP and phone issues
| Finding | Fix |
|---------|-----|
| Postcode typo (5 digits instead of 4) | Fix in page content + submit URL in GSC for reindex |
| Corrupt tel: href (garbled number) | Fix in page builder + search sitewide via Better Search Replace |
| Multiple phone numbers in meta descriptions | Decide canonical number with client, then bulk replace in Yoast metadesc fields |
| Address without office status context | Add disclosure text (e.g. "Sales Enquiries only") — match existing heading style |

### Local SEO
| Finding | Fix |
|---------|-----|
| GBP primary phone is mobile, website uses 1300 | Client to update in GBP → Info → Phone |
| GBP has <10 photos | Client to upload: project completions, team, equipment, premises |
| GBP service area not populated | Client to add all serviced suburbs |
| 0 responses to existing reviews | Client to respond personally to all — use reviewer's first name + mention service |
| Low review count vs competitors | Implement post-job review card/QR code + 24hr SMS follow-up |

### Backlinks
| Finding | Fix |
|---------|-----|
| Backlink with anchor text explicitly mentioning "PBN" | Add to disavow file immediately |
| Known spam link domains (link shorteners, screenshot farms) | Add to disavow file |

---

## Design notes rule (always apply)

For **every** change that affects a visible element on the site, include a DESIGN NOTE in the
developer brief describing:
- The existing CSS class or component being used (e.g. `class="small_font"` on H1s)
- The sizing/spacing pattern to match (e.g. ALL CAPS in hero banner for hub pages)
- Whether the change shortens or lengthens existing text (flag if it may affect layout)
- Which device to check (desktop + mobile for any banner/hero change)
- Whether an existing component should be reused rather than creating a new one

Example:
> DESIGN NOTE: The existing H1 on sub-service pages uses the CSS class "small_font".
> Use the same class on the new H1. The new text "Bollards Mackay" is slightly longer
> than a single suburb name — verify it does not overflow the banner on mobile.

---

## Workflow

1. Read the full audit file — extract all 6 phases completely before doing anything
2. Create item IDs for every finding (TITLE-001, SCHEMA-001, GBP-001, etc.)
3. Categorise by: who does it (dev/client/SEO), and urgency (emergency/high/medium/low)
4. Create `quick-wins-action-plan.html` — batched view for internal use
5. Identify what requires client data before starting (blocked list)
6. Create `developer-requirements.txt` — one file the dev can act on independently
7. Provide client data checklist conversationally or as an appendix

**File locations:**
- `clients/[domain]/quick-wins-action-plan.html`
- `clients/[domain]/developer-requirements.txt`

---

## What NOT to do

- Do not assign GBP changes to developers — always Section E (client)
- Do not mix blocked tasks with actionable tasks — always Section F
- Do not write pseudocode in the developer doc — provide real, copy-paste-ready code
- Do not list "nice to have" content suggestions in the developer doc — only implementation tasks
- Do not write DESIGN NOTE only when you remember — it is required on every visual change
- Do not include estimated time on any change — the dev team doesn't need it
  and it's not our job to estimate their work
- Do not include Priority labels (CRITICAL/HIGH/MEDIUM/LOW) — the section order
  already communicates urgency. Section A = do first, that's all they need
- Do not explain WHY the change is needed (SEO impact, Google behaviour, ranking effect)
  — describe only WHAT to change (current value, new value, URL, code)
- Do not include 'After:' verification steps (e.g. 'flush cache', 'verify in GSC',
  'check in Google Rich Results Test') — those are the SEO team's job, not the developer's
- Do not hard-wrap prose lines at 70 characters. Write descriptive text as single long
  lines so pasting into Google Docs doesn't create unwanted line breaks. Exception:
  code blocks, URL lists, and structural elements (section headers, dividers) can
  stay on separate lines
- Do not include CMS navigation instructions (e.g. "WP Admin → Yoast → Search Appearance")
  — the developer knows their tools. Describe WHAT to change, not HOW to navigate to it
- Do not use URI paths alone (e.g. `/services/line-marking/`) — always write the full URL
  (e.g. `https://[domain]/services/line-marking/`) so it's clear and copy-pasteable

---

**First established:** May 2026 — group1linemarking.com.au SEO audit review (Hardy audit)
**Reference client:** `clients/group1linemarking.com.au/`
  - `developer-requirements.txt` — 27 dev tasks, full JSON-LD code, design notes
  - `quick-wins-action-plan.html` — 47 items across 5 batches
