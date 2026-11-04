# script-20 report

## Result
- `projects/script-20/output/final.mp4` — 96.417 s, 2560x1440, 30 fps, **verify PASS** (duration, streams, resolution, frozen spans, 36 joins black-free).
- 35 pieces in 19 groups, one per narrated line, hand-built in `work/hand_plan.py` (no click log, baked recorder zoom -> no plan zooms/ripples). Speeds 0.76–1.48x, no `pace:` warning, no hold.
- Longest still in the final (freezedetect n=0.003, d=1.5): 2.53 s at the very end is cursor-only (2.4 s, 94.0–96.4); next 2.4 s (84.7). All ≤ 2.5 s except the closing one, which is 2.4 s.

## Stages
- probe / transcribe / align / scenes / frames: reused (the new 239.5 s recording replaced the committed 265 s take; the work files were already current). Alignment passed.
- analyze + sync: done by hand from 1 s / 0.5 s sheets (a–s) instead of actions.json; the committed hand_plan was for the old take and was rewritten. actions.json/sync.json were not produced.
- preview: rendered 3 times (fixes below); final render 4.2 min; verify PASS.

## Judgment calls
- Take order differs from the script: the take does Effects/Outline first (49–70 s) and duplicates later (71.6 s). Followed the audio order and jumped (cross-faded) to the footage that shows each line.
- The recording's home page (0–7.6 s) is completely static: used only 2.2 s of it, then the finished heading (224–227) and the shadowed pair (109–111).
- Group clicks land 0.5 s after the word "Group"; the duplicate pop (src 71.6) lands on "CMD and D".
- Reused footage: 131–139 Position/Layers panel serves L7, L9, L10, L12; 57–61 and 59–61 outline panel used for L6 and L13.
- Fixed in preview: a blurred recorder-zoom frame at the L14/L19 cut; a 3 s static home opening (final freezedetect); a 2.53 s static slider piece in L19.

## Per-line table (frames checked in final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0–6.86 | 0–2.2, 224–227, 109.2–110.9 | home, finished outline+shadow heading, shadow copy | yes |
| 2 | 6.86–10.74 | 9.2–11.1, 19–21 | Create-design dialog, text box typed "Hello" | yes |
| 3 | 10.74–16.36 | 24–29.6 | font size growing 42 -> 127 | yes |
| 4 | 16.36–21.14 | 43–46, 71.5–73.7 | hover Duplicate, the duplicate pops on "CMD and D" | yes |
| 5 | 21.14–24.54 | 47.4–51.2 | click Effects, Outline highlighted | yes (Outline panel lands slightly after the word) |
| 6 | 24.54–30.64 | 65.6–68.4, 57–61.4 | colour palette, thickness slider | yes (colour/thickness in audio order) |
| 7 | 30.64–33.70 | 131.9–133.9, 136.4–137.5 | click Position, Layers tab with both copies | yes |
| 8 | 33.70–42.02 | 80.3–83.6, 83.6–86.6, 87–90.4 | select copy, Drop effect, direction/offset sliders | partly (softness slider not shown) |
| 9 | 42.02–46.76 | 134–137, 137.4–139.2 | Arrange panel (Backward/To back), Layers rows | partly (the actual send-back click is not in the take) |
| 10 | 46.76–53.26 | 130.8–133.4, 133.4–136.5 | selected text, Position panel, Align Middle/Centre | partly (align click not visible) |
| 11 | 53.26–58.54 | 115–119, 122–124.4 | copy dragged onto the first with guides, then single heading | partly (shadow is barely visible at that zoom) |
| 12 | 58.54–64.96 | 72–74.6, 133.8–137 | offset copy aligned by drag, Align panel | yes |
| 13 | 64.96–73.38 | 59–61.6, 86–89, 100.6–103.2 | outline panel, shadow panel, transparency slider | partly (borrowed panels) |
| 14 | 73.38–75.58 | 147.1–148.9 | Group -> Ungroup | yes |
| 15 | 75.58–78.18 | 180.4–183.4 | grouped heading moved/resized (size tooltip) | yes |
| 16 | 78.18–83.98 | 232.6–237.6 | grouped heading selected, font size shown | partly (take never edits wording) |
| 17 | 83.98–87.08 | 74–77 | two copies drifting out of alignment | yes |
| 18 | 87.08–91.14 | 203.6–205.8, 217.6–220.8 | present mode, download dialog | yes |
| 19 | 91.14–96.42 | 98–100.7, 104.4–107 | shadow sliders, colour swatch | partly |

## Uncertain
- Lines 9–11, 13, 16, 19 show the closest panels, not the exact gesture.
- Background-colour footage (155–177 s) and the context-menu/ungroup footage (192–197 s) are unused.

## Check these
- 19.5–20 s (duplicate pop, cross-fade), 31–33 s (recorder zoom blur), 54 s (overlap, shadow hard to see), 94–96.4 s (cursor-only 2.4 s ending).

## Lessons added
- script-20 re-edit entry appended to docs/lessons.md.
