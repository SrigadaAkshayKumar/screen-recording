# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads | 5.780 | A1 Uploads in the left sidebar | 4.600 | 0.80x |
| 3 | menu | 8.260 | A2 menu (...) beside Upload files | 7.400 | 1.13x |
| 3 | Folder. | 10.660 | A3 Upload folder button | 10.100 | 1.12x |
| 4 | folder | 13.160 | A5 voiceovers-2026-10-07T17-58-23 folder | 13.900 | 1.52x |
| 4 | confirm | 14.740 | A6 Upload button in the folder picker | 15.150 | 0.79x |
| 5 | confirm | 19.740 | A7 Upload in the browser permission prompt | 18.700 | 1.00x +1.4s hold |
| 7 | Check | 24.080 | A9 back arrow in Upload options | 31.700 | 3.00x |
| 8 | homepage | 27.860 | A10 Projects - Canva browser tab | 41.400 | 2.57x |
| 8 | Projects | 28.720 | A11 Your projects in the sidebar | 50.300 | 1.40x |
| 8 | folder. | 30.280 | A12 Uploads folder | 58.600 | 2.44x |
| 9 | it | 31.520 | A18 voiceovers-2026-10-07T17-58-23 folder | 122.200 | 1.77x |
| 14 | uploading | 48.460 | A14 File Explorer in the taskbar | 102.600 | 1.79x |
| 18 | individually | 68.200 | A20 voiceovers-2026-10-10T12-26-47 folder | 130.100 | 1.05x |

## Builder decisions

- A10->A11: cut src 41.90-49.60 - too long to fast-forward at <= 2.00x (junk: cursor idles on the homepage before Your projects)
- A11->A12: cut src 52.90-57.40 - too long to fast-forward at <= 2.00x (junk: idle on Your projects, cursor wanders to Date modified)
- A18: after A12 (until src 60.00) jumps ahead to src 121.40 - narration order
- A14: after A18 (until src 128.00) jumps back to src 78.00 - narration order
- A20: after A14 (until src 121.40) jumps ahead to src 128.20 - narration order

## Judgment calls

- **Fast-forward first.** All in-scene footage plays at 0.8-2.4x. The idle Upload options panel runs
  at 3.6x and still spans at 8x. Two idles are cut because the narration packs homepage -> Projects ->
  Uploads folder into 4 s while the recording takes 17 s, so they could not fit at ≤ 2x:
  - homepage idle, src 41.9-49.6;
  - Your projects idle, src 52.9-57.4.
- **Narration order (three jumps):**
  - L9 "Open it" -> jumps ahead from the Uploads folder (src 60.0) to the editor, where the uploaded
    folder is opened (122.2);
  - L10-L13 -> jumps back to the editor at src 78.0 (Folders tab -> Upload options, idle at 3.6x);
  - L14-L16 ZIP -> File Explorer (102.6-117) in recording order, then the Folders tab;
  - L18 "individually" -> jumps over the already shown first-folder opening (121.4 -> 128.2) to open
    the second folder (130.1).
- **Anchors:** "Uploads", "menu", "Folder", "folder" (2nd), "confirm" (picker Upload), "confirm"
  (browser prompt), "Check" (back to the Folders tab with the folder uploading), "homepage" (browser
  tab), "Projects", "folder" (Uploads folder), "it" (open the uploaded folder), "uploading" (File
  Explorer), "individually" (open the other folder).
- **Hold:** 1.4 s on the browser permission prompt (L5 "If your browser asks for permission").
- No zooms (the recorder zooms). A16 has no ripple.
