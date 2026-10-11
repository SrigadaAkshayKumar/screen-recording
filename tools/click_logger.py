"""OPTIONAL: log every mouse click while you record -> clicks.json.

Start this at the same moment as your screen recorder, then make your FIRST action a click on an
empty area of the screen (it marks the sync point). Stop with Ctrl+C. Times are seconds since this
script started; x/y are in the same units as the logged screen size (physical pixels on Windows,
points on macOS). scenes.py converts them to recording time and pixels.

    python tools/click_logger.py --out clicks.json

macOS: grant your terminal Accessibility and Input Monitoring permission (System Settings ->
Privacy & Security), or no clicks are reported.
"""
from __future__ import annotations

import argparse
import ctypes
import datetime as dt
import json
import os
import platform
import sys
import threading
import time
from pathlib import Path


def screen_info() -> dict:
    sysname = platform.system()
    if sysname == "Windows":
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)      # per-monitor aware: physical pixels
        except (AttributeError, OSError):
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except (AttributeError, OSError):
                pass
        u = ctypes.windll.user32
        w, h = u.GetSystemMetrics(0), u.GetSystemMetrics(1)
        try:
            scale = u.GetDpiForSystem() / 96.0
        except (AttributeError, OSError):
            scale = 1.0
        return {"width": w, "height": h, "dpi_scale": scale, "units": "physical pixels"}
    if sysname == "Darwin":
        try:
            cg = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")
            cg.CGMainDisplayID.restype = ctypes.c_uint32
            cg.CGDisplayCopyDisplayMode.restype = ctypes.c_void_p
            cg.CGDisplayCopyDisplayMode.argtypes = [ctypes.c_uint32]
            for fn in ("CGDisplayModeGetWidth", "CGDisplayModeGetHeight", "CGDisplayModeGetPixelWidth"):
                getattr(cg, fn).restype = ctypes.c_size_t
                getattr(cg, fn).argtypes = [ctypes.c_void_p]
            mode = cg.CGDisplayCopyDisplayMode(cg.CGMainDisplayID())
            w, h = cg.CGDisplayModeGetWidth(mode), cg.CGDisplayModeGetHeight(mode)
            pw = cg.CGDisplayModeGetPixelWidth(mode)
            return {"width": int(w), "height": int(h), "dpi_scale": pw / w if w else 1.0, "units": "points"}
        except OSError:
            pass
    try:
        import tkinter
        r = tkinter.Tk()
        r.withdraw()
        w, h = r.winfo_screenwidth(), r.winfo_screenheight()
        r.destroy()
        return {"width": w, "height": h, "dpi_scale": 1.0, "units": "unknown"}
    except Exception:
        return {"width": None, "height": None, "dpi_scale": 1.0, "units": "unknown"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="clicks.json")
    a = ap.parse_args()
    screen = screen_info()            # before pynput so the DPI awareness applies to its hooks
    try:
        from pynput import mouse
    except ImportError:
        print("error: pynput is not installed - run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(2)

    out = Path(a.out)
    lock = threading.Lock()
    t0 = time.perf_counter()
    data = {"version": 1, "started_at": dt.datetime.now().astimezone().isoformat(timespec="milliseconds"),
            "platform": platform.system(), "screen": screen, "clicks": []}
    down: dict[str, dict] = {}

    def save():
        tmp = out.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        os.replace(tmp, out)

    def on_click(x, y, button, pressed):
        t = round(time.perf_counter() - t0, 3)
        name = getattr(button, "name", str(button))
        with lock:
            if pressed:
                c = {"t": t, "x": int(x), "y": int(y), "button": name}
                data["clicks"].append(c)
                down[name] = c
                print(f"  {t:8.3f}s  {name:<6} {int(x)},{int(y)}", flush=True)
            elif name in down:
                c = down.pop(name)
                c.update({"t_up": t, "x_up": int(x), "y_up": int(y)})
            save()

    save()
    print(f"logging clicks to {out} (screen {screen['width']}x{screen['height']} {screen['units']}, "
          f"scale {screen['dpi_scale']:.2f})")
    print("start the recorder now; first action: click an empty area. Ctrl+C to stop.", flush=True)
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    try:
        while listener.is_alive():
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass
    finally:
        listener.stop()
        with lock:
            data["stopped_after"] = round(time.perf_counter() - t0, 3)
            save()
    print(f"\n{len(data['clicks'])} clicks -> {out}")


if __name__ == "__main__":
    main()
