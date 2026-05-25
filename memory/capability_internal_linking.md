---
name: internal-linking capability
description: Internal linking process — workflow, link selection rules, and developer handoff format standards
type: feedback
---

# Capability: internal-linking

**When triggered:** Any client engagement requiring contextual internal links to be added or improved.

**Full instructions:** `seo/tools/internal-linking/project-instructions.txt`

**Deliverables:** Always two files, both at `seo/clients/[domain]/internal-linking/`:
- `[domain].txt` — source of truth, plain text
- `[domain].html` — same content, rendered for sharing with developers

---

## Developer handoff format (confirmed standard — apply every time)

**Group by source page — not by keyword or batch.**

Every page that needs edits gets one block. All Find/Replace pairs for that page are listed together under its URL. Separate page blocks with `---`.

```
Page: https://example.com/some-page/

Find:
{exact paragraph text}
Replace With:
{paragraph with <a> tag inserted}

Find:
{next paragraph on the same page}
Replace With:
{modified version}

---

Page: https://example.com/another-page/
...
```

**What to exclude from the handoff (dev does not need this):**
- No REQUEST headers, no batch labels, no dates
- No notes or explanations after Replace With blocks
- No audit findings, no summaries, no anchor type metadata
- No header section at the top of the file

**Bold tag rule:** If the Find text contains bold in the original, retain `<strong>` tags in Replace With.

**Location page templates:** Only use `[TEMPLATE — apply to ALL /slug-[suburb]/ pages]` if the client actively prioritises those pages. Otherwise scope to the specific URL only.

---

## HTML file rules

- Monospace font, `white-space: pre-wrap`, no colour coding, no badges, no design elements
- All HTML tags in Replace With blocks must be entity-escaped: `<` → `&lt;`  `>` → `&gt;`
- Start directly with the first `Page:` block — no intro copy
- Serve on localhost with `python3 -m http.server 8080` when user wants to review

---

---

## GEO-RELEVANCE — CRITICAL

**Never introduce a city name into body content of a page focused on a different city.** If the source page body text is focused on Melbourne, do not append or insert sentences that mention Brisbane, Sydney, or any other city. If the target link is a city-specific page (e.g., /areas-we-serve/brisbane/bollards/), the source page must already contain copy mentioning that city or national coverage — do not create cross-city mentions by adding new sentences. If no geographically appropriate paragraph exists on that page, find a different source page.

**When writing surrounding sentences for links, match the geographic scope of the paragraph being edited.** If the paragraph mentions "Melbourne", the surrounding sentence should reference Melbourne or Victoria, not Sydney, Brisbane, or other markets. If the linked page is a general service page that covers multiple cities, write the surrounding sentence to reference the source page's city only (e.g., "available across Melbourne and Victoria" not "across Sydney and Melbourne" on a Melbourne page).

**What to look for when selecting a paragraph for a city-specific target link:**
- The paragraph already mentions that city by name, OR
- The paragraph describes national/Australia-wide coverage, OR
- The paragraph is topically generic without any geographic lock-in

**If no suitable paragraph exists on the source page:** Remove the link from the plan. Check whether the target URL is already reached from another valid source page in the plan — if it is, no replacement is needed. If it is not, find a geographically appropriate source page (same city or state as the target) and use a paragraph on that page instead. Only proceed if you have fetched and read the alternative source page.

**City → State generalisations that are always safe:**
- Melbourne source page → "across Melbourne and Victoria" or "across Victoria"
- Sydney source page → "across Sydney and NSW"
- Brisbane/Gold Coast source page → "across Queensland" or "throughout South East Queensland"

---

---

## Anchor text — city placement rule

**Never include a city name inside the anchor text when it is appended as a suffix to a service description.** Anchors like "deceased estate lawyers in Melbourne" or "commercial lawyers in Melbourne" look over-optimised and unnatural.

**Instead, place the city contextually in the surrounding sentence — outside the anchor.**

The anchor covers the service or topic. The geo-context comes from the sentence around it.

**Examples:**

| ❌ City inside anchor | ✅ City in surrounding sentence |
|---|---|
| `contact our <a>deceased estate lawyers in Melbourne</a> today` | `a Deceased Estate in Melbourne, contact our <a>deceased estate lawyers</a> today` |
| `our <a>estate planning lawyers in Melbourne</a> can help` | `a business owner in Melbourne, our <a>estate planning lawyers</a> can help` |
| `give our <a>commercial lawyer Melbourne</a> team a call` | `new venture in Melbourne, give our <a>commercial lawyer</a> team a call` |
| `our <a>commercial lawyers in Melbourne</a> prepare` | `our <a>commercial lawyers</a> in Melbourne prepare` |

**Exceptions — these are fine:**
- Anchor IS the city name: `<a href="/property-lawyer-melbourne">Melbourne</a> and Casey` — natural geographic reference
- Anchor is suburb-specific from a hub page: `<a>commercial law services for Berwick</a>` — the suburb is the distinguishing element
- Anchor contains city as part of a natural phrase: `<a>Melbourne-wide commercial matters</a>` — not a service+city suffix pattern

---

## Copy quality — writing rules

These rules exist because AI tools naturally prioritise keyword fitting over natural English. Every Replace With block must pass all four checks before it is final.

**1. Grammar first — no clunky adjective phrases**
The surrounding sentence must remain grammatically flawless after the link is inserted. Never invert natural English word order just to cram a keyword string in.
- ❌ `"give our commercial lawyer team a call"` — nobody says this
- ✅ `"give our team of commercial lawyers a call"`
- ❌ `"contact our deceased estate lawyer staff today"`
- ✅ `"contact our deceased estate lawyers today"`

**2. Retain brand adjectives and the company name**
Do not delete positive brand words ("friendly", "experienced") or the actual company name just to make a link fit. Blend the anchor into the existing brand voice — never overwrite it.
- ❌ Original: `"contact our experienced and friendly staff today"` → AI deleted "and friendly staff" to force the anchor → wrong
- ✅ Correct: `"contact our experienced and friendly deceased estate lawyers today"`
- ❌ Original: `"When you have Wollerman Shacklock prepare..."` → AI stripped the firm name and wrote `"When you have our commercial lawyers in Melbourne prepare..."` → wrong
- ✅ Correct: `"When you have the commercial lawyers at Wollerman Shacklock prepare..."`

**3. Fix adjacent typos while rewriting**
If the sentence being modified contains a pre-existing grammar error or typo, fix it as part of the rewrite. Do not leave errors sitting next to newly inserted copy.
- ❌ Left in place: `"We assist in all aspect of Estate Planning"` (existing typo untouched)
- ✅ Fixed during edit: `"We assist in all aspects of Estate Planning"`

**4. Read it aloud — it must sound like human writing**
Read the completed Replace With block aloud. If it sounds like it was assembled by an SEO tool rather than written by a copywriter, rewrite it. The test: would the site's author be comfortable if this sentence appeared under their name?

*Source: wslegal.com.au internal linking review, May 2026.*

---

## Link selection rules

**Scan the full REPLACE block for secondary linking opportunities**
When writing a REPLACE block for a primary link, scan the entire replacement text for any other mentions that have a corresponding target page and would be logical for a reader to follow. If the link passes the borderline test (connection is obvious from anchor text alone), add it to the same REPLACE block.

Do not treat each REPLACE block as a single-link operation. One paragraph can carry multiple links if the content supports it naturally. Examples of what to look for:
- A suburb list where some names have dedicated location pages (e.g. "including Berwick, Narre Warren, Pakenham" when /property-lawyer-berwick etc. exist -> link each)
- A service mentioned in passing that has its own page (e.g. "commercial lease agreements" on a commercial lawyer page -> link to /commercial-lease-lawyer-melbourne)
- A related practice area referenced in a sentence being modified (e.g. "probate" on a wills page -> link to /probate-lawyer-melbourne)

**Do not link:** names with no corresponding target page, the page itself (no self-links), or anything that fails the borderline test.

**Anchor variety across pages**
When the same destination can be reached from multiple source pages, prefer the source page where the natural anchor text differs from anchors already chosen for that destination elsewhere in the plan. Avoid using the same anchor string (e.g. "Velux skylights") for the same target URL across multiple pages — it creates a templated footprint.

**Avoid parenthetical anchors**
Don't wrap text that sits inside parentheses or an aside. e.g. `Tubular skylights (or <a>sun tunnels</a>)` — the link sits inside a parenthetical, which reads awkwardly and reduces naturalness. Choose a different sentence on the same page where the target phrase appears in the main clause.

**Borderline anchors — leave unlinked**
If an anchor only works because the link was inserted (rather than because a reader would naturally expect to follow it), leave it unlinked. The connection must be obvious from the anchor text alone. "Leaks, drafts, and other issues" → repairs page is borderline; "skylight repair services" → repairs page is clear.

---

## Why

Established during centralskylights.com.au internal linking engagement (April 2026). Developer feedback drove the simplification: group by page so the dev can open one page, make all changes, close it — without hunting across multiple REQUEST blocks for the same page. Link selection rules added April 2026 following quality review of the same engagement. Copy quality rules added May 2026 following wslegal.com.au review.
