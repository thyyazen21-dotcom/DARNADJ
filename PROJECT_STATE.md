# PROJECT_STATE — DARNADJ

_Last updated: 2026-10-13 12:21 UTC_

## Repository (source of truth)
- Repo: `thyyazen21-dotcom/DARNADJ`
- Branch: `main`
- Baseline SHA (start of this work): `9a598f178d8d28406a24abf8ccd980da52ba7f6d`
- Push method: token URL `https://x-access-token:$GITHUB_TOKEN@github.com/thyyazen21-dotcom/DARNADJ.git` (token never printed).

## Production artifacts
- **Production Blogger theme (native XML, not React/Vite):**
  `project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/theme/IMPORT_THIS_THEME.xml`
- **Sample content:** `DarnaDJ_Updated_Package/06_Sample_Content/` (AR pack, 12 posts, images, per-post copy-paste HTML)
- Content templates: `DarnaDJ_Updated_Package/05_Content_Templates/`
- Static pages: `project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/content_templates/static_pages/`
- Tests: `tests/price_logic.test.js`, `tests/sample_posts.test.js`
- Backup of original theme: `project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/theme/_archive/IMPORT_THIS_THEME.original-repo-9a598f1.xml`

## Theme shape (current)
- `b:templateVersion='2.0.0'`
- 6 `<b:section>`: `header-widgets`, `home-before-posts`, `main-blog`, `home-after-posts`, `sidebar-widgets`, `footer-widgets`
- 5 `<b:widget>`: `Blog1` (Blog), `HTML1` (HTML), `Label1` (Label), `HTML2` (HTML), `PopularPosts1` (PopularPosts)
- 5 `<b:includable id='main'>` (one per widget)
- `PopularPosts1` uses `numItemsToShow` (Blog widget keeps `numPostsToShow`)
- Price logic markers preserved for tests: `var DARNA_SERVICE_FEE_RATE` … `// Expose for testing`
- XML well-formed (verified with `xml.dom.minidom`)

## Baseline problems (confirmed) → status
1. Layout editor inherited visitor CSS → **FIXED** (`body#layout` isolation).
2. Cards wrapped so the whole section was one grid cell → **FIXED** (grid on the cards, not the section).
3. Forbidden visitor messages (admin price notice + fee notice) → **REMOVED** (0 in theme, 0 in sample bodies).
4. Price not USD-style / no separator / no unit → **FIXED** (`$1,100 / شهر`).
5. No per-card gallery → **FIXED** (per-card carousel, isolated).
6. Detail page single column, no specs/amenities/location/terms/form/similar → **FIXED**.
7. Search/filters limited → **FIXED** (full client-side filter engine).
8. No contact/inquiry form → **FIXED** (validated + WhatsApp deep link).

## Current phase
- Phases A–D **complete**. Phase E (commit/push + final report) in progress.

## Next phase
- See `NEXT_STEPS.md`.
