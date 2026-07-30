"""Driver for the suburb-service leg of /content:research (globallocksmiths.com.au).

Assembles `clusters/<cluster_id>/research/suburb-data/<suburb>-<service>.json`
bundles by calling the plugin's own library function
`scripts.suburb_service_research.research_suburb_service()`.

Division of labour (why this script exists):
- The Brave MCP call and the Claude synthesis can only be done by an agent.
  Agents write two files per pair:
    research/raw/brave-local-<suburb>-<service-slug>.json   (verbatim MCP response)
    research/raw/_synthesis/<suburb>-<service-slug>.json    (synthesis dict, 5 keys)
- This script injects those as the library's `provider` and `synthesiser`, so the
  bundle shape and `operating_model` carry-through stay the plugin's contract,
  not a hand-rolled reimplementation.

Usage:
    PYTHONPATH="$PLUGIN_ROOT" python3 run_suburb_bundles.py <client_dir> <cluster_id> [--service "smart lock installation"]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts.raw_fixture_paths import slugify_fixture_key
from scripts.research_providers import FixtureDataProvider
from scripts.suburb_service_research import research_suburb_service

REQUIRED_PHYSICAL_KEYS = (
    "climate_context",
    "building_stock",
    "council_notes",
    "demographic_skew",
    "common_concerns",
)


class BraveNoticeSalvagingProvider(FixtureDataProvider):
    """FixtureDataProvider whose `fetch_brave_local` can read THIS account's shape.

    Plugin defect (v0.17.0, confirmed live 2026-07-30): when the Brave key lacks the
    Pro local-search plan, the MCP response is a prose notice IMMEDIATELY followed by
    concatenated JSON objects on the SAME line:

        No location data was returned. ... Falling back to general web search.{"url":…}{"url":…}

    `research_providers._coerce_json_stream` has an NDJSON-plus-notice-line branch, but
    it splits on newlines — so a notice that shares its line with the payload defeats it,
    the whole-text `raw_decode` also fails on the leading prose, and `fetch_brave_local`
    falls back to `{"query":…, "results": []}`.

    The consequence is silent and severe: every bundle gets `local_signals: []` while its
    `synthesis` is fully populated, so the evidence trail for each claim disappears while
    the bundle still looks valid. Fixed here rather than by editing the installed plugin.
    """

    def fetch_brave_local(self, query: str) -> dict:
        data = super().fetch_brave_local(query)
        if data.get("results"):
            return data

        path = self._dir / f"brave-local-{slugify_fixture_key(query)}.json"
        if not path.exists():
            return data

        text = path.read_text(encoding="utf-8", errors="replace")
        start = text.find("{")
        if start == -1:
            return data

        decoder = json.JSONDecoder()
        records: list[dict] = []
        idx = start
        while idx < len(text):
            try:
                obj, end = decoder.raw_decode(text, idx)
            except ValueError:
                nxt = text.find("{", idx + 1)
                if nxt == -1:
                    break
                idx = nxt
                continue
            if isinstance(obj, dict):
                records.append(obj)
            idx = end
            while idx < len(text) and text[idx] in " \t\r\n,":
                idx += 1

        if not records:
            return data
        return {"query": query, "fallback_to_web": True, "results": records}


def load_operating_model(client_dir: Path) -> str | None:
    profile = json.loads((client_dir / "client-profile.json").read_text())
    return profile.get("operating_model")


def suburbs_for_cluster(client_dir: Path, cluster_id: str, service: str) -> list[tuple[str, str]]:
    """Derive (suburb, entry_slug) pairs from the cluster's entry files.

    The suburb is taken from the entry's primary_keyword by stripping the
    service prefix — the keyword is the authoritative per-page target, so the
    suburb string used for research matches exactly what the page targets.
    """
    pairs: list[tuple[str, str]] = []
    for path in sorted((client_dir / "entries").glob("*.json")):
        entry = json.loads(path.read_text())
        if entry.get("cluster_id") != cluster_id:
            continue
        keyword = (entry.get("primary_keyword") or "").strip().lower()
        if not keyword.startswith(service.lower()):
            print(f"SKIP {path.name}: primary_keyword {keyword!r} does not start with service "
                  f"{service!r} — cannot derive suburb without guessing", file=sys.stderr)
            continue
        suburb = keyword[len(service):].strip()
        if not suburb:
            print(f"SKIP {path.name}: keyword is the bare service, no suburb component",
                  file=sys.stderr)
            continue
        pairs.append((suburb, path.stem))
    return pairs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("client_dir")
    ap.add_argument("cluster_id")
    ap.add_argument("--service", default="smart lock installation")
    args = ap.parse_args()

    client_dir = Path(args.client_dir).resolve()
    raw_dir = client_dir / "research" / "raw"
    staged_dir = raw_dir / "_synthesis"
    out_dir = client_dir / "clusters" / args.cluster_id / "research" / "suburb-data"
    out_dir.mkdir(parents=True, exist_ok=True)

    operating_model = load_operating_model(client_dir)
    if operating_model == "online_remote":
        print("HALT: operating_model is online_remote — per-suburb ground truth does not apply. "
              "Nothing written.", file=sys.stderr)
        return 1
    print(f"operating_model: {operating_model}")

    provider = BraveNoticeSalvagingProvider(raw_dir)
    pairs = suburbs_for_cluster(client_dir, args.cluster_id, args.service)
    print(f"pairs resolved: {len(pairs)}")

    written = 0
    failures: list[str] = []

    for suburb, entry_slug in pairs:
        pair_slug = slugify_fixture_key(f"{suburb} {args.service}")
        staged = staged_dir / f"{pair_slug}.json"

        if not staged.exists():
            failures.append(f"{suburb}: missing staged synthesis {staged.name}")
            continue

        synthesis_payload = json.loads(staged.read_text())

        # Guard: the physical contract (mobile_service_area) owes all five keys.
        # A silently-thin synthesis would poison the planner, so fail loudly.
        if operating_model in ("premises_per_location", "mobile_service_area", None):
            missing = [k for k in REQUIRED_PHYSICAL_KEYS if k not in synthesis_payload]
            if missing:
                failures.append(f"{suburb}: synthesis missing required keys {missing}")
                continue

        # Verify the Brave fixture the library is about to read actually exists.
        # FixtureDataProvider returns an empty-results stub for a missing file,
        # which would produce a bundle with zero local_signals that LOOKS valid.
        brave_fixture = raw_dir / f"brave-local-{pair_slug}.json"
        if not brave_fixture.exists():
            failures.append(f"{suburb}: missing brave-local fixture {brave_fixture.name}")
            continue

        result = research_suburb_service(
            suburb,
            args.service,
            provider,
            lambda _collected, payload=synthesis_payload: payload,
            operating_model=operating_model,
        )

        bundle = result.to_json()
        if not bundle.get("local_signals"):
            print(f"WARN {suburb}: brave-local fixture present but yielded 0 local_signals — "
                  f"synthesis is running on no local evidence", file=sys.stderr)

        out_path = out_dir / f"{pair_slug}.json"
        out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n")
        written += 1
        print(f"  wrote {out_path.relative_to(client_dir)} "
              f"({len(bundle.get('local_signals', []))} local signals)")

    print(f"\nsuburb-service bundles written: {written}/{len(pairs)}")
    if failures:
        print(f"FAILURES ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
