# Danton Developments — Master Content Comparison Report
## Live vs Staging Pre-Launch Audit

**Live:** https://dantondevelopments.com.au  
**Staging:** https://dantondevelstg.wpenginepowered.com  
**Date:** 2026-06-29  
**Pages audited:** 32 total  
- 5 service pages  
- 13 suspended ceilings location pages  
- 13 partition walls location pages  
- 1 additional page checked directly (/office-partitions-walls/)

---

## MASTER ACTION LIST

### 🔴 HIGH — Fix before launch (actual content changes)

| # | Page | Issue | Detail |
|---|---|---|---|
| 1 | /suspended-ceilings-richmond/ | Word "Homes" incorrectly inserted in heading | Live: "Suspended Ceilings for Richmond: Why Choose Danton Developments" → Staging: "Suspended Ceilings for Richmond **Homes**: Why Choose Danton Developments". Richmond is a commercial page — "Homes" is inaccurate. Remove it. |
| 2 | /suspended-ceilings/ | JS redirect on live only | Live /suspended-ceilings/ has a JS redirect → /suspended-ceilings-epping/. Staging loads the service page normally. Confirm: remove redirect from live, or add it to staging? |
| 3 | /suspended-ceilings/ | Missing words in bullet point on staging | Staging: "Office partition walls creating meeting rooms" — Live: "Office partition walls creating meeting rooms **and private spaces**". Add the 3 missing words. |
| 4 | /office-partitions-walls/ | Colons missing from all 5 "Why Choose" bullet points | Staging drops the colon separator after each bold label. Live: "**25+ Years Experience:** Our industry experts…" → Staging: "**25+ Years Experience** Our industry experts…". Fix across all 5 bullets. |
| 5 | /partition-walls-williams-landing/ | Truncated word "Quot" persists on staging | "The Danton Developments Process" Step 2 is labelled "Design and Quot" on both live AND staging — the word "Quote" is cut off. Needs manual fix on staging before launch. |
| 6 | /partition-walls-southbank/ | Wording changed — needs confirmation | Live: "Compliances and management approvals" → Staging: "Building permits and management approvals". Confirm which version is correct with the client/copywriter. |

### 🟡 MEDIUM — Confirm intent before launch (structural/design decisions)

| # | Page | Issue |
|---|---|---|
| 7 | /office-partition-walls/ (wrong slug) | **Correct URL is /office-partitions-walls/** (with 's'). Original audit brief listed the wrong slug — this page exists and is fine. Update any internal links, sitemaps, or docs that reference the wrong slug. |
| 8 | /suspended-ceilings-epping/ | Page title on staging adds "| Danton Developments" suffix — not on live. All other 12 suspended ceilings pages already have the suffix; this is likely a standardisation fix. Confirm intentional. |
| 9 | /plasterboard-partitions/ | Phone number format differs: Live "0403709884" (no spaces) → Staging "0403 709 884" (correct format). Staging is right; live has a typo. Confirm and optionally fix live site too. |
| 10 | /suspended-ceilings/ | Intro paragraphs not confirmed on staging — two opening paragraphs from live need visual verification on staging. |
| 11 | /suspended-ceilings/ | Heading levels: H3 subheadings on live promoted to H2 on staging for several sections. Confirm this heading hierarchy change is intentional (affects SEO). |
| 12 | /partition-walls-preston/ + /partition-walls-grovedale/ | Numbered process steps lose numbering on staging — becomes a plain bullet list. If ordered steps were intentional, developer needs to restore numbering. |
| 13 | /suspended-ceilings-cheltenham/ | 4 H3 subheadings inside "Why Choose" section removed as headings on staging — content kept as bold paragraphs. Confirm intentional. |

### ✅ No action needed — Intentional redesign additions (consistent sitewide)

These are present on staging only — all pages — and are additions, not changes to existing content:

| Element | Notes |
|---|---|
| Trust badge bar in hero (25+ Years / Premium Materials / 3000+ Projects / Fully Insured) | New template feature |
| Breadcrumb navigation | New template feature |
| "Other Services" card strip | New template feature |
| "Our Recent Work" photo gallery | New template feature |
| "Built on Experience. Driven by Quality." brand logo bar (16 logos) | New template feature |
| "Get in Touch" mid-page CTA block with contact form | New template feature |
| "Maintenance & Emergency Repairs" CTA banner above footer | New template feature |
| Inline dual CTAs ("Get a Free Quote | 0403 709 884") between sections | New template feature |
| Expanded footer: Instagram, ABN (38 105 969 589), opening hours | New template feature |
| FAQ accordion (answers collapsed, first expanded) vs fully expanded on live | New template feature |
| Bold bullet labels: em-dash format (live) → colon format (staging) | Consistent template change across all partition walls pages |
| "Areas We Serve" moves before FAQ across all partition walls pages | Consistent template change |
| FAQ heading: H2 (live) → H3 (staging) across all location pages | Consistent template change |

---

## PAGE-BY-PAGE STATUS SUMMARY

### Service Pages

| Page | Status |
|---|---|
| /suspended-ceilings/ | ⚠️ 3 issues (JS redirect, missing words in bullet, intro para needs visual check) |
| /office-partition-walls/ | ❌ Wrong URL in brief — correct URL is /office-partitions-walls/ |
| /office-partitions-walls/ | ⚠️ 1 issue (colons missing in "Why Choose" bullets), section reorder confirmed |
| /glass-partition-walls/ | ✅ Core content matches |
| /plasterboard-partitions/ | ⚠️ 1 minor issue (phone number format) |
| /ceiling-replacement-repairs/ | ✅ Full match |

### Suspended Ceilings Location Pages

| Page | Status |
|---|---|
| /suspended-ceilings-epping/ | ⚠️ Page title suffix differs (likely intentional fix) |
| /suspended-ceilings-truganina/ | ✅ Full match |
| /suspended-ceilings-williams-landing/ | ✅ Full match |
| /suspended-ceilings-preston/ | ℹ️ H3→H2 heading level change (confirm intent) |
| /suspended-ceilings-cheltenham/ | ℹ️ 4 H3 subheadings converted to bold paragraphs (confirm intent) |
| /suspended-ceilings-cremorne/ | ℹ️ H3→H2 heading level change (confirm intent) |
| /suspended-ceilings-richmond/ | 🔴 Word "Homes" added to heading — needs removal |
| /suspended-ceilings-port-melbourne/ | ✅ Full match |
| /suspended-ceilings-collingwood/ | ✅ Full match |
| /suspended-ceilings-southbank/ | ✅ Full match |
| /suspended-ceilings-geelong/ | ✅ Full match |
| /suspended-ceilings-grovedale/ | ✅ Full match |
| /suspended-ceilings-moolap/ | ✅ Full match |

### Partition Walls Location Pages

| Page | Status |
|---|---|
| /partition-walls-epping/ | ✅ Content match (section reorder = template) |
| /partition-walls-truganina/ | ✅ Content match (section reorder = template) |
| /partition-walls-williams-landing/ | 🔴 Typo "Design and Quot" persists on staging |
| /partition-walls-preston/ | ℹ️ Process steps lose numbering on staging |
| /partition-walls-cheltenham/ | ✅ Content match |
| /partition-walls-cremorne/ | ✅ Content match |
| /partition-walls-richmond/ | ✅ Content match (section reorder = template) |
| /partition-walls-port-melbourne/ | ✅ Content match (section reorder = template) |
| /partition-walls-collingwood/ | ✅ Content match (section reorder = template) |
| /partition-walls-southbank/ | ⚠️ One word changed — "Compliances" → "Building permits" (confirm intent) |
| /partition-walls-geelong/ | ✅ Content match (section reorder = template) |
| /partition-walls-grovedale/ | ℹ️ Process steps lose numbering on staging |
| /partition-walls-moolap/ | ✅ Content match (section reorder = template) |

---

## SCORECARD

| Category | Count |
|---|---|
| 🔴 Fix before launch | 6 issues |
| 🟡 Confirm intent | 7 items |
| ✅ Full content match | 20 pages |
| ℹ️ Structural-only differences | 6 pages |

**Bottom line:** The core content migration is in excellent shape — 20 of 32 pages are a full match. The only actual content errors are: 1 wrong word inserted (Richmond), 1 truncated word (Williams Landing), 1 wording change needing confirmation (Southbank), and missing colons on the /office-partitions-walls/ "Why Choose" section. Everything else is either a clean match or intentional design template changes.
