---
name: python-artisan
description: Design, structure, and optimize native Python CLI tools and scripts for Android AGY v2. Covers zero-dependency architectures, Shebang management (agy-fix-paths), execution workarounds on noexec shared storage, and integration with Google AI Studio / Gemini APIs. Use when creating or refactoring Python CLIs, writing standalone scripts, or automating workflows.
tools: Read, Glob, Grep, Bash
---

# Python Artisan (AGY v2 on Android)

Architecture and development standards for high-performance, portable Python scripts and CLI utilities running in native Android userspace.

## Core Directives for Android

1. **Shared Storage `noexec` Rule**:
   - `/storage/emulated/0/...` is mounted with `noexec`. Direct execution (`./script.py`) fails with `Permission denied (exit code 126)`.
   - **Always invoke with explicit interpreter**: `python script.py`.
   - To create global CLI commands, place executable launcher scripts in `$PREFIX/bin/` (e.g. `$PREFIX/bin/my-tool`) or install entrypoints via pip.
2. **Post-Install Shebang Fixes**:
   - After installing Python scripts globally via `pip` or setup tools, always execute:
     ```bash
     agy-fix-paths
     ```
   - This patches hardcoded desktop shebangs (`#!/usr/bin/python`) to Antigravity's userspace binary (`/data/user/0/com.agy/files/usr/bin/python`).
3. **Storage Isolation**:
   - Save all generated assets strictly inside `/storage/emulated/0/Antigravity/` designated subfolders (`программы/`, `видео/`, `изображения/`, `песочница/`).

---

## 1. Zero-Dependency Portable CLI Architecture

Design utilities relying primarily on Python's rich standard library to ensure instant execution without virtual environment overhead:

```python
#!/usr/bin/env python3
"""Modular, zero-dependency CLI pattern for Antigravity AGY v2."""

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Optional


@dataclass
class AppConfig:
  api_key: Optional[str]
  output_dir: Path
  verbose: bool = False


def load_google_ai_config() -> Optional[str]:
  """Read active Google AI Studio API key from standard Antigravity config."""
  cfg_path = Path.home() / ".gemini/config/google_ai.json"
  if cfg_path.exists():
    try:
      with open(cfg_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("api_key") or data.get("google_api_key")
    except Exception:
      pass
  return None


def main() -> int:
  parser = argparse.ArgumentParser(
      description="Portable CLI tool for Antigravity."
  )
  parser.add_argument("command", choices=["run", "status", "clean"])
  parser.add_argument("-v", "--verbose", action="store_true")
  parser.add_argument(
      "-o",
      "--output",
      default="/storage/emulated/0/Antigravity/песочница",
      type=Path,
  )

  args = parser.parse_args()
  config = AppConfig(
      api_key=load_google_ai_config(),
      output_dir=args.output,
      verbose=args.verbose,
  )

  if args.command == "status":
    print(
        f"[OK] Python {sys.version.split()[0]} | Config loaded | Key:"
        f" {'found' if config.api_key else 'missing'}"
    )
  return 0


if __name__ == "__main__":
  sys.exit(main())
```

---

## 2. Google AI Studio & Gemini API Integration

When building tools like `google_nano_banana` or `google_video_generator`:
- Access configured keys via `~/.gemini/config/google_ai.json`.
- Prefer native `urllib.request` for minimal payloads or the modern `google-genai` SDK for complex multimodal generation.
- Stream chunks cleanly without buffering massive objects in memory.
- For long-running generation jobs, schedule with `agy-daemon` and trigger Android notifications via `agy-notify post`.

---

## 3. High-Performance Concurrency Pattern

Use standard library `concurrent.futures.ThreadPoolExecutor` for parallel network or I/O operations on the Snapdragon 8 Elite:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def process_item(item_id: int):
  # Perform task
  return item_id, True


def run_batch(items):
  with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(process_item, i): i for i in items}
    for f in as_completed(futures):
      item_id, success = f.result()
      print(f"Processed item {item_id}: {success}")
```
