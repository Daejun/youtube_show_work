"""Use Claude to extract a fact-grounded structured analysis from a transcript.

Returns the parsed JSON described in prompts/extract_facts.md.
Uses prompt caching on the (large) transcript block so subsequent calls
(e.g. generating both minimal and rich reports) are cheap.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any

from anthropic import Anthropic

from .fetch_metadata import Metadata
from .fetch_transcript import TranscriptResult
from .utils import format_timestamp, read_prompt

DEFAULT_MODEL = os.environ.get("YTSHOW_MODEL", "claude-sonnet-4-6")


@dataclass
class Analysis:
    data: dict[str, Any]
    model: str
    transcript_block: str  # cached so callers can reuse for reports


def format_transcript_block(segments) -> str:
    lines = []
    for seg in segments:
        ts = format_timestamp(seg.start)
        lines.append(f"[{ts}] {seg.text}")
    return "\n".join(lines)


def _metadata_block(meta: Metadata) -> str:
    parts = [
        f"title: {meta.title}",
        f"channel: {meta.channel}",
        f"url: {meta.url}",
        f"video_id: {meta.video_id}",
        f"duration_seconds: {meta.duration}",
    ]
    if meta.upload_date:
        parts.append(f"upload_date: {meta.upload_date}")
    if meta.chapters:
        parts.append("youtube_chapters:")
        for c in meta.chapters:
            parts.append(
                f"  - {format_timestamp(c.start)}–{format_timestamp(c.end)} {c.title}"
            )
    return "\n".join(parts)


def _strip_code_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\n", "", t)
        if t.endswith("```"):
            t = t[: -len("```")]
    return t.strip()


def analyze(
    meta: Metadata,
    transcript: TranscriptResult,
    model: str = DEFAULT_MODEL,
    client: Anthropic | None = None,
) -> Analysis:
    client = client or Anthropic()
    system_prompt = read_prompt("extract_facts.md")
    transcript_block = format_transcript_block(transcript.segments)
    meta_block = _metadata_block(meta)

    user_content = [
        {
            "type": "text",
            "text": f"# Video metadata\n{meta_block}\n",
        },
        {
            "type": "text",
            "text": f"# Transcript ({transcript.source}, lang={transcript.language})\n{transcript_block}",
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": "Now produce the JSON described in the system prompt.",
        },
    ]

    msg = client.messages.create(
        model=model,
        max_tokens=8000,
        system=[
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_content}],
    )

    raw = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
    cleaned = _strip_code_fence(raw)
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Claude did not return valid JSON for analysis: {e}\n--- raw ---\n{raw[:2000]}"
        ) from e

    return Analysis(data=data, model=model, transcript_block=transcript_block)
