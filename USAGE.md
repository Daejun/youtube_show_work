# Using ytshow

How to set up and run the pipeline on a fresh machine. For what the project does and what it produces, see [README.md](README.md).

There are two ways to run it:

- **As a Claude Code skill** (recommended) — no `ANTHROPIC_API_KEY` needed; Claude Code does the inference. Always produces Korean variants alongside English. See [Skill flow](#skill-flow).
- **As a Python CLI** — the original `ytshow` CLI that calls `api.anthropic.com` directly. Requires an API key, produces English reports only. See [CLI flow](#cli-flow).

Both share the same setup.

## Setup on a fresh clone

### Linux / macOS / WSL2 (recommended)

```bash
# 1. System dependencies (sudo on Linux; brew on macOS)
sudo apt-get install -y ffmpeg pandoc fonts-noto-cjk    # Debian/Ubuntu
# brew install ffmpeg pandoc                            # macOS

# 2. Python venv + package + PDF engine
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e '.[stt,test]'
pip install weasyprint

# 3. Sanity check
python -m pytest -q              # 11 tests should pass (offline; no Claude)
fc-list :lang=ko | head -1       # confirms Korean fonts for KO PDFs
which ffmpeg pandoc              # both required
```

### Windows

Two options:

1. **WSL2 (recommended)** — install Ubuntu under WSL2, then use the Linux setup above. The Claude Code VSCode extension supports the WSL backend, and everything in this repo (including the bash snippets in [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md)) just works.
2. **Native Windows + PowerShell**:

   ```powershell
   # System deps
   winget install -e --id Gyan.FFmpeg
   winget install -e --id JohnMacFarlane.Pandoc
   # Korean fonts: Windows ships Malgun Gothic — no install needed.

   # Python venv + package + PDF engine
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -U pip
   pip install -e ".[stt,test]"
   pip install weasyprint    # if this fails (GTK/Pango), use wkhtmltopdf:
                             # winget install -e --id wkhtmltopdf.wkhtmltox

   # Sanity check
   python -m pytest -q
   ```

   [src/ytshow/convert.py](src/ytshow/convert.py) auto-detects the PDF engine in the order `weasyprint → wkhtmltopdf → xelatex → pdflatex`. If weasyprint refuses to install on native Windows (it sometimes does), `wkhtmltopdf` is the easiest fallback and renders Korean glyphs from Malgun Gothic without extra config.

### System dependencies

| Package | Why |
|---|---|
| `ffmpeg` | Whisper STT fallback when no captions are available |
| `pandoc` | `.pdf` / `.docx` conversion from Markdown |
| `weasyprint` (or `wkhtmltopdf` on native Windows) | pandoc's PDF engine |
| `fonts-noto-cjk` (Linux/WSL2) / Malgun Gothic (Windows built-in) | Korean glyphs in PDFs |

No `ANTHROPIC_API_KEY` is needed for the skill flow.

## Skill flow

Open this repo in Claude Code. The skill at [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md) is auto-discovered. Then ask Claude Code:

```
/ytshow https://www.youtube.com/watch?v=XXXXXXXXXXX
```

or natural language, in any language:

```
이 영상 분석/보고서 만들어줘 https://youtu.be/XXXXXXXXXXX
make a report for https://www.youtube.com/live/XXXXXXXXXXX
extract verbatim quotes from <URL>
```

Claude Code will:

1. Run [scripts/fetch_only.py](scripts/fetch_only.py) for metadata + captions (with cache, retry, and Whisper fallback).
2. Read the transcript and produce `cache/<id>.facts.json` per [prompts/extract_facts.md](prompts/extract_facts.md).
3. Run `build_document` to produce two analysis docs (the exhaustive archive).
4. Write four curated reports (EN minimal/rich + KO minimal/rich) — no inline timestamps, no `## Transcript notes`, paired Korean variant.
5. Convert each report to PDF + DOCX via pandoc.
6. Run [scripts/grounding_check.py](scripts/grounding_check.py) to verify every blockquote body is verbatim transcript.
7. **Commit the 14 new output files to git and push to `origin/main`** so the reports sync across machines. `cache/` stays local. To opt out of the push for a single run, tell Claude Code "don't push" in the same message that triggers the skill.

Output per video: 14 files in `outputs/docs/` (2 analysis docs) and `outputs/reports/` (4 reports × md/pdf/docx). Tracked in git; pulling on another machine fetches them.

The skill's full instructions — including chunking guidance for >60 min videos, translation rules, and editorial conventions — live in [.claude/skills/ytshow/SKILL.md](.claude/skills/ytshow/SKILL.md). The skill is self-contained: read it once and you know exactly what the skill flow does.

### Deleting old reports

A companion skill at [.claude/skills/ytshow-clean/SKILL.md](.claude/skills/ytshow-clean/SKILL.md) removes the 14 output files for a given video id (or all videos) and commits + pushes the deletion. Trigger it with:

```
/ytshow-clean https://www.youtube.com/watch?v=XXXXXXXXXXX
이 영상 보고서 지워줘 <URL>
delete reports for <id>
```

It does not regenerate anything — if you want to refresh, run `ytshow-clean` first, then `ytshow` again.

## CLI flow

The original Python CLI. It does **not** produce Korean variants and does **not** apply the skill-flow editorial rules (curation, no inline timestamps, no Transcript notes section). Use when you want the upstream prompt-driven behavior verbatim.

Set the API key:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export YTSHOW_MODEL=claude-sonnet-4-6   # optional; this is the default
```

End-to-end:

```bash
ytshow run "https://www.youtube.com/live/XXXXXXXXXXX" --variant both --formats md,pdf,docx
```

Step by step:

```bash
ytshow metadata "https://www.youtube.com/live/XXXXXXXXXXX"      # no Claude call
ytshow analyze-cmd "https://www.youtube.com/live/XXXXXXXXXXX"   # Claude: facts JSON + docs
ytshow report-cmd outputs/docs/XXXXXXXXXXX.rich.md --variant rich --formats md,pdf,docx
```

Heads-up: the captions step in the CLI calls `youtube-transcript-api.list_transcripts(...)`, which was removed in v1.x. If you hit `AttributeError`, either pin the dependency (`pip install 'youtube-transcript-api>=0.6,<1.0'`) or switch to the skill flow (which uses [scripts/fetch_only.py](scripts/fetch_only.py) for captions).

## Editorial conventions (skill flow)

These do not apply to the CLI flow.

- **Reports are curated, not exhaustive.** The analysis doc (`outputs/docs/`) holds every fact and the full transcript. Reports drop host handoffs ("X hands over to Y"), tee-ups ("let's check in with Z"), meta-narration about show staging, closing-section recap, throwaway pleasantries, and fragment quotes that have no standalone meaning.
- **No inline timestamps in the report body.** No `[mm:ss]` after bullets, in paragraphs, after entity names, or after speaker attribution. Chapter heading time ranges like `### Galaxy XR feature drop (07:00–11:42)` are kept as structural anchors. The analysis doc still carries every timestamp.
- **No `## Transcript notes` section** in reports. Caveats about caption gaps stay in `analysis.notes` inside the facts JSON if relevant.
- **Always produce a paired Korean variant.** Naming: `<id>.<variant>.ko.{md,pdf,docx}`. Translation rule — *prose only*: section headers and narrative translate to Korean; **names, organizations, products, places, and verbatim quote bodies stay in the source-transcript language**. Numbers-table cell values stay original; only the Context column translates.

The grounding check ([scripts/grounding_check.py](scripts/grounding_check.py)) verifies every report blockquote body (EN + KO) is a verbatim substring of the rich analysis doc's `## Full transcript` section. Run it after every change:

```bash
python scripts/grounding_check.py <video_id>
```

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `AttributeError: ... has no attribute 'list_transcripts'` | CLI flow uses youtube-transcript-api 0.6.x API; the package on PyPI is 1.x | Pin to `youtube-transcript-api>=0.6,<1.0`, or use the skill flow |
| `Sign in to confirm you're not a bot` | YouTube rate-limit / anti-bot trip on rapid yt-dlp calls | Wait ~30s and retry; [scripts/fetch_only.py](scripts/fetch_only.py) caches metadata + srt so re-runs don't re-hit YouTube |
| `SSL: CERTIFICATE_VERIFY_FAILED` from yt-dlp | Transient YouTube innertube glitch (not a real cert issue) | Retry — the helper backs off 3×. Sanity-check the network with `curl https://www.googleapis.com` |
| pandoc PDF fails with "weasyprint not found" | Venv not activated, or weasyprint not installed | `source .venv/bin/activate && pip install weasyprint` |
| KO PDF shows □□□ (tofu) | No CJK font on the system | `sudo apt install fonts-noto-cjk` |
| KO PDFs are 10× larger than EN | Noto Sans CJK is embedded into each KO PDF | Expected — Korean PDFs are 300–550 KB vs 20–40 KB for EN |
| Grounding check warns about unmatched quote | Paraphrased quote inside `"..."` in a report, or quote text doesn't match transcript word-for-word | Rewrite the quote as a verbatim substring of a transcript segment (or of segments joined by a single space) |
| Skill not appearing in `/` menu | Repo not opened as a Claude Code workspace | Open the repo root folder in Claude Code; skills load from `.claude/skills/<name>/SKILL.md` relative to the workspace |

## Token / context budget for the skill flow

Approximate transcript size as `duration_seconds × 80` characters (English caption rate). At 30 min that's ~25 KB and fits in context easily. Above ~60 min (>~50 KB text), Claude Code chunks per chapter inside the skill — produce `facts[]` and `quotes[]` chapter by chapter, then merge into one `facts.json` before building docs.

## What this pipeline does not handle

- **Visual content** (slides, on-screen text, demos, chart contents). Transcript only.
- **Live, currently-airing streams** with no captions yet. Wait for the replay's captions, or fall back to Whisper STT (slow, no speaker labels).
- **Non-English videos without manual captions.** Auto-captions are much less clean; the Whisper fallback default is `base.en` — pass `--whisper-model medium` (or larger) for non-English audio.
