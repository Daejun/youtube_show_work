"""Convert Markdown documents to PDF and DOCX via pandoc."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def have_pandoc() -> bool:
    return shutil.which("pandoc") is not None


def _convert(md_path: Path, out_path: Path, extra_args: list[str] | None = None) -> Path:
    if not have_pandoc():
        raise RuntimeError("pandoc not found on PATH")
    cmd = ["pandoc", str(md_path), "-o", str(out_path)]
    if extra_args:
        cmd.extend(extra_args)
    subprocess.run(cmd, check=True)
    return out_path


def to_docx(md_path: Path, out_path: Path | None = None) -> Path:
    out = out_path or md_path.with_suffix(".docx")
    return _convert(md_path, out)


def to_pdf(md_path: Path, out_path: Path | None = None) -> Path:
    out = out_path or md_path.with_suffix(".pdf")
    # try a PDF engine that's commonly available; fall back to default
    for engine in ("weasyprint", "wkhtmltopdf", "xelatex", "pdflatex"):
        if shutil.which(engine):
            return _convert(md_path, out, ["--pdf-engine", engine])
    return _convert(md_path, out)


def convert_all(md_path: Path, formats: list[str]) -> dict[str, Path]:
    out: dict[str, Path] = {"md": md_path}
    for fmt in formats:
        if fmt == "pdf":
            out["pdf"] = to_pdf(md_path)
        elif fmt == "docx":
            out["docx"] = to_docx(md_path)
        elif fmt == "md":
            continue
        else:
            raise ValueError(f"unsupported format: {fmt}")
    return out
