# Sync notes
plan.json comes from `work/hand_plan.py` (hand budget per narration interval), not plan_builder; check.py --plan: OK, no pace warnings.

## Judgment calls
- Anchors: see work/sync.json. A1 lands on "moment" (not "playhead") so the approach plays at ~1x instead of 2.6x. A7 (add) on "design" so preview->add has 1.7 s.
- Cuts (cross-faded): 3.8-11.2 (idle), 15.7-19.3 and 20.2-28.7 (cursor idle at sidebar), 41.8-50.9 (search results loading), 60.3-65.7 (preview popover), 72-88.5 (idle with clip on timeline), 95.4-99, 103.5-116, 132.5-136.6, 138-147.4 etc. (repeat drags/idle), 175-203 (play spinner), 211.6-217.6 (download skeleton).
- Intro plays 0-3.8 at 0.75x (zoom-out + cursor), then cursor approach to the timeline.
- No zooms and no ripples anywhere: the recorder's zoom is baked in; ripples would land in the wrong place.
- L5 ("open apps / audio in elements") plays over the search-results loading/arrival: the recording never opens Apps.
- L7 ("open uploads") plays over the clip being added and moving to the timeline: no Uploads step recorded.
- L11-13 (align/lead-in) use clip-drag footage with tooltips (131-138, 147-158); L14 uses 140.5-143.4 (play click), L15 uses 203-207 (playback), L16 uses Share -> Download -> MP4 (208.5-221.2).
