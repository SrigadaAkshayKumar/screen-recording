# script-05 — report

## Result
`projects/script-05/output/final.mp4`: 91.600 s (voiceover 91.613 s), 2560x1440, **verify PASS**.
`check.py --plan` OK with no pace warnings. Preview and final freezedetect (n=0.003): longest still stretch 2.4 s
(out 7.7-10.1, Canva "Create a design" dialog; the 2.33 s static opening at 0-2.3 s is the same kind).

## Stages
- probe, transcribe, align (19/19 lines ok), scenes, frames: **reused** (270.1 s, 1920x1080, 30 fps, baked recorder zoom, no clicks.json).
- analyze / sync: **not run as skills**. This take has recorder zoom baked in and the recording is 3x longer than the voiceover, so I built
  `work/hand_plan.py` (same recipe as earlier projects) from 1 s / 0.5 s contact sheets; it writes `work/plan.json` (no zooms, no ripples,
  no sync entries). `work/actions.json` and `work/sync.json` were not written. Hand edits to plan.json would be overwritten by re-running the script.
- preview render x4 (each ~28 s), final render 3 min 16 s, verify PASS (0 zoom peaks, 34 join boundaries clean).

## Judgment calls
- Followed the audio order. Source jumps are cross-faded (xfade); several jumps skip static footage between near-identical frames.
- Dead time: the recording has long static stretches (src 37.5-44.5, 62-66, 135-144, 155-178, 202-234, 238-252) where only the cursor moves.
  They were fast-forwarded at 2x for at most ~2.3 s (L5, L13) or skipped with a cross-fade where narration left no room (the rest). Nothing is held.
- L1 + L2 are one group: the take opens on a 8 s static home page, so the opening is 2.0 s static (1x) then the cursor/zoom move to Create at 0.76x.
- L5/L6: no footage of "check the crop"/"detailed original" beyond the placed/zoomed image; File > margins menu is shown over L6.
- L8: the Download click is shown at ~34.7 s; the static 62-66 s dialog was skipped.
- L9: the take has a stray "close all tabs" dialog (src 81.7-85) — skipped.
- L12 uses the tile-grid preview from src 189.6-192.4 (the earlier Poster footage 125-132 is static); L16 reuses src 186-189 and 192.8-196.
- L18: Multiple demo (src 234.5-238), then jumps to the switch back to Poster (252.3-255). L19 skips the static poster view (255-257.6) and the 2x piece is the click lead-in.
- All speeds 0.75-2.0x; actions 0.76-1.43x.

## Uncertain
- Out 7.7-10.1 is a 2.4 s near-static shot (dialog open, cursor barely moves); below the 2.5 s limit but at the edge.
- Click times were never logged; word-to-UI timing was judged by eye from frames (±0.5 s).

## Check these
- 10.8-11.5: custom-size click lands ~1 s before "custom size".
- 31-33: Download panel still shows PNG at "PDF" (PDF chosen ~32.5).
- 51.5-54: L12 starts on the Poster option already selected, then the tile grid appears.
- 70-72: cross-fade jump in L16.

## Per-line table (frames from final.mp4 at line start+0.4 s and middle)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-7.14 | 7.3-13.7 | Canva home, cursor/zoom to Create, dialog opens | yes |
| 2 | 7.14-10.82 | 13.7-16.4 | Create a design dialog, cursor to Custom size | yes |
| 3 | 10.82-16.4 | 16.4-18.3, 18.3-22.3 (2x), 23.5-24.7 | Custom size 60x40, Create new design | yes (click ~1 s early) |
| 4 | 16.4-19.0 | 30.4-33.6 | Uploads panel, image dragged onto page | yes |
| 5 | 19.0-23.36 | 33.6-39.8 | image resized to the page | partly |
| 6 | 23.36-28.58 | 44.6-51.8 | zoom on placed image, File menu opens | partly |
| 7 | 28.58-33.7 | 53.4-60.8 | Share, Download panel, PDF, Print preset | yes |
| 8 | 33.7-37.8 | 66.0-70.1 | Download click, downloading toast | yes |
| 9 | 37.8-41.84 | 77.6-81.0, 85.2-86.2 | Downloads folder, Open with menu, Acrobat shows poster | yes |
| 10 | 41.84-48.34 | 94.2-95.4, 101.8-103.6, 104.4-109.4 | Print dialog, printer list, Page Setup paper size list | yes |
| 11 | 48.34-51.54 | 122.0-125.2 | Poster clicked in Page Sizing and Handling | yes |
| 12 | 51.54-54.28 | 189.6-192.4 | Poster option, tile grid in preview | yes |
| 13 | 54.28-59.82 | 131.6-134.6, 134.6-139.2 (2x) | Tile Scale 100% field zoomed | yes |
| 14 | 59.82-65.04 | 145.3-148.0, 150.6-154.2 | Overlap field, Cut marks ticked | yes |
| 15 | 65.04-67.76 | 179.4-182.1 | zoomed preview, page 1 of 1 | partly |
| 16 | 67.76-72.76 | 186.0-188.9, 192.8-196.0 | settings and preview changing | partly |
| 17 | 72.76-78.16 | 45.0-47.85 (0.75x), 198.6-200.2 | Canva artwork, then Acrobat tile preview | yes |
| 18 | 78.16-85.0 | 234.5-238.0, 252.3-255.0 | Multiple clicked, preview of several pages per sheet | yes |
| 19 | 85.0-91.61 | 257.6-260.2 (2x), 260.2-266.5 | Print clicked, printing progress, save dialog | yes |

## Lessons added
See docs/lessons.md (script-05 2026-11-03 entry).
