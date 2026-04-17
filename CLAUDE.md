# fahad_projects — Task Router

## What this system is
This repo is the single source of truth for all work. Every task — SEO client work, personal projects, and any future domain — lives here. Claude handles routing automatically.

## At every session start (mandatory — triggers automatically on first message)
If this is the first message in the conversation (no prior history), run this routine automatically before responding — no trigger phrase needed from the user.

1. **Sync** — `cd /home/invoi/fahad_projects && git pull`
2. Read `./MEMORY.md` — understand what domains and active projects exist
3. Identify the task domain from what the user describes
4. Load `memory/MEMORY.md` and any relevant client/project files
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
| SEO, keyword research, clients, SERP, rankings, Google, Ahrefs, GKP, websites, traffic | `clients/` | `memory/MEMORY.md` |
| Personal projects, personal tools, personal websites, non-work tasks | `personal/` | `personal/memory/MEMORY.md` |
| Something that doesn't fit above | **Ask first** | — |

## File discipline — always follow
```
clients/[domain]/             ← client root (brief, onboarding form)
  [capability]/               ← deliverables for that capability
  memory/                     ← client-specific memory files
memory/                       ← cross-client rules (feedback, master reference, capabilities)
tools/[capability]/           ← shared scripts and instructions
global/                       ← global rules (CLAUDE.md, task_tracker.py)
```

- Deliverables → `clients/[domain]/[capability]/`
- Client memory → `clients/[domain]/memory/`
- Cross-client rules → `memory/`
- Root `memory/` → auto-loaded by Claude — write here AND at `.claude/projects/` path
- **Never create files outside this structure without asking**
- **Never create a new top-level domain folder without user approval**
- **All project deliverables must stay in the client folder** — reports, audit outputs, and any generated files go under `clients/[domain]/[capability]/`. Tool folders (`tools/[capability]/`) are for scripts and instructions only — never for client output.

## Adding a new domain
If a task doesn't fit any existing domain: "This looks like [X] work — should I create a new domain for it?" If yes, create: `[domain]/`, `[domain]/CLAUDE.md`, `[domain]/memory/MEMORY.md`.

## Auto-learning — always on, never needs to be asked
Every conversation is a learning opportunity. Without being asked:
- **Capability-level instructions** → save to that capability's memory file
- **Global rules** → save to `global/CLAUDE.md` and to root `memory/` if applicable
- **Project-specific learnings** → save to `clients/[domain]/memory/` AND mirror to `~/.claude/projects/-home-invoi-fahad-projects/memory/`
- After saving, briefly note what was saved — one line, not a full recap

## Memory — two-location rule
Every memory file must be written in two places:
1. `~/.claude/projects/-home-invoi-fahad-projects/memory/` — auto-loaded by Claude Code
2. `/home/invoi/fahad_projects/memory/` — visible inside the project folder

Client-specific memory also goes in `clients/[domain]/memory/`.
