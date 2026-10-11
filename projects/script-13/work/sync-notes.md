# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Upload | 9.740 | A1 Upload item in the Create menu | 22.300 | 1.29x |
| 2 | homepage, | 10.920 | A3 Open button in the file picker | 26.750 | 3.77x |
| 2 | imported | 12.320 | A5 Open button in the upload toast | 31.950 | 3.71x |
| 3 | text | 14.580 | A6 text box of the resume | 94.900 | 1.57x |
| 3 | menu. | 15.960 | A7 font name box (Carlito) | 98.700 | 2.75x |
| 4 | apply | 18.340 | A8 Change all button | 105.700 | 2.94x |
| 5 | brand | 27.620 | A9 Edit link under Brand Kit | 130.500 | 1.19x |
| 6 | category, | 30.640 | A10 font dropdown of the Title style | 133.900 | 1.13x |
| 7 | finish. | 35.000 | A11 Save button | 138.450 | 1.04x |
| 8 | select | 37.160 | A12 font name box in the editor | 144.900 | 2.99x |
| 8 | Uploaded | 39.680 | A13 Canva Sans under Brand Kit | 147.900 | 1.19x |
| 9 | weights. | 42.940 | A14 close X of the Font panel | 149.700 | 1.00x +1.5s hold |
| 13 | appearance | 55.880 | A15 Share button | 168.950 | 1.49x |
| 13 | editable | 57.000 | A16 Download icon in the Share panel | 170.900 | 1.74x |
| 13 | render | 58.420 | A17 file type dropdown | 171.800 | 1.00x +0.5s hold |
| 13 | PNG | 60.920 | A18 PNG option | 181.000 | 3.68x |
| 13 | using | 62.200 | A19 Download button | 184.700 | 2.89x |
| 14 | pages | 64.960 | A20 Add page button | 192.500 | 2.83x |
| 15 | Upload | 66.980 | A21 Uploads tab in the sidebar | 194.200 | 0.84x |
| 15 | PNGs | 67.420 | A22 Upload files button | 195.300 | 2.50x |
| 15 | image | 69.080 | A24 uploaded PDF-page image thumbnail | 200.300 | 3.01x |
| 15 | each | 70.500 | A25 corner handle of the image | 205.300 | 3.52x |
| 18 | Download | 79.300 | A26 Share button | 227.500 | 2.52x |
| 18 | compare | 81.140 | A27 Download button (PDF) | 233.500 | 3.26x |

## Builder decisions

- A6: after A5 (until src 34.60) jumps ahead to src 94.00 - narration order
- A8->A9: cut src 116.00-129.80 - too long to fast-forward at <= 2.00x (junk: font panel reopened, wandering through Brand Kit list)
- A25->A26: fast-forwarded src 211.30-226.40 instead of cutting it (junk: idle on the finished page)

## Judgment calls
- Audio order followed. Only one backward/forward jump: A5 (design opens, 34.5) -> A6 (select text, src 94.0); the 35.6-93.6 hovering/scrolling is unused (cannot fit in 2 s of narration).
- Zooms: none. The recording has baked-in recorder zoom/pan; ripples only.
- Anchors: A1 "Upload", A3 "homepage", A5 "imported" (the 4.1 s upload wait runs fast-forwarded in between), A6 "text", A7 "menu", A8 "apply", A9 "brand" (Edit under Brand Kit), A10 "category", A11 "finish" (Save of the brand fonts, no font file upload exists in the recording), A12/A13 "select"/"Uploaded", A14 "weights", A15-A19 on L13 (Share > Download > PNG > Download, narrated as "PDF tool"), A20 "pages", A21/A22/A24/A25 on L15, A26 "Download" and A27 "compare" on L18.
- A2 (Upload files click) and A23 (Open in picker) have no word of their own: they play on the way between anchors; ripples still fire.
- Cuts: 8.5-18.2 pre-take (off-topic); 116.0-129.8 font-panel wandering (did not fit at 2x); 241-246 recording tail. 211.3-226.4 idle fast-forwarded instead of cut.
- L10-12 (opinion lines) play over the idle design (src ~150-168, includes a 10 s still).
- L17 "Add new Canva text above it" has no footage; plays over the fast-forwarded idle page.
- Warnings accepted: A5/A7/A14/A25 results land slightly after their line ends (0.3-2.8 s); A25's drag is narrated as "edge to edge" but finishes ~2.8 s late.
