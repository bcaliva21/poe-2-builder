#!/usr/bin/env python3
"""Create or refresh a character session from PoB code or JSON."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from decode_pob import decode_pob

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "sessions"


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", name.strip()).strip("-").lower()
    return slug or "character"


def read_text(path: Path | None, stdin: bool) -> str:
    if stdin:
        return sys.stdin.read()
    if path is None:
        raise ValueError("Need --pob-file, --pob-stdin, or --json")
    return path.read_text(encoding="utf-8")


def summarize_pob_xml(xml_text: str) -> dict:
    """Best-effort extract. PoB schemas vary; keep whatever we can parse."""
    summary: dict = {
        "source": "path_of_building",
        "class": None,
        "ascendancy": None,
        "level": None,
        "main_skill_hint": None,
        "notes": [],
        "raw_tags": {},
        "stats": {},
    }

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        summary["notes"].append("Decoded PoB payload was not valid XML; saved raw text only.")
        summary["preview"] = xml_text[:2000]
        return summary

    # Common PoB XML shapes: Build attribute fields, PlayerStat rows, Skill sets
    build = root if root.tag.endswith("PathOfBuilding") or root.tag == "PathOfBuilding" else root.find(".//PathOfBuilding")
    target = build if build is not None else root

    for key in ("className", "ascendClassName", "level", "characterLevel"):
        val = target.attrib.get(key) if hasattr(target, "attrib") else None
        if val:
            if "class" in key.lower() and "ascend" not in key.lower():
                summary["class"] = val
            elif "ascend" in key.lower():
                summary["ascendancy"] = val
            elif "level" in key.lower():
                try:
                    summary["level"] = int(float(val))
                except ValueError:
                    summary["level"] = val

    # Collect PlayerStat-like numbers when present
    stats = {}
    for elem in root.iter():
        tag = elem.tag.split("}")[-1]
        if tag in {"PlayerStat", "Stat"} and elem.attrib:
            name = elem.attrib.get("stat") or elem.attrib.get("name")
            value = elem.attrib.get("value")
            if name and value is not None:
                stats[name] = value
        if tag in {"Skill", "Gem"} and summary["main_skill_hint"] is None:
            hint = elem.attrib.get("name") or elem.attrib.get("skillId") or elem.attrib.get("gemId")
            if hint and "Support" not in hint:
                summary["main_skill_hint"] = hint

    # Keep a useful subset if the export is huge
    interesting = [
        "AverageDamage",
        "TotalDPS",
        "CritChance",
        "CritMultiplier",
        "AttackSpeed",
        "CastSpeed",
        "Life",
        "EnergyShield",
        "Mana",
        "Armour",
        "Evasion",
        "FireResist",
        "ColdResist",
        "LightningResist",
        "ChaosResist",
    ]
    lowered = {k.lower(): (k, v) for k, v in stats.items()}
    for key in interesting:
        hit = lowered.get(key.lower())
        if hit:
            summary["stats"][hit[0]] = hit[1]

    # Also keep any stat whose name suggests crit/shock/ailment
    for k, v in stats.items():
        lk = k.lower()
        if any(s in lk for s in ("crit", "shock", "ailment", "ignite", "bleed", "poison", "dps", "life", "energy")):
            summary["stats"].setdefault(k, v)

    if not summary["stats"] and stats:
        # Cap dump so character.json stays readable
        summary["stats"] = dict(list(stats.items())[:80])
        summary["notes"].append("Stored first 80 raw stats; refine parser if needed.")

    summary["raw_tags"]["root_tag"] = root.tag
    return summary


def write_session(slug: str, meta: dict, character: dict, build_text: str | None) -> Path:
    folder = SESSIONS / slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (folder / "character.json").write_text(json.dumps(character, indent=2) + "\n", encoding="utf-8")
    notes = folder / "notes.md"
    if not notes.exists():
        notes.write_text("# Notes\n\n- Session created by scripts/new_session.py\n", encoding="utf-8")
    if build_text is not None:
        # PoB is usually XML; still keep .xml extension for agents
        (folder / "build.xml").write_text(build_text, encoding="utf-8")
    (SESSIONS / "active.md").write_text(
        f"# Active session\n\nslug: `{slug}`\n\npath: `sessions/{slug}/`\n",
        encoding="utf-8",
    )
    return folder


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Session name / character name")
    parser.add_argument("--pob-file", type=Path, help="File containing a PoB code")
    parser.add_argument("--pob-stdin", action="store_true", help="Read PoB code from stdin")
    parser.add_argument("--json", type=Path, help="Existing character JSON to copy/normalize")
    parser.add_argument("--league", default="unknown", help="League label for meta.json")
    args = parser.parse_args()

    slug = slugify(args.name)
    now = datetime.now(timezone.utc).isoformat()

    if args.json:
        data = json.loads(args.json.read_text(encoding="utf-8"))
        character = data if isinstance(data, dict) else {"data": data}
        character.setdefault("source", "json_upload")
        build_text = None
        source = "json"
    elif args.pob_file or args.pob_stdin:
        code = read_text(args.pob_file, args.pob_stdin)
        build_text = decode_pob(code)
        character = summarize_pob_xml(build_text)
        source = "pob"
    else:
        print("Provide --json or --pob-file/--pob-stdin", file=sys.stderr)
        return 1

    meta = {
        "name": args.name,
        "slug": slug,
        "league": args.league,
        "source": source,
        "updated_at": now,
    }
    folder = write_session(slug, meta, character, build_text)
    print(f"Wrote {folder}")
    print(f"Active session -> sessions/{slug}/")
    if character.get("class") or character.get("stats"):
        print(
            "Summary:",
            character.get("class"),
            character.get("ascendancy"),
            f"level={character.get('level')}",
            f"stats={len(character.get('stats', {}))}",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
