# script-10 report

## Result
output/final.mp4 — 94.87 s (voiceover 94.877 s), 2560x1440, **verify PASS**. check.py --plan OK, no `pace:` warnings. Preview freezedetect (d=1.2): only the opening 1.4 s.

## Stages
- probe, transcribe, align, scenes, frames: reused (current; recording 219.4 s, 1920x1080, 30 fps, no clicks log).
- analyze / sync: replaced by a hand plan (`work/hand_plan.py`), as in earlier hand-plan projects: the recording has a baked recorder zoom and no click log, so there are no reliable click anchors. actions.json is intentionally empty (`check.py --actions` reports that; same as earlier hand-plan runs), plan has no zooms/ripples/sync.
- preview + review: 38 joins/review frames read; render, verify: PASS.

## Judgment calls
- Followed the audio order; one group per narration line (or short run) starting on the line's start; moving windows from freezedetect (n=0.002, d=0.8) plus 8 contact sheets.
- 21 groups at 0.77-1.10x (0.83x lowest after the opening); no speed above 1.1x, no holds. The static home screen at the start is a fixed 2.4 s piece.
- Progress/idle spans (e.g. 123-140 s, 173-189 s, 22 s of static editing) skipped as dead time, not played.
- No zooms or ripples (footage already has the recorder's zoom baked in).
- Footage borrowed (the take does not follow the script exactly): lines 5-7 (frame explanation/resize) use nearby frame-placement/resize footage; "Click outside to finish" (L14) uses the end of the drag-drop (89-90.8 s); lines 17-20 (explanatory lines on rotation/mask) reuse the crop/rotate footage cross-faded; L16 "face away from diagonal" uses crop-zoom footage.

## Uncertain
- The recording shows no separate "Elements > Frames search" typing; Frames are picked from Browse categories.
- Rotation (L15) is shown with the crop-panel rotate slider, not a rotated frame.
- Download: footage shows PNG/transparent options, no JPG choice highlighted.

## Check these
- 0:00-0:10 opening still then new design.
- 0:20-0:30 frame choice/resize cross-fades (borrowed footage).
- 0:38-0:46 Uploads drag-drop timing vs. "Wait until the photo fills the frame".
- 0:56-1:20 rotate/explanatory lines (reused crop footage).
- 1:27-1:34 download panel.

## Lessons added
- script-10 run entry in docs/lessons.md.
