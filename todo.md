# Place-dj Targeted Production Upgrade — 8 Themes (LOW-CREDIT)

## Checkpoint Recovery (done)
- [x] Verify git clean at 3322990
- [x] Confirm pre-upgrade backup exists
- [x] Confirm theme size 144284 bytes

## Inspection (done)
- [x] Map CSS classes / sections / widgets
- [x] Confirm file encoding (markup+JS strings = literal UTF-8; regexes = \uXXXX)

## Stage 1 — CSS (done)
- [x] Header height fix (.header-inner min-height:60px + gap 12px 16px)
- [x] Search-bar shrink fix (min-width:0; flex:0 1 auto)
- [x] New CSS block (top-picks, rating, sidebar filter card, discovery)
- [x] Footer 2-column mobile

## Stage 2 — Markup (done)
- [x] U6 hero/footer/add-property marketing copy
- [x] U7 region section (9 cards + intro + place-dj.com links, verbatim)
- [x] U2 remove filter from content-area
- [x] U2 insert HTML4 widget in sidebar (below HTML2 ad)
- [x] U3 insert home-top-picks section before «عقارات مميزة»
- [x] U4 insert rating section before «عقارات مشابهة»

## Stage 3 — JS (done)
- [x] darnaInitTopPicks (editorial, real data only)
- [x] darnaInitRating (stars + localStorage + average + previous list + endpoint hook)
- [x] Wire both into darnaInit
- [x] Replace Google Forms JS note with marketing copy
- [x] Rating summary label + CSS

## Stage 4 — Blogger Layout / meta (done)
- [x] U8 header-widgets + footer-widgets visible in Layout
- [x] U8 home-top-picks showaddelement=yes
- [x] U6 fallback meta description consistency

## Verification (done)
- [x] XML well-formed
- [x] JS syntax (node --check)
- [x] Run tests/place_dj_theme.test.js (52 passed, 0 failed)
- [x] Run tests/validate_structure.py (44 passed, 0 failed)
- [x] Verify footer links on live site (scraped https://www.place-dj.com/)
- [x] Verify all 8 upgrades present in theme (grep evidence)
- [x] Confirm live site NOT published (still shows old content)
- [x] Upgrade 1 header behavior: static markup/CSS/JS verified; live-render = NOT TESTED (needs Blogger import)

## Final — Package, commit (in progress)
- [x] Write test report (PASS/FAIL/NOT TESTED/BLOCKED)
- [x] Update PLACE_DJ_EXECUTION_STATE.md
- [x] Build ZIP package (final XML, backup, state, report, import/rollback) → Place-dj_Final_Package.zip (127,565 bytes, 12 files)
- [x] Commit + push to GitHub → commit d12a4c9 pushed to thyyazen21-dotcom/DARNADJ main
- [x] Deliver report with readiness status → READY TO IMPORT (not published)

## Hotfix — Blogger widget id validation (owner install error)
- [x] Diagnose: "The new widget id HTMLFilter1 is invalid for type: HTML"
- [x] Rename HTMLTopPicks1 → HTML3, HTMLFilter1 → HTML4 (Blogger requires <Type><Number>)
- [x] Add widget-id-format guard to both test suites
- [x] Re-run tests (45 structure + 56 JS = 101 pass, 0 fail)
- [x] Update test report + execution state
- [ ] Rebuild ZIP + re-commit + re-push
