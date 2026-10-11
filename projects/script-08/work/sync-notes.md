# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | computer. | 7.920 | A1 File Explorer icon in the taskbar | 17.700 | 2.23x |
| 5 | Open | 17.800 | A2 File Explorer minimize button | 37.900 | 2.04x |
| 5 | Uploads | 19.700 | A3 Uploads in the Canva sidebar | 44.500 | 0.79x |
| 5 | Upload | 20.860 | A4 Upload files button | 49.100 | 1.21x |
| 6 | Choose | 22.500 | A5 voice recording file in the dialog | 50.600 | 0.91x |
| 6 | Open | 23.940 | A6 Open button | 51.800 | 0.83x |
| 7 | Audio | 27.460 | A7 Audio tab | 52.800 | 1.00x +2.5s hold |
| 7 | add | 28.060 | A8 voice.mp3 in the Audio list | 66.200 | 2.33x |
| 8 | Move | 29.420 | A9 audio track on the timeline | 67.900 | 1.25x |
| 9 | Play | 33.020 | A10 Play button | 84.600 | 1.47x |
| 10 | trim | 38.240 | A11 audio track beginning handle | 103.900 | 1.00x +3.0s hold |
| 11 | Move | 40.720 | A12 trimmed audio track | 118.600 | 3.02x |
| 12 | Trim | 44.280 | A13 audio track end handle | 121.500 | 0.81x |
| 12 | adjust | 46.880 | A14 Volume button in the audio toolbar | 130.100 | 2.12x |
| 14 | voice | 53.020 | A16 Upload files button (second time) | 146.900 | 1.00x +2.9s hold |
| 16 | convert | 62.680 | A17 Cancel button in the dialog | 163.000 | 1.67x |
| 16 | supported | 64.000 | A18 File Explorer icon in the taskbar | 164.300 | 0.98x |
| 18 | Make | 68.760 | A19 File Explorer minimize button | 176.700 | 1.00x +3.4s hold |
| 18 | Share, | 71.240 | A20 Share button | 181.300 | 1.85x |
| 18 | Download | 72.100 | A21 Download in the share panel | 183.400 | 2.44x |
| 18 | Video. | 73.640 | A22 MP4 Video file type | 185.400 | 1.30x |
| 19 | Your | 75.000 | A23 Download button | 188.500 | 1.10x |

## Builder decisions

- intro: fast-forwarded src 5.00-17.20 instead of cutting it (junk: idle Canva screen before the Explorer is opened)
- A1->A2: fast-forwarded src 22.60-36.40 instead of cutting it (junk: idle File Explorer, nothing changes)
- A2->A3: cut src 38.80-43.90 - too long to fast-forward at <= 2.00x (junk: idle, cursor drifting to the sidebar)
- A3->A4: cut src 45.40-48.60 - too long to fast-forward at <= 2.00x (junk: idle Uploads panel, cursor moving to Upload files)
- A9->A10: cut src 72.60-84.00 - too long to fast-forward at <= 2.00x (junk: idle timeline, cursor wandering to Play)
- A10->A11: cut src 86.30-103.40 - too long to fast-forward at <= 2.00x (junk: playback and replay, hovering the timeline)
- A11->A12: cut src 111.00-118.20 - too long to fast-forward at <= 2.00x (idle timeline between the two trims)
- A13->A14: cut src 126.80-129.90 - too long to fast-forward at <= 2.00x (junk: idle timeline)
- A14->A16: cut src 132.40-146.00 - too long to fast-forward at <= 2.00x (junk: idle with the volume popup open)
- A16->A17: fast-forwarded src 149.50-162.40 instead of cutting it (junk: idle open-file dialog)
- A18->A19: cut src 165.20-176.20 - too long to fast-forward at <= 2.00x (junk: idle File Explorer)
- A19->A20: fast-forwarded src 177.60-180.90 instead of cutting it (junk: idle Canva editor)
- A22->A23: cut src 186.60-188.20 - too long to fast-forward at <= 2.00x (junk: idle download panel)

## Judgment calls

- No zooms: the recorder's auto-zoom is baked into most of the recording (lessons.md, script-1). Ripples only; drags (A9, A11, A12, A13, A15) have no ripple because their pixels are low confidence.
- Narration order is the footage order, so no out-of-order jumps were needed. Narrated "select the audio" (L10) has no separate click; "preview" (L12) is held on the volume popup because the only playback happens earlier (A10).
- A1 on "computer": opening File Explorer illustrates "save the file to your computer"; the idle Explorer (22.6-36.4) is fast-forwarded under L3-L4.
- A16-A18 (a second Upload files dialog, cancelled, then Explorer again) are not in the script's steps. They are used under L14-L17 (link vs. local file, convert, file extension) as illustration, fast-forwarded (~1.7x) rather than cut.
- A8 "add": the menu detour (60.3-65.4, Add audio menu opened by mistake) is cut; the idle voice.mp3 preview before it is fast-forwarded/cut by the builder.
- A23 on "Your" (L19): the final Download click starts the "downloading" toast that stays on screen while L19 plays; tail trimmed at src 194.0.
- Cuts the builder made because the idle spans did not fit at <= 2x are listed in the notes above (11 cuts, all in-scene idle time). 
- Warnings: A1, A9, A11, A22 results land slightly after their line ends (0.3-0.6 s), harmless. A15 (volume slider drag) has no word: it follows A14 within 0.3 s.
