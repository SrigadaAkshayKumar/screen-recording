# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads | 7.000 | A1 Uploads in the left sidebar | 15.650 | 2.24x |
| 3 | Upload | 9.360 | A2 Upload files button | 19.750 | 1.74x |
| 4 | audio | 11.040 | A3 script-15 audio file in the picker | 25.600 | 1.22x |
| 4 | Open. | 12.240 | A4 Open button | 31.150 | 1.29x |
| 6 | file | 18.060 | A8 script-15 file in the Audio tab | 59.750 | 0.96x |
| 7 | Add | 21.100 | A6 Add audio button on the timeline | 54.850 | 0.92x |
| 7 | select | 24.260 | A7 Uploads item in the Add audio menu | 56.500 | 1.00x +1.5s hold |
| 9 | Drag | 27.680 | A9 audio track | 80.100 | 1.17x |
| 10 | drag | 34.140 | A10 right edge of the audio track | 84.700 | 1.00x +1.9s hold |
| 11 | track | 37.660 | A11 audio track menu (three dots) | 98.700 | 1.59x |
| 11 | volume | 39.320 | A12 Volume in the menu | 102.000 | 1.99x |
| 11 | adjust | 40.620 | A13 volume slider | 104.300 | 1.77x |
| 12 | play | 42.340 | A14 Play button | 111.750 | 2.01x |
| 13 | already | 45.240 | A17 first video thumbnail | 126.500 | 1.62x |
| 13 | tracks | 47.500 | A18 Audio tools button in the toolbar | 155.200 | 1.68x |
| 13 | competing | 49.220 | A19 video volume slider | 156.200 | 1.00x +0.7s hold |
| 15 | PNG, | 55.560 | A23 File type dropdown | 204.500 | 1.00x +2.5s hold |
| 16 | MP4 | 60.980 | A24 MP4 Video option | 205.800 | 1.00x +4.1s hold |
| 17 | end | 65.840 | A20 end of the video clip | 192.500 | 1.00x +3.2s hold |
| 19 | Share, | 71.940 | A21 Share button | 199.900 | 1.21x |
| 19 | Download | 72.760 | A22 Download in the Share panel | 201.350 | 1.77x |
| 19 | download | 75.400 | A25 Download button | 210.900 | 2.18x |

## Builder decisions

- intro: fast-forwarded src 0.00-12.00 instead of cutting it (junk: idle start before the first action)
- A2->A3: cut src 20.60-24.40 - too long to fast-forward at <= 3.00x (file picker loading/browsing)
- A3->A4: cut src 26.40-30.40 - too long to fast-forward at <= 3.00x (cursor wanders in the picker)
- A8: after A4 (until src 35.00) jumps ahead to src 58.00 - narration order
- A6: after A8 (until src 61.00) jumps back to src 53.30 - narration order
- A9: after A7 (until src 58.20) jumps ahead to src 61.00 - narration order
- A7->A9: cut src 62.50-79.30 - too long to fast-forward at <= 3.00x (junk: unnarrated playback test (clock stays at 0:01))
- A10->A11: cut src 88.40-96.80 - too long to fast-forward at <= 3.00x (junk: hesitation: track held mid-drag, cursor hovering)
- A13->A14: cut src 106.60-110.60 - too long to fast-forward at <= 3.00x (cursor idle after slider)
- A17: after A14 (until src 112.95) jumps ahead to src 123.00 - narration order
- A14->A17: fast-forwarded src 112.60-121.90 instead of cutting it (junk: preview playing, nothing changes)
- A17->A18: cut src 128.60-153.50 - too long to fast-forward at <= 3.00x (junk: unnarrated video clip resizing and idle)
- A23: after A19 (until src 158.50) jumps ahead to src 203.00 - narration order
- A19->A23: fast-forwarded src 157.50-192.00 instead of cutting it (junk: cursor idles, then Uploads panel browsed (Images/Audio tabs) with no action)
- A19->A23: fast-forwarded src 202.40-204.20 instead of cutting it (idle in Download dialog (dropdown replayed after))
- A20: after A24 (until src 207.00) jumps back to src 192.00 - narration order
- A24->A20: fast-forwarded src 206.40-210.20 instead of cutting it (cursor travels to Download button)
- A22->A25: fast-forwarded src 202.40-204.20 instead of cutting it (idle in Download dialog (dropdown replayed after))
- A22->A25: cut src 206.40-210.20 - too long to fast-forward at <= 3.00x (cursor travels to Download button)

## Judgment calls

- Follow-the-audio reorders: L6 "click the file" shows A8 (59.75 s) before L7's Add audio button (A6, 54.85 s) and Uploads menu item (A7, 56.5 s) - cross-fades between them. L15-16 show the file-type dropdown and MP4 choice (A23/A24, 204-206 s) before L17's timeline-end drag (A20, 192.5 s); L19 then plays Share -> Download -> dropdown again -> Download, so that the narrated "Share, Download and MP4 Video" is shown at its words.
- Anchor words: Uploads, Upload (Files), audio (file), Open, file, Add, select, Drag, drag, track (menu), volume, adjust, play, already (video added), tracks (Audio tools), competing (slider), PNG (dropdown list shows JPG/PNG/PDF), MP4, end, Share, Download, download (2nd).
- A5 (upload progress wait), A15 (Uploads), A16 (Videos tab) have no anchor: they play at whatever speed their interval gets (A15/A16 still got ripples from the builder).
- No zooms: the recorder already zooms the footage (lessons.md, script-1). Ripples only.
- ff: idle start (0-12 s, 4.4x because static), preview playback 112-122 s, idle after the video-volume popover 157-192 s (jumped over by the cross-fade to 203 s), idle in the Download dialog 202-204 s. Cut (did not fit <= 3x): picker 20.6-24.4 and 26.4-30.4, playback test 62.5-79.3, held drag 88.4-96.8, idle after slider 106.6-110.6, video clip resizing 128.6-153.5, cursor travel 206.4-210.2.
- Holds up to 4.1 s: 56.2-60.3 s on the open file-type dropdown (shows JPG/PNG/PDF/MP4 while it is narrated), 61.5-64.7 s on the dialog after choosing MP4, 50.2-52.7 s on the video volume popover.
- L1 and L14 (intro, "Here's the part many tutorials skip") have no matching on-screen action; they play over the idle start and the volume popover.
