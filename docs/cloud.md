# Running in the cloud (GitHub Actions + Google Drive)

Videos stay in Google Drive and only code and small JSON files go to GitHub. You start a run by
clicking **Run workflow**. The workflow edits **every video in the Drive inbox**, one after another,
and puts the results in the Drive output folder.

## Which Drive, which folders

The workflow uses the Google account you log into during `rclone config` (step 1 below), and works
in that account's **My Drive**. On the first run it creates this layout:

```
My Drive/screencast-editor/        <- the name can be changed with the variable DRIVE_FOLDER
  inbox/                           <- you put the files here
  output/                          <- the workflow puts the results here
```

### inbox: the to-do list

Put in as many videos as you like (3, 15, 25…). Every run edits all of them, one after another.
There are two ways to put them in, and you can mix them:

```
inbox/
  script-01/                       <- one folder per video: the folder name is the project name,
    screen recording.mp4              the file names inside don't matter
    voiceover final.mp3
    script.md                      <- optional
  script-02.mp4                    <- or loose files: video and voiceover with the same name
  script-02.mp3
```

- **Folder:** one video and one audio file, with any names. A `.md`/`.txt` in it is used as the
  script, and a `.json` as the click log. If a folder holds several videos, they pair by name
  inside it.
- **Loose files:** `<name>.mp4` + `<name>.mp3` (also `.mov`, `.mkv`, `.wav`, `.m4a`, …), plus an
  optional `<name>.md` or `<name>.json`.
- Without a script, the voiceover transcript is used.
- Anything incomplete (a video with no audio, or the reverse) is skipped and named in the run log.
- Nothing is remembered as "done". Every run edits everything that is in the inbox, so clear the
  inbox after a batch. Names can repeat in the next batch: when a `script-01` arrives with
  different files, the old `script-01` edits are discarded and it is edited from scratch.

### output

`output/<name>/` contains `final.mp4`, `report.md` (every editing decision), `checks/`,
`cloud-status.txt` and `work/` (the editing data). A newer run with the same name **replaces** that
folder, so download or rename finished videos before you reuse a name.

## One-time setup

### 1. Connect rclone to Google Drive (on your laptop)

rclone is already installed (`winget install Rclone.Rclone` if it is missing). Run:

```
rclone config
```
- `n` (new remote). Name: **`gdrive`** (exactly this).
- Storage: type `drive` (Google Drive).
- client_id and client_secret: press Enter (leave them blank).
- scope: `1` (full access).
- service_account_file: Enter. Edit advanced config: `n`. Use web browser to authenticate: `y`.
  Log in with **the Google account whose Drive should be used** and allow access.
- Configure as Shared Drive: `n`. Then `y` to keep the remote, and `q` to quit.

Test it: `rclone lsf gdrive:` should list your My Drive.

Copy the configuration for GitHub:
```
rclone config show gdrive
```
Copy everything from `[gdrive]` to the end, including the long `token = {...}` line.

### 2. GitHub repository settings

Go to Settings -> Secrets and variables -> Actions:

| kind | name | value |
|---|---|---|
| Secret | `RCLONE_CONF` | the `[gdrive]` block from step 1 |
| Secret (optional) | `ANTHROPIC_API_KEY` | an Anthropic API key. Lets Claude make the editing decisions in the cloud |
| Secret (optional) | `CLAUDE_CODE_OAUTH_TOKEN` | the alternative to the API key: run `claude setup-token` on your laptop to use your Claude Pro/Max plan |
| Variable (optional) | `DRIVE_FOLDER` | another Drive folder name instead of `screencast-editor` |

Settings -> Actions -> General -> Workflow permissions: choose **Read and write permissions**.

## Running

1. Put the videos and voiceovers in `screencast-editor/inbox` in Drive.
2. On GitHub, open Actions -> **Edit screencasts** -> **Run workflow**.
   - `projects`: `all` edits everything in the inbox. A list like `script-05,script-07` edits only those.
   - `model`: the Claude model for the editing decisions. Leave it blank for the default.
3. Each video runs as its own job, one at a time. A failed video doesn't stop the others. The run
   summary shows each video's status, and results appear in `screencast-editor/output/<name>/`.

## What happens to each video

1. **Mechanical stages:** probe, transcribe, align, scenes and frames.
2. **Editing decisions** (what is clicked when, and which word each click lands on):
   - With a Claude key, Claude Code runs the `screencast-edit` skill unattended. It does the same
     thing as `/screencast-edit <name>` in the terminal, including the preview review and the report.
   - Without a key, the job ends with the warning "needs analysis". You can then run
     `/screencast-edit <name>` on the laptop for those same files and push `projects/<name>/work/`.
     The next run of the workflow reuses those decisions and only renders.
3. **Render and verify:** `final.mp4` is rendered and checked with `verify.py`.
4. **Save:** the results go to Drive, and `work/` is committed to the repo. If the same files are
   run again, nothing is redone except the render.

## Limits and costs

- GitHub Actions minutes are free and unlimited for public repositories. Private repositories get
  2,000 free minutes a month. One 75 s video with a 3-4 minute recording takes about 10-20 minutes
  without Claude, and 20-60 minutes with the Claude stages. Each job may run up to 4 hours.
- The Claude stages read many frame images, so each video uses API credit (or plan usage).
- Never commit `rclone.conf` or keys. Treat the `RCLONE_CONF` secret like a password: it gives
  access to your Drive.
