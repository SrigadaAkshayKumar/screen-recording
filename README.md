# screencast-editor

Turn a **silent screen recording** plus a **voiceover** (and its script) into a finished tutorial
video: the screen actions are retimed so every click lands on the word that describes it, with a
smooth zoom and a click ripple. Runs locally on Windows or macOS.

## Setup

Needs Python 3.11+ and ffmpeg on your PATH.

```bash
# ffmpeg
winget install Gyan.FFmpeg        # Windows
brew install ffmpeg               # macOS

# Python deps
python -m venv .venv
.venv\Scripts\activate            # Windows   (macOS: source .venv/bin/activate)
pip install -r requirements.txt
```

The first transcription downloads the faster-whisper `small.en` model (~470 MB), and it's cached
after that.

## Recording tips

- Record the screen **without** audio. Record the voiceover separately and follow the script.
- Optional but recommended: run the click logger while you record, so click times and positions
  come from the log instead of being inferred from frames:
  ```bash
  python tools/click_logger.py --out clicks.json
  ```
  Start it at the same moment as the recorder, make your **first action a click on an empty
  area**, and stop it with Ctrl+C. It assumes you record the whole primary screen. If you record
  only a region, pass `--click-region x,y,w,h` to `scenes.py`. On macOS, give your terminal
  Accessibility and Input Monitoring permission.
- The script is optional: without one, the voiceover transcript is used. With one, put on-screen directions on their own lines in parentheses:
  `(On screen: the Upload dialog)`. These lines aren't spoken, and the analyze step uses them as hints.

## Running in the cloud

See [docs/cloud.md](docs/cloud.md): GitHub Actions edits every video in a Google Drive inbox folder and puts the results in an output folder.

## Usage with Claude Code (recommended)

```bash
python tools/new_project.py demo --video rec.mp4 --audio vo.mp3 [--script script.md] [--clicks clicks.json]
```

Then, in Claude Code from this folder:

```
/screencast-edit demo
```

Claude runs every stage, reads the frames, decides the timing and zooms, renders, verifies, and
writes `projects/demo/output/report.md` with every judgment call it made. Outputs:
`output/final.mp4`, `output/preview.mp4`, `output/report.md`, `output/checks/zoom_*.jpg`.

To correct something, edit the JSON for that stage in `projects/demo/work/` (e.g. an action's
position in `actions.json`, a cut in `sync.json`) and ask Claude to continue. Earlier stages are reused.

## Usage by hand

```bash
P=projects/demo
python tools/probe.py        --project $P
python tools/transcribe.py   --project $P
python tools/align_script.py --project $P
python tools/scenes.py       --project $P
python tools/frames.py       --project $P --sheets --event-sheets
#   write work/actions.json (see .claude/skills/screencast-analyze/SKILL.md)
python tools/check.py        --project $P --actions
#   write work/sync.json   (see .claude/skills/screencast-sync/SKILL.md)
python tools/plan_builder.py --project $P
python tools/render.py       --project $P --preview
python tools/render.py       --project $P
python tools/verify.py       --project $P
```

Useful extras:

| command | what it does |
|---|---|
| `frames.py --at 12.4 --crop 0,0,400,300 --grid --mark 100,60` | one frame, region at native res, pixel grid, crosshair |
| `frames.py --around 12.4` | 0.5 s before/after a change |
| `frames.py --video $P/output/preview.mp4 --sheet-at 5,10,15` | contact sheet of the preview |
| `render.py --preview --from 20 --to 30` | quick check of one range |
| `render.py --cursor-halo --ripple-color "#FF5A36"` | yellow cursor halo, custom ripple colour |
| `render.py --check` | validate plan.json without rendering |

## Layout

```
tools/                 CLIs (one per stage) + common.py, check.py helpers
.claude/skills/        screencast-edit (orchestrator), screencast-analyze, screencast-sync
docs/lessons.md        mistakes that cost a render; read before every run
projects/<name>/
  input/               recording.*, voiceover.*, script.md, clicks.json
  work/                every intermediate JSON + frames/
  output/              final.mp4, preview.mp4, report.md, checks/
```

See `CLAUDE.md` for the pipeline contract and the plan.json format.
