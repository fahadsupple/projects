# Research agent — top-level-pages cluster (content:research)

You are gathering SERP + PAA ground-truth for ONE page keyword for Robot Cleaning Solutions (Melbourne Bayside / SE house cleaning). Output must exactly mirror the existing bundle schema so the planner and writer can consume it.

## Fixed context
- Working directory (all paths resolve here): `/home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content`
- Location for DataForSEO/Brave: Melbourne, Victoria, Australia. `location_code` 21167 (Melbourne, Victoria) or `location_name` "Melbourne,Victoria,Australia"; `language_code` "en".
- You have DataForSEO + Brave MCP tools available via ToolSearch. Load schemas with `ToolSearch("select:<tool_name>")` before calling.

## Your assigned keyword
- ENTRY_ID: `<ENTRY_ID>`
- PRIMARY_KEYWORD: `<PRIMARY_KEYWORD>`

## Steps
1. **SERP** — `serp_organic_live_advanced` for the primary keyword, Melbourne VIC. Capture the top 10 organic results (title, url, description, rank), any AI overview, PAA questions, and related searches present in the SERP payload. Write the raw response to `clusters/top-level-pages/research/raw/serp-<ENTRY_ID>.json`.
2. **Keyword data** — `dataforseo_labs_google_keyword_overview` (or `kw_data_google_ads_search_volume`) for volume/intent; `dataforseo_labs_google_related_keywords` and `dataforseo_labs_google_keyword_suggestions` for expansion. `dataforseo_labs_search_intent` for intent + probability. Save each raw response to `clusters/top-level-pages/research/raw/<endpoint>-<ENTRY_ID>.json`.
3. **PAA / related** — if the SERP payload did not include PAA, run a Brave web search for the keyword and capture the "People also ask"/related angle. Collect 4–8 real PAA questions searchers ask for this keyword.
4. **Competitor pages** — from the top organic results, note the 3–5 most relevant Melbourne house-cleaning competitor pages and one-line what each does well (structure, trust signals, content gaps we can beat).
5. **On-page (optional, cheap)** — you MAY `on_page_content_parsing` the top 1–2 competitor URLs to extract their heading structure for gap analysis. Skip if it errors.

## Write the synthesized bundle
Write `clusters/top-level-pages/research/keyword-<ENTRY_ID>.json` with EXACTLY these top-level keys (mirror the existing bundle schema):
```
{
  "keyword": "<PRIMARY_KEYWORD>",
  "search_volume": <int or null>,
  "intent": "<informational|commercial|transactional|navigational>",
  "intent_probability": <float or null>,
  "serp_results": [ {"rank":1,"title":"...","url":"...","description":"..."}, ... up to 10 ],
  "paa_questions": [ {"question":"..."}, ... 4-8 real questions ],
  "related_searches": [ "...", ... ],
  "keyword_suggestions": [ "...", ... ],
  "related_keywords": [ "...", ... ],
  "competitor_pages": [ {"url":"...","wins_on":"..."}, ... ],
  "ai_overview": "<text or null>",
  "synthesis": {
    "content_gaps": [ "...", ... ],
    "recommended_outline": [ "H2: ...", "H2: ...", ... ],
    "competitor_takeaways": [ "...", ... ],
    "paa_to_answer": [ "...", ... 4-8 ],
    "differentiation_angles": [ "...", ... ]
  }
}
```

## Rules
- Use ONLY real API data. If a call returns nothing, record null / empty array — never invent SERP results, volumes, or PAA.
- Do NOT write any page content. Research only.
- Keep the raw fixtures — they are the provenance.

## Return (short text only)
Report: entry_id, primary keyword, search volume, intent, number of SERP results captured, number of PAA questions captured, and the single sharpest differentiation angle you found. Do NOT paste the full bundle.
