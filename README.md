# ytshow

Turn a YouTube URL into a fact-grounded **analysis document** and a **report**, in both a *minimal* and a *rich* style.

## What it produces

For every video id `<id>`:

```
outputs/docs/<id>.minimal.md      # compact analysis doc (clean, header + bullets only)
outputs/docs/<id>.rich.md         # detailed analysis doc (metadata table, entities, quotes…)
outputs/reports/<id>.minimal.md   # fact-only report, minimal style
outputs/reports/<id>.rich.md      # fact-only report, rich style
outputs/reports/<id>.<variant>.pdf   # (optional, requires pandoc)
outputs/reports/<id>.<variant>.docx  # (optional, requires pandoc)
```

Both variants are **strictly fact-based**: every claim is grounded in the transcript and every sentence carries a `[mm:ss]` (or `[hh:mm:ss]`) citation. External knowledge, interpretation, and speculation are forbidden by the system prompts.

## Pipeline

```
URL
 └─ yt-dlp ............... metadata + chapters
 └─ youtube-transcript-api  manual captions → auto captions
      └─ fallback: yt-dlp audio → faster-whisper (local STT)
 └─ Claude (claude-sonnet-4-6, with prompt caching)
      └─ extract_facts: chapter splits, facts, quotes, entities, numbers
 └─ build_document → outputs/docs/<id>.{minimal,rich}.md
 └─ Claude → outputs/reports/<id>.{minimal,rich}.md   (per-variant prompt)
 └─ pandoc → .pdf, .docx (optional)
```

## Install

```bash
pip install -e .[stt]              # add ,test for pytest
```

System dependencies (for the optional bits):

- `ffmpeg` — required for the Whisper fallback (yt-dlp audio extraction)
- `pandoc` — required to produce `.pdf` / `.docx` from the Markdown
- For PDF, install one of `weasyprint`, `wkhtmltopdf`, or a TeX engine

Set your API key:

```bash
export ANTHROPIC_API_KEY=sk-...
# Optional: override the default model
export YTSHOW_MODEL=claude-sonnet-4-6
```

## Use

End-to-end:

```bash
ytshow run "https://www.youtube.com/live/a3-OJxxW810" --variant both --formats md,pdf,docx
```

Step by step:

```bash
ytshow analyze-cmd "https://www.youtube.com/live/a3-OJxxW810"
ytshow report-cmd outputs/docs/a3-OJxxW810.rich.md --variant rich --formats md,pdf,docx
```

Inspect metadata only (no Claude calls):

```bash
ytshow metadata "https://www.youtube.com/live/a3-OJxxW810"
```

## Style: minimal vs rich

| | minimal | rich |
|---|---|---|
| Headers | `#`, `##` only | up to `####` |
| Tables | no | yes |
| Bold/italic | no | yes |
| Quotes | one-line `>` | blockquote + context |
| Length | compact | thorough |
| Grounding rule | same | same |

## Fact-grounding rules (enforced by prompts)

- Use **only** what is in the transcript / analysis document.
- Every factual sentence ends with `[mm:ss]` or `[hh:mm:ss]`.
- Quotes are verbatim substrings of the transcript.
- Names, quotes, proper nouns are kept in their original language.
- If something is not stated, omit it or write `not stated in transcript`. No guessing.

## Layout

```
src/ytshow/
  cli.py              # `ytshow analyze-cmd | report-cmd | run | metadata | video-id`
  pipeline.py         # end-to-end orchestration
  fetch_metadata.py   # yt-dlp
  fetch_transcript.py # youtube-transcript-api → faster-whisper fallback
  analyze.py          # Claude → fact-extraction JSON
  build_document.py   # JSON → minimal/rich Markdown analysis docs
  build_report.py     # analysis doc → minimal/rich Markdown reports
  convert.py          # pandoc → PDF / DOCX
  utils.py
prompts/
  extract_facts.md
  report_factual_minimal.md
  report_factual_rich.md
tests/
  test_utils.py
  test_grounding.py
```

## Tests

```bash
pip install -e .[test]
pytest -q
```

Note: tests do not hit the network or Claude. They check id parsing, timestamp formatting, and that the document builder keeps quotes/facts grounded with timestamps.
