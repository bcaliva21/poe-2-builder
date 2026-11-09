# poe-2-builder

Local Path of Exile 2 brain pack for any coding agent (Cursor, Claude, Gemini, etc.).

Open this repo, load a character session (PoB code or JSON), then ask build-specific or generic questions. The agent is instructed to reason from the mechanics corpus + your session stats, not from vibes.

## Quick start

1. Open this folder in your agent of choice.
2. Run `/poe-2-builder` or ask a PoE2 build question.
3. Paste a Path of Building code, point at a JSON file, or load a saved session.
4. Ask anything: scaling choices, gem swaps, defenses, generic theory.

```bash
# Decode a PoB code into a new session
python3 scripts/new_session.py --name my-char --pob-file pob.txt

# Or from stdin
pbpaste | python3 scripts/new_session.py --name my-char --pob-stdin

# Or copy an existing character JSON
python3 scripts/new_session.py --name my-char --json path/to/character.json
```

## Layout

```text
AGENTS.md                          # always-on answering rules for this repo
.cursor/skills/poe-2-builder/      # /poe-2-builder intake + Q&A skill
knowledge/mechanics/               # composable game physics (source of truth)
knowledge/reference/               # optional dumps (RePoE / PoB extracts)
sessions/                          # saved character contexts
scripts/                           # PoB decode + session helpers
```

## What this is / is not

**Is:** a knowledge + session pack that makes agents better at PoE2 than a naked chat bot.

**Is not:** a scraper for poe.ninja private character APIs, a live trade bot, or a full PoB replacement.

Preferred character intake: **PoB export code** or a JSON file you already have. If you use a poe.ninja profile page, export/copy the character data yourself into `sessions/` rather than hammering unsupported endpoints.

## After a patch

1. Skim patch notes for combat/ailment/defense changes.
2. Update the affected files under `knowledge/mechanics/`.
3. Bump the patch pin in `knowledge/mechanics/sources.md`.
4. Re-export your character into a fresh session if needed.
