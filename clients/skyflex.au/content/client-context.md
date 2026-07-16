# skyflex.au — Content Plugin Context

_Rebuilt: 2026-07-16T06:44:13Z_

## 1. Who this client is

- **Domain:** skyflex.au
- **Audience:** Our ideal customers are homeowners and businesses in Melbourne (and Sydney) looking to transform their outdoor spaces into comfortable, year-round living areas. This includes homeowners wanting to enhance their backyards, patios, and gardens with stylish, adjustable louvred pergolas, as well as commercial property owners seeking to add functional and aesthetically appealing outdoor structures. Our customers value quality, durability, and affordability, and may be either DIY enthusiasts who want to install a pergola kit themselves, or those who prefer to use our approved installer network. They are looking for solutions that handle Melbourne's variable weather conditions and add long-term value to their property.
- **Services:** BBQ Pods, DIY Pergola Kits, Folding Arm Awnings, Louver Roofs, Pergolas, Retractable Roof Systems, Smart Outdoor TVs, Smartoilets
- **Locations served:** Melbourne, Sydney, Queensland

## 2. Notes from the analyst

### Deliverable format — existing vs new content (analyst directive, 2026-07-16, Fahad)

**Every final deliverable must visually distinguish EXISTING content from NEW content**, so the client/developer can see at a glance what is being reused unchanged versus what is being added, and where.

- **Existing content** = text copied VERBATIM from the current live page (nothing changed). Render it on a **yellow background** (`background:#fff3b0` / highlight) in the combined review HTML export.
- **New content** = anything newly written for this engagement. Render it plainly (no highlight).
- **CRITICAL — existing content is shown IN POSITION, embedded in the final content, not listed separately (2026-07-16 clarification).** The deliverable for any page that has existing content must present the INTENDED FINAL PAGE: the existing content (yellow) interleaved with the new content (plain) in the exact order they should appear, so the developer sees at a glance what to keep AND where it sits relative to the new blocks. For `add-blocks` pages this is the whole point: show the existing page body (yellow) with the new blocks (plain) placed where they belong around it. For `rewrite-existing` pages: show the new content (plain) with any verbatim-retained existing spans (yellow) in place, and reference the existing content being replaced. Do NOT just append a list of existing spans at the end — position them.
- This applies to **every entry**, per page-mode:
  - `add-blocks` (homepage, louvred-pergolas-sydney): the existing page body is preserved verbatim → shown yellow; the added blocks → shown plainly. This is where the distinction matters most.
  - `rewrite-existing` (the 4 product pages): most of the body is newly written, but any sentence/spec/price copied verbatim from the existing page must still be marked yellow.
  - `new-page` (smart-toilets): all new → nothing yellow.
- **Provenance is a writer-agent responsibility:** the writer must retain and label which spans are copied-existing vs newly-written so the exporter can highlight them. The exporter renders the yellow-vs-plain distinction in the combined review document.
- **Existing content must be captured** for the add-blocks + rewrite pages (fetch the current live page) so there is a verbatim source to mark yellow. Homepage is research-skipped, so its current content must be fetched at generate/export time.

---

### Analyst decisions — 2026-07-14 (Fahad)

#### 1. COMMERCIAL MODEL IS PER-PRODUCT — never assume DIY add-to-cart

`client-profile.json` describes Skyflex as a "DIY product retailer". **The live site contradicts this three ways.** Analyst decision: the model genuinely varies by SKU. Each page must reflect its **own live commercial terms**, verified from that entry's research bundle.

| Entry | Actual live commercial model | Writer implication |
|---|---|---|
| `delta-commercial-folding-arm` | **Supply-only.** $2,000–$2,300, marked "(Supplied)", add-to-cart, no install. | Buy/ship framing OK. Do not imply installation. |
| `skyflex-bbq-pods` | **Consultation-led custom.** $13,500. Live page: *"Custom Order Product – Not available for direct online purchase. Consultation Required."* | **Do NOT write buy-now / DIY / add-to-cart framing or CTAs.** Enquiry/consultation CTA only. |
| `louvred-pergolas-sydney` | **Hybrid.** Live page says *"SkyFlex designs and installs"*; also a DIY kit shipped to Sydney via an approved-installer network. | Lead on kit-shipped-to-Sydney + installer network. Do not claim a Sydney branch. |

**WRITER RULE:** before writing any CTA or purchase framing, read the entry's live-page commercial terms from its research bundle. Never default to add-to-cart.

#### 2. SMART TOILETS = conversion asset, NOT an organic contender

Research verdict is that a new page **will not rank organically**, and writing it well will not change that:

- Skyflex has **2 SKUs** (both sitting in WooCommerce `Uncategorized`); competitors field **8–31** products with real facets. A 2-product grid reads as thin *by construction* — a range problem, not a copy problem.
- **Zero bathroom topical authority.** The entire corpus is outdoor living.
- Every top-20 domain is a bathroom/plumbing specialist, category pure-play, or toilet manufacturer. **No adjacent-vertical or generalist retailer appears anywhere in the top 20.**
- Neither Google's AI Overview nor ChatGPT cites skyflex.au; all cited sources are bathroom specialists.

**Decision: build it anyway, as a paid/direct landing + conversion asset.** Requirements:

- Target the head term **`smart toilets` (2,400/mo)** — geo modifier dropped (Melbourne and national SERPs share 9 of the top 10 domains, so the modifier costs ~98% of addressable demand for zero differentiation).
- Match the **faceted category-grid** shape Google rewards: 12–13 of the top 20 are faceted collection pages; **zero product-detail pages rank.**
- Include the on-page FAQ block (11 real PAA questions captured in research).
- **Set expectations with the client: do not promise organic rankings.**

#### 3. Keywords are FIXED page targets — do not swap them (corrected 2026-07-16)

The primary keyword on each entry is the **client-assigned target** from the prior keyword→URL engagement, mapped to a specific live URL. **The pipeline's job is to optimise each page to serve its assigned keyword — not to second-guess the keyword.** An earlier analyst pass wrongly swapped 5 primaries on the reasoning that low/zero DataForSEO volume meant a keyword was "wrong." That was overreach and has been reverted: **zero *measured* volume is not zero searches** (DataForSEO floors low counts to null), and an exact product-plus-location match is a legitimate target for a niche product page.

**Assigned primaries (authoritative — use these):**

| Entry | Primary (assigned) | Lead secondary (higher-volume, same-SERP capture) |
|---|---|---|
| delta-commercial-folding-arm | `retractable awning melbourne` | `waterproof retractable awning` (320) |
| delta-pro-retractable-roof | `retractable roof system melbourne` | `retractable roof pergola` (720) |
| skyflex-4k-android-smart-outdoor-tv | `waterproof tv australia` | `weatherproof tv` (390) |
| skyflex-bbq-pods | `bbq pods melbourne` | `bbq pods` (720) |
| smart-toilets | `smart toilets melbourne` | `smart toilets` (2,400) |
| louvred-pergolas-sydney | `pergolas sydney` (**ranks #2**) | `louvred pergolas sydney` |

**How the research is used (advisory, not a swap):** where the exact assigned term has low measured volume, the SAME page also targets the higher-volume head term as a lead secondary — they share a SERP (e.g. `bbq pods melbourne` and `bbq pods` overlap on 12 of ~16 organic domains), so one well-optimised page ranks for both. The assigned term goes in the title tag / H1 (exact match); the head term is worked naturally into headings and body. **No keyword is dropped.**

The SERP-intent findings below (installer-domination on some geo terms) are **page-strategy input** — they tell the writer what the page must do to compete and what a realistic timeline is — **not** a licence to change the target keyword.

#### 4. INSTALLER-INTENT on some geo terms — a page-difficulty signal, not a keyword verdict

Some of Skyflex's **geo-scoped** keywords have SERPs skewed to installer/vendor-discovery intent (local pack present + few/no product pages ranking) — notably `retractable awning melbourne` and `retractable roof system melbourne`. This does **not** mean the keyword is wrong; it means the page has to work harder and the timeline is longer. What it tells the writer:

- The page must look like a credible **buy-here** destination (clear product, price/enquiry path, specs, differentiation) to stand out in a SERP of service pages.
- Capturing the higher-volume non-geo head term as a lead secondary is the realistic near-term traffic path while the exact geo term matures.
- Set client expectations on timeline for the geo term; don't promise a fast win against a local pack.

**And the pattern is not universal** — `pergolas sydney` and `bbq pods` are winnable by a product retailer. The test is not "does a `/product/` URL rank" but **"do product *retailers* rank"**. On `pergolas sydney`, zero product-detail URLs rank yet Skyflex sits at #2 and DIY brand Pergolux at #7. Read each SERP; don't assume the pattern.

#### 5. Live-site defects to send to the client (independent of content work)

- **BBQ pods page:** title tag reads `Delta Motorised | Skyflex`; meta description is about **louvred pergolas**. Both are copy-paste leftovers from another product and never mention BBQ pods.
- **Sydney pergolas page:** links to **`skyflex.com.au`** (wrong domain — the live site is `skyflex.au`), and shows a **Melbourne phone number** on a Sydney page.
- **Outdoor TV page:** the 5 testimonials are all about louvre-roof/pergola installs by "Chris" — none are about the TV.
- **Smart toilets:** both SKUs sit in WooCommerce `Uncategorized` — the taxonomy does not exist yet.

#### 6. Facts — publishable vs suppressed

The fact extractor bucketed 7 unrelated percentages into one `metrics.percentage` fact. Split into distinct facts; placements set:

- **Publishable (`any`):** `social-proof.referral-rate` = **50%** of new business from referrals.
- **Suppressed (`off-page`):** `social-proof.retention-rate` = 100% (unsubstantiated absolute claim — misleading-representation risk); all per-product discount figures (volatile promo pricing that goes stale).

#### 7. Content-integrity guardrails carried from research

- **Do NOT write** "anti-glare screen" or "corrosion-resistant casing" on the outdoor TV page — both have **zero search volume** *and* appear nowhere on the live page. Writing them is fabrication. (They sit in the entry's secondary-keyword list, so they will look legitimate.)
- **Outdoor TV — 1000 nits is the category floor, not a differentiator.** Competitors filter 1000/1500/2000/3500 nits and class 1000-nit units as *partial sun*. Frame brightness honestly (≈3× an indoor TV's ~300 nits) and lead on **full-sun vs partial-shade placement** — the page currently says nothing about it.
- **Sydney suburb ground truth is INSUFFICIENT.** Brave returned zero locations/discussions/FAQs. **Do not invent** Sydney climate, council rules, or building-stock claims. The suburb-data file carries an explicit `prohibited_claims` list — honour it.
- **No FAQ block for the awning or BBQ pod pages from PAA** — both returned **zero** PAA questions and zero Brave discussions. There is nothing data-grounded to seed one from. Do not invent questions.

