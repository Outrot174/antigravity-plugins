---
name: token-efficiency-craft
description: Maximize context window efficiency and eliminate wasted tokens. Enforces terminal output pruning, surgical line-range file inspection, differential edits, observation masking, and zero-boilerplate communication. Use when dealing with large codebases, long tasks, noisy logs, or optimizing API costs.
tools: Read, Glob, Grep, Bash
---

# Token Efficiency & Context Compression (AGY v2)

Battle-tested guidelines and patterns to minimize token usage, prevent context window exhaustion, and speed up agent execution.

---

## 1. Terminal Output Pruning (Anti-Bloat Rules)

Never allow shell commands to flood the context with thousands of unstructured lines.

### 🚫 Prohibited (Context Killers) vs. ✅ Required (Pruned):

| Anti-Pattern (Massive Token Waste) | Token-Lean Alternative | Why |
| :--- | :--- | :--- |
| `adb shell logcat` | `adb shell "logcat -d -t 50 *:E"` | Reduces 50,000 lines down to the last 50 error lines. |
| `git diff` | `git diff --stat` or `git diff -U2 <file>` | Gives immediate high-signal delta without thousands of diff lines. |
| `grep -rn "pattern" .` | `grep -rn "pattern" --exclude-dir={.git,node_modules,build,.gradle} .` | Prevents dumping minified bundles, lockfiles, and binaries into context. |
| `cat build.log` | `grep -E -C 2 "(FAILED|ERROR|Exception)" build.log \| head -n 40` | Isolates the actual failure in 40 lines. |
| `find .` | `find . -maxdepth 3 -not -path '*/.*'` | Restricts traversal depth and ignores hidden cache folders. |

---

## 2. File Reading Discipline (Progressive Disclosure)

- **Never read entire large files**:
  When inspecting an existing 500+ line file, use `view_file` with explicit line bounds:
  ```json
  {
    "AbsolutePath": "/path/to/file.kt",
    "StartLine": 45,
    "EndLine": 95
  }
  ```
- **Structure First, Implementation Second**:
  Inspect class signatures and method headers before reading method bodies.
- **Ignore Lockfiles**:
  Never dump `package-lock.json`, `Cargo.lock`, or `yarn.lock` into the prompt. Query package versions via `npm info <pkg>` or targeted `grep` in `package.json`.

---

## 3. Surgical Edits (Zero Overwrite Waste)

- **Prefer `replace_file_content`**:
  Replacing a single 5-line block consumes <50 tokens. Overwriting a 600-line file with `write_to_file` burns >2,500 tokens on every single edit.
- **Narrow Diff Bounds**:
  Set `StartLine` and `EndLine` tightly around the target block (3-5 lines of context is plenty; do not wrap 100 unchanged lines).

---

## 4. Response Compression & Zero-Boilerplate

- **Eliminate Conversational Echo**:
  Do not repeat back the user's question, do not write introductory filler ("Sure, I would be happy to help you with..."), and do not re-explain basic language syntax.
- **No Double-Printing**:
  When an artifact or file is created, point the user to the clickable file link:
  `[MainActivity.kt](file:///path/to/MainActivity.kt)`
  Do not re-paste the entire contents in markdown prose.
- **Structured Diffs**:
  When reporting changes, provide a concise table of modified files and a 1-sentence rationale.

---

## 5. Persistent Memory Offloading

Offload long-term facts, architecture decisions, and environment parameters into the native MCP memory server (`memory-mcp-server`) instead of re-injecting huge text files into every subsequent turn.
