# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 6 | custom | 25.540 | A1 Custom size in the Create a design menu | 56.600 | 0.90x |
| 7 | millimetres. | 28.240 | A3 mm option | 65.400 | 1.11x |
| 8 | create | 30.900 | A6 Create new design button | 81.900 | 1.94x |
| 9 | uploads | 33.040 | A7 Uploads tab | 91.400 | 1.50x |
| 11 | enlarge | 44.120 | A9 photo corner handle | 103.000 | 0.76x |
| 12 | click | 46.660 | A10 photo (double click) | 113.700 | 1.57x |
| 13 | centred | 49.260 | A11 photo crop frame | 116.800 | 1.19x |
| 15 | original | 61.020 | A13 Original aspect ratio | 137.100 | 1.40x |
| 15 | instead. | 62.320 | A14 Done button | 138.100 | 0.77x |
| 18 | replacement | 78.120 | A15 Share button | 159.900 | 1.13x |
| 18 | retouching. | 78.980 | A16 Download in share panel | 161.300 | 1.63x |
| 19 | marks | 82.760 | A18 PDF option | 167.300 | 0.85x |
| 20 | Print | 84.340 | A20 Print preset | 169.100 | 1.14x |
| 22 | digital | 93.260 | A21 Digital preset | 186.000 | 1.13x |

## Judgment calls
- Narration order = recording order for the whole flow, so no out-of-order anchors.
- Anchors: Custom size@"custom", mm@"millimetres", Create new design@"create", Uploads@"uploads", enlarge drag@"enlarge", double click@"click", crop drag@"centred", Original aspect@"original", Done@"instead", Share@"replacement", Download@"retouching", PDF@"marks", Print preset@"Print", Digital@"digital".
- Unanchored (narration too fast or no matching words): A2 units dropdown, A4/A5 width/height fields (typing plays inside), A8 add photo (anchoring it created a 2 s hold), A12 Done after first crop, A17 file-type dropdown, A19 Advanced settings.
- Intro (0-24 s, no on-screen steps narrated) uses the earlier design in the recording (src 10.6-45.4) plus the homepage approach (52.7+), at ~0.9x. Idle stretches there are cut, not held.
- Cuts (all cross-faded): idle/loading spans listed in sync.json; every still longer than ~1.5 s was cut down because fast-forwarding it left >2.5 s of unmoving screen or >2x speed.
- The recording already contains baked-in camera zoom/pan, so no zooms and no ripples were added (cursor coordinates are only approximate).
- The unnarrated photo resize (src 138-159) is kept to cover the "Here's the part many tutorials skip" talk at ~1.1x; Download panel idle (174-181) cut.
- A6's result (new blank design) is partly cut (loading); the cut jumps from Create click to the loaded design.
- No pace warnings remain; remaining warnings are only "not tied to a word" for the unanchored actions above.
