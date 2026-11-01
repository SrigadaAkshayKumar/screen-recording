# script-08 report

## Result
output/final.mp4 — 100.031 s (voiceover 100.032 s), 2560x1440. verify.py: PASS. check.py --plan: OK, no pace warnings.

## Stages
- probe, transcribe, align (20/20 lines ok), scenes, frames: reused (already current).
- analyze: coarse notes only (work/analyze-notes.md); actions.json not written (check.py --actions rejects an empty list for hand plans; no clicks log, recorder zoom baked in).
- sync: hand plan work/hand_plan.py -> plan.json. Preview rendered, review sheets read, final rendered (218 s), verify PASS.

## Judgment calls
- Followed audio order; each of 20 groups starts exactly on its line start; speeds 0.78-1.33x, no 8x/cut dead time, no zooms/ripples (footage already zoomed by the recorder).
- Static spans from freezedetect and scenes `stills` skipped. Two unavoidable static pieces: opening home screen 2.4 s (src 6.0-7.9) and 1.9 s at src 33.13-34.77 (L5); both under 2.5 s.
- Jumps in source (L9-L12, L13-L18) are cross-faded; footage matched by step: L6 select Contact, L7 toolbar > Link, L8 pages list/Done, L9 Preview, L10 click Contact in preview, L12 Show navigation toggle, L16 link box, L19 Publish, L20 published site.
- Source budget: L13/L14 had only ~8.8 s of moving footage for 12.3 s, so L11 was shortened to start at 117.67 and L13 continues from it.

## Uncertain
- Conceptual lines L1-L5, L11, L13-L15, L17, L18 use related rather than literal footage (no anchor-link/hashtag demo exists in the take).
- Preview freezedetect (d=1.2): 0-2.4 s opening, 22.6-24.5 s, 64.4-65.6 s, 82.3-83.6 s (the last two are cursor-only on the source).

## Check these
- 22.6-24.5 s (static design view), 64-66 s and 82-84 s (little movement).
- 36.7 s: link panel "Done" cross-fade into Preview; 57.7 s join.

## Lessons added
- One entry in docs/lessons.md.
