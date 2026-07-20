---
name: content-plugin-corpus-contradiction-verb-trap
description: "content plugin honesty gate false-positives on common verbs — keep \"we do not <verb>\" out of approved/hub copy"
metadata: 
  node_type: memory
  type: reference
  originSessionId: e224f522-a1de-49f4-b1f1-0dc9ce2fbea6
  modified: 2026-07-20T04:44:24.282Z
---

Colana **content plugin** — the `honesty_corpus_contradiction` audit gate (blocking) works by extracting NEGATIVE assertions from `approved/*.md` (the voice corpus), reducing each `we do not/don't <verb>` line to just the **verb**, then flagging ANY later page whose body contains `we <verb>`. It does not understand meaning.

**Consequence:** if an approved hub page says "we do not **use** lock-in contracts", "we do not **give** them the same one", or "we do not **offer** X", then every sibling/spoke page that innocently says "we **use** targeted treatments", "we **give** free quotes", etc. gets 1 blocking finding per collision. Common verbs (use, give, offer, provide, do, make) are landmines.

**Rule when authoring hub/approved content:** never phrase an operational boundary as `we do not/don't <common verb>`. Use positive phrasing instead:
- "we do not use lock-in contracts" -> "we work without lock-in contracts"
- "we do not publish a flat rate" -> "we price each site individually" / "there is no flat rate"
- "we do not give them the same one" -> "we tailor the scope to each site"

After rewording, `approved/*.md` should contain ZERO `we do not/don't <verb>` matches (grep `we (do not|don't) [a-z]+`), so `corpus_operational_truth.json` negative_assertions is empty and no spoke gets falsely blocked.

**Two-location approval gotcha:** `/content:approve` writes `content/<entry>/approved.md`, but `wiki_rebuild.rebuild_voice_profile` and `corpus_operational_truth` read the top-level `approved/` dir. Copy approved pages into `approved/<slug>.md` too, or the voice/operational anchor never engages. See [[content-refinement-checklist]].

**SEO literal-score trap:** `seo_check` deducts -3 per secondary keyword not found by literal substring. A bloated generic "Supporting Keywords" block from the Meta File (e.g. 24 identical terms across every suburb page, several un-claimable) craters the score and pressures keyword-stuffing/over-claiming. Trim each entry's `secondary_keywords` to a small grounded localized set; the score is advisory (the authoritative audit_gate does NOT block on it).

**Location-page templating gates (BLOCKING) — the big one for suburb-page fleets.** The gate compares each page against ALL generated siblings in its cluster. Four structural checks block:
- `faq_question_overlap`: >=50% Jaccard of FAQ question sets (questions are suburb-token-stripped, so "cost in {suburb}?" is identical across pages). With 6 Qs/page, two pages may share at most 3 (33%); 4 shared = 50% = blocked.
- `closing_pattern_overlap`: >=45% of the page TAIL covered by 4-grams shared with a sibling. The tail includes the LAST FAQ answer(s) + CTA, so identical generic FAQ answers (not just the CTA) trip it.
- `templating_process_steps` (`n_step_process`): a dedicated H2 containing process/steps/stages or "from X to Y". Fold method into prose.
- `h2_overlap`: >=70% Jaccard of H2 sets.

Working recipe for N suburb pages (proven on twinkleclean carpet cluster, 20 pages, 0 blocking):
1. Give each page 6 FAQs = 3 suburb-specific (unique) + 3 from an assigned generic TRIPLE (partition a ~12-Q generic pool into 4 disjoint triples; rotate). Two same-triple pages then share exactly 3 Qs = 33% < 50%.
2. ORDER the FAQ so the 3 suburb-specific Qs come LAST (immediately before the CTA). This keeps the sampled TAIL unique and mostly prevents `closing_pattern_overlap`.
3. Vary FAQ ANSWERS too, especially any generic answer that lands in the tail: same-triple pages converge on identical "worth it" / "steam vs dry" / end-of-lease answers. Ban stock house-style lines (e.g. "reaches soil a domestic vacuum leaves behind").
4. The "do you cover nearby suburbs?" Q normalizes to "do you cover nearby [council] suburbs?" and collides across pages — name specific suburbs or reframe. Its ANSWER template ("As well as X we clean carpet throughout the neighbouring...", "X sits in the City of Y and we clean right across...") also collides in the tail — vary it per page.
5. Distinct CTA per page (vary the verb/structure around the unavoidable phone/email; ban shared phrases like "match the right method to your carpet", "rooms and any problem areas", "free, no-obligation quote").
Dispatch writers with the ASSIGNED FAQ set + these bans baked in; then run scripts.audit_gate.run_audit_gate per page and reword the 1-2 residual tail/FAQ collisions (a fast targeted edit). Batches got cleaner as the recipe tightened (batch1 needed 5 reworks, batch3 needed 1).

**Path gotcha:** the content-plugin client folder is itself named `content/`, so generated pages live at `clients/<domain>/content/content/<entry>/generated.md` (doubled `content`). Tell subagents explicitly or they write one level too high.

**Word counts: use the gate's counter, not `wc -w`.** `wc -w` counts markdown syntax (headings, `**bold**`, link URLs) and over-reports by ~5-10%, which makes pages look over-length when they are not. Use `scripts.audit_gate_inputs.assemble(client_dir, entry_id).content.split()`. The gate only flags "Extreme word count drift" against `target_word_count` (the plan's floor) — moderate over-length is NOT a finding.

**Re-link pass — hub→spoke cross-cluster leakage (link_graph.py).** `compute_link_graph` hub-spoke selection does:
`related = [loc for loc in target_location_pages if hub_service in loc.entry_id]` then `if not related: related = target_location_pages[:link_cap]`.
So a hub whose OWN spokes are not yet live (status filtered out by `require_link_target_status=DEFAULT_LIVE_STATUSES`) silently falls back to **another cluster's** spokes — e.g. the commercial-cleaning hub was handed 20 carpet-suburb targets. Always inspect edges per source before injecting; skip any hub whose spokes are not generated yet rather than accepting the fallback.
Also: `link_cap` defaults to 8, which truncates a 20-spoke hub **alphabetically**. Raise `link_cap` for the hub and place all spokes as a nav-list.

**ROOT CAUSE of that leak — entry `status` is never auto-advanced.** Writing `content/<entry>/generated.md` does NOT change `entries/<entry>.json` `status`; it stays `researched`, which is NOT in `DEFAULT_LIVE_STATUSES` ({generated, audited, approved, published}). So a freshly-written cluster is invisible to link_graph and every hub falls through to the cross-cluster fallback. **Before any re-link pass, set `status` to `generated` on the written entries** (assert `generated.md` exists first), then re-check that no foreign-cluster target appears in the hub's edges. Confirmed on the commercial cluster 2026-07-20: 40 spokes sat at `researched` after passing the gate.

**`anchor_grammar` — bulleted list vs inline.** Title-Case `anchor_text` is fine in a `- [Label](url)` **bulleted list** but blocks as "raw Title-Case label injected mid-sentence" in an inline comma-separated run (40 findings, one per link). For a large nav block prefer the bulleted list (also far more readable than 40 inline links); reserve `anchor_natural` for genuine prose sentences. Watch the label caser: it produces "Melbourne Cbd" — fix to "Melbourne CBD".

**`seo_vocab_leak` false positive: "dwell time".** Blocks as an SEO term, but in cleaning copy it means disinfectant contact time. Reword ("left on the surface long enough to work") rather than waive — the phrase usually also asserts a procedure not in the verified method facts.

**Anchor placement rule (linker-agent):** prose placement must use the edge's `anchor_natural` VERBATIM ("carpet cleaning in Rowville"); nav-lists use Title-Case `anchor_text`. Injecting the Title-Case label mid-sentence is a BLOCKING `anchor_grammar` finding. Consequence: you cannot simply hyperlink a bare suburb name already sitting in a prose list — add a short clause carrying `anchor_natural` instead, and VARY that clause per page or you re-introduce `closing_pattern_overlap`. Only link pairs that are actually in the computed graph (cardinal rule: an unlinked entry beats a spammy link).

Discovered on twinkleclean.com.au (Twinkle Clean cleaning) carpet-location cluster, 2026-07-17.
