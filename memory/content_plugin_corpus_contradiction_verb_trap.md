---
name: content-plugin-corpus-contradiction-verb-trap
description: "content plugin honesty gate false-positives on common verbs — keep \"we do not <verb>\" out of approved/hub copy"
metadata: 
  node_type: memory
  type: reference
  originSessionId: e224f522-a1de-49f4-b1f1-0dc9ce2fbea6
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

Discovered on twinkleclean.com.au (Twinkle Clean cleaning) carpet-location pilot, 2026-07-17.
