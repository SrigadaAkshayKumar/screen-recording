"""Word timestamps for the voiceover with faster-whisper -> work/words.json [{word,start,end,prob}].

The model (small.en by default, ~470 MB) downloads on first run and is cached by huggingface_hub.
"""
from __future__ import annotations

import time

from common import Project, die, parser, write_json


def main():
    ap = parser(__doc__)
    ap.add_argument("--model", default="small.en", help="faster-whisper model (default small.en)")
    ap.add_argument("--compute-type", default="int8")
    ap.add_argument("--no-vad", action="store_true", help="disable the silence filter")
    ap.add_argument("--prompt-from-script", action="store_true",
                    help="prime the decoder with the script's vocabulary (helps product names)")
    a = ap.parse_args()
    pr = Project(a.project)
    vo = pr.voiceover

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        die("faster-whisper is not installed - run: pip install -r requirements.txt")

    prompt = None
    if a.prompt_from_script:
        txt = " ".join(l.strip() for l in pr.script.read_text(encoding="utf-8").splitlines()
                       if l.strip() and not l.strip().startswith(("(", "#", "[")))
        prompt = txt[:600]

    print(f"loading {a.model} ({a.compute_type}, CPU) - first run downloads the model ...", flush=True)
    t0 = time.time()
    model = WhisperModel(a.model, device="cpu", compute_type=a.compute_type)
    segments, info = model.transcribe(
        str(vo), language="en", word_timestamps=True, beam_size=5,
        vad_filter=not a.no_vad, initial_prompt=prompt,
    )
    words = []
    text = []
    for seg in segments:
        text.append(seg.text.strip())
        for w in seg.words or []:
            tok = w.word.strip()
            if tok:
                words.append({"word": tok, "start": w.start, "end": max(w.end, w.start), "prob": w.probability})
        print(f"  {seg.end:7.2f}s / {info.duration:.2f}s  {seg.text.strip()[:70]}", flush=True)
    if not words:
        die("no speech found in the voiceover")

    write_json(pr.w("words.json"), words)
    pr.w("transcript.txt").write_text("\n".join(text) + "\n", encoding="utf-8")
    low = [w for w in words if w["prob"] < 0.4]
    print(f"{len(words)} words in {time.time() - t0:.0f}s; {len(low)} low-confidence")
    print(f"-> {pr.w('words.json')}")


if __name__ == "__main__":
    main()
