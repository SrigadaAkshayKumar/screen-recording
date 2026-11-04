# script-19 — report

## Result
`projects/script-19/output/final.mp4` — 98.352 s, 2560x1440 (take is 1920x1080, rendered up), 30 fps. **verify PASS** (duration, streams, resolution, frozen spans, black frames at joins). Full-res freezedetect (n=0.003, d=1.7) on the final: only the static homepage opening (2.13 s) and a 1.8 s span at 9.7 s (loading page at the end of L2); nothing over 2.5 s. `check.py --plan` OK with no `pace:` warning; 20 groups at 0.81-1.36x (L18 and the static editor piece at 1.0x).

## Stages
- probe, transcribe, align (all 20 lines ok/fuzzy, L9 0.76 fuzzy), scenes, frames: **reused** (not re-run).
- analyze / sync skills: **not run as skills.** The take has a baked recorder zoom and no click log, so there are no zooms or ripples. As in earlier runs I wrote `work/hand_plan.py` (pieces per line, cross-faded jumps) from 1 s / 2 s contact sheets, freezedetect windows (n=0.003, d=0.8) and native crops. No actions.json / sync.json exist; the plan has an empty `sync` list.
- Gate E (`check.py --plan`): pass. Preview (540p) rendered and reviewed; the final was rendered twice (first one led to the three fixes below).
- final render ~6 min; verify PASS.

## Judgment calls
- Followed the audio order. The take does logo -> invoice number/date -> bill-to -> business name -> table -> totals -> payment; the narration says business name/logo first, then client, then number/date. Pieces jump (xfade) accordingly.
- Dead time: static spans of the take were skipped or played at <=1.5x; no hold frames used. Moving-window footage is used at 0.8-1.4x.
- Fixes after the first final: L2 ended on a blank loading page (now ends on the loaded editor, 2 s at 1x); L18 had the Share click 2.3 s after the word "Share" (piece now starts at 306.3 s at 1x, Share click lands at ~83.4 s, Download panel at ~84.5 s, Digital preset visible by ~87 s); L20 started on the PDF instead of the editor (reordered).
- The take does not contain a duplicate/master-template step, nor typed currency "EUR" etc. as separate gestures; those lines borrow nearby footage (see table).

## Uncertain
- Word-level sync of clicks is only checked for Share/Download (L18). Other lines are matched at line level by content, not by click-on-word.
- Contents of src 270-277, 292-296 (L12/L13) were identified from 2-4 s sheets only.

## Check these
- 8.5-10 s: loading/blank page transition at the end of L2 (~1.8 s).
- 11.5-17.2 (L3): the logo replace, then a jump to the business-name edit (src 116-119).
- 50.5-55 (L12 currency) and 60-71 (L14): borrowed table/totals footage.
- 91.5-98.3 (L20): no duplicate footage exists; shows the editor and the Download panel.

## Per-line table (verified on frames of final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 intro | 0-4.8 | 8.3-12.8 | Canva home, cursor to search box / Templates tab | yes |
| 2 search + template | 4.8-11.5 | 12.8-14.6, 15.4-17.5, 21-23 | "invoice" typed in search, template grid, template clicked, editor opens | yes (blank load frames ~8.6-9.7) |
| 3 name, logo, contact | 11.5-17.2 | 31.5-34, 52-54.5, 116-119 | old logo selected/deleted, new logo placed and resized, business name selected | partly (name edit is last) |
| 4 client section | 17.2-20.5 | 91.3-93.8, 83.9-85.4 | Bill-to block selected/edited | yes |
| 5 number + dates | 20.5-25.1 | 58-60, 61.3-62.7, 66.7-68.5 | invoice number line selected and typed | yes |
| 6 date format | 25.1-27.5 | 78.3-80.7 | zoomed: date line shows new date, cursor to Bill-to | yes |
| 7 line items | 27.5-30.8 | 141.2-142.3, 143.7-146.4 | table selected, first row | yes |
| 8 description/qty/price/total | 30.8-36.3 | 146.4-149.2 (1.5x), 149.2-150.9, 152.2-153.5, 158.9-160.1 | row cells edited | yes |
| 9 3 sessions x 50 = 150 | 36.3-43.4 | 184.5-187.2, 192.3-193.3, 204-205.2, 170.1-171.4 | unit price / total columns being edited | partly (values too small to read) |
| 10 subtotal | 43.4-46.7 | 221.2-222.9, 229.3-230.7 | zoom into totals box, cursor on total | yes |
| 11 adjustments, amount due | 46.7-50.6 | 234.6-235.9, 239.8-242.2, 246.2-247.5 | totals area edited | yes |
| 12 currency | 50.6-54.9 | 292.2-295.2, 271-272.2 | zoomed totals/amount area | partly |
| 13 payment | 54.9-60.5 | 252.5-254.5, 256.8-257.9, 259.5-261, 274.6-276.4 | payment/notes box at bottom of page edited | partly |
| 14 layout, no recalculation | 60.5-71.6 | 172.3-175, 177.5-179.3, 180.9-182.3, 208.7-210.2, 211.8-212.9, 194.4-195.8 | quantity/price cells in the table being changed | partly |
| 15 verify arithmetic | 71.6-73.8 | 334.1-335.7, 339.1-340.1 | PDF with Sub-Total/Tax/Total | yes |
| 16 remove unused | 73.8-77.6 | 283.1-284.3, 288.8-292.2 | notes block selected at page bottom | partly |
| 17 business/tax details | 77.6-82.2 | 295.2-300.7 | bottom-right block selected and resized | partly |
| 18 Share, Download, PDF, Digital | 82.2-88.4 | 306.3-310.7 (1x), 314.8-316.5 | Share click at ~83.4, Share panel/Download at 84.5, PDF panel with Digital preset 85.6-87.3 | yes |
| 19 open PDF | 88.4-91.5 | 329.7-333.3 | "File downloaded" toast, PDF opens (brief black load at ~90.5) | yes |
| 20 master template | 91.5-98.4 | 352.8-354.3, 359.1-360.4, 364-367.3 | back in the editor, Download panel again | no (no duplicate footage in the take) |

## Lessons added
See docs/lessons.md (2026-11-04 script-19).
