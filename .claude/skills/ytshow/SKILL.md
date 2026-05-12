---
name: ytshow
description: Turn a YouTube URL into a fact-grounded analysis document and report (minimal and rich variants, md/pdf/docx, English + Korean) without spending an ANTHROPIC_API_KEY. Use when the user wants a summary, transcript-grounded report, fact-check, or speaker-attributed quote list from a YouTube video. Backed by this repository — deterministic plumbing (yt-dlp metadata, captions, build_document, pandoc) runs as Python; the LLM steps (extract_facts → JSON, analysis_doc → report) are performed by Claude Code directly. Outputs land in outputs/docs and outputs/reports.
---

# ytshow (skill flow)

This skill replaces the two `anthropic.Anthropic().messages.create(...)` calls in the upstream `ytshow` pipeline with direct work by Claude Code, so no `ANTHROPIC_API_KEY` is needed.

## When to use

Invoke when the user says any of:

- "make a report / summary / fact-check for `<YouTube URL>`"
- "extract verbatim quotes from `<YouTube URL>`"
- "produce minimal and rich versions of the analysis"
- "/ytshow `<URL>`"

Skip if the user wants **visual** content (slides, on-screen text, charts). This skill is transcript-only. Tell the user and stop, or offer to add a frame-sampling pass separately.

## Paths

All paths are **relative to the repository root**. Run from the repo root (`cd` into the cloned directory first). The skill ships inside the repo, so wherever the repo is cloned, the skill auto-loads alongside it.

- Venv: `.venv/` — created on first setup.
- Helper scripts: `scripts/fetch_only.py`, `scripts/grounding_check.py`.
- Prompts (read-only reference): `prompts/extract_facts.md`, `prompts/report_factual_minimal.md`, `prompts/report_factual_rich.md`.
- Cache: `cache/<video_id>.{metadata.json,en.srt,bundle.json,facts.json,transcript.txt}` — gitignored.
- Outputs: `outputs/{docs,reports}/<video_id>.<variant>[.ko].{md,pdf,docx}` — gitignored.

## Setup on a fresh clone

If `.venv/` does not exist, set it up once. Pick the section that matches the host OS.

### Linux / macOS / WSL2 (recommended)

```bash
# System deps (sudo on Linux; brew on macOS)
sudo apt-get install -y ffmpeg pandoc fonts-noto-cjk    # Debian/Ubuntu
# brew install ffmpeg pandoc                            # macOS

# Python venv + package + PDF engine
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e '.[stt,test]'
pip install weasyprint
```

### Windows (native PowerShell)

```powershell
# System deps
winget install -e --id Gyan.FFmpeg
winget install -e --id JohnMacFarlane.Pandoc
# Korean fonts: Windows already ships Malgun Gothic — no install needed.

# Python venv + package + PDF engine
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -U pip
pip install -e ".[stt,test]"
pip install weasyprint    # if this fails (GTK/Pango), install wkhtmltopdf instead:
                          # winget install -e --id wkhtmltopdf.wkhtmltox
```

`src/ytshow/convert.py` auto-detects the PDF engine in this order: `weasyprint → wkhtmltopdf → xelatex → pdflatex`. If weasyprint refuses to install on native Windows (this happens), `wkhtmltopdf` is the easiest fallback. The Korean Noto/Malgun glyphs work with all three.

### Verify (any OS)

```bash
python -m pytest -q              # 11 tests should pass
```

Korean PDF rendering check — only matters if the user will read KO PDFs. On Linux/WSL run `fc-list :lang=ko | head -1`; on Windows assume Malgun Gothic is installed.

No `ANTHROPIC_API_KEY` is needed — the skill flow performs the LLM work in-session.

### Shell command portability

All workflow snippets below use bash-style syntax (`source .venv/bin/activate`, forward-slash paths). On native Windows PowerShell, the only routine substitution you need is the venv activation:

| Linux / macOS / WSL2 / Git Bash | Native Windows PowerShell |
|---|---|
| `source .venv/bin/activate` | `.venv\Scripts\Activate.ps1` |
| `python3` | `python` |
| `python scripts/fetch_only.py "<URL>"` | identical (Python args are quoted-path-safe) |

Everything done through Python (`-c "..."`, the helpers in `scripts/`, the convert/build modules) is cross-platform — Pathlib normalizes separators, and pandoc/yt-dlp behave the same.

## Hard rules (carry over from `prompts/extract_facts.md`)

These are **load-bearing**. Reread the prompts on each run.

- Use **only** information present in the transcript. No outside knowledge, no inference, no opinions, no speculation.
- Quotes are **verbatim substrings** of a transcript segment — or a substring of the segments joined by a single space. The grounding check enforces this.
- Preserve the original language for names, quotes, and proper nouns. Do not romanize.
- If something is not stated, omit it or write `not stated in transcript`. Do not guess.
- No emoji. No decorative banners.

The "every factual sentence ends with `[mm:ss]`" rule from the upstream prompts applies to **facts JSON and analysis docs**, *not* to the reader-facing reports (see step 5 — reports have no timestamps).

## Workflow

Activate the venv first:

```bash
source .venv/bin/activate
```

### 1. Fetch metadata + transcript

```bash
python scripts/fetch_only.py "<URL>"
```

`fetch_only.py` uses yt-dlp for both metadata and captions (srt), falls back to faster-whisper STT only if no captions exist. It is **cache-aware**: if `cache/<id>.metadata.json` or `cache/<id>.<lang>.srt` already exist, it reuses them. This matters because YouTube rate-limits rapid metadata calls — retry with backoff.

The script writes `cache/<id>.bundle.json` and prints a one-line summary.

If you hit "Sign in to confirm you're not a bot" on a clean cache, wait ~30s and retry. If `SSL: CERTIFICATE_VERIFY_FAILED` shows up, it is almost always a transient YouTube/innertube glitch (the helper retries 3× already); verify the network is fine with `curl https://www.googleapis.com`.

### 2. Read the bundle as a flat transcript

```bash
python -c "
import json
b = json.load(open('cache/<id>.bundle.json'))
for s in b['transcript']['segments']:
    print(f\"[{s['ts']}] {s['text']}\")
" > cache/<id>.transcript.txt
```

Then `Read` the transcript file. Aim to load the **entire** transcript into your context. ~30 min videos (~25 KB text) fit easily. Above ~60 min (>~50 KB text), chunk per chapter.

### 3. Produce `cache/<id>.facts.json`

This is your version of the `extract_facts` LLM call. Output a single JSON object with **exactly** the keys defined in `prompts/extract_facts.md` (read that file each run to confirm the schema):

```
{
  "overview": "...",
  "chapters": [{"title", "start", "end", "facts": [...], "quotes": [{"speaker","text","time"}]}],
  "entities": {"people":[], "organizations":[], "products":[], "places":[]},
  "numbers": [{"value","context","time"}],
  "keywords": [...],
  "notes": [...]
}
```

Chapter splits come from YouTube chapters in the metadata when available; otherwise pick factual splits.

**Verify every quote is a verbatim transcript substring** before continuing:

```bash
python -c "
import json
b = json.load(open('cache/<id>.bundle.json'))
f = json.load(open('cache/<id>.facts.json'))
tx = ' '.join(s['text'] for s in b['transcript']['segments'])
segs = [s['text'] for s in b['transcript']['segments']]
missing = [(ch['title'], q['speaker'], q['text'])
           for ch in f['chapters']
           for q in ch.get('quotes', [])
           if q['text'] not in tx and not any(q['text'] in s for s in segs)]
print('missing:', len(missing))
for m in missing: print(' -', m)
"
```

If any quote is missing, rewrite it as a verbatim substring or remove it. Never leave a paraphrase inside quotation marks.

### 4. Build the two analysis documents

```bash
python -c "
import json
from ytshow.fetch_metadata import Metadata, Chapter
from ytshow.fetch_transcript import TranscriptResult, TranscriptSegment
from ytshow.build_document import write_documents
from ytshow.utils import DOCS_DIR, ensure_dirs
ensure_dirs()
b = json.load(open('cache/<id>.bundle.json'))
f = json.load(open('cache/<id>.facts.json'))
m = dict(b['metadata']); chapters = [Chapter(**c) for c in m.pop('chapters', [])]
meta = Metadata(chapters=chapters, **m)
segs = [TranscriptSegment(start=s['start'], end=s['end'], text=s['text']) for s in b['transcript']['segments']]
tr = TranscriptResult(segments=segs, source=b['transcript']['source'], language=b['transcript']['language'])
print(write_documents(meta, tr, f, out_dir=DOCS_DIR))
"
```

Produces `outputs/docs/<id>.minimal.md` and `outputs/docs/<id>.rich.md`. Pure Python templating — no LLM call.

### 5. Write the EN reports directly

Reread `prompts/report_factual_minimal.md` and `prompts/report_factual_rich.md` for the section structure. Then `Read` the analysis doc and `Write` each report.

Structure:

- `outputs/reports/<id>.minimal.md` — only `#` and `##` headers; no tables, bold, italic, emoji, or horizontal rules. Sections in order: title, `## Overview` (one short paragraph), `## Topics covered`, `## People, organizations, products`, `## Numbers and data points` (omit if none), `## Notable quotes`.
- `outputs/reports/<id>.rich.md` — up to `####` headers; tables and blockquotes OK. Sections in order: title, `## Metadata` (table), `## Executive summary`, `## Topics covered` with `###` per chapter, `## People, organizations, products, places`, `## Numbers and data points` (two-column table: Value | Context), `## Notable quotes` (blockquotes). **Do not add `## Transcript notes`** — the user does not want it.

**Reports MUST NOT contain timestamps in the body.** Inline `[mm:ss]` citations interrupt reading. This overrides the upstream "every factual sentence ends in `[mm:ss]`" rule for the *report* surface. The analysis docs still hold every timestamp, and the grounding check still validates verbatim quotes.

Concretely:

- Overview / Executive summary: no timestamps.
- `### chapter` intro paragraphs: no timestamps. Write a topic *label*, not a factual assertion. (e.g. "The October Galaxy XR launch, the first feature drop, and a sneak peek at autospatialization.")
- Bullets: no trailing `[mm:ss]`. Each bullet is just a fact sentence.
- Entity lists (People / Organizations / Products / Places): names only.
- Numbers table: two columns — `| Value | Context |`. Drop the Time column.
- Blockquotes: verbatim transcript text; speaker attribution line is just `— Speaker`.
- Chapter heading time ranges like `### Galaxy XR feature drop (07:00–11:42)` are OK — those are structural anchors, not inline citations.

**Reports are curated, NOT exhaustive.** The analysis docs are the archive. Reports pick the substantive announcements, demos, numbers, partnerships, and quotes, and **drop**:

- Host handoffs and tee-ups: "X hands over to Y", "let's check in with Z next", "back to you, A", "with that, I'm going to hand things over to…".
- Meta-narration about show staging: "Juston demonstrates by walking around and activating Gemini to ask questions".
- Closing-section recap that just repeats earlier announcements. If the closing introduces something new, keep that one line; otherwise drop the section entirely.
- Throwaway pleasantries: "Thanks, Sameer", "Hi everybody", "It's good to see you".
- Fragment quotes with no standalone meaning ("Take XREAL's Project Aura.", "Nano Banana really expands what you can").

If a transcript line is *just* a transition with no factual payload, it does not belong in the report — even though it stays in the analysis doc.

### 5b. Korean variant — always produce alongside English

Produce a Korean variant for each report at `outputs/reports/<id>.<variant>.ko.md`. The full set per video is `minimal.md`, `minimal.ko.md`, `rich.md`, `rich.ko.md`, plus their `.pdf` / `.docx`. The user wants both languages by default.

Translation rule — *prose only*:

- Section headers translate: `## Overview` → `## 개요`, `## Executive summary` → `## 핵심 요약`, `## Topics covered` → `## 다루는 주제`, `## People, organizations, products` → `## 인물 · 조직 · 제품`, `## Numbers and data points` → `## 수치 및 데이터`, `## Notable quotes` → `## 주요 인용`, `## Metadata` → `## 메타데이터`. Use `·` (middle dot, U+00B7) between joined nouns.
- Narrative paragraphs and bullet sentences translate to Korean.
- **Names, organizations, products, places stay in their original language** — Sameer, Shahram, Warby Parker, Gentle Monster, Android XR, Galaxy XR, Project Aura, Jetpack Glimmer, East Village. Do not romanize.
- **Verbatim quote bodies stay in the original language** — same English text as in the EN report. Only the section heading around quotes is Korean. Quote attribution stays `— Speaker`.
- **Numbers table cell values stay original** — `October`, `over 60`, `next year`, dollar amounts (e.g. one-dollar-per-month pricing copied verbatim from the transcript). Only the Context column is translated. Avoid writing a literal dollar-sign-followed-by-digit anywhere in **this SKILL.md** because Claude Code's slash-command handler substitutes those tokens with positional args from the user's invocation; in the actual report markdown the original dollar text renders fine, since reports are produced by the `Write` tool, not by slash-command expansion.
- Chapter heading time ranges translate the descriptor, keep product names English: `### Galaxy XR feature drop (07:00–11:42)` → `### Galaxy XR 기능 업데이트 (07:00–11:42)`.

This preserves grounding: the same English verbatim quotes appear in both EN and KO reports, so `scripts/grounding_check.py` matches them against the analysis-doc transcript section regardless of language.

If the source video is in a language other than English, the rule flips automatically: the EN report becomes a Korean-or-original-language summary and the `.ko.md` is the explicit Korean version. Quotes always stay in the transcript's original language.

### 6. Convert to PDF + DOCX

```bash
python -c "
from pathlib import Path
from ytshow.convert import convert_all
for v in ('minimal', 'rich', 'minimal.ko', 'rich.ko'):
    md = Path(f'outputs/reports/<id>.{v}.md')
    if md.exists():
        out = convert_all(md, ['pdf', 'docx'])
        print(v, out)
"
```

PDF engine: weasyprint (in the venv). Pandoc will warn about unsupported CSS — cosmetic, safe to ignore. Korean PDFs are ~10× larger than English (300–550 KB vs 20–40 KB) because Noto Sans CJK is embedded. If KO PDFs show boxes/tofu instead of Korean glyphs, install `fonts-noto-cjk`.

### 7. Grounding check

```bash
python scripts/grounding_check.py <id>
```

Confirms every blockquote body (excluding `— speaker` attribution) in every report file (EN minimal, EN rich, KO minimal, KO rich) appears in the `## Full transcript` section of the rich analysis doc. Must report `OK`. If `WARNING: N unmatched`, fix those quotes — never ship a report with ungrounded quotes.

### 8. Final inventory

Fourteen files per video (2 analysis docs + 4 reports × 3 formats):

- `outputs/docs/<id>.minimal.md`
- `outputs/docs/<id>.rich.md`
- `outputs/reports/<id>.minimal.{md,pdf,docx}`
- `outputs/reports/<id>.rich.{md,pdf,docx}`
- `outputs/reports/<id>.minimal.ko.{md,pdf,docx}`
- `outputs/reports/<id>.rich.ko.{md,pdf,docx}`

Show the user a summary and the first ~30 lines of each report.

### 9. Commit and push outputs

`outputs/` is tracked in git so reports sync across machines. After a successful run (grounding check `OK`, all 14 files present), commit and push:

```bash
git add outputs/docs/<id>.* outputs/reports/<id>.*
git commit -m "Add ytshow outputs for <video-title-or-id> (<id>)"
git push
```

Notes:

- Use a descriptive commit message: video title in plain ASCII if possible, with the video id in parentheses (e.g. `Add ytshow outputs for The Android Show XR Edition (a3-OJxxW810)`). The id matters most — it is the unique key.
- Stage only the new video's files. Don't bulk-add unrelated changes the user may have in flight (`git status` first if uncertain).
- If the push is rejected because the remote moved, do a `git pull --rebase` and try again. Don't force-push — the outputs branch is shared.
- `cache/` is still gitignored and stays local. Other machines regenerate it on demand.
- If the user explicitly says "don't push" or "skip push" for this run, skip this step. The default is to push.

After push, tell the user the commit hash and confirm the remote is in sync.

## Token / context budget

Approximate the formatted transcript at `duration_seconds * 18` characters (~14 chars/sec of English speech plus `[mm:ss]` prefix overhead). Roughly 4 chars per token, so:

| Video length | Transcript text | Tokens |
|---|---|---|
| 30 min | ~31 KB | ~8K |
| 60 min | ~63 KB | ~16K |
| 2 hr | ~125 KB | ~32K |
| 3 hr | ~190 KB | ~48K |

The model's 200K-token context window easily holds **up to ~2–3 hours of video** alongside the system prompt, your reasoning, and the output JSON. No chunking is needed for typical 30–60 min videos.

**Chunk above ~3 hours** (lectures, full conference recordings, marathon livestreams) to keep long-context attention quality high: process chapters one at a time, producing per-chapter `facts[]` and `quotes[]`, then merge into a single `facts.json` before step 4.

If the transcript is in a high-density language (Korean, Japanese, Chinese), the chars/sec rate is similar but each character is more tokens — divide the chunk threshold by ~2 for those.

## What this skill does **not** handle

- **Visual content** (slides, on-screen text, demos, chart contents). Transcript only.
- **Live, currently-airing streams** with no captions yet. Wait for the replay's captions, or fall back to Whisper STT (slow, no speaker labels).
- **Non-English videos without manual captions.** Auto-captions are much less clean; the Whisper fallback default is `base.en` — pass `--whisper-model medium` for better non-English quality.

## Common failure modes

| Symptom | Cause | Fix |
|---|---|---|
| `AttributeError: ... has no attribute 'list_transcripts'` | upstream `fetch_transcript.py` uses youtube-transcript-api 0.6.x API; the package on PyPI is now 1.x | use `scripts/fetch_only.py` — it bypasses youtube-transcript-api entirely |
| `Sign in to confirm you're not a bot` | YouTube rate-limit / anti-bot trip | wait 30s and retry; helper caches metadata + captions so re-runs don't re-hit YouTube |
| `SSL: CERTIFICATE_VERIFY_FAILED` from yt-dlp | transient YouTube innertube glitch (not a real cert problem) | retry; helper has 3× backoff. Verify with `curl https://www.googleapis.com` |
| pandoc PDF fails with "weasyprint not found" | venv not activated or weasyprint not installed | `source .venv/bin/activate && pip install weasyprint` |
| KO PDF shows tofu (□□□) instead of Korean | no CJK font | `sudo apt install fonts-noto-cjk` |
| Grounding check warns | paraphrased quote in report | rewrite as a verbatim transcript substring |
