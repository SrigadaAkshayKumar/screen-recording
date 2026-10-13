# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | sharp | 9.160 | A2 video thumbnail | 8.200 | 0.86x |
| 3 | blur | 16.720 | A3 Blur slider in CapCut | 51.600 | 0.85x |
| 3 | export | 19.360 | A4 Export button in CapCut | 67.400 | 1.25x |
| 4 | Upload | 22.900 | A5 Open button in the file dialog | 85.000 | 1.02x |
| 5 | version | 25.420 | A6 uploaded blurred video thumbnail | 88.400 | 1.35x |
| 5 | whole | 27.840 | A7 corner handle of the blurred clip | 91.200 | 1.16x |
| 7 | sharp | 35.180 | A8 sharp video thumbnail | 111.650 | 1.19x |
| 8 | resize | 39.000 | A9 corner handle of the sharp clip | 124.800 | 1.14x |
| 9 | centre | 43.220 | A10 Position button | 131.450 | 1.43x |
| 10 | timeline | 47.060 | A11 start handle of the clip on the timeline | 138.400 | 0.92x |
| 11 | speed | 51.300 | A12 Speed control | 143.000 | 1.08x |
| 12 | volume | 56.320 | A13 clip audio / volume control | 151.400 | 1.16x |
| 15 | Play | 70.280 | A14 Play button | 178.300 | 0.78x |
| 16 | filled | 75.020 | A15 Share button | 198.300 | 1.18x |
| 16 | download | 76.880 | A16 Download button | 200.900 | 1.40x |
| 16 | MP4 | 78.080 | A17 File type dropdown | 202.500 | 1.33x |

## Builder decisions

- A3: after A2 (until src 11.50) jumps ahead to src 48.50 - narration order
- A5: after A4 (until src 69.00) jumps ahead to src 83.00 - narration order
- A8: after A7 (until src 99.00) jumps ahead to src 110.70 - narration order
- A9: after A8 (until src 114.60) jumps ahead to src 123.40 - narration order
- A10: after A9 (until src 129.60) jumps ahead to src 130.20 - narration order
- A11: after A10 (until src 134.00) jumps ahead to src 137.40 - narration order
- A13: after A12 (until src 148.00) jumps ahead to src 150.60 - narration order
- A14: after A13 (until src 160.00) jumps ahead to src 176.00 - narration order
- A15: after A14 (until src 183.00) jumps ahead to src 197.40 - narration order

## Judgment calls
- No zooms/ripples: recorder baked-in zoom (lessons 2026-10-10/11) plus unverified coordinates.
- L1-L2: A1 left unanchored; the intro plays src 0.3-11.5 (empty Canva, Uploads, clip added) at ~0.86x. A2 anchored on "sharp".
- L3 uses CapCut (src 48.5-54 blur drag, cut 54-66.5 idle, then export at 67.4), cross-faded.
- L4-L5 upload dialog / add blurred / enlarge: src 83-99, 1.0-1.35x. L7-L11 use the redo footage (110.7-143) in narration order with cross-faded jumps (A8-A11, A13, A14, A15).
- L13-L14 explanation plays src 151.4-160 and 176-178 at ~0.78x (no hold, no still over 2.5 s).
- Unfixable/accepted warnings: A7 and A9 results appear 1.2 s / 0.6 s after their lines end (long drags); A1 unanchored by design.
- check.py --plan: no pace warnings.
