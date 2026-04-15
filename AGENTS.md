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

# fahad_projects — Task Router

## What this system is
This repo is the single source of truth for all work. Every task — SEO client work, personal projects, and any future domain — lives here. Claude handles routing automatically.

## At every session start (mandatory — triggers automatically on first message)
If this is the first message in the conversation (no prior history), run this routine automatically before responding — no trigger phrase needed from the user.

1. **Sync** — `cd /home/invoi/fahad_projects && git pull`
2. Read `./MEMORY.md` — understand what domains and active projects exist
3. Identify the task domain from what the user describes
4. Load that domain's `[domain]/memory/MEMORY.md` and any relevant project files
5. If the domain is unclear → ask before doing anything or creating any file

## After every message where a file changed (mandatory)
After every memory update, deliverable change, or rule change — commit and push:
```bash
cd /home/invoi/fahad_projects && git add -A && git commit -m "specific description of what changed" && git push
```
GitHub (`fahadsupple/projects`) is the source of truth. Changes that aren't pushed don't exist on other machines.

## Domain routing table

| What the user is working on | Folder | Memory to load |
|---|---|---|
| SEO, keyword research, clients, SERP, rankings, Google, Ahrefs, GKP, websites, traffic | `seo/` | `seo/memory/MEMORY.md` |
| Personal projects, personal tools, personal websites, non-work tasks | `personal/` | `personal/memory/MEMORY.md` |
| Something that doesn't fit above | **Ask first** | — |

## File discipline — always follow
```
seo/
  clients/[domain]/           ← client root (brief, onboarding form)
    [capability]/             ← deliverables for that capability
    memory/                   ← client-specific memory files
  memory/                     ← cross-client rules only (feedback, master reference)
  tools/[capability]/         ← shared scripts and instructions

memory/                       ← root memory (auto-loaded by Claude)
global/                       ← global rules (CLAUDE.md, task_tracker.py)
```

- Deliverables → `seo/clients/[domain]/[capability]/`
- Client memory → `seo/clients/[domain]/memory/`
- Cross-client rules → `seo/memory/`
- Root `memory/` → auto-loaded by Claude — write here AND at `.claude/projects/` path
- **Never create files outside this structure without asking**
- **Never create a new top-level domain folder without user approval**
- **All project deliverables must stay in the client folder** — reports, audit outputs, and any generated files go under `seo/clients/[domain]/[capability]/`. Tool folders (`seo/tools/[capability]/`) are for scripts and instructions only — never for client output.

## Adding a new domain
If a task doesn't fit any existing domain: "This looks like [X] work — should I create a new domain for it?" If yes, create: `[domain]/`, `[domain]/CLAUDE.md`, `[domain]/memory/MEMORY.md`.

## Auto-learning — always on, never needs to be asked
Every conversation is a learning opportunity. Without being asked:
- **Capability-level instructions** → save to that capability's memory file
- **Global rules** → save to `global/CLAUDE.md` and to root `memory/` if applicable
- **Project-specific learnings** → save to `seo/clients/[domain]/memory/` AND mirror to `~/.claude/projects/-home-invoi-fahad-projects/memory/`
- After saving, briefly note what was saved — one line, not a full recap

## Memory — two-location rule
Every memory file must be written in two places:
1. `~/.claude/projects/-home-invoi-fahad-projects/memory/` — auto-loaded by Claude Code
2. `/home/invoi/fahad_projects/memory/` — visible inside the project folder

Client-specific memory also goes in `seo/clients/[domain]/memory/`.
