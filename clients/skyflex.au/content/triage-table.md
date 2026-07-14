# Triage Table — skyflex.au (upgrade mode)

Generated at intake, 2026-07-14. Every URL below was **probed live** before classification.

> **Probe note.** A first pass with a default user-agent returned `403` on all 7 URLs. That was a
> bot filter, not real page status — re-probing with normal browser headers returned true statuses.
> No row here is classified on the 403 result. (`parse_meta_file.py` explicitly warns about this:
> WAF blocks are transient and must not be mistaken for 404s.)

| # | URL | HTTP | Detected page type | Role | Mode | Notes |
|---|-----|------|--------------------|------|------|-------|
| 1 | https://skyflex.au | 200 | homepage | working-entry | add-blocks | Client: add **two paragraphs only** for `pergolas melbourne`; existing copy must not change. Also a voice-corpus anchor (4,396 words live). |
| 2 | https://skyflex.au/louvred-pergolas-sydney/ | 200 | service-location | working-entry | add-blocks | Client: add **two paragraphs only** for `pergolas sydney`; existing copy must not change. Also a voice-corpus anchor (4,435 words live). |
| 3 | https://skyflex.au/smart-toilets/ | **404** | product-category | working-entry | **new-page** | Page does not exist. Net-new category page for U6 + U7 Smartoilet. **Blocked on a CMS prerequisite** — see below. |
| 4 | https://skyflex.au/product/skyflex-4k-android-smart-outdoor-tv/ | 200 | product | working-entry | rewrite-existing | Primary `waterproof tv australia`. **See waterproof-claim warning below.** |
| 5 | https://skyflex.au/product/skyflex-bbq-pods/ | 200 | product | working-entry | rewrite-existing | **Defect: page title is `Delta Motorised \| Skyflex`** — wrong product, copy-pasted from another SKU. |
| 6 | https://skyflex.au/product/delta-commercial-folding-arm/ | 200 | product | working-entry | rewrite-existing | Primary `retractable awning melbourne`; carries 3 more keywords incl. both Sydney terms. |
| 7 | https://skyflex.au/product/delta-pro-retractable-roof/ | 200 | product | working-entry | rewrite-existing | Primary `retractable roof system melbourne`. |

**Role rationale.** All 7 URLs appear in the Meta File, which is the authoritative target set — so all 7
are `working-entry`. None are `skip`. Rows 1 and 2 double as the **voice corpus**: they are the only
pages whose existing copy the client has explicitly told us to preserve, which makes them the honest
voice anchors for this brand. No `/content:ingest-approved` corpus has been supplied yet.

## Blockers and defects surfaced during triage

1. **`/smart-toilets/` cannot ship as a page yet (hard blocker).** The URL 404s, and the two SKUs it
   would cover (U6 + U7 Smartoilet) currently sit in WooCommerce's default *Uncategorized* bucket —
   no smart-toilet category taxonomy exists. The content can be written, but the category must be
   created before it can be published.

2. **Wrong title on the BBQ Pods product page.** `/product/skyflex-bbq-pods/` returns
   `<title>Delta Motorised | Skyflex</title>`. This is a live SEO defect independent of the content
   work and should go to the developer regardless of what this pipeline produces.

3. **"Waterproof" claim on the Outdoor TV page needs product-spec confirmation.** The primary keyword
   for row 4 is `waterproof tv australia`, and 2 of its secondary keywords assert an
   `ip55 waterproof rating`. Do **not** let the writer assert a waterproof/IP rating until the client
   confirms the TV actually carries a certified IP rating — writing an unsubstantiated durability
   claim is both an ACCC exposure and a returns liability. Targeting the keyword is fine; *asserting
   the spec* is not, unless verified.

4. **Homepage vs Sydney-page differentiation risk.** Rows 1 and 2 each receive exactly two new
   paragraphs, for `pergolas melbourne` and `pergolas sydney` respectively — same product, same block
   size, adjacent intent. Without an explicit differentiation requirement in the cluster plan these
   will read as swapped-suburb boilerplate, which is precisely what the audit gate blocks.
