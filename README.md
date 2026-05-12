# ytshow

Turn a YouTube URL into a fact-grounded **analysis document** and a **report**, in both a *minimal* and a *rich* style, in **English and Korean**.

Two ways to run it:

- **As a Claude Code skill (recommended).** No `ANTHROPIC_API_KEY` needed — Claude Code itself does the inference. The skill is bundled in this repo at `.claude/skills/ytshow/` and auto-loads when you open the project in Claude Code. See [Use it as a skill](#use-it-as-a-skill).
- **As a Python CLI with an Anthropic API key.** The original `ytshow run …` flow that calls `api.anthropic.com` directly. See [Use it as a CLI](#use-it-as-a-cli).

Both flows share the same deterministic plumbing (yt-dlp metadata, caption fetching, document assembly, pandoc) and produce the same output layout.

## What it produces

For every video id `<id>`:

```
outputs/docs/<id>.minimal.md          # compact analysis doc (archive — keeps every fact + full transcript)
outputs/docs/<id>.rich.md             # detailed analysis doc (metadata table, entities, quotes, full transcript)

outputs/reports/<id>.minimal.{md,pdf,docx}        # curated English report — minimal style
outputs/reports/<id>.rich.{md,pdf,docx}           # curated English report — rich style
outputs/reports/<id>.minimal.ko.{md,pdf,docx}     # Korean variant of the minimal report
outputs/reports/<id>.rich.ko.{md,pdf,docx}        # Korean variant of the rich report
```

**Analysis docs** are the archive — they include every per-chapter fact with `[mm:ss]` citations and the full timestamped transcript.

**Reports** are the reader-facing surface:

- No inline timestamps anywhere in the body (citations interrupt reading).
- Curated, not exhaustive — host handoffs, tee-ups ("X will explain next"), recap-only closings, and throwaway pleasantries are dropped.
- Korean variant translates *prose only*: person names, organizations, products, places, and verbatim quote bodies stay in the original language.

Verbatim quotes in reports remain exact transcript substrings and are validated by [scripts/grounding_check.py](scripts/grounding_check.py).

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
      • CLI flow:   Anthropic SDK writes EN reports per-variant (no KO in CLI mode)
 └─ pandoc → .pdf, .docx
 └─ scripts/grounding_check.py → confirms every blockquote is a verbatim transcript substring
```

The youtube-transcript-api breakage in 1.x (the upstream code at [src/ytshow/fetch_transcript.py](src/ytshow/fetch_transcript.py) was written against 0.6.x) is bypassed in the skill flow by [scripts/fetch_only.py](scripts/fetch_only.py), which uses yt-dlp for captions.

## Setup on a fresh clone

```bash
# system deps (sudo)
sudo apt-get install -y ffmpeg pandoc fonts-noto-cjk

# python venv + package + PDF engine
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e '.[stt,test]'
pip install weasyprint

# sanity
python -m pytest -q              # 11 tests should pass (offline, no Claude)
fc-list :lang=ko | head -1       # confirms Korean fonts for KO PDFs
which ffmpeg pandoc              # both required
```

System dependencies:

- `ffmpeg` — Whisper STT fallback (only used when no captions are available).
- `pandoc` — `.pdf` / `.docx` conversion from Markdown.
- `weasyprint` — pandoc PDF engine (pip-installable, pure Python).
- `fonts-noto-cjk` — Korean glyphs in PDFs.

## Use it as a skill

Open this repo in Claude Code. The skill is at [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md) and is auto-discovered. Then ask Claude Code something like:

> /ytshow https://www.youtube.com/watch?v=XXXXXXXXXXX
>
> 또는: 이 영상 분석/보고서 만들어줘 https://youtu.be/XXXXX

Claude Code will run the deterministic helpers ([scripts/fetch_only.py](scripts/fetch_only.py), [src/ytshow/build_document.py](src/ytshow/build_document.py), [src/ytshow/convert.py](src/ytshow/convert.py), [scripts/grounding_check.py](scripts/grounding_check.py)) and perform the two LLM steps directly. Output: all 14 files listed above. No `ANTHROPIC_API_KEY` is consumed.

The skill enforces the project's editorial rules: curated reports, no inline timestamps, no `## Transcript notes` section, always-paired Korean variant. Full rules in [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md).

## Use it as a CLI

The original `ytshow` CLI is still wired up and calls Claude via the Anthropic SDK. It does **not** produce KO variants and does **not** apply the curation/no-timestamp editorial rules — those are skill-flow conventions.

Set your API key:

```bash
export ANTHROPIC_API_KEY=sk-...
# Optional: override the default model
export YTSHOW_MODEL=claude-sonnet-4-6
```

End-to-end:

```bash
ytshow run "https://www.youtube.com/live/XXXX" --variant both --formats md,pdf,docx
```

Step by step:

```bash
ytshow analyze-cmd "https://www.youtube.com/live/XXXX"
ytshow report-cmd outputs/docs/XXXX.rich.md --variant rich --formats md,pdf,docx
```

Metadata only (no Claude calls):

```bash
ytshow metadata "https://www.youtube.com/live/XXXX"
```

Heads-up — at the time of writing, `youtube-transcript-api` 1.x removed the `list_transcripts` class method that [src/ytshow/fetch_transcript.py](src/ytshow/fetch_transcript.py) calls; if the captions step errors with `AttributeError`, either pin the dependency to `youtube-transcript-api>=0.6,<1.0` or switch to the skill flow (which uses `scripts/fetch_only.py`).

## Style: minimal vs rich

| | minimal | rich |
|---|---|---|
| Headers | `#`, `##` only | up to `####` |
| Tables | no | yes |
| Bold / italic | no | yes |
| Quotes | one-line `>` (per-quote bullet in skill flow) | blockquote with speaker attribution |
| Length | compact | thorough |
| Verbatim quotes | yes | yes |
| Inline timestamps in body (skill flow) | no | no |
| KO variant | yes | yes |

## Fact-grounding rules

Enforced by the prompts in [prompts/](prompts/) for the CLI flow, and by the skill instructions in [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md) for the skill flow:

- Use **only** what is in the transcript / analysis document.
- Quotes are verbatim substrings of the transcript.
- Names, quotes, and proper nouns are kept in their original language.
- If something is not stated, omit it. No guessing.

Additional editorial rules in the **skill flow** (not enforced by the CLI):

- Reports are curated, not exhaustive. Drop handoffs, tee-ups, meta-narration, closing-recap, and fragment quotes. The analysis doc remains the exhaustive archive.
- Reports contain no inline timestamps; chapter heading time ranges like `(07:00–11:42)` are kept as structural anchors.
- No `## Transcript notes` section in reports.
- Always produce a paired Korean report (`<id>.<variant>.ko.md`) alongside the English one.

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
  fetch_only.py                  # skill-flow helper: yt-dlp subs + cache, bypasses youtube-transcript-api
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
pip install -e .[test]
pytest -q
```

Offline — does not hit the network or Claude. Checks id parsing, timestamp formatting, and that the document builder keeps quotes/facts grounded with timestamps.
