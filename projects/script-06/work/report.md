# script-06 report

## Result
- `projects/script-06/output/final.mp4`, 96.966 s (voiceover 96.967 s), 2560x1440 delivered, **verify PASS** (no freeze over 3 s, 25 joins free of black frames).
- `check.py --plan`: OK, no `pace:` warnings. Preview freezedetect (n=0.003, d=1.2): longest still 2.4 s (opening), then 2.0 s (out 68.7, line 15 end: 1.1 s planned hold + still tail), others 1.4-1.6 s.

## Stages
- probe, transcribe, align (all 22 lines ok, 100 % match), scenes, frames: reused (already current).
- analyze/sync: done by hand plan (`work/hand_plan.py`, the recipe from earlier runs) rather than actions.json/sync.json, because no clicks log exists and sync is by line. `work/actions.json` and `sync.json` were not written.
- Preview render, review sheet (23 join frames), final render (~4.4 min), verify: ran.

## Judgment calls
- Audio order followed; one group per narration line, L1-L3 merged (the recording is silent and the first 6.3 s are a static page).
- Speeds 0.75-1.36x for actions; only dead time sped up: opening still (src 1.5-6.3) at 2x = 2.4 s.
- No zooms or ripples (no click log; matches earlier hand plans).
- L15 plays at 0.75x and then holds the last frame 1.1 s (source budget).
- Footage is borrowed where the take lacks the exact step: L1-3 intro, L13 "smaller near corner" uses the shrink-while-rotated footage (125.5-129.3), L19 "useful distinction" uses a brief JPG/PNG settings piece (191.3-192.7), L20 element transparency uses the transparency slider at 217.9-221.8.
- Recording order differs from the script (position at 96 s comes after transparency at 80 s); I followed the narration, so L9 precedes L10 footage-wise and cuts have 6 cross-fades.

## Uncertain
- Whether L8 "transparent background" footage (logo placed, 71.6-78.5) is what the client expects for the line.
- L12/L13 take the rotation and shrink steps from the same continuous sequence.

## Check these
- 0-2.4 s: static opening at 2x.
- 8.9-12.5 s and 12.5-14 s: end of the intro (design page, text panel).
- 63.9-69.9: line 15 hold at 68.8.
- 83-85: cross-fades between PNG settings and transparency footage.

## Lessons added
- One entry for script-06 (see docs/lessons.md).
