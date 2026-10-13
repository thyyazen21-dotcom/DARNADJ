# RECOVERY_CHECKPOINT — DARNADJ

_Checkpoint: 2026-10-13 12:21 UTC_

This file lets a future session resume **without chat memory**. Read this first,
then `PROJECT_STATE.md`, then `NEXT_STEPS.md`.

## Where the work lives
- Repo clone: `/workspace/darna_repo` (branch `main`).
- Production theme: `project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/theme/IMPORT_THIS_THEME.xml`.
- Sample content: `DarnaDJ_Updated_Package/06_Sample_Content/`.
- Helper scripts (workspace, not committed): `/workspace/fix_theme.py`,
  `/workspace/enrich_samples.py`, `/workspace/clean_sample_bodies.py`,
  `/workspace/build_preview.py`.

## State at this checkpoint
- Phases A–D complete; Phase E (commit/push + report) in progress.
- Theme: 86,121 bytes, XML well-formed, 6 sections / 5 widgets, 0 forbidden strings.
- Tests: price 15/15, sample 111/111.
- Sample bodies: fee messages removed; clean USD price line.

## How to resume
1. `cd /workspace/darna_repo && git fetch && git status` — confirm branch/SHA.
2. Re-run gates: `node tests/price_logic.test.js && node tests/sample_posts.test.js`.
3. Re-check theme: `python3 -c "import xml.dom.minidom as m; m.parse('project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/theme/IMPORT_THIS_THEME.xml')"`.
4. If sample content needs regeneration: run `/workspace/clean_sample_bodies.py`
   then `/workspace/enrich_samples.py` (in that order), then `build_preview.py`.
5. Continue from `NEXT_STEPS.md`.

## Safety rules (unchanged)
- Never force-push. Never destructive changes. Original theme backed up in
  `theme/_archive/`. If a push fails, keep local changes and document it.
- GitHub is the final source of truth; verify the remote SHA after pushing.
