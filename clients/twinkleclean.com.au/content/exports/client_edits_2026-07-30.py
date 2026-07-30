"""Client-requested edits, 30 Jul 2026 (3 changes, applied surgically).

1. Remove "every cleaner communicates clearly in English" claims ->
   "our management team provides clear and responsive communication".
2. Carpet hub: remove "Most of this work is residential." sentence so
   residential and commercial carpet cleaning carry equal weight.
3. Qualify truck-mounted carpet cleaning as available for sites with
   suitable access (apartments / high-rise may not allow truck access).

Each replacement is exact-match and must occur exactly once per file copy,
otherwise the script aborts without writing anything. Applied to all four
copies: exports/source-md/, content/<e>/generated.md, content/<e>/approved.md,
approved/<e>.md.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../content/exports
CONTENT = HERE.parent                            # .../content

MGMT = "our management team provides clear and responsive communication"

# entry_id -> list of (old, new)
EDITS = {
    # ---------- Change 1: English claim ----------
    "homepage": [
        ("Our cleaners are police-checked, trained in workplace and chemical safety as well as cleaning technique, and communicate clearly in English.",
         f"Our cleaners are police-checked and trained in workplace and chemical safety as well as cleaning technique, and {MGMT}."),
        ("Yes. Every cleaner is police-checked, trained in workplace and chemical safety, and communicates clearly in English.",
         f"Yes. Every cleaner is police-checked and trained in workplace and chemical safety, and {MGMT}."),
    ],
    "commercial-cleaning-bayswater": [
        ("- Trained in workplace and chemical safety\n- Communicates clearly in English\n\nWe also hold $20 million public liability insurance plus WorkCover.",
         f"- Trained in workplace and chemical safety\n\nOur management team provides clear and responsive communication, and we also hold $20 million public liability insurance plus WorkCover."),
    ],
    "commercial-cleaning-camberwell": [
        ("Every cleaner is police-checked, trained in workplace and chemical safety, and communicates clearly in English, and we hold $20 million public liability insurance plus WorkCover.",
         f"Every cleaner is police-checked and trained in workplace and chemical safety, {MGMT}, and we hold $20 million public liability insurance plus WorkCover."),
    ],
    "commercial-cleaning-cheltenham": [
        ("Every cleaner is police-checked, trained in workplace and chemical safety and communicates clearly in English, which matters on an industrial site.",
         f"Every cleaner is police-checked and trained in workplace and chemical safety, and {MGMT}, which matters on an industrial site."),
    ],
    "commercial-cleaning-croydon": [
        ("Our cleaners are police-checked, trained in workplace and chemical safety and communicate clearly in English, which matters on a working site.",
         f"Our cleaners are police-checked and trained in workplace and chemical safety, and {MGMT}, which matters on a working site."),
    ],
    "commercial-cleaning-dandenong": [
        ("Our cleaners are trained in workplace and chemical safety and in professional cleaning techniques, and they communicate clearly in English.",
         f"Our cleaners are trained in workplace and chemical safety and in professional cleaning techniques, and {MGMT}."),
    ],
    "commercial-cleaning-docklands": [
        ("Our cleaners are police-checked, trained in workplace and chemical safety and communicate clearly in English, which matters when a building manager or concierge needs to speak with someone on site at 9pm.",
         f"Our cleaners are police-checked and trained in workplace and chemical safety, and {MGMT}, which matters when a building manager or concierge needs to reach someone at 9pm."),
    ],
    "commercial-cleaning-hawthorn": [
        ("Our people are police-checked, trained in workplace and chemical safety, and communicate clearly in English, which matters when a building manager wants a straight answer at 9pm.",
         f"Our people are police-checked and trained in workplace and chemical safety, and {MGMT}, which matters when a building manager wants a straight answer at 9pm."),
    ],
    "commercial-cleaning-noble-park": [
        ("Our cleaners communicate clearly in English, and if something needs to be explained twice, it gets explained twice.",
         "Our management team provides clear and responsive communication, and if something needs to be explained twice, it gets explained twice."),
    ],
    "commercial-cleaning-ringwood": [
        ("Yes. Our team is trained in workplace and chemical safety as well as professional cleaning techniques, and communicates clearly in English.",
         f"Yes. Our cleaners are trained in workplace and chemical safety as well as professional cleaning techniques, and {MGMT}."),
    ],
    "commercial-cleaning-scoresby": [
        ("Our cleaners are police-checked, trained in workplace and chemical safety, and communicate clearly in English, which is what a facilities manager handing over access credentials wants to hear.",
         f"Our cleaners are police-checked and trained in workplace and chemical safety, and {MGMT}, which is what a facilities manager handing over access credentials wants to hear."),
    ],
    "commercial-cleaning-southbank": [
        ("Cleaners are police-checked, trained in workplace and chemical safety, and communicate clearly in English, which matters when they hold building credentials for a secured floor.",
         f"Cleaners are police-checked and trained in workplace and chemical safety, and {MGMT}, which matters when cleaners hold building credentials for a secured floor."),
    ],
    "commercial-cleaning-wantirna": [
        ("Every cleaner is police-checked and trained in workplace and chemical safety, with strong English communication, and the business carries $20 million public liability insurance plus WorkCover.",
         f"Every cleaner is police-checked and trained in workplace and chemical safety, {MGMT}, and the business carries $20 million public liability insurance plus WorkCover."),
    ],
    "commercial-cleaning-blackburn": [
        # near-variant: same per-cleaner claim without the word "English"
        ("Ours are police-checked, trained in workplace and chemical safety, and communicate clearly.",
         f"Ours are police-checked and trained in workplace and chemical safety, and {MGMT}."),
    ],
    "carpet-cleaning-noble-park": [
        ("If English is a second language at home, you will still get a friendly cleaner who explains the job in simple terms before we start.",
         "If English is a second language at home, you will still get plain, jargon-free advice with the job explained in simple terms before we start."),
        ("an honest quote, no jargon, and a cleaner who explains the job in simple terms before starting, whatever language is spoken at home.",
         "an honest quote, no jargon, and the job explained in simple terms before starting, whatever language is spoken at home."),
    ],
    # ---------- Change 2: carpet hub residential sentence ----------
    # ---------- Change 3: truck-mounted suitability qualifier ----------
    "carpet-cleaning": [
        ("Most of this work is residential. We clean carpet in houses, units and apartments",
         "We clean carpet in houses, units and apartments"),
        ("Our core process uses truck-mounted hot water extraction, often called steam cleaning, which flushes dirt and residue out of the pile and lifts it away with powerful suction.",
         "Our core process uses truck-mounted hot water extraction, often called steam cleaning, which flushes dirt and residue out of the pile and lifts it away with powerful suction. Truck-mounted cleaning is available for sites with suitable access, as truck access may not be possible for every apartment or high-rise property."),
    ],
    "carpet-cleaning-moorabbin": [
        ("which flushes dirt out of the pile and draws the moisture back out, so carpet is left damp rather than soaked.",
         "which flushes dirt out of the pile and draws the moisture back out, so carpet is left damp rather than soaked. Truck-mounted cleaning is available where site access allows."),
    ],
    "carpet-cleaning-dandenong": [
        ("which flushes dirt out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked.",
         "which flushes dirt out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked. The truck-mounted setup is available for sites with suitable access."),
    ],
    "carpet-cleaning-bentleigh": [
        ("which flushes dirt and residue out of the pile and then draws the moisture back out, so the carpet is left damp rather than soaked.",
         "which flushes dirt and residue out of the pile and then draws the moisture back out, so the carpet is left damp rather than soaked. Truck-mounted cleaning is available where the site has suitable access."),
    ],
    "carpet-cleaning-oakleigh": [
        ("which flushes dirt out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked.",
         "which flushes dirt out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked. Truck-mounted cleaning is available where access suits it."),
    ],
    "carpet-cleaning-noble-park-truck": [],  # placeholder, real edit below
    "carpet-cleaning-ringwood": [
        ("It flushes dirt and residue out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked.",
         "It flushes dirt and residue out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked. The truck-mounted setup is available where site access allows."),
    ],
    "carpet-cleaning-glen-waverley": [
        ("which flushes soil out of the pile and draws the moisture back out, leaving the carpet damp instead of soaked.",
         "which flushes soil out of the pile and draws the moisture back out, leaving the carpet damp instead of soaked. Truck-mounted cleaning is available where the property has suitable access."),
    ],
    "carpet-cleaning-box-hill": [
        ("which pushes hot water and solution deep into the pile and then vacuums the loosened dirt and moisture straight back out, so carpet is left damp rather than soaked.",
         "which pushes hot water and solution deep into the pile and then vacuums the loosened dirt and moisture straight back out, so carpet is left damp rather than soaked. Truck-mounted cleaning is available for sites with suitable access, though truck access may not be possible for every apartment or high-rise building."),
    ],
    "carpet-cleaning-bayswater": [
        ("It drives hot water into the carpet, loosens the soil settled at the bottom of the pile, and draws the moisture back out, so the carpet is left damp rather than wet.",
         "It drives hot water into the carpet, loosens the soil settled at the bottom of the pile, and draws the moisture back out, so the carpet is left damp rather than wet. Truck-mounted cleaning is available where site access suits it."),
    ],
    "carpet-cleaning-rowville": [
        ("which flushes dirt out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked. For the full detail",
         "which flushes dirt out of the pile and draws the moisture back out, so the carpet is left damp rather than soaked. Truck-mounted cleaning is available where site access allows. For the full detail"),
    ],
    "carpet-cleaning-croydon": [
        ("which flushes dirt out of the pile and pulls the moisture back out, so carpet is left damp rather than soaked.",
         "which flushes dirt out of the pile and pulls the moisture back out, so carpet is left damp rather than soaked. The truck-mounted setup is available where the site has suitable access."),
    ],
    "carpet-cleaning-richmond": [
        ("which flushes soil out of the pile and draws the moisture back with strong suction, so carpet is left damp rather than soaked.",
         "which flushes soil out of the pile and draws the moisture back with strong suction, so carpet is left damp rather than soaked. Truck-mounted cleaning is available where building access suits it."),
    ],
    "carpet-cleaning-cheltenham": [
        ("which drives heated water and solution into the pile then draws it straight back out, so carpet is left damp rather than saturated.",
         "which drives heated water and solution into the pile then draws it straight back out, so carpet is left damp rather than saturated. Truck-mounted cleaning is available for sites with suitable access."),
    ],
}

# noble park carpet: truck edit goes on the same entry as the English edits
EDITS["carpet-cleaning-noble-park"].append(
    ("which drives hot water and solution into the pile then vacuums the loosened dirt and moisture straight back out, leaving the carpet damp rather than soaked.",
     "which drives hot water and solution into the pile then vacuums the loosened dirt and moisture straight back out, leaving the carpet damp rather than soaked. Truck-mounted cleaning is available for sites with suitable access.")
)
del EDITS["carpet-cleaning-noble-park-truck"]


def copies(entry):
    return [
        HERE / "source-md" / f"{entry}.md",
        CONTENT / "content" / entry / "generated.md",
        CONTENT / "content" / entry / "approved.md",
        CONTENT / "approved" / f"{entry}.md",
    ]


def main():
    # Phase 1: validate every replacement in every copy before touching anything
    problems = []
    for entry, pairs in EDITS.items():
        for path in copies(entry):
            if not path.exists():
                problems.append(f"MISSING FILE: {path}")
                continue
            text = path.read_text()
            for old, _ in pairs:
                n = text.count(old)
                if n != 1:
                    problems.append(f"{path}: expected 1 occurrence, found {n}: {old[:70]}...")
    if problems:
        print("ABORT - nothing written:")
        for p in problems:
            print(" ", p)
        raise SystemExit(1)

    # Phase 2: apply
    touched = 0
    for entry, pairs in EDITS.items():
        for path in copies(entry):
            text = path.read_text()
            for old, new in pairs:
                text = text.replace(old, new)
            path.write_text(text)
            touched += 1
    print(f"OK: {sum(len(p) for p in EDITS.values())} replacements across "
          f"{len(EDITS)} entries, {touched} file copies updated")


if __name__ == "__main__":
    main()
