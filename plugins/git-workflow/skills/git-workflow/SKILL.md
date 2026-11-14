---
name: git-workflow
description: Standardized Git operations, Conventional Commits, changelog creation, Android shared-storage safe directory configuration, and clean branch management. Use when preparing git commits, resolving dubious ownership on Android, creating release tags, or managing repository remotes.
tools: Read, Glob, Grep, Bash
---

# Git Workflow & Conventional Commits (Android AGY v2)

Streamlined Git operations tailored for the Android userspace environment and shared storage partitions (`/storage/emulated/0/...`).

## Android Storage Requirements

Android mounts shared storage with specific user IDs (`media_rw`, `u0_a...`). Git will throw `fatal: detected dubious ownership in repository` unless properly configured:

```bash
# Required environment setup before running git on shared storage:
export GIT_CONFIG_NOSYSTEM=1
git config --global --add safe.directory "<path_to_repo>"
```

---

## 1. Conventional Commits Standard

Format: `<type>(<scope>): <subject>`

### Commit Types:
- `feat`: A new user-facing feature or capability.
- `fix`: A bug fix.
- `refactor`: Code change that neither fixes a bug nor adds a feature.
- `docs`: Documentation updates only.
- `style`: Formatting, missing semicolons, whitespace changes.
- `perf`: Code change that improves performance.
- `test`: Adding or correcting tests.
- `chore`: Build tasks, dependency updates, package configuration.

### Rules:
1. Subject line in imperative mood ("add", not "added" or "adds").
2. Max 72 characters in subject line.
3. Don't end subject line with a period.

---

## 2. Standard Workflow Commands

### Status & Staging
```bash
# Check status cleanly
git status -s

# Stage surgical files
git add path/to/file1 path/to/file2

# Review staged diff
git diff --cached
```

### Commit & Push
```bash
# Commit with conventional format
git commit -m "feat(module): add structured logcat streaming"

# Safe push to remote
git push origin <branch_name>
```

### Releases & Tags
```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release v1.0.0: initial public version"

# Push tag to GitHub
git push origin v1.0.0
```
