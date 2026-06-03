# Energus — Site Architecture Analysis
**Date:** 3 Jun 2026  
**Scope:** Root service pages, URL structure, meta overhaul, +Australia targeting

---

## 1. Current Site Audit — Critical Issues Found

### Issue 1 — ALL PAGES have identical meta description (P0)
Every single page on the site returns:  
`"Commercial Solar Installations"`  
This applies to ~30+ pages including completely different services (battery, industrial solar, locations).  
Google ignores duplicate meta descriptions and generates its own — this is the #1 quick win on the entire site.

### Issue 2 — Three different pages share the same H1 (P0 cannibalisation)
- `/commercial-solar-panels/`
- `/commercial-solar-installer/`
- `/battery-for-business/`

All three carry: **"COMMERCIAL SOLAR PANELS INSTALLATION COMPANY IN NSW"**  
This is triple cannibalisation + geographic restriction ("IN NSW") for a national company.

### Issue 3 — /commercial-solar/ redirects to the wrong page
`/commercial-solar/` → 301 → `/commercial-solar-installer/`  
The most logical root URL for the entire commercial solar silo is wasted as a redirect to a specific installer page.

### Issue 4 — /industrial-solar/ exists but is broken
`/industrial-solar/` returns 200 OK but displays the **homepage title** ("Energus - Solar Energy for Australian Business"), has no H2s, and has a thin/unoptimised page. The underscore URL `/industrial_solar_energy/` also still exists and is indexed.

### Issue 5 — Three battery pages cannibalising each other
| URL | Title | H1 |
|-----|-------|----|
| `/battery/` | "Commercial Battery Storage & Installation \| Energus" | "Transforming Commercial & Industrial Energy Storage" |
| `/battery-for-business/` | "Battery for Business -Top commercial solar and battery installer" | "COMMERCIAL SOLAR PANELS INSTALLATION COMPANY IN NSW" ← wrong! |
| `/commercial-battery-installer/` | "Commercial Battery Installer -Top commercial solar and battery installer" | "Top Commercial Battery Storage Installer" |

Three pages. Zero coordination. One of them has a completely wrong H1.

### Issue 6 — State location archive pages are indexed with no content
`/locations/nsw/`, `/locations/qld/`, `/locations/vic/` — these are WordPress taxonomy archive pages with title "NSW Archives" and H1 "Location Archives:". They have no real content and should be noindexed immediately before the new city pages are built.

---

## 2. Root Service Pages Architecture

The new location pages use a **flat URL structure**:
- `/commercial-solar-sydney/` (not `/commercial-solar/sydney/`)
- `/industrial-solar-sydney/`
- `/commercial-battery-storage-sydney/`

This means the root service pages act as **topical hubs** linked from breadcrumbs and internal links — not URL parents. Three root pages are required:

---

### Root 1: Commercial Solar — `/commercial-solar/`

| | Current State | Recommended |
|-|---------------|-------------|
| **URL** | Exists as 301 → `/commercial-solar-installer/` | Remove redirect, create new page |
| **Target keyword** | — | `commercial solar australia` |
| **Secondary keywords** | — | `commercial solar company`, `commercial solar installers` |
| **Title tag** | (redirect, no title) | `Commercial Solar Installers Australia \| Energus` |
| **H1** | (redirect, no H1) | `Commercial Solar Installers Australia` |
| **Meta description** | (redirect, no meta) | `Energus are Australia's top-rated commercial solar installers. End-to-end design, installation and monitoring across NSW, VIC, QLD and SA. 55MW+ delivered.` |
| **Page purpose** | — | National hub → links to all city pages |

**Developer action:**  
1. Delete the redirect from `/commercial-solar/` → `/commercial-solar-installer/` in the redirect plugin
2. Create new WordPress page at slug `commercial-solar`
3. Add breadcrumbs: Home > Commercial Solar

---

### Root 2: Industrial Solar — `/industrial-solar/`

| | Current State | Recommended |
|-|---------------|-------------|
| **URL** | 200 OK — page exists (but broken: shows homepage title, no H2s, thin content) | Keep URL, full content rebuild |
| **Also:** `/industrial_solar_energy/` | Still indexed, underscores | 301 → `/industrial-solar/` |
| **Target keyword** | `industrial solar energy` (weak intent) | `industrial solar australia` |
| **Secondary keywords** | — | `industrial solar panels`, `industrial solar installers` |
| **Title tag** | "Energus - Solar Energy for Australian Business" ← homepage title! | `Industrial Solar Installers Australia \| Energus` |
| **H1** | "INDUSTRIAL SOLAR ENERGY" | `Industrial Solar Installers Australia` |
| **Meta description** | "Commercial Solar Installations" (wrong) | `Energus specialises in large-scale industrial solar installations across Australia. In-house engineers, Tier 1 panels, ISO-certified. 55MW+ delivered.` |

**Developer action:**  
1. Fix page title (it's displaying homepage title — likely a Yoast bug or missing page title setting)
2. Rewrite H1 to `Industrial Solar Installers Australia`
3. Add H2 structure (currently no H2s at all)
4. Add 301 from `/industrial_solar_energy/` → `/industrial-solar/`

---

### Root 3: Commercial Battery Storage — `/commercial-battery-storage/`

| | Current State | Recommended |
|-|---------------|-------------|
| **URL** | 404 — doesn't exist | Create new page |
| **Consolidate from:** | `/battery/`, `/battery-for-business/`, `/commercial-battery-installer/` | All 301 → `/commercial-battery-storage/` |
| **Target keyword** | — | `commercial battery storage australia` |
| **Secondary keywords** | — | `commercial battery storage systems`, `battery energy storage system australia` |
| **Title tag** | — | `Commercial Battery Storage Australia \| Energus` |
| **H1** | — | `Commercial Battery Storage Australia` |
| **Meta description** | — | `Energus designs and installs commercial battery storage systems for Australian businesses. C&I BESS, demand management, and backup power across NSW, VIC, QLD and SA.` |

**Developer action:**  
1. Create new page at slug `commercial-battery-storage`
2. Add 301 redirects: `/battery/` → `/commercial-battery-storage/`, `/battery-for-business/` → `/commercial-battery-storage/`, `/commercial-battery-installer/` → `/commercial-battery-storage/`
3. Keep `/battery/` content structure as reference for the new page (it has the best title tag of the three)

---

## 3. Full URL Change Register

| Priority | Action | From | To | Notes |
|----------|--------|------|----|-------|
| P0 | Remove redirect + create page | `/commercial-solar/` (→ /commercial-solar-installer/) | `/commercial-solar/` (new root) | |
| P0 | Create new page | 404 | `/commercial-battery-storage/` | Consolidation root |
| P0 | 301 redirect | `/battery/` | `/commercial-battery-storage/` | |
| P0 | 301 redirect | `/battery-for-business/` | `/commercial-battery-storage/` | |
| P0 | 301 redirect | `/commercial-battery-installer/` | `/commercial-battery-storage/` | |
| P1 | 301 redirect | `/industrial_solar_energy/` | `/industrial-solar/` | Underscore URL |
| P1 | Noindex | `/locations/nsw/` | — | Thin archive page |
| P1 | Noindex | `/locations/qld/` | — | Thin archive page |
| P1 | Noindex | `/locations/vic/` | — | Thin archive page |
| P1 | Noindex | `/locations/other/` | — | Thin archive page |

---

## 4. Existing Pages — Title/H1/Meta Fix List

These pages stay at their current URLs but need immediate on-page fixes:

| Page | Fix | Current | Recommended |
|------|-----|---------|-------------|
| `/commercial-solar-panels/` | Title | "Commercial Solar Panels - commercial solar for business" | "Commercial Solar Panels Australia \| Energus" |
| `/commercial-solar-panels/` | H1 | "COMMERCIAL SOLAR PANELS INSTALLATION COMPANY IN NSW" | "Commercial Solar Panels for Australian Businesses" |
| `/commercial-solar-panels/` | Meta | "Commercial Solar Installations" | "Energus supplies and installs commercial solar panels for businesses Australia-wide. Tier 1 panels, in-house engineers, 10-year workmanship warranty." |
| `/commercial-solar-installer/` | Title | "Commercial Solar Installer -Top commercial solar installer, battery installer" | "Commercial Solar Installer Australia \| Energus" |
| `/commercial-solar-installer/` | H1 | "COMMERCIAL SOLAR PANELS INSTALLATION COMPANY IN NSW" | "Australia's Top-Rated Commercial Solar Installer" |
| `/commercial-solar-installer/` | Meta | "Commercial Solar Installations" | "Energus is one of Australia's top 5 commercial solar installers. CEC-accredited, ISO-certified, 55MW+ delivered. Get a free commercial solar quote today." |
| `/solar-for-business/` | Title | "Solar Energy for Business - commercial solar system" | "Solar for Business Australia \| Commercial Solar Systems — Energus" |
| `/solar-for-business/` | H1 | "SOLAR ENERGY FOR BUSINESS" | "Solar Energy Solutions for Australian Businesses" |
| `/solar-for-business/` | Meta | "Commercial Solar Installations" | "Cut energy bills with a commercial solar system from Energus. We design, install and monitor solar for Australian businesses of all sizes. Tier 1 panels, full service." |
| `/industrial-solar/` | Title | "Energus - Solar Energy for Australian Business" ← homepage title! | "Industrial Solar Installers Australia \| Energus" |
| `/industrial-solar/` | H1 | "INDUSTRIAL SOLAR ENERGY" | "Industrial Solar Installers Australia" |
| `/industrial-solar/` | Meta | "Commercial Solar Installations" | "Energus specialises in large-scale industrial solar for Australian businesses. In-house engineers, Tier 1 panels, ISO-certified project delivery across NSW, VIC, QLD and SA." |
| **ALL 30+ pages** | Meta | "Commercial Solar Installations" (identical on all) | **Each page needs a unique meta description** |

---

## 5. Opinion: "[Keyword] + Australia" on Root Service Pages

**Recommendation: YES — strong yes.**

Here's why this is the right call for Energus specifically:

**A. The search intent is correct for the root**  
A business owner typing "commercial solar australia" is in national evaluation mode — they want to assess providers before calling one. That person is Energus's ideal prospect. Capturing them on the root page before they narrow to a city is higher-funnel and higher-value.

**B. It differentiates root pages from city pages cleanly**  
- Root: `/commercial-solar/` → targets "commercial solar australia" (national intent)
- City: `/commercial-solar-sydney/` → targets "commercial solar sydney" (local intent)
No cannibalisation, no confusion for Google.

**C. It signals national authority to Google**  
The "Australia" modifier on the root tells Google this is the hub for all state/city pages. Combined with internal links from every city page back to the root, this creates a proper silo that passes authority upward.

**D. B2B buyers search differently to consumers**  
Commercial solar buyers are CFOs and property developers — they often search nationally first ("who are the best commercial solar companies in Australia?"), then narrow. Residential solar buyers search locally. Energus is B2B, so national modifier makes sense.

**E. Volume is secondary for B2B**  
Even if "commercial solar australia" has low volume (likely 30–100/mo), the conversion intent for B2B is very high. One closed commercial solar deal is $100K+. You don't need 10,000 clicks.

**Target keywords for root pages:**

| Root Page | Primary Keyword | Secondary |
|-----------|----------------|-----------|
| `/commercial-solar/` | commercial solar australia | commercial solar company australia, commercial solar installers australia |
| `/industrial-solar/` | industrial solar australia | industrial solar panels australia, industrial solar installers |
| `/commercial-battery-storage/` | commercial battery storage australia | commercial battery storage systems australia, C&I battery storage |

---

## 6. Location Pages — Breadcrumb & Internal Link Structure

All city pages should use this breadcrumb pattern (regardless of flat URL):

**Commercial Solar:**  
Home > [Commercial Solar](/commercial-solar/) > Commercial Solar Sydney

**Industrial Solar:**  
Home > [Industrial Solar](/industrial-solar/) > Industrial Solar Sydney

**Commercial Battery Storage:**  
Home > [Commercial Battery Storage](/commercial-battery-storage/) > Commercial Battery Storage Sydney

**Regional pages** (Newcastle, Wetherill Park, etc.) also breadcrumb through /commercial-solar/.

**Internal linking rule:**  
Every location page should link back to:
1. The root service page (`/commercial-solar/`)
2. 2–3 related city pages (e.g. Sydney links to Melbourne and Brisbane)
3. The relevant case study if there's one in that city/region

---

## 7. Summary Action Checklist

### Developer (WordPress)
- [ ] Delete redirect: `/commercial-solar/` → `/commercial-solar-installer/`
- [ ] Create page at `/commercial-solar/` (commercial solar australia root)
- [ ] Create page at `/commercial-battery-storage/` (new battery root)
- [ ] Add 301: `/battery/` → `/commercial-battery-storage/`
- [ ] Add 301: `/battery-for-business/` → `/commercial-battery-storage/`
- [ ] Add 301: `/commercial-battery-installer/` → `/commercial-battery-storage/`
- [ ] Add 301: `/industrial_solar_energy/` → `/industrial-solar/`
- [ ] Noindex: `/locations/nsw/`, `/locations/qld/`, `/locations/vic/`, `/locations/other/`
- [ ] Fix `/industrial-solar/` page title (showing homepage title — check Yoast settings)

### Content/SEO (Yoast)
- [ ] Write unique meta descriptions for ALL 30+ pages (P0 — currently all identical)
- [ ] Fix H1 on `/commercial-solar-panels/` — remove "IN NSW"
- [ ] Fix H1 on `/commercial-solar-installer/` — remove "IN NSW"
- [ ] Fix H1 on `/battery-for-business/` (wrong H1 entirely — it's a commercial solar H1)
- [ ] Update title tags on all pages (see table in Section 4)
- [ ] Write content for `/commercial-solar/` root page
- [ ] Rebuild content for `/industrial-solar/` (currently thin, no H2s)
- [ ] Write content for `/commercial-battery-storage/` root page

### New Location Pages (35 total to build)
- 5 × Commercial Solar (capital cities)
- 5 × Industrial Solar (capital cities)
- 5 × Commercial Battery Storage (capital cities)
- 20 × Commercial Solar (regional cities)
