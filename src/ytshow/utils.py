from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUTS_DIR = REPO_ROOT / "outputs"
DOCS_DIR = OUTPUTS_DIR / "docs"
REPORTS_DIR = OUTPUTS_DIR / "reports"
PROMPTS_DIR = REPO_ROOT / "prompts"
CACHE_DIR = REPO_ROOT / "cache"


def extract_video_id(url: str) -> str:
    """Return the 11-character YouTube video id from any common URL form."""
    u = urlparse(url)
    host = (u.hostname or "").lower()

    if host in {"youtu.be"}:
        vid = u.path.lstrip("/").split("/")[0]
    elif host.endswith("youtube.com"):
        if u.path == "/watch":
            vid = parse_qs(u.query).get("v", [""])[0]
        else:
            # /live/<id>, /shorts/<id>, /embed/<id>, /v/<id>
            parts = [p for p in u.path.split("/") if p]
            vid = parts[-1] if parts else ""
    else:
        vid = url

    vid = vid.split("&")[0].split("?")[0]
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
        raise ValueError(f"Could not extract a YouTube video id from: {url!r}")
    return vid


def format_timestamp(seconds: float) -> str:
    """Seconds -> [hh:mm:ss] or [mm:ss] when under an hour."""
    s = int(round(seconds))
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    if h:
        return f"{h:02d}:{m:02d}:{sec:02d}"
    return f"{m:02d}:{sec:02d}"


def ensure_dirs() -> None:
    for d in (DOCS_DIR, REPORTS_DIR, CACHE_DIR):
        d.mkdir(parents=True, exist_ok=True)


def read_prompt(name: str) -> str:
    path = PROMPTS_DIR / name
    return path.read_text(encoding="utf-8")
