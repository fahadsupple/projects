# Global Rules for Claude Code

## Task Tracking (Crash Recovery)

Whenever you start a **significant or multi-step task** (anything that takes more than one exchange, or involves file changes, code runs, configuration, etc.), register it immediately:

```bash
python3 ~/.claude/task_tracker.py add "brief description of the task"
```

When the task is fully complete, mark it done:

```bash
python3 ~/.claude/task_tracker.py done <id>
```

To see all tracked tasks at any time:

```bash
python3 ~/.claude/task_tracker.py list
```

**Why:** At every session start, the system checks `~/.claude/active_tasks.json` for any tasks that were never marked done — meaning the session likely crashed or was interrupted. Those tasks are automatically injected into your context so you can re-run them from scratch.

### Rules

- Register a task **before** you start working on it, not after
- Mark it done **only when fully complete** — not when in-progress
- Keep descriptions specific enough to re-run without additional context
  - Bad: "fix bug"
  - Good: "Fix auth token refresh in /home/invoi/project/src/auth.py — token was expiring before refresh"
- One task ID per discrete piece of work
- Clean up old done tasks periodically: `python3 ~/.claude/task_tracker.py clear-done`

## Conversation Logs

All conversations are automatically saved to `~/logs/YYYY-MM-DD/` as markdown files when a session ends. You do not need to do anything — this is handled by a Stop hook.

To search logs:

```bash
~/logs/search.sh "keyword"
~/logs/search.sh "keyword" 2026-03-26   # specific date
~/logs/search.sh "keyword" -l           # list matching files only
```

---

## Autonomy — Default Behaviour

If something can be done without the user's involvement, do it. Don't ask the user to run commands, open terminals, navigate UIs, or perform steps that Claude Code can execute directly via tools. Only involve the user when:
- A browser-based action is required (OAuth flows, UI navigation)
- A destructive or irreversible action needs explicit confirmation
- Missing information genuinely can't be inferred

Everything else: just do it.

---

## fahad_projects — GitHub Sync (Always Apply)

GitHub (`github.com/fahadsupple/projects`) is the **single source of truth**. All work is synced to it. Learnings, memory updates, and deliverables must end up there after every message where a file changed.

### At every session start — pull first
Run before loading memory or doing any work:

```bash
cd /home/invoi/fahad_projects && git pull
```

- If pull reports a conflict → stop immediately, tell the user exactly which files conflict, do not proceed until resolved
- If pull fails (no network) → warn the user, proceed with local, flag that sync is needed at end of session

### After every message where a file changed — commit and push
```bash
cd /home/invoi/fahad_projects && git add -A && git commit -m "descriptive message of what changed" && git push
```

**What triggers a commit:**
- Any memory file created or updated (client files, master reference, feedback)
- Any deliverable created or updated (keyword plans, HTML reports)
- Any rule or system-level change (CLAUDE.md, MEMORY.md, setup.sh)

**Commit message rules:**
- Be specific: "Update client_wslegal.md — added entity structure section" not "update memory"
- One commit per logical unit of work, not one commit per file

---

## fahad_projects — Task Routing (Always Apply)

All work lives in `/home/invoi/fahad_projects/`. This applies on every machine, every tool, every session.

### At every session start
1. **Pull from GitHub first** — `cd /home/invoi/fahad_projects && git pull`
2. Read `/home/invoi/fahad_projects/MEMORY.md` — understand what domains and active projects exist
3. Identify the task domain from what the user describes
4. Load `seo/memory/MEMORY.md` and relevant client files before doing anything
5. If domain is unclear → ask before creating any file or writing anything

### Domain routing
| Task type | Folder | Memory to load |
|---|---|---|
| SEO / keywords / clients / SERP / rankings / Ahrefs / GKP / websites / traffic | `seo/` | `seo/memory/MEMORY.md` |
| Personal projects / personal tools / non-work | `personal/` | `personal/memory/MEMORY.md` |
| Doesn't fit any domain | **Ask user first** | — |

### Client file structure
All work for a given client lives under `seo/clients/[client-domain]/[capability]/`. Examples:
- `seo/clients/wslegal.com.au/keyword-research/keyword-plan.html`
- `seo/clients/wslegal.com.au/internal-linking/report.html`
- Client-level shared assets (brief, onboarding form) stay at `seo/clients/[client-domain]/` root — not inside a capability subfolder
- Client memory → `seo/clients/[client-domain]/memory/`
- Cross-client rules → `seo/memory/`

**Why:** Everything for a client is findable in one place, capability subfolders prevent cross-capability file sprawl.

### Rules
- Never create a new top-level domain folder without explicit user approval
- Never create files outside the correct domain structure without asking
- If task spans domains → work in primary domain, flag any crossover
- New domain: ask "This looks like [X] — should I create a new domain for it?"

### Auto-learning — always on
Every conversation is a source of learning. Without being asked:
- **Capability instructions** → save to that capability's memory file immediately
- **Global rules or preferences** → save to `global/CLAUDE.md` and commit
- **Project learnings** → save to the relevant client or project memory file
- Briefly confirm what was saved in one line so the user knows it's captured
- Never wait to be asked — learning is the default behaviour, not an exception

### Never assume — always ask for missing data
If a decision requires data that isn't available (search volume, client detail, SERP result, competitive info), **stop and ask** rather than guessing or proceeding.
- If search volume is needed → ask for a specific GKP search
- If client detail is unclear → ask the user to check with the client
- Frame the ask specifically: say exactly what data is needed and why, so it can be answered in one go
