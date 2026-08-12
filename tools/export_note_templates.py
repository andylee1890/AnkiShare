#!/usr/bin/env python3
"""Export Anki note-type templates through the local AnkiMCP HTTP endpoint."""

from __future__ import annotations

import json
import re
import shutil
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "note-templates"
MCP_URL = "http://127.0.0.1:3141/"


def call_tool(name: str, arguments: dict | None = None) -> dict:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments or {}},
    }
    request = urllib.request.Request(
        MCP_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        raw = response.read().decode("utf-8")
    for line in raw.splitlines():
        if line.startswith("data: "):
            result = json.loads(line[6:])
            if "error" in result:
                raise RuntimeError(result["error"])
            content = result["result"]
            if "structuredContent" in content:
                return repair_mojibake(content["structuredContent"])
            return repair_mojibake(json.loads(content["content"][0]["text"]))
    raise RuntimeError("AnkiMCP returned no JSON-RPC data event")


def repair_mojibake(value):
    if isinstance(value, dict):
        return {key: repair_mojibake(item) for key, item in value.items()}
    if isinstance(value, list):
        return [repair_mojibake(item) for item in value]
    if not isinstance(value, str):
        return value
    try:
        return value.encode("latin-1").decode("utf-8")
    except UnicodeError:
        return value


def safe_name(value: str, index: int) -> str:
    normalized = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "-", value).strip(" .")
    normalized = re.sub(r"\s+", " ", normalized)
    return f"{index:02d}-{normalized or 'model'}"


def write_text(path: Path, content: str) -> None:
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def main() -> None:
    models = call_tool("model_names")["modelNames"]
    staging = ROOT / ".note-templates-staging"
    shutil.rmtree(staging, ignore_errors=True)
    staging.mkdir(parents=True)

    manifest = []
    for index, model_name in enumerate(models, start=1):
        fields = call_tool("model_field_names", {"model_name": model_name})
        templates = call_tool("model_templates", {"model_name": model_name})
        styling = call_tool("model_styling", {"model_name": model_name})
        directory = safe_name(model_name, index)
        model_dir = staging / directory
        cards_dir = model_dir / "cards"
        cards_dir.mkdir(parents=True)

        template_entries = templates.get("templates", templates)
        if isinstance(template_entries, dict):
            template_entries = [
                {"name": name, **value} for name, value in template_entries.items()
            ]
        exported_cards = []
        for card_index, template in enumerate(template_entries, start=1):
            card_name = template.get("name", f"card-{card_index}")
            card_dir = cards_dir / safe_name(card_name, card_index)
            card_dir.mkdir()
            front = template.get("Front", template.get("front", ""))
            back = template.get("Back", template.get("back", ""))
            write_text(card_dir / "front.html", front)
            write_text(card_dir / "back.html", back)
            exported_cards.append({"name": card_name, "path": str(card_dir.relative_to(model_dir))})

        css = styling.get("css", styling.get("styling", ""))
        write_text(model_dir / "style.css", css)
        metadata = {
            "model_name": model_name,
            "fields": fields.get("fields", fields.get("field_names", [])),
            "cards": exported_cards,
        }
        write_text(model_dir / "model.json", json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
        manifest.append({"model_name": model_name, "path": directory, "cards": len(exported_cards)})

    write_text(staging / "manifest.json", json.dumps({"models": manifest}, ensure_ascii=False, indent=2) + "\n")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    staging.rename(OUTPUT)
    print(f"Exported {len(manifest)} note types to {OUTPUT}")


if __name__ == "__main__":
    main()
