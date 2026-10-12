# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 4 | empty | 16.620 | A1 empty area of the page | 30.100 | 0.78x |
| 4 | Animate | 18.400 | A2 Animate button in the toolbar | 34.550 | 1.26x |
| 8 | Open | 30.840 | A3 Magic Animate card | 44.600 | 0.81x |
| 9 | combination | 35.460 | A4 Professional (recommended style) | 65.500 | 0.78x |
| 10 | alternative | 40.980 | A6 Bold alternative style | 122.800 | 1.01x |
| 11 | Preview | 42.940 | A5 page 2 thumbnail | 90.200 | 1.07x |
| 13 | select | 54.960 | A9 right-hand bottle | 200.400 | 1.33x |
| 14 | timing | 59.320 | A7 timing (clock) button | 140.600 | 0.92x |
| 18 | presentation, | 76.840 | A8 Present button | 192.400 | 1.22x |
| 18 | share | 79.680 | A10 Share button | 205.200 | 0.95x |
| 18 | Share, | 82.000 | A11 Download in Share panel | 206.800 | 1.00x +0.7s hold |
| 18 | MP4 | 84.000 | A12 MP4 Video in file type list | 212.000 | 1.30x |

## Builder decisions

- A6: after A4 (until src 70.20) jumps ahead to src 121.90 - narration order
- A5: after A6 (until src 124.00) jumps back to src 89.30 - narration order
- A9: after A5 (until src 105.00) jumps ahead to src 199.20 - narration order
- A7: after A9 (until src 203.00) jumps back to src 139.20 - narration order
- A8: after A7 (until src 159.00) jumps ahead to src 189.50 - narration order
- A10: after A8 (until src 194.20) jumps ahead to src 204.30 - narration order

## Judgment calls

- Anchors: A1 "empty", A2 "Animate" (L4); A3 "Open" (L8, click Magic Animate); A4 "combination" (L9, the Professional click: "Open"->"Choose" leaves only 3.4 s, so the click sits on "combination" to keep the loading/idle cut at <=1.5x); A6 "alternative" (L10, Bold style); A5 "Preview" (L11, page 2 thumbnail); A9 "select" (L13, select the bottle); A7 "timing" (L14, clock button); A8 "presentation" (L18, Present); A10 "share" (L18, Share); A11 second "Share," (L18, Download in the Share panel, a bit before the word "Download" so that MP4 gets enough time); A12 "MP4".
- Out-of-order footage (audio order wins): alternative style (src 122.8) before the page review (90.2), object selection (200.4) before timing (140.6), Present (192.4) after timing; all cross-faded.
- Cuts (cross-faded): 11.8-28.9 wandering and recorder zoom, 31.0-33.2 zoom transition, 45.5-49.4 Magic Animate loading screen, 50.4-63.8 idle on the recommended style, 207.4-210.0 idle in the download panel. No in-scene fast-forward above 1.33x was needed; no pace warnings.
- No zooms (recording has baked-in zoom); ripples only on A3, A4, A6.
- Present mode shows only ~1.8 s (192.4-194.2) and then jumps to the Share click, because L18 gives 3 s for Present + Share.
- A13 (final Download click at 218.0) is not narrated and falls ~0.3 s after the end of the plan (src_end 217.68); the video ends on the MP4 Download panel, idle for the last ~3 s (closing hold, source is static there).
- Unmentioned actions: the empty-area click happens before "Animate" is narrated, per the script; timing slider/toggle, Transitions panel and extra alt styles are not narrated and play at ~1.2x or are not used.
- Warnings left: "A2: result appears at 20.07 s, after line 4 ends" (the panel opens ~1.7 s after the click; harmless, L5 is about the panel), "A13 not tied to a word" (intentional).
