---
name: infra-dataforseo-mcp-npx-fix
description: "DataForSEO MCP failing to connect across ALL plugins is a corrupted npx cache, not bad credentials — fix with a global npm install"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 03c565da-296a-4e5a-a5de-ca2c8728523d
---

When DataForSEO MCP shows "✘ Failed to connect" in `claude mcp list` for **every** plugin at once (content, kwr, schema, seoaudit) while brave-search and playwright connect fine, the cause is a **corrupted npx cache**, not credentials.

Diagnose by running the launcher directly — a corrupt cache surfaces as `npm error code ENOTEMPTY` / `syscall rename` under `~/.npm/_npx/<hash>/`:

```bash
/home/invoi/.claude/plugins/cache/colana-mp/content/<ver>/scripts/mcp-launch.sh dataforseo npx -y dataforseo-mcp-server
```

**Fix (verified 2026-07-14):**

```bash
rm -rf ~/.npm/_npx/787bcb63918aaa21     # the dataforseo-mcp-server npx cache dir
npm install -g dataforseo-mcp-server    # ~324 packages, ~15s
```

The global install makes `npx -y dataforseo-mcp-server` resolve from PATH instead of re-downloading, which sidesteps the broken cache. All plugins reconnect without changing any `.mcp.json`.

**Gotchas:**
- Do NOT `timeout 120` the reinstall — killing npx mid-install re-corrupts the cache and you loop on the same failure.
- Credentials live at `~/.claude/credentials/dataforseo.env` (`DATAFORSEO_USERNAME` / `DATAFORSEO_PASSWORD`) and are shared across all SEO plugins. Verify them independently before blaming them:
  ```bash
  curl -s -u "$DATAFORSEO_USERNAME:$DATAFORSEO_PASSWORD" https://api.dataforseo.com/v3/appendix/user_data
  ```
  `status_code: 20000` = creds are fine, look at the cache instead.

Related: [[feedback_workflow]]
