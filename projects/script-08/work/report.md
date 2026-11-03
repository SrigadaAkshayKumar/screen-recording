# script-08 report

## Result
`projects/script-08/output/final.mp4`, 92.026 s (= voiceover), 2560x1440. verify: **PASS** (duration, streams, resolution, frozen spans, 34 join boundaries clean). `check.py --plan`: OK, no `pace:` warnings.

## Stages
- probe, transcribe, align, scenes, frames: reused (work files current; no re-transcription). Alignment: 20 lines, L4 `bad` (0.46) and L3 `fuzzy`, so their times are approximate.
- analyze/sync: no actions.json. The take is covered by the committed hand plan (`work/hand_plan.py`), which already matches this 92.026 s / 20-line voiceover. I reused it and checked it against frames rather than regenerating it.
- preview rendered and reviewed with 40 frames (line start+0.3 s and line middle). Final rendered (~4.3 min) and verified.

## Judgment calls
- Audio order followed; in-scene dead time is fast-forwarded, never cut. Per-line groups run 0.77-1.30x; the only hold is 0.7 s (12.28-12.98), well under 1.5 s.
- Source jumps (e.g. L6 -> src 44 s, L12 -> src 138 s, L14 back to 112 s) are cross-faded joins, because the take does these steps in a different order from the narration.
- No zooms/ripples (the take has a baked recorder zoom).
- Freezedetect on the final (n=0.002, d=1.5): 14.3 s (2.37 s, static field, fixed piece), 21.8 s (1.73), 27.6 s (1.63), 41.4 s (2.0), 82.5 s (1.83). All are under 2.5 s.

## Per-line table
Frames were checked on the preview, which has the same plan and timeline as final.mp4. I did not re-sample the final's frames individually, but verify and freezedetect ran on the final.

| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-6.48 | 2.2-7.4 | Canva home, then Create design / Custom size | yes |
| 2 | 6.48-10.24 | 7.4-10.4 | Custom size panel, units dropdown | yes |
| 3 | 10.24-17.30 | 10.4-15.8 | width/height fields, units, values typed | yes |
| 4 | 17.30-21.68 | 15.8-19.4 | Create design click, blank sheet loads | partly (blank sheet, not yet the 85x110 entry) |
| 5 | 21.68-26.24 | 19.4-23.3 | blank unfolded sheet | yes |
| 6 | 26.24-30.32 | 44.2-49.5 | File menu, Rulers and guides | yes |
| 7 | 30.32-34.66 | 71.8-83.2 | Add guides panel, rows=2, Add guides | yes |
| 8 | 34.66-36.68 | 86.0-88.4 | horizontal guide across the card | yes |
| 9 | 36.68-39.46 | 88.6-91.0 | page one, full card | yes |
| 10 | 39.46-43.34 | 91.0-100.2 | lower half selected | yes |
| 11 | 43.34-50.22 | 103.9-112.2 | upper half and back-cover text | yes |
| 12 | 50.22-52.14 | 137.8-139.8 | Add page, page 2 | yes |
| 13 | 52.14-58.50 | 139.8-154.0 | page 2 panels | yes |
| 14 | 58.50-62.56 | 112.2-116.4 | whole design (mockup-check line) | partly (no mockup footage in the take) |
| 15 | 62.56-69.80 | 116.4-161.1 | design, then Download panel | partly |
| 16 | 69.80-77.54 | 161.1-168.0 | Download panel, file type list | partly (illustrates settings) |
| 17 | 77.54-80.30 | 67.1-70.0 | File menu | partly (Clear guides not visible) |
| 18 | 80.30-84.30 | 86.4-102.4 | Add guides panel, guide on page | yes |
| 19 | 84.30-88.88 | 210.2-224.0 | PDF, Print preset, advanced settings | yes |
| 20 | 88.88-92.03 | 184.0-187.2 | PDF downloaded toast | yes |

## Uncertain
- The take has no footage of a paper mockup (L14-15) or drawing and removing a fold line (L17); nearest relevant panels are used.
- L3/L4 timings come from low-confidence alignment.

## Check these
- 14.3-16.7 s: static typed-field piece (2.4 s), nearly frozen.
- 21.8 s and 27.6 s: calm moments after page load (1.6-1.7 s).
- 77.5-80.3 s: File menu stands in for removing the line.

## Lessons added
None; no render had to be redone.
