---
name: kb-add-project
description: Add a project (a repo) to this knowledge base. Creates its folder and index note from the template, declares its depth (full or black box), adds its repo variable to `.env.example` and `.env`, lists the docs its source repo already maintains, and adds its row to the `kb/index.md`. Use when the user wants the KB to start covering a new repo, or when kb-init runs it once per project.
---

# Adding a project to the KB

Paths to KB content in this skill (`index.md`, `context.md`, `links.md`, `cross-project/`, `org/`, and project folders) are relative to `kb/`. `docs/`, `.env`, `.env.example`, and `scratch/` are at the repo root.

## 1. Gather

Get each of these from the user. If `kb-init` already collected them, take them from there.

- **Name:** kebab-case. It is also the folder name (`shop-web`).
- **Local clone path** and **remote URL.**
- **What it is:** one sentence.
- **Depth:** full, or black box (`docs/adr/0003-depth-per-project.md`). Black box is for projects the KB's owners don't own. For those, also get the **owning team**.
- **How it connects** to the projects already in the KB, if it does.

Derive the variable name from the folder name: upper snake case plus `_REPO` (`shop-web` → `$SHOP_WEB_REPO`).

If a folder with that name already exists, stop and say so.

## 2. Find the docs the source repo already maintains

Look in the clone for these, but don't read them in full. The KB points to these documents; it never copies them:

- `README.md`, `CONTRIBUTING.md`
- a glossary (`CONTEXT.md`, `GLOSSARY.md`, `docs/glossary*`)
- decision records (`docs/adr/`, `docs/decisions/`, `adr/`)
- agent instructions (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`)
- runbooks and deploy docs under `docs/`
- a PR template (`.github/pull_request_template.md`) and any repo skills (`.claude/skills/`)

For a black-box project, list only what an integrator needs: the README and the API or SDK docs.

## 3. Create the folder

Create `kb/<name>/<name>.md` from `references/project-index.md`, filled in. Fill in "Read this folder for" and "Read `cross-project/` instead for" concretely, because these lines are what route the next agent. For a black-box project, "Read this folder for" names only the integration surface.

## 4. Wire it in

- **`kb/index.md`:** add the repo to its **Repos** table:

  `| [<name>](<name>/<name>.md) | <what it is, in one line> | <full or black box> | `$<VAR>` |`

  If this is the KB's fourth repo, move the whole table to `kb/repos.md` instead. Open that file with a one-line statement of what it covers, then replace the Repos section with a Reference entry: `- [repos.md](repos.md): every documented repo, its depth, and its variable. Read when: you need a repo, its owner, or its clone variable.` From then on, add repos to `kb/repos.md`.

  Don't add a topic for the repo. Topics are subjects people ask about, and `kb-intake` creates them as knowledge arrives. If the project changes how the projects fit together, update that section too, in plain terms rather than folder names.
- **`.env.example`:** add the variable with a one-line comment saying what the repo is, and its depth if it's a black box. Derive the path from `${REPOS_ROOT}` when the clone sits under it.
- **`.env`:** add the real path.
- **`cross-project/`:** if this is the KB's second project and the folder was removed, recreate it from `references/cross-project-index.md`. If a contract with an existing project is already known, record it through `kb-intake`. Don't write it here.
- **`links.md`:** add the remote URL under "Repos".

## 5. Verify

- The variable resolves to an existing folder.
- Every new link resolves.
- Nothing was left with a `{{` placeholder.

Offer to commit with a message like `Add <name> to the KB (<depth>)`.
