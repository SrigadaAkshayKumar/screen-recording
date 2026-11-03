# script-09 report

## Result
- `projects/script-09/output/final.mp4`, 101.6 s, 2560x1440, **verify PASS** (duration, streams, resolution, frozen spans, black frames at 36 joins).
- Strict freezedetect (n=0.003, d=1.5) on final: longest still 2.53 s (static opening), then 2.43, 2.4, 2.27, 2.2, 2.0, 1.87, 1.53 s. None over 2.5 s except the opening (+0.03 s).

## Stages
- probe, transcribe, align (21 lines, all ok), scenes, frames: reused (already current).
- analyze / sync: done as a hand plan (`work/hand_plan.py`), as in earlier projects. No click log, so there are no zooms or ripples and no actions.json/sync.json; the plan is built from freezedetect moving windows and 9 contact sheets.
- check.py --plan: first run had 1 pace warning (0.37 s piece, folder hover), fixed by dropping that piece. Second run clean.
- preview + review sheet (23 frames) read; final render and verify: PASS.

## Judgment calls
- One group per narration line, starting on the line's start; follows the audio order. Lines 1-2 and 6-7 are merged into one group each.
- Source is mostly static (cursor only), so static spans are fixed pieces at <=2x (opening 0.16-5.13 at 1.99x; 14.3-17.7 at 1.7x; 62.6-66.17 at 1.5x; 80-84.23 at 1.76x; 206.27-210.97 at 1.96x; 196-200.4 at 1.83x) and every other piece is 0.76-1.5x. Waits (upload/processing toasts) were fast-forwarded or skipped, not held; no holds, no zooms.
- Upload progress (src 29.4-48.7) and the long processing wait (src 73-80) are mostly skipped; narration has no step for them.
- L19-L20 (library photos / reduce to 50 images) have no matching footage: borrowed the home folder view, download dialog and an idle folder view.
- L21 shows the download menu on a cutout (src 225-233); the transparent-PNG result itself is not shown.

## Uncertain
- No analyze-notes/sync-notes (hand plan). Cursor-click times were not verified to words since there is no click log.

## Check these
- 0:00-0:05 static home opening (2.5 s at 2x).
- 0:41-0:46 edited vs original folder listing: mostly static with a toast.
- 1:29-1:35 footage for the "50 images / plan" lines is borrowed.
- 1:36-1:41 download menu ending.

## Lessons added
- script-09 entry in docs/lessons.md.
