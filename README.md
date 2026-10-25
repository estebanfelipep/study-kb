# kb

A blueprint for knowledge bases that AI agents can navigate. Each knowledge base (KB) covers one or more related software projects.

A KB built from this template records what the code doesn't say on its own:

- how the repos connect
- why things are the way they are
- workflows, gotchas, and who owns what

It is plain markdown in a git repo. It is organized so an agent loads only the files a question needs, rather than reading everything up front.

## Principles

- **Progressive disclosure, by topic.** [kb/index.md](kb/index.md) is a map of the KB's top-level topics, the subjects people ask about. Each topic links to the files that cover it, across repos. Each folder's index note lists that folder's files. Every entry says what it covers and *when to read it*, so an agent picks files from the entries instead of globbing the KB.
- **One place per fact.** Facts true of one project live in that project's folder. Contracts and workflows that span projects live once, in `cross-project/`, with pointers from each side.
- **Point to the source repos' docs, don't copy them.** Each project's own README, ADRs, and glossary stay the copy that gets maintained. The KB links to them.
- **Verify, then reconcile, then write.** New information is checked against source code where it can be. A conflict with existing text is raised and confirmed before anything is overwritten.
- **Current facts only.** Files state what is true now, and git history is the changelog.
- **Answer only from what's written.** Agents name each gap rather than filling it with plausible guesses. A gap becomes the next intake.
- **Agent-agnostic.** [AGENTS.md](AGENTS.md) holds the rules, and [CLAUDE.md](CLAUDE.md) imports it. Skills are plain markdown that any agent can follow.

The reasoning behind each of these is recorded in [docs/adr/](docs/adr/adr.md).

## Getting started

1. Create a new repo from this template, and clone it next to the repos it will document.
2. Open it with your coding agent and ask it to **run `kb-init`**. The skill interviews you about the KB's name and purpose, then about each project. For each project it asks for the repo path, what the project is, whether to document it in full or as a black box, and how the projects connect. It then fills in the placeholders, creates one folder per project, writes `.env`, and removes this template's scaffolding, including `examples/`.
3. From then on, feed the KB through **`kb-intake`**. Meeting notes, decisions, gotchas, links, or a plain "remember that…" all work.

To see what a filled-in KB looks like before starting, browse [examples/acme/](examples/acme/acme.md).

## Browsing in Obsidian

The repo is also an [Obsidian](https://obsidian.md) vault: open the folder with **Open folder as vault**. The committed `.obsidian/` settings keep Obsidian compatible with the KB's rules:

- Links are standard relative markdown links, not wikilinks, and they update when you rename a file.
- Pasted images go to an `images/` folder next to the note.
- `scratch/` is excluded, and daily notes are off, so no stray files land in the KB.
- Each folder's index is named after the folder (`shop-web/shop-web.md`), so graph nodes read as folder names instead of a row of identical `index` labels. The graph also colors `cross-project/`, `docs/adr/`, and `org/`.

Personal layout state (`.obsidian/workspace*.json`) is gitignored.

Use Obsidian to **read and see the shape** of the KB. Open the **local graph** and **backlinks** panels on a topic file to see what connects to it. Keep **writing** through `kb-intake`. A hand edit skips verification, reconciliation, and index updates, so ask an agent to check the indexes afterwards.

## Layout

```
kb/                 ← all the knowledge, and nothing else
  index.md          ← the topic map, plus the repos: start here
  context.md        ← glossary of terms and abbreviations
  links.md          ← every external link in the KB, in one place
  <project>/        ← one folder per project, each with its own index, <project>/<project>.md
  cross-project/    ← contracts and workflows that span projects
  org/              ← optional: teams, ownership, initiatives (created on first use)

AGENTS.md           ← rules every agent follows here (CLAUDE.md imports it)
docs/adr/           ← decisions about how the KB itself is run
.claude/skills/     ← kb-init, kb-add-project, kb-intake, kb-open-pr
.obsidian/          ← shared Obsidian vault settings (the vault is the repo root)
.env.example        ← repo path variables ($WEB_REPO, ...); copy to .env
scratch/            ← gitignored working files
examples/acme/      ← a worked, fictional KB, laid out like kb/ (removed by kb-init)
```

## Skills

The skills live in `.claude/skills/<name>/SKILL.md`. Claude Code loads them automatically. Other agents can be pointed at the file when the task matches.

- **`kb-init`**: turns this template into a specific KB. Run it once.
- **`kb-add-project`**: adds a project folder, its index, its repo variable, and its row in the root index.
- **`kb-intake`**: records new information. It routes the information to the right folder and file, verifies it against source, reconciles it with what's already written, and keeps every index current.
- **`kb-open-pr`**: opens a draft PR on any documented repo. It adds testing steps a cold reviewer can follow and checks for changes that affect other repos.

## Status

This is an early version of the blueprint, extracted from two KBs in real use. The conventions are stable. The skills will keep evolving.
