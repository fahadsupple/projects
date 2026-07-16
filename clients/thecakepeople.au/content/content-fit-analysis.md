# The Cake People — Content Fit Analysis

**Date:** 16 July 2026
**Question:** Can the written content (`Thecakepeople.au.docx`) drop into the existing live pages, or will it require changes?
**Method:** Fetched all 22 live URLs (DataForSEO content-parsing / WebFetch) and compared each against the matching block in the docx.

---

## Short answer

**Technically it fits — but it's a *replace*, not a *drop-in-alongside*, and several pages need work before the swap.**

1. **Field compatibility: yes.** Shopify product-description and collection-description fields are rich-text. Our copy (headings + paragraphs + FAQ written as plain body text) pastes straight in with **no theme/template change**. The FAQ is written as text, so it needs no accordion app (add one only if you want it styled).
2. **Every live page already has 250–450 words of its own SEO copy.** So "accommodating" the new content means **choosing replace vs merge per page** — not filling a blank. Only `/pages/custom-cakes` is nearly empty.
3. **The real work is 7 fixes below**, not formatting.

---

## The 7 things that need doing before/while loading

| # | Issue | Pages affected | Action |
|---|---|---|---|
| 1 | **Our copy drops product/safety specifics the live page carries** | sugar-free, cupcakes, McQueen, Minecraft, Bluey, logo-cupcakes | Port the specifics forward (see table) or the page regresses |
| 2 | **Two docx blocks merge two pages under one H1** | Peppa+Roblox; Sugar-free+Vegan | Split each into two, map 1:1 to the separate live URLs |
| 3 | **Messi product page is a 404** | /products/messi-football-goat-character-cake | Page must be **created/published**, not edited |
| 4 | **Vegan positioning conflict** | /collections/vegan-cakes | Live page *deliberately* de-emphasises "plant-based" (argues it wins mainstream categories); our copy leads hard with "100% plant-based" — client call |
| 5 | **Homepage is sectioned, not a description field** | thecakepeople.au | 918-word narrative can't drop in as-is; needs a section-placement decision or a new SEO text section |
| 6 | **8 long character-*collection* versions + 2 pages have no matching URL in the list** | see "Orphan content" | Confirm those collections/pages exist or should be created — else the content has no home |
| 7 | **FAQ styling** | all collections + most products | Fits as text now; add a theme accordion block only if desired |

---

## Per-page fit matrix (the 22 listed URLs)

### Product pages (9)
| URL | Live now | Our copy | Verdict |
|---|---|---|---|
| /products/peppa-pig-cake | MEDIUM ~250w, keeps "7-inch" | 326w + FAQ | ✅ Replace — retains size spec |
| /products/roblox-cake | MEDIUM ~230w | 414w, **folds existing intro in + adds the allergen note the live page was missing** | ✅ Best-case — superset |
| /products/kpop-demon-hunters-image-cake | MEDIUM ~230w, feature list | 365w + FAQ | ✅ Replace — comparable |
| /products/hot-wheels-cake | LONG ~300w, "Single Tall Layer" | 402w, has layer + serves | ✅ Replace — confirm layer wording carried |
| /products/lightning-mcqueen-cake | LONG ~380w, feature/benefit blocks, upgrade options | 351w, **no layer/size/serves spec** | ⚠️ Replace **but port cake specs + upgrade options first** |
| /products/minecraft-cake | LONG ~400w, "Standard Triple Layer" **+ 3D upgrade**, "Minecraft Movie" tie-in | 297w, **no layer / 3D / movie** | ⚠️ Replace **but port triple-layer + 3D-upgrade option** (revenue upsell) |
| /products/bluey-cake | MEDIUM ~230w, "Bluey **and Bingo**", 2 hard-coded testimonials, 7-inch | 454w, titled just "Bluey" | ⚠️ Replace **but keep "& Bingo" + decide on testimonials** |
| /products/custom-logo-cupcakes | LONG ~430w **incl its own 6-Q FAQ** + cross-sell | 720w + its own 6-Q FAQ | ⚠️ Replace **and dedupe the two FAQs; keep cross-sell link** |
| /products/messi-football-goat-character-cake | **404 — does not exist** | 382w ready | 🔴 **Create the page** |

### Collection pages (11)
| URL | Live now | Our copy | Verdict |
|---|---|---|---|
| /collections/signature-celebration-cakes | LONG ~430w | 932w + FAQ | ✅ Replace / upgrade |
| /collections/birthday-cakes | LONG ~380w (emoji labels) | 945w + FAQ | ✅ Replace / upgrade |
| /collections/kids-birthday-cakes | LONG ~350w | 757w + FAQ | ✅ Replace / upgrade |
| /collections/vintage-cake | LONG ~450w (cleanest, real H2s) | 742w + FAQ | ✅ Replace / upgrade |
| /collections/gluten-free | LONG ~250w | 855w + FAQ | ✅ Replace / upgrade |
| /collections/egg-free-dairy-free-cakes | LONG ~260w | 716w + FAQ | ✅ Replace / upgrade |
| /collections/edible-image-cake | LONG ~380w, 61 products | 813w + FAQ | ✅ Replace / upgrade |
| /collections/gender-reveal-cakes | LONG ~360w, **only 3 products** | 892w + FAQ | ⚠️ Replace — note copy far exceeds inventory (thin range) |
| /collections/sugar-free-cakes | LONG ~290w, **xylitol dog-toxicity safety warning + named products + exact medals** | merged w/ vegan, **none of those specifics** | 🔴 Split block **+ port the safety warning** (do not lose) + product names |
| /collections/vegan-cakes | LONG ~300w, "we don't lead with plant-based" positioning | merged into sugar-free block, leads with plant-based | 🔴 Split block **+ resolve positioning conflict** |
| /collections/cupcakes | LONG ~340w, **8 named flavour descriptions** (Triple Choc, Choc Mint, Fairy Floss, Biscoff, Caramel Latte, Vanilla Bliss, Choc Strawberry, Marshmallow) | 1015w + FAQ, **no flavour names** | ⚠️ Replace **but port the 8 flavour blurbs** |

### Page + Home (2)
| URL | Live now | Our copy | Verdict |
|---|---|---|---|
| /pages/custom-cakes | **SHORT ~55w only** | 771w + FAQ | ✅ **Easiest win** — near-empty page, content just fills it |
| thecakepeople.au (home) | MEDIUM, **sectioned** (reviews block, dietary grid, About block) | "Cakes Melbourne Loves" 918w single narrative | ⚠️ Can't drop into a sectioned homepage as-is — needs a section decision |

---

## Orphan content — written but no matching URL in the list

The docx also contains content whose declared target URL is **not** among the 22 pages:

- **8 long character *collection* versions** → `/collections/barbie-cakes`, `/bluey-cakes`, `/hot-wheels-cakes`, `/kpop-demon-hunters-cakes`, `/lightning-mcqueen-cakes`, `/messi-cakes`, `/minecraft-cakes`, `/peppa-pig-cakes`. The list only has character **products**, not collections. **Barbie has no product page at all.** → Confirm whether these collections exist / should be created, or this content is surplus.
- **`/pages/cake-delivery-melbourne`** (798w) — new page from the KWR plan; not in the list.
- **`/collections/gluten-free-cupcakes`** (1,468w, "vegan cupcakes melbourne") — not in the list.

## Data-hygiene notes in the docx (fix before hand-off to dev)
- Peppa block is mislabelled `kw: roblox cakes` and merges Peppa + Roblox collection copy.
- Sugar-free block is labelled `kw: vegan cakes melbourne` and merges sugar-free + vegan copy.
- Both need splitting so a developer can load one block per URL without untangling.

---

## Bottom line
No template or theme rebuild is required — the copy fits the fields. What it needs is **content reconciliation**: port ~6 pages' existing specifics forward, split 2 merged blocks, create the Messi page, make a call on the vegan positioning and the homepage placement, and confirm the orphan collection/page targets. Green-verdict pages (12 of 22) can be swapped as-is; the rest need the edits above first.
