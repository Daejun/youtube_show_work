"""Grounding sanity check.

Every blockquote line in a generated report (lines that start with `> ` but are
not the speaker attribution line `> — ...`) must appear as a substring of the
"## Full transcript" section in the rich analysis document for the same video.

Usage:
    python scripts/grounding_check.py <slug-or-video-id>

The argument can be either the slug used in the filenames or the original
YouTube video id; the script resolves the slug via the cached bundle or
``outputs/INDEX.md``.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from ytshow.utils import resolve_slug_from_id


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


def _resolve_basename(arg: str, docs_dir: Path) -> str:
    """Return the basename used in outputs/ for ``arg`` (slug or id)."""
    if (docs_dir / f"{arg}.rich.md").exists():
        return arg
    slug = resolve_slug_from_id(arg)
    if slug and (docs_dir / f"{slug}.rich.md").exists():
        return slug
    return arg  # caller will surface a clear "file not found" below


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "usage: grounding_check.py <slug-or-video-id> [reports_dir] [docs_dir]",
            file=sys.stderr,
        )
        return 2
    arg = sys.argv[1]
    reports_dir = Path(sys.argv[2] if len(sys.argv) > 2 else "outputs/reports")
    docs_dir = Path(sys.argv[3] if len(sys.argv) > 3 else "outputs/docs")

    basename = _resolve_basename(arg, docs_dir)
    rich_path = docs_dir / f"{basename}.rich.md"
    if not rich_path.exists():
        print(
            f"no rich analysis doc found for {arg!r} (tried {rich_path})",
            file=sys.stderr,
        )
        return 2
    rich_doc = rich_path.read_text(encoding="utf-8")
    transcript = extract_transcript_section(rich_doc)
    # strip leading [hh:mm:ss] timestamps to a single text blob
    transcript_text = re.sub(r"\[\d{1,2}:\d{2}(?::\d{2})?\]\s*", "", transcript)
    transcript_text = " ".join(transcript_text.split())

    total_quotes = 0
    misses: list[tuple[str, str]] = []
    targets = []
    for variant in ("minimal", "rich"):
        for suffix in (f"{variant}.md", f"{variant}.ko.md"):
            p = reports_dir / f"{basename}.{suffix}"
            if p.exists():
                targets.append((suffix, p))
    if not targets:
        print(f"no reports found for {basename!r} in {reports_dir}", file=sys.stderr)
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
