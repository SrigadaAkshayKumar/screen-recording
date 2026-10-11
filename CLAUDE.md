# screencast-editor

Turns a **silent screen recording** + a **separate voiceover** + its **script** into a finished
tutorial video: screen actions retimed so each click lands on the word that describes it, with a
smooth zoom and a ripple on clicks. Mechanical steps are deterministic Python CLIs in `tools/`;
judgment steps are Claude Code skills in `.claude/skills/`. Every stage writes a JSON file in
`projects/<name>/work/`, so any stage can be re-run or hand-corrected without redoing the rest.

**Read `docs/lessons.md` before every run.** Any mistake that cost a render gets added there.

## Stage order

| # | stage | kind | writes |
|---|---|---|---|
| 0 | `tools/new_project.py <name> --video --audio [--script] [--clicks]` | tool | `input/` |
| 1 | `tools/probe.py` | tool | `work/probe.json` |
| 2 | `tools/transcribe.py` | tool | `work/words.json`, `work/transcript.txt` |
| 3 | `tools/align_script.py` (no script.md -> the transcript becomes it) | tool | `work/lines.json` |
| 4 | `tools/scenes.py` | tool | `work/scenes.json` (+ `work/clicks_rec.json`) |
| 5 | `tools/frames.py --sheets --event-sheets` | tool | `work/frames/*.jpg` |
| 6 | **screencast-analyze** | skill | `work/actions.json`, `work/analyze-notes.md` |
| 7 | **screencast-sync** -> `tools/plan_builder.py` | skill + tool | `work/sync.json`, `work/plan.json`, `work/sync-notes.md` |
| 8 | `tools/render.py --preview` + review | tool + judgment | `output/preview.mp4`, `work/render.json` |
| 9 | `tools/render.py` | tool | `output/final.mp4` |
| 10 | `tools/verify.py` | tool (gate) | `work/verify.json`, `output/checks/` |
| 11 | report | skill | `output/report.md` |

**screencast-edit** orchestrates all of it, never asks questions mid-run, and records every
judgment call in `output/report.md`. Gates: alignment ≥ 30 % (align_script), `check.py --actions`,
`check.py --plan` (render refuses an invalid plan), preview review, `verify.py`.

Optional: `tools/click_logger.py` runs *while recording* and logs every click; with
`input/clicks.json` present, click times/positions come from the log (after scenes.py converts
them to recording time and pixels), not from frame guessing.

Helper modules: `tools/common.py` (paths, JSON, ffmpeg frame reader), `tools/check.py` (segment
mapping + validators, also a CLI).

## Conventions

- Python CLIs use argparse and take `--project projects/<name>`; they exit non-zero with a clear
  `error:` message on bad input. Run them from the repo root.
- **Times**: seconds as floats, 3 decimals (`common.write_json` rounds every float).
  Source/recording times are `t`, `src_*`; output-video times are `out_*`.
- **Coordinates**: always recording pixels (x right, y down from the top-left), even when an image
  was sampled from the 540p preview — tools convert.
- **Frame convention**: frame i of the recording is shown at time i/fps, timestamps start at 0 at
  the first frame, VFR input is resampled to `probe.recording.fps`. `FrameReader`, `grab_frame`,
  scenes.py and render.py all follow it — keep it that way.
- Inputs keep a fixed stem and their original extension (`recording.mov` is fine) so nothing is
  re-encoded; `Project.recording` finds them.
- Images for Claude are ≤ 1600 px wide (except `--crop`, which is native resolution).
- JSON is written atomically; a hand-edited file is picked up by the next stage. plan.json carries
  a `generated_hash`: plan_builder refuses to overwrite hand edits without `--force`.
- No media in git (`.gitignore` covers inputs, frames, outputs, *.mp4/*.mp3/*.wav).

## plan.json (render input)

```json
{
  "output": {"duration": 73.8, "fps": 30, "width": 1920, "height": 1080},
  "segments": [
    {"src_start": 4.2, "src_end": 9.0, "out_start": 7.1, "out_end": 8.6, "mode": "speed"},
    {"src_start": 9.0, "src_end": 9.0, "out_start": 8.6, "out_end": 9.4, "mode": "hold"},
    {"src_start": 15.5, "src_end": 16.7, "out_start": 9.4, "out_end": 10.6, "mode": "speed", "xfade": true}
  ],
  "zooms": [{"out_t": 8.6, "x": 44, "y": 418, "scale": 1.8, "in": 0.45, "hold": 0.8, "out": 0.5}],
  "ripples": [{"out_t": 8.6, "x": 44, "y": 418}],
  "intro": null, "outro": null,
  "sync": [{"action": "A1", "line": 2, "word": "Open", "word_t": 8.6}],
  "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": false}
}
```

- `speed` maps output time linearly onto `src_start..src_end`; `hold` shows `src_start` frozen.
  `xfade: true` cross-fades 6 frames from the previous segment's last frame (use on cut joins).
  `wait: true` allows up to 8x instead of 4x. Segments follow the narration order, so the source
  may jump back (always with `xfade`) when the recording did a step later than it is narrated.
- A zoom reaches full scale at `out_t` (the click), starts at `out_t - in`, holds `hold`, then
  zooms out over `out`. Overlapping zooms blend into one move.
- `intro`/`outro` are descriptive; the segments do the work (e.g. a leading hold).
- `sync` ties actions to words; check.py verifies each click lands within ±0.15 s of `word_t`.
- `duration` must equal the voiceover duration (±0.1 s); width/height must equal the recording.

## Testing a change

There is no unit-test suite. Exercise the tools on a project (a synthetic one is fine: render a
fake UI with OpenCV, make a voiceover with any TTS) and run `check.py`, `render.py --preview`,
and `verify.py`. Look at the frames, not just the exit codes.
