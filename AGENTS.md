# AnkiShare Instructions

This repository version-controls Anki note-type definitions and release metadata.
It is not an Anki collection backup.

## Boundaries

- Do not commit `.apkg`, `.colpkg`, `collection.anki2`, `collection.anki21`, media,
  card history, review history, or user data.
- Treat `note-templates/` as a checked-in snapshot of the active local Anki models.
- Use the local AnkiMCP server for all Anki reads and writes. Do not edit an APKG
  database directly.
- Default to read-only inspection. Before any Anki write, state the query, affected
  note/card counts, and representative samples; wait for explicit user confirmation.
- Before confirmed bulk writes, create an Anki export backup under `F:\data\AnkiBackups`.

## Template Workflow

1. Run `python tools/export_note_templates.py` while AnkiMCP is running locally.
2. Review the resulting Git diff in `note-templates/`.
3. Commit reviewed template changes with a clear description of the Anki note type.
4. Apply a reviewed template change back to Anki through AnkiMCP only after explicit confirmation.

The exporter connects only to `http://127.0.0.1:3141/` and uses read-only MCP tools:
`model_names`, `model_field_names`, `model_templates`, and `model_styling`.
