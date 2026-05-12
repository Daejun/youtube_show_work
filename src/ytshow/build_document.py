"""Produce two analysis-document variants (minimal, rich) from the analysis JSON."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .fetch_metadata import Metadata
from .fetch_transcript import TranscriptResult
from .utils import DOCS_DIR, format_timestamp


def _format_upload_date(d: str | None) -> str:
    if not d or len(d) != 8:
        return d or "unknown"
    return f"{d[0:4]}-{d[4:6]}-{d[6:8]}"


def _format_duration(sec: int) -> str:
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}h {m}m {s}s"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


def build_minimal_doc(meta: Metadata, transcript: TranscriptResult, analysis: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {meta.title}")
    lines.append("")
    lines.append(f"channel: {meta.channel}")
    lines.append(f"uploaded: {_format_upload_date(meta.upload_date)}")
    lines.append(f"duration: {_format_duration(meta.duration)}")
    lines.append(f"url: {meta.url}")
    lines.append(f"transcript_source: {transcript.source} ({transcript.language})")
    lines.append("")

    lines.append("## Overview")
    lines.append(analysis.get("overview", "").strip() or "not stated in transcript")
    lines.append("")

    lines.append("## Chapter summaries")
    for ch in analysis.get("chapters", []):
        title = ch.get("title", "Chapter")
        start = ch.get("start", "")
        end = ch.get("end", "")
        lines.append(f"### {title} ({start}–{end})")
        for f in ch.get("facts", []):
            lines.append(f"- {f}")
        lines.append("")

    lines.append("## Full transcript")
    for seg in transcript.segments:
        lines.append(f"[{format_timestamp(seg.start)}] {seg.text}")
    lines.append("")
    return "\n".join(lines)


def _bullets(items: list[str]) -> list[str]:
    return [f"- {x}" for x in items] if items else ["- none stated in transcript"]


def build_rich_doc(meta: Metadata, transcript: TranscriptResult, analysis: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {meta.title}")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Channel | {meta.channel} |")
    lines.append(f"| Uploaded | {_format_upload_date(meta.upload_date)} |")
    lines.append(f"| Duration | {_format_duration(meta.duration)} |")
    if meta.view_count is not None:
        lines.append(f"| Views | {meta.view_count:,} |")
    if meta.like_count is not None:
        lines.append(f"| Likes | {meta.like_count:,} |")
    lines.append(f"| URL | {meta.url} |")
    lines.append(f"| Transcript source | {transcript.source} ({transcript.language}) |")
    if meta.tags:
        lines.append(f"| Tags | {', '.join(meta.tags[:20])} |")
    lines.append("")

    if meta.description:
        lines.append("### Description (from YouTube)")
        lines.append("")
        lines.append("> " + meta.description.strip().replace("\n", "\n> "))
        lines.append("")

    lines.append("## Overview")
    lines.append("")
    lines.append(analysis.get("overview", "").strip() or "not stated in transcript")
    lines.append("")

    lines.append("## Keywords")
    lines.append("")
    kws = analysis.get("keywords", [])
    lines.append(", ".join(kws) if kws else "not stated in transcript")
    lines.append("")

    entities = analysis.get("entities") or {}
    if any(entities.get(k) for k in ("people", "organizations", "products", "places")):
        lines.append("## Entities")
        lines.append("")
        for group, label in [
            ("people", "People"),
            ("organizations", "Organizations"),
            ("products", "Products / works"),
            ("places", "Places"),
        ]:
            items = entities.get(group) or []
            if not items:
                continue
            lines.append(f"### {label}")
            for it in items:
                lines.append(f"- {it.get('name','')} [{it.get('time','')}]")
            lines.append("")

    numbers = analysis.get("numbers") or []
    if numbers:
        lines.append("## Numbers and data points")
        lines.append("")
        lines.append("| Value | Context | Time |")
        lines.append("|---|---|---|")
        for n in numbers:
            lines.append(
                f"| {n.get('value','')} | {n.get('context','')} | {n.get('time','')} |"
            )
        lines.append("")

    lines.append("## Chapters")
    lines.append("")
    for ch in analysis.get("chapters", []):
        title = ch.get("title", "Chapter")
        start = ch.get("start", "")
        end = ch.get("end", "")
        lines.append(f"### {title} ({start}–{end})")
        lines.append("")
        lines.append("**Facts**")
        for f in _bullets(ch.get("facts", [])):
            lines.append(f)
        quotes = ch.get("quotes") or []
        if quotes:
            lines.append("")
            lines.append("**Quotes**")
            for q in quotes:
                speaker = q.get("speaker") or "unknown"
                text = (q.get("text") or "").strip()
                t = q.get("time", "")
                lines.append(f"> {text}")
                lines.append(f"> — {speaker} [{t}]")
                lines.append("")
        lines.append("")

    notes = analysis.get("notes") or []
    if notes:
        lines.append("## Transcript notes / caveats")
        lines.append("")
        for n in notes:
            lines.append(f"- {n}")
        lines.append("")

    lines.append("## Full transcript")
    lines.append("")
    for seg in transcript.segments:
        lines.append(f"[{format_timestamp(seg.start)}] {seg.text}")
    lines.append("")
    return "\n".join(lines)


def write_documents(
    meta: Metadata,
    transcript: TranscriptResult,
    analysis: dict[str, Any],
    out_dir: Path = DOCS_DIR,
) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    minimal_path = out_dir / f"{meta.video_id}.minimal.md"
    rich_path = out_dir / f"{meta.video_id}.rich.md"
    minimal_path.write_text(build_minimal_doc(meta, transcript, analysis), encoding="utf-8")
    rich_path.write_text(build_rich_doc(meta, transcript, analysis), encoding="utf-8")
    return {"minimal": minimal_path, "rich": rich_path}
