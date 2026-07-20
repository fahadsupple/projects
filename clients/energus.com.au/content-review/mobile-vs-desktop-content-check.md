# energus.com.au — Mobile vs Desktop Content Parity Check

**Date:** 2026-07-20
**Scope:** SEO pages only — homepage, all location pages, `/aboutus`, `/earc-solar-skin/`, `/newconstructions/`, `/commercial-battery-storage/`
**Pages checked:** 49
**Result: 47 clean, 2 with genuine content mismatches**

---

## Method

Desktop and mobile user-agents return **byte-identical HTML** (verified: 186,154 bytes both ways on `/commercial-solar/`). This is not two separately-served templates — it is one Elementor build using responsive show/hide. So the only valid test is real rendering, not fetching.

- Chromium rendered at **1440×900** (desktop UA) and **390×844** (iPhone UA, touch + mobile emulation)
- Each page fully scrolled to trigger lazy-loaded sections
- Visible text only — text nodes kept only where `checkVisibility()` passes with opacity and CSS checks, so anything hidden by a breakpoint rule drops out
- Scoped to `main#main`, with `nav`, `[role=navigation]`, `.elementor-nav-menu`, `ul.menu`, `header`, `footer` and breadcrumbs excluded by ancestor lookup
- Compared as a multiset of visible body-text chunks

**Per instruction:** H1 counts, meta titles, meta descriptions and OG tags were **not** assessed. Duplicate H1s are irrelevant here so long as the content matches.

---

## Findings — content mismatches

### 1. Homepage — `https://energus.com.au/`

| Version | Text |
|---|---|
| Desktop only | we've participated in pricing **quotations** for |
| Mobile only | we've participated in pricing for |

Same sentence, two different copy versions. Desktop and mobile are being fed separate text blocks that have drifted apart.

### 2. `/newconstructions/` — two mismatches

| Version | Text |
|---|---|
| Desktop only | request a **solar quote** for your site |
| Mobile only | request a **quotation** for your site |
| Desktop only | we've participated in pricing **quotations** for |
| Mobile only | we've participated in pricing for |

The second mismatch is the **same string as the homepage** — this is one shared block that exists in two drifted copies, appearing on at least two pages. Fixing it at source likely fixes both.

The first is a CTA wording difference: "request a solar quote" vs "request a quotation". Minor commercially, but it means the mobile CTA is missing the "solar" keyword.

---

## Clean — no mismatch found

All 45 location pages returned identical visible body content across both viewports:

- **Commercial solar (30):** adelaide, albury, ballarat, brisbane, bundaberg, cairns, dandenong, geelong, gladstone, gold-coast, mackay, melbourne, mount-gambier, new-south-wales, newcastle, penrith, queensland, shepparton, south-australia, sunshine-coast, sydney, toowoomba, townsville, victoria, wagga-wagga, wetherill-park, whyalla, wollongong, yatala
- **Commercial battery storage (6):** adelaide, brisbane, gold-coast, melbourne, sydney, plus the `/commercial-battery-storage/` root
- **Industrial solar (5):** adelaide, brisbane, gold-coast, melbourne, sydney
- **Location hubs (5):** `/locations/`, `/locations/nsw/`, `/locations/qld/`, `/locations/vic/`, `/locations/other/`

Also clean: `/aboutus`, `/earc-solar-skin/`.

This is a meaningful result rather than a null one — the check demonstrably detects real differences (it caught three), so 45 clean location pages is positive evidence of parity, not an absence of testing.

---

## Side findings — outside the content-parity brief, but worth acting on

These surfaced while locating pages and are flagged for awareness, not as part of the mobile/desktop question.

1. **`/about/` 301-redirects to `/products/about-solar-inverters/`** — a *product* page, not the About page. The real About page is `/aboutus`. Anyone following an `/about/` link lands on inverter product content. Likely a misconfigured redirect worth correcting to point at `/aboutus`.

2. **`/aboutus` and `/newconstructions/` are missing from the XML sitemap.** Both return 200 and both are live pages; `/newconstructions/` is one you flagged as an SEO page. Neither appears in `page-sitemap.xml`. `/earc-solar-skin/` is correctly included.

3. **`/aboutus` has no trailing slash** while every other URL on the site does. Minor consistency issue.

---

## Caveat on interpretation

Accordions and tabs load in whatever state the template sets, and the script reads that state as-is. If a section were collapsed on mobile but expanded on desktop it would surface as a diff even though the content is present on both. **None of the three findings above are of that type** — all three are word-level copy differences within visible running text, so all three are genuine content drift rather than UI state.

---

## Reproducing

`compare.py` in this folder is the check script. Raw per-page output is in `seo.json` and `about.json`, including full chunk counts per page.

```bash
python3 compare.py <urls-file> <output.json>
```
