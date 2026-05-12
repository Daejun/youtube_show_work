"""High-level orchestration: URL -> analysis docs -> reports -> conversions."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .analyze import analyze
from .build_document import write_documents
from .build_report import write_reports
from .convert import convert_all, have_pandoc
from .fetch_metadata import Metadata, fetch_metadata
from .fetch_transcript import TranscriptResult, fetch_transcript
from .utils import DOCS_DIR, REPORTS_DIR, ensure_dirs, extract_video_id


@dataclass
class PipelineResult:
    metadata: Metadata
    transcript: TranscriptResult
    analysis: dict
    doc_paths: dict[str, Path]
    report_paths: dict[str, dict[str, Path]]  # variant -> {fmt: path}


def run_pipeline(
    url: str,
    variants: list[str],
    formats: list[str],
    languages: list[str] | None = None,
    allow_whisper: bool = True,
    whisper_model: str = "base.en",
    model: str | None = None,
    skip_reports: bool = False,
) -> PipelineResult:
    ensure_dirs()
    video_id = extract_video_id(url)

    meta = fetch_metadata(url)
    # canonical URL
    canonical_url = f"https://www.youtube.com/watch?v={meta.video_id}"
    transcript = fetch_transcript(
        canonical_url,
        meta.video_id,
        languages=languages,
        allow_whisper=allow_whisper,
        whisper_model=whisper_model,
    )

    analysis = analyze(meta, transcript, model=model) if model else analyze(meta, transcript)
    doc_paths = write_documents(meta, transcript, analysis.data, out_dir=DOCS_DIR)
    slug = doc_paths.get("slug") or doc_paths["minimal"].stem.split(".")[0]

    report_paths: dict[str, dict[str, Path]] = {}
    if not skip_reports:
        for variant in variants:
            source_doc = doc_paths[variant].read_text(encoding="utf-8")
            paths = write_reports(
                slug,
                source_doc,
                [variant],
                out_dir=REPORTS_DIR,
                model=model or analysis.model,
            )
            md_path = paths[variant]
            fmt_paths = {"md": md_path}
            other_formats = [f for f in formats if f != "md"]
            if other_formats and have_pandoc():
                fmt_paths.update(convert_all(md_path, other_formats))
            report_paths[variant] = fmt_paths

    return PipelineResult(
        metadata=meta,
        transcript=transcript,
        analysis=analysis.data,
        doc_paths=doc_paths,
        report_paths=report_paths,
    )
