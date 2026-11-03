# script-01 report

## Result
output/final.mp4, 92.087 s, 2560x1440. verify.py PASS. check.py --plan: OK, no `pace:` warning (only "action not tied to a word" warnings, because the hand plan has no sync anchors). freezedetect (n=0.003, d=1.2) on final: longest 2.2 s (static opening at 2x), one 1.2 s spot.

## Stages
- probe, transcribe, align (22 lines, all ok), scenes, frames: reused.
- analyze: coarse actions.json (14 low-confidence landmarks) + analyze-notes.md. check.py --actions OK.
- sync: hand plan (work/hand_plan.py), 36 segments, plan.json OK.
- preview ran twice, final rendered three times (fix rounds: a 1.4 s freeze at the end of the frame-resize piece; blurred zoom-transition frames at the start of L4 and L8; L21 stopped before the MP4 option appeared). Verify PASS on the last render.

## Judgment calls
- Audio order followed; L4 (page background) borrows footage recorded earlier than L3's.
- Speeds 0.89-1.22x everywhere except the 2.2 s static opening (2x). No holds, no cuts of in-scene time; dead stretches were skipped by choosing moving pieces, joined with cross-fades.
- Intro (L1) = home screen at 2x, then the finished filmstrip animation (src 370-373). L18 and L22 reuse the preview-play footage (347-351), L19 the animation preview inside the Animate panel.
- No zooms or ripples (the recording already has recorder zoom and no click log).

## Per-line table (frames taken from final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-5.36 | 3.5-7.9 (2x), 370-373 | Canva home, then the finished filmstrip scene | partly (intro borrowed) |
| 2 | 5.36-7.7 | 9.3-10.6, 11.7-13.0 | Video icon on home, then the design dialog | yes |
| 3 | 7.7-14.5 | 35.2-36.9, 44.0-45.6, 49.2-53.4 | Elements panel, black rectangle added, stretched to a wide strip | yes (blurry mid join) |
| 4 | 14.5-18.1 | 25.7-29.3 | Background colours panel, lavender picked, page turns lavender | yes (page colour differs from L3 footage: recorded earlier) |
| 5 | 18.1-23.38 | 70.8-72.0, 75.0-77.4, 82.0-83.5 | Elements, "frames" search, Frames tab, frame on the page | yes |
| 6 | 23.38-30.4 | 84.2-86.6, 91.2-95.8 | frame resized, duplicated into several windows | yes (take has four frames) |
| 7 | 30.4-33.64 | 167.8-171.2 | uploaded photo dragged into the first frame | yes |
| 8 | 33.64-38.42 | 198.0-199.6, 208.5-211.5 | photo in frame selected, uploads panel/photo adjust | partly (no clear double-click crop) |
| 9 | 38.42-43.34 | 235.3-240.5 | Graphics results, white square chosen and placed | yes |
| 10 | 43.34-46.92 | 255.0-256.8, 279.7-281.6 | duplicate of the square, row copied top and bottom | partly |
| 11 | 46.92-49.02 | 283.5-285.6 | finished strip with squares inside the black bar | yes |
| 12 | 49.02-54.1 | 287.8-289.0, 290.0-293.7 | everything selected, Group button | yes |
| 13 | 54.1-56.54 | 293.5-296.0 | grouped strip, page background outside it | yes |
| 14 | 56.54-58.7 | 296.6-298.8 | group moved toward the right edge | yes |
| 15 | 58.7-63.76 | 306.8-309.8, 311.0-313.2 | Animate button, Animate panel, Create an animation | yes |
| 16 | 63.76-68.02 | 316.0-321.2 | strip dragged left, path drawn | yes |
| 17 | 68.02-71.42 | 323.0-324.8, 331.3-333.3 | movement settings panel (speed, style) | yes |
| 18 | 71.42-75.04 | 347.4-351.0 | preview play, whole strip moving as one | yes |
| 19 | 75.04-79.76 | 333.8-338.0 | strip sliding in the animation settings view | partly |
| 20 | 79.76-85.44 | 360.4-362.8, 364.8-368.0 | scene length dragged on the timeline | yes |
| 21 | 85.44-89.52 | 375.8-380.6 | Share panel, Download panel with MP4 Video | yes |
| 22 | 89.52-92.087 | 349.0-351.6 | preview playing the finished movement (not the downloaded file itself) | partly |

## Uncertain
- actions.json is coarse; no click-exact sync. Lines 1, 8, 10, 19, 22 use borrowed or approximate footage.
- Join at ~10.7 s (L3) is a cross-fade over a blurry recorder-zoom transition.

## Check these
- 0-2.2 s static opening; 10.7 s join; 35-38 s (L8 uploads panel); 89.5-92 s (plays the in-editor preview, not a downloaded file).

## Lessons added
- script-01 entry in docs/lessons.md.
