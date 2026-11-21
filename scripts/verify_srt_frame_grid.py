#!/usr/bin/env python3
"""Zero-dependency NLE frame-grid validator for .srt subtitle files.

Checks whether every subtitle cue start/end timestamp snaps cleanly onto an
integer frame boundary for standard NLE frame rates (23.976 .. 120 fps), and
detects 1-frame flash gaps or cue overlaps.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

FPS_RATIONAL = {
    "23.976": 24000 / 1001,
    "24": 24.0,
    "25": 25.0,
    "29.97": 30000 / 1001,
    "30": 30.0,
    "48": 48.0,
    "50": 50.0,
    "59.94": 60000 / 1001,
    "60": 60.0,
    "120": 120.0,
}

CUE_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2}),(\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2}),(\d{3})"
)


def to_ms(h: str, m: str, s: str, ms: str) -> int:
    return ((int(h) * 60 + int(m)) * 60 + int(s)) * 1000 + int(ms)


def nearest_frame_delta_ms(ms: int, fps: float) -> tuple[int, float]:
    frame_idx = round(ms * fps / 1000.0)
    # Standard SRT integer-ms floor/round representation of exact frame N
    exact_ms = frame_idx * 1000.0 / fps
    valid_ms = {int(exact_ms), round(exact_ms)}
    delta = 0.0 if ms in valid_ms else abs(ms - exact_ms)
    return frame_idx, delta


def audit_srt(path: pathlib.Path, fps_key: str, tolerance_ms: float = 1.5) -> int:
    fps = FPS_RATIONAL[fps_key]
    text = path.read_text(encoding="utf-8-sig")
    matches = list(CUE_RE.finditer(text))
    if not matches:
        print(f"[WARN] {path.name}: no valid SRT timestamps found.")
        return 1

    off_grid = 0
    overlaps = 0
    one_frame_flashes = 0
    prev_end_frame = None

    for idx, m in enumerate(matches, 1):
        g = m.groups()
        start_ms = to_ms(*g[:4])
        end_ms = to_ms(*g[4:])
        sf, s_err = nearest_frame_delta_ms(start_ms, fps)
        ef, e_err = nearest_frame_delta_ms(end_ms, fps)
        if s_err > tolerance_ms or e_err > tolerance_ms:
            off_grid += 1
            print(
                f"  Cue #{idx}: off-grid timestamp ({start_ms}ms -> {end_ms}ms, "
                f"nearest frames #{sf}->#{ef}, err={max(s_err, e_err):.2f}ms)"
            )
        if prev_end_frame is not None:
            gap_frames = sf - prev_end_frame
            if gap_frames < 0:
                overlaps += 1
                print(f"  Cue #{idx}: overlap with previous cue ({gap_frames} frames)")
            elif gap_frames == 1:
                one_frame_flashes += 1
                print(f"  Cue #{idx}: 1-frame black flash gap detected (frame #{prev_end_frame}->#{sf})")
        prev_end_frame = ef

    status = "PASS" if (off_grid == 0 and overlaps == 0 and one_frame_flashes == 0) else "ISSUES"
    print(
        f"[{status}] {path.name} @ {fps_key}fps | cues={len(matches)} | "
        f"off_grid={off_grid} | overlaps={overlaps} | 1f_flash={one_frame_flashes}"
    )
    return 0 if status == "PASS" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify SRT integer-frame alignment.")
    parser.add_argument("srt_file", type=pathlib.Path, help="Path to .srt file")
    parser.add_argument("--fps", choices=list(FPS_RATIONAL.keys()), default="24")
    args = parser.parse_args()
    return audit_srt(args.srt_file, args.fps)


if __name__ == "__main__":
    sys.exit(main())
