# AnkiShare

Version-controlled Anki note templates and release metadata for published English-learning decks.

This repository is the source-control companion to the local Anki collection. Anki remains the editor and the source of truth for notes, media, scheduling, and APKG export. Git tracks the note-type definitions that need careful review: fields, card front/back HTML, and CSS.

## Layout

- `note-templates/`: exported note-type snapshots, one directory per model.
- `tools/export_note_templates.py`: read-only export from the local AnkiMCP server.
- `exports/`: ignored local APKG release output.

Each note-type directory contains `model.json`, `style.css`, and one `front.html` / `back.html` pair for each card template.

## Refresh templates

Keep Anki Desktop and AnkiMCP running, then execute:

```powershell
python tools/export_note_templates.py
git diff -- note-templates
```

The script reads `http://127.0.0.1:3141/` only. It does not change Anki, export cards, or access AnkiWeb.

## Publishing decks

Export reviewed decks from Anki to the ignored `exports/` directory, test the APKG in Anki, and attach the verified file to a GitHub Release. Keep the release version and checksum in the release notes; do not commit the APKG itself.
