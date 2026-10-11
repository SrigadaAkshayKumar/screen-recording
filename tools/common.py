"""Shared helpers for the screencast-editor CLIs: project paths, JSON I/O, ffmpeg access."""
from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg", ".opus"}


def die(msg: str, code: int = 2) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def warn(msg: str) -> None:
    print(f"warning: {msg}", file=sys.stderr)


# ---------------------------------------------------------------- projects

class Project:
    """Paths inside projects/<name>/. Inputs keep a fixed stem; the extension is kept as given."""

    def __init__(self, path: str | Path):
        p = Path(path)
        if not p.exists() and not p.is_absolute() and (ROOT / p).exists():
            p = ROOT / p
        if not p.is_dir():
            die(f"project folder not found: {path} (create it with tools/new_project.py)")
        self.root = p.resolve()
        self.name = self.root.name
        self.input = self.root / "input"
        self.work = self.root / "work"
        self.output = self.root / "output"
        self.frames = self.work / "frames"
        for d in (self.work, self.output):
            d.mkdir(parents=True, exist_ok=True)

    def find_input(self, stem: str, exts: set[str], required: bool = True) -> Path | None:
        hits = [f for f in sorted(self.input.glob(stem + ".*")) if f.suffix.lower() in exts]
        if not hits:
            if required:
                die(f"missing input: {self.input / stem}.* ({', '.join(sorted(exts))})")
            return None
        return hits[0]

    @property
    def recording(self) -> Path:
        return self.find_input("recording", VIDEO_EXTS)

    @property
    def voiceover(self) -> Path:
        return self.find_input("voiceover", AUDIO_EXTS)

    @property
    def script(self) -> Path:
        p = self.input / "script.md"
        if not p.exists():
            die(f"missing input: {p}")
        return p

    @property
    def clicks(self) -> Path | None:
        p = self.input / "clicks.json"
        return p if p.exists() else None

    def w(self, name: str) -> Path:
        return self.work / name

    def need(self, name: str, producer: str):
        """Load work/<name>, or exit with a pointer to the stage that produces it."""
        p = self.work / name
        if not p.exists():
            die(f"{p} not found - run {producer} first")
        return read_json(p)

    def maybe(self, name: str):
        p = self.work / name
        return read_json(p) if p.exists() else None


def parser(description: str, project: bool = True) -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=description)
    if project:
        ap.add_argument("--project", required=True, help="projects/<name>")
    return ap


# ---------------------------------------------------------------- JSON

def _round(o):
    if isinstance(o, float):
        if math.isnan(o) or math.isinf(o):
            return None
        return round(o, 3)
    if isinstance(o, (np.floating,)):
        return _round(float(o))
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, dict):
        return {k: _round(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_round(v) for v in o]
    return o


def write_json(path: Path, obj) -> None:
    """Write JSON with every float rounded to 3 decimals, atomically (safe to hand-edit between runs)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(_round(obj), f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


def read_json(path: Path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        die(f"{path} is not valid JSON (line {e.lineno}, col {e.colno}): {e.msg}")
    except OSError as e:
        die(f"cannot read {path}: {e}")


def file_fingerprint(path: Path) -> str:
    """Cheap identity of a media file: size + SHA-1 of its first and last MiB."""
    import hashlib
    path = Path(path)
    size = path.stat().st_size
    h = hashlib.sha1()
    with open(path, "rb") as f:
        h.update(f.read(1 << 20))
        if size > 2 << 20:
            f.seek(-(1 << 20), os.SEEK_END)
            h.update(f.read(1 << 20))
    return f"{size}:{h.hexdigest()[:16]}"


def r3(t: float) -> float:
    return round(float(t), 3)


def tname(t: float) -> str:
    """Timestamp for file names: 12.3 -> '0012.300'."""
    return f"{t:08.3f}"


# ---------------------------------------------------------------- ffmpeg

def ffbin(name: str) -> str:
    exe = shutil.which(name)
    if not exe:
        die(f"{name} not found on PATH - install ffmpeg (winget install Gyan.FFmpeg / brew install ffmpeg)")
    return exe


def ffprobe(path: Path) -> dict:
    cmd = [ffbin("ffprobe"), "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        die(f"ffprobe failed on {path}: {res.stderr.strip()}")
    return json.loads(res.stdout)


def video_size(path: Path) -> tuple[int, int]:
    for s in ffprobe(path)["streams"]:
        if s.get("codec_type") == "video":
            return int(s["width"]), int(s["height"])
    die(f"no video stream in {path}")


def parse_rate(s: str | None) -> Fraction | None:
    try:
        f = Fraction(s)
        return f if f > 0 else None
    except (TypeError, ValueError, ZeroDivisionError):
        return None


def fps_fraction(probe: dict) -> Fraction:
    return Fraction(probe["recording"]["fps_fraction"])


def even(x: float) -> int:
    return max(2, int(round(x / 2)) * 2)


def run(cmd: list[str], what: str) -> subprocess.CompletedProcess:
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        die(f"{what} failed:\n{res.stderr.strip()[-2000:]}")
    return res


class FrameReader:
    """Decode a video as a constant-frame-rate stream of numpy frames.

    Frame i is the source frame shown at time i/fps (the same convention every tool uses:
    timestamps start at 0 at the first frame, VFR input is resampled to `fps`).
    """

    def __init__(self, path: Path, fps: Fraction, size: tuple[int, int], gray: bool = False,
                 start_index: int = 0, scale_flags: str = "bicubic"):
        self.path, self.fps, self.size, self.gray = path, fps, size, gray
        self.scale_flags = scale_flags
        self.channels = 1 if gray else 3
        self.frame_bytes = size[0] * size[1] * self.channels
        self.proc = None
        self.index = -1
        self.last = None
        self.eof = False
        self._open(start_index)

    def _open(self, start_index: int):
        self.close()
        w, h = self.size
        vf = f"setpts=PTS-STARTPTS,fps={self.fps.numerator}/{self.fps.denominator}," \
             f"scale={w}:{h}:flags={self.scale_flags}"
        cmd = [ffbin("ffmpeg"), "-v", "error", "-nostdin"]
        if start_index > 0:
            cmd += ["-ss", f"{max(0.0, (start_index - 0.5) / float(self.fps)):.6f}"]
        cmd += ["-i", str(self.path), "-an", "-sn", "-vf", vf, "-f", "rawvideo",
                "-pix_fmt", "gray" if self.gray else "bgr24", "-"]
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                     bufsize=self.frame_bytes * 2)
        self.index = start_index - 1
        self.eof = False

    def read(self):
        """Next frame, or None at end of stream."""
        if self.eof:
            return None
        buf = self.proc.stdout.read(self.frame_bytes)
        if len(buf) < self.frame_bytes:
            self.eof = True
            return None
        self.index += 1
        shape = (self.size[1], self.size[0]) if self.gray else (self.size[1], self.size[0], 3)
        self.last = np.frombuffer(buf, np.uint8).reshape(shape)
        return self.last

    def get(self, index: int, reseek_after: int = 300):
        """Frame `index` (reading forward; re-seeks for big jumps). Holds the last frame past EOF."""
        if index == self.index and self.last is not None:
            return self.last
        if index < self.index or index - self.index > reseek_after:
            self._open(index)
        while self.index < index:
            if self.read() is None:
                break
        return self.last

    def close(self):
        if self.proc:
            try:
                self.proc.stdout.close()
            except OSError:
                pass
            self.proc.kill()
            self.proc.wait()
            self.proc = None


def grab_frame(path: Path, t: float, fps: Fraction | None = None, size: tuple[int, int] | None = None):
    """One BGR frame at time t (frame floor(t*fps) when fps is known), optionally resized."""
    if size is None:
        size = video_size(path)
    if fps is not None:
        t = max(0.0, (math.floor(t * float(fps) + 1e-6) - 0.25) / float(fps))
    w, h = size
    cmd = [ffbin("ffmpeg"), "-v", "error", "-nostdin", "-ss", f"{max(0.0, t):.6f}", "-i", str(path),
           "-frames:v", "1", "-an", "-vf", f"scale={w}:{h}:flags=bicubic",
           "-f", "rawvideo", "-pix_fmt", "bgr24", "-"]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0 or len(res.stdout) < w * h * 3:
        # past the end: fall back to the last decodable frame
        if t > 0.5:
            return grab_frame(path, t - 0.25, None, size)
        die(f"could not decode a frame at {t:.3f}s from {path}")
    return np.frombuffer(res.stdout[: w * h * 3], np.uint8).reshape(h, w, 3).copy()


def save_jpg(path: Path, img, quality: int = 88) -> None:
    """cv2.imwrite fails silently on non-ASCII Windows paths; encode in memory instead."""
    import cv2
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    if not ok:
        die(f"could not encode {path}")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(buf.tobytes())


def parse_color(s: str) -> tuple[int, int, int]:
    """'#RRGGBB' or 'r,g,b' -> BGR tuple for OpenCV."""
    s = s.strip()
    try:
        if s.startswith("#") and len(s) == 7:
            r, g, b = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
        else:
            r, g, b = (int(v) for v in s.split(","))
    except ValueError:
        die(f"bad colour {s!r}: use #RRGGBB or r,g,b")
    return (b, g, r)


def parse_times(s: str) -> list[float]:
    try:
        return [float(v) for v in s.split(",") if v.strip()]
    except ValueError:
        die(f"bad time list {s!r}: use comma-separated seconds, e.g. 3.2,7.85")
