#!/bin/bash
# AgentOps setup — run once on any new machine after cloning
# Usage: bash setup.sh
# Works on: Linux, macOS, Windows (Git Bash)

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Setting up AgentOps on $(hostname)..."

# Detect OS
IS_WINDOWS=false
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
  IS_WINDOWS=true
  echo "  Detected: Windows (Git Bash)"
else
  echo "  Detected: Unix (Linux/macOS)"
fi

# 1. Create ~/.claude/ if it doesn't exist
mkdir -p ~/.claude

# 2. Link global CLAUDE.md → ~/.claude/CLAUDE.md
if [ -f ~/.claude/CLAUDE.md ] && [ ! -L ~/.claude/CLAUDE.md ]; then
  echo "  Backing up existing ~/.claude/CLAUDE.md → ~/.claude/CLAUDE.md.bak"
  mv ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak
fi

if [ "$IS_WINDOWS" = true ]; then
  # Windows: copy instead of symlink (symlinks require admin/developer mode)
  cp "$REPO_DIR/global/CLAUDE.md" ~/.claude/CLAUDE.md
  echo "  ✓ ~/.claude/CLAUDE.md ← copied from global/CLAUDE.md"
  echo "  ⚠ Windows: re-run setup.sh after git pull to update rules"
else
  ln -sf "$REPO_DIR/global/CLAUDE.md" ~/.claude/CLAUDE.md
  echo "  ✓ ~/.claude/CLAUDE.md → global/CLAUDE.md (symlinked)"
fi

# 3. Link task_tracker.py → ~/.claude/task_tracker.py
if [ "$IS_WINDOWS" = true ]; then
  cp "$REPO_DIR/global/task_tracker.py" ~/.claude/task_tracker.py
  echo "  ✓ ~/.claude/task_tracker.py ← copied"
else
  ln -sf "$REPO_DIR/global/task_tracker.py" ~/.claude/task_tracker.py
  echo "  ✓ ~/.claude/task_tracker.py → global/task_tracker.py (symlinked)"
fi

# 4. Memory auto-load (Unix only — Windows relies on CLAUDE.md instruction)
if [ "$IS_WINDOWS" = false ]; then
  HOME_HASH=$(echo "$HOME" | tr '/' '-')
  HASH="${HOME_HASH}-AgentOps"
  mkdir -p ~/.claude/projects/$HASH
  if [ -L ~/.claude/projects/$HASH/memory ]; then
    rm ~/.claude/projects/$HASH/memory
  fi
  ln -sf "$REPO_DIR/memory" ~/.claude/projects/$HASH/memory
  echo "  ✓ Claude Code memory auto-load → AgentOps/memory/"
fi

# 5. Configure git
git config --global credential.helper store
git config --global core.autocrlf input
echo "  ✓ Git configured (credentials store + line endings)"

echo ""
echo "Setup complete."
echo "Open Claude Code from ~/AgentOps/ for all work:"
echo "  cd ~/AgentOps && claude"
