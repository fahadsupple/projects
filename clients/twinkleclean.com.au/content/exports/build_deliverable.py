"""Driver: assemble the 63-page Twinkle Clean deliverable .docx.

Source of truth:
  - Page order + meta (URL, keywords, meta title/description) -> meta.json
  - Per-page body markdown            -> source-md/<entry_id>.md

The two service-hub files in source-md/ have had their suburb internal-link
sections removed, so this reproduces the client-approved doc exactly (prose,
FAQs, CTAs and meta identical; no suburb-link lists on the hubs).

Usage:  python3 build_deliverable.py            # -> twinkleclean-content-63-pages.docx
        python3 build_deliverable.py OUT.docx   # custom output path
"""
import json
import sys
from pathlib import Path

import build_docx

HERE = Path(__file__).resolve().parent
META = HERE / "meta.json"
SRC = HERE / "source-md"
DEFAULT_OUT = HERE / "twinkleclean-content-63-pages.docx"


def load_entries():
    meta = json.loads(META.read_text())
    meta.sort(key=lambda m: m["page_no"])
    entries = []
    for m in meta:
        md_path = SRC / f"{m['entry_id']}.md"
        if not md_path.exists():
            raise FileNotFoundError(f"missing markdown for {m['entry_id']}: {md_path}")
        entries.append((m["page_no"], md_path.read_text(), m))
    return entries


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    entries = load_entries()
    if len(entries) != 63:
        raise SystemExit(f"expected 63 pages, got {len(entries)}")
    build_docx.build(entries, str(out))
    print(f"wrote {out} ({len(entries)} pages)")


if __name__ == "__main__":
    main()
