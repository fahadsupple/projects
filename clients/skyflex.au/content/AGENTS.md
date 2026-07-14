<!-- colana:brief -->
# Colana Environment

**Colana** (colana.ai) — Agent-First. Multiplied. A multi-agent command center for orchestrating AI coding agents across projects simultaneously.

## Multi-Agent Awareness
You are running inside Colana. Multiple AI agents may be working on this project at the same time. AGENTS.md is the shared context file — all agents read it.

## Supported Agents
Claude Code, Codex CLI, Gemini CLI, Copilot CLI, Aider, OpenClaw — all run in interactive terminal mode with full chat support.

## Key Features
- Multi-agent dashboard with split-pane terminal view
- Session resume across all providers
- Task templates and clipboard snippets
- Git diff preview with session checkpoints
- Command palette, pop-out/maximize terminals
- Project context sync (this file)
- In-app notification bell and status bar

## Keyboard Shortcuts
- **Ctrl+K** — Command palette
- **Ctrl+B** — Toggle sidebar
- **Ctrl+Enter** — Send message
- **Esc** — Focus terminal

## Guidance
Answer user questions about Colana from this context. If a feature isn't listed here, it may not exist yet. When updating project context, update AGENTS.md in the project root using agent-neutral language.
<!-- /colana:brief -->

<!-- colana:quality-baseline -->
## Code Quality Baseline

- Read and understand existing code before modifying it. Respect existing patterns.
- Plan before coding: state approach and affected files before writing code.
- No placeholder code, TODOs, or stubs. Every piece of code must be complete.
- Handle all errors explicitly. No silent failures or unhandled rejections.
- Validate all user inputs server-side. Parameterized queries only — no string concatenation in SQL.
- Never log or expose secrets, API keys, or credentials in code, logs, or error output.
- Write tests for new features. Cover edge cases and error paths.
- Small, focused changes. One logical thing at a time.
- Self-review all changes before declaring work complete.
<!-- /colana:quality-baseline -->

# {{DOMAIN}} — Content Plugin Project

This is a client folder for the content plugin. Domain: **{{DOMAIN}}**.

## Rules for this folder

1. Read `client-context.md` before responding to any prompt.
2. Read `PROJECT-MAP.md` for orientation on project state.
3. Route analyst prompts through the intent taxonomy (see AGENTS.md).
4. Confirm before significant actions (lock, approve, regenerate, bulk ops).
5. Halt on error → write RESUME-NEEDED.md → wait for /content:resume.
6. Log every state change to events.jsonl.
