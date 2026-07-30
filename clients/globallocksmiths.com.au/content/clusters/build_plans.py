"""Generate + lock the two cluster plans for globallocksmiths.com.au.

Runs the plugin's own `generate_cluster_plan` / `validate_plan` /
`render_plan_markdown` / `lock_plan`, supplying the LLM-authored synthesis (this
file) as the `synthesiser` callable.

Two deviations from a naive call, both deliberate:

1. `generate_cluster_plan` does not copy `client_data_signals` out of the synthesis
   into the plan dict, even though `render_plan_markdown`, `credibility_block_check`,
   `audit_gate_inputs` and the writer-agent all read it. It is injected here BEFORE
   `lock_plan` hashes, which the module's own comments confirm is hash-stable
   (canonical_json_bytes sorts keys). Injecting after the hash would break lock
   integrity.

2. `years_in_business` is NOT computed, though the cluster-plan prompt says to.
   The analyst resolved on 2026-07-28 that tenure ships as "since 2002" and never as
   a year-count, and removed `years_of_combined_experience` from the profile so the
   writer could not emit one. Computing it here would reintroduce exactly that.
   For the same reason `why_started` is not copied verbatim — its text contains
   "more than 25 years of hands-on experience".

Usage (CWD must be the client folder — generate_cluster_plan resolves the fact
ledger from Path(".")):
    PYTHONPATH="$PLUGIN_ROOT" python3 build_plans.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from scripts.cluster_planner import (
    generate_cluster_plan,
    lock_plan,
    render_plan_markdown,
    validate_plan,
)

CLIENT = Path(".").resolve()
HUB = "service-hubs"
SPOKE = "service-location-smart-lock-installation"

# Tokens the analyst ruled out. Passed to validate_plan as a self-check: the plan
# states availability positively ("Monday to Friday, 9am to 5pm") and never names
# these, so a clean validation proves no prohibited claim leaked into plan text.
BANNED = ["24/7", "emergency", "24 hours", "around the clock",
          # Elapsed-tenure phrasings. The analyst banned year-counts; these are
          # in the validator so a regression fails the build instead of needing
          # a manual grep.
          "25 years", "24 years", "over 20 years", "more than 25 years"]

# ---------------------------------------------------------------- signals ----
# Every value below is copied from client-profile.json. Keys whose value would be
# a guess are omitted rather than filled (prompt rule: never "founder_name": "unknown").
CLIENT_DATA_SIGNALS = {
    "business_name": "Global Locksmiths",
    "registered_name": "Global Locksmiths Pty Ltd",
    "founder_name": "Shane Tipping",
    "year_established": 2002,
    "tenure_phrasing": "since 2002",
    # Deliberately does NOT spell out an example year-count. The writer-agent reads
    # this block and pulls from it, so a banned client claim written here verbatim —
    # even as a "don't write this" example — puts the exact prohibited string in
    # front of the writer. Describe the shape, never instantiate it.
    "_tenure_note": (
        "Write tenure ONLY as the literal phrase in tenure_phrasing above. Never "
        "express tenure as an elapsed number of years, and never derive one by "
        "subtracting year_established from the current year. Analyst-resolved "
        "2026-07-28: a hardcoded elapsed count ships correct and silently goes "
        "stale, which is why years_of_combined_experience was removed from the "
        "profile entirely."
    ),
    "former_trading_name": "Newmans Locksmiths",
    "ABN": "43 969 968 576",
    "phone": "1300 333 565",
    "operating_hours": "Monday to Friday, 9am to 5pm",
    "operating_model": "mobile_service_area",
    "_premises_note": (
        "No premises anywhere — analyst-confirmed 2026-07-29. business_address is "
        "deliberately absent, not a gap. Never write 'based in <suburb>', 'our "
        "<suburb> branch', 'depot', 'showroom', or 'drop in'. The van comes to the "
        "customer."
    ),
    "team_size": "Shane Tipping plus one qualified locksmith",
    "client_count": "over 1,000 projects completed",
    "review_average": 5,
    "referral_rate_pct": 20,
    "repeat_customer_rate_pct": 75,
    "service_area": "Melbourne Metro and Geelong",
    "certifications": [
        "Master Locksmiths Association of Australasia (MLAA) accreditation",
        "Australian New Zealand Locksmiths Association (ANZLA) accreditation",
        "All locksmiths are fully licensed and insured in Victoria",
    ],
    "guarantees": [
        "Standard 12-month warranty on all work completed",
        "100% satisfaction guarantee",
        "Free, no-obligation quotes before any work begins",
    ],
    "insurance": "All work is fully insured",
    "customer_process": [
        "Customer contacts Global Locksmiths on 1300 333 565 or via the online enquiry form",
        "Free, no-obligation quote provided before any work begins",
        "Mobile locksmith attends the customer's address within the service area",
        "Work completed on site, backed by the 12-month workmanship warranty",
    ],
    "usps_verbatim": [
        "Previously trading as Newmans Locksmiths",
        "Proud members of both the Australian New Zealand Locksmiths Association (ANZLA) and the Master Locksmiths Association of Australasia (MLAA)",
        "Our technical and management staff are trained and qualified Master Locksmiths",
        "Fully licensed, insured, and accredited",
        "Standard 12-month warranty on all work completed",
        "100% satisfaction guarantee",
        "Free, no-obligation quotes",
        "5-star rated service trusted by thousands of satisfied customers",
        "1,000's projects completed",
        "Treating every customer, from domestic clients to high-profile individuals, with the same high standard of service",
    ],
    "admissible_hardware_vocabulary": {
        "_source": "research/geo-contamination-qa.md — replaces British terms that "
                   "contaminated the st-albans research (uPVC, anti-snap, Ultion, Nuki)",
        "lock_types": ["smart mortice lock", "smart deadbolt", "fire-rated smart lock for unit doors"],
        "incumbent_brands_a_retrofit_must_mate_with": ["Lockwood", "Lane", "Lemaar"],
    },
}

# Only ONE fact is `confirmed` in client-facts.json. metrics.percentage,
# social-proof.clients and service.duration are all `conflict` (social-proof.clients
# is extractor noise off the ABN/phone digits; service.duration=24 is the 24-hour
# claim leaking in). Mandating any of those would be the exact structural pressure
# that forces a writer to invent — so only the founding year is declared.
REQUIRES_FACTS = ["company.founding-year"]

# ------------------------------------------------------------ hub synthesis ---
HUB_SYNTHESIS = {
    "universal_required": [
        "What smart lock installation by a licensed locksmith actually involves end to end: assessing the existing door and hardware, confirming the chosen lock suits that door, fitting, and commissioning the lock with the customer before leaving.",
        "Which existing Australian door hardware a smart lock has to mate with — Lockwood, Lane and Lemaar locksets are the incumbents on Melbourne doors — and what a retrofit onto each practically involves.",
        "The door situations that change the job: aluminium-framed and glazed doors, apartment and common-property entrances, security screen doors, bifold and sliding doors, and doors with no existing deadbolt bore.",
        "Whether Global Locksmiths will fit a smart lock the customer has already bought, and what the customer should check before buying one.",
        "How pricing works: free, no-obligation quote before any work begins, quoted per door after the hardware and door are confirmed. State that pricing is provided on quote — do not publish a figure or a range.",
        "FULL credibility block (hub standard). A dedicated H2 that NAMES the business — e.g. 'About Global Locksmiths' or 'Global Locksmiths across Melbourne' — placed as section 2 or 3, after the lede. Populate from client_data_signals: founder Shane Tipping, operating since 2002, previously trading as Newmans Locksmiths, over 1,000 projects completed, MLAA and ANZLA accreditation, fully licensed and insured in Victoria, 12-month workmanship warranty, 100% satisfaction guarantee. Integrate each as proof of a specific claim, not as a list. Never title this section 'Why Choose Us' — the templating gate blocks that shape.",
        "Availability and how to book, stated positively and in the page's first half: Global Locksmiths operates Monday to Friday, 9am to 5pm, as a mobile service that travels to the customer's address across Melbourne Metro and Geelong. Booking is by phone on 1300 333 565 or the online enquiry form.",
        "What the 12-month workmanship warranty and 100% satisfaction guarantee actually cover on a smart lock installation.",
    ],
    "cluster_specific_required": [
        "This is the metro-wide PILLAR page for the 41-page smart lock set. It must frame smart lock installation as a Melbourne-wide mobile service and link down to the suburb pages, which are the only entries carrying suburb-level detail. Do not attempt suburb-specific claims here.",
        "Answer the commercial-intent questions the live SERP surfaces for 'smart lock installation melbourne' — this is the only entry in the whole project with measured search demand (90/mo, commercial intent, competition 0.93). Treat it as the page that has to convert comparison shoppers, not the page that has to rank a long tail.",
        "Include a section on choosing between smart lock types that a customer can act on — keypad, fingerprint, app/WiFi, and whether a mechanical key override remains — because 'which one do I commit to' recurs across the suburb research as the live decision point.",
        "Name the competitive reality honestly: dedicated smart-lock installers in Melbourne publish service areas concentrated in the bayside and inner south-east. Global Locksmiths is a licensed mobile locksmith covering Melbourne Metro and Geelong, which is the differentiator for customers outside that band. Frame as coverage, never as a claim about a named competitor.",
        "Disambiguation budget: if the page needs to separate a locksmith-fitted smart lock from a DIY retail purchase, give that section roughly 80-100 words. It is a deliberate play and must not swallow the page.",
    ],
    "per_entry_unique_angle": {
        "smart-lock-installation-melbourne": (
            "The metro-wide pillar and the only entry with measured demand. Its unique job is "
            "breadth and decision-making: it carries the full credibility block, the smart-lock "
            "type comparison, the retrofit-onto-Lockwood/Lane/Lemaar explanation, and the "
            "hub-to-spoke links out to all 40 suburb pages. Every suburb page defers to this "
            "page for the full credentials and the buying decision, and this page never claims "
            "suburb-level specifics."
        )
    },
    "execution_order_within_cluster": ["smart-lock-installation-melbourne"],
    "requires_facts": REQUIRES_FACTS,
    "client_data_signals": CLIENT_DATA_SIGNALS,
}

# ---------------------------------------------------------- spoke synthesis ---
# Each angle is grounded in that suburb's own suburb-data bundle. Angles
# differentiate by the DOOR SITUATION and BUYING BEHAVIOUR the local records
# actually evidence — never by topic exclusion, and never by a generic
# "X is in Melbourne's inner west" geography statement.
SPOKE_ANGLES = {
    "smart-lock-installation-altona": "Aluminium door frames with glazed side panels are the evidenced local door type, and the resident brief that surfaced expected drilling into that frame and a slim-profile lock. Lead on whether a slim smart lock suits an aluminium-framed glazed door and what drilling it honestly involves.",
    "smart-lock-installation-altona-north": "Same aluminium-and-glazing door reality as Altona, but the local brief additionally stipulated a licensed locksmith with prior experience of that specific model. Lead on why model-specific installation experience and a Victorian licence matter more than a generic lock-fitting quote.",
    "smart-lock-installation-ascot-vale": "Local records show doors carrying legacy Australian hardware rather than modern euro-cylinder profiles. Lead on retrofitting a smart lock onto an existing Lockwood/Lane-era lockset — whether it goes straight onto the current deadbolt or the door has to be re-prepped.",
    "smart-lock-installation-braybrook": "The live local demand is fit-only labour on hardware the customer already owns. Lead on the customer-supplied-lock path: what Global Locksmiths will and will not fit, and what to check on the box before buying.",
    "smart-lock-installation-brighton": "Bayside coverage is the live question here — the evidenced concern is confirming a Melbourne smart-lock installer actually travels to Brighton, because the dedicated specialists cluster their service areas rather than covering the whole metro. Lead on mobile coverage and the free quote before travel.",
    "smart-lock-installation-caroline-springs": "Records frame the area as spanning both modern and established homes, with customer-supplied hardware the live signal. Lead on how the same estate can need two different retrofit approaches depending on whether the door is a newer build or an older one.",
    "smart-lock-installation-deer-park": "Detached-dwelling hardware throughout, and the evidenced buyer behaviour is comparing quotes before committing. Lead on what a free, no-obligation quote covers and why a per-door quote after seeing the door beats a phone estimate.",
    "smart-lock-installation-docklands": "Filed by local records as inner-city rather than suburban housing, with customer-supplied online purchases the live signal. Lead on high-rise apartment entry doors: what an owners corporation controls, and fitting a lock the customer bought online.",
    "smart-lock-installation-essendon": "Apartment and mixed residential/commercial stock, and the evidenced decision point is which credential to commit to and whether a mechanical key override remains. Lead on choosing between keypad, fingerprint and app entry when a building also needs a fallback key.",
    "smart-lock-installation-flemington": "Multi-dwelling stock with shared access points, and the live concern is fitting a smart lock without giving up the cylinder already in the door. Lead on keeping existing cylinder access while adding smart entry.",
    "smart-lock-installation-footscray": "Local records evidence lever/latch hardware and traditional deadlocks being converted, with the live worry that a WiFi deadbolt fits but the door then will not close and lock properly. Lead on door alignment and latch engagement after a conversion.",
    "smart-lock-installation-hawthorn": "Mixed stock where apartments and units sit alongside houses, and the evidenced anxiety is irreversible door modification. Lead on what is reversible and what is permanent when a smart lock goes onto an existing door.",
    "smart-lock-installation-hoppers-crossing": "Detached-house hardware, and the live question is whether a retail smart lock already bought will fit the existing door. Lead on the pre-purchase fit check — backset, door thickness and existing bore — before the customer commits to hardware.",
    "smart-lock-installation-kensington": "The strongest permission story in the set: local records show contract locksmith work for owners corporations and real estate agents, fire-exit hardware alongside digital locks, and master key systems. Lead on WHO authorises a smart lock on a shared or compliance-controlled door, and how it joins an existing keying hierarchy.",
    "smart-lock-installation-kew": "Detached-house entrances, and the evidenced question is whether a quoted price includes the lock hardware or only the labour. Lead on separating hardware cost from installation labour in the free quote.",
    "smart-lock-installation-kingsville": "A mixed residential-plus-institutional profile locally, with the live concern being whether a smart lock ties into an existing keying or access-control regime rather than standing alone. Lead on integrating one smart lock into a wider key system.",
    "smart-lock-installation-maidstone": "The local job feed shows no single dominant door type and, critically, two of the three doors named will not take a standard smart deadbolt — a screen door over a slider and a glazed patio door. Lead on establishing whether the chosen lock can physically go on the door the customer actually has.",
    "smart-lock-installation-maribyrnong": "Records evidence existing residential doors being retrofitted rather than new installs, with customer-supplied hardware the live signal. Lead on the retrofit-onto-an-existing-door path and installing a lock the customer sourced themselves.",
    "smart-lock-installation-moonee-ponds": "Local records describe a split door stock rather than one dominant type, and the evidenced question is whether the smart lock can drop onto just the existing top lock instead of re-fitting the whole door. Lead on partial versus full lockset replacement.",
    "smart-lock-installation-newport": "The only suburb where local records describe doors that are not standard hinged single leaves — a bifold door with an old mortise lock, plus a named Eufy install where the customer wanted advice before buying. Lead on smart locks for bifold and non-standard doors, and pre-purchase advice.",
    "smart-lock-installation-point-cook": "Named master-planned estate housing, and the live question is whether the existing handle-and-lock set has to come out and what replaces it. Lead on what changes visually and functionally on a newer estate door.",
    "smart-lock-installation-port-melbourne": "The evidenced local record is a Bay Street apartment whose entry door cannot be locked from outside at all. Lead on apartment entry doors with interior-only locking, and what smart entry can and cannot solve there.",
    "smart-lock-installation-prahran": "Local job records are apartment and unit work, and the live question is whether a smart lock can go onto the deadlock already fitted rather than replacing the whole door hardware. Lead on working with the existing deadlock in a unit.",
    "smart-lock-installation-richmond": "Every Richmond door in the records is an existing door being retrofitted, and the two described are a 1960s apartment entry and a fire-rated entry door requiring a Yale Unity fire-rated lock. Lead on fire-rated and older apartment entry doors, and on avoiding a visibly re-worked cut-out.",
    "smart-lock-installation-seddon": "Records split on the state of existing hardware, with the live question being whether a smart lock can go on a door with no deadbolt bore at all and what that involves. Lead on doors that have never had a deadbolt.",
    "smart-lock-installation-south-melbourne": "Both local job signals are retrofits onto existing doors, and the evidenced concern is whether the installer is allowed to touch an apartment's main entry door. Lead on permission and building rules before hardware.",
    "smart-lock-installation-south-yarra": "Records evidence a split between apartment stock and standalone dwellings, with the live question being whether a smart lock retrofits onto the mechanical hardware already there or the whole lockset changes. Lead on the retrofit-versus-replace decision.",
    "smart-lock-installation-spotswood": "The local signal is a review of drilling work on an existing front door, and the evidenced worry is whether electronic entry means permanently drilling it. Lead on exactly what gets drilled, what is concealed by the new hardware, and what is permanent.",
    "smart-lock-installation-st-albans": "The clearest coverage story in the set: dedicated smart-lock installers publish service areas running bayside and inner south-east with no western suburb, while general mobile locksmiths do cover 3021. Lead on a licensed mobile locksmith actually travelling west, and on smart lock work being available here at all.",
    "smart-lock-installation-st-kilda": "Multi-unit rather than single-dwelling work, and the evidenced question is fitting a smart lock to an apartment complex entrance and integrating it with the existing master key system. Lead on complex entrances and master key integration.",
    "smart-lock-installation-sunshine": "The one local property record shows standalone housing with several external doors, and the live question is a main entry that already has or is about to get a security screen door. Lead on smart locks behind a security screen — reach, clearance and keypad access.",
    "smart-lock-installation-sunshine-west": "The evidenced local concern is whether new hardware will cover the holes left by the old lock or leave gaps needing filling. Lead on the cosmetic outcome of a swap: hole coverage, filling and what the door looks like afterwards.",
    "smart-lock-installation-tarneit": "Both local job records describe front doors not pre-prepared for smart hardware, making Tarneit a cutting-and-drilling market rather than a swap market. Lead on installing into an unprepared door, including customer-supplied hardware needing a hole made.",
    "smart-lock-installation-toorak": "Records evidence a split residential and commercial door stock, and the live decision is whether to go digital at all or stay mechanical. Lead on the honest case for staying mechanical, and when a smart lock genuinely earns its place.",
    "smart-lock-installation-truganina": "A residential-alongside-commercial-and-industrial property mix, with cost the dominant evidenced question. Lead on what drives the price of a smart lock installation across a house versus a commercial door, quoted per door.",
    "smart-lock-installation-werribee": "The local record names three doors where the door is wood and the frame differs, and the live question is whether an already-purchased smart lock will fit and be installed. Lead on multi-door jobs and matching one lock choice across doors that are not identical.",
    "smart-lock-installation-williams-landing": "Street-facing detached houses with a single main entry door in a newer estate, and the live question is simply whether a smart lock will fit the door they already have. Lead on the straightforward single-front-door install and what confirms fit.",
    "smart-lock-installation-williamstown": "Records point to two distinct door situations rather than one, with the live question being retrofitting older original door hardware without changing how the door behaves. Lead on preserving the look and action of an original door.",
    "smart-lock-installation-wyndham-vale": "New detached housing in growth-corridor estates, and the evidenced demand is fit-only labour on customer-supplied retail hardware. Lead on the fit-only service for new-estate front doors.",
    "smart-lock-installation-yarraville": "The dominant evidenced concern is not knowing what a smart lock install should cost in the first place. Lead on making the free, no-obligation quote genuinely useful — what is assessed, what is quoted per door, and why a figure cannot be given sight-unseen.",
}

SPOKE_SYNTHESIS = {
    "universal_required": [
        "What smart lock installation on this suburb's doors actually involves: confirming the existing door and hardware suit the chosen lock, fitting it, and commissioning it with the customer before leaving.",
        "Whether a smart lock will fit the customer's existing door — the single recurring question across every suburb's research. Cover existing lockset, door material and thickness, and what happens when the door is not pre-prepared.",
        "Whether Global Locksmiths will install a smart lock the customer has already bought, and what to check before buying one.",
        "How to get a price: a free, no-obligation quote before any work begins, quoted per door once the door and hardware are confirmed. State pricing is on quote — never publish a figure or a range.",
        "LEAN credibility block (suburb-page standard, v0.14.0). An H2 that NAMES the business — e.g. 'About Global Locksmiths' — carrying ONLY the trust floor: founder Shane Tipping, operating since 2002, over 1,000 projects completed, and fully licensed and insured in Victoria. Then link to the Melbourne smart lock installation hub for the full credentials. Do NOT repeat the full accreditation, warranty, guarantee and review set on every suburb page — the same eight facts across forty pages reads as templated boilerplate to a human even when it clears the coded gates. Never title this section 'Why Choose Us'. Each page must phrase this block differently.",
        "Availability and booking, stated positively and in the page's first half: Global Locksmiths is a mobile locksmith operating Monday to Friday, 9am to 5pm, travelling to the customer's address in this suburb. Book on 1300 333 565 or the online enquiry form.",
        "A link up to the metro-wide smart lock installation hub page, and the 12-month workmanship warranty stated once.",
    ],
    "cluster_specific_required": [
        "The suburb name appears in the title tag, the H1, and the first paragraph — and reads as natural language a customer would say aloud, never an inverted keyword construction.",
        "The page's local proof must come from THAT SUBURB's own bundle in `clusters/service-location-smart-lock-installation/research/suburb-data/<suburb>-smart-lock-installation.json`. Use `building_stock`, `demographic_skew`, `council_notes` and `common_concerns`. Where a field reads 'Insufficient local data', write nothing in its place — do not substitute general knowledge about the suburb. Several bundles are deliberately thin because wrong-place records were discarded; a shorter honest page is the required outcome.",
        "Answer the door-situation question named in this entry's per_entry_unique_angle as a substantive section, not a passing mention. That question is what makes this page different from the other 39.",
        "Where the entry's research bundle has PAA questions, answer them in the FAQ. Do NOT use PAA answers sourced from checkatrade.com — that is a UK trade directory whose pricing is in pounds and whose install timings do not describe Australian practice. It survived Melbourne-scoped SERP calls on several entries and reached at least one PAA answer.",
        "Use Australian door and hardware vocabulary only: smart mortice lock, smart deadbolt, fire-rated smart lock for unit doors, and the incumbent brands a retrofit mates with (Lockwood, Lane, Lemaar). Never use uPVC or anti-snap — those are British door conventions that entered the raw research via UK homonym results and would read as obviously foreign here.",
        "Never state or imply a physical presence in the suburb. Global Locksmiths is a mobile service with no premises anywhere: no 'based in', no branch, depot or showroom, no invitation to drop in. The van travels to the customer.",
    ],
    "per_entry_unique_angle": SPOKE_ANGLES,
    "execution_order_within_cluster": [
        # Archetypal first: richest, most specific bundles set the pattern the rest
        # differentiate from. Thin-bundle suburbs run last so the corpus is already
        # dense by the time the writer has least local material to work with.
        "smart-lock-installation-kensington",
        "smart-lock-installation-maidstone",
        "smart-lock-installation-richmond",
        "smart-lock-installation-newport",
        "smart-lock-installation-tarneit",
        "smart-lock-installation-sunshine",
        "smart-lock-installation-port-melbourne",
        "smart-lock-installation-st-kilda",
        "smart-lock-installation-flemington",
        "smart-lock-installation-essendon",
        "smart-lock-installation-docklands",
        "smart-lock-installation-prahran",
        "smart-lock-installation-south-melbourne",
        "smart-lock-installation-south-yarra",
        "smart-lock-installation-hawthorn",
        "smart-lock-installation-kingsville",
        "smart-lock-installation-footscray",
        "smart-lock-installation-seddon",
        "smart-lock-installation-spotswood",
        "smart-lock-installation-moonee-ponds",
        "smart-lock-installation-ascot-vale",
        "smart-lock-installation-maribyrnong",
        "smart-lock-installation-williamstown",
        "smart-lock-installation-altona",
        "smart-lock-installation-altona-north",
        "smart-lock-installation-werribee",
        "smart-lock-installation-hoppers-crossing",
        "smart-lock-installation-point-cook",
        "smart-lock-installation-williams-landing",
        "smart-lock-installation-wyndham-vale",
        "smart-lock-installation-truganina",
        "smart-lock-installation-caroline-springs",
        "smart-lock-installation-braybrook",
        "smart-lock-installation-sunshine-west",
        "smart-lock-installation-deer-park",
        "smart-lock-installation-toorak",
        "smart-lock-installation-kew",
        "smart-lock-installation-yarraville",
        "smart-lock-installation-brighton",
        "smart-lock-installation-st-albans",
    ],
    "requires_facts": REQUIRES_FACTS,
    "client_data_signals": CLIENT_DATA_SIGNALS,
}


def load_context(cluster_id: str, prior_plans: list[dict]) -> dict:
    entries: dict[str, dict] = {}
    for p in sorted((CLIENT / "entries").glob("*.json")):
        e = json.loads(p.read_text(encoding="utf-8"))
        if e.get("cluster_id") == cluster_id:
            entries[e["entry_id"]] = e

    research: dict[str, dict] = {}
    word_counts: dict[str, dict] = {}
    rdir = CLIENT / "clusters" / cluster_id / "research"
    for eid in entries:
        rp = rdir / f"keyword-{eid}.json"
        if rp.exists():
            bundle = json.loads(rp.read_text(encoding="utf-8"))
            research[eid] = bundle
            wc = bundle.get("word_count_recommendation")
            word_counts[eid] = wc if isinstance(wc, dict) else {"recommended": 1200, "source": "default"}

    return {
        "cluster_id": cluster_id,
        "entries": entries,
        "research": research,
        "word_counts": word_counts,
        "voice_profile": (CLIENT / "voice-profile.md").read_text(encoding="utf-8"),
        "client_context": (CLIENT / "client-context.md").read_text(encoding="utf-8"),
        "prior_plans": prior_plans,
        "client_dir": str(CLIENT),
    }


def build(cluster_id: str, synthesis: dict, prior_plans: list[dict]) -> dict:
    ctx = load_context(cluster_id, prior_plans)
    print(f"\n=== {cluster_id} ===")
    print(f"  entries: {len(ctx['entries'])}  research bundles: {len(ctx['research'])}")
    if len(ctx["research"]) != len(ctx["entries"]):
        missing = sorted(set(ctx["entries"]) - set(ctx["research"]))
        print(f"  WARNING missing research for: {missing}", file=sys.stderr)

    plan = generate_cluster_plan(ctx, lambda _inp: synthesis)

    # Deviation 1 (see module docstring): carry client_data_signals into the plan
    # BEFORE lock_plan hashes it. generate_cluster_plan drops it despite four
    # downstream consumers reading it.
    if "client_data_signals" not in plan and synthesis.get("client_data_signals"):
        plan["client_data_signals"] = synthesis["client_data_signals"]
        print("  injected client_data_signals (generate_cluster_plan does not carry it)")

    ledger = json.loads((CLIENT / "client-facts.json").read_text(encoding="utf-8"))
    validate_plan(
        plan,
        banned_terms=BANNED,
        cluster_total_entries=len(ctx["entries"]),
        fact_ledger=ledger,
    )
    print(f"  validate_plan: PASS (banned-term self-check clean: {BANNED})")

    (CLIENT / "clusters" / cluster_id / "plan.md").write_text(
        render_plan_markdown(plan), encoding="utf-8")
    print(f"  wrote clusters/{cluster_id}/plan.md")

    locked = lock_plan(plan, CLIENT, cluster_id)
    print(f"  locked: {locked.get('lock_sha', '')[:16]}…")
    return locked


def main() -> int:
    hub = build(HUB, HUB_SYNTHESIS, prior_plans=[])
    # Hub planned first so the spoke cluster can see the angles it already owns.
    spoke = build(SPOKE, SPOKE_SYNTHESIS, prior_plans=[hub])
    print(f"\nPlans generated and locked: {HUB} (1 entry), {SPOKE} (40 entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
