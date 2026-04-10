#!/usr/bin/env python3
"""
Global task tracker for Claude Code.
Persists tasks across sessions so crashed/incomplete work is resumed automatically.

State file: ~/.claude/active_tasks.json
Hook use:   python3 ~/.claude/task_tracker.py session_start   (called by SessionStart hook)
CLI use:    python3 ~/.claude/task_tracker.py add "description" [--project /path]
            python3 ~/.claude/task_tracker.py done <id>
            python3 ~/.claude/task_tracker.py list
            python3 ~/.claude/task_tracker.py clear-done
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

STATE_FILE = Path.home() / ".claude" / "active_tasks.json"


# ── state I/O ──────────────────────────────────────────────────────────────

def load() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {"tasks": []}


def save(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


# ── commands ───────────────────────────────────────────────────────────────

def cmd_add(description: str, project: str | None = None):
    state = load()
    task = {
        "id": str(uuid4())[:8],
        "description": description,
        "project": project or os.environ.get("PWD", os.getcwd()),
        "status": "running",
        "created_at": now_iso(),
        "completed_at": None,
    }
    state["tasks"].append(task)
    save(state)
    print(f"[task] added: {task['id']} — {description}")


def cmd_done(task_id: str):
    state = load()
    matched = False
    for t in state["tasks"]:
        if t["id"] == task_id or t["id"].startswith(task_id):
            t["status"] = "done"
            t["completed_at"] = now_iso()
            matched = True
            print(f"[task] done: {t['id']} — {t['description']}")
            break
    if not matched:
        print(f"[task] not found: {task_id}", file=sys.stderr)
        sys.exit(1)
    save(state)


def cmd_list():
    state = load()
    tasks = state["tasks"]
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        status = "✓" if t["status"] == "done" else "⟳"
        print(f"  [{status}] {t['id']}  {t['description'][:80]}  ({t['project']})")


def cmd_clear_done():
    state = load()
    before = len(state["tasks"])
    state["tasks"] = [t for t in state["tasks"] if t["status"] != "done"]
    after = len(state["tasks"])
    save(state)
    print(f"[task] removed {before - after} completed task(s)")


def cmd_session_start():
    """
    Called by the SessionStart hook.
    Reads incomplete tasks and outputs JSON with additionalContext
    so Claude automatically picks up where it left off.
    """
    state = load()
    incomplete = [t for t in state["tasks"] if t["status"] != "done"]

    if not incomplete:
        # No output needed — silent
        return

    lines = [
        "⚠️  PENDING TASKS FROM A PREVIOUS SESSION:",
        "",
        "The following tasks were started but never marked complete (session may have crashed).",
        "Please re-run each one from scratch in this session, then mark them done.",
        "",
    ]
    for t in incomplete:
        lines.append(f'• [{t["id"]}] {t["description"]}')
        lines.append(f'  Project: {t["project"]}')
        lines.append(f'  Started: {t["created_at"]}')
        lines.append("")
    lines += [
        "When you finish each task, run:",
        "  python3 ~/.claude/task_tracker.py done <id>",
        "",
        "To see all tracked tasks:",
        "  python3 ~/.claude/task_tracker.py list",
    ]

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "\n".join(lines),
        }
    }
    print(json.dumps(output))


# ── entrypoint ─────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0]

    if cmd == "session_start":
        cmd_session_start()

    elif cmd == "add":
        if len(args) < 2:
            print("Usage: task_tracker.py add <description> [--project /path]")
            sys.exit(1)
        description = args[1]
        project = None
        if "--project" in args:
            idx = args.index("--project")
            project = args[idx + 1] if idx + 1 < len(args) else None
        cmd_add(description, project)

    elif cmd == "done":
        if len(args) < 2:
            print("Usage: task_tracker.py done <id>")
            sys.exit(1)
        cmd_done(args[1])

    elif cmd == "list":
        cmd_list()

    elif cmd == "clear-done":
        cmd_clear_done()

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
