"""Fetch a timed transcript.

Strategy (in order):
1. youtube-transcript-api manual captions (preferred lang, then any)
2. youtube-transcript-api auto-generated captions
3. yt-dlp audio download -> faster-whisper STT

Returns a list of (start_seconds, end_seconds, text) segments and a source label.
"""
from __future__ import annotations

import logging
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)


@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str


@dataclass
class TranscriptResult:
    segments: list[TranscriptSegment]
    source: str  # "manual", "auto", "whisper"
    language: str | None


def _try_youtube_transcript_api(
    video_id: str, languages: list[str]
) -> TranscriptResult | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api._errors import (
            TranscriptsDisabled,
            NoTranscriptFound,
            VideoUnavailable,
        )
    except Exception as e:  # pragma: no cover
        log.warning("youtube-transcript-api not importable: %s", e)
        return None

    try:
        listing = YouTubeTranscriptApi.list_transcripts(video_id)
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        log.info("no captions via API: %s", e)
        return None
    except Exception as e:
        log.warning("transcript list failed: %s", e)
        return None

    # try manual first in preferred languages, then any manual, then generated
    def fetch(transcript) -> TranscriptResult:
        data = transcript.fetch()
        segs = [
            TranscriptSegment(
                start=float(d["start"]),
                end=float(d["start"]) + float(d.get("duration", 0) or 0),
                text=str(d["text"]).replace("\n", " ").strip(),
            )
            for d in data
            if str(d.get("text", "")).strip()
        ]
        source = "auto" if transcript.is_generated else "manual"
        return TranscriptResult(segments=segs, source=source, language=transcript.language_code)

    # manual in preferred langs
    try:
        t = listing.find_manually_created_transcript(languages)
        return fetch(t)
    except Exception:
        pass
    # any manual
    for t in listing:
        if not t.is_generated:
            try:
                return fetch(t)
            except Exception:
                continue
    # generated in preferred langs
    try:
        t = listing.find_generated_transcript(languages)
        return fetch(t)
    except Exception:
        pass
    # any generated
    for t in listing:
        if t.is_generated:
            try:
                return fetch(t)
            except Exception:
                continue
    return None


def _download_audio(url: str, out_dir: Path) -> Path:
    """Download the bestaudio track via yt-dlp. Requires ffmpeg for m4a/mp3 muxing."""
    import yt_dlp

    out_template = str(out_dir / "%(id)s.%(ext)s")
    opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "bestaudio/best",
        "outtmpl": out_template,
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
                "preferredquality": "0",
            }
        ],
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
    vid = info.get("id")
    for p in out_dir.iterdir():
        if p.stem == vid and p.suffix in {".m4a", ".mp3", ".wav", ".webm", ".opus"}:
            return p
    raise RuntimeError("audio file not found after yt-dlp download")


def _whisper_transcribe(
    audio_path: Path, language: str | None, model_size: str
) -> TranscriptResult:
    """Transcribe an audio file with faster-whisper.

    Tries ``device='auto'`` first so GPU users get the speedup, then falls
    back to ``device='cpu'`` if the CUDA runtime is missing (common on
    fresh Windows installs without the NVIDIA libraries).
    """
    from faster_whisper import WhisperModel

    def _run(device: str, compute_type: str) -> tuple[list[TranscriptSegment], object]:
        model = WhisperModel(model_size, device=device, compute_type=compute_type)
        segments, info = model.transcribe(
            str(audio_path),
            language=language,
            vad_filter=True,
            word_timestamps=False,
        )
        out: list[TranscriptSegment] = []
        # iterating the segments generator is what actually triggers GPU/CPU work,
        # so any device-load failure surfaces here, not at model construction.
        for s in segments:
            text = (s.text or "").strip()
            if not text:
                continue
            out.append(TranscriptSegment(start=float(s.start), end=float(s.end), text=text))
        return out, info

    try:
        out, info = _run("auto", "auto")
    except RuntimeError as e:
        msg = str(e).lower()
        cuda_missing = (
            "cublas" in msg
            or "cudnn" in msg
            or "cuda" in msg
            or "not found or cannot be loaded" in msg
        )
        if not cuda_missing:
            raise
        # Retry on CPU with int8 quantization — slower but works without CUDA.
        out, info = _run("cpu", "int8")
    return TranscriptResult(segments=out, source="whisper", language=info.language)


def fetch_transcript(
    url: str,
    video_id: str,
    languages: list[str] | None = None,
    allow_whisper: bool = True,
    whisper_model: str = "base.en",
) -> TranscriptResult:
    langs = languages or ["en", "en-US", "en-GB"]

    result = _try_youtube_transcript_api(video_id, langs)
    if result and result.segments:
        return result

    if not allow_whisper:
        raise RuntimeError(
            "no captions available and Whisper fallback disabled"
        )

    if not shutil.which("ffmpeg"):
        raise RuntimeError(
            "ffmpeg is required for Whisper fallback but was not found on PATH"
        )

    with tempfile.TemporaryDirectory(prefix="ytshow_audio_") as tmp:
        audio = _download_audio(url, Path(tmp))
        lang = langs[0].split("-")[0] if langs else None
        return _whisper_transcribe(audio, language=lang, model_size=whisper_model)
