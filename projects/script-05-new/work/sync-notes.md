# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 5 | open | 26.480 | A1 CapCut editor (taskbar) | 47.500 | 1.29x |
| 6 | blur | 29.860 | A2 Blur slider in the video effect | 51.500 | 1.18x |
| 6 | export | 32.480 | A3 Export button | 60.900 | 1.56x |
| 7 | Upload | 36.100 | A5 Uploads tab | 81.800 | 1.22x |
| 8 | first | 38.840 | A6 blurred video thumbnail | 87.800 | 1.31x |
| 8 | enlarge | 39.520 | A7 corner handle of the blurred clip | 88.400 | 0.88x |
| 10 | sharp | 48.300 | A8 sharp video thumbnail | 111.400 | 1.24x |
| 11 | resize | 52.100 | A9 resize handle of the sharp clip | 119.600 | 0.84x |
| 12 | center | 56.340 | A10 sharp clip (centering) | 125.700 | 1.44x |
| 13 | timeline | 60.180 | A11 clip on the timeline | 139.000 | 1.56x |
| 14 | Keep | 64.040 | A12 clip end handle on the timeline | 145.000 | 1.55x |
| 19 | Play | 82.800 | A13 Play button | 158.800 | 1.32x |
| 20 | Once | 87.180 | A14 Share button | 198.200 | 1.05x |
| 20 | download | 90.020 | A15 Download in the share panel | 199.700 | 1.00x +1.3s hold |

## Builder decisions

- A13: after A12 (until src 152.00) jumps back to src 141.00 - narration order
- A14: after A13 (until src 162.00) jumps ahead to src 196.80 - narration order

## Judgment calls
- No zooms, no ripples: the footage has baked-in recorder zoom/pan and there is no click log, so ripples would land in the wrong place (lessons 2026-10-10, 10-11 script-18).
- Anchors: open (L5), blur/export (L6), Upload (L7), "first" for the blurred thumbnail (L8; "blurred" left no room for the file-picker cut), enlarge, sharp, resize, center, timeline, Keep (L14), Play (L19), Once/download (L20).
- A4 (CapCut dialog Export click) is unanchored: L6 ends 1.2 s before L7, no room; the export progress/"file exists" popups (67.6-81.5) are cut as loading.
- Cuts (cross-faded): idle Canva 35.7-47.2, blur slider idle 55.2-60.5, export dialog 63.8-66.4, loading 67.6-81.5, file picker 84.6-87.0, retake 98.5-110.6, canvas idle 113.6-118.6, idle review 130.7-138.0.
- Reorder/replay: before "Play" the timeline footage 141-152 s is replayed (jump back, cross-fade) to give L13-L18 enough slow footage instead of a 5 s hold. After "Play" the plan plays 158.8-162 and jumps ahead to the Share click at 196.8 (the scrubbing to "middle and end" at 164-196 is skipped).
- Narrated but not on screen: "set the background copy's volume to zero" (L15) - never shown in the recording; timeline footage plays instead.
- The recording's first 35 s (sharp clip uploaded and placed) play under L1-L5; they show the empty-space design of L3 but also an upload that is not narrated.
- All pace: warnings cleared; the only remaining check.py warning is that A4 is not tied to a word (intentional).
