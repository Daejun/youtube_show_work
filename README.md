# ytshow

Turn a YouTube URL into a fact-grounded **analysis document** and a **report**, in both a *minimal* and a *rich* style, in **English and Korean**.

For setup and how to run it, see **[USAGE.md](USAGE.md)**.

Two ways to run it:

- **As a Claude Code skill** (recommended) — no `ANTHROPIC_API_KEY` needed. The skill at [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md) auto-loads when you open this repo in Claude Code, and Claude Code itself performs the LLM steps in-session. Always produces a paired Korean variant.
- **As a Python CLI** — the original `ytshow` command that calls `api.anthropic.com` via the Anthropic SDK. Requires an API key, produces English reports only.

Both share the same deterministic plumbing (yt-dlp metadata, captions, document assembly, pandoc) and the same output layout.

## What it produces

For every video id `<id>`:

```
outputs/docs/<id>.minimal.md          # compact analysis doc (archive — every fact + full transcript)
outputs/docs/<id>.rich.md             # detailed analysis doc (metadata table, entities, quotes, full transcript)

outputs/reports/<id>.minimal.{md,pdf,docx}        # curated English report — minimal style
outputs/reports/<id>.rich.{md,pdf,docx}           # curated English report — rich style
outputs/reports/<id>.minimal.ko.{md,pdf,docx}     # Korean variant of the minimal report (skill flow only)
outputs/reports/<id>.rich.ko.{md,pdf,docx}        # Korean variant of the rich report (skill flow only)
```

**Analysis docs** are the archive — they include every per-chapter fact with `[mm:ss]` citations and the full timestamped transcript.

**Reports** are the reader-facing surface. In the skill flow they have no inline timestamps in the body (chapter heading time ranges are kept), they are curated rather than exhaustive, and they always come in EN/KO pairs. Verbatim quotes in reports are exact transcript substrings, validated by [scripts/grounding_check.py](scripts/grounding_check.py).

## Pipeline

```
URL
 └─ yt-dlp ........................ metadata + chapters
 └─ yt-dlp manual/auto subtitles (srt) — preferred
      └─ fallback: yt-dlp audio → faster-whisper (local STT)
 └─ extract_facts → JSON
      • skill flow: Claude Code does it directly (no API key)
      • CLI flow:   Anthropic SDK (claude-sonnet-4-6, with prompt caching)
 └─ build_document → outputs/docs/<id>.{minimal,rich}.md
 └─ analysis doc → reports
      • skill flow: Claude Code writes curated EN + KO reports
      • CLI flow:   Anthropic SDK writes EN reports per-variant
 └─ pandoc → .pdf, .docx
 └─ scripts/grounding_check.py → confirms every blockquote is a verbatim transcript substring
```

## Style: minimal vs rich

| | minimal | rich |
|---|---|---|
| Headers | `#`, `##` only | up to `####` |
| Tables | no | yes |
| Bold / italic | no | yes |
| Quotes | one-line bullet | blockquote with speaker attribution |
| Length | compact | thorough |
| Verbatim quotes | yes | yes |
| Inline timestamps in body (skill flow) | no | no |
| KO variant | yes (skill flow) | yes (skill flow) |

## Fact-grounding rules

Enforced by the prompts in [prompts/](prompts/) for the CLI flow, and by the skill instructions in [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md) for the skill flow:

- Use **only** what is in the transcript / analysis document.
- Quotes are verbatim substrings of the transcript.
- Names, quotes, and proper nouns are kept in their original language.
- If something is not stated, omit it. No guessing.

Additional editorial rules unique to the skill flow are documented in [USAGE.md § Editorial conventions](USAGE.md#editorial-conventions-skill-flow).

## Layout

```
.claude/skills/ytshow/SKILL.md   # the project-level skill — auto-loaded by Claude Code
src/ytshow/
  cli.py                         # ytshow analyze-cmd | report-cmd | run | metadata | video-id
  pipeline.py                    # end-to-end orchestration (CLI flow)
  fetch_metadata.py              # yt-dlp
  fetch_transcript.py            # youtube-transcript-api → faster-whisper fallback (CLI flow)
  analyze.py                     # Anthropic SDK → fact-extraction JSON (CLI flow)
  build_document.py              # JSON → minimal/rich Markdown analysis docs
  build_report.py                # analysis doc → minimal/rich Markdown reports (CLI flow)
  convert.py                     # pandoc → PDF / DOCX
  utils.py
scripts/
  fetch_only.py                  # skill-flow helper: yt-dlp subs + cache, bypasses youtube-transcript-api 1.x
  grounding_check.py             # verifies every blockquote body is a transcript substring (EN + KO)
prompts/
  extract_facts.md
  report_factual_minimal.md
  report_factual_rich.md
tests/
  test_utils.py
  test_grounding.py
outputs/                         # gitignored; generated per run
cache/                           # gitignored; per-video metadata / srt / bundle / facts / transcript
```

## Tests

```bash
pytest -q
```

Offline — does not hit the network or Claude. Checks id parsing, timestamp formatting, and that the document builder keeps quotes/facts grounded with timestamps.
