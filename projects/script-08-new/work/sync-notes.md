# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | mobile | 6.930 | A1 Create design dialog (Create button) | 17.700 | 0.75x |
| 2 | templates | 9.370 | A2 search field | 20.000 | 0.94x |
| 2 | layout. | 11.790 | A3 YouTube Shorts tile | 24.300 | 1.78x |
| 4 | Upload | 17.510 | A4 Uploads tab | 34.500 | 0.91x |
| 5 | Trim | 20.350 | A6 footage video thumbnail | 44.100 | 1.41x |
| 5 | quickly. | 22.570 | A7 trim handle of clip | 54.000 | 1.53x |
| 7 | using | 29.150 | A8 Text tab | 61.600 | 1.16x |
| 8 | easy | 31.330 | A9 Add a heading | 64.300 | 1.24x |
| 8 | subject. | 32.890 | A10 heading text | 68.400 | 1.22x |
| 9 | screen | 35.390 | A11 font size / text box | 73.500 | 1.04x |
| 10 | captions | 42.210 | A12 Captions in toolbar | 110.600 | 0.89x |
| 11 | Generate | 46.670 | A14 Generate captions button | 144.500 | 1.14x |
| 11 | choose | 49.310 | A13 caption style | 135.400 | 0.95x |
| 13 | Keep | 58.570 | A15 caption | 186.500 | 1.25x |
| 14 | Preview | 63.310 | A16 play/preview button | 194.000 | 1.16x |
| 14 | muted | 65.330 | A17 audio / mute | 204.300 | 1.39x |
| 15 | Download | 69.630 | A18 Share button | 215.000 | 0.86x |
| 16 | file | 72.750 | A19 Download button | 225.400 | 1.06x |

## Builder decisions

- A2->A3: fast-forwarded src 21.00-23.00 instead of cutting it (typing dwell)
- A7: after A6 (until src 45.50) jumps ahead to src 52.00 - narration order
- A12: after A11 (until src 76.50) jumps ahead to src 107.50 - narration order
- A14: after A12 (until src 113.20) jumps ahead to src 142.00 - narration order
- A13: after A14 (until src 146.00) jumps back to src 134.40 - narration order
- A15: after A13 (until src 140.00) jumps ahead to src 179.50 - narration order
- A16: after A15 (until src 190.50) jumps ahead to src 192.50 - narration order
- A17: after A16 (until src 195.50) jumps ahead to src 203.00 - narration order
- A18: after A17 (until src 206.00) jumps ahead to src 213.00 - narration order
- A19: after A18 (until src 217.80) jumps ahead to src 224.90 - narration order

## Judgment calls
- No zooms and no ripples anywhere: the recorder's baked-in auto-zoom makes recording-pixel cursor positions unreliable (lessons 2026-10-10 script-1, 2026-10-11 script-18).
- Narration is very brisk against a 238 s recording, so anchors sit on the nearest word that still gives 0.75-1.5x: A4 Uploads on "Upload"; A6 (place footage) on "Trim" and A7 (trim) on "quickly" (a step later than the words "place it" / "Trim"); A8 Text on "using"; A9 on "easy"; A10 on "subject"; A11 on "screen".
- A5 (Videos tab) is not anchored; it plays inside the A4->A6 stretch.
- Narration order differs from the recording for L11: Generate (A14) is shown first, then style choice (A13, jumped back to 134.4, cross-faded). Continuity oddity: the style panel is seen before/after captions are generated.
- L12 ("hidden by YouTube's interface") is covered by footage 179.5-186.5 of the captioned video; A15 caption drag anchored on "Keep".
- Cuts (cross-faded): 28.5-33.5 template loading, 36.0-41.6 still uploads panel, 65.3-67.5 idle heading edit, 70.0-72.5 colour panel; 21.0-23.0 typing dwell is fast-forwarded. Junk: 0-12.5 (earlier design), 78-104.5 (idle/rehearsal; the preview play in it is reused at 192+ instead), 229.5+ (download progress = loading screen).
- Narrated "Upload that file to YouTube ... publishing settings" has no footage; L16 plays the download starting (225.4-229.3).
- Remaining check.py warnings (not pace): A3 and A7 results appear after their lines end (consequence of the compressed anchoring above); A5 unanchored.
