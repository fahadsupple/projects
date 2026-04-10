# AgentOps — Task Router

## What this system is
This repo is the single source of truth for all work across all machines. Every task — SEO client work, personal projects, and any future domain — lives here. You never need to think about where things go. Claude handles routing automatically.

## At every session start (mandatory — triggers automatically on first message)
If this is the first message in the conversation (no prior history), run this routine automatically before responding — no trigger phrase needed from the user.

1. **Sync safely** — commit any uncommitted local changes first, then pull. Never overwrite local.
2. Read `./MEMORY.md` — understand what domains and active projects exist
3. Identify the task domain from what the user describes
4. Load that domain's `[domain]/memory/MEMORY.md` and any relevant project files
5. If the domain is unclear → ask before doing anything or creating any file

## After any update (mandatory)
After every memory update, deliverable change, or rule change — commit and push:
```bash
git -C ~/AgentOps add -A
git -C ~/AgentOps commit -m "specific description of what changed"
git -C ~/AgentOps push
```
GitHub is the source of truth. Changes that aren't pushed don't exist on other machines.

## Domain routing table

| What the user is working on | Folder | Memory to load |
|---|---|---|
| SEO, keyword research, clients, SERP, rankings, Google, Ahrefs, GKP, websites, traffic | `seo/` | `seo/memory/MEMORY.md` |
| Personal projects, personal tools, personal websites, non-work tasks | `personal/` | `personal/memory/MEMORY.md` |
| Something that doesn't fit above | **Ask first** | — |

## File discipline — always follow
- Deliverables (HTML reports, CSVs, exports) → `[domain]/clients/[client]/` or `[domain]/projects/[project]/`
- Memory (insights, rules, project state, learnings) → `[domain]/memory/`
- Global rules (apply everywhere) → `global/`
- **Never create files outside this structure without asking**
- **Never create a new top-level domain folder without user approval**

## Adding a new domain
If a task doesn't fit any existing domain: "This looks like [X] work — should I create a new domain for it?" If yes, create: `[domain]/`, `[domain]/CLAUDE.md`, `[domain]/memory/MEMORY.md`. Follow the same structure as seo/ or personal/.

## Always confirm capability before starting work
Before doing anything on a task, identify which capability it maps to and confirm with the user:
- "This looks like **[Capability Name]** work — proceeding under that. Correct?"
- If it maps to a new capability that doesn't exist yet → "This doesn't fit an existing capability. Should I create **[Capability Name]** for it?"
- Only proceed once confirmed — never assume and dive in
- If a task spans multiple capabilities → name both and ask which to file it under

## Auto-learning — always on, never needs to be asked
Every conversation is a learning opportunity. Without being asked:
- **Capability-level instructions** (how to do something, a new rule for a specific tool, a process correction) → save immediately to that capability's memory file
- **Global rules** (how to behave, communication preferences, system-level decisions) → save immediately to `global/CLAUDE.md` and commit
- **Project-specific learnings** (client decisions, SERP findings, strategy rationale) → save to the relevant client memory file
- After saving, briefly note what was saved so the user knows it's captured — one line, not a full recap
- This is the core of how AgentOps improves over time — every session makes the system smarter

## Cross-domain tasks
If a task genuinely spans two domains, work in the primary domain and flag what (if anything) needs to be noted in the other domain's memory.
