# Multilingual SRT PRO (多语种SRT PRO：帧级字幕精制)

[**English**](https://bbllhenhj.github.io/multilingual-srt-pro-docs/en/) | [**简体中文**](./README.md) | [**Free Online 9:16 SRT Reframe & FCPXML Web Studio (No Login)**](https://bbllhenhj.github.io/multilingual-srt-pro-docs/en/#studio)

> **Multilingual SRT PRO** is an on-device AI Agent Skill (Alipay AIPay PAYATHON 2026 Machine Pay Track entry) built for YouTube/Shorts creators, documentary editors, and cross-border short-drama localization teams. When you already have an **approved narration script**, it performs **100% local word-level acoustic forced alignment** for zero homophone typos, applies **breath-pause & syntax line-breaking across 27 locales**, and snaps every cue to **10 exact NLE frame rates (23.976–120 fps)** with zero video uploads.

- **Free Browser Companion Utility (Route B)**: [SRT Reframe & Frame-Rate Studio](https://bbllhenhj.github.io/multilingual-srt-pro-docs/en/#studio) — Convert existing `16:9` two-line `.srt` files into `9:16` single-line vertical captions (with EN/DE/FR/ES anti-orphan preposition binding), fix `23.976 ↔ 24` / `29.97 ↔ 30 fps` NTSC pull-up drift, audit `>20 CPS` cues, and export Final Cut Pro `.fcpxml` v1.10 connected Basic Titles 100% in browser memory.
- **Full On-Device AI Agent Skill (Route A — Official Download)**: https://aipay.alipay.com/community?view=work%2FHKWI_f70adb9f65ce499d8abf3ebd65effdef (Visit the official Alipay AIPay work page and click **"下载 Skill 包" / Download Skill Pack** to install into Claude Code, Cursor, or Antigravity `skills/`).
- **Entity Disambiguation**: `Multilingual SRT PRO` (`multilingual-srt-pro`) is a local `SKILL.md` AI Agent Skill for script-locked forced alignment and NLE frame quantization. It is **unaffiliated** with the standalone GUI desktop app `Videosrt Pro`.

---

## Micro-Pricing & 24-Hour Free Revision Policy

- **Pay-per-use micro-billing (No monthly subscription)**: **`0.50 CNY` (~`$0.07 USD`) per run** via Alipay AIPay Machine Pay (Nov 2026 promotional baseline; live rate displayed on the official work page).
- **24-Hour Free Revision Guarantee**: **Re-using EITHER the same script text OR the same audio file within 24 hours incurs zero repeat charges:**
  1. **Same Audio + Updated Script (Free for 24h)**: Fix wording tweaks, translation polish, capitalization, or punctuation against the same audio track;
  2. **Same Script + Re-Recorded Audio (Free for 24h)**: Swap in a new voiceover take, adjusted pacing, or alternate voice actor while keeping your approved script;
  3. **Unlimited Layout & Frame-Rate Exports (Free for 24h)**: Switch freely between `16:9` two-line landscape captions and `9:16` single-line vertical captions, or re-export across `23.976`, `24`, `25`, `29.97`, `30`, `59.94`, and `60 fps`.
- **No Alipay Account?** Overseas creators without Alipay can use the [Browser Reframe & FCPXML Studio](https://bbllhenhj.github.io/multilingual-srt-pro-docs/en/#studio) and [`scripts/verify_srt_frame_grid.py`](./scripts/verify_srt_frame_grid.py) 100% free, and [join our International Card / Batch Pass waitlist via GitHub Issues](https://github.com/bbllhenhj/multilingual-srt-pro-docs/issues/new?title=International+Card+%2F+Stripe+Batch+Pass+Request).

---

## 2026 Subtitle Alignment & NLE Formatting Matrix

| Dimension | Multilingual SRT PRO (Full Skill) | Free Browser Studio (In-Repo) | Descript | Premiere Pro Native | WhisperX (CLI) | Vrew |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Input Required** | **Plain approved script + raw video/audio** | Existing `.srt` file | Raw video/audio | Raw video + transcript | Raw video/audio | Raw video + optional script |
| **Core Mechanism** | **Local phoneme forced alignment + breath/syntax solver** | Proportional char-weighted split + rational frame math | Cloud ASR + script sync | Speech-to-text + Import Corrected Transcript | Local ASR + wav2vec2 | Cloud ASR + script import |
| **Script Fidelity** | **100% verbatim (zero homophone typos, 8,000+ words)** | Preserves existing SRT text | Occasional jargon drift | Loses sync on heavy script edits | ASR typos unless patched | Drifts under BGM / fast speech |
| **NLE Integer-Frame Snap** | **10 exact rates (`23.976–120 fps`), zero 1-frame flash** | **10 exact rates + NTSC drift scaling + `.fcpxml`** | Arbitrary ms | Sequence timebase; SRT rounds ms | Unquantized float ms | Arbitrary ms |
| **27-Locale Syntax Wrap** | **0.77 EN width ratio; zero DE/EN orphan words; RTL** | EN/DE/FR/ES preposition binding for 9:16 | Char-count wrap | Fixed char limit | Acoustic chunks | Optimized for KO/JA |
| **Media Privacy** | **100% local decoding (0 bytes uploaded)** | **100% local browser JS** | Cloud upload required | Local (Creative Cloud) | Local (requires Python/CUDA) | Cloud audio upload |
| **Pricing** | **`0.50 CNY` (~`$0.07`)/run · 24h free revisions** | **100% Free** | `$16–$24 / mo` | `$22.99 / mo` | Free (self-hosted GPU) | Free tier + `$8–$20 / mo` |

---

## Verified Benchmark `.srt` Samples & Frame Verifier

All files in [`samples/`](./samples/) are quantized to exact integer frame boundaries (`round(frame * 1000 / fps)`):

- [`samples/01_cn_24fps_landscape_16x9.srt`](./samples/01_cn_24fps_landscape_16x9.srt) — Simplified Chinese `24fps` 16:9 two-line (`Frame 6: 00:00,250` -> `Frame 53: 00:02,208` -> `Frame 132: 00:05,500`)
- [`samples/02_cn_60fps_portrait_9x16.srt`](./samples/02_cn_60fps_portrait_9x16.srt) — Simplified Chinese `60fps` 9:16 vertical single-line (`<=13` chars)
- [`samples/03_en_30fps_balanced_ratio_077.srt`](./samples/03_en_30fps_balanced_ratio_077.srt) — English `30fps` 16:9 balanced syntax wrap (`0.77` measured short/long line width ratio)
- [`samples/04_de_24fps_zero_orphan.srt`](./samples/04_de_24fps_zero_orphan.srt) — German `24fps` clause-frame protection (zero orphan words)

Verify any `.srt` against NLE frame grids offline with zero dependencies:
```bash
python scripts/verify_srt_frame_grid.py samples/03_en_30fps_balanced_ratio_077.srt --fps 30
```
