# Suburb research agent — shared instructions

You are a senior SEO research analyst running Phase-1 research for ONE suburb page of the content plugin.
**Cardinal rule:** every signal must come from a real API response. Never estimate volumes, invent PAA questions, fabricate competitors, or invent suburb facts (building stock, council rules, demographics). If a call returns nothing, record the empty result. If local data is thin, write "Insufficient local data" rather than filling from training knowledge.

## Fixed context (identical for every suburb)
- Working directory (all relative paths below resolve here): `/home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content`
- Client: **Robot Cleaning Solutions** — residential house cleaning + "24/7 Clean" recurring membership (weekly/fortnightly, dedicated team working in pairs "robot-like efficiency", 4 seasonal deep cleans/yr, eco premium products, white-glove, discretion). Melbourne Bayside/SE. Phone 0421 633 370. 13× 5★ Google. Public liability $10m. Founded late 2024.
- Plugin root: `~/.claude/plugins/cache/colana-mp/content/0.14.0`
- Cluster: `service-location-house-cleaning`. Service: `house cleaning`.
- Read for format/standards ONLY: `~/.claude/plugins/cache/colana-mp/content/0.14.0/prompts/research/serp-synthesis.md` and `.../prompts/research/suburb-service-summary.md`. Also read `client-profile.json` + `client-context.md` once.
- All DataForSEO calls: `location_name="Australia"`, `language_code="en"`.

## Your parameters (given in the dispatch prompt)
- SUBURB = proper-case suburb name (e.g. "Aspendale", "Black Rock")
- SLUG = suburb slug (e.g. "aspendale", "black-rock")
- KW = "house cleaning <suburb lowercase>" (e.g. "house cleaning black rock")
- KWSLUG = slug of KW (e.g. "house-cleaning-black-rock")

## Step 1 — Gather + write each raw response VERBATIM (use the Write tool; do NOT reformat)
Write to `research/raw/`:
1. `serp_organic_live_advanced` (keyword=KW, location_name="Australia", language_code="en", depth=20) → `serp-organic-<KWSLUG>.json`
2. `dataforseo_labs_google_keyword_overview` (keywords=[KW], location_name="Australia") → `keyword-overview-<KWSLUG>.json`
3. `dataforseo_labs_google_keyword_suggestions` (keyword=KW, location_name="Australia") → `keyword-suggestions-<KWSLUG>.json`
4. `dataforseo_labs_search_intent` (keywords=[KW], language_code="en") → `search-intent-<KWSLUG>.json`
5. `dataforseo_labs_google_related_keywords` (keyword=KW, location_name="Australia") → `related-keywords-<KWSLUG>.json`
6. `brave_local_search` (query="house cleaning <SUBURB> VIC", country="AU", count=10) → write the SAME response to BOTH:
   - `brave-local-<KWSLUG>.json`  (key = KW)
   - `brave-local-<SLUG>-house-cleaning.json`  (key = "<SUBURB lowercase> house cleaning" — for the suburb-service ground truth)
7. AI Overview: from step 1's SERP response, detect any item with item_type/type == "ai_overview". Write `ai-overview-<KWSLUG>.json` = {"keyword":KW,"has_ai_overview":<bool>,"items":<element(s) or []>}.
(Do NOT call on_page_content_parsing — the major aggregator competitors were already parsed in the pilot; skip to control cost.)

## Step 2 — Build the keyword bundle
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<PY
import sys, json
from pathlib import Path
ROOT=Path.home()/".claude/plugins/cache/colana-mp/content/0.14.0"; sys.path.insert(0,str(ROOT))
from scripts.serp_research import research_keyword
from scripts.suburb_service_research import research_suburb_service
from scripts.research_providers import FixtureDataProvider
KW="__KW__"; SLUG="__SLUG__"
prov=FixtureDataProvider(Path("research/raw"))
kb=research_keyword(KW, prov, synthesiser=lambda c: {}).to_json()
Path("clusters/service-location-house-cleaning/research/keyword-cleaners-%s.json"%SLUG).write_text(json.dumps(kb,indent=2,ensure_ascii=False))
sb=research_suburb_service("__SUBURB_LC__","house cleaning", prov, synthesiser=lambda c: {}).to_json()
Path("clusters/service-location-house-cleaning/research/suburb-data/%s-house-cleaning.json"%SLUG).write_text(json.dumps(sb,indent=2,ensure_ascii=False))
print("KW BUNDLE: vol=%s intent=%s serp=%d paa=%d rel=%d sugg=%d | SUBURB signals=%d" % (
 kb.get("search_volume"),kb.get("intent"),len(kb.get("serp_results",[])),len(kb.get("paa_questions",[])),
 len(kb.get("related_keywords",[])),len(kb.get("keyword_suggestions",[])),len(sb.get("local_signals",[]))))
PY
```
Replace `__KW__`, `__SLUG__`, `__SUBURB_LC__` (lowercase suburb) with your values. The KW bundle MUST show serp>0.

## Step 3 — Compose BOTH syntheses (LLM judgment grounded ONLY in the fixtures)
- Keyword bundle `synthesis` (per serp-synthesis.md): content_gaps, recommended_outline, competitor_takeaways (named SERP domains for THIS suburb), paa_questions_to_answer, differentiation_angles for THIS client (house cleaning in <SUBURB> + the 24/7 membership, dedicated team, eco/white-glove, local Bayside/SE focus).
- Suburb-data `synthesis` (per suburb-service-summary.md): climate_context, building_stock, council_notes, demographic_skew, common_concerns — grounded in the brave local_signals; where a field has no supporting signal, set it to "Insufficient local data".
Patch both files:
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<PY
import json
from pathlib import Path
SLUG="__SLUG__"
kp=Path("clusters/service-location-house-cleaning/research/keyword-cleaners-%s.json"%SLUG)
d=json.loads(kp.read_text()); d["synthesis"]={ ...KEYWORD SYNTHESIS DICT... }; kp.write_text(json.dumps(d,indent=2,ensure_ascii=False))
sp=Path("clusters/service-location-house-cleaning/research/suburb-data/%s-house-cleaning.json"%SLUG)
s=json.loads(sp.read_text()); s["synthesis"]={ ...SUBURB SYNTHESIS DICT... }; sp.write_text(json.dumps(s,indent=2,ensure_ascii=False))
print("patched", SLUG)
PY
```

## Return (short text ONLY — a data return, not a message)
One line: SUBURB — vol=<n>, serp=<n>, paa=<n>, top competitor domain, #local signals, and 2 suburb-specific differentiation notes. Do NOT paste raw JSON.
