---
name: Workflow Preferences
description: How Fahad wants Claude to behave — save all learnings, always ask not assume, list capabilities on request, autonomous operation
type: feedback
originSessionId: 81e50042-3c9e-4c29-91de-238cd6a73314
---
## Save all learnings as we go
User explicitly wants all learnings and decisions saved to memory as work progresses through client projects.

**Why:** So future conversations have full context without needing to re-read files or re-explain decisions.

**How to apply:** After each significant step or decision in a project, save the relevant context to memory immediately. Include reasoning behind decisions, not just the decision itself.

---

## Always list available capabilities when asked
When the user asks "what can you do", "what capabilities do you have", or similar — always list all capabilities that exist at that moment. Include: capability name, one-line description, where it lives.

**How to apply:** Also list capabilities as they are created through new work assigned. If a new tool/script/process is built, add it to the capabilities list in memory so it appears in future listings.

---

## Always ask — never assume or proceed without key information
If a decision requires data that isn't available (search volume, client preference, SERP result, competitive detail), **stop and ask** rather than guessing.

**Why:** Proceeding without key data leads to wrong recommendations.

**How to apply:**
- If search volume is needed → ask for a specific GKP search
- If client detail is ambiguous → ask the user to clarify or check with the client
- Frame the ask specifically: say exactly what data is needed and why, so the user can get it in one go

---

## Autonomy — Default Behaviour
If something can be done without the user's involvement, do it. Don't ask the user to run commands, open terminals, navigate UIs, or perform steps Claude Code can execute directly.

Only involve the user when:
- A browser-based action is required (OAuth flows, UI navigation)
- A destructive or irreversible action needs explicit confirmation
- Missing information genuinely can't be inferred

Everything else: just do it.

---

## Conversation Logs
All conversations are automatically saved to `~/logs/YYYY-MM-DD/` as markdown files when a session ends. This is handled by a Stop hook — no manual action needed.

To search logs:
```bash
~/logs/search.sh "keyword"
~/logs/search.sh "keyword" 2026-03-26   # specific date
~/logs/search.sh "keyword" -l           # list matching files only
```

## No GitHub sync
There is no GitHub repository sync. Everything is autonomous inside `/home/invoi/fahad_projects/`. Do not reference or attempt to push to any remote repo.
