#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")
LANGUAGE_TAG = re.compile(r"^[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*$")
UI_KEYS = (
    "bookLabel",
    "start",
    "navigation",
    "previous",
    "toggle",
    "replay",
    "next",
    "continueAudio",
    "cover",
    "audioError",
)


def load_story(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read story JSON: {error}") from error


def validate(story_path: Path, structure_only: bool = False) -> list[str]:
    data = load_story(story_path)
    errors: list[str] = []
    book = data.get("book")
    pages = data.get("pages")
    speakers = data.get("speakers", {})
    ui = data.get("ui")

    if not isinstance(book, dict):
        errors.append("book must be an object")
        book = {}
    for key in ("series", "title", "output_basename"):
        if not isinstance(book.get(key), str) or not book[key].strip():
            errors.append(f"book.{key} must be a non-empty string")
    basename = book.get("output_basename", "")
    if isinstance(basename, str) and (Path(basename).name != basename or any(c in basename for c in '<>:"/\\|?*')):
        errors.append("book.output_basename must be a safe filename without a path or extension")
    language = book.get("language")
    if not isinstance(language, str) or not LANGUAGE_TAG.match(language):
        errors.append("book.language must be a BCP 47 language tag such as en, zh-CN, or fr")
        language = ""

    if ui is not None and not isinstance(ui, dict):
        errors.append("ui must be an object")
        ui = {}
    if isinstance(ui, dict):
        for key, value in ui.items():
            if key in UI_KEYS and (not isinstance(value, str) or not value.strip()):
                errors.append(f"ui.{key} must be a non-empty string")
    if language and not language.lower().startswith(("en", "zh")):
        if not isinstance(ui, dict):
            errors.append("ui must provide localized reader controls for languages other than English or Chinese")
        else:
            for key in UI_KEYS:
                if not isinstance(ui.get(key), str) or not ui[key].strip():
                    errors.append(f"ui.{key} is required for language {language}")

    if not isinstance(speakers, dict):
        errors.append("speakers must be an object")
        speakers = {}
    for name, config in speakers.items():
        if not isinstance(config, dict) or not HEX_COLOR.match(str(config.get("color", ""))):
            errors.append(f"speakers.{name}.color must be a six-digit hex color")

    if not isinstance(pages, list) or not pages:
        errors.append("pages must be a non-empty array")
        return errors

    base = story_path.parent
    cover_count = 0
    for index, page in enumerate(pages, start=1):
        label = f"pages[{index - 1}]"
        if not isinstance(page, dict):
            errors.append(f"{label} must be an object")
            continue
        for key in ("chapter", "title", "image", "alt", "lines"):
            if key not in page:
                errors.append(f"{label}.{key} is required")
        if page.get("cover"):
            cover_count += 1
        image = page.get("image")
        if isinstance(image, str) and not structure_only and not (base / image).is_file():
            errors.append(f"{label}.image does not exist: {image}")
        audio = page.get("audio")
        if isinstance(audio, str) and audio and not structure_only and not (base / audio).is_file():
            errors.append(f"{label}.audio does not exist: {audio}")
        lines = page.get("lines")
        if not isinstance(lines, list) or not lines:
            errors.append(f"{label}.lines must be a non-empty array")
            continue
        for line_index, line in enumerate(lines):
            line_label = f"{label}.lines[{line_index}]"
            if not isinstance(line, dict) or not isinstance(line.get("text"), str) or not line["text"].strip():
                errors.append(f"{line_label}.text must be a non-empty string")
                continue
            speaker = line.get("speaker")
            if speaker and speaker not in speakers:
                errors.append(f"{line_label}.speaker is not defined in speakers: {speaker}")
            if "speech_text" in line and not isinstance(line["speech_text"], str):
                errors.append(f"{line_label}.speech_text must be a string")

    if cover_count != 1 or not pages[0].get("cover"):
        errors.append("exactly the first page must be marked cover: true")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate reusable picturebook story data.")
    parser.add_argument("story", type=Path)
    parser.add_argument("--structure-only", action="store_true", help="Do not require media files to exist.")
    args = parser.parse_args()
    story_path = args.story.resolve()
    errors = validate(story_path, args.structure_only)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"OK: {story_path}")


if __name__ == "__main__":
    main()

