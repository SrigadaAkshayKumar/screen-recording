# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | select | 5.920 | A2 photo (hummingbird) | 21.500 | 1.01x |
| 3 | photo | 9.960 | A3 photo, not the page background | 28.200 | 1.66x |
| 4 | Animate | 12.800 | A4 Animate button in toolbar | 36.400 | 2.89x |
| 5 | Remove | 17.500 | A5 Remove animation button | 52.600 | 3.45x |
| 7 | Play | 23.100 | A6 Play button | 64.500 | 2.12x |
| 8 | empty | 27.720 | A7 empty area of the page | 88.000 | 1.96x |
| 9 | Animate | 29.720 | A9 Animate button in toolbar | 142.350 | 2.17x |
| 10 | Remove | 33.100 | A10 Remove animation button | 144.900 | 0.75x |
| 14 | motion | 52.120 | A8 Effects tab on text | 121.700 | 1.17x |
| 19 | Preview | 72.200 | A11 Play button | 172.450 | 0.88x |

## Builder decisions

- A4->A5: fast-forwarded src 38.00-51.50 instead of cutting it (junk: cursor browsing the Animate panel)
- A6->A7: cut src 66.00-80.43 - too long to fast-forward at <= 2.00x (junk: preview playing / timeline scrubbing / idle)
- A9: after A7 (until src 90.00) jumps ahead to src 139.50 - narration order
- A7->A9: cut src 89.50-120.00 - too long to fast-forward at <= 2.00x (junk: repeated preview plays and idle)
- A8: after A10 (until src 166.00) jumps back to src 120.50 - narration order
- A10->A8: fast-forwarded src 149.00-165.00 instead of cutting it (junk: hovering over the photo, idle)
- A11: after A8 (until src 135.00) jumps ahead to src 168.00 - narration order

## Judgment calls
- Recorder auto-zoom is baked in: no plan zooms; ripples only on A2 and A11 (unzoomed clicks). All other clicks `no_ripple`.
- A1 (home -> design reopen, 15.5-20 s) is not anchored: it plays under "Open your design" (src_start 15.5; 0-15.4 idle cut).
- Anchors: A2 "select", A3 "photo", A4 "Animate", A5 "Remove", A6 "Play", A7 "empty" (page click), A9 "Animate" again, A10 "Remove", A8 (Effects tab) on "motion" in L14, A11 "Preview" in L19.
- Order conflict: A9/A10 (src 142-145) are narrated before A8 (src 121.7); cross-faded jump back to 120.5, then forward to 168 for A11.
- Cuts (too long to fast-forward): src 37-51.5 (Animate panel browsing), 66-80.4 (preview/idle), 89.5-120 (repeated previews). Fast-forwarded: 149-165 (hover idle), tail 172-188 (scrubbing).
- Narrated but missing in footage: page-tab Animate/Remove (L9-10: A9/A10 re-use the object's panel), transition settings (L11-12), Delete Path (L13; the Create-an-Animation panel at 143-148 plays over it), text-tab Animate/Remove (84-88 s) not shown (no room under L5 order). Lines L15-18 play over the Effects panel / hover footage.
- A1 position, A7 position, A10 time are low confidence.
