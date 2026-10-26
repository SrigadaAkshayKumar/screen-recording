# Sync notes (script-06)
Hand plan from `work/hand_plan.py`: 20 per-line groups starting on each lines.json start, 0.77-1.14x, no holds, no zooms/ripples (baked recorder zoom).
## Judgment calls
- Pieces come from freezedetect (n=0.003 d=0.8) moving windows of the source, extended <=0.5 s into stills, streamed in source order (footage order roughly matches narration topics: new design, template search, table rows, colours).
- Opening: 1.5 s of the static finished planner then moving footage at 0.77x (the 0.77x is the lowest speed used).
- Narration-vs-footage mapping is by order/time share, not click sync; steps like "group checkbox and line" have no dedicated footage and play whatever the stream shows.
