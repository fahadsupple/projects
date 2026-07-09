---
name: daily-task-capability
description: "Daily Task doc — dev handoff process for URL restructures, new page creation, and template mapping from a Meta Data keyword/URL sheet"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d1aa026f-21f7-48b3-a394-c06abc4f1006
---

# Capability: daily-task

**When triggered:** Client has a keyword/URL meta spreadsheet (new pages to build, existing pages to rename) and needs a developer-facing "Daily Tasks" document — the structural/technical handoff, not the page copy itself.

**Reference sample:** `clients/acsdebtcollection.com.au/Acsdebtcollection - Daily Tasks.docx` — read this first every time; it defines the tone and instruction style (plain, imperative, one action per line).

**Deliverables:** Always saved to `clients/[domain]/daily-task/`:
- `[Domain].com.au - Daily Tasks.docx` — the dev handoff doc
- `screenshot-*-annotated.png` — every annotated screenshot embedded in the doc, kept as standalone files too

---

## Step 1 — Read the source spreadsheet correctly

- **Only read the sheet literally named "Meta Data".** Ignore every other sheet in the workbook (e.g. "Keywords", "Meta Data for Hardy").
- **Always ignore any sheet with "Hardy" in its name**, regardless of client — this is a standing rule, not client-specific.
- Read cell **fill colour**, not just cell value. `openpyxl` with `data_only=True`, then check `cell.fill.patternType == 'solid'` and `cell.fill.fgColor.rgb`.
  - **Yellow fill (`FFFFFF00`) = new page to be created.** Build it from a template.
  - **No fill on a URL row = the page already exists.** No new page needed — either it's a straight content/meta update in place, or (if a "Current URL: https://..." note appears directly below/near it) it needs a rename + 301.
- **A redirect is only in scope if the sheet explicitly says so** via a "Current URL: https://..." line. Do not infer or invent a redirect just because a similar-looking page already exists elsewhere on the site — even if that other page is a better content match. If the sheet doesn't say to redirect it, leave it alone and flag the mismatch instead of deciding unilaterally (see Step 3).

## Step 2 — Cross-check the live site before writing any instruction

For every URL in the sheet, check live HTTP status (`curl -s -o /dev/null -w "%{http_code}"`) before writing the daily task line:
- 200 + not yellow + no "Current URL" note → existing page, content-update-only.
- 200 + "Current URL" note pointing elsewhere → this IS the rename source; the sheet's target URL is the destination.
- 404 + yellow → straightforward new page.
- 404 + NOT yellow + no redirect note → **inconsistency in the sheet — flag it explicitly in the doc, don't silently resolve it** (see naztech.com.au example: `/mobile-auto-electrician/` was 404 but unmarked; flagged rather than assumed).

Also pull the site's full page inventory (`/sitemap_index.xml` → `/page-sitemap.xml` or equivalent) to see the *complete* current page list — the Meta Data sheet only shows target URLs, not what else already exists that might overlap or compete with the new pages.

## Step 3 — Template selection: compare content richness, don't assume

When multiple existing pages could plausibly serve as the template/redirect source for a new target URL, **actually fetch and compare their content** (word count, H2/H3 depth, FAQ/reviews sections present) — don't default to whichever one has the most literally-matching slug. Thin, generic pages and rich, well-built pages can both exist for overlapping topics on the same site.

**If the richer content match and the sheet's literal instruction disagree, stop and ask the client/analyst — do not pick one silently.** This happened on naztech.com.au: the sheet said rename `/cars/` → `/car-aircon-regas/`, but `/mobile-air-conditioning-repairs-servicing/` was a far richer content match for that same target keyword. Surfaced as an explicit question rather than assumed either way.

## Step 4 — Screenshot annotation style

Match the visual style of the client-provided example screenshots exactly (red rectangle outline around the section that changes + a solid red label box with bold white text explaining the instruction, positioned above/beside the section — not overlapping it).

Process:
1. Playwright full-page screenshot at 1440×900 desktop viewport.
2. Get exact bounding boxes of the elements to annotate via `page.evaluate` (`getBoundingClientRect()` + `window.scrollY` for full-page coordinates).
3. Annotate with PIL (`ImageDraw.rectangle` for the red outline, a solid-red label box with wrapped white `DejaVuSans-Bold` text near it — see working helper function pattern used for naztech.com.au, don't rebuild from scratch each time).
4. Embed the finished PNG directly in the docx at ~6.5 inch width (`document.add_picture(path, width=Inches(6.5))`).

Only screenshot pages that need visual/layout instructions (usually the homepage and the template page). Pure URL/redirect/nav/footer instructions stay as plain text lines, matching the ACS sample's pattern — don't screenshot everything.

## Step 5 — Daily Task doc structure (standard section order)

1. **Rename existing pages + add 301 redirects** — only the rows with explicit "Current URL" notes.
2. **Create new location/suburb pages** — grouped by silo, "Using [X] as a template, create these new pages" phrasing (verbatim pattern from the ACS sample). If a whole silo has zero existing pages to use as a template, say so explicitly and instruct that the first suburb page built in that silo becomes the template for the rest.
3. **Create new general/root pages** — one per silo. If a rich existing page can't be used as a redirect source (per Step 3 decision) but is a good structural/depth reference, say so explicitly and separate "content depth reference" from "redirect source" as two different things — they are not interchangeable.
4. **Content updates on existing pages (no URL change)** — homepage and any other page that's already at its target URL.
5. **Hub/"near me" page rebuild** — if a sheet row is yellow despite the URL already existing (e.g. `/areas-we-serve/`), treat it as a substantial rebuild, not a small edit, and specify it becomes the internal-linking hub to all the new silo pages.
6. **Screenshots** — embedded, per Step 4.
7. **Navigation changes** — itemised, one bullet per action (rename/remove/add), matching ACS sample phrasing style exactly ("Rename X to Y", "Add X as the first item in the dropdown under Y", "Add a second-level dropdown with...").
8. **Footer changes** — itemised the same way.
9. **Open items** — every flagged inconsistency from Steps 1–3, plus a note that meta titles/H1s/descriptions are a separate content deliverable if the sheet's content columns are blank. Never fabricate placeholder copy to fill gaps — state plainly that it's pending.

## Never do this

- Never invent H1/meta title/description copy that isn't in the source sheet, even to make the doc feel "complete." State it's pending as a separate content deliverable.
- Never resolve a sheet inconsistency (ambiguous highlighting, conflicting redirect logic) by picking the option that seems most sensible — ask, or flag it explicitly in the Open Items section.
- Never assume suburb/location lists match earlier keyword research memory without checking — cross-reference and flag discrepancies (e.g. naztech.com.au's Meta Data sheet had 14 suburbs and "Clyde"; the earlier finalised KWR memory had 15 suburbs including Mooroolbark and "Clyde North" — flagged, not silently reconciled).

*Source: naztech.com.au daily task build, 9 Jul 2026 — first use of this capability, modelled on the acsdebtcollection.com.au sample doc the client provided.*


## Template selection can change mid-project — re-check imagery/copy balance every time

The client can override the default "use the most-populated existing page as template" logic at any point (e.g. naztech.com.au: switched from the Pakenham suburb page to the full homepage as the template for all new location pages, after the doc was already built once). When this happens:
- Rebuild every "using X as the template" reference in the doc, including the rename note for any existing page that used the old template (its content now needs rebuilding to the new template too, not just its URL).
- **Before finalising, screenshot and check the new template page for business-segment/imagery bias** — if the client serves multiple distinct customer/vehicle/product types, verify the template represents all of them neutrally. Check: hero image/copy, any brand/logo grids (are they empty/broken?), equipment or product list sections (does every service line get a column/tile, or do 1-2 dominate?), and section headings (do they use exclusionary language like "commercial operators" when the business also serves other customer types?).
- If the template is heavily biased toward one segment and will be replicated across many new pages (suburb pages, location pages), that bias multiplies across the whole site. Flag it as its own numbered section in the doc with annotated screenshots per biased element (hero, logo grid, list columns, tile grid), not folded into the general template instructions.
- Add an explicit warning against literally duplicating a long/rich template's every section on every new page — trim per-page content to what's realistic for that page's narrower scope (e.g. a single-service suburb page doesn't need the full multi-sector equipment list the homepage has), while keeping the same visual structure/section pattern.

*Source: naztech.com.au, 9 Jul 2026 — client switched the location-page template from Pakenham to the homepage mid-build, which surfaced that the homepage itself was heavily industrial/commercial-skewed (empty brand logo grid, zero light-automotive equipment column, "Trusted by Commercial Operators" heading) and needed its own fix before being scaled across 42 pages.*
