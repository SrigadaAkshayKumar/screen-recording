"""Align script.md sentences to the transcribed words -> work/lines.json.

Each line: {id, text, start, end, notes, match, status, word_range, words}.
Lines wholly in parentheses or brackets, e.g. "(On screen: the Upload dialog)", are not spoken:
they become `notes` on the next sentence. Inline "(Label: ...)" cues are moved to notes too.
"""
from __future__ import annotations

import difflib
import re

from common import Project, die, parser, write_json

NUMS = {w: str(i) for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}
NUMS.update({"first": "1st", "second": "2nd", "third": "3rd"})
ABBR = {"e.g.", "i.e.", "etc.", "vs.", "mr.", "mrs.", "ms.", "dr.", "no.", "approx.", "fig."}
TOKEN = re.compile(r"[A-Za-z0-9']+")


def norm(tok: str) -> str:
    t = re.sub(r"[^a-z0-9]", "", tok.lower().replace("’", "'"))
    return NUMS.get(t, t)


def clean_md(line: str) -> str:
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)            # images
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)         # links -> text
    line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)        # list markers
    line = re.sub(r"^\s*>\s?", "", line)                         # quotes
    return re.sub(r"[*_`~]", "", line).strip()


def split_sentences(par: str) -> list[str]:
    out, start = [], 0
    for m in re.finditer(r"[.!?]+[\"')\]”]*\s+", par):
        prev = par[start:m.end()].split()
        if prev and prev[-1].lower() in ABBR:
            continue
        out.append(par[start:m.end()].strip())
        start = m.end()
    if par[start:].strip():
        out.append(par[start:].strip())
    return out


def parse_script(text: str) -> list[dict]:
    """-> [{text, notes}] for every spoken sentence."""
    sentences: list[dict] = []
    pending: list[str] = []
    par: list[str] = []
    par_notes: list[str] = []

    def flush():
        nonlocal par, par_notes, pending
        if par:
            for s in split_sentences(" ".join(par)):
                if TOKEN.search(s):
                    sentences.append({"text": s, "notes": pending})
                    pending = []
            if par_notes:
                sentences[-1]["notes"] += par_notes
        par, par_notes = [], []

    for raw in text.splitlines():
        s = raw.strip()
        if not s or s.startswith("#") or s in ("---", "***"):
            flush()
            continue
        if re.fullmatch(r"\(.*\)|\[.*\]", s):
            flush()
            pending.append(s[1:-1].strip())
            continue
        line = clean_md(s)
        inline = re.findall(r"\(([A-Za-z ]{2,20}:[^)]*)\)", line)
        if inline:
            par_notes += [n.strip() for n in inline]
            line = re.sub(r"\s*\([A-Za-z ]{2,20}:[^)]*\)", "", line)
        if line:
            par.append(line)
    flush()
    if pending and sentences:
        sentences[-1]["notes"] += pending
    return sentences


def fuzzy_pairs(a: list[str], b: list[str]) -> list[tuple[int, int]]:
    """Monotonic pairs of similar tokens inside a 'replace' block."""
    pairs, j0 = [], 0
    for i, ta in enumerate(a):
        best, bj = 0.0, -1
        for j in range(j0, min(len(b), j0 + 4)):
            r = difflib.SequenceMatcher(None, ta, b[j]).ratio()
            if r > best:
                best, bj = r, j
        if best >= 0.75 and len(ta) >= 3:
            pairs.append((i, bj))
            j0 = bj + 1
    return pairs


def main():
    ap = parser(__doc__)
    ap.add_argument("--bad", type=float, default=0.6, help="flag lines whose match ratio is below this")
    a = ap.parse_args()
    pr = Project(a.project)
    words = pr.need("words.json", "tools/transcribe.py")
    script = pr.input / "script.md"
    if not script.exists():
        # No script supplied: the transcript becomes the script (no on-screen notes, exact match).
        script.write_text(pr.w("transcript.txt").read_text(encoding="utf-8"), encoding="utf-8")
        print(f"no script.md - using the transcript as the script ({script})")
    sents = parse_script(script.read_text(encoding="utf-8"))
    if not sents:
        die(f"no spoken sentences found in {script}")

    # Script tokens (with sentence id) and transcript tokens (with word index).
    s_tok, s_sid = [], []
    for k, s in enumerate(sents):
        for t in TOKEN.findall(s["text"]):
            if norm(t):
                s_tok.append(norm(t))
                s_sid.append(k)
    t_tok, t_wid = [], []
    for i, w in enumerate(words):
        for t in TOKEN.findall(w["word"]):
            if norm(t):
                t_tok.append(norm(t))
                t_wid.append(i)

    sm = difflib.SequenceMatcher(None, s_tok, t_tok, autojunk=False)
    match: dict[int, int] = {}        # script token -> transcript word index
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for d in range(i2 - i1):
                match[i1 + d] = t_wid[j1 + d]
        elif op == "replace":
            for di, dj in fuzzy_pairs(s_tok[i1:i2], t_tok[j1:j2]):
                match[i1 + di] = t_wid[j1 + dj]

    n = len(sents)
    ntok = [0] * n
    lo, hi = [None] * n, [None] * n
    lead, trail = [0] * n, [0] * n
    for ti, k in enumerate(s_sid):
        ntok[k] += 1
    for k in range(n):
        idx = [ti for ti, sk in enumerate(s_sid) if sk == k]
        m = [ti for ti in idx if ti in match]
        if m:
            lo[k], hi[k] = match[m[0]], match[m[-1]]
            lead[k] = idx.index(m[0])
            trail[k] = len(idx) - 1 - idx.index(m[-1])
    nmatch = [sum(1 for ti, sk in enumerate(s_sid) if sk == k and ti in match) for k in range(n)]

    # Hand transcript words in the gaps between matched sentences to the sentences whose
    # leading/trailing tokens did not match, and spread what remains over unmatched sentences.
    rng: list[list[int] | None] = [[lo[k], hi[k]] if lo[k] is not None else None for k in range(n)]
    adlib: list[int] = []
    anchors = [k for k in range(n) if rng[k]]
    if not anchors:
        die("the script does not match the transcript at all - wrong script or voiceover?")
    bounds = [(-1, None)] + [(k, None) for k in anchors] + [(n, None)]
    for (p, _), (q, _) in zip(bounds, bounds[1:]):
        g0 = rng[p][1] + 1 if p >= 0 else 0
        g1 = rng[q][0] - 1 if q < n else len(words) - 1
        gap = list(range(g0, g1 + 1))
        if not gap:
            continue
        between = list(range(p + 1, q))
        want_p = int(trail[p] * 1.5) + (1 if trail[p] else 0) if p >= 0 else 0
        want_q = int(lead[q] * 1.5) + (1 if lead[q] else 0) if q < n else 0
        if not between and want_p and want_q and want_p + want_q > len(gap):
            want_p = round(len(gap) * trail[p] / (trail[p] + lead[q]))
            want_q = len(gap) - want_p
        take_p = gap[:min(want_p, len(gap))]
        rest = gap[len(take_p):]
        take_q = rest[len(rest) - min(want_q, len(rest)):] if want_q else []
        mid = rest[: len(rest) - len(take_q)]
        if take_p:
            rng[p][1] = take_p[-1]
        if take_q:
            rng[q][0] = take_q[0]
        if between and mid:
            tot = sum(ntok[k] for k in between)
            pos = 0
            for j, k in enumerate(between):
                cnt = len(mid) - pos if j == len(between) - 1 else round(len(mid) * ntok[k] / tot)
                if cnt > 0:
                    rng[k] = [mid[pos], mid[min(pos + cnt, len(mid)) - 1]]
                    pos += cnt
        elif mid:
            adlib += mid

    lines = []
    prev_end = 0.0
    for k, s in enumerate(sents):
        ratio = nmatch[k] / ntok[k] if ntok[k] else 0.0
        r = rng[k]
        if r and r[0] <= r[1]:
            start, end = words[r[0]]["start"], words[r[1]]["end"]
            ws = [{"i": i, "word": words[i]["word"], "start": words[i]["start"], "end": words[i]["end"]}
                  for i in range(r[0], r[1] + 1)]
            status = "ok" if ratio >= 0.8 else ("fuzzy" if ratio >= a.bad else "bad")
        else:
            start = end = prev_end
            ws, r, status = [], None, "missing"
        prev_end = end
        lines.append({"id": k + 1, "text": s["text"], "start": start, "end": end, "notes": s["notes"],
                      "match": ratio, "status": status, "word_range": r, "words": ws})

    write_json(pr.w("lines.json"), lines)
    total = sum(nmatch) / max(1, sum(ntok))
    for ln in lines:
        flag = "" if ln["status"] == "ok" else f"  <-- {ln['status'].upper()}"
        print(f"L{ln['id']:<3} {ln['start']:7.2f}-{ln['end']:7.2f}  {ln['match']:4.0%}  {ln['text'][:60]}{flag}")
    if adlib:
        print(f"unscripted speech (ad-libs): " + " ".join(words[i]["word"] for i in adlib))
    bad = [ln for ln in lines if ln["status"] in ("bad", "missing")]
    print(f"overall match {total:.0%}; {len(bad)} line(s) matched badly")
    print(f"-> {pr.w('lines.json')}")
    if total < 0.3:
        die("under 30% of the script matched the voiceover - check that they belong together", 1)


if __name__ == "__main__":
    main()
