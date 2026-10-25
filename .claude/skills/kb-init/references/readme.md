# {{KB_DISPLAY_NAME}}

{{KB_PURPOSE}}

It covers these projects:

{{PROJECT_BULLETS}}

It records what the code doesn't say on its own: how the repos connect, decisions, workflows, ownership, and gotchas. It is written mainly for an agent to navigate. It was built from the [kb blueprint](https://github.com/estebanfelipep/kb).

## Setup

```sh
cp .env.example .env              # then point REPOS_ROOT at your clones
set -a; source .env; set +a       # makes the $…_REPO variables available
```

## Layout

```
kb/                 ← all the knowledge, and nothing else
  index.md          ← start here: the topic map, plus the repos
  context.md        ← glossary
  links.md          ← every external link, in one place
{{PROJECT_FOLDERS}}
  cross-project/    ← contracts and workflows spanning repos

AGENTS.md           ← rules every agent follows here
docs/adr/           ← decisions about how this KB is run
.claude/skills/     ← kb-add-project, kb-intake, kb-open-pr
.obsidian/          ← shared Obsidian vault settings (the vault is the repo root)
scratch/            ← gitignored working files
```

## Skills

- **`kb-intake`**: records new information in the KB. It routes the information to the right folder, verifies it against source, reconciles it with what's already written, and keeps the indexes current.
- **`kb-add-project`**: adds a project to the KB.
- **`kb-open-pr`**: opens a draft PR on any documented repo, with testing steps a cold reviewer can follow and checks for changes that affect other repos.

The rules every agent follows here are in [AGENTS.md](AGENTS.md).
