---
name: File Structure — All Work Saved in fahad_projects
description: All work must be saved inside /home/invoi/fahad_projects/ — no files created outside this directory
type: feedback
originSessionId: 81e50042-3c9e-4c29-91de-238cd6a73314
---
## All work and output files go inside /home/invoi/fahad_projects/

Never create files outside `/home/invoi/fahad_projects/`. All deliverables, scripts, client files, and project folders must live inside this directory.

**Why:** User wants all work consolidated in one place — fahad_projects is the single working directory.

**Structure (matches Agent-SEO-skills exactly):**
```
fahad_projects/
  seo/
    clients/[domain]/[capability]/   ← all client deliverables and data
    memory/                          ← SEO memory files
    tools/[capability]/              ← shared scripts and instructions
  global/                            ← global rules and scripts
  memory/                            ← root memory files (mirrored here too)
```

**How to apply:**
- Client deliverables → `/home/invoi/fahad_projects/seo/clients/[domain]/[capability]/`
  - e.g. `seo/clients/triplejfurniture.com.au/keyword-research/keyword-plan.html`
  - e.g. `seo/clients/verdehomes.com.au/spelling-mistakes-finder/audit.html`
- Tool scripts → `/home/invoi/fahad_projects/seo/tools/[capability]/`
- Memory files → `/home/invoi/fahad_projects/memory/` (mirrored from `~/.claude/projects/-home-invoi-fahad-projects/memory/`)

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
