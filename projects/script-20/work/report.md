# script-20 re-edit 3 report

## Result
`projects/script-20/output/final.mp4` - 95.200 s, 3420x1922, verify **PASS** (duration, streams, resolution, no freeze >3 s, 28 joins without black frames). `check.py --plan`: OK, no pace warnings. Final render 5.2 min.

## Stages
- probe, transcribe, align, scenes: reused. frames: new 1 s sheets (62 tiles) plus 0.3 s sheets of 21.5-27.1, 29.6-33.2, 33.4-41 and 38.8-42.2.
- analyze: redone from scratch (work/analyze-notes.md, work/actions.json, `check.py --actions` OK; coordinates approximate, medium confidence, unused because no zooms/ripples).
- sync: work/hand_plan.py -> work/plan.json (30 segments, no zooms/ripples; recorder zoom is baked in), notes in work/sync-notes.md.
- preview reviewed (frames at line starts/mid-lines), final render, verify PASS. Frames of final.mp4 checked at 13.6, 15, 18.6, 25.6, 27, 29, 31.5, 33, 35, 39.5, 42.7, 45 s (same plan as the preview).

## Judgment calls
- L4-L10 play src 20.5-41.9 in recording order with no jump back; speeds 0.75-1.1x, three holds of 1.4-1.45 s on meaningful frames (type list open, Select pages framed, cursor on "This page").
- Timing to the word: Custom click ~30.3 and checklist ~31.0 ("shows a checklist"); selection changes from 32.7 ("deselect all ... tick only the one"); only page 3 ticked ~39.9 ("page there"); Download click 42.85 ("click Download"); file opens ~44.9 ("save file").
- L8 and L9 show different footage (L8: pages ticked/unticked; L9: only page 2, none ticked + error, then page 3 ticked).
- L13-L19 use only related footage (download panel, page selection, file type list, pages view), cross-faded, never the same piece twice in a row. The early design/intro footage is gone.
- Cut: black frame 3.2-3.9; 12.1-20.5 (static page, pages grid, not narrated). Download wait played at 2x (wait flag).
- L12 is PDF first, then the image (narration order), cross-faded jump back.

## Per-line table (out window | source | what is shown | match)
| L | out | src | shown | match |
|---|---|---|---|---|
| 1 | 0-5.92 | 0-3.15, 3.9-5.5 | Canva home, editor loads | yes |
| 2 | 5.92-8.76 | 5.5-8.4 | page 1 appears, page strip | yes |
| 3 | 8.76-12.42 | 8.4-12.1 | page strip, "Page 2/3" tooltips, page 3 | yes |
| 4 | 12.42-16.82 | 20.5-24.0, 24.0-26.1 | page 3 right-click menu, Download page clicked ~14.9, panel slides in | mostly: no Share in the take; click is ~1.4 s after "Download" |
| 5 | 16.82-25.46 | 26.1-31.6 | type list opens ~18.5 (hold 19.0-20.4), PNG chosen ~24, PNG options | mostly: list opens at "JPG"/"image" not "PNG" |
| 6 | 25.46-27.98 | 31.6 (hold, zoom) 31.6-32.2 | Select pages row framed, cursor reaches it | yes (no separate dropdown in the take) |
| 7 | 27.98-31.3 | 32.2 hold, 32.2-33.1 | cursor on "This page (3)", Custom clicked ~30.3, checklist with page 3 ticked | yes |
| 8 | 31.3-36.8 | 33.1-37.0 | checklist: pages ticked/unticked, Clear all | yes |
| 9 | 36.8-40.46 | 37.0-39.9 | only page 2, none ticked (error), page 3 ticked ~39.9 | yes |
| 10 | 40.46-44.4 | 39.9-41.9, 41.9-45.0 | only page 3 ticked, Download click 42.85, download toast | yes |
| 11 | 44.4-47.18 | 45.0-46.0, 46.0-48.3 | file opens, star.png viewer | yes |
| 12 | 47.18-53.54 | 55.5-58.3, 48.3-50.9 | PDF (one page), then the PNG artwork | yes |
| 13 | 53.54-56.32 | 22.4-24.5 | Download page click, panel opens | related |
| 14 | 56.32-61.82 | 31.4-35.6 | download menu page selection (This page / Custom / checklist) | related |
| 15 | 61.82-65.22 | 39.0-41.6 | final selection, Download enabled | related |
| 16 | 65.22-69.94 | 26.3-30.0 | file type list | related |
| 17 | 69.94-76.8 | 24.0-26.8, 29.9-32.3 | PDF panel, PNG options | related |
| 18 | 76.8-82.9 | 15.1-17.6, 19.0-21.2 | pages view, page menu | related |
| 19 | 82.9-90.08 | 33.0-38.4 | page-selection checklist | related |
| 20 | 90.08-95.2 | 58.5-62.4 | PDF page viewer, closing | yes |

## Uncertain
- No Share click in the take; Download page click lands at out ~14.9 (narration "Download" at 13.5).
- File type list opens at out 18.5, after the "PNG" word (17.0): 1.5x on cursor travel would be needed.
- The Custom click happens before the checklist edits in the take, so "choose Custom" (L9) is shown by the Custom checklist, not the click.
- L13-L19 are reuse (no matching action in the take).

## Check these
- 14-19 (Download page click, list opening), 26-31 (Select pages, Custom click), 39.5-43 (page 3 ticked, Download click), 47-53.5 (PDF then image, jump back), 53.5-90 (reuse).

## Lessons added
One entry in docs/lessons.md.
