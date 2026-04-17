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

## Link selection rules

**Anchor variety across pages**
When the same destination can be reached from multiple source pages, prefer the source page where the natural anchor text differs from anchors already chosen for that destination elsewhere in the plan. Avoid using the same anchor string (e.g. "Velux skylights") for the same target URL across multiple pages — it creates a templated footprint.

**Avoid parenthetical anchors**
Don't wrap text that sits inside parentheses or an aside. e.g. `Tubular skylights (or <a>sun tunnels</a>)` — the link sits inside a parenthetical, which reads awkwardly and reduces naturalness. Choose a different sentence on the same page where the target phrase appears in the main clause.

**Borderline anchors — leave unlinked**
If an anchor only works because the link was inserted (rather than because a reader would naturally expect to follow it), leave it unlinked. The connection must be obvious from the anchor text alone. "Leaks, drafts, and other issues" → repairs page is borderline; "skylight repair services" → repairs page is clear.

---

## Why

Established during centralskylights.com.au internal linking engagement (April 2026). Developer feedback drove the simplification: group by page so the dev can open one page, make all changes, close it — without hunting across multiple REQUEST blocks for the same page. Link selection rules added April 2026 following quality review of the same engagement.
