---
name: client-compliancefdev
description: Compliance Fixer (compliancefdev.wpenginepowered.com) — Melbourne rental compliance, WP Engine dev site, spelling/content audit complete 23 Jul 2026
metadata:
  type: project
---

# Compliance Fixer — compliancefdev.wpenginepowered.com

## Business
- **Compliance Fixer** — Victorian rental property safety compliance (smoke alarm, gas, electrical safety checks + rectification works).
- Founded 2020 by **Luke Terella** and **Michael Bailey** (co-founder Michael Bailey featured on 7News as a subject matter expert).
- Address: 20/260 Wickham Rd, Highett VIC 3190 · Phone: **1800 548 502** · Email: **service@compliancefixer.com.au**
- Part of the **Fixer Group** — sister brands include **Appliance Fixer** and **Oven Fixer** (this matters: testimonials on the site are from those sister brands).
- Claims: 50,000+ inspections, 95% client retention, 25+ in-house technicians (no subcontractors), $20M public liability, "Mum's Place" standard.

## Site
- WP Engine **dev/staging** environment. WordPress + Yoast SEO.
- 72 URLs: 66 pages (`page-sitemap.xml`) + 6 blog posts (`post-sitemap.xml`). No orphan pages outside the sitemap.
- Structure: 4 core service pages, ~14 rectification service pages, 5 audience pages, 34 suburb pages, `/areas-we-serve/`, blog.
- **All 72 pages are `noindex, nofollow`** and have **no canonical tags**; `robots.txt` is empty. Correct for staging — must be reversed at launch.
- **Crawl note:** the host rate-limits (HTTP 429) at roughly 40 requests. Crawl with ≤6 workers then retry the remainder sequentially with ~3s delays.

## Related client folder
`clients/compliancefixe.wpenginepowered.com/` holds an earlier spelling audit for what appears to be the same client on a different WP Engine environment — check it before starting new work here.

## Work delivered
- **23 Jul 2026** — Full-site spelling / AU English / content anomaly audit.
  Deliverable: `clients/compliancefdev.wpenginepowered.com/spelling-mistakes-finder/compliancefdev.wpenginepowered.com.html`
  99 findings (30 wrong content, 37 grammar, 12 typos, 8 company name, 7 punctuation, 5 US English) + 18 site-wide structural observations.

### Highest-severity items found (for follow-up verification)
1. `/contact/` meta description belongs to a **concrete resurfacing business**.
2. All four testimonials praise **Appliance Fixer / Oven Fixer**, not Compliance Fixer.
3. **"Competitor 1 / Competitor 2"** placeholder table headers live on 20 pages.
4. `[INSERT LINK TO OTHER BLOG ON THIS)` editor note published live in a blog post.
5. Wrong phone **04 0367 1657** on `/rcd-safety-switch-replacements/` and `/hot-water-service-repairs/`.
6. **"100k+ safety checks"** on homepage/About contradicts "50,000+" used ~90× site-wide.
7. Nav menu item **"Switchboard & Main Earth Upgradesz"** on all 72 pages.
8. `/areas-we-serve/` lists only **Portsea and Geelong** under "areas we serve".
9. `/home-owners/` is titled Homeowners but all copy addresses landlords/rental providers.

### Systemic content-production faults worth watching on future rounds
- A **"ensure" → "make sure"** find-and-replace was run without proofreading, producing broken sentences (incl. two meta descriptions).
- A **"comprehensive" → "extensive" / "wide-ranging"** replacement produced 141 awkward collocations; one page still says "Comprehensive".
- Card label + description are concatenated with **no separator** in the template across ~18 pages.
- Multiple lead-ins ending in ":" have **no list following** (missing bullet content).
- Image alt text is largely **auto-generated from filenames**, carrying filename typos (Baibley, Compliacne, Rectifaction, Gurantee, divisons, Missinon, Upgradesz) into 59+ pages. Fixing alt text alone is not enough — the media filenames need renaming.

See also [[capability_content_review]], [[capability_pre_launch_audit]].
