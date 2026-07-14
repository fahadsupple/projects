---
name: capability-supporting-keywords
description: "Finds supporting keywords per mapped page by extracting genuinely frequently-appearing wordings from live Google SERP data (organic titles/descriptions repeated 3+ times, PAA questions, related searches/people-also-search, popular products/shopping titles) for the page's primary keyword, then filtering ONLY for accuracy against the client's live product page. Does not invent content topics, does not exclude terms for being 'redundant' with existing page content, does not apply a separate abstract buying-intent-stage filter — real SERP frequency plus real accuracy is the whole test."
metadata:
  node_type: memory
  type: capability
  originSessionId: skyflex-supporting-keywords-2026-07-06
---

# Supporting Keywords Capability

**Trigger:** Once a keyword→URL mapping round is finalized (P/S roles locked), before handing off to copywriting/content brief. Also triggerable directly: "find supporting keywords for [page/keyword]."

**The test is exactly two steps — nothing more:**
1. **Is this wording genuinely frequent in the real SERP** for the page's primary keyword?
2. **Is this accurate** — does the client's actual product/page genuinely offer or match it?

That's it. Do not add a third filter layer based on reasoning about "redundancy with existing page copy" or "buying-intent journey stage" — both were tried and both caused real problems (see History below). If a term is genuinely frequent AND accurate, include it, even if a version of it already appears in the page's spec table — using the same vocabulary the whole category's SERP uses, in multiple places on the page (subheadings, body, FAQ, schema), has real semantic-SEO value beyond a single spec-table row.

---

## Process

**Step 1 — Identify the page's real target.**
Use the page's tracked Primary keyword. Pull SERP for Secondary keywords too if they represent a meaningfully different intent (different city, different product variant).

**Step 2 — Pull live SERP data** (`serp_organic_live_advanced`, depth 20, correct AU geo). Capture all of:
- Organic titles + meta descriptions
- People Also Ask questions
- Related Searches / People Also Search
- Popular Products / Shopping titles
- AI Overview text (see caution below)

**Step 3 — Extract genuinely frequent wordings. Be literal and mechanical about "frequent":**
- **Organic titles/descriptions/popular-products:** only count a term as frequent if it appears in **3 or more separate, distinct competitor listings** — not once, not "implied across a couple of them."
- **PAA questions:** each PAA question counts as a valid frequency signal on its own — Google surfaces PAA precisely because it aggregates real, common searcher questions. No need for a PAA question to repeat multiple times to qualify.
- **Related Searches / People Also Search:** same — each entry is itself an aggregate-frequency signal from Google, valid on its own.
- **AI Overview text — caution:** AI Overview often contains buying-consideration asides (e.g. "consider pairing with a soundbar," "check your power point location") that appear **once**, as a single aside, not as a repeated theme across multiple sources. Do not treat a single AI Overview aside as "frequent" — it isn't. Only pull an AI Overview point through if the same idea is corroborated by an actual PAA question, a related search, or repeated across 3+ organic titles/descriptions. This distinction is what separates genuinely useful items (a real PAA question) from noise (a single passing tip).

**Step 4 — Accuracy filter (the only other filter — mandatory, live-page check every time).**
For every candidate that survived Step 3, visit the actual live page (Playwright, not memory/prior notes) and confirm it against the real Specs/Description/trust-badges. Three outcomes:
- **Confirmed** — client's product genuinely has/matches this → keep
- **Wrong product** — this describes a different item in the client's own catalog (e.g. a louvre-blade roof term applied to a fabric-based retractable roof product, or an aluminium term applied to a product that's a different material) → drop
- **Not offered / unconfirmed** — client doesn't sell this variant, doesn't operate this way, or it can't be verified → drop, or flag "⚠ ask client to confirm" only if it's plausible and worth raising, don't guess

**Do NOT drop a term just because it already appears on the page.** That is not a valid reason for exclusion under this capability — see History.

**Step 5 — Deliver honestly, no fixed quota.** Comma-separated list per page. Count varies naturally by how much genuine SERP frequency + accurate confirmation exists — don't pad, don't force a round number.

**Step 6 — Self-review before delivering:**
- Every term is either a 3+-times-repeated organic wording, a real PAA question, or a real related-search/people-also-search entry — not an invented topic, not a single AI Overview aside stretched into a theme
- Every term passed the live-page accuracy check
- No cross-contamination between two different products in the client's own catalog
- No competitor brand names or competitor-specific retailer terms (e.g. "Bunnings," a named competitor product line) carried over as the client's own supporting keywords

**Step 7 — Promotion check (unchanged from prior versions, still run after Step 5 for every page).**
Shortlist candidates with plausible standalone search volume. Pull actual Google Ads volume — never promote off SERP-frequency alone. Promote to a tracked Secondary only when volume is meaningful relative to the page's existing Secondaries, the angle is genuinely distinct, it passed Steps 3–4, and it doesn't cannibalize another page. Specify the dedicated H2 and content angle. Present separately from the plain list, with volume data.

---

## History — why this is the final version, and what NOT to reintroduce

1. **v1** — SERP frequency only, no live-page check at all. Produced false claims (unconfirmed spec, a competitor's product wrongly attributed to the client, specs blended across two different client products). **Fixed by:** adding the live-page accuracy check (now Step 4).
2. **v2** — added accuracy check but no frequency discipline; basically just returned the page's own spec sheet restated. **This was actually fine to include as supporting keywords, in hindsight** — see point 4 below.
3. **v3** — introduced a "redundancy" filter (exclude anything already on the page) in response to v2 looking like a restated spec sheet. **This was a mistake.** Using category-standard vocabulary in multiple places on a page (not just once in a spec table) has real semantic value; "already stated once" is not a valid reason to exclude a term.
4. **v4** — introduced an additional "buying-intent journey stage" filter (reject installation/warranty/maintenance-type topics) layered on top of invented content-gap topics that were never actually verified as frequent SERP elements to begin with. Some rejections were right (e.g. "outdoor tv power point requirements," "pairing an outdoor soundbar" — correctly rejected) but for the wrong reason stated at the time ("wrong buying-intent stage"). The real reason they were wrong: **they were never genuinely frequent SERP signals in the first place** — they were single AI Overview asides that got creatively expanded into full "content gap" topics, not real PAA questions or repeated organic wordings. Once frequency is measured honestly (Step 3), these fail on frequency alone — no separate abstract intent-stage philosophy is needed.
5. **v5 (current)** — collapsed back to exactly two tests: genuine frequency (mechanically counted, PAA/related-searches count as valid on their own, single AI Overview asides do not) + accuracy (live-page check, no redundancy exclusion). This produces lists that mix real product-feature vocabulary (which is often also frequent in competitor SERPs) with genuine PAA-sourced angles (e.g. "can you put a regular tv outside," "does a pergola need council approval in melbourne" — both real PAA questions, both accurate, both worth including) — without inventing topics or rejecting accurate vocabulary for being "already known."

## Links
- [[capability_keyword_url_mapping]] — the mapping process this feeds into; reuses its "SERP Pattern Method" frequency threshold (3+ mentions) as the basis for Step 3
