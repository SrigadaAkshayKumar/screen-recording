# script-10 report (diagonal-crop take, new 90.647 s / 20-line voiceover)

## Result
`projects/script-10/output/final.mp4` — 90.63 s, 2560x1440, **verify PASS** (duration, streams, resolution, no freezes >3 s, 31 join boundaries clean). `check.py --plan` OK with **no `pace:` warnings**. freezedetect (d=1.7) on the final: no frozen stretch at all (preview d=1.5 also clean). Speeds per line 0.81-1.22x, no holds, no zooms/ripples (the recorder's own zoom is baked into the footage).

## Stages
- probe, transcribe, align, scenes, frames: reused (already current; not re-run). Alignment: all 20 lines matched (no bad/missing).
- analyze + sync: done as a hand plan (`work/hand_plan.py`, same recipe as earlier script-N projects): per-line groups of source pieces chosen from freezedetect (n=0.002, d=0.8) and 1 s contact sheets; `actions.json` is a stub (empty actions; `check.py --actions` rejects an empty list — same as other hand-plan projects, so Gate D was not applicable).
- preview: 1 fix round (L14 had a 2.37 s near-static stretch; replaced by two shorter pieces around the rotation). Final render + verify: PASS.

## Judgment calls
- Follow the audio order: footage is reused out of recording order with cross-fades (e.g. L7 resize uses 65-67 s, L8 placement 60-62 s; L15/L16 re-use crop-session footage 112-124 s; L17 uses the rotate-slider session 144-152 s). No dead time cut; static spans were played at 1x as short pieces (opening 0-4.2 s at fixed 2.2 s = ~1.9x).
- The take has no footage of typing "triangle frame / diagonal frame" (L3), nor a visible "decorative graphic vs image frame" comparison (L5), so those lines show the nearest real step (Frames panel, frame placed on the page).
- Waits/idle spans in the take (123-140 s, 173-189 s, 74-79 s, 91-98 s, 104-110 s) were skipped, not stretched.
- No zooms/ripples: the recording already has the recorder's baked zoom.

## Per-line table (frames taken from final.mp4)
| L | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0.0-5.9 | 0-4.2 (2.2 s), 4.2-7.6 | Canva home, then Create a design menu opening | yes |
| 2 | 5.9-8.3 | 8.9-10.0, 16.9-18.4 | new blank design, then Elements panel opened | yes |
| 3 | 8.3-13.3 | 20.2-24.6 | Frames category clicked (~9.5), frames list | partly (no typed search in footage) |
| 4 | 13.3-15.8 | 24.6-27.1 | cursor on triangle frame, it lands on page | yes |
| 5 | 15.8-20.0 | 27.1-31.3 | frame on page, selected (image frame container) | partly |
| 6 | 20.0-22.9 | 36.9-39.6 | zoomed view of the frame with its toolbar | yes |
| 7 | 22.9-25.1 | 65.0-67.3 | corner handle dragged, size label, frame enlarged | yes |
| 8 | 25.1-34.0 | 60.3-62.6, 67.3-69.9, 71.8-74.1 | right-triangle frame placed, large against one side, empty side free | yes |
| 9 | 34.0-37.8 | 79.8-83.5 | Uploads panel, photo dragged over the frame | yes |
| 10 | 37.8-41.1 | 83.5-86.7 | photo fills the frame on release | yes |
| 11 | 41.1-44.0 | 86.8-89.5 | double-click, crop panel appears | yes |
| 12 | 44.0-49.9 | 99.0-103.0, 110.8-112.4 | crop mode, image moved inside the shape | yes |
| 13 | 49.9-51.6 | 103.0-104.7 | Done / back to normal view | yes |
| 14 | 51.6-57.2 | 154.6-156.8, 158.3-161.7 | frame rotated | yes |
| 15 | 57.2-63.3 | 112.4-114.5, 115.8-119.8 | bird in the triangle, away from the diagonal edge | yes |
| 16 | 63.3-68.4 | 119.8-124.0 | finished crop result | yes |
| 17 | 68.4-74.9 | 144.0-147.7, 149.8-152.3 | rotate slider turns the photo; the diagonal mask stays | yes |
| 18 | 74.9-78.2 | 161.9-165.2 | frame with photo inside, zoomed out | yes |
| 19 | 78.2-83.4 | 189.5-194.6 | double-click again, crop panel reopened, Done | yes |
| 20 | 83.4-90.6 | 195.0-198.0, 200.0-202.7, 205.8-209.0 | Share > Download, file-type list (JPG/PNG), transparent background toggle | partly (file type shows JPG at 87 s while PNG is narrated) |

## Uncertain
- L3/L5 lack footage for the typed search and the "decorative graphic" distinction.
- L20: the take selects JPG first; PNG + transparent toggle appears at the end.

## Check these
- 8.3-10 s (Frames click vs "Frames category"), 87 s (JPG shown while "PNG" is narrated), 49.9-52 s (Done), cross-fade joins around 25, 57, 63, 68 s.

## Lessons added
- Appended a short script-10 re-edit entry to docs/lessons.md.
