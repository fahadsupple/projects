---
name: File Structure — All Work Saved in fahad_projects
description: All work must be saved inside /home/invoi/fahad_projects/ — canonical folder structure, git sync rules
type: feedback
---
## All work and output files go inside /home/invoi/fahad_projects/

Never create files outside `/home/invoi/fahad_projects/`. All deliverables, scripts, client files, and project folders must live inside this directory.

**Why:** User wants all work consolidated in one place — fahad_projects is the single working directory, synced to GitHub.

**Structure:**
```
fahad_projects/
  seo/
    clients/[domain]/           ← client root (brief, onboarding form, form-submission)
      keyword-research/         ← keyword plan HTML, GKP/, ahrefs/
      internal-linking/         ← internal link reports and data
      spelling-mistakes-finder/ ← spelling audit HTML reports
      url-audit/                ← URL/meta audit files
      memory/                   ← client-specific memory files
    memory/                     ← cross-client rules only (feedback_*.md, keyword_research_master.md)
    tools/[capability]/         ← shared scripts and project-instructions.txt
  global/                       ← global rules (CLAUDE.md, task_tracker.py, setup.sh)
  memory/                       ← root memory files (auto-loaded by Claude Code)
```

**How to apply:**
- Deliverables → `seo/clients/[domain]/[capability]/`
  - e.g. `seo/clients/triplejfurniture.com.au/keyword-research/keyword-plan.html`
  - e.g. `seo/clients/wslegal.com.au/keyword-research/GKP/conveyancer-general.csv`
- Client root assets (brief, onboarding form) → `seo/clients/[domain]/` root
- Client memory → `seo/clients/[domain]/memory/`
- Cross-client rules → `seo/memory/` (feedback_*.md, keyword_research_master.md)
- Tool scripts → `seo/tools/[capability]/`

**Memory — Two-location rule:**
Write memory to BOTH locations:
1. `/home/invoi/.claude/projects/-home-invoi-fahad-projects/memory/` — auto-loaded by Claude
2. `/home/invoi/fahad_projects/memory/` — visible inside the project folder

Everything lives in `/home/invoi/fahad_projects/`, which is synced to `github.com/fahadsupple/projects` (remote: origin).

**Session start — always pull first:**
```bash
cd /home/invoi/fahad_projects && git pull
```

**End of EVERY message where a file changed — commit and push:**
```bash
cd /home/invoi/fahad_projects && git add -A && git commit -m "description of what changed" && git push
```

This runs after every single response where any file changed — not just at end of session. Local files and GitHub must always be in sync. Never skip this.
