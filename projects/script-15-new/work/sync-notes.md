# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | select | 7.840 | A1 Canvas page (deselects clip) | 8.500 | 1.08x |
| 3 | playhead | 10.100 | A2 Playhead on the timeline (audio clip) | 19.000 | 1.02x |
| 4 | split | 16.800 | A3 Split in the audio context menu | 43.550 | 1.02x |
| 4 | split | 18.860 | A8 Split button in the floating toolbar (second split) | 143.850 | 0.92x |
| 5 | divided | 23.240 | A4 Timeline: two sections at the playhead (view only) | 45.500 | 0.92x |
| 6 | playhead | 27.740 | A6 Playhead to the end of the pause | 134.000 | 0.96x |
| 6 | split | 29.440 | A7 Split button in the floating toolbar | 136.200 | 1.29x |
| 7 | Select | 30.820 | A9 Short section between the cuts | 148.100 | 1.45x |
| 7 | delete | 33.320 | A10 Delete (trash) button | 151.000 | 1.16x |
| 8 | into | 35.360 | A11 Remaining section | 155.400 | 1.27x |
| 9 | listen | 41.040 | A5 Play button | 102.400 | 0.88x |
| 10 | place | 45.560 | A12 Uploaded video in Uploads panel | 160.900 | 1.19x |
| 12 | captions, | 56.440 | A13 Captions button in toolbar | 177.000 | 1.02x |
| 13 | select | 63.440 | A14 Uploaded video clip in the timeline | 193.200 | 0.94x |
| 13 | audio | 64.720 | A15 Audio tools menu | 194.800 | 1.25x |
| 13 | extract | 66.100 | A16 Extract button | 196.800 | 1.45x |
| 14 | export | 72.320 | A17 Share button | 224.600 | 1.17x |
| 14 | video. | 74.400 | A18 Download in share panel | 227.400 | 1.35x |

## Builder decisions

- A2: after A1 (until src 9.60) jumps ahead to src 17.80 - narration order
- A3: after A2 (until src 24.20) jumps ahead to src 41.90 - narration order
- A8: after A3 (until src 44.60) jumps ahead to src 143.00 - narration order
- A4: after A8 (until src 146.20) jumps back to src 43.80 - narration order
- A6: after A4 (until src 46.80) jumps ahead to src 131.00 - narration order
- A9: after A7 (until src 137.40) jumps ahead to src 147.30 - narration order
- A11: after A10 (until src 152.80) jumps ahead to src 154.60 - narration order
- A5: after A11 (until src 158.30) jumps back to src 100.30 - narration order
- A12: after A5 (until src 105.90) jumps ahead to src 159.00 - narration order
- A13: after A12 (until src 170.00) jumps ahead to src 175.00 - narration order
- A14: after A13 (until src 182.00) jumps ahead to src 191.60 - narration order
- A17: after A16 (until src 201.50) jumps ahead to src 222.00 - narration order

## Judgment calls
- Follow the audio: each line gets footage of its step; 12 cross-faded jumps (reorders) because the recording does the steps in another order/take (split via menu at 43 s, toolbar split at 136/144 s, delete at 151 s, move at 155 s).
- L1/L2 play the opening 0-9.6 s; the frozen page 9.8-16.3 s is skipped; L3 playhead = 19 s.
- L4 shows the context menu (43 s) and then the toolbar Split (143.9 s) for "or Split".
- L5 reuses 43.8-46.8 s (two sections); L9 "listen" uses the playback at 102 s; L10/L11 use the uploaded video on the timeline (160-170 s); L12 captions 177 s; L13 select video / Audio tools / Extract at 193-197 s; L14 preview + share + download at 222-227 s.
- No zooms, no ripples (baked-in recorder zoom, see lessons). No cuts or ff spans: nothing needed fast-forward; all speeds 0.88-1.45x.
- Pace: the one 'screen does not move' warning (59-61 s, panel idle after captions open) was fixed by moving prev_until/src_from.
- Remaining warnings (not fixable): A11 drag result lands 1.2 s after line 8 ends (the drag itself takes 2 s in the footage); A18 download panel appears 0.3 s after the last word.
