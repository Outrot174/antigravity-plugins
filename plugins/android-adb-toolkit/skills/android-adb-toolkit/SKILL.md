---
name: android-adb-toolkit
description: Elevated Android diagnostics, package management, logcat crash analysis, and activity control via native loopback ADB (uid=2000). Use when developing Android apps, installing/testing APKs, debugging runtime exceptions, checking battery/memory, or accessing protected application directories.
tools: Read, Glob, Grep, Bash
---

# Android ADB Development & Diagnostics Toolkit

Autonomous Android management utilizing Antigravity's native elevated loopback ADB bridge (`uid=2000(shell)` at `127.0.0.1:44875`).

## Core Directives

1. **Native Invocation**:
   Execute commands directly via `adb shell "<command>"`. Never invoke Shizuku (it is decommissioned).
2. **Elevated Access**:
   Elevated operations run under `uid=2000(shell)`, granting access to inspect third-party packages, system properties, and protected paths (`/storage/emulated/0/Android/data`).
3. **No Blind ADB Taps**:
   Never run repetitive blind `input tap` loops to navigate interfaces. Use targeted `am start` intent triggers or UI hierarchy dumps (`uiautomator dump`) instead.

---

## Workflows & Common Operations

### 1. Crash Investigation & Filtered Logcat
Always pull structured, scoped logs instead of dumping millions of lines:

```bash
# Capture recent crashes and fatal exceptions
adb shell "logcat -d -b crash -t 100"

# Scoped logcat for specific tag or package errors
adb shell "logcat -d -t 150 *:E"

# Follow logs for specific package in background
adb shell "logcat -d -t 200 | grep -E '(AndroidRuntime|FATAL|CryptoHunter|grafik)'"
```

### 2. APK & Package Management
```bash
# List all installed 3rd-party applications
adb shell "pm list packages -3"

# Install or reinstall an APK without losing app data
adb shell "pm install -r \"/storage/emulated/0/Antigravity/программы/.../app-debug.apk\""

# Get package installation path and APK details
adb shell "pm path <package_name>"

# Clear app data and cache (reset state)
adb shell "pm clear <package_name>"

# Uninstall application
adb shell "pm uninstall <package_name>"
```

### 3. Activity & Component Lifecycle
```bash
# Start an explicit activity
adb shell "am start -n <package_name>/<activity_path>"

# Start an activity with intent extras
adb shell "am start -n <package_name>/.MainActivity -e 'debug_mode' 'true'"

# Force stop application
adb shell "am force-stop <package_name>"

# Inspect running tasks and top resumed activity
adb shell "dumpsys activity activities | grep -E 'ResumedActivity|mFocusedApp'"
```

### 4. Protected Storage Access
Inspect application-private directories inaccessible to standard app sandbox:
```bash
# Inspect app data files
adb shell "ls -la /storage/emulated/0/Android/data/<package_name>/files"

# Copy diagnostic data to user workspace
adb shell "cp -r /storage/emulated/0/Android/data/<package_name>/files /storage/emulated/0/Antigravity/песочница/"
```

### 5. Diagnostics & Resource Profiling
```bash
# Memory footprint analysis
adb shell "dumpsys meminfo <package_name>"

# Battery status and power consumption
adb shell "dumpsys battery"

# System properties (model, OS build, ABI)
adb shell "getprop ro.build.version.release"
adb shell "getprop ro.product.model"
```
