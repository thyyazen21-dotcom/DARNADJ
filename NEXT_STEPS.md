# NEXT_STEPS — DARNADJ

_Last updated: 2026-10-13 12:21 UTC_

## Immediate (Phase E — this work unit)
1. Commit the theme + sample content + tests + docs to `main`.
2. Push to `thyyazen21-dotcom/DARNADJ` and **verify the remote SHA** matches local.
3. Produce the final 7-section report.

## Recommended follow-ups (not blockers)
- **Blogger live validation (manual, needs the owner's account):**
  - Upload `IMPORT_THIS_THEME.xml` via Blogger → Theme → Backup/Restore.
  - Open Layout editor and confirm sections are draggable and undistorted.
  - Publish one sample post (`sample_posts_html/DJ-APT-0001.html`) with the labels
    from its header comment; confirm card + detail render and filters work.
  - Confirm `PopularPosts1` shows 5 items (setting `numItemsToShow=5`).
- **Images:** sample posts use Unsplash URLs; local copies exist in
  `06_Sample_Content/images/` for upload to Blogger if desired.
- **Optional Blogger import file for posts:** the attached zip ships
  `Demo Content/Upload Post Content.xml` (a Blogger post-export). It is **not**
  regenerated here because the brief forbids mislabeling a paste file as an import
  file; per-post paste HTML is the supported path. A valid import file could be
  produced later if the owner wants a one-click post import.

## Known limitations / honest notes
- Local tests validate the XML, the shipped JS price functions, and the sample
  content — they do **not** execute inside Blogger itself. Blogger-side behaviour
  (widget rendering, layout editor) is asserted by static/structural checks only.
- No backend: the inquiry form opens WhatsApp; it does not store submissions.
