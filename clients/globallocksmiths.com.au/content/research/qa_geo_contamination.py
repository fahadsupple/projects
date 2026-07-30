"""Geo-contamination QA over the collected research fixtures.

This project's 41 target keywords are bare "smart lock installation <suburb>" strings
with no city qualifier, and the suburb names collide with places outside Melbourne.
Three DISTINCT failure modes were confirmed live on 2026-07-30, and only the first is
fixed by the SERP location parameter:

1. INTERNATIONAL homonym — Brighton/Sussex, Maidstone/Kent, St Albans/Herts.
   Melbourne city scoping removed most of it, but `checkatrade.com` (UK trade directory,
   GBP pricing) survived scoping on multiple entries.
2. INTERSTATE homonym — "sunshine" resolved largely to Sunshine Coast QLD: 6 of 9
   organic results were QLD/Brisbane businesses on (07) numbers, and Google's own
   related_searches echoed "Sunshine Coast". City scoping CANNOT fix this, because the
   competing entity is a stronger national one.
3. AI-probe country ceiling — `ai_optimization_chat_gpt_scraper` accepts only a
   country-level location, so it cannot be city-scoped at all. Maidstone resolved
   entirely as Kent UK (GBP pricing, four .co.uk brands, both citations UK).

None of these are visible to the plugin's own completeness manifest, which only records
whether a fixture FILE exists. A contaminated fixture is present, well-formed, and wrong.

The point of this pass is that a downstream planner or writer must never take a
contaminated fixture's prices, competitors or citations as Melbourne ground truth.

Usage:
    python3 qa_geo_contamination.py <client_dir> [--json <out_path>]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SERVICE_PREFIX = "smart-lock-installation-"

INTL = {
    "gbp": re.compile(r"£|\bGBP\b"),
    "uk_tld": re.compile(r"\.co\.uk\b|\.org\.uk\b|\.uk\b", re.I),
    "checkatrade": re.compile(r"checkatrade", re.I),
    "uk_place": re.compile(r"\b(Kent|Sussex|Hertfordshire|Hove|Surrey|Essex|"
                           r"Yorkshire|Wales|United Kingdom)\b"),
}
# Australian-but-wrong-city. Deliberately excludes bare "Melbourne"/"VIC".
INTERSTATE = {
    "qld": re.compile(r"\b(Sunshine Coast|Brisbane|Queensland|QLD|Gold Coast|"
                      r"Hinterland)\b", re.I),
    "nsw": re.compile(r"\b(Sydney|New South Wales|NSW)\b", re.I),
    "wa": re.compile(r"\b(Perth|Western Australia)\b", re.I),
    "sa_other": re.compile(r"\b(Adelaide|Darwin|Hobart|Canberra)\b", re.I),
    "phone_07": re.compile(r"\(07\)|\+61 ?7 "),
    "phone_02": re.compile(r"\(02\)|\+61 ?2 "),
    "phone_08": re.compile(r"\(08\)|\+61 ?8 "),
}
VIC = re.compile(r"\b(Melbourne|Victoria|VIC)\b", re.I)


def entry_name(path: Path, prefix: str) -> str:
    return path.name[len(prefix):].replace(SERVICE_PREFIX, "").replace(".json", "")


def serp_domains(data: dict) -> tuple[list[str], list[str]]:
    """Return (organic_domains, local_pack_domains)."""
    items = data.get("items") or []
    org = [i.get("domain") or "" for i in items if i.get("type") == "organic"]
    lp = [i.get("domain") or "" for i in items if i.get("type") == "local_pack"]
    return [d for d in org if d], [d for d in lp if d]


def hits(text: str, table: dict) -> dict:
    return {k: len(rx.findall(text)) for k, rx in table.items() if rx.findall(text)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("client_dir")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    raw = Path(args.client_dir) / "research" / "raw"
    report: dict[str, dict] = {}

    for serp in sorted(raw.glob(f"serp-organic-{SERVICE_PREFIX}*.json")):
        name = entry_name(serp, "serp-organic-")
        text = serp.read_text(encoding="utf-8", errors="replace")
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            report[name] = {"error": "serp fixture unparseable"}
            continue

        org, lp = serp_domains(data)
        non_au_org = [d for d in org if not d.endswith(".au")]
        uk_org = [d for d in org if re.search(r"\.uk$", d, re.I) or "checkatrade" in d.lower()]

        rec: dict = {
            "serp": {
                "organic": len(org),
                "local_pack": len(lp),
                "local_pack_all_au": all(d.endswith(".au") for d in lp) if lp else None,
                "non_au_organic": non_au_org,
                "uk_organic": uk_org,
                "intl_signals": hits(text, INTL),
                "interstate_signals": hits(text, INTERSTATE),
                "vic_mentions": len(VIC.findall(text)),
            }
        }

        ai = raw / f"ai-overview-{SERVICE_PREFIX}{name}.json"
        if ai.exists():
            atext = ai.read_text(encoding="utf-8", errors="replace")
            ai_intl = hits(atext, INTL)
            ai_inter = hits(atext, INTERSTATE)
            ai_vic = len(VIC.findall(atext))
            intl_w = sum(ai_intl.values())
            rec["ai"] = {
                "intl_signals": ai_intl,
                "interstate_signals": ai_inter,
                "vic_mentions": ai_vic,
                # GBP pricing plus UK domains, outweighing VIC mentions, is the
                # Maidstone signature: the engine answered about the wrong country.
                "verdict": ("FOREIGN" if intl_w >= 3 and intl_w > ai_vic
                            else "MIXED" if intl_w >= 3 else "ok"),
            }
        else:
            rec["ai"] = {"verdict": "MISSING"}

        # Overall severity for the analyst.
        s = rec["serp"]
        interstate_w = sum(s["interstate_signals"].values())
        flags = []
        if s["uk_organic"]:
            flags.append("intl-organic")
        if s["intl_signals"].get("gbp"):
            flags.append("gbp-pricing")
        if interstate_w >= 6 and interstate_w > s["vic_mentions"]:
            flags.append("interstate-majority")
        elif interstate_w >= 3:
            flags.append("interstate-present")
        if rec["ai"]["verdict"] in ("FOREIGN", "MIXED"):
            flags.append(f"ai-{rec['ai']['verdict'].lower()}")
        rec["flags"] = flags
        report[name] = rec

    # ---- print ----
    print(f"{'entry':<24} {'org':>3} {'lp':>3} {'ai':<8} flags")
    clean = 0
    for name, rec in report.items():
        if "error" in rec:
            print(f"{name:<24} {'ERR':>3} {'-':>3} {'-':<8} {rec['error']}")
            continue
        s = rec["serp"]
        f = ", ".join(rec["flags"]) or "-"
        if not rec["flags"]:
            clean += 1
        print(f"{name:<24} {s['organic']:>3} {s['local_pack']:>3} "
              f"{rec['ai']['verdict']:<8} {f}")

    flagged = [(n, r) for n, r in report.items() if r.get("flags")]
    print(f"\n{len(report)} entries scanned — {clean} clean, {len(flagged)} flagged")

    if flagged:
        print("\n--- Detail: do NOT use these as Melbourne ground truth ---")
        for name, rec in flagged:
            print(f"\n{name}:  {', '.join(rec['flags'])}")
            s = rec["serp"]
            if s["uk_organic"]:
                print(f"    UK organic: {', '.join(s['uk_organic'])}")
            if s["interstate_signals"]:
                print(f"    interstate: {s['interstate_signals']} "
                      f"(vs {s['vic_mentions']} VIC mentions)")
            if rec["ai"]["verdict"] in ("FOREIGN", "MIXED"):
                print(f"    ai-probe {rec['ai']['verdict']}: "
                      f"{rec['ai']['intl_signals']} vs {rec['ai']['vic_mentions']} VIC")

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\nwrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
