# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Canva's | 16.760 | A1 Edit button in Canva toolbar | 15.100 | 0.90x |
| 2 | process | 18.880 | A2 Filters "See all" | 17.400 | 1.08x |
| 4 | Upload | 27.640 | A3 Import button (CapCut) | 37.500 | 0.95x |
| 4 | timeline. | 30.200 | A6 "+" add to timeline on the clip | 42.400 | 1.25x |
| 5 | effects, | 31.500 | A7 Effects tab | 71.000 | 1.46x |
| 5 | effects, | 32.960 | A8 Video effects | 73.900 | 1.23x |
| 6 | Apply | 35.740 | A9 blur effect thumbnail | 103.200 | 1.19x |
| 6 | strength | 38.360 | A11 Blur strength slider | 114.500 | 1.22x |
| 7 | Extend | 41.560 | A10 end of the effect strip | 108.300 | 1.12x |
| 8 | Play | 45.080 | A12 Play button in the preview | 139.300 | 1.11x |
| 9 | result | 51.140 | A13 Export button | 149.500 | 0.94x |
| 11 | open | 59.300 | A14 Uploads in the Canva sidebar | 184.300 | 1.58x |
| 12 | it | 62.980 | A18 blurred clip thumbnail | 206.700 | 1.28x |
| 12 | position, | 65.340 | A20 Position button | 218.800 | 1.31x |
| 13 | place | 67.880 | A22 Text tab | 246.000 | 1.46x |
| 13 | or | 69.940 | A23 Add a heading | 248.300 | 1.12x |
| 15 | transparency | 75.680 | A25 Transparency button | 284.100 | 1.01x |
| 15 | how | 77.120 | A26 Transparency slider | 285.500 | 0.97x |
| 18 | Preview | 84.120 | A24 finished design (idle, reused for the closing lines) | 277.500 | 0.81x |

## Builder decisions

- A11: after A9 (until src 105.50) jumps ahead to src 113.60 - narration order
- A10: after A11 (until src 117.60) jumps back to src 107.80 - narration order
- A12: after A10 (until src 113.60) jumps ahead to src 138.50 - narration order
- A13->A14: fast-forwarded src 151.50-156.50 instead of cutting it (export dialog dwell)
- A13->A14: fast-forwarded src 162.90-165.50 instead of cutting it (export dialog dwell)
- A25: after A23 (until src 253.00) jumps ahead to src 283.00 - narration order
- A24: after A26 (until src 287.40) jumps back to src 273.70 - narration order

## Judgment calls

- **No zooms.** The recorder bakes in auto-zoom in many places and click coordinates are rough (no clicks.json), so zooms would frame the wrong place. Ripples only, and `no_ripple` on clicks inside recorder zoom or with uncertain position (A1, A2, A8-A11, A14, A15, A19, A21, A22, A24-A26).
- **Audio order.** The recording extends the strip (108-113 s) before adjusting strength (114-117 s); narration says strength first. A11 (strength) is anchored on L6, A10 (extend) on L7, each with cross-faded jumps (`src_from`/`prev_until`). A12 (play) jumps ahead to 138.5.
- **Cuts with cross-fade (dead time/loading/unnarrated):** 25-36.8 (end of Canva scene + CapCut idle), 39.3-41 (file dialog loading), 43.6-70.3 (idle), 72.3-73.4 and 74.6-100.6 (CapCut loading spinner, 26 s), 109.4-111.6, 144.4-148.9 (playback finished, frozen), 156.9-162.5 and 166-174.5 (export dialog dwell and the real export, not narrated), 176-183.8 (original clip deleted in Canva), 185.2-206 (Canva upload loading/browsing, four cuts), 208.3-218.4, 220-230.9, 232.6-245.2 (unnarrated Canva edits). Export dialog 151.5-156.5 and 162.9-165.5 are fast-forwarded (ff, under 2x).
- **Anchors** on the word naming the control: Edit on "Canva's" (start of line 2), See all on "process", Import on "Upload", add-to-timeline on "timeline", Effects/Video effects on the two "effects,", Apply on "Apply", strength on "strength", extend on "Extend", Play on "Play", Export on "result" (later than "Export" to keep the approach under 1.5x), Uploads on "open", add thumbnail on "it", Position on "position,", Text on "place", Add a heading on "or", Transparency on "transparency", slider on "how".
- **Closing lines (17-18) have no footage.** The recording ends mid transparency drag at 287.4 s. A24 is a pseudo action (kind scroll) so the builder can reuse the idle finished design (273.7-281.8 s, text over the blurred clip) at ~0.8x/1x under "Use a clip with the blur rendered" and "Preview your Canva design and download...". The Canva preview/download is not in the recording.
- **Narrated 'browse the blur category'** has no click in the recording; the Video effects list (101 s) plays there.
- **Unmentioned/unanchored actions:** A4, A5 (file dialog), A15-A17 (Canva upload dialog, Videos tab), A19 (resize), A21 (trim): they play inside their neighbours' intervals.
- **Unfixable warning:** A26 (transparency slider drag) completes at 79.3 s, 1 s after line 15 ends, because A25 and A26 are only 0.5 s apart in the narration. The slider move plays during "It does not blur...".
