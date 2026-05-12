"""Sanity check that quotes in a generated report appear in the source transcript.

These are pure-Python checks; they do not call Claude or the network.
"""
from __future__ import annotations

import re

from ytshow.build_document import build_minimal_doc, build_rich_doc
from ytshow.fetch_metadata import Metadata
from ytshow.fetch_transcript import TranscriptResult, TranscriptSegment


def _fixture():
    meta = Metadata(
        video_id="testvideo01",
        url="https://www.youtube.com/watch?v=testvideo01",
        title="A Test Video",
        channel="Tester",
        uploader_id="@tester",
        upload_date="20260101",
        duration=125,
        view_count=10,
        like_count=1,
        description="desc",
        tags=["a", "b"],
        chapters=[],
    )
    tr = TranscriptResult(
        segments=[
            TranscriptSegment(0.0, 5.0, "Hello world this is segment one."),
            TranscriptSegment(5.0, 10.0, "We discuss Acme Corp and revenue of one billion dollars."),
            TranscriptSegment(10.0, 65.0, "More content here."),
            TranscriptSegment(65.0, 125.0, "Closing remarks and goodbye."),
        ],
        source="manual",
        language="en",
    )
    analysis = {
        "overview": "A short test video about Acme Corp.",
        "keywords": ["Acme", "revenue"],
        "chapters": [
            {
                "title": "Intro",
                "start": "00:00",
                "end": "00:05",
                "facts": ["The speaker greets the audience [00:00]."],
                "quotes": [
                    {
                        "speaker": "unknown",
                        "text": "Hello world this is segment one.",
                        "time": "00:00",
                    }
                ],
            },
            {
                "title": "Acme",
                "start": "00:05",
                "end": "00:10",
                "facts": ["Acme Corp had revenue of one billion dollars [00:05]."],
                "quotes": [
                    {
                        "speaker": "unknown",
                        "text": "We discuss Acme Corp and revenue of one billion dollars.",
                        "time": "00:05",
                    }
                ],
            },
        ],
        "entities": {
            "people": [],
            "organizations": [{"name": "Acme Corp", "time": "00:05"}],
            "products": [],
            "places": [],
        },
        "numbers": [
            {"value": "one billion dollars", "context": "Acme Corp revenue", "time": "00:05"}
        ],
        "notes": [],
    }
    return meta, tr, analysis


def _extract_quotes(md: str) -> list[str]:
    # capture blockquote lines and lines beginning with "- " that contain quoted text in double quotes
    out: list[str] = []
    for line in md.splitlines():
        s = line.strip()
        if s.startswith(">"):
            out.append(s.lstrip("> ").strip())
        for m in re.findall(r'"([^"]+)"', s):
            out.append(m.strip())
    return [q for q in out if q]


def test_minimal_doc_quotes_grounded_in_transcript():
    meta, tr, analysis = _fixture()
    md = build_minimal_doc(meta, tr, analysis)
    transcript_text = " ".join(s.text for s in tr.segments)
    for q in _extract_quotes(md):
        # the speaker attribution line should be ignored
        if q.startswith("—"):
            continue
        assert q in transcript_text or any(q in s.text for s in tr.segments), (
            f"quote not found in transcript: {q!r}"
        )


def test_rich_doc_quotes_grounded_in_transcript():
    meta, tr, analysis = _fixture()
    md = build_rich_doc(meta, tr, analysis)
    transcript_text = " ".join(s.text for s in tr.segments)
    for q in _extract_quotes(md):
        if q.startswith("—"):
            continue
        if q.startswith("desc"):  # metadata description blockquote
            continue
        assert q in transcript_text or any(q in s.text for s in tr.segments), (
            f"quote not found in transcript: {q!r}"
        )


def test_facts_contain_timestamps():
    meta, tr, analysis = _fixture()
    md = build_minimal_doc(meta, tr, analysis)
    # every fact bullet under "## Chapter summaries" must end with [mm:ss] or [hh:mm:ss]
    in_chapters = False
    for line in md.splitlines():
        if line.startswith("## Full transcript"):
            in_chapters = False
        if line.startswith("## Chapter summaries"):
            in_chapters = True
            continue
        if in_chapters and line.startswith("- "):
            assert re.search(r"\[\d{1,2}:\d{2}(?::\d{2})?\]", line), (
                f"fact bullet missing timestamp: {line!r}"
            )
