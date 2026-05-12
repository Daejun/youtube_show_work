"""Generate fact-grounded reports (minimal and rich) from an analysis document.

Both variants share the same analysis-document context, so we use prompt
caching on that block to keep cost low when generating both.
"""
from __future__ import annotations

import os
from pathlib import Path

from anthropic import Anthropic

from .utils import REPORTS_DIR, read_prompt

DEFAULT_MODEL = os.environ.get("YTSHOW_MODEL", "claude-sonnet-4-6")

VARIANT_PROMPTS = {
    "minimal": "report_factual_minimal.md",
    "rich": "report_factual_rich.md",
}


def generate_report(
    analysis_doc_markdown: str,
    variant: str,
    model: str = DEFAULT_MODEL,
    client: Anthropic | None = None,
) -> str:
    if variant not in VARIANT_PROMPTS:
        raise ValueError(f"unknown variant: {variant}")

    client = client or Anthropic()
    system_prompt = read_prompt(VARIANT_PROMPTS[variant])

    user_content = [
        {
            "type": "text",
            "text": "# Analysis document (fact source)\n\n" + analysis_doc_markdown,
            "cache_control": {"type": "ephemeral"},
        },
        {
            "type": "text",
            "text": (
                "Using ONLY the analysis document above, write the report described "
                "in the system prompt. Output Markdown only."
            ),
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
    return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text").strip()


def write_reports(
    basename: str,
    analysis_doc_markdown: str,
    variants: list[str],
    out_dir: Path = REPORTS_DIR,
    model: str = DEFAULT_MODEL,
    client: Anthropic | None = None,
) -> dict[str, Path]:
    """Write report markdowns named ``<basename>.<variant>.md``.

    ``basename`` is typically the slug returned by
    :func:`ytshow.build_document.write_documents`, but accepts any
    filename-safe string (e.g. a legacy video id).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    client = client or Anthropic()
    paths: dict[str, Path] = {}
    for v in variants:
        md = generate_report(analysis_doc_markdown, v, model=model, client=client)
        p = out_dir / f"{basename}.{v}.md"
        p.write_text(md, encoding="utf-8")
        paths[v] = p
    return paths
