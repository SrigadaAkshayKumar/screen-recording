# Sync notes (hand plan: work/hand_plan.py, no sync.json/anchors)
Per-line map (line -> source range -> what is seen):
1 intro -> 127.9-135.1 path settings, Done, text added | 2 -> 9.6-14.7 Canva home, create dialog | 3 -> 25.5-31.8 elements panel
4 -> 32.8-38.5 recent graphics/background | 5 -> 38.5-44.8 background placed (no visible "lock" click) | 6 -> 110.9-114.7 character selected, Animate
7 -> 114.7-118.5 Create an animation, route drawing | 8 -> 118.5-122.4 route toward house | 9 -> 122.4-124.0 + 126.8-131.0 settings, Done
10 -> 116.5-121.0 (replay of route drawing, no footage for the advice) | 11 -> 148.5-158 text box/animation + 172.9-176.1 timeline bar
12 -> 196.8-201.1 + 205.4-207.8 plus button / add page menu | 13 -> 177.3-189.9 timeline edits (no real "reuse" footage)
14 -> 98.0-100.6 character search (transition line) | 15 -> 100.6-106.0 character placed | 16 -> 106.4-110.5 + 127.9-131.9 character + path settings
17 -> 216.1-225.9 share, download, MP4 (the "preview the complete sequence" part is not shown: playback is flagged static).
## Judgment calls
- Recording order differs from narration (animate steps come before text; scene add shown from later footage) - follow audio.
- Every group starts on its line start, 0.82-1.32x, no holds, no pace warnings.
- Two plan zooms (2.0x on the canvas at out 32.6 and 47.4) because the route drawing is small-area motion that freezedetect and the eye read as static.
- Remaining freezedetect(n=0.003,d=1.5) blips on the preview: 33.5 (1.7s), 35.2 (2.3s), 37.5, 39.7, 48.6 (<=1.7s) during route drawing; final verify PASS (3 s limit).
