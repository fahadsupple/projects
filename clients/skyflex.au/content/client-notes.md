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

#### 3. Keyword swaps applied — all SERP-verified 2026-07-14

Four of six primaries were mis-targeted. Two (`bbq pods melbourne`, `louvred pergolas sydney`) had **zero search volume — they were slugs, not keywords.**

| Entry | Old primary | New primary | Vol |
|---|---|---|---|
| delta-commercial-folding-arm | retractable awning melbourne | `waterproof retractable awning` | 320 |
| delta-pro-retractable-roof | retractable roof system melbourne | `retractable roof pergola` | 720 |
| skyflex-4k-android-smart-outdoor-tv | waterproof tv australia | `weatherproof tv` | 390 |
| skyflex-bbq-pods | bbq pods melbourne *(zero volume)* | `bbq pods` | 720 |
| smart-toilets | smart toilets melbourne | `smart toilets` | 2,400 |
| louvred-pergolas-sydney | — unchanged, **already ranks #2** | `pergolas sydney` | 1,300 |

Old terms retained as secondaries. Every replacement was verified with a live SERP check (local pack present? product URLs in top 20?), **not** taken from DataForSEO intent labels alone — the first-choice replacement for the retractable-roof page (`retractable fabric roof`) was itself found to be installer-owned (0 product URLs) and rejected.

#### 4. INSTALLER-INTENT is the recurring trap for this client

Skyflex's **geo-scoped** keywords skew to installer/vendor-discovery intent (local pack + zero product pages ranking); **non-geo** terms skew transactional. This client previously rejected "pergola builders" terms for the same reason.

**But it is not universal** — `pergolas sydney` and `bbq pods` are both winnable by a product retailer. The test that matters is not "does a `/product/` URL rank" but **"do product *retailers* rank"**. On `pergolas sydney`, zero product-detail URLs rank yet Skyflex sits at #2 and DIY brand Pergolux at #7. Check the SERP, don't assume the pattern.

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
