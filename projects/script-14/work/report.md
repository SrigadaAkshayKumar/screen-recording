# script-14 report

## Result
output/final.mp4, 91.667 s, 3420x1922, verify PASS. check.py --plan: no `pace:` warnings. Preview freezedetect (d=1.2): only the 1.6 s closing hold-like still at 89.7-91.3 (closing allowed up to 3 s).

## Stages
- probe, transcribe, align, scenes, frames: reused (work files current; 150.1 s take, 91.672 s voiceover, 18 lines).
- analyze/sync: done as a hand plan (work/hand_plan.py, per-line groups; no zooms or ripples, same recipe as earlier script-14/16/17 runs) from freezedetect (n=0.002, d=0.8) gaps and 7 contact sheets. No actions.json/sync.json written.
- preview render + review sheets: done, no fixes needed. Final render ~5 min, verify PASS.

## Judgment calls (per line: source range, does it show the step)
Audio order followed; each group starts at its line's start, speed 0.85-1.48x, joins cross-faded when not contiguous.
1. 4.0-12.3: finished design with embedded video. Yes.
2. 12.9-15.9: YouTube share dialog, copy link. Yes.
3. 36.1-42.8: Canva editor, Apps, search. Yes.
4. 46.3-52.8 (1.48x): open YouTube Embed app, paste link, results. Yes (fast-forwarded, dead time).
5. 56.0-59.5 + 67.6-71.2: video placed on page, then corner-handle resize. Yes.
6. 71.2-75.7: resizing/proportions. Mostly (same drag continued).
7. 60.3-63.3: presentation/playback of the embed. Yes.
8. 16.0-19.6: source video on YouTube. Conceptual match.
9. 19.6-24.9 (0.85x): source tab switching/leaving YouTube. Conceptual, weak.
10. 77.0-79.4: Apps panel, transition. Conceptual.
11. 52.8-55.9: embed search results from YouTube. Conceptual.
12. 63.3-67.5: embed player in editor. Conceptual.
13. 129.0-136.0: Share > Download > MP4 file type list. Yes.
14. 81.2-84.4, 86.2-88.2, 91.8-94.0 (1.10x): Uploads, Upload files dialog, uploaded clip placed. Yes; processing wait skipped.
15. 112.4-115.0 (trim) then 106.0-108.9 (volume): out of recording order, narration order kept. Yes.
16. 95.0-99.4: playback of uploaded clip. Conceptual.
17. 72.4-76.6: embed in editor/playback. Conceptual.
18. 141.9-149.05: export review tips / final design. Conceptual closing.
Footage shared between lines only where conceptual (8-12, 16-18); the take has no footage of a restricted/private video or a network issue.

## Uncertain
- Lines 8-12, 16-18 are explanatory with borrowed footage; no real footage exists.
- Line 4 ends before the Add to Design click is clearly shown (that click sits at ~55-56 s src, just before line 5 starts at 56.0).

## Check these
- 8.3 and 11.3 s (opening to share dialog), 22.4 s (Add to Design to placement), 40.7-46.9 s (L9 leaves YouTube), 63.8-70.5 s (upload steps), 70.5-76 s (trim then volume), 86-91 s (closing).

## Lessons added
- One line in docs/lessons.md (run log).
