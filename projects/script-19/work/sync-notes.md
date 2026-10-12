# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | create | 6.560 | A1 Video category on the Canva homepage | 16.400 | 0.98x |
| 2 | vertical | 8.520 | A2 Instagram Reel design | 18.600 | 1.12x |
| 4 | Open | 15.200 | A3 Uploads in the left sidebar | 23.700 | 0.76x |
| 4 | click | 16.240 | A4 Upload files button | 24.900 | 1.15x |
| 4 | select | 17.720 | A5 Open button of the file picker (footage selected) | 29.000 | 1.01x |
| 5 | Drag | 19.260 | A7 uploaded clip thumbnail | 31.700 | 1.04x |
| 6 | dragging | 24.220 | A8 right edge of the clip on the timeline | 37.900 | 1.25x |
| 8 | select | 32.800 | A11 video on the canvas | 64.500 | 1.36x |
| 8 | crop | 34.720 | A12 video on the canvas (move) | 72.000 | 1.30x |
| 8 | fit | 35.740 | A13 right handle of the video | 73.400 | 1.37x |
| 9 | subject | 38.700 | A14 start of the timeline | 118.850 | 0.79x |
| 10 | Add | 40.940 | A16 Text in the left sidebar | 159.900 | 1.00x +0.7s hold |
| 10 | panel. | 42.660 | A17 Add a heading | 162.000 | 1.22x |
| 11 | timing | 43.840 | A15 Timing slider | 140.900 | 1.10x |
| 12 | boxes | 48.200 | A18 heading text box | 174.000 | 1.01x |
| 13 | away | 51.760 | A20 heading text box | 184.500 | 1.04x |
| 14 | music | 58.500 | A21 Uploads in the left sidebar | 204.400 | 1.07x |
| 14 | voiceover | 59.720 | A22 Audio tab | 207.000 | 1.15x |
| 14 | audio | 60.820 | A23 voice-over.mp3 | 208.200 | 1.09x |
| 15 | music | 62.600 | A24 Volume button in the toolbar | 221.600 | 1.35x |
| 15 | speech | 63.720 | A25 volume slider | 222.500 | 0.80x |
| 17 | canvas | 68.900 | A26 playhead on the timeline | 236.700 | 0.91x |
| 18 | Review | 73.700 | A27 first clip on the canvas | 244.200 | 1.15x |
| 19 | Play | 78.920 | A28 Play button | 267.800 | 1.26x |
| 19 | check | 80.280 | A29 Share button | 284.900 | 1.18x |
| 19 | layer, | 81.560 | A30 Download in the share panel | 286.400 | 1.17x |
| 19 | MP4 | 83.060 | A32 MP4 Video option | 290.600 | 1.47x |
| 20 | Review | 84.820 | A33 Download button | 296.500 | 1.08x |

## Builder decisions

- A16: after A14 (until src 119.70) jumps ahead to src 159.20 - narration order
- A15: after A17 (until src 162.80) jumps back to src 140.40 - narration order
- A18: after A15 (until src 144.30) jumps ahead to src 173.00 - narration order

## Judgment calls

- **No zooms, no ripples**: the recorder has baked-in auto-zoom (many frames are zoomed), so cursor coordinates are only approximate (all low confidence) and a plan zoom/ripple would double-zoom or land off the cursor (lessons 2026-10-10/11).
- **Anchors**: each action sits on the word that names it (Open/click/select for the upload steps, "Drag", "dragging" for trim, "select/crop/fit" for the canvas edit, "Add"/"panel." for text, "timing", "boxes", "away", "music/voiceover/audio", "music/speech", "canvas", "Review", "Play/check/layer,/MP4", "Review"). Several are placed on a neighbouring word instead of the ideal one so every approach stays 0.75-1.5x.
- **Order conflicts** (builder notes): the recording sets the clip *timing* (140 s) before adding the heading (160 s); narration is heading first, so A15 jumps back with a cross-fade. The heading is therefore not yet on the canvas while timing is shown. A14 (playhead to first clip, "keep subject visible") and A16 jump forward over idle time.
- **Cuts (18, cross-faded)**: file-picker browsing, upload loading, idle cursor stretches, fine crop tweaks (75-118 s), scrubbing, playback of the full reel (269-284.7), a browser download-history popup opened by accident (280-284.7). Only dead time or mistakes; narrated steps all play. No stretch is played faster than 1.5x and there is no held frame over 0.7 s.
- **Unnarrated actions** (no anchor): A6 Videos tab, A9/A10 adding the second (horizontal) clip (plays during line 7, which has no matching action), A19 text colour, A31 file-type dropdown.
- Narrated with no action: "9x16 canvas, 1080x1920" (canvas simply visible), "Add other text boxes" (shows typing the heading text), "Here's the part many tutorials skip" (continues the volume footage), "Review each clip separately" (clip select/scrub).
- Dropped as actions (cut instead): second crop moves at 85-88 s and the first-clip trim at 130 s.
- Warning left: A2 result appears 11.4 s, after line 2 ends - the canvas loads while line 3 (canvas size) is read; intended.
