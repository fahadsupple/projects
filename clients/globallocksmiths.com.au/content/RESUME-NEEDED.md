# RESUME-NEEDED — voice corpus ingest halted

**Halted:** 2026-07-29
**Phase:** `ingest-approved` (voice corpus)
**Everything else is complete.** Intake, the profile, all 41 entries and the
service-hub reclassification are done and committed. Only the voice-corpus step
is blocked.

## Why

The analyst authorised taking brand voice from the live website. Six pages were
fetched and extracted — but the live site asserts, in customer-facing copy, the
exact claims the analyst ruled out on 2026-07-28/29:

| Claim on the live site | Analyst ruling |
|---|---|
| "24 hours a day, 7 days a week, including weekends and public holidays" | Mon–Fri 9–5 only |
| "an emergency lockout in the middle of the night" | No emergency service |
| "We typically arrive within 30 to 60 minutes" | No response-time promise |
| "for over fifteen years" | Use "since 2002" only — and this is a 4th conflicting tenure |

Counts across the six extracted pages: 12 × 24/7-type, 7 × emergency,
5 × response-time, 8 × tenure year-count. The homepage and both suburb pages are
affected; Brighton's title tag is "Locksmith Brighton | Fast 24/7 Mobile", which
suggests the claim is templated across the site's ~90 suburb pages (sampled 2,
not verified site-wide).

## Why this blocks rather than warns

`approved/*.md` is not just a style reference. `wiki_rebuild.rebuild_corpus_operational_truth()`
parses it into `corpus_operational_truth.json` as the client's *operational truth*,
and `rebuild_voice_profile()` builds the voice anchor from the same files. The
writer-agent reads both. Ingesting these pages as-is would reintroduce the banned
claims as ground truth across all 41 new pages — cancelling the corrections.

## State

- 6 raw pages: `intake/upgrade-inbox/*.html`
- 6 extracted markdown: `intake/upgrade-inbox/extracted-md/`
- `approved/` deliberately does **not** exist — nothing has been ingested
- `corpus_operational_truth.json` is empty, as it should be

## Options for the analyst

1. **Scrub then ingest** — strip the offending sentences from the six extracts,
   ingest the remainder as voice corpus. Fastest. The voice survives; the false
   claims don't. Departs from "preserve voice corpus verbatim", so the edit gets
   recorded in the event log.
2. **Ingest the cleanest pages only** — `blog-are-smart-locks-worth-it` is the one
   file with zero hits on any banned pattern, and it is the closest topic match to
   the cluster. Narrow but clean voice base.
3. **Client fixes the site first** — the live pages advertise a service the client
   does not provide, which is a live commercial exposure independent of this
   project. Ingest afterwards from corrected copy.
4. **Skip the corpus** — proceed with no voice anchor. Generation still runs; the
   output will be competent but generic.

Resume with `/content:resume` once decided.
