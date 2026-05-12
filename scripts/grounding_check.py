"""Grounding sanity check.

Every blockquote line in a generated report (lines that start with `> ` but are
not the speaker attribution line `> — ...`) must appear as a substring of the
"## Full transcript" section in the rich analysis document for the same video.

Usage:
    python scripts/grounding_check.py <video_id>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def extract_transcript_section(rich_doc: str) -> str:
    """Return the body after the '## Full transcript' header."""
    marker = "## Full transcript"
    idx = rich_doc.find(marker)
    if idx == -1:
        return rich_doc  # fall back to whole doc
    return rich_doc[idx + len(marker):]


def extract_quoted_lines(report_md: str) -> list[str]:
    out: list[str] = []
    for raw in report_md.splitlines():
        s = raw.rstrip()
        if not s.startswith(">"):
            continue
        body = s.lstrip("> ").strip()
        if not body:
            continue
        if body.startswith("—"):
            # speaker attribution line "— Speaker [00:00]"
            continue
        out.append(body)
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: grounding_check.py <video_id> [reports_dir] [docs_dir]", file=sys.stderr)
        return 2
    video_id = sys.argv[1]
    reports_dir = Path(sys.argv[2] if len(sys.argv) > 2 else "outputs/reports")
    docs_dir = Path(sys.argv[3] if len(sys.argv) > 3 else "outputs/docs")

    rich_doc = (docs_dir / f"{video_id}.rich.md").read_text(encoding="utf-8")
    transcript = extract_transcript_section(rich_doc)
    # strip leading [hh:mm:ss] timestamps to a single text blob
    transcript_text = re.sub(r"\[\d{1,2}:\d{2}(?::\d{2})?\]\s*", "", transcript)
    transcript_text = " ".join(transcript_text.split())

    total_quotes = 0
    misses: list[tuple[str, str]] = []
    targets = []
    for variant in ("minimal", "rich"):
        for suffix in (f"{variant}.md", f"{variant}.ko.md"):
            p = reports_dir / f"{video_id}.{suffix}"
            if p.exists():
                targets.append((suffix, p))
    if not targets:
        print(f"no reports found for {video_id} in {reports_dir}", file=sys.stderr)
        return 2
    for label, p in targets:
        for q in extract_quoted_lines(p.read_text(encoding="utf-8")):
            total_quotes += 1
            # also try with surrounding double quote stripping
            q_norm = " ".join(q.split())
            if q_norm in transcript_text:
                continue
            misses.append((label, q))

    print(f"checked {total_quotes} blockquote bodies across {len(targets)} report files")
    if misses:
        print(f"WARNING: {len(misses)} unmatched:")
        for v, q in misses:
            print(f"  [{v}] {q!r}")
        return 1
    print("OK: all blockquote bodies are substrings of the rich analysis transcript section")
    return 0


if __name__ == "__main__":
    sys.exit(main())
