# Provenance — skyflex-bbq-pods

Entry: `skyflex-bbq-pods` | Mode: rewrite-existing (live page had zero body copy, so treated as build-from-scratch) | Generated: 2026-07-16

The exporter should render EXISTING spans on a yellow highlight (`background:#fff3b0`) and NEW spans plainly.

---

## EXISTING — verbatim facts carried over from the live page

These are the only load-bearing values reproduced unchanged from the current live product page (`https://skyflex.au/product/skyflex-bbq-pods/`, Playwright snapshot). Every one is a fixed fact, not a phrasing.

| Span in `generated.md` | Verbatim source on live page | Where used |
|---|---|---|
| `$13,500` (rendered "from $13,500") | live `price`: **"$13,500.00"** (Product schema `lowPrice: "13500.00"`) | Lede; "What you are buying" section |
| `2200w x 2300h x 770w` | live `variations[0]`: **"2200w x 2300h x 770w"** | "Two sizes" bullet 1 |
| `2850w x 2300h x 770w` | live `variations[1]`: **"2850w x 2300h x 770w"** | "Two sizes" bullet 2 |
| Product name "Skyflex BBQ Pods" | live H1: **"SKYFLEX BBQ PODS"** (recased) | H1, body |
| Phone `03 9498 0505` | client_data_signals `phone` (live page section "TALK TO OUR AUSTRALIAN TEAM") | CTA |
| Commercial basis: custom order, consultation required, not for direct online purchase | live short_description: **"Custom Order Product – Not available for direct online purchase / Consultation Required – Speak with our team for pricing, delivery, and customisation"** | Lede + "How a made-to-order pod comes together" + "What you are buying" |

**Note on the commercial-terms language:** the live page states the terms using en-dash punctuation ("Custom Order Product – Not available…"). Reproducing the dashes would violate the zero-dash rule, so the *facts* are carried over (custom order, consultation required, not sold for direct online purchase, pricing/delivery/customisation set by the team) but re-expressed in dash-free prose. The facts are EXISTING; the sentences are NEW phrasing of them.

## DEFECTS FIXED — live title/meta REPLACED, not carried over

These live values are copy-paste errors from another product (louvred pergolas). They are **NOT** existing-content-to-keep; they are being corrected, so they carry NO yellow highlight.

| Field | Live value (WRONG — defect) | New value (product-accurate) |
|---|---|---|
| `title` | **"Delta Motorised \| Skyflex"** | "BBQ Pods Melbourne \| Skyflex Outdoor Kitchen Pods" |
| `meta_description` | **"At SkyFlex, we supply a fantastic range of delta motorised louvred pergolas. Follow this link to learn more or contact us directly to learn more!"** | "A made-to-order BBQ pod outdoor kitchen for Melbourne. Configure the size and layout with the Skyflex team by consultation, then have it delivered." |

## NEW — newly written for this engagement

Essentially the entire page. The live page carried **no description tab and no attribute table** (only the "IMPORTANT INFORMATION" block), so all prose is new:

- The H1 and the full lede
- All five H2 sections and their body copy: "How a made-to-order BBQ pod comes together", "Two sizes to plan your space around", "What you are buying, and how these BBQ pods compare", "About Skyflex", "Book a BBQ pod consultation"
- The category price comparison ("$17,000 and $24,000") — grounded in research (competitor konoba "From $18,990.00" and the live AI Overview citing $16,999–$23,950), not invented, and stated at category level without naming competitors
- The "About Skyflex" credibility passage — the underlying facts (founder Christopher Mitsopoulos, established 2023, 100+ customers, 50% referral) are from `publishable_facts` / `client_data_signals`; the wording is new and differs from all three sibling pages

## Flags — could not ground, therefore omitted (not invented)

- **No materials / motorisation / IP rating / finish spec** exists in this product's research bundle (attribute_table empty; competitors' 304-steel / plug-and-play specs belong to competitors, not Skyflex). These were omitted rather than fabricated; the copy honestly frames finish and fit-out as decided during consultation.
- **No FAQ block** — the SERP returned zero PAA and Brave returned zero community questions. Per the locked plan's data-gated FAQ rule, no FAQ was written.
- **"Up to 8x cheaper"** appears as a section heading on the live page but reads as sitewide theme chrome and is a pergola-line USP; it was omitted to avoid an unsupported claim on this premium custom product (the plan permits but does not require it).
- **$15,500** (Product schema `highPrice`) was not asserted as a specific figure; the honest "from $13,500" plus "starting point, not a final quote" covers the larger variant without over-committing a number the visible price element does not show.
