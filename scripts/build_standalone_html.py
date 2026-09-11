#!/usr/bin/env python3
import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = SKILL_ROOT / "assets" / "book.template.html"


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a self-contained responsive picturebook HTML.")
    parser.add_argument("story", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    args = parser.parse_args()

    story_path = args.story.resolve()
    base = story_path.parent
    data = json.loads(story_path.read_text(encoding="utf-8"))
    pages = data.get("pages", [])
    if not pages:
        raise SystemExit("story.json has no pages")

    for page in pages:
        image_path = (base / page["image"]).resolve()
        if not image_path.is_file():
            raise SystemExit(f"Missing image: {image_path}")
        page["image_data"] = data_uri(image_path)
        audio_name = page.get("audio")
        if audio_name:
            audio_path = (base / audio_name).resolve()
            if not audio_path.is_file():
                raise SystemExit(f"Missing audio: {audio_path}")
            page["audio_data"] = data_uri(audio_path)
        else:
            page["audio_data"] = ""

    book = data.get("book", {})
    basename = book.get("output_basename") or book.get("title") or "picturebook"
    output = args.output.resolve() if args.output else base / "output" / "html" / f"{basename}.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    template = args.template.resolve().read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    document = template.replace("__DOCUMENT_TITLE__", html.escape(str(book.get("title", "Picturebook"))))
    document = document.replace("__BOOK_DATA_JSON__", payload)
    if "__BOOK_DATA_JSON__" in document:
        raise SystemExit("Template replacement failed")
    output.write_text(document, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

