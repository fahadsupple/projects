# Triple J Furniture — E-E-A-T & Content Quality Audit

**Domain:** triplejfurniture.com.au  
**Audit date:** 5 June 2026  
**Auditor:** Colana / Fahad Projects  
**Platform:** Shopify (theme: Funiter 1.0)

---

## 1. Audit Scope

Pages reviewed:
- Homepage: `https://triplejfurniture.com.au/`
- `/collections/lounges-and-sofas` (note: not `/collections/sofas-lounges` — 404)
- `/collections/bedroom-furniture`
- `/collections/coffee-tables`
- `/collections/bar-stools`
- `/collections/dining-table` (note: not `/collections/dining-tables` — 404)
- `/pages/about-us`
- `/policies/refund-policy`
- `/pages/warranty-policy`
- `/pages/faq`

---

## 2. E-E-A-T Signals Audit

### 2.1 Experience (first-hand, real-world experience)

| Signal | Present? | Notes |
|---|---|---|
| Owner/founder bio | Partial | Onboarding names Lily Tioaquen with "25+ years in furniture manufacturing, purchasing, retailing" — but this detail does NOT appear on the About Us page or anywhere visible on the live site |
| Team credentials visible | No | No team page, no named staff, no "meet the team" content |
| Behind-the-scenes content | No | No supplier photos, warehouse imagery, or showroom process content |
| Custom/bespoke project examples | No | Custom furniture service mentioned in footer ("Custom Furniture Sydney") but no portfolio or case study pages |
| Community involvement (Red Cross/CMS) | No | Not mentioned anywhere on the live site despite being in onboarding |
| Customer count | Yes | "Over 20,000 customers served" — present on homepage |
| Years in trade | Yes | "More than 20 years in the trade" — homepage and footer |

**Assessment:** Experience signals exist only as bland numerical claims. No personal story, no founder narrative, no staff faces, no behind-the-scenes content.

---

### 2.2 Expertise

| Signal | Present? | Notes |
|---|---|---|
| Furniture industry knowledge demonstrated | Partial | Homepage copy mentions "furniture manufacturers, importers, interior designers and joinery specialists" with combined 30 years experience — but no named experts, no bios |
| Material/construction explanations | Partial | Product descriptions include material specs; collection pages contain some FAQ content about materials |
| Buying guides | No | No dedicated buying guides (e.g., "How to choose a sofa", "What size dining table do I need") |
| Style/room planning content | No | No blog, no editorial guides, no interior design advice section |
| Sustainability/sourcing explanation | Partial | Some product descriptions mention SVLK-certified timber; not systematically applied across all products |
| FAQ content | Yes | Homepage has FAQPage JSON-LD schema with 3 FAQs. Several collection pages have FAQ sections embedded in bottom copy. `/pages/faq` exists but rendered content was blocked by JS |

**Assessment:** Expertise is implied but not demonstrated. The site presents products competently but misses the opportunity to prove deep category knowledge through guides, editorial content, or expert commentary.

---

### 2.3 Authoritativeness

| Signal | Present? | Notes |
|---|---|---|
| Brand mentions / PR | Not audited (off-site) | DR 8 — very low. No evidence of press coverage on-site |
| Industry associations | No | No memberships, certifications, or accreditation logos |
| Awards | No | None displayed |
| Media / press coverage | No | Nothing referenced on-site |
| ABN displayed | Yes | Footer: "ABN Number 92 123 587 173" |
| Physical address displayed | Yes | "590 Hume Hwy, Yagoona" — present on contact and footer |
| Google Business Profile | Not visible on-site | GSC/GBP not audited in this pass |

**Assessment:** Authority signals are minimal. ABN and address display is positive. No third-party validation signals (associations, awards, media) are present on the site.

---

### 2.4 Trustworthiness

| Signal | Present? | Notes |
|---|---|---|
| ABN displayed | Yes | Footer — "ABN Number 92 123 587 173" |
| **ABN DISCREPANCY** | **Flag** | Onboarding form (Q2) states ABN: **95123587173**. Footer displays ABN: **92 123 587 173** (= 92123587173). These are **different numbers** — confirm correct ABN with client immediately |
| Physical address | Yes | 590 Hume Hwy, Yagoona NSW 2199 |
| Phone | Yes | 02 9790 2588 — in header and footer |
| Email | Yes | sales@triplejfurniture.com.au — in header and footer |
| Business hours | Yes | "Monday to Friday, 9am to 5pm" — mentioned in collection copy |
| Returns/refund policy | Yes | `/policies/refund-policy` — exists and accessible |
| Warranty policy | Yes | `/pages/warranty-policy` — exists and accessible |
| Privacy policy | Yes | Linked from footer |
| Shipping policy | Yes | Linked from footer |
| Customer reviews | Partial | TrustShop review app is installed and configured for product-level reviews. No aggregate site-level review count or star rating is displayed on homepage. Review counts on individual products were not audited |
| Security / payment trust | Yes | Shopify Payments, Apple Pay, PayPal — secure checkout implied |
| Live chat | Claimed | Homepage copy references "live chat" but no visible widget confirmed from HTML |
| Public liability insurance | Not displayed | $20M cover per onboarding — not mentioned on site |

**Assessment:** Core trust signals (contact details, ABN, policies) are present. The ABN discrepancy between onboarding and footer is a material credibility risk that must be resolved. Reviews exist at the product level but the site does not aggregate or display them prominently on collection or homepage level.

---

## 3. Establishment Date Discrepancy

**Critical inconsistency identified:**

| Source | Year |
|---|---|
| Onboarding form (Q3, submitted by owner) | **2003** |
| Website USP block (homepage) | **1997** |
| Website footer copy | "20 years" (consistent with ~2006, but copy is static) |
| About Us page | "20 years" |
| Onboarding form Q14 (USPs) | "Established since 1997 — over 20 years of experience" |

The onboarding form Q3 says 2003, but Q14 (USPs, also filled by the owner) says 1997. The live site uses 1997 throughout.

**Recommendation:** Clarify with the client directly whether the business was established in 1997 or 2003. The 1997 claim appears in the owner's own USP wording, suggesting it may refer to an earlier entity, prior business involvement, or a predecessor operation. The 2003 may be the incorporation date of the current legal entity. Either way, the copy should be consistent and accurate — Google's quality raters flag contradictory establishment claims as a trust signal failure.

---

## 4. Collection Page Content Audit

### 4.1 Content Depth by Page

| Page | Title Tag | Meta Description | Top Intro Copy? | Bottom Editorial Block? | FAQ Section? | Score |
|---|---|---|---|---|---|---|
| `/collections/lounges-and-sofas` | "Lounges Sydney | Quality Lounge Suites | Triple J Furniture" | Yes — specific, includes warranty + price beat | No intro above products | Yes — strong FAQ, CTA at bottom | 7/10 |
| `/collections/bedroom-furniture` | "Bedroom Furniture Sydney | Beds, Tallboys & Storage | Triple J Furniture" | Yes — specific | No intro above products | Yes — strong FAQ (7 questions), CTA at bottom | 8/10 |
| `/collections/coffee-tables` | "Coffee Tables Sydney | Designer Pieces | Triple J Furniture" | Yes — specific | No intro above products | Yes — strong FAQ (5 questions), CTA at bottom | 7/10 |
| `/collections/bar-stools` | "Kitchen Bar Stools Sydney | Triple J Furniture" | No meta description present | No intro above products | Yes — strong FAQ (5 questions), CTA at bottom | 6/10 |
| `/collections/dining-table` | "Dining Table | Triple J Furniture" | No meta description present | No intro above products | No — no bottom editorial block found | 3/10 |

### 4.2 Key Observations

**Strengths:**
- Most collection pages have strong bottom editorial blocks with FAQ content, buying advice, and local Sydney context
- FAQ content is well-written and addresses genuine purchase questions (sizing, materials, delivery, apartments)
- Bedroom, coffee tables, and lounges pages have relevant FAQPage schema-style content
- Titles for most pages include "Sydney" location modifier and specific category name

**Weaknesses:**
1. **No top intro copy on any collection page** — the editorial content appears only at the bottom, below the entire product grid. Users (and crawlers) hit products immediately without category context. A 2–3 sentence intro above the grid would immediately improve relevance signalling
2. **Dining table page is thin** — no meta description, no bottom editorial block, no FAQ content. Title is generic "Dining Table | Triple J Furniture". This is the weakest collection page audited
3. **Bar stools page missing meta description** — content is strong but the meta tag is absent
4. **Collection URLs are non-intuitive** — the keyword-targeted URLs like `/collections/sofas-lounges` and `/collections/dining-tables` return 404s. Actual URLs are `/collections/lounges-and-sofas` and `/collections/dining-table`. This means any external links using the expected URL pattern will 404

---

## 5. Homepage Content Audit

### 5.1 Structure and Content Quality

**Page title:** "Affordable Furniture Sydney | Triple J Furniture" — good, primary keyword + brand  
**Meta description:** "Shop affordable furniture in Sydney at Triple J Furniture. Quality living, dining and bedroom pieces with a Price Beat Guarantee and up to 10-year warranty." — good, includes USPs

**Content present on homepage:**
- Main H1 editorial block: ~250 words covering value proposition, showroom, delivery, range overview — well-written, Sydney-targeted
- USP block: Price Beat Guarantee, Established since 1997, Warranty up to 10 years, Showroom, Secure online payment
- Category navigation copy blocks: Living Room, Dining & Kitchen, Bedroom, Home Office & Outdoor — brief but relevant
- "Why Choose Triple J Furniture" section: 5 bullet points + 2 paragraphs on team expertise and custom services
- Bottom CTA: Showroom hours, phone, email, live chat mention
- FAQPage JSON-LD schema: 3 questions/answers (visible in source, likely rendered in page)

**Content gaps on homepage:**
- Testimonials section: The About Us page references "Testimonials" as a section header, but no actual review content is rendered (likely loaded via JS from TrustShop — no static fallback text)
- No imagery alt-text audit performed (beyond-scope of this content audit)
- OG site name is "Triplejfurniture " (trailing space — minor but worth fixing for social sharing)

---

## 6. About Us Page Audit

**URL:** `/pages/about-us`  
**Content:** Thin. Consists of:
- One paragraph: "Triple J Furniture has been supplying the south-western district of Sydney and the wider online community with stunning furniture for 20 years. We stock a variety of furniture... Your satisfaction is always our top priority..."
- A "Reasons to shop with us" section with four icons: Price Beat Guarantee, Establish Since 1997 *(typo: "Establish" should be "Established")*, Fast and free customer support, Testimonials
- A Testimonials placeholder — no actual review content rendered

**Issues:**
1. **Extremely thin narrative content** — the page says almost nothing about who the business is, who runs it, or why it exists
2. **Typo on a trust signal** — "ESTABLISH SINCE 1997" should be "ESTABLISHED SINCE 1997"
3. **No founder story** — Lily Tioaquen's 25+ year background from the onboarding form is entirely absent from the live site. This is the single biggest missed E-E-A-T opportunity on the site
4. **No team content** — no names, photos, or credentials for any staff
5. **Testimonials section is empty** — relies on JS to populate; renders no content server-side, meaning Google likely sees an empty section

---

## 7. Warranty Policy Audit

**URL:** `/pages/warranty-policy`  
**Content summary:** The page covers structural warranty (1 year from purchase date), what is and is not covered, and the claim process.

**Issue: Warranty duration inconsistency**  
The warranty policy page states: *"This warranty covers defects in materials and workmanship under normal residential use for a period of **one year** from the date of purchase."*

However, the site's primary USP — featured on the homepage, in collection page copy, and in FAQs — is **"warranty up to 10 years"**.

This is a significant trust signal conflict. Shoppers who read the warranty policy will see "1 year" and conclude the "up to 10 years" marketing claim is misleading. The policy should clarify:
- The 10-year claim likely applies to specific premium products (frame/structural warranty)
- The 1-year standard may apply to most items
- The current policy page does not mention the 10-year option at all

**Recommendation:** Rewrite the warranty policy to clarify the tiered structure (e.g., "1-year standard / up to 10-year structural warranty on selected products"). This prevents chargeback disputes and supports the E-E-A-T trust dimension.

---

## 8. Thin Content — Shopify Collection Page Weakness

**Typical Shopify pattern observed here:**

Collection pages on Shopify default to product grids with no editorial content. Triple J has partially addressed this by adding bottom editorial blocks on most key pages. However:

1. **No content above the fold on collection pages** — the page goes directly from breadcrumb to product filter to product grid. Google sees a large list of product snippets before any editorial text.
2. **The dining-table collection page has no editorial content at all** — just a product grid across 19 pages
3. **Category description is not in a crawlable position** — all editorial text sits below 100+ product listings; Google's crawl budget allocation and content weighting tends to favour above-the-fold content

**Priority fix order:**
1. Dining table collection — add bottom editorial block + meta description immediately (most urgent — currently a bare product grid with generic title)
2. Bar stools — add meta description
3. All collection pages — consider adding a 2-sentence intro above the product grid

---

## 9. Schema Markup Audit

| Schema type | Present? | Location | Notes |
|---|---|---|---|
| FAQPage | Yes | Homepage | 3 questions in JSON-LD — valid structure |
| Organization | No | — | Not present — missed opportunity for NAP, logo, sameAs social |
| LocalBusiness | No | — | Not present — critical for Sydney showroom E-E-A-T |
| Product | Via Shopify | Product pages | Shopify generates basic Product schema automatically |
| Review / AggregateRating | Partial | Product pages | TrustShop may inject review schema on product pages — not confirmed for collection pages |
| BreadcrumbList | Not confirmed | — | Not seen in homepage source |
| WebSite (SearchAction) | Not confirmed | — | Shopify may generate; not seen in homepage source |

**Priority additions:**
- `LocalBusiness` schema with NAP (address, phone, hours, ABN) — critical
- `Organization` schema with logo and social profile links
- Review aggregate schema on collection pages (if TrustShop supports this)

---

## 10. Summary: Priority Issues by Severity

### Critical (fix immediately)
1. **ABN discrepancy** — onboarding says 95123587173, footer displays 92123587173. Verify with client and correct. Incorrect ABN is a legal and trust risk.
2. **Warranty policy contradicts marketing claim** — policy says 1 year; USPs say up to 10 years. Rewrite policy to explain tiered warranty structure.
3. **Establishment date inconsistency** — 1997 (site) vs 2003 (onboarding Q3). Confirm correct date with client; standardise across all pages.

### High (address in next sprint)
4. **About Us page is too thin** — 2 sentences of copy, empty testimonials section, typo ("ESTABLISH"), no founder story
5. **Dining table collection page is bare** — no meta description, no editorial block. Weakest collection page.
6. **No LocalBusiness or Organization schema** — Sydney showroom has no structured data to support local E-E-A-T
7. **Founder/owner credentials not on site** — Lily Tioaquen's 25+ years experience, team specialists, community involvement (Red Cross/CMS) all absent from live content

### Medium (content improvement backlog)
8. **Bar stools page missing meta description** — straightforward fix
9. **No top intro copy on any collection page** — editorial context appears only below products
10. **No blog or buying guides** — expertise is claimed but not demonstrated through content
11. **No aggregate review display on homepage or collections** — TrustShop is installed but not showcasing review summary
12. **OG site name trailing space** — "Triplejfurniture " should be "Triple J Furniture"

### Low (monitor)
13. **404 on expected collection URLs** — `/collections/sofas-lounges` and `/collections/dining-tables` return 404 (actual URLs differ). No SEO impact if redirects are in place, but worth checking
14. **Testimonials on About Us renders empty without JS** — Google likely sees an empty section; add static fallback quotes
15. **"20 years" copy is static** — footer and About Us say "20 years" regardless of current year. If 1997 is correct, it should say "28 years" in 2026.

---

## 11. What is Working Well

- Homepage has genuine, well-written editorial content (not keyword-stuffed)
- Most collection pages have strong bottom editorial blocks with location-specific FAQ content
- ABN, physical address, phone, email, and business hours are consistently displayed
- Policy pages (refund, shipping, warranty, privacy) all exist and are linked
- TrustShop review system is installed and configured (even if not prominent)
- Product descriptions include material specs, dimensions, and warranty notes
- Meta titles on key collection pages include "Sydney" modifier and category keywords
- FAQPage JSON-LD schema is present on homepage with valid structure

---

*File created: 5 June 2026 | Audit basis: live site crawl + HTML analysis*
