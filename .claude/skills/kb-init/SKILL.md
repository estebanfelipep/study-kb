---
name: kb-init
description: Turn a fresh copy of the kb blueprint into a specific knowledge base. Interviews the user about the KB's name, purpose, and the projects it covers, then fills the `{{…}}` placeholders, creates one folder per project via kb-add-project, writes `.env`, and removes the template scaffolding (including `examples/`). Use once, right after creating a repo from the template, or whenever the `kb/index.md` still contains `{{` placeholders.
---

# Initializing a KB from the blueprint

Run this once per KB. Work through the steps in order.

Paths to KB content in this skill (`index.md`, `context.md`, `links.md`, `cross-project/`, `org/`, and project folders) are relative to `kb/`. `docs/`, `.env`, `.env.example`, and `scratch/` are at the repo root.

## 1. Confirm this is an uninitialized template

Grep for `{{` in `kb/index.md` and `.claude/skills/kb-init/references/readme.md`. If `kb/index.md` has no placeholders left, the KB is already initialized. Stop and say so. To add a project to an existing KB, use `kb-add-project`.

## 2. Interview

Ask these questions, batching them where your agent allows. Don't guess any of the answers.

1. **Name.** Use kebab-case for the repo (`payments-kb`) and a display name for headings (`Payments KB`).
2. **Purpose.** One sentence: whose tribal knowledge this KB holds, and about what.
3. **Audience.** Is the KB private to its owners, or shared with the people it documents? Private is the default, and `AGENTS.md`'s "Outward-facing content" rule assumes it. If the KB is shared, note that in the README and drop that rule.
4. **Projects.** For each project, collect what `kb-add-project` needs: name, local clone path, remote URL, what it is, and depth (full, or black box for projects owned by someone else; see `docs/adr/0003-depth-per-project.md`).
5. **How they connect.** Two or three bullets: who calls whom, and who installs whose package. With a single project, ask which external systems it depends on instead.
6. **Org knowledge.** Will the KB hold teams, ownership, and initiatives? If so, create `kb/org/` now. If not, it can still be created on first use.

_Done when every question has an answer from the user._

## 3. Fill the root files

- **`README.md`:** replace it with `references/readme.md`, filled in. The current README describes the blueprint, not this KB.
- **`kb/index.md`:** fill `{{KB_NAME}}` and `{{HOW_PROJECTS_CONNECT}}`, as bullets in plain terms (who calls whom), without folder names. Leave **Topics** empty: `kb-intake` builds them as knowledge arrives.
- **`.env.example`:** set `KB_REPO` to this repo's folder name. Point `REPOS_ROOT` at the parent folder the user's clones share. If clones live in different places, give each variable an absolute path instead.
- **`AGENTS.md`:** leave it as is unless the audience answer was "shared", in which case remove the "Outward-facing content" section. The project list lives in `kb/index.md`, not here.

## 4. Add each project

Run `kb-add-project` once per project with the answers from step 2. It creates the folder, its index, the repo's entry in the Repos table, and the repo variable.

If there is only one project and it has no external systems to describe, delete `kb/cross-project/`. `kb-intake` recreates it when it's first needed.

## 5. Write `.env`

Copy `.env.example` to `.env` with the user's real paths. Then check that every variable resolves to a folder that exists:

```sh
set -a; source .env; set +a
for v in $(grep -oE '^[A-Z_]+_REPO' .env.example); do printf '%s=%s ' "$v" "${!v}"; [ -d "${!v}" ] && echo ok || echo MISSING; done
```

Report any `MISSING` folder. Don't silently drop the variable.

## 6. Remove template scaffolding

- Delete `examples/`.
- Delete `.claude/skills/kb-init/`. The skill has done its job, and leaving it in place invites a second run.
- Remove the `kb-init` lines from the Skills sections of `AGENTS.md` and `README.md`.
- Remove the `examples/` paragraph from `AGENTS.md`.

## 7. Verify

- `grep -rn '{{' --include='*.md' .` returns nothing outside `.claude/skills/*/references/`.
- Every folder has its index (`<folder>/<folder>.md`), and every markdown file and subfolder is listed in its parent's index.
- Every link in every index resolves.

## 8. Hand off

Tell the user what was created. Offer to commit with a message like `Initialize <name> from the kb blueprint`, and suggest a first `kb-intake`. A good start is the README, ADRs, and glossary of each full-depth repo, recorded as pointers rather than copies.
