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

## AgentOps — GitHub Sync (Always Apply)

GitHub (`github.com/fahadwaheedmir/AgentOps`) is the **single source of truth**. All machines sync to it. Learnings, memory updates, and deliverables created on any machine must end up there.

### Detecting session start — automatic, no trigger needed
If there is no prior conversation history (this is the first message in the session), automatically run the full new session routine before responding to anything — regardless of what the user's first message says. The user never needs to type "new session" or any other trigger.

### At every session start — sync safely, never overwrite
Run in this exact order before loading memory or doing any work:

```bash
# Step 1: commit any local changes that haven't been pushed yet
git -C ~/AgentOps add -A
git -C ~/AgentOps diff --cached --quiet || git -C ~/AgentOps commit -m "Auto-commit local changes before pull"

# Step 2: pull from GitHub (adds missing remote changes, never overwrites)
git -C ~/AgentOps pull
```

- Local changes are always committed first — nothing is ever silently overwritten
- Pull only adds what's missing from remote — it merges, it does not replace
- If pull reports a conflict → stop immediately, tell the user exactly which files conflict, do not proceed until resolved
- If pull fails (no network) → warn the user, proceed with local, flag that sync is needed at end of session
- Local copy is always kept — GitHub is the sync target, not the replacement

### After any update — commit and push
After every significant piece of work — memory update, new deliverable, rule change, new project context — commit and push:
```bash
git -C ~/AgentOps add -A
git -C ~/AgentOps commit -m "descriptive message of what changed"
git -C ~/AgentOps push
```
**What triggers a commit:**
- Any memory file created or updated (client files, master reference, feedback)
- Any deliverable created or updated (keyword plans, HTML reports)
- Any rule or system-level change (CLAUDE.md, MEMORY.md, setup.sh)
- End of any session where files changed

**Commit message rules:**
- Be specific: "Update client_wslegal.md — added entity structure section" not "update memory"
- One commit per logical unit of work, not one commit per file

### Never let machines fall out of sync
- Always pull at session start on every machine before touching any file
- Always push at session end after any file changes
- If you forget to push on one machine and start on another → pull will catch it

---

## AgentOps — Task Routing (Always Apply)

All work lives in `~/AgentOps/`. This applies on every machine, every tool, every session.

### At every session start
1. **Pull from GitHub first** — `git -C ~/AgentOps pull`
2. Read `~/AgentOps/MEMORY.md` — understand what domains and active projects exist
3. Identify the task domain from what the user describes
4. Load `~/AgentOps/[domain]/memory/MEMORY.md` and relevant project files before doing anything
5. If domain is unclear → ask before creating any file or writing anything

### Domain routing
| Task type | Folder | Memory to load |
|---|---|---|
| SEO / keywords / clients / SERP / rankings / Ahrefs / GKP / websites / traffic | `seo/` | `seo/memory/MEMORY.md` |
| Personal projects / personal tools / non-work | `personal/` | `personal/memory/MEMORY.md` |
| Doesn't fit any domain | **Ask user first** | — |

### Client file structure
All work for a given client lives under `[domain]/clients/[client-domain-url]/[capability]/`. Examples:
- `seo/clients/wslegal.com.au/keyword-research/keyword-plan.html`
- `seo/clients/wslegal.com.au/internal-links/report.html`
- Client-level shared assets (brief, onboarding form) stay at `clients/[client-domain-url]/` root — not inside a capability subfolder

**Why:** Everything for a client is findable in one place, capability subfolders prevent cross-capability file sprawl, no duplicate folder hierarchies across domains.

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
