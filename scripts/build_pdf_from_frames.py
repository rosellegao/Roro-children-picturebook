#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an A4 landscape picturebook PDF from 16:9 page frames.")
    parser.add_argument("story", type=Path)
    parser.add_argument("frames", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--background", default="#F3C766")
    args = parser.parse_args()

    story_path = args.story.resolve()
    data = json.loads(story_path.read_text(encoding="utf-8"))
    pages = data.get("pages", [])
    if not pages:
        raise SystemExit("story.json has no pages")
    frames_dir = args.frames.resolve()
    frames = [frames_dir / f"page-{index:02d}.png" for index in range(1, len(pages) + 1)]
    missing = [str(path) for path in frames if not path.is_file()]
    if missing:
        raise SystemExit("Missing frames:\n" + "\n".join(missing))
    for path in frames:
        with Image.open(path) as image:
            if image.size != (1920, 1080):
                raise SystemExit(f"Expected a 1920x1080 frame, got {image.size}: {path}")

    book = data.get("book", {})
    basename = book.get("output_basename") or book.get("title") or "picturebook"
    output = args.output.resolve() if args.output else story_path.parent / "output" / "pdf" / f"{basename}-large-print-landscape.pdf"
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = landscape(A4)
    image_height = width * 1080 / 1920
    image_y = (height - image_height) / 2
    pdf = Canvas(str(output), pagesize=(width, height), pageCompression=1)
    pdf.setTitle(str(book.get("title", basename)))
    pdf.setAuthor(str(book.get("series", "Picturebook")))
    pdf.setSubject(str(book.get("subtitle", book.get("title", "Picturebook"))))
    for frame in frames:
        pdf.setFillColor(HexColor(args.background))
        pdf.rect(0, 0, width, height, fill=1, stroke=0)
        pdf.drawImage(ImageReader(str(frame)), 0, image_y, width=width, height=image_height, preserveAspectRatio=True)
        pdf.showPage()
    pdf.save()
    print(output)


if __name__ == "__main__":
    main()

