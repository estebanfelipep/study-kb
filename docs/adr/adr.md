# KB decisions — index

These records cover how this KB itself is run. They are not about the projects it documents; those projects keep their own decisions in their own repos. Each record follows `.claude/skills/kb-intake/references/adr-format.md`.

## Files

- [0001-git-history-as-changelog.md](0001-git-history-as-changelog.md): KB files state only the current facts, and history lives in git. Read when: you're about to write "previously…" or a dated note into a file, or writing a commit message.
- [0002-progressive-disclosure-folders.md](0002-progressive-disclosure-folders.md): why `kb/index.md` is a topic map rather than a folder list, why files are still filed per project with a `cross-project/` folder, and why every folder has its own index. Read when: adding a topic, a folder, or a repo, restructuring, or tempted to file a fact in two places.
- [0003-depth-per-project.md](0003-depth-per-project.md): why each project is documented either in full or as a black box. Read when: adding a project, or deciding how much detail to record about a repo your team doesn't own.
- [0004-agents-md-canonical.md](0004-agents-md-canonical.md): why the rules live in [AGENTS.md](../../AGENTS.md) and the skills are plain markdown. Read when: adding agent-specific config, or wondering why [CLAUDE.md](../../CLAUDE.md) is one line.
- [0005-knowledge-in-kb-folder.md](0005-knowledge-in-kb-folder.md): why all knowledge lives in `kb/` and tooling stays at the repo root. Read when: adding a top-level folder or file, or deciding whether something is knowledge or tooling.
