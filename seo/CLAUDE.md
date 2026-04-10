# SEO Domain Context

This folder contains all SEO client work. If Claude Code is opened directly from this folder, load `./memory/MEMORY.md` immediately before doing anything else.

## Structure
```
seo/
  clients/[domain]/           ← client root (brief, onboarding form)
    [capability]/             ← deliverables for that capability
      keyword-research/       ← keyword plan HTML, GKP/, ahrefs/
      internal-linking/       ← internal link reports
      spelling-mistakes-finder/ ← audit HTML reports
      url-audit/              ← URL/meta audit files
    memory/                   ← client-specific memory
  memory/                     ← cross-client rules only (feedback, master reference)
  tools/[capability]/         ← shared scripts and project instructions
```

## Memory to load
Always read `./memory/MEMORY.md` first. It points to:
- `keyword_research_master.md` — all process rules, keyword standards, SERP rules, industry insights
- Feedback files — cross-client rules and learnings

Client-specific memory lives in `clients/[domain]/memory/` — load from there.

## Key rules (quick reference — full detail in memory files)
- Every keyword needs a modifier — never bare root keywords
- GKP is the source of truth for volume — always ask for GKP data, never assume
- Non-subset pairing rule — two keywords on the same page must not be linguistic subsets of each other
- SERP validation mandatory before finalising any keyword
- Mixed SERP = replace the keyword, not patch it
- Always save learnings and decisions to the relevant client memory file
- If data is missing to make a decision, ask for it — never proceed on assumptions
