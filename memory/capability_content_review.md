# Capability: Content & Image Review

## What this is
A live audit of a client's website — visiting every page via Playwright to check:
- Content accuracy (facts, claims, contact details)
- Spelling and grammar
- Image relevance (does the image match the content?)
- Anomalies (broken links, duplicate text, placeholder content)
- Technical content issues (wrong redirects, missing sitemap entries)

## When to use
When the client wants a general "health check" of their site content, or before a keyword content push where we need to know the baseline state of existing pages.

## Process

### 1. Discover pages
- Navigate to `sitemap.xml` (or `sitemap_index.xml`)
- If 404: check `robots.txt` for the correct sitemap URL
- Use `page-sitemap.xml` for content pages (not post/product/category sitemaps unless relevant)
- Note image count per page from sitemap — 0 images on pages is a flag

### 2. Categorise pages
- Group by type: core/service pages, location pages, gallery pages
- For location pages (templated): audit 1–2 samples per template type, apply findings to all
- For gallery sub-pages (image-only): spot-check structure only
- Skip legal pages (trading terms, disclaimer) unless asked

### 3. Audit each page
For each page:
- `browser_navigate` to the URL
- `browser_take_screenshot` with `fullPage: true`, save as `screenshots/NN-page-name.jpeg`
- `browser_snapshot` on the article/main element to capture text
- Log all issues found

### 4. Check for systemic issues
Always check:
- [ ] Redirects — do service-level URLs redirect to the right place?
- [ ] Internal links — do inline links point to real pages?
- [ ] Pages referenced in nav or body that aren't in the sitemap
- [ ] Consistent facts across all pages (business age, Google rating, phone, address)

### 5. Write report
Save to `clients/[domain]/content-review/content-audit-YYYY-MM-DD.md`
Screenshots to `clients/[domain]/content-review/screenshots/`

## Issue severity tiers
- **Critical**: Broken links, wrong content displayed, broken UI (counters stuck at 0)
- **High**: Typos on important pages, duplicate H1, stale facts, missing sitemap entries
- **Medium**: Grammar errors, duplicate intro paragraphs, inaccurate business descriptions
- **Low/Advisory**: Image relevance, dated content, SEO opportunities

## Playwright constraint
Playwright MCP only saves screenshots to its allowed roots:
- `/home/invoi/.colana/worktrees/fahad-projects/[worktree-id]/`
- `/home/invoi/.colana/worktrees/fahad-projects/[worktree-id]/.playwright-mcp/`

Create a `screenshots/` folder in the worktree, save there, then `cp -r` to the client folder after.

## Key things to check (checklist)
- [ ] Business age / "years in business" — correct number?
- [ ] Google rating — consistent across all pages?
- [ ] Phone number format — consistent and correct?
- [ ] Email link — single intact anchor, not split?
- [ ] Address — correct postcode and street?
- [ ] Hours — formatted correctly, no spaces in time?
- [ ] All H1 tags — only one H1 per page?
- [ ] VEU / program mentions — brackets closed properly?
- [ ] Inline URL fragments — any raw paths left in text?
- [ ] Redirect chains — do service URLs land on correct pages?
- [ ] Sitemap coverage — are all key pages included?
- [ ] Duplicate bullets or paragraphs?
- [ ] Placeholder/template text left in?
- [ ] "Factory" or other wrong business descriptor?

## Deliverable
Markdown file: `content-audit-YYYY-MM-DD.md`
Sections:
1. Summary table (Critical / High / Medium / Low counts)
2. Pages audited table
3. Issues by severity (C1, C2... / H1, H2... / M1... / L1...)
4. Image relevance assessment table
5. Pages not audited + reason
6. Recommended fix priority order with estimated time

## Reference
First run: mckinnonheating.com.au, 2026-06-24. 118 pages in sitemap, 15 core+sample pages audited, 19 issues found (4 critical, 6 high, 5 medium, 4 advisory).
