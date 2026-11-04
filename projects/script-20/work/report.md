# script-20 report

## Result
`projects/script-20/output/final.mp4` - 96.417 s (= voiceover), 2560x1440, verify **PASS** (duration, streams, resolution, no freeze > 3 s, 31 joins clean). `check.py --plan`: OK, no `pace:` warning (only "action not tied to a word" notes, expected for a hand plan). Source bitrate not measured; recording is 1920x1080 with baked-in recorder zoom (soft source possible). Final render 2.7 min.

## Stages
- probe, transcribe, align (19 lines, all ok), scenes, frames: reused (not re-run).
- analyze: new 0.5-1 s sheets over the whole take; work/actions.json (14 actions, coordinates are placeholders, no click log and no zooms used), `check.py --actions` OK.
- sync: work/hand_plan.py -> plan.json (31 pieces, 0.76-1.5x, no holds, cross-fade on every jump). Preview reviewed at every line start and middle; L8 was shifted once so "Drop" is selected on the word.
- render final, verify PASS. Frames of final.mp4 checked at 1.0, 4.5, 8.5, 22, 23, 24.3, 26, 29, 34.2, 35.5, 36.3, 38.5 s; the rest checked on the preview (same plan, same pieces).

## Judgment calls
- Narration order wins; the take does things in another order (see table). No zooms/ripples: recorder zoom is baked in, no clicks logged.
- Lines with no matching footage (keyboard shortcut, Position/Layers panel, download of a test image) use the closest step and are marked partly.
- L1: 2.2 s of the home page, then the finished heading, because the home page is static for 8 s (stills 1.2-9.2).
- L8 plays 1.0x then 1.46x (slider footage is not narrated beat by beat). Longest real-footage still: only the 2.2 s home opening.

## Per-line table (out window | source | what is shown | match)
| L | out | src | shown | match |
|---|---|---|---|---|
| 1 | 0-6.86 | 0-2.2, 255-259.2 | Canva home, then the finished heading in the page view | partly (result shown, no outline/shadow detail) |
| 2 | 6.86-10.74 | 12.2-13.8, 21.4-23.2, 26.8-28.6 | Create a design dialog, Text panel with Title / add text box, Hello on the page | yes |
| 3 | 10.74-16.36 | 28.6-31.2, 42.2-45.0, 45.2-46.8 | text size 164 set, toolbar with Alignment tooltip, centre guides | partly (no spacing, font choice not distinct) |
| 4 | 16.36-21.12 | 47.9-51.5 | Duplicate button hovered, clicked at ~17.9 (the "D"), stacked copy appears | yes (button, not the keyboard shortcut) |
| 5 | 21.12-24.54 | 63.0-65.2, 65.2-66.4, 70.3-71.5 | text selected, Effects click, Outline chosen at ~24.1 | yes |
| 6 | 24.54-30.64 | 191.2-194.2, 72.6-77.2 | colour palette opens, then thickness slider dragged 50 -> ~90 | yes |
| 7 | 30.64-33.70 | 92.8-95.6 | second copy appears below and is selected, Effects hover | partly (no Position/Layers panel) |
| 8 | 33.70-42.00 | 97.8-100.0, 100.0-108.9 | effect list (Neon hover), Drop chosen ~35.9, direction/offset/blur/transparency sliders | yes |
| 9 | 42.00-46.76 | 141.6-146.4 | shadow copy moved onto the front copy, centre guides | partly (no layer-order control) |
| 10 | 46.76-53.25 | 195.5-200.8 | both boxes selected, centre guides, letters snap together | partly (no Position panel) |
| 11 | 53.25-58.54 | 181.0-185.5 | single overlapped Hello after alignment, zoomed | yes |
| 12 | 58.54-64.90 | 147.6-150.8, 216.7-219.8 | copy offset above the front text, then lower copy selected | partly |
| 13 | 64.90-73.38 | 173.5-180.8 | Effects panel with Outline highlighted on one copy, two copies on the page | yes |
| 14 | 73.38-75.56 | 202.8-205.2 | Group clicked, toolbar turns to Ungroup | yes |
| 15 | 75.56-78.14 | 223.6-226.6 | group corner handle dragged, group larger | yes |
| 16 | 78.14-83.98 | 236.5-242.5 | grouped heading with font toolbar (page 2) | partly (conceptual) |
| 17 | 83.98-87.08 | 213.4-216.5 | duplicate offset, letters misaligned then two separated copies | yes |
| 18 | 87.08-91.14 | 249.0-253.1 | full-screen preview of the heading with shadow | partly (no download in the take) |
| 19 | 91.14-96.42 | 121.0-125.7, 193.9-196.0 | offset slider raised, then colour palette | yes |

## Uncertain
- analyze-notes.md: coordinates are placeholders; keyboard shortcut, Position/Layers and download have no footage.
- L3: the spacing and font choices are not visible as separate actions.

## Check these
- 33.7-36 (Neon is highlighted until Drop is chosen at ~35.9), 42-46.8 (alignment shown for "move behind"), 61.7-65 and 78-84 (page 2 / group footage used for explanatory lines), 87-91 (preview instead of download).

## Lessons added
- One entry (hover on other effects before the click).
