# AGENTS.md is canonical; skills are plain markdown

The rules every agent follows live in [AGENTS.md](../../AGENTS.md). [CLAUDE.md](../../CLAUDE.md) is a one-line import of it (`@AGENTS.md`). Skills live in `.claude/skills/<name>/SKILL.md`, which Claude Code loads natively. They are written as self-contained markdown runbooks, so any other agent can follow them when pointed at the file. No skill depends on a skill or file outside this repo. Formats a skill relies on, like the ADR and glossary formats, ship in that skill's `references/` folder.

The KB is meant to outlive any one agent tool. If the rules were duplicated per tool, the copies would drift apart. If a skill depended on a global skill, a fresh clone would behave differently on every machine.

## Considered options

- **CLAUDE.md as the canonical file.** Rejected: other agents don't read it.
- **One copy of the rules per tool** (`.cursor/rules`, `.github/copilot-instructions.md`, …). Rejected: the copies drift. A tool-specific file is fine only as a thin pointer to `AGENTS.md`.
