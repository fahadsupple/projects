---
name: File Structure — All Work Saved in fahad_projects
description: All work must be saved inside /home/invoi/fahad_projects/ — no files created outside this directory
type: feedback
originSessionId: 81e50042-3c9e-4c29-91de-238cd6a73314
---
## All work and output files go inside /home/invoi/fahad_projects/

Never create files outside `/home/invoi/fahad_projects/`. All deliverables, scripts, client files, and project folders must live inside this directory.

**Why:** User wants all work consolidated in one place — fahad_projects is the single working directory.

**Structure:**
```
fahad_projects/
  seo/
    clients/[domain]/
      [capability]/    ← deliverables and data for that capability
      memory/          ← project memory specific to this client
    memory/            ← cross-client rules only (feedback, master reference)
    tools/[capability]/← shared scripts and instructions
  global/              ← global rules and scripts
  memory/              ← root memory files (auto-loaded by Claude)
```

**How to apply:**
- Client deliverables → `seo/clients/[domain]/[capability]/`
  - e.g. `seo/clients/triplejfurniture.com.au/keyword-research/keyword-plan.html`
- Client project memory → `seo/clients/[domain]/memory/`
  - e.g. `seo/clients/triplejfurniture.com.au/memory/client_triplejfurniture.md`
- Cross-client rules → `seo/memory/` (feedback_*.md, keyword_research_master.md)
- Tool scripts → `seo/tools/[capability]/`

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
