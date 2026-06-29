# Danton Developments — Staging Anomaly Report
**URL audited:** https://dantondevelstg.wpenginepowered.com  
**Date:** 2026-06-29  
**Auditor:** Claude (Playwright browser audit)  
**Pages checked:** 48 URLs across homepage, all service pages, new pages, location pages, footer links  

---

## Summary

| Category | Count |
|---|---|
| Critical issues | 5 |
| Content/copy anomalies | 7 |
| Broken/missing pages (404s) | 0 |
| SEO / title tag issues | 11 |
| Layout / visual anomalies | 2 |
| Form issues | 1 |
| Pre-launch blocking items | 1 |

---

## 1. Critical Issues

### 1.1 PHP Fragment Visible On-Page — Sitewide
**Severity:** Critical  
**Pages affected:** All pages except /about/ and /contact-us/ (confirmed on 18+ pages)  
**What:** The literal text `; ?>` renders visibly inside the "Get in Touch" section on every affected page. It sits between the subheading "Ready to start your project? Contact us today for a free, no-obligation quote." and the phone/email fields.  
**Evidence (exact rendered text):**
```
Ready to start your project? Contact us today for a free, no-obligation quote.
; ?>

Phone number
0403 709 884
```
**Cause:** A PHP conditional block in the template (likely `if(...): ?>...<?php endif; ?>`) has a closing fragment leaking into the rendered HTML. The template file containing `.get-in-touch-details` needs to be fixed.  
**Fix:** Find and correct the malformed PHP template tag in the "Get in Touch" section component. The text node "`; ?>`" must be removed from rendered output.

---

### 1.2 Broken Footer Logo — Sitewide
**Severity:** Critical  
**Pages affected:** All pages (sitewide — the footer logo is a template component)  
**What:** The footer logo image file `dantondevelopments-logo.png` fails to load (naturalWidth = 0). The logo renders as a broken image icon in the footer's `ft-column-one` section.  
**Evidence:**
- Footer logo src: `wp-content/uploads/dantondevelopments-logo.png` — broken  
- Header logo src: `wp-content/themes/dantondevelopments/assets/images/dantondevelopments-logo-header.png` — loads correctly  
**Fix:** Upload the footer logo file to the correct path, or update the footer template to reference the same image used in the header.

---

### 1.3 JavaScript Error On Every Page Load — footer.js
**Severity:** Critical  
**Pages affected:** All pages (sitewide)  
**What:** `footer.js` throws `TypeError: Cannot set properties of null (setting 'onclick')` on `window.onload` on every page. The script attempts to find `document.getElementById("modal-close")` and `document.getElementById("bonus-modaloverlay")`, then sets onclick on the result. Neither element exists anywhere on the site, so the result is null and the assignment throws.  
**Evidence (footer.js lines 30–39):**
```js
window.onload = () => {
  const close = document.getElementById("modal-close");
  const overlay = document.getElementById("bonus-modaloverlay");

  close.onclick = () => {           // ← throws: cannot set onclick on null
    overlay.style.display = "none";
  };
};
```
**Fix:** Either add a null guard (`if (close) { close.onclick = ... }`) or remove this block entirely if the planned modal/popup feature is not being implemented on this site.

---

### 1.4 Hi-Pages Rating Shows Incomplete Text
**Severity:** Critical (looks broken to visitors)  
**Pages affected:** Homepage  
**What:** The testimonials/reviews section renders the Hi-Pages badge as:  
`[Hi-pages logo image] is rated **Average**`  
The numeric score (e.g. "4.8/5" or "4.9") is missing from the template. The sentence reads like a broken template with the variable unfilled.  
**Evidence (raw HTML):**
```html
<p><img alt="Hi-pages Logo"> is rated <strong>Average</strong></p>
```
**Fix:** Update the Hi-Pages widget or hardcode the rating score (e.g. "is rated **4.9** Average" or "is rated **4.9/5**"). The numeric value is missing between "rated" and "Average".

---

### 1.5 Entire Site Set to noindex, nofollow
**Severity:** Pre-launch blocking (expected on staging, must not go live this way)  
**Pages affected:** All pages  
**What:** Every page returns `<meta name="robots" content="noindex, nofollow">`. This is correct and expected for a staging environment. However, this must be confirmed removed before DNS cutover or the live site will be deindexed.  
**Fix:** Confirm the WordPress "Discourage search engines from indexing this site" checkbox (Settings → Reading) is unchecked on the live environment before launch. Do not copy the staging robots setting to live.

---

## 2. Content / Copy Anomalies

### 2.1 Typo: "hghest" Instead of "highest"
**Page:** Homepage  
**Location:** Suspended Ceilings section, paragraph below the 4 service cards  
**Exact text:** `"Whether you need a modern office ceiling or an exposed industrial finish, we deliver results that meet the hghest standards."`  
**Fix:** Change `hghest` to `highest`.

---

### 2.2 "Partitions Walls" Pluralisation Error — All 6 Homepage Service Cards
**Page:** Homepage  
**Location:** Partition Walls Melbourne section — the service card labels  
**What:** All 6 partition wall service cards use the grammatically incorrect plural "Partitions Walls" instead of "Partition Walls". Affected labels:
- "Shop Partitions Walls" → should be "Shop Partition Walls"
- "Factory Partitions Walls" → should be "Factory Partition Walls"
- "Office Partitions Walls" → should be "Office Partition Walls"
- "Commercial Partitions Walls" → should be "Commercial Partition Walls"
- "Glass Partitions Walls" → should be "Glass Partition Walls"
- "Plasterboard Partitions Walls" → should be "Plasterboard Partition Walls"

Note: The page titles and H1s for these pages are correctly written ("Shop Partition Walls Melbourne", etc.). The error is only in the homepage card labels.

---

### 2.3 Double Spaces in Form Field Placeholders
**Pages:** Homepage (contact form popup) and /contact-us/  
**What:** Two form fields have double spaces in their placeholder text:
- `"Enter Your  First Name*"` (two spaces between "Your" and "First")
- `"Enter Your  Last Name*"` (two spaces between "Your" and "Last")  
**Fix:** Remove the extra space from both placeholder values in the form template.

---

### 2.4 Nav Label: "Project" Should Be "Projects"
**Location:** Main navigation, 4th item  
**What:** Nav label reads "Project" but the linked page is /projects/ and the page title is "Projects". All references elsewhere use the plural.  
**Fix:** Change the nav menu item text from "Project" to "Projects".

---

### 2.5 Awkward Phrasing — "Lowering Disruption"
**Page:** Homepage  
**Location:** "Working Across Melbourne and Geelong" section  
**Exact text:** `"...accommodating many types of project schedules and lowering disruption to your business operations."`  
**Issue:** "Lowering disruption" is not natural Australian English. Should be "minimising disruption" or "reducing disruption".

---

### 2.6 Repeated AI Phrasing — "Making Sure That"
**Page:** Homepage  
**Location:** Two instances in the homepage body copy  
- `"...making sure that your operations experience minimal disruption..."`
- `"...Fire-rated wall systems making sure that compliance standards are met"`  
**Issue:** "Making sure that" reads as AI-generated text and is unusual in trade copy. "Ensuring" is the natural equivalent and is shorter.

---

### 2.7 Footer Top Bar Label: "Maintenance & Emergency Repairs"
**Location:** Footer top bar (the dark bar above the footer columns)  
**What:** The top bar displays the label "Maintenance & Emergency Repairs" followed by a phone number and "Get a Free Quote" button. This label appears to be either a placeholder or an odd choice for a site-wide footer banner — it implies the footer CTA is only relevant for emergencies/repairs, whereas the site is a general commercial fitout business.  
**Note:** This may be intentional design. Flag with client to confirm the label is deliberate and not a leftover from a template.

---

## 3. Broken or Missing Pages (404s)

**Result: None found.**

All 48 URLs checked return HTTP 200. This includes:
- All 10 new pages: /plaster-ceilings/, /drop-ceilings/, /office-fitouts/, /shop-fitouts/, /plastering/, /shop-partition-walls/, /factory-partition-walls/, /commercial-partition-walls/, /testimonials/, /services/ — all 200 OK
- All 13 partition-walls location pages — all 200 OK
- All 13 suspended-ceilings location pages — all 200 OK
- All footer service links — all 200 OK
- /about/, /areas/, /contact-us/, /projects/, /privacy-policy/ — all 200 OK

**Specific checks from brief:**
- /suspended-ceilings/ — 200 OK, no redirect (confirmed: staging does NOT redirect to /suspended-ceilings-epping/ unlike live) ✓
- /partition-walls/ — 200 OK, real hub page with H1 "Partition Walls Melbourne" ✓
- /areas/ — 200 OK, lists all 26 location pages ✓

---

## 4. SEO / Title Tag Issues

### 4.1 Duplicate Title Tags — /partition-walls/ and /office-partitions-walls/
Both pages share the title: `"Office Partitions Melbourne | Danton Developments"`
- `/partition-walls/` — title: "Office Partitions Melbourne | Danton Developments", H1: "Partition Walls Melbourne"
- `/office-partitions-walls/` — title: "Office Partitions Melbourne | Danton Developments", H1: "Office Partitions Melbourne"

Additionally, the `/partition-walls/` title tag says "Office Partitions Melbourne" but the H1 says "Partition Walls Melbourne" — a direct mismatch. The title for `/partition-walls/` should be updated to reflect "Partition Walls Melbourne".

---

### 4.2 Eight Service Pages Missing "Melbourne" in Title Tag
The H1 on each of these pages correctly includes "Melbourne", but the `<title>` tag omits it. This is a missed geo-targeting opportunity for the most important ranking signal.

| Page | Current Title | H1 |
|---|---|---|
| /drop-ceilings/ | Drop Ceilings \| Danton Developments | Drop Ceilings Melbourne |
| /plaster-ceilings/ | Plaster Ceilings \| Danton Developments | Plaster Ceilings Melbourne |
| /shop-partition-walls/ | Shop Partition Walls \| Danton Developments | Shop Partition Walls Melbourne |
| /factory-partition-walls/ | Factory Partition Walls \| Danton Developments | Factory Partition Walls Melbourne |
| /commercial-partition-walls/ | Commercial Partition Walls \| Danton Developments | Commercial Partition Walls Melbourne |
| /office-fitouts/ | Office Fitouts \| Danton Developments | Office Fitouts Melbourne |
| /shop-fitouts/ | Shop Fitouts \| Danton Developments | Shop Fitouts Melbourne |
| /plastering/ | Plastering \| Danton Developments | Plastering Melbourne |

**Fix:** Add "Melbourne" to each title tag, e.g. "Drop Ceilings Melbourne | Danton Developments".

---

### 4.3 Missing Meta Description — /testimonials/
The `/testimonials/` page has no `<meta name="description">` tag at all. Every other page has a meta description.  
**Fix:** Add a meta description to the Testimonials page (e.g. "Read genuine client reviews for Danton Developments — suspended ceilings and partition walls across Melbourne and Geelong. 100+ satisfied clients.").

---

### 4.4 Title Separator Inconsistency — /testimonials/
**What:** Testimonials page uses a dash as the title separator (`Testimonials - Danton Developments`) while all other pages use a pipe (`|`).  
**Fix:** Change to `Testimonials | Danton Developments`.

---

### 4.5 Missing H2s on Several New Service Pages
The following pages have no `<h2>` elements — the heading hierarchy jumps from H1 directly to H3, which is an SEO structural issue:
- /plaster-ceilings/
- /drop-ceilings/
- /services/

Pages with existing H2 structure (correct): /suspended-ceilings/, /exposed-grid-ceilings/, /ceiling-replacement-repairs/, /office-partitions-walls/, /glass-partition-walls/, /plasterboard-partitions/, and all location pages.

---

## 5. Forms

### Contact Page (/contact-us/)
| Check | Result |
|---|---|
| H1 present | "Contact Us" ✓ |
| Form renders | ✓ (Contact Form 7) |
| Fields present | First Name, Last Name, Phone, Email, Service dropdown, Message ✓ |
| reCAPTCHA | Present (text reference + Google Privacy/Terms links) ✓ |
| Map embed | Present ✓ |
| PHP leak | Not present on this page ✓ |
| Honeypot spam field | Present (CF7 honeypot) ✓ |

### Homepage / Service Page Popup Form (#free-quote)
| Check | Result |
|---|---|
| Anchor exists on every page | ✓ (popup form embedded in every page template) |
| Free Quote CTA links resolve correctly | ✓ (resolve to current page's #free-quote anchor) |
| reCAPTCHA | Present ✓ |
| Double spaces in placeholders | First Name and Last Name placeholders have double spaces ✗ (see 2.3) |

---

## 6. New Pages — Quality Check

All 10 new pages exist and have real, complete content. No placeholder text, no lorem ipsum.

| Page | H1 | Word Count | Meta Desc | Notes |
|---|---|---|---|---|
| /plaster-ceilings/ | Plaster Ceilings Melbourne | ~700 | ✓ | No H2s |
| /drop-ceilings/ | Drop Ceilings Melbourne | ~670 | ✓ | No H2s |
| /office-fitouts/ | Office Fitouts Melbourne | ~650 | ✓ | — |
| /shop-fitouts/ | Shop Fitouts Melbourne | ~640 | ✓ | — |
| /plastering/ | Plastering Melbourne | ~640 | ✓ | — |
| /shop-partition-walls/ | Shop Partition Walls Melbourne | ~650 | ✓ | — |
| /factory-partition-walls/ | Factory Partition Walls Melbourne | ~650 | ✓ | — |
| /commercial-partition-walls/ | Commercial Partition Walls Melbourne | ~640 | ✓ | — |
| /testimonials/ | Testimonials | ~1,100 | MISSING | Dash in title, no H2s visible |
| /services/ | Services | ~270 | ✓ | Thin content, no H2s, no Melbourne modifier in H1 |

**Notes on /services/:** Word count of ~270 (excluding nav/footer) is very thin for a hub page. The H1 "Services" has no geo modifier. This may be intentional as a navigation hub, but it will not rank competitively.

---

## 7. Layout / Visual Anomalies

### 7.1 Hero Section — Video Background
The homepage hero uses an HTML5 video background. The accessibility tree shows the video fallback text ("Your browser does not support HTML5 video.") which is correct — this text only appears to non-video browsers. The visual screenshot confirms the video background loads and the H1 text overlays correctly.

### 7.2 Mobile Rendering
Viewport tested at 375×812 (iPhone SE). The homepage stacks correctly on mobile — content is readable, no horizontal overflow observed, navigation hamburger menu present. No critical mobile breakage detected visually.

### 7.3 Logo Carousel — Missing Alt Text
The brand/supplier logo carousel in the middle of the homepage contains approximately 20 logos without alt text (showing only as `img [ref=eXXX]` in the accessibility tree with no alt attribute or empty alt). Named logos confirmed (Armstrong, USG Boral, Dalken, Festool, Gyprock, Hilti) but many are missing. Low priority for launch but should be addressed.

---

## 8. Pre-Launch Checklist

Items that MUST be done before go-live, in addition to fixing the issues above:

| Item | Status |
|---|---|
| Remove noindex/nofollow from live site (Settings → Reading) | Must confirm on live |
| Fix PHP fragment "; ?>" in Get in Touch template | Fix required |
| Upload footer logo file (dantondevelopments-logo.png) | Fix required |
| Fix footer.js null reference error (add null guard for #modal-close) | Fix required |
| Add missing Hi-Pages numeric rating score | Fix required |
| Fix "hghest" typo on homepage | Fix required |
| Fix "Partitions Walls" → "Partition Walls" on 6 homepage service cards | Fix required |
| Add meta description to /testimonials/ | Fix required |
| Fix title tag on /partition-walls/ (currently "Office Partitions Melbourne", should be "Partition Walls Melbourne") | Fix required |
| Fix double space in form placeholders (First Name, Last Name) | Recommended |
| Add Melbourne to 8 service page title tags | Recommended |
| Change nav "Project" → "Projects" | Recommended |
| Fix /testimonials/ title separator dash → pipe | Recommended |
| Add H2 structure to /plaster-ceilings/, /drop-ceilings/, /services/ | Recommended |
| Test staging staging robots setting is not mirrored to live | Must confirm |
