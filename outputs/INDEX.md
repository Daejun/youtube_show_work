# Outputs index

This file maps each output slug to the source YouTube video so the filenames in `outputs/docs/` and `outputs/reports/` are easy to recognize at a glance.

The `<id>` column is the unique YouTube video id — keep it for any script or skill that expects the id form.

| Slug | Video title | Channel | Uploaded | YouTube id | URL |
|---|---|---|---|---|---|
| `android-show-io-2026` | The Android Show \| I/O Edition 2026 | Android | 2026-05-12 | `dXCCleAddEA` | https://www.youtube.com/watch?v=dXCCleAddEA |

## File naming

Per video, 14 files land in `outputs/`:

```
outputs/docs/<slug>.minimal.md
outputs/docs/<slug>.rich.md

outputs/reports/<slug>.minimal.{md,pdf,docx}
outputs/reports/<slug>.rich.{md,pdf,docx}
outputs/reports/<slug>.minimal.ko.{md,pdf,docx}
outputs/reports/<slug>.rich.ko.{md,pdf,docx}
```

`<slug>` is a 3–5 word kebab-case abbreviation of the video title.
