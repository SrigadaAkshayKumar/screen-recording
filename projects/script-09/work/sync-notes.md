# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Open | 7.520 | A1 Uploads sidebar button | 13.200 | 1.36x |
| 2 | timeline. | 10.800 | A3 talking video thumbnail | 18.700 | 1.68x |
| 4 | text, | 16.660 | A4 Text sidebar button | 36.300 | 1.52x |
| 4 | captions. | 20.020 | A5 Captions under Dynamic text | 42.600 | 1.88x |
| 5 | Select | 21.520 | A6 talking video on timeline | 49.600 | 1.07x |
| 5 | generate | 23.660 | A7 Generate captions button | 55.400 | 1.50x |
| 6 | reading | 26.340 | A9 Play button | 77.100 | 0.90x |
| 7 | Correct | 27.680 | A14 Captions button in toolbar | 171.900 | 1.04x |
| 7 | spending | 30.180 | A15 transcript line (edit) | 175.700 | 1.52x |
| 9 | Select | 36.140 | A10 caption on timeline | 96.600 | 1.48x |
| 10 | Position | 39.780 | A11 caption on the page | 106.000 | 0.82x |
| 12 | contrast | 51.780 | A13 Effect colour button | 128.400 | 1.12x |
| 16 | captions | 64.840 | A16 Styles tab in Captions panel | 194.500 | 1.00x |
| 17 | Watch | 69.180 | A17 Play button | 213.100 | 1.38x |
| 19 | share, | 77.460 | A18 Share button | 229.000 | 1.61x |
| 19 | video. | 79.740 | A21 Download button | 240.400 | 1.23x |
| 20 | exported | 81.240 | A23 File Explorer in taskbar | 277.000 | 1.00x |
| 20 | subtitles | 82.980 | A24 exported video file (double click) | 290.800 | 1.15x |

## Builder decisions

- A3->A4: cut src 25.30-34.00 - too long to fast-forward at <= 2.00x (junk: clip trimmed / page blank, not narrated)
- A5->A6: cut src 43.60-49.00 - too long to fast-forward at <= 2.00x (junk: cursor wanders in the Captions panel)
- A9: after A7 (until src 56.30) jumps ahead to src 75.60 - narration order
- A14: after A9 (until src 77.80) jumps ahead to src 171.20 - narration order
- A10: after A15 (until src 183.00) jumps back to src 95.10 - narration order
- A16: after A13 (until src 137.90) jumps ahead to src 191.00 - narration order
- A13->A16: fast-forwarded src 137.80-149.70 instead of cutting it (junk: idle, cursor only)
- A17: after A16 (until src 199.00) jumps ahead to src 211.60 - narration order
- A21: after A18 (until src 230.60) jumps ahead to src 239.20 - narration order
- A23: after A21 (until src 241.00) jumps ahead to src 276.10 - narration order
- A23->A24: cut src 278.20-290.00 - too long to fast-forward at <= 2.00x (junk: browsing the Downloads folder)

## Judgment calls

- **No zooms, no ripples.** The recording has the recorder's baked-in auto-zoom on nearly every
  click; the plan's zoom/ripple would double-zoom or land in the wrong place (lessons 2026-10-10,
  2026-10-11). All actions are `no_ripple`, `zooms: []`.
- **Narration order wins**, so the footage jumps (cross-faded): L7 (correct transcription) uses
  src 171-183 before L9 (style, src 96+); L16 jumps to the Styles tab (191+); L17 to the second
  Play (211+); L19-20 jump over the download wait (241-276) to the Explorer/player.
- Anchor words: A1 Uploads @ "Open" and A3 thumbnail @ "timeline" (the Videos tab A2 is not
  anchored: no room, 0.4-0.9 s gaps would need > 4x); A4 Text @ "text", A5 Captions @ "captions",
  A6 @ "Select", A7 Generate @ "generate"; A9 Play @ "reading" (not "Play": the caption
  processing wait had to be cut and "Play" came only 1.3 s after "generate"); A14 Captions
  button @ "Correct", A15 edit line @ "spending"; A10 select caption @ "Select"; A11 drag @
  "Position"; A13 Effect colour @ "contrast"; A16 Styles @ "captions"; A17 Play @ "Watch";
  A18 Share @ "share"; A21 Download @ "video"; A23 Explorer @ "exported"; A24 open file @ "subtitles".
- A12 (playhead scrub 124.5, "test a section") is not anchored: it plays inside the A11->A13
  interval (src 123.5-128.4), which avoided a 2.6 s hold. A19 (Download item) and A20 (MP4 option)
  are not anchored: 0.6-0.9 s between "share", "download", "mp4" is too short; the panel shows
  "MP4 Video" while the Download click lands on "video".
- Cuts (cross-faded): 25.3-34.0 (clip trim, blank page, not narrated), 43.6-49.0 and 50.8-53.4
  (cursor wandering in the Captions panel), 56.6-74.7 (Creating your captions loading screen),
  99.0-105.4 (playhead scrubbing before the drag), 114.5-123.5 (idle after drag),
  217.8-220.4 (cursor-only), 278.2-290.0 (browsing the Downloads folder), 297.5+ (recorder stop).
  Most of these did not fit at <= 2x. 137.8-149.7 (idle, caption selected) was fast-forwarded
  by the builder, but the A13->A16 jump skips it anyway.
- Not shown: the second download attempt (249-253), the 255-274 download progress (cut),
  anything about "view-only accessibility captions" (L15, nothing like it in the recording;
  the Effect colour panel plays there instead).
- Pace: no `pace:` warnings. Approach speeds are up to 1.88x on mixed cursor travel (A5);
  everything else <= 1.7x.
