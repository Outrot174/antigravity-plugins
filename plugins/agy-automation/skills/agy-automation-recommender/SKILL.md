---
name: agy-automation-recommender
description: Analyze a codebase and recommend tailored Antigravity (AGY v2) automations (skills, project rules, hooks, MCP servers, agy-daemon background tasks, and ADB workflows). Use when user asks for automation recommendations, wants to optimize their Antigravity setup, asks how to structure agents for a project, or wants to automate recurring tasks.
tools: Read, Glob, Grep, Bash
---

# Antigravity Automation Recommender (AGY v2)

Analyze project codebase patterns to recommend tailored Antigravity (AGY v2) automations across all extensibility options.

**This skill is read-only.** It analyzes the codebase and outputs concrete recommendations tailored to Antigravity's native Android runtime, user rules, and agent hierarchy.

## Output Guidelines

- **Recommend 1-2 per category**: Keep recommendations focused, high-signal, and immediately actionable.
- **Tailor to Android & Antigravity**: Suggest native `agy-daemon` jobs, `.agents/skills/`, `.agents/rules/`, and elevated `adb shell` workflows when relevant.
- **Storage Isolation Compliance**: Always ensure suggested paths respect `/storage/emulated/0/Antigravity/` and native interpreter execution (`bash`, `python`, `sh`).

## Automation Types Overview

| Type | Best For | Location / Command |
|------|----------|-------------------|
| **Project Rules** | Enforcing code style, architectural constraints, and safety guidelines | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` |
| **Skills** | Repeatable procedures, domain expertise, and multi-step workflows | `.agents/skills/<name>/SKILL.md` or global `~/.gemini/config/plugins/<name>/skills/` |
| **Daemon Tasks** | Background watchers, periodic health checks, cron jobs, low battery alerts | `agy-daemon task add ...` |
| **Status Alerts** | Android notification bar progress and alerts | `agy-notify post -t "..." -m "..."` |
| **MCP Servers** | Tool integrations (GitHub, databases, web search, custom APIs) | `~/.gemini/config/mcp_config.json` |
| **Elevated ADB** | Android package management, activity launch, logcat inspection | `adb shell "<cmd>"` |

## Workflow

### Phase 1: Codebase Analysis

Detect project profile and tools:
```bash
# Detect project type
ls -la package.json pyproject.toml Cargo.toml go.mod build.gradle* app/ 2>/dev/null
# Check Android specifics
ls -la AndroidManifest.xml app/src/main/AndroidManifest.xml 2>/dev/null
# Check git and existing rules
ls -la .agents/ .git/ AGENTS.md GEMINI.md 2>/dev/null
```

### Phase 2: Category Recommendations

#### A. Project Rules (`.agents/rules/*.md` or `AGENTS.md`)
- **Android / Kotlin**: Recommend rules for coroutine dispatchers, Jetpack Compose best practices, and `-march=armv8-a` native flags.
- **Python / Node**: Recommend rules for clean imports, type annotations, and shebang path fixes (`agy-fix-paths`).
- **Safety / Storage**: Enforce shared storage execution rules (never run `./script.sh` on `noexec` mounts; use `bash script.sh`).

#### B. Skills (`.agents/skills/<name>/SKILL.md`)
- **Android Builds**: Skill for running Gradle builds and installing output APK via `adb shell pm install -r`.
- **API / Backend**: Skill for testing endpoints via `curl` and validating schemas.
- **3D / Graphics**: Skill for procedural Three.js / WebGL / OBJ assets.

#### C. Background Tasks (`agy-daemon`)
- **File Watcher**: `agy-daemon task add --name "Build on Change" --watch-file "build.gradle" --command "..."`
- **Git / PR Watcher**: `agy-daemon task add --name "PR Watch" --github-pr "owner/repo" --interval 10m --command "..."`
- **Battery Watcher**: `agy-daemon task add --name "Battery Alert" --battery-below 15 --command "agy-notify post -t 'Low Battery' -m 'Save your work'"`

#### D. MCP Servers (`mcp_config.json`)
- **GitHub**: `@modelcontextprotocol/server-github` via native `npx -y`.
- **Databases**: SQLite or PostgreSQL MCP server for backend inspection.

### Phase 3: Deliver Report
Provide a clean markdown report showing exact configurations, file paths, and copy-pasteable commands.
