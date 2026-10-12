# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 4 | apps | 16.780 | A1 Apps in left sidebar | 15.100 | 0.90x |
| 5 | Face | 22.020 | A3 Face Blur in Video app | 29.600 | 1.05x |
| 8 | Upload | 33.460 | A4 Choose file button | 42.900 | 1.16x |
| 8 | control, | 35.440 | A5 Open button in file picker | 45.150 | 1.14x |
| 8 | strength. | 37.260 | A6 Intensity slider | 58.700 | 1.18x |
| 10 | Run | 42.240 | A7 Process your video button | 79.400 | 0.94x |

## Builder decisions

- A3: after A1 (until src 19.00) jumps ahead to src 28.00 - narration order
- A6: after A5 (until src 46.60) jumps ahead to src 58.00 - narration order
- A7: after A6 (until src 61.50) jumps ahead to src 77.50 - narration order

## Judgment calls
- Recording has baked-in recorder zoom: no zooms, no ripples (all clicks `no_ripple`).
- Anchors: A1 "apps", A3 "Face", A4 "Upload", A5 "control", A6 "strength", A7 "Run". A2 (typing BGblur) is unanchored: anchoring it at "search" left a 1.2 s hold in front of a 0.05 s piece, so its footage plays inside A1->A3 (src 15.1-19.0) at ~1x.
- Reorders (cross-faded): A3 jumps ahead to src 28.0; A6 to src 58.0; A7 to src 77.5 (the recording does slider/idle time that narration compresses).
- Line 9 (select a style): no click exists in the recording; plays over the slider/panel footage.
- Lines 11-19 (add to design, play clip, tracking, website, export) have NO footage: the recording ends with the face-detection progress still running. The tail is src 82.3-175.5 fast-forwarded at 1.96x (hand-edited into plan.json, since plan_builder only plays tails at 1x / holds; plan.json carries the hand edit, a re-run needs --force). Not cut and no hold >1.5 s, in line with the pace rule.
- Warnings left: "A6 result after line 8 ends" (slider response is seen at 60.1 src; harmless); "A2 not tied to a word" (explained above).
