# Multilingual SRT PRO — Frame-Accurate Subtitle Benchmarks & Utilities

**English** | [简体中文](./README.zh-CN.md) | [Browser Tool (SRT Reframe & FCPXML)](https://bbllhenhj.github.io/multilingual-srt-pro-docs/en/#studio) | [中文网页版](https://bbllhenhj.github.io/multilingual-srt-pro-docs/)

Public documentation, verified integer-frame `.srt` benchmark samples, a zero-dependency frame-grid verifier, and a client-side browser utility for scripted video subtitle workflows in Premiere Pro, DaVinci Resolve, Final Cut Pro, and CapCut / Jianying.

> **Scope & Disambiguation**: This repository hosts open utilities, benchmark samples, and technical specs for the closed-source on-device AI Agent Skill **Multilingual SRT PRO** (`multilingual-srt-pro`, Alipay AIPay PAYATHON 2026 Machine Pay Track). It is unaffiliated with the standalone desktop GUI software `Videosrt Pro`.

---

## 1. Open Utilities Included Here (Free, Local Execution)

### Browser Tool: SRT Reframe & Frame-Rate Studio
Open directly in any browser (no login, runs locally in browser memory):
- **Live URL**: https://bbllhenhj.github.io/multilingual-srt-pro-docs/en/#studio
- Converts existing `16:9` two-line `.srt` files into `9:16` single-line vertical captions (with basic EN/DE/FR/ES preposition anti-orphan handling).
- Rescales `23.976 <-> 24` and `29.97 <-> 30 fps` (`1000/1001`) pull-up drift and quantizes cue boundaries onto 10 exact NLE frame grids (`23.976`, `24`, `25`, `29.97`, `30`, `48`, `50`, `59.94`, `60`, `120 fps`) to eliminate 1-frame black gaps.
- Flags cues exceeding `20 CPS` and exports Final Cut Pro `.fcpxml` (v1.10 connected Basic Titles).

### CLI Frame-Grid Verifier (Python Standard Library Only)
Check whether any `.srt` file lands on exact integer frame boundaries (`round(frame * 1000 / fps)`) with zero frame gaps or overlaps:

```bash
python scripts/verify_srt_frame_grid.py samples/03_en_30fps_balanced_ratio_077.srt --fps 30
```

### Benchmark `.srt` Samples
All files in [`samples/`](./samples/) can be imported directly into Premiere Pro, DaVinci Resolve, Final Cut Pro, or Jianying to inspect frame alignment and line wrapping:

| Sample File | Locale & Layout | Frame Rate | Notes |
| :--- | :--- | :--- | :--- |
| [`samples/01_cn_24fps_landscape_16x9.srt`](./samples/01_cn_24fps_landscape_16x9.srt) | Simplified Chinese, 16:9 two-line | `24 fps` | Exact frame seams (`Frame 6: 00:00,250` -> `Frame 53: 00:02,208` -> `Frame 132: 00:05,500`) |
| [`samples/02_cn_60fps_portrait_9x16.srt`](./samples/02_cn_60fps_portrait_9x16.srt) | Simplified Chinese, 9:16 single-line | `60 fps` | Max 13 chars per line |
| [`samples/03_en_30fps_balanced_ratio_077.srt`](./samples/03_en_30fps_balanced_ratio_077.srt) | English, 16:9 two-line | `30 fps` | Syntax-aware wrap (`0.77` measured short/long line width ratio) |
| [`samples/04_de_24fps_zero_orphan.srt`](./samples/04_de_24fps_zero_orphan.srt) | German, 16:9 two-line | `24 fps` | Clause-frame protection (no dangling articles or prepositions) |

---

## 2. Full On-Device AI Agent Skill (Multilingual SRT PRO)

When starting from an **approved narration script** + raw local video/audio (rather than an existing `.srt`), the closed-source `SKILL.md` package runs local acoustic forced alignment without uploading source video files:

- **Supported hosts**: Claude Code, Cursor, Antigravity (macOS / Windows, local execution).
- **Script locking**: Keeps the approved script verbatim to avoid ASR homophone typos on domain terminology and numbers (tested on 8,000+ word scripts).
- **27-locale formatting**: Breath-pause segmentation, balanced syntax wrapping, RTL support (Arabic), and 10-rate integer-frame snapping.
- **Official Download Page**: https://aipay.alipay.com/community?view=work%2FHKWI_f70adb9f65ce499d8abf3ebd65effdef (click **"下载 Skill 包"** on the Alipay AIPay showcase page).

### Billing & Revision Terms
- **Pay-per-use**: `0.50 CNY` (~`$0.07 USD`) per run via Alipay AIPay Machine Pay (Nov 2026 baseline; live rate is governed by the official work page).
- **24-hour free revisions**: Re-running with **either the same script text or the same audio file** within 24 hours does not trigger repeat charges:
  1. Same audio with edited script wording, terminology, or punctuation.
  2. Same script with a re-recorded voiceover take or adjusted pacing.
  3. Switching layouts (`16:9` <-> `9:16`) or exporting across any of the 10 supported frame rates.
- **Users without Alipay**: The browser utility and Python verifier in this repo are free to use without an account. You can also log international payment requests via [GitHub Issues](https://github.com/bbllhenhj/multilingual-srt-pro-docs/issues/new?title=International+Payment+Request).

---

## 3. Feature Comparison

| Dimension | Multilingual SRT PRO (Skill) | Browser Studio (This Repo) | Descript | Premiere Pro Native | WhisperX (CLI) | Vrew |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Input** | Approved script + local media | Existing `.srt` | Raw media | Raw media + transcript | Raw media | Raw media + optional script |
| **Alignment Method** | Local phoneme forced alignment | Char-weighted split + rational frame math | Cloud ASR + sync | Speech-to-text + import | Local ASR + wav2vec2 | Cloud ASR + script import |
| **Script Fidelity** | Verbatim script lock | Preserves input text | Occasional jargon drift | Can lose sync on edits | ASR typos unless patched | Can drift under BGM |
| **Integer-Frame Snap** | 10 exact rates (`23.976–120 fps`) | 10 exact rates + NTSC scaling + `.fcpxml` | Arbitrary ms | Sequence timebase | Float ms | Arbitrary ms |
| **Media Upload** | None (local decoding) | None (browser JS) | Cloud upload | Local | Local (Python/CUDA) | Cloud upload |
| **Pricing** | `0.50 CNY`/run (24h free revisions) | Free | `$16–$24/mo` | `$22.99/mo` | Free (self-hosted) | Free tier + `$8–$20/mo` |
