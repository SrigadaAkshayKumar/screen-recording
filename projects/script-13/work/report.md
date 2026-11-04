# script-13 report (AI Voice Changer in Canva)

## Result
- `projects/script-13/output/final.mp4`: 102.264 s, 2560x1440 (1920x1080 recording), voiceover audio. **verify PASS** (duration, streams, resolution, frozen spans, black frames at joins).
- No pace warning from `check.py --plan`. Speeds 0.76-1.67x (1.67x only on one 1.5 s cursor-approach / panel-open piece in L4). No holds, no zooms, no ripples (the recorder already bakes zooms into the take).
- Final freezedetect (n=0.003, d=1.5): longest cursor-only stretch 2.03 s (the opening), others 1.7-1.9 s. Nothing over 2.5 s.

## Stages
- probe, transcribe, align (18 lines, all `ok`), scenes, frames: **reused** (not re-run).
- analyze/sync: no `actions.json`/`sync.json`. The take has baked recorder zoom and a script that is not step-for-step, so, as in earlier script-13 runs, I wrote a hand plan, `work/hand_plan.py` (18 per-line groups, start on each line's start). It was built from freezedetect (n=0.003, d=0.8) on the source, scenes `stills` and 1 s / 0.5 s frame sheets. `plan.json` passes `check.py --plan`.
- preview: rendered 4 times (about 43 s each); fixes below. final: rendered once (5.6 min).

## Judgment calls
- Audio order is followed. The take is mostly in script order, but it has no footage for several lines (see table, "partly"), so nearby footage is borrowed and marked.
- Source 7-12 s (an earlier panel flash before the Apps search) is used only for the intro (L1) and is the one odd-looking spot.
- First preview had a 2.6 s static stretch (voice panel, src 55-58) in L7 and a 3.6 s toast freeze (src 187-191) in L16. Fixes: L7 got more moving footage (upload dialog, uploaded state, voice list zoom) plus one 1.5 s static piece; L16 uses the "Generating…" panel instead of the toast.
- L14 "mute" originally landed 1.3 s late; the piece was re-cut so the "Mute all" click lands on "mute" (72.9 s).
- Waits cut/skipped: 89-108 s and 123-177 s are the "Generating…" progress bar (static); skipped with cross-fades, not slowed down. Download wait 273-295 s skipped.
- 108-123 s is the user opening the original voice file/player while waiting; reused for L9 (listening) and L11 (keep the original).

## Per-line table (frames taken from final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 intro | 0.00-6.36 | 5.0-6.8, 6.8-11.0 | Canva editor with the video design, then Apps/AI Voice Changer panel opening | partly (generic intro) |
| 2 prepare recording / save a copy | 6.36-10.46 | 15.0-18.2 | Windows file explorer opening on the folder with the voice file | partly |
| 3 little background noise | 10.46-14.82 | 24.0-28.6 | Media player playing the voice recording (seek bar moving) | yes |
| 4 open design, select Apps, search AI Voice Changer | 14.82-20.36 | 33.4-35.8, 35.8-38.3, 38.3-41.0 | cursor to Apps (click on "Apps" at 16.96), search box, typing "ai voice changer" on "AI Voice Changer" | yes |
| 5 open the app listing, review | 20.36-26.64 | 48.7-53.8 | results grid, click AI Voice Changer, panel with voice/requirements text scrolling | yes |
| 6 upload your audio file | 26.64-28.60 | 63.2-64.9 | cursor to "Choose file" in the app, click | yes |
| 7 supported formats / check the app | 28.60-41.46 | 64.9-69.0, 69.0-71.6, 77.1-79.6, 53.8-55.3, 55.3-56.8 | file dialog, voice file chosen and opened, uploaded file in panel, voice-styles list, panel text (format note), idle panel | partly (formats text is small; no zoom) |
| 8 choose voice / generate a test | 41.46-44.76 | 86.0-89.2 | cursor to Generate, click on "generate" (42.9), "Generating…" appears | yes (voice choice shown earlier at L10) |
| 9 listen for words, pauses, distortion | 44.76-50.34 | 114.6-117.4, 118.3-119.7, 121.3-122.4 | media player playing the audio, then back to Canva generating panel | partly (take never plays the generated result; this is the original voice player) |
| 10 less dramatic voice / controls | 50.34-55.68 | 79.6-84.6 | voice-styles list zoomed, cursor on Male voice 2, preview playing | partly |
| 11 keep original to compare | 55.68-60.68 | 108.7-112.6 | explorer with the original `voice` file, opening it | yes |
| 12 add to design | 60.68-64.02 | 181.9-185.2 | "Add to design" click, audio track appears under the video | yes |
| 13 align, trim, volume | 64.02-69.74 | 204.8-207.0, 210.5-213.6 | playhead on the timeline with audio track, dragging the clip end to trim | partly (volume shown in L14) |
| 14 mute original audio | 69.74-77.92 | 222.8-225.8, 225.8-228.4, 232.9-234.4 | video clip selected, Audio tools, volume slider, "Mute all" on "mute", cursor to Apps | yes |
| 15 distinction / text to speech | 77.92-83.06 | 234.4-236.0, 239.67-243.8 | Apps search results, then "AI Voice by Audiox: Generate AI text-to-speech voiceovers" listing | yes |
| 16 changer processes audio vs AI Voice generates from text | 83.06-89.94 | 86.8-89.6, 122.4-123.4, 252.5-255.9 | Generate click + "Generating…" (processing supplied audio), then text-to-speech app with text input | partly |
| 17 preview the scene | 89.94-94.98 | 194.3-198.6 | click play in editor, preview playing | yes (last 1.7 s the screen changes only slightly) |
| 18 download MP4, play exported file | 94.98-102.26 | 266.2-269.6, 297.6-300.8, 306.8-309.9 | Share > Download > MP4 file type, Chrome downloads list, exported video playing in Media Player | yes |

## Uncertain
- No click log, so "lands on the word" was checked by eye on frames (±0.5 s), not to the frame.
- L9/L10/L16 borrow footage (see table).

## Check these
- 0-2 s: static Canva opening (2.0 s, cursor only).
- 6.4-10 s (L2): explorer opening animation; 12.5-14 s: audio player seek.
- 39.9-41.5 s and 50.6-55.6 s: cursor-only stretches of 1.7-1.9 s on the voice panel.
- 92-95 s: preview playing, small motion only.

## Lessons added
- Yes, one entry in docs/lessons.md (script-13, 2026-11-04).
