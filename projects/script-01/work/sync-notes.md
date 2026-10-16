# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 1 | timeline. | 5.480 | A1 video thumbnail in Uploads | 6.400 | 1.17x |
| 3 | once | 11.240 | A2 Play button | 21.300 | 1.09x |
| 4 | Open | 15.980 | A3 Elements tab (side rail) | 25.000 | 0.78x |
| 4 | selected | 24.060 | A4 Record voiceover | 33.900 | 1.10x |
| 5 | start | 29.300 | A6 Record button | 38.500 | 0.88x |
| 7 | keep | 38.600 | A7 Finish button | 70.200 | 1.40x |
| 8 | Listen | 40.120 | A8 Play button | 90.800 | 1.32x |
| 9 | trim | 44.660 | A9 end of the audio clip | 98.300 | 1.65x |
| 11 | record | 50.600 | A10 Home - Canva browser tab | 119.400 | 1.13x |
| 11 | create | 53.160 | A11 Video design type | 121.400 | 0.78x |
| 11 | design | 54.820 | A12 Instagram Reel blank design | 123.600 | 1.33x |
| 12 | Open | 57.520 | A13 Add audio | 134.800 | 1.44x |
| 12 | narration, | 59.140 | A14 Record voiceover | 140.600 | 1.23x |
| 12 | original | 61.980 | A16 original design browser tab | 169.700 | 1.30x |
| 13 | choose | 68.020 | A17 Audio tools | 174.300 | 0.76x |
| 13 | audio. | 70.300 | A18 Extract button | 182.200 | 0.92x |
| 15 | Preview | 76.980 | A19 Play button | 196.200 | 1.23x |
| 15 | download | 78.940 | A20 Share button | 201.300 | 1.22x |
| 15 | design | 79.740 | A21 Download in Share panel | 202.400 | 1.37x |
| 15 | video. | 80.960 | A22 Download button | 207.200 | 1.31x |

## Builder decisions

- A1->A2: cut src 11.70-20.30 - too long to fast-forward at <= 2.00x (cursor hesitates over timeline before pressing Play)
- A6->A7: cut src 46.50-60.50 - too long to fast-forward at <= 2.00x (narrator recording in progress, preview only loops)
- A7->A8: cut src 71.20-89.80 - too long to fast-forward at <= 2.00x (idle timeline after Finish, before listening)
- A12->A13: cut src 127.00-134.30 - too long to fast-forward at <= 2.00x (templates panel loading and idle cursor)
- A13->A14: cut src 136.00-139.80 - too long to fast-forward at <= 2.00x (menu open, cursor hovering)
- A14->A16: cut src 142.00-158.60 - too long to fast-forward at <= 2.00x (recording bar idle)
- A14->A16: cut src 160.00-168.80 - too long to fast-forward at <= 2.00x (menu hovering, idle)
- A17->A18: cut src 175.40-181.20 - too long to fast-forward at <= 2.00x (Extract audio panel open, cursor idle)
- A19->A20: cut src 197.60-200.30 - too long to fast-forward at <= 2.00x (preview playing, nothing to teach)
- A21->A22: cut src 203.20-206.40 - too long to fast-forward at <= 2.00x (cursor travels across a static Download panel)

## Judgment calls

- Recorder baked-in zoom on the footage: no zooms, no ripples (all actions in no_ripple).
- Anchors: A1 "timeline" (video placed), A2 "once" (Play lands ~0.7 s after "Play": anchoring on "Play" would need
  <0.75x or a held frame), A3 "Open", A4 "selected" (Record voiceover click is 8 s of footage after the Audio panel
  opens; the panel hover plays under "select record voiceover ... check the microphone", the mic prompt appears on
  "check the correct microphone"), A6 "start", A7 "keep" (Finish), A8 "Listen", A9 "trim", A10-A12 on line 11,
  A13/A14/A16 on line 12, A17 "choose", A18 second "audio", A19-A22 on line 15.
- A5 (Allow this time) and A15 (close recording bar) are not anchored: no room between their neighbours.
- Cuts (cross-faded; none fit fast-forward at <= 2x): 11.7-20.3 (hesitation before Play), 46.5-60.5 and 64.5-69.2
  (narrator's recording running / paused), 71.2-89.8 (idle before listening), 104.2-118.6 (idle, then new design),
  127-134.3, 136-139.8, 142-158.6, 160-168.8 (loading / idle menu / idle recording bar), 175.4-181.2 (panel idle),
  189.5-195.3 (idle), 197.6-200.3 (preview), 203.2-206.4 (cursor crossing a static panel). 13 cuts in 82 s, because
  the recording is 211 s for an 82 s voiceover.
- Not shown: "delete the camera video" (no deletion visible in the recording; plays under the sentence), "record
  yourself", "copy the audio track into your original design" (only the tab switch is recorded).
- A18's result (track separated, 184 s) lands 1 s after line 13 ends: that is the extraction wait, played at 1.2x.
