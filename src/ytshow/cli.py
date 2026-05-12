"""CLI entrypoint for ytshow."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from .analyze import analyze
from .build_document import write_documents
from .build_report import write_reports
from .convert import convert_all, have_pandoc
from .fetch_metadata import fetch_metadata
from .fetch_transcript import fetch_transcript
from .pipeline import run_pipeline
from .utils import DOCS_DIR, REPORTS_DIR, ensure_dirs, extract_video_id

app = typer.Typer(help="YouTube video -> fact-grounded analysis doc + report")
console = Console()


VARIANT_OPT = typer.Option(
    "both", "--variant", "-v", help="minimal | rich | both"
)
FORMAT_OPT = typer.Option(
    "md,pdf,docx", "--formats", "-f", help="comma-separated: md,pdf,docx"
)


def _parse_variants(v: str) -> list[str]:
    if v == "both":
        return ["minimal", "rich"]
    if v in {"minimal", "rich"}:
        return [v]
    raise typer.BadParameter("variant must be one of: minimal, rich, both")


def _parse_formats(f: str) -> list[str]:
    allowed = {"md", "pdf", "docx"}
    parts = [x.strip() for x in f.split(",") if x.strip()]
    bad = [p for p in parts if p not in allowed]
    if bad:
        raise typer.BadParameter(f"unsupported formats: {bad}")
    return parts


@app.command()
def analyze_cmd(
    url: str,
    languages: str = typer.Option("en", "--languages", "-l", help="comma-separated caption languages to try"),
    no_whisper: bool = typer.Option(False, help="disable Whisper STT fallback"),
    whisper_model: str = typer.Option("base.en", help="faster-whisper model size"),
    model: Optional[str] = typer.Option(None, "--model", help="override Claude model"),
):
    """Fetch metadata + transcript, run analysis, write both analysis docs (minimal & rich)."""
    ensure_dirs()
    langs = [x.strip() for x in languages.split(",") if x.strip()]

    console.print(f"[bold]fetching metadata[/bold] {url}")
    meta = fetch_metadata(url)
    console.print(f"  title: {meta.title}")
    console.print(f"  channel: {meta.channel}  duration: {meta.duration}s")

    console.print("[bold]fetching transcript[/bold]")
    canonical_url = f"https://www.youtube.com/watch?v={meta.video_id}"
    tr = fetch_transcript(
        canonical_url,
        meta.video_id,
        languages=langs,
        allow_whisper=not no_whisper,
        whisper_model=whisper_model,
    )
    console.print(f"  source: {tr.source} ({tr.language})  segments: {len(tr.segments)}")

    console.print("[bold]running analysis (Claude)[/bold]")
    a = analyze(meta, tr, model=model) if model else analyze(meta, tr)

    paths = write_documents(meta, tr, a.data)
    for k, p in paths.items():
        console.print(f"  wrote {k} -> {p}")


@app.command()
def report_cmd(
    doc: Path = typer.Argument(..., exists=True, readable=True, help="path to analysis doc .md"),
    variant: str = VARIANT_OPT,
    formats: str = FORMAT_OPT,
    model: Optional[str] = typer.Option(None, "--model", help="override Claude model"),
):
    """Generate report(s) from an existing analysis document."""
    ensure_dirs()
    variants = _parse_variants(variant)
    fmts = _parse_formats(formats)
    basename = doc.stem.split(".")[0]
    source_doc = doc.read_text(encoding="utf-8")

    paths = write_reports(basename, source_doc, variants, model=model or "claude-sonnet-4-6")
    for v, p in paths.items():
        console.print(f"  wrote {v} report -> {p}")
        other = [f for f in fmts if f != "md"]
        if other:
            if not have_pandoc():
                console.print("[yellow]pandoc not installed; skipping pdf/docx conversion[/yellow]")
            else:
                converted = convert_all(p, other)
                for fmt, cp in converted.items():
                    if fmt != "md":
                        console.print(f"    {fmt} -> {cp}")


@app.command()
def run(
    url: str,
    variant: str = VARIANT_OPT,
    formats: str = FORMAT_OPT,
    languages: str = typer.Option("en", "--languages", "-l"),
    no_whisper: bool = typer.Option(False, help="disable Whisper STT fallback"),
    whisper_model: str = typer.Option("base.en", help="faster-whisper model size"),
    model: Optional[str] = typer.Option(None, "--model"),
):
    """End-to-end: URL -> analysis docs -> report(s) -> (PDF/DOCX)."""
    variants = _parse_variants(variant)
    fmts = _parse_formats(formats)
    langs = [x.strip() for x in languages.split(",") if x.strip()]

    result = run_pipeline(
        url=url,
        variants=variants,
        formats=fmts,
        languages=langs,
        allow_whisper=not no_whisper,
        whisper_model=whisper_model,
        model=model,
    )

    console.print(f"[bold green]done[/bold green] {result.metadata.title}")
    for v, p in result.doc_paths.items():
        console.print(f"  doc[{v}] -> {p}")
    for v, fmt_paths in result.report_paths.items():
        for fmt, p in fmt_paths.items():
            console.print(f"  report[{v}.{fmt}] -> {p}")


@app.command()
def video_id(url: str):
    """Print the YouTube video id for a URL."""
    typer.echo(extract_video_id(url))


@app.command()
def metadata(url: str):
    """Dump raw metadata as JSON (no Claude calls)."""
    meta = fetch_metadata(url)
    typer.echo(json.dumps(meta.to_dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    app()
