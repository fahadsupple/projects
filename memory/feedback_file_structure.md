---
name: File Structure — All Work Saved in fahad_projects
description: All work must be saved inside /home/invoi/fahad_projects/ — no files created outside this directory
type: feedback
originSessionId: 81e50042-3c9e-4c29-91de-238cd6a73314
---
## All work and output files go inside /home/invoi/fahad_projects/

Never create files outside `/home/invoi/fahad_projects/`. All deliverables, scripts, client files, and project folders must live inside this directory.

**Why:** User wants all work consolidated in one place — fahad_projects is the single working directory.

**How to apply:**
- Keyword research deliverables → `/home/invoi/fahad_projects/keyword-research/[client-domain]/`
- Internal linking → `/home/invoi/fahad_projects/internal linking/`
- Spelling mistakes finder → `/home/invoi/fahad_projects/spelling-mistakes-finder/`
- New capabilities → `/home/invoi/fahad_projects/[capability-name]/`
- **Memory files → `/home/invoi/fahad_projects/memory/`** (mirrored from the auto-memory system at `~/.claude/projects/-home-invoi-fahad-projects/memory/`)
- All other folders → inside `/home/invoi/fahad_projects/`

When writing new memory, write to BOTH locations:
1. `/home/invoi/.claude/projects/-home-invoi-fahad-projects/memory/` — auto-loaded by Claude
2. `/home/invoi/fahad_projects/memory/` — visible inside the project folder

Everything lives in `/home/invoi/fahad_projects/`, which is synced to `github.com/fahadsupple/projects` (remote: origin).

**Session start — always pull first:**
```bash
cd /home/invoi/fahad_projects && git pull
```

**End of EVERY message — commit and push:**
```bash
cd /home/invoi/fahad_projects && git add -A && git commit -m "description of what changed" && git push
```

This runs after every single response where any file changed — not just at end of session. Local files and GitHub must always be in sync. Never skip this.
