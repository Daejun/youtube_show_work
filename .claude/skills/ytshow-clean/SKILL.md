---
name: ytshow-clean
description: Delete previously-generated ytshow analysis docs and reports for a specific YouTube video (or all videos) under this repo's outputs/ directory, then commit and push the deletion so other machines also drop them on `git pull`. Use when the user says "delete the report for X", "remove old outputs", "clean up the reports for video Y", "기존 리포트 삭제", "이 영상 보고서 지워줘", or "/ytshow-clean <URL or id>". Optionally also clears the cache for the same id.
---

# ytshow-clean (skill flow)

Companion to the `ytshow` skill. Removes generated artifacts under `outputs/` (and optionally `cache/`) for one or all videos, then commits and pushes so the deletion propagates.

## When to use

Invoke when the user says:

- "기존 리포트 삭제해줘", "이 영상 보고서 지워줘"
- "delete / remove / clean up the reports for `<URL>` (or `<video_id>`)"
- "clear all outputs", "전체 보고서 다 비워줘"
- "/ytshow-clean `<URL or id>`"

Do **not** invoke for: editing one report (use the `ytshow` skill to regenerate), or for changes that aren't outputs (those are not in scope).

## Paths the skill touches

All paths are relative to the repository root (run from there).

Per-video outputs live under a slug-based basename (see the `ytshow` skill for how the slug is derived from the title):

- `outputs/docs/<slug>.minimal.md`
- `outputs/docs/<slug>.rich.md`
- `outputs/reports/<slug>.minimal.{md,pdf,docx}`
- `outputs/reports/<slug>.rich.{md,pdf,docx}`
- `outputs/reports/<slug>.minimal.ko.{md,pdf,docx}`
- `outputs/reports/<slug>.rich.ko.{md,pdf,docx}`
- `outputs/INDEX.md` — shared map; the row for the deleted slug should be dropped, not the whole file.
- (optional, only if the user asks) `cache/<id>.{metadata.json,en.srt,bundle.json,facts.json,transcript.txt}` — cache stays keyed by YouTube id.

The first set is tracked in git. `cache/` is gitignored.

## Workflow

### 1. Resolve the slug (or "all")

The user supplies a YouTube URL, a bare 11-char id, a slug, or the literal word "all" / "전체". Files are named by slug, so resolve to a slug before deleting:

```bash
source .venv/bin/activate
python -c "
import sys
from ytshow.utils import extract_video_id, resolve_slug_from_id
arg = sys.argv[1]
try:
    vid = extract_video_id(arg)
    slug = resolve_slug_from_id(vid) or vid
except ValueError:
    slug = arg  # treat as an already-resolved slug
print(slug)
" "<URL, id, or slug>"
```

If the user said "all" / "전체", skip the resolver and act on every slug present under `outputs/` (each unique basename in `outputs/docs/*.rich.md`).

### 2. Show what will be deleted, get confirmation

List the files that exist for that slug before deleting. **Never delete silently.** Even though `git` allows recovery via reflog/history, the user should see the blast radius first.

```bash
ls -la outputs/docs/<slug>.* outputs/reports/<slug>.* 2>/dev/null || echo "no files for <slug>"
```

Print the list and ask the user to confirm in one of:

- "OK, delete" / "yes" / "응" / "지워"
- "abort" / "no" / "취소"

If the user already said something unambiguous like "지워" / "delete it" in the triggering message, skip the explicit confirmation prompt. Just summarize what is about to be deleted and proceed.

For "all", also list how many slugs are covered: e.g. "3 slugs found: android-show-io-edition-2026, foo-bar-baz-2025, lorem-ipsum-2024 — 42 files total."

### 3. Delete the files

```bash
# Single video
rm -f outputs/docs/<slug>.minimal.md outputs/docs/<slug>.rich.md \
      outputs/reports/<slug>.minimal.md outputs/reports/<slug>.minimal.pdf outputs/reports/<slug>.minimal.docx \
      outputs/reports/<slug>.rich.md outputs/reports/<slug>.rich.pdf outputs/reports/<slug>.rich.docx \
      outputs/reports/<slug>.minimal.ko.md outputs/reports/<slug>.minimal.ko.pdf outputs/reports/<slug>.minimal.ko.docx \
      outputs/reports/<slug>.rich.ko.md outputs/reports/<slug>.rich.ko.pdf outputs/reports/<slug>.rich.ko.docx

# All
git ls-files outputs/ | grep -v '^outputs/INDEX\.md$' | xargs -r rm -f
```

Windows PowerShell equivalent for a single slug:

```powershell
Remove-Item -ErrorAction SilentlyContinue `
  outputs\docs\<slug>.minimal.md, outputs\docs\<slug>.rich.md, `
  outputs\reports\<slug>.*
```

After deleting the per-video files, drop the matching row from `outputs/INDEX.md`. The simplest way is to clear `cache/<id>.bundle.json` then regenerate the index by walking remaining docs — or just hand-edit the table to remove the slug row. Do not delete the whole `INDEX.md`; other videos still need their rows.

Only touch tracked files. Do not blow away `.gitkeep` placeholders if they exist.

### 4. Cache (only if asked)

If the user wants the cache cleared too (e.g. "전부 다 지워" / "also clear cache"):

```bash
rm -f cache/<id>.*
```

For "all":

```bash
# Don't `rm -rf cache/` — keep the directory itself.
rm -f cache/*.metadata.json cache/*.en.srt cache/*.bundle.json cache/*.facts.json cache/*.transcript.txt
```

The user should be told that clearing the cache means the next ytshow run for the same id will re-fetch from YouTube (which can trip rate limits).

### 5. Commit the deletion and push

`outputs/` is tracked. Stage the deletion, commit, push:

```bash
git add -A outputs/
git status --short
git commit -m "Remove ytshow outputs for <id-or-summary>"
git push
```

Commit message guidance:

- Single video: `Remove ytshow outputs for <video-title-or-id> (<id>)`. The id matters most.
- Multiple videos: `Remove ytshow outputs for <N> videos (<id1>, <id2>, ...)`.
- All: `Remove all ytshow outputs from outputs/`.

Skip the push if the user explicitly said "don't push" or "local only".

### 6. Report what happened

Tell the user:

- The slug(s) (with corresponding video id) and file count actually deleted.
- The commit hash.
- Whether the push succeeded (and the remote branch).
- Whether the cache was also cleared.

## Edge cases

| Situation | Behavior |
|---|---|
| The slug has no files under `outputs/` | Report "no outputs found for `<slug>`" and stop. Don't commit an empty change. |
| Some of the 14 files are missing | Delete what exists, ignore the rest, proceed. The user may have run a previous partial run. |
| The user supplies "all" but `outputs/` is empty (only `.gitkeep`) | Tell them, do nothing. |
| `git push` fails because remote moved | `git pull --rebase` then push again. Don't force-push. |
| The user pasted multiple URLs at once | Resolve each to an id, ask once for confirmation across the whole set, then delete and make one commit covering all of them. |
| The user wants `cache/` cleared but `outputs/` kept | Just delete cache files; no git operation (cache is gitignored). |
| The repo has uncommitted unrelated changes in flight | Stage only `outputs/` paths with explicit file lists, not `git add -A`. The "all" delete path uses `git add -A outputs/` which is scoped to outputs/ and safe. |

## What this skill does not do

- It does not regenerate reports — that is the `ytshow` skill's job.
- It does not edit reports (e.g. fix a quote, change a section). Regenerate via `ytshow` instead.
- It does not touch the analysis-document `.gitkeep` markers.
- It does not delete the skill files themselves (`.claude/skills/`), source code (`src/`, `scripts/`), prompts, tests, or anything outside `outputs/` and (optionally) `cache/`.
