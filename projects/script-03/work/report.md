# script-03 report — Canva business-card bleed

## Result
`projects/script-03/output/final.mp4` — 87.333 s (voiceover 87.34 s), 2560x1440, **verify PASS** (no freeze over 3 s, 34 joins clean, audio+video streams ok).
preview freezedetect (d=1.2): opening 2.33 s, then 1.9, 1.8, 2.1 and a 2.4 s closing static PDF view (cursor-only; all < 2.5 s). `check.py --plan`: OK, no `pace:` warnings (19 groups at 0.78-1.32x).

## Stages
- probe, transcribe, align (19/19 lines ok, 2 lines 95 % match), scenes, frames: **reused** (already current).
- analyze + sync: done by hand from 9 sheets and ~120 single frames -> `work/hand_plan.py` -> `work/plan.json` (no zooms/ripples: no click log, recorder zoom is baked in). analyze-notes.md / sync-notes.md written; no actions.json (same as earlier hand-plan projects).
- preview rendered and reviewed (freezedetect + joins), final rendered (266 s), verify PASS.

## Judgment calls
- Audio order followed. The recording ticks Show margins first and Show print bleed last; narration is bleed first, so L4 = File menu -> Rulers submenu -> bleed hover -> bleed click (src 84.3-85.5), L5 = margins hover (src 58.8-61), cross-faded jump.
- L1 opening: home screen is static for 6 s; played as one 2.3 s piece at 2x, then the home-screen scroll/hover (6.33-9.1) at 0.8x.
- Dead time (hover over the menu, static PDF) fast-forwarded at <= 1.3x; nothing cut inside a scene except long idle spans (src 8.8-17.9, 96-101, 137-144, 162-176, 231-240) that are skipped as jumps.
- L16 (concept line) reuses bleed-guide frames (src 86.4-88.9) then the PDF with crop marks (228.6-232.1, 240.6-242.7). L19 reordered so the line does not end on a 3 s static PDF view.
- L11 and L5 have no exact footage (see table).

## Per-line verification (frames from final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-5.8 | 0.5-5.1 (2x), 6.33-9.1 | Canva home, scroll/hover over cards | yes |
| 2 | 5.8-11.64 | 17.9-23.6 | click on the business-card design, editor opens | yes |
| 3 | 11.64-14.56 | 28.8-32.4 | Resize button -> size panel opens (finished size) | yes |
| 4 | 14.56-18.94 | 45.4-47.8, 69.4-71.6, 84.3-85.5 | File menu, Rulers and guides, cursor to Show print bleed, ticked | yes |
| 5 | 18.94-21.02 | 58.8-61.1 | cursor on Show margins (already ticked, bleed unticked in this take) | partly |
| 6 | 21.02-23.3 | 85.5-87.7 | menu closes, bleed guides visible around card | yes |
| 7 | 23.3-27.38 | 87.7-89.5, 91.1-93.0 | decorative bottom shape and top background selected | yes |
| 8 | 27.38-33.94 | 93.0-96.0, 101.6-104.6 | top blue background selected, colour panel | yes |
| 9 | 33.94-39.8 | 112.1-118.9 | phone, email, address, title and name boxes selected | yes |
| 10 | 39.8-43.52 | 119.7-122.6 | name box then whole card with margin guides | yes |
| 11 | 43.52-48.36 | 104.6-108.6 | blue rectangle selected, colour panel (no enlarging drag in take) | partly |
| 12 | 48.36-53.4 | 144.3-150.8 | whole design selected, then text-box handle drag | partly |
| 13 | 53.4-56.22 | 181.0-184.4 | Share button, panel, Download panel | yes |
| 14 | 56.22-62.04 | 186.0-195.3 | file-type list -> PDF, Print preset, Advanced settings | yes (L14 opens on the PNG panel for ~0.5 s) |
| 15 | 62.04-66.34 | 198.4-200.9, 206.8-209.2 | Crop marks and bleed toggled on, Download click | yes |
| 16 | 66.34-74.08 | 86.4-88.9, 228.6-232.1, 240.6-242.7 | design with bleed guides, then PDF with crop marks | yes |
| 17 | 74.08-76.44 | 216.2-218.6 | "File Downloaded" toast | partly |
| 18 | 76.44-80.08 | 224.0-228.6 | Open file click, PDF opens | yes |
| 19 | 80.08-87.34 | 247.2-249.3, 242.7-247.1 | PDF text, cursor over website/address, zoomed out view | yes |

## Uncertain
- L5: Show margins is already ticked in the take, so no tick lands on "Turn on".
- L11: no rectangle enlarge in the take; selected rectangle shown instead.
- L12: text-box resize is the only drag in the take.

## Check these
- 14.5-21 (File menu / bleed / margins order jumps back); 56.2-57 (PNG panel before PDF is chosen); 62-66 (crop marks toggle then Download); 82-87 (closing PDF view, near-static 2.4 s).

## Lessons added
- One entry in docs/lessons.md (script-03 re-edit).
