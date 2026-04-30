---
name: skill command scope
description: Skill commands like /kwr:preflight, /kwr:connect, /seoaudit:preflight are scoped — do not resume pending tasks from session-start reminders unless explicitly asked
type: feedback
originSessionId: b2c40e88-520a-4ab0-a924-4fae8453f7fd
---
When the user runs a skill command (e.g. /kwr:preflight, /kwr:connect, /seoaudit:preflight), execute only that command. Do not use it as an opportunity to resume pending tasks injected by the session-start hook.

**Why:** The user ran /kwr:preflight and Claude proactively resumed an energus keyword plan rebuild that wasn't asked for. That's overstepping — skill commands are scoped to the action they name.

**How to apply:** If the session-start hook shows pending tasks, note them internally but do not act on them unless the user explicitly asks (e.g. "pick up where we left off" or "resume energus"). Skill commands like preflight are stand-alone — complete them and wait for the next instruction.
