"""Skill helper: fetch metadata + transcript and emit a JSON bundle.

Transcript strategy:
  1. yt-dlp manual subtitles (srt) in the requested languages
  2. yt-dlp automatic captions (srt) in the requested languages
  3. faster-whisper STT on yt-dlp-downloaded audio (only if --allow-whisper)

This bypasses youtube-transcript-api (which broke in 1.x, see fetch_transcript.py)
and produces the same TranscriptResult shape the rest of the pipeline expects.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from dataclasses import asdict
from pathlib import Path

import yt_dlp

from ytshow.fetch_metadata import fetch_metadata
from ytshow.fetch_transcript import TranscriptResult, TranscriptSegment, _whisper_transcribe
from ytshow.utils import extract_video_id, format_timestamp


def _srt_time_to_seconds(s: str) -> float:
    # "HH:MM:SS,mmm"
    h, m, rest = s.split(":")
    sec, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000.0


_TIMING_RE = re.compile(
    r"(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})"
)


def parse_srt(text: str) -> list[TranscriptSegment]:
    """Parse a YouTube-style .srt into TranscriptSegment list.

    YouTube auto captions often contain per-word fade-in markup (<00:00:01.234>),
    HTML-like <c> tags, and karaoke-style duplicates. We strip those and merge
    only the visible plaintext per cue.
    """
    segments: list[TranscriptSegment] = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for block in blocks:
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        # find the timing line
        timing_idx = None
        for i, ln in enumerate(lines):
            if _TIMING_RE.search(ln):
                timing_idx = i
                break
        if timing_idx is None:
            continue
        m = _TIMING_RE.search(lines[timing_idx])
        start = _srt_time_to_seconds(m.group(1))
        end = _srt_time_to_seconds(m.group(2))
        body = " ".join(lines[timing_idx + 1 :])
        # strip yt-style inline timestamp markers like <00:00:01.234> and <c> tags
        body = re.sub(r"<[^>]+>", "", body)
        body = re.sub(r"\s+", " ", body).strip()
        if not body:
            continue
        segments.append(TranscriptSegment(start=start, end=end, text=body))
    return segments


def _try_subs(
    video_id: str,
    langs: list[str],
    cache_dir: Path,
    automatic: bool,
    retries: int = 3,
) -> TranscriptResult | None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "writesubtitles": not automatic,
        "writeautomaticsub": automatic,
        "subtitleslangs": langs,
        "subtitlesformat": "srt",
        "outtmpl": str(cache_dir / "%(id)s.%(ext)s"),
        "noplaylist": True,
    }
    canonical = f"https://www.youtube.com/watch?v={video_id}"
    import time

    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.extract_info(canonical, download=True)
            last_err = None
            break
        except Exception as e:
            last_err = e
            time.sleep(2 * (attempt + 1))
    if last_err is not None:
        print(
            f"yt-dlp subs ({'auto' if automatic else 'manual'}) failed after {retries} attempts: {last_err}",
            file=sys.stderr,
        )
        return None
    # look for the resulting .srt file
    for lang in langs:
        for suffix in (f".{lang}.srt", f".{lang.split('-')[0]}.srt"):
            p = cache_dir / f"{video_id}{suffix}"
            if p.exists():
                segs = parse_srt(p.read_text(encoding="utf-8"))
                if segs:
                    return TranscriptResult(
                        segments=segs,
                        source=("auto" if automatic else "manual"),
                        language=lang,
                    )
    return None


def _whisper_fallback(video_id: str, langs: list[str], model_size: str) -> TranscriptResult:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required for the Whisper fallback")
    canonical = f"https://www.youtube.com/watch?v={video_id}"
    with tempfile.TemporaryDirectory(prefix="ytshow_audio_") as tmp:
        tmp_dir = Path(tmp)
        opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio/best",
            "outtmpl": str(tmp_dir / "%(id)s.%(ext)s"),
            "noplaylist": True,
            "postprocessors": [
                {"key": "FFmpegExtractAudio", "preferredcodec": "m4a", "preferredquality": "0"}
            ],
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(canonical, download=True)
        vid = info.get("id")
        audio = None
        for p in tmp_dir.iterdir():
            if p.stem == vid and p.suffix in {".m4a", ".mp3", ".wav", ".webm", ".opus"}:
                audio = p
                break
        if not audio:
            raise RuntimeError("audio file not found after yt-dlp download")
        lang = (langs[0].split("-")[0] if langs else None)
        return _whisper_transcribe(audio, language=lang, model_size=model_size)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default=None)
    ap.add_argument("--cache-dir", default="cache")
    ap.add_argument("--languages", default="en")
    ap.add_argument("--no-whisper", action="store_true")
    ap.add_argument("--whisper-model", default="base.en")
    args = ap.parse_args()

    video_id = extract_video_id(args.url)
    langs = [s.strip() for s in args.languages.split(",") if s.strip()]
    cache_dir = Path(args.cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    meta_cache = cache_dir / f"{video_id}.metadata.json"
    if meta_cache.exists():
        from ytshow.fetch_metadata import Metadata, Chapter
        raw = json.loads(meta_cache.read_text(encoding="utf-8"))
        chapters = [Chapter(**c) for c in raw.pop("chapters", [])]
        meta = Metadata(chapters=chapters, **raw)
    else:
        meta = fetch_metadata(args.url)
        meta_cache.write_text(json.dumps(meta.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

    # use cached SRT if present, else fetch
    tr: TranscriptResult | None = None
    cached_srt = None
    for suffix in (f".{langs[0]}.srt" if langs else "", *(f".{l}.srt" for l in langs)):
        p = cache_dir / f"{video_id}{suffix}"
        if p.exists() and p.stat().st_size > 0:
            cached_srt = p
            break
    if cached_srt is not None:
        segs = parse_srt(cached_srt.read_text(encoding="utf-8"))
        if segs:
            tr = TranscriptResult(segments=segs, source="manual", language=langs[0] if langs else None)
            print(f"using cached SRT: {cached_srt}", file=sys.stderr)
    if tr is None:
        tr = (
            _try_subs(meta.video_id, langs, cache_dir, automatic=False)
            or _try_subs(meta.video_id, langs, cache_dir, automatic=True)
        )
    if tr is None or not tr.segments:
        if args.no_whisper:
            raise SystemExit("no captions found and --no-whisper specified")
        tr = _whisper_fallback(meta.video_id, langs, args.whisper_model)

    bundle = {
        "video_id": meta.video_id,
        "metadata": meta.to_dict(),
        "transcript": {
            "source": tr.source,
            "language": tr.language,
            "segments": [
                {"start": s.start, "end": s.end, "ts": format_timestamp(s.start), "text": s.text}
                for s in tr.segments
            ],
        },
    }
    out_path = Path(args.out) if args.out else cache_dir / f"{meta.video_id}.bundle.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "video_id": meta.video_id,
                "title": meta.title,
                "channel": meta.channel,
                "duration_seconds": meta.duration,
                "transcript_source": tr.source,
                "transcript_language": tr.language,
                "segment_count": len(tr.segments),
                "char_count": sum(len(s.text) for s in tr.segments),
                "bundle_path": str(out_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
