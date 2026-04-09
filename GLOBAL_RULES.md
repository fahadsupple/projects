# GLOBAL_RULES.md

This file defines the interaction modes and global instructions for Gemini CLI in this workspace.

## 1. Interaction Modes

To distinguish between **training** (updating these rules) and **execution** (performing tasks), the following tokens SHOULD be used at the beginning of messages to set the context:

### `[MODE: TRAINING]`
- **Purpose:** To update, refine, or add new instructions to this `GLOBAL_RULES.md` or other configuration files.
- **Behavior:**
  - I will prioritize analyzing your input to update the project's rules and documentation.
  - I will propose changes to the rules before applying them.
  - I will NOT perform functional code changes (e.g., bug fixes, feature implementations) in this mode unless they are part of a documentation/rule update.
- **Verification:** I will confirm when the rule updates are finalized.

### `[MODE: EXECUTION]`
- **Purpose:** To perform engineering tasks, bug fixes, feature development, or code analysis.
- **Behavior:**
  - I will operate based on the **existing** rules in `GLOBAL_RULES.md` and standard system instructions.
  - I will focus on fulfilling the technical objective (testing, building, validating code).
  - I will NOT modify the rules in this mode.
- **Default:** If no mode is specified, this is the default operating state for technical tasks.

---

## 2. Global Core Instructions

*(Reserved for future rules to be added via Training Mode)*
