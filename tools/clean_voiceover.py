"""Cut spoken script headings out of a voiceover before editing (one-off batch fix).

The 2026-10 batch's voiceovers were generated from the full script text, so they also speak the
"SCRIPT N" line, the title and the "(On screen: ...)" note. This tool transcribes the voiceover,
aligns it to the script, and removes the audio of those lines, keeping a natural pause at each join.

    python tools/clean_voiceover.py --scripts voiceover-fix/all-scripts.txt --number 1 \
        --audio inbox/script-01-new.mp3 --write-script inbox/script-01-new.md --backup orig/

The audio file is replaced in place (the original is copied to --backup). --write-script saves the
spoken lines only, so the pipeline aligns against the real narration.
"""
import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PAUSE = 0.30      # silence kept on each side of a cut (s) -> about 0.6 s between sentences
LEAD = 0.25       # silence kept before the first spoken word
FADE = 0.015      # tiny fade on each join to avoid clicks


def tokens(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9']+", text.lower().replace("’", "'")) if t.strip("'")]


def script_block(path: Path, number: int) -> list[str]:
    blocks = re.split(r"\n=+\s*\n", path.read_text(encoding="utf-8"))
    for b in blocks:
        lines = [l.strip() for l in b.splitlines() if l.strip()]
        if lines and re.fullmatch(rf"SCRIPT\s+{number}", lines[0], re.I):
            return lines
    raise SystemExit(f"error: no 'SCRIPT {number}' block in {path}")


def is_junk(i: int, line: str) -> bool:
    # line 0 "SCRIPT N", line 1 the title, and any "(On screen: ...)" note
    return i < 2 or (line.startswith("(") and line.endswith(")"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scripts", required=True)
    ap.add_argument("--number", type=int, required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--write-script")
    ap.add_argument("--backup")
    ap.add_argument("--log", help="write the cut list as JSON here")
    ap.add_argument("--model", default="small.en")
    a = ap.parse_args()

    audio = Path(a.audio)
    if not audio.exists():
        raise SystemExit(f"error: {audio} not found")
    lines = script_block(Path(a.scripts), a.number)

    stoks, slabel = [], []                     # script tokens and whether each is junk
    for i, line in enumerate(lines):
        t = tokens(line)
        stoks += t
        slabel += [is_junk(i, line)] * len(t)
    n_junk = sum(slabel)

    from faster_whisper import WhisperModel
    model = WhisperModel(a.model, device="cpu", compute_type="int8")
    segs, info = model.transcribe(str(audio), language="en", word_timestamps=True, beam_size=5, vad_filter=False)
    words = [{"word": w.word.strip(), "start": w.start, "end": w.end} for s in segs for w in (s.words or [])]
    dur = info.duration
    if not words:
        raise SystemExit("error: no speech found in the voiceover")

    atoks, owner = [], []                      # transcript tokens -> index of their word
    for wi, w in enumerate(words):
        for t in tokens(w["word"]):
            atoks.append(t)
            owner.append(wi)

    label = [None] * len(words)
    matched_junk = 0
    sm = difflib.SequenceMatcher(None, stoks, atoks, autojunk=False)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            wi = owner[blk.b + k]
            if label[wi] is None:
                label[wi] = slabel[blk.a + k]
            matched_junk += slabel[blk.a + k]
    # unmatched words take the label of the nearest matched word before them (after, at the start)
    last = next((l for l in label if l is not None), False)
    for i in range(len(label)):
        if label[i] is None:
            label[i] = last
        last = label[i]

    cuts, i = [], 0
    while i < len(words):
        if not label[i]:
            i += 1
            continue
        j = i
        while j + 1 < len(words) and label[j + 1]:
            j += 1
        prev_end = words[i - 1]["end"] if i > 0 else None
        next_start = words[j + 1]["start"] if j + 1 < len(words) else None
        a0 = 0.0 if prev_end is None else prev_end + PAUSE
        b0 = dur if next_start is None else next_start - (LEAD if prev_end is None else PAUSE)
        if b0 - a0 > 0.1 and (j - i >= 2 or i == 0):      # a lone mismatched word is never cut
            cuts.append({"start": round(a0, 3), "end": round(b0, 3),
                         "text": " ".join(w["word"] for w in words[i:j + 1])})
        i = j + 1

    removed = sum(c["end"] - c["start"] for c in cuts)
    print(f"script {a.number}: {len(words)} words, junk tokens matched {matched_junk}/{n_junk}, "
          f"{len(cuts)} cut(s), {removed:.2f} s removed of {dur:.2f} s")
    for c in cuts:
        print(f"  cut {c['start']:7.2f}-{c['end']:7.2f}: {c['text']}")
    if n_junk and matched_junk < 0.6 * n_junk:
        print(f"::warning::script {a.number}: only {matched_junk}/{n_junk} heading words found in the voiceover")
    if not cuts:
        print("nothing to cut; audio left unchanged")
    else:
        keep, t = [], 0.0
        for c in cuts:
            if c["start"] > t:
                keep.append((t, c["start"]))
            t = c["end"]
        if t < dur:
            keep.append((t, dur))
        parts, labels = [], []
        for k, (s, e) in enumerate(keep):
            d = e - s
            parts.append(f"[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,"
                         f"afade=t=in:d={FADE},afade=t=out:st={max(0, d - FADE):.3f}:d={FADE}[k{k}]")
            labels.append(f"[k{k}]")
        graph = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(keep)}:v=0:a=1[out]"
        if a.backup:
            Path(a.backup).mkdir(parents=True, exist_ok=True)
            shutil.copy2(audio, Path(a.backup) / audio.name)
        tmp = audio.with_name(audio.stem + ".clean.tmp" + audio.suffix)
        codec = ["-c:a", "libmp3lame", "-q:a", "2"] if audio.suffix.lower() == ".mp3" else []
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(audio), "-filter_complex", graph,
                        "-map", "[out]", *codec, str(tmp)], check=True)
        os.replace(tmp, audio)
    if a.write_script:
        Path(a.write_script).write_text(
            "\n\n".join(l for i, l in enumerate(lines) if not is_junk(i, l)) + "\n", encoding="utf-8")
    if a.log:
        Path(a.log).write_text(json.dumps({"script": a.number, "duration_before": round(dur, 3),
                                           "removed": round(removed, 3), "cuts": cuts}, indent=2))


if __name__ == "__main__":
    sys.exit(main())
