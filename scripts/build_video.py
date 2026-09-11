#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def locate_ffmpeg(explicit: Path | None) -> Path:
    if explicit:
        return explicit.resolve()
    system = shutil.which("ffmpeg")
    if system:
        return Path(system)
    try:
        import imageio_ffmpeg

        return Path(imageio_ffmpeg.get_ffmpeg_exe())
    except ImportError as error:
        raise SystemExit("ffmpeg is required. Pass --ffmpeg or install imageio-ffmpeg.") from error


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Combine 16:9 picturebook frames and page audio into an MP4.")
    parser.add_argument("story", type=Path)
    parser.add_argument("frames", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--ffmpeg", type=Path)
    parser.add_argument("--between-page-pause", type=float, default=0.45)
    parser.add_argument("--ending-hold", type=float, default=1.5)
    args = parser.parse_args()

    story_path = args.story.resolve()
    root = story_path.parent
    data = json.loads(story_path.read_text(encoding="utf-8"))
    pages = data.get("pages", [])
    if not pages:
        raise SystemExit("story.json has no pages")
    ffmpeg = locate_ffmpeg(args.ffmpeg)
    frames_dir = args.frames.resolve()
    book = data.get("book", {})
    basename = book.get("output_basename") or book.get("title") or "picturebook"
    output = args.output.resolve() if args.output else root / "output" / "video" / f"{basename}-full-story-1080p.mp4"
    output.parent.mkdir(parents=True, exist_ok=True)
    build_dir = output.parent / f".{output.stem}-segments"
    build_dir.mkdir(parents=True, exist_ok=True)
    segments: list[Path] = []

    for index, page in enumerate(pages, start=1):
        frame = frames_dir / f"page-{index:02d}.png"
        if not frame.is_file():
            raise SystemExit(f"Missing frame: {frame}")
        audio_name = page.get("audio")
        if not audio_name:
            raise SystemExit(f"Page {index} has no audio path")
        audio = (root / audio_name).resolve()
        if not audio.is_file():
            raise SystemExit(f"Missing audio: {audio}")
        pause = args.ending_hold if index == len(pages) else args.between_page_pause
        segment = build_dir / f"page-{index:02d}.mp4"
        run([
            str(ffmpeg), "-hide_banner", "-loglevel", "warning", "-y",
            "-loop", "1", "-framerate", "30", "-i", str(frame), "-i", str(audio),
            "-filter_complex", "[0:v]scale=1920:1080:flags=lanczos,format=yuv420p[outv]",
            "-map", "[outv]", "-map", "1:a:0",
            "-af", f"apad=pad_dur={pause:.3f},aresample=48000", "-shortest",
            "-r", "30", "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage",
            "-crf", "19", "-profile:v", "high", "-level", "4.1", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
            "-movflags", "+faststart", str(segment),
        ])
        segments.append(segment)

    concat_file = build_dir / "segments.txt"
    concat_file.write_text("\n".join(f"file '{path.as_posix()}'" for path in segments) + "\n", encoding="utf-8")
    run([
        str(ffmpeg), "-hide_banner", "-loglevel", "warning", "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        "-af", "aresample=async=1:first_pts=0", "-movflags", "+faststart", str(output),
    ])
    print(output)


if __name__ == "__main__":
    main()

