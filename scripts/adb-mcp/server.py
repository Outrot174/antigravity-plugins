#!/data/user/0/com.agy/files/usr/bin/python
"""
Native Android ADB MCP Server for Antigravity AGY v2.
Provides elevated device control, logcat crash analysis, package management,
and system diagnostics over standard Model Context Protocol (JSON-RPC stdio).
Zero-dependency: uses only standard Python libraries.
"""

import sys
import json
import subprocess
import os

ADB_BIN = "/data/user/0/com.agy/files/usr/bin/adb"
if not os.path.isfile(ADB_BIN):
    ADB_BIN = "adb"

def run_adb(args):
    try:
        cmd = [ADB_BIN] + args
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
        out = res.stdout.strip()
        err = res.stderr.strip()
        if res.returncode != 0:
            return f"Error (code {res.returncode}): {err if err else out}"
        return out if out else "(No output)"
    except Exception as e:
        return f"Execution error: {str(e)}"

TOOLS = [
    {
        "name": "adb_crash_analyzer",
        "description": "Analyze recent Android crashes, fatal exceptions, ANRs, and native SIGSEGV from logcat crash buffer.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "package_name": {
                    "type": "string",
                    "description": "Optional package name to filter crashes (e.g. com.example.app)"
                },
                "lines": {
                    "type": "integer",
                    "description": "Number of crash buffer lines to retrieve (default: 80)"
                }
            }
        }
    },
    {
        "name": "adb_device_info",
        "description": "Get real-time device health, model, battery level, Android version, thermal status, and RAM usage.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "adb_app_control",
        "description": "Control Android application lifecycle: start activity, force stop, clear app cache/data, or list packages.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["start", "stop", "clear", "list"],
                    "description": "Action to perform on the application"
                },
                "package_name": {
                    "type": "string",
                    "description": "Target application package name (e.g. com.agy)"
                },
                "activity_name": {
                    "type": "string",
                    "description": "Specific activity component for 'start' (optional, e.g. .MainActivity)"
                }
            },
            "required": ["action"]
        }
    },
    {
        "name": "adb_shell",
        "description": "Execute an elevated command directly inside ADB shell (uid=2000) for system inspection.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "Shell command to execute via ADB (e.g. 'dumpsys package com.agy')"
                }
            },
            "required": ["command"]
        }
    }
]

def handle_call(name, args):
    if name == "adb_crash_analyzer":
        lines = args.get("lines", 80)
        pkg = args.get("package_name")
        out = run_adb(["shell", f"logcat -b crash -d -t {lines}"])
        if pkg:
            filtered = [l for l in out.splitlines() if pkg in l]
            return "\n".join(filtered) if filtered else f"No crashes matching '{pkg}' found in last {lines} lines.\n\nFull buffer tail:\n{out[:1000]}"
        return out

    elif name == "adb_device_info":
        model = run_adb(["shell", "getprop ro.product.model"])
        brand = run_adb(["shell", "getprop ro.product.brand"])
        android_v = run_adb(["shell", "getprop ro.build.version.release"])
        sdk = run_adb(["shell", "getprop ro.build.version.sdk"])
        battery = run_adb(["shell", "dumpsys battery | grep level"])
        mem = run_adb(["shell", "cat /proc/meminfo | head -n 3"])
        return f"Device: {brand} {model}\nAndroid: {android_v} (API {sdk})\nBattery: {battery.strip()}\nMemory:\n{mem.strip()}"

    elif name == "adb_app_control":
        action = args.get("action")
        pkg = args.get("package_name")
        act = args.get("activity_name", "")
        if action == "list":
            return run_adb(["shell", "pm list packages -3 | head -n 50"])
        if not pkg:
            return "Error: package_name required for start/stop/clear."
        if action == "start":
            target = f"{pkg}/{act}" if act else pkg
            return run_adb(["shell", f"am start -n {target}"])
        elif action == "stop":
            return run_adb(["shell", f"am force-stop {pkg}"])
        elif action == "clear":
            return run_adb(["shell", f"pm clear {pkg}"])
        return f"Unknown action: {action}"

    elif name == "adb_shell":
        cmd = args.get("command", "")
        return run_adb(["shell", cmd])

    return f"Unknown tool: {name}"

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {"listChanged": False}
                    },
                    "serverInfo": {
                        "name": "android-adb-mcp",
                        "version": "1.0.0"
                    }
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "notifications/initialized":
            pass

        elif method == "ping":
            res = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": TOOLS
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            output_text = handle_call(tool_name, tool_args)
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": output_text
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif msg_id is not None:
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {method} not found"
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
