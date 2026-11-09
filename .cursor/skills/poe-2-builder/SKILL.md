---
name: poe-2-builder
description: Path of Exile 2 build advisor for this repo. Loads or creates a character session from Path of Building code or JSON, then answers build-specific or generic PoE2 questions using knowledge/mechanics and session stats. Use when the user mentions PoE2, Path of Exile 2, PoB codes, poe.ninja profiles, build scaling, gems, uniques, ailments, crit, defenses, or invokes /poe-2-builder.
---

# PoE2 Builder

## Intake

1. Read `sessions/active.md`.
2. If empty / missing, ask for **one**:
   - PoB code (paste)
   - Path to character JSON
   - Existing session name
3. Create or load the session:
   - Prefer `python3 scripts/new_session.py ...` for PoB/JSON intake.
   - Write `sessions/<slug>/meta.json`, `character.json`, optional `build.xml` / `notes.md`.
   - Point `sessions/active.md` at that folder.
4. Summarize class, ascendancy, main skills, and any parsed offensive/defensive stats you found.
5. Note gaps (e.g. no crit chance in export).

## Answer any question

1. Map the question to systems → open matching `knowledge/mechanics/*.md`.
2. Use active session numbers for build-specific asks.
3. Derive the answer from formulas + data. Do not invent a special-case FAQ.
4. Structure:
   - Verdict (1-2 sentences)
   - Why (formulas + character numbers)
   - Confidence + missing inputs
5. For comparisons (stat A vs stat B): evaluate marginal gain at current values, caps, and uptime.

## Session commands the user may say

- "load session X"
- "save this as X"
- "clear session" / "generic only"
- "refresh from this PoB code"

## Anti-patterns

- Answering build-specific questions with only generic vibes
- Fetching unsupported poe.ninja character APIs
- Claiming exact DPS without the stats needed to compute it
