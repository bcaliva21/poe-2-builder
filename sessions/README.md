# Sessions

Each saved character lives in its own folder:

```text
sessions/
  active.md                 # pointer to the current session
  my-witch/
    meta.json               # name, source, timestamps
    character.json          # normalized stats / summary for the agent
    build.xml               # decoded PoB XML when source was PoB
    notes.md                # freeform notes / prior conclusions
```

Create sessions with:

```bash
python3 scripts/new_session.py --name my-witch --pob-file /path/to/code.txt
python3 scripts/new_session.py --name my-witch --json /path/to/character.json
```

Clear the active session by resetting `active.md` to "None" when you want generic-only answers.
