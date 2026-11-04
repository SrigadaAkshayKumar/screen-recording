# script-15 report

## Result
`projects/script-15/output/final.mp4` — 87.667 s (voiceover 87.677 s), 3420x1922 (delivered 1440p), **verify PASS**.
`check.py --plan` clean (no `pace:` warnings). Group speeds 0.76–1.21x. freezedetect on the final (d=1.5): only the opening
(0–2.37 s, static Canva home, cursor only) and 41.7–43.5 s (1.77 s, preview-time loading of the duration box). No zooms/ripples (recorder zoom is baked into the take).

## Stages
- probe, transcribe, align (all 19 lines ok), scenes, frames: **reused** (work files were current; 160.0 s recording, 87.677 s voiceover).
- analyze/sync: done by hand as `work/hand_plan.py` (the committed one was for a different, 345 s take and was discarded). It writes plan.json and a stub actions.json (`actions: []`; `check.py --actions` therefore reports "needs a non-empty actions list" — expected for a hand plan, no clicks/zooms to sync).
- preview: rendered, reviewed at line starts/middles; one fix (L4 piece start 22.9 -> 22.4 so it opens on the cursor reaching the clip, not on a blurred frame). final render ~7.7 min; verify PASS.

## Judgment calls
- Follow the audio order; one group per line starting on its lines.json start; no holds, no cuts except loading screens skipped (dark loading 8.3–10.4, blank editor idle 11.5–12.8) with cross-fades. 8 jumps are cross-faded.
- The recording does not contain every narrated step (no multi-scene selection, no separate title-strip drag before the heading). Closest footage was used and marked "partly" below.
- Opening: 2.3 s of the static home screen at 1x (cap), then moving footage.
- Footage reused for L7 (46–50 and 98–100) and L12/L10 from the trim/duration toolbar (the duration control lives in the Trim panel in this take).

## Per-line table (verified on final.mp4 frames at each line's start/middle)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 intro | 0–5.88 | 1.1–6.4 | Canva home, then Create-a-design dialog | yes |
| 2 open Video design | 5.88–9.4 | 6.4–8.3, 10.4–11.6 | Videos chosen, blank video design opens | yes |
| 3 Page Mode / timeline | 9.4–15.0 | 12.8–17.8 | editor loads, timeline appears at bottom | partly (no pencil/Page Mode in take) |
| 4 select clip | 15.0–17.76 | 22.4–25.4 | clip clicked in Uploads, selected in timeline | yes |
| 5 zoom timeline | 17.76–21.76 | 25.9–30.4 | zoom slider, timeline zoomed in | yes |
| 6 drag right edge left | 21.76–24.7 | 43.0–46.2 | ↔ handle on clip's right edge, clip shortens | yes |
| 7 drag edge outward | 24.7–31.44 | 46.2–50.0, 98.0–100.0 | clip extended again; edge drag | yes |
| 8 left edge | 31.44–34.96 | 83.8–87.0 | ↔ handle on the left edge of the clip | partly |
| 9 preview | 34.96–39.22 | 100.2–104.2 | playhead playing the preview | yes |
| 10 clock control | 39.22–45.54 | 87.8–92.6 | clip selected, floating toolbar time control hovered/clicked | yes |
| 11 enter duration | 45.54–47.62 | 76.9–78.9 | toolbar time item, Trim panel with duration field | partly |
| 12 several scenes, same duration | 47.62–52.04 | 80.1–83.6 | Trim panel scrubbing, preview starts (single clip only) | partly |
| 13 title strip, extend edge | 52.04–58.64 | 128.8–133.6, 134.2–135.4 | cyan "Heading of video" strip selected, edge dragged | yes |
| 14 title separate timing | 58.64–62.22 | 135.4–138.4 | title strip above clip bar | yes |
| 15 timeline zoom | 62.22–67.34 | 55.0–59.5 | zoom slider changes timeline scale | yes |
| 16 not longer/shorter | 67.34–70.76 | 60.0–62.7 | zoomed timeline, same clip length (1:18) | yes |
| 17 moving vs trimming | 70.76–76.42 | 65.8–70.8 | clip bar with cursor at its edge | partly |
| 18 check final scene | 76.42–80.8 | 144.0–148.0 | finished design with title, ↔ on timeline, playing | yes |
| 19 preview, then download | 80.8–87.68 | 148.0–153.5, 156.0–158.8 | Share panel, Download file type MP4, download toast | yes |

## Uncertain
- L3, L8, L11, L12, L17 are approximate matches (see table): the take lacks those exact gestures.
- No clicks log: nothing is pinned to words to the frame; the visible edits land within the narrated line, not on a specific word.

## Check these
- 0–2.4 s static opening; 41.7–43.5 s (loading of the clip in the trim panel).
- 15.4 s and 18 s (recorder-zoom blur at piece starts), 76–77 s (L18 start).

## Lessons added
- 2026-11-04 script-15 entry in docs/lessons.md.
