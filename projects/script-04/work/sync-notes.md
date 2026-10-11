# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads | 7.640 | A1 Uploads in the left sidebar | 14.100 | 1.85x |
| 3 | Upload | 10.000 | A2 Upload files button | 16.200 | 0.89x |
| 3 | image, | 11.660 | A3 Cognizant Onboarding image in the picker | 25.500 | 0.90x |
| 3 | Open. | 12.480 | A4 Open button | 26.300 | 0.98x |
| 5 | thumbnail | 16.220 | A6 image thumbnail in the Uploads panel | 35.200 | 2.38x |
| 6 | Drag | 18.540 | A9 image on the page | 41.600 | 1.21x |
| 7 | corner | 21.000 | A8 corner handle of the image | 38.800 | 0.77x |
| 8 | select | 26.220 | A10 image on the page | 51.600 | 2.11x |
| 8 | Crop | 27.320 | A11 Crop in the toolbar | 54.300 | 2.45x |
| 9 | Adjust | 28.660 | A12 crop handle | 71.300 | 2.24x |
| 9 | Done | 30.780 | A13 Done in the Crop panel | 79.900 | 3.16x |
| 10 | Elements, | 35.700 | A14 Elements in the left sidebar | 89.200 | 1.89x |
| 10 | find | 36.620 | A15 Frames category | 91.500 | 2.50x |
| 10 | add | 37.500 | A16 circle frame | 93.900 | 2.73x |
| 11 | image | 39.720 | A17 image dragged into the frame | 99.600 | 2.57x |
| 12 | image | 41.980 | A18 image inside the frame (double-click) | 118.300 | 2.74x |
| 12 | reposition | 43.320 | A19 photo inside the frame | 121.600 | 2.46x |
| 14 | Cropping | 48.160 | A21 Crop in the toolbar (second crop) | 142.800 | 1.10x |
| 15 | enlarging | 54.180 | A23 corner handle (enlarge) | 155.000 | 2.03x |
| 16 | Edit | 59.760 | A24 Edit in the toolbar | 175.500 | 1.34x |
| 16 | adjustment | 61.300 | A25 Adjust tool | 179.000 | 2.27x |
| 17 | change | 63.640 | A26 Brightness slider | 184.500 | 2.35x |
| 18 | Share, | 67.580 | A27 Share button | 193.000 | 2.16x |
| 18 | download | 68.500 | A28 Download in the Share panel | 194.600 | 1.74x |
| 18 | format | 69.880 | A29 File type dropdown (PNG) | 197.900 | 2.39x |
| 19 | Your | 71.160 | A30 Download button | 206.000 | 2.03x |

## Builder decisions

- A2->A3: cut src 17.00-24.80 - too long to fast-forward at <= 2.00x (junk: navigating the file picker to Downloads)
- A9: after A6 (until src 37.80) jumps ahead to src 41.40 - narration order
- A8: after A9 (until src 43.20) jumps back to src 38.50 - narration order
- A10: after A8 (until src 41.40) jumps ahead to src 43.20 - narration order
- A11->A12: cut src 56.00-70.00 - too long to fast-forward at <= 2.00x (junk: idle in the Crop panel)
- A12->A13: cut src 77.40-79.30 - too long to fast-forward at <= 2.00x (junk: idle before Done)
- A17->A18: cut src 105.00-117.50 - too long to fast-forward at <= 2.00x (junk: idle after resizing the frame)
- A23->A24: cut src 161.00-174.00 - too long to fast-forward at <= 2.00x (junk: idle after enlarging (recorder zooms))
- A29->A30: cut src 199.00-204.50 - too long to fast-forward at <= 2.00x (junk: hovering the Download panel options)

## Judgment calls

- **Fast-forward first.** Every in-scene stretch plays at 0.8-2.7x; the Crop handle drags at 3.2x.
  Cut, because they could not fit at ≤ 2x:
  - file picker navigation 17.0-24.8;
  - Crop panel idle 56-70;
  - idle 77.4-79.3, idle 105-117.5 and idle 161-174;
  - Download-panel hovering 199-204.5.

  Hard cut: the undo that removes the frame (125.6-141.5).
- **Narration order:** L6 "Drag" shows the move (41.6) first, then jumps back for L7 "corner handle"
  (resize 38.8), then skips ahead past the move to the selection for cropping (43.2).
  Continuity: during "Drag" the image is already enlarged.
- **Anchors:**
  - Uploads, Upload, image (file pick), Open, thumbnail, Drag, corner, select, Crop (2nd "crop" in L8),
    Adjust, Done;
  - Elements, find (Frames category), add (circle frame), image (drag into frame), image
    (double-click), reposition;
  - Cropping (second crop), enlarging (resize to 1080x1349), Edit, adjustment (Adjust tool),
    change (brightness);
  - Share, download, format (file-type list), and L19 "Your" for the final Download click. On
    "need" it would need 5x.
- **Unanchored:** wait for the thumbnail (8x), collapse panel (no ripple), Done after reposition,
  Done after the second crop.
- **Review fix:** the preview showed the file-type dropdown (JPG/PNG/PDF/SVG/MP4) only inside a
  cross-fade. Added it as action A29 on "format" and moved the Download click to "Your".
- No zooms (the recorder zooms). Ending: 1.5 s at 1x after Download, then a 2.6 s hold.
