"""Fetch YouTube video metadata via yt-dlp (no media download)."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any

import yt_dlp


@dataclass
class Chapter:
    title: str
    start: float
    end: float


@dataclass
class Metadata:
    video_id: str
    url: str
    title: str
    channel: str
    uploader_id: str | None
    upload_date: str | None  # YYYYMMDD
    duration: int  # seconds
    view_count: int | None
    like_count: int | None
    description: str
    tags: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    chapters: list[Chapter] = field(default_factory=list)
    is_live: bool = False
    was_live: bool = False
    language: str | None = None
    thumbnail: str | None = None

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["chapters"] = [asdict(c) for c in self.chapters]
        return d


def fetch_metadata(url: str) -> Metadata:
    """Extract metadata only — does not download media."""
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": False,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    chapters_raw = info.get("chapters") or []
    chapters = [
        Chapter(
            title=str(c.get("title") or f"Chapter {i+1}"),
            start=float(c.get("start_time") or 0),
            end=float(c.get("end_time") or 0),
        )
        for i, c in enumerate(chapters_raw)
    ]

    return Metadata(
        video_id=str(info.get("id") or ""),
        url=str(info.get("webpage_url") or url),
        title=str(info.get("title") or ""),
        channel=str(info.get("channel") or info.get("uploader") or ""),
        uploader_id=info.get("uploader_id"),
        upload_date=info.get("upload_date"),
        duration=int(info.get("duration") or 0),
        view_count=info.get("view_count"),
        like_count=info.get("like_count"),
        description=str(info.get("description") or ""),
        tags=list(info.get("tags") or []),
        categories=list(info.get("categories") or []),
        chapters=chapters,
        is_live=bool(info.get("is_live")),
        was_live=bool(info.get("was_live")),
        language=info.get("language"),
        thumbnail=info.get("thumbnail"),
    )
