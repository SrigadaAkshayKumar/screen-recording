# Analyze notes (script-17-new)

- No click log. Click times were read from single frames at 0.2-1 s steps (+-0.3 s). Pixel coordinates are rough
  (read off contact sheets, recording pixels) and only matter for ripples, which this plan does not use.
- **The recorder has baked-in auto-zoom** (zoomed views at ~9-13, 18-20, 29-32, 36-39, 46, 49-53, 74-75, 77-80, 91-98, ...).
  Per docs/lessons.md: no plan zooms and no ripples (a ripple in recording pixels would land away from the cursor).
- The recording holds ~4 takes of the same steps (186 s for a 74 s voiceover): mute the voiceover (13-22), play (32-49),
  restore volume (50-54), mute the video (75-80), music track volume (91-97), browser site-info sound popup (120-127),
  video volume again (106-115, 131-135), play (141-150), Share -> Download (160-182).
- Dead time not used: 0-6.3 (frozen opening, only cursor jitter), 23.1-28.6, 55.9-62.9, 67.9-73.6, 82-90.8, 102.5-105.5,
  117-119.7, 136.6-138.4, 154-156.8, 171.4-173.
- Low confidence: A10, A11, A13, A14 (time or position); A4 click time (cursor on Play at 32.0, playing at 33.0).
- Script says "mute control or set volume to zero": the recording drags the slider to 0 (A3); the mute icon highlights.
- The narration about the "browser tab speaker" is illustrated by the site-info Sound toggle (120-127); the recording does not show a tab speaker icon.
