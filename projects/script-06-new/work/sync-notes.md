# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | upload | 7.950 | A1 Uploads tab in the left sidebar | 19.500 | 1.00x +5.8s hold |
| 2 | uploads. | 9.190 | A2 Upload files button | 21.100 | 1.29x |
| 3 | canvas, | 11.090 | A4 uploaded clip thumbnail | 24.550 | 1.08x |
| 3 | select | 13.650 | A5 video clip in the timeline | 40.600 | 1.23x |
| 4 | Remover | 16.130 | A6 BG Remover in the toolbar | 42.900 | 0.93x |
| 5 | Edit | 21.870 | A8 Edit in the toolbar | 70.600 | 1.06x |
| 8 | play | 31.530 | A7 Play button | 64.500 | 0.94x |
| 9 | colour, | 39.050 | A9 colour swatch in the toolbar | 131.000 | 0.88x |
| 10 | position | 42.210 | A12 Position in the toolbar | 152.400 | 1.14x |
| 10 | move | 44.610 | A10 blue background clip in timeline | 140.900 | 1.08x |
| 11 | position | 47.370 | A11 end handle of the clip | 148.800 | 1.20x |
| 12 | tutorials | 51.510 | A13 timeline zoom control | 195.600 | 0.85x |
| 15 | footage | 66.410 | A14 Play button | 225.200 | 1.02x |
| 16 | Preview | 70.210 | A15 Play button | 237.000 | 1.29x |
| 17 | Export | 73.610 | A16 Share button | 241.900 | 1.44x |
| 17 | save | 75.510 | A17 File type dropdown (MP4 Video) | 244.500 | 1.37x |
| 17 | background. | 77.350 | A18 Download button | 254.450 | 1.28x |

## Builder decisions

- A5: after A4 (until src 26.30) jumps ahead to src 39.20 - narration order
- A8: after A6 (until src 47.40) jumps ahead to src 69.00 - narration order
- A7: after A8 (until src 72.20) jumps back to src 49.00 - narration order
- A9: after A7 (until src 69.20) jumps ahead to src 129.10 - narration order
- A12: after A9 (until src 133.70) jumps ahead to src 151.50 - narration order
- A10: after A12 (until src 154.00) jumps back to src 139.90 - narration order
- A10->A11: cut src 143.20-147.80 - too long to fast-forward at <= 2.00x (extra track dragging)
- A13: after A11 (until src 151.20) jumps ahead to src 194.50 - narration order
- A14: after A13 (until src 210.20) jumps ahead to src 224.60 - narration order
- A15: after A14 (until src 229.50) jumps ahead to src 236.40 - narration order

## Judgment calls
- Audio order followed: A8 (Edit, rec 70.6) is shown before A7 (Play, rec 64.5) because the audio opens Edit (L5) before play/inspect (L8); A12 Position before A10 layer drag (L10).
- Anchor words: upload/uploads (A1/A2), canvas (A4), select (A5), Remover (A6), Edit (A8), play (A7), colour (A9), position (A12), move (A10), position L11 (A11), tutorials (A13), footage (A14), Preview (A15), Export/save/background (A16-A18).
- A3 (Open in file dialog) is not anchored: no room in the narration; its dialog is cut 21.6-23.0 (cross-fade).
- Intro (0-5.75 s) was hand-edited in plan.json: the recording starts with 15 s of an idle editor, so the intro plays moving footage of the finished preview (src 227.5-233.25, 1x), then cross-fades to the first step. Re-running plan_builder would revert this.
- Other cuts: 54.6-62.6 idle timeline after processing; 143.2-147.8 extra-track dragging (too long for 2x); 245.6-253.2 idle Download panel.
- A "wait" for processing is not an action; L7 plays rec 49-54.6 (thumbnails turning into cut-outs) as the wait.
- No zooms and no ripples: the recorder baked in auto-zoom through most of the clicks (lesson 2026-10-10/11), so coordinates in recording pixels would not match the picture. All actions are in no_ripple.
- Unmentioned in the audio and skipped: trim of the 33 s clip (rec 33-36), blue swatch pick, gradient pick, scrubbing 196-210 beyond what L12-L14 reuse.
- Closing: src_end 257.5 (desktop/recorder stop after 257.6 cut), 0.75x then a 1.4 s hold.
