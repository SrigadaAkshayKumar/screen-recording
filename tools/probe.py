"""ffprobe the recording and the voiceover -> work/probe.json (durations, fps, size)."""
from __future__ import annotations

from fractions import Fraction

from common import Project, die, ffprobe, parse_rate, parser, read_json, write_json


def stream(info: dict, kind: str) -> dict | None:
    return next((s for s in info["streams"] if s.get("codec_type") == kind), None)


def duration(info: dict, s: dict | None) -> float:
    for v in (info.get("format", {}).get("duration"), (s or {}).get("duration")):
        try:
            if v is not None and float(v) > 0:
                return float(v)
        except ValueError:
            pass
    return 0.0


def main():
    a = parser(__doc__).parse_args()
    pr = Project(a.project)
    warnings: list[str] = []

    rec_path = pr.recording
    info = ffprobe(rec_path)
    v = stream(info, "video")
    if not v:
        die(f"{rec_path} has no video stream")
    r = parse_rate(v.get("r_frame_rate"))
    avg = parse_rate(v.get("avg_frame_rate"))
    vfr = bool(r and avg and abs(float(r) - float(avg)) > 0.05 * float(r))
    # Every tool decodes at this rate through ffmpeg's fps filter, so VFR input becomes CFR.
    fps = r if r and 1 <= r <= 60 else (avg if avg and 1 <= avg <= 60 else Fraction(30))
    fps = fps.limit_denominator(1001)
    if vfr:
        warnings.append(f"recording is variable frame rate (r={float(r):.3f}, avg={float(avg):.3f}); "
                        f"all tools resample it to {float(fps):.3f} fps")
    rotation = None
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd:
            rotation = sd["rotation"]
    if rotation:
        warnings.append(f"recording has rotation metadata ({rotation}); screen recordings normally do not")
    rec_dur = duration(info, v)
    if rec_dur <= 0:
        die(f"cannot read the duration of {rec_path}")
    w, h = int(v["width"]), int(v["height"])
    if w % 2 or h % 2:
        warnings.append(f"recording size {w}x{h} is odd; libx264 needs even sizes - render will fail")

    vo_path = pr.voiceover
    ainfo = ffprobe(vo_path)
    au = stream(ainfo, "audio")
    if not au:
        die(f"{vo_path} has no audio stream")
    vo_dur = duration(ainfo, au)
    if vo_dur <= 0:
        die(f"cannot read the duration of {vo_path}")

    clicks = None
    if pr.clicks:
        c = read_json(pr.clicks)
        clicks = {"count": len(c.get("clicks", [])), "screen": c.get("screen"), "platform": c.get("platform")}
        if not clicks["count"]:
            warnings.append("clicks.json has no clicks")

    if vo_dur > rec_dur * 4:
        warnings.append(f"voiceover ({vo_dur:.1f}s) is over 4x the recording ({rec_dur:.1f}s); expect long holds")

    out = {
        "recording": {
            "file": rec_path.name, "duration": rec_dur, "fps": float(fps),
            "fps_fraction": f"{fps.numerator}/{fps.denominator}", "width": w, "height": h,
            "codec": v.get("codec_name"), "vfr": vfr, "has_audio": stream(info, "audio") is not None,
            "frames": int(round(rec_dur * float(fps))),
        },
        "voiceover": {
            "file": vo_path.name, "duration": vo_dur, "codec": au.get("codec_name"),
            "sample_rate": int(au.get("sample_rate", 0)), "channels": au.get("channels"),
        },
        "clicks": clicks,
        "warnings": warnings,
    }
    write_json(pr.w("probe.json"), out)
    print(f"recording  {w}x{h} @ {float(fps):.3f} fps, {rec_dur:.3f}s ({rec_path.name})")
    print(f"voiceover  {vo_dur:.3f}s ({vo_path.name})")
    if clicks:
        print(f"clicks     {clicks['count']} logged")
    for m in warnings:
        print(f"warning: {m}")
    print(f"-> {pr.w('probe.json')}")


if __name__ == "__main__":
    main()
