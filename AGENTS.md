# Agent instructions

This repo is a knowledge base (KB) for one or more related projects. All of the knowledge lives in `kb/`, and its map is [kb/index.md](kb/index.md). Everything outside `kb/` is tooling: these rules, `docs/` (decisions and rules about how the KB is run), the skills, and the Obsidian and env config. The KB holds what isn't obvious from their code: how they connect, why things are the way they are, workflows, ownership, and gotchas.

**If `kb/index.md` still contains `{{` placeholders, this KB hasn't been set up yet.** Run the `kb-init` skill before doing anything else.

## Navigating: start at `kb/index.md`

The KB uses progressive disclosure. Load only what the question needs:

1. Read `kb/index.md` and pick the topic, or topics, the question is about.
2. Open only the files those topics list. They may sit in different folders.
3. If you need neighbors, read the index of the folder a file sits in (`<folder>/<folder>.md`).

Don't glob or read the whole KB up front. Each entry says what it covers and when to read it, so choose from the entries.

`examples/`, if present, is a fictional sample KB for people learning the format. It is not part of this KB. Never answer from it or write to it.

## Organizing: folders and indexes

Folder and file paths in this section are relative to `kb/`, except `docs/`, which sits at the repo root.

- **Project folders** hold facts that are true of one project. There is one folder per project, named after the project in kebab-case.
- **`cross-project/`** holds anything that spans two or more projects: contracts between repos (endpoints, payload shapes, shared secrets and env vars that must match) and workflows that span repos (local linking, coordinated releases, a change needing PRs in several repos). Record a contract once, here. In each affected project's index, add a one-line pointer to it.
- **`org/`** holds knowledge that isn't about any one project's code: teams, ownership, initiatives, and processes. Create it, with its index (`org/org.md`), the first time something belongs there.
- **`docs/`**, at the repo root outside `kb/`, holds the rules and decisions about how *this KB* is run. `docs/adr/` holds its hard-to-reverse decisions. Decisions about the projects themselves belong in the projects' own repos, or in their KB folder.
- **Files at the top of `kb/`:** [context.md](kb/context.md) is the glossary, and [links.md](kb/links.md) collects every external link in one place.
- **Every content folder has an index note named after the folder:** `shop-web/shop-web.md`, `cross-project/cross-project.md`, `docs/adr/adr.md`. The top of `kb/` is the one exception. Its index is `kb/index.md`, the single place navigation starts. A folder-named index has a distinct name in search, editor tabs, and Obsidian's graph, where a dozen files all called `index` would be indistinguishable. Two consequences follow. No topic file may share its folder's name, because that name is taken by the index. Subfolders need names that are unique across the KB, so that their indexes are too.
- **`kb/index.md` is a topic map, not a folder list.** It never lists folders. It lists the KB's top-level **topics**: the subjects people ask about, such as "Checkout" or "Authentication", not the names of repos or folders. Each topic links to every file that covers it, wherever that file lives, so a topic that spans three repos is one entry. A file may appear under several topics. Each entry looks like this:

  ```
  - **Topic**: what it covers. Read when: <the kind of question it answers>.
    - [file.md](folder/file.md)
  ```

  Below the topics, a **Repos** section lists the documented repos: name (linked to its folder index), what it is, depth, and variable. Once there are more than three repos, move that list to `kb/repos.md` and link it from the index's Reference section.
- **Every folder index lists every markdown file and subfolder in its folder,** one line each:

  `- [file.md](file.md): what it covers. Read when: <the kind of question it answers>.`

  A folder index lists only its own folder's contents. It never lists grandchildren. `kb/index.md` is the exception, because topics cut across folders.
- **Topic files start broad.** Name them in kebab-case after the subsystem (`checkout-flow.md`, not `notes-oct.md`). Split a topic into its own file only once a shared file has grown slow to search. Promote related files into a subfolder, with its own index (`<folder>/<folder>.md`), once a topic has several files.
- **Images** go in an `images/` subfolder of the folder that uses them, named `<topic>-<yyyy-mm-dd>.<ext>`. Link them from the topic file. Indexes don't list images.
- **Moves keep indexes true.** Whenever you add, rename, split, or move a file or folder, update the parent folder's index in the same change. Also update every topic in `kb/index.md` that links to the file.

## Depth: full or black box

Each project's index declares its depth ([ADR 0003](docs/adr/0003-depth-per-project.md)):

- **Full:** internals included.
- **Black box:** the project is owned by someone else, so the KB records only its integration surface. That means what it exposes, how the documented projects depend on it, who owns it, and a pointer to its repo. It never records its internal architecture.

## Repo paths are variables, not literals

The documented repos are referred to by variable, such as `$WEB_REPO`. Their values live in `.env` at the repo root. `.env` is gitignored, and `.env.example` is the committed template that lists every variable. Markdown doesn't interpolate, so resolve variables first: `set -a; source .env; set +a`.

When writing KB content or skills, refer to a repo by its variable, never by an absolute path. Write a path inside a repo relative to its variable, as in `$WEB_REPO/src/app/api/route.ts`. If a file needs a variable that isn't in `.env.example` yet, add it there as well as in `.env`.

## Writing content

- **Current facts only.** State what is true now. Never write "(previously X)", "(as of…)", or a changelog section: git history records it ([ADR 0001](docs/adr/0001-git-history-as-changelog.md)). Because history lives only in git, commit messages must say *why* a change was made and where the information came from.
- **Link, don't mention.** Refer to another KB file with a relative markdown link (`[checkout-flow.md](../shop-web/checkout-flow.md)`), not a backticked path. Never use `[[wikilinks]]`. Relative links are what agents follow, what GitHub renders, and what draws the edges in Obsidian's graph. Paths into the documented repos (`$WEB_REPO/...`) stay in backticks, because they point outside the KB.
- **Keep diagrams within 72 columns.** Keep every line of an ASCII diagram in a code block at 72 characters or fewer. Obsidian's editor can't scroll a code block sideways, so anything wider wraps and breaks the diagram's alignment. Break a long label or annotation onto its own row rather than widening the diagram.
- **Tag sources inline.** Use `_(source: <person or meeting>, <date>)_` when a fact traces to someone. Use `_(verified against source, <yyyy-mm-dd>)_` when you checked it in code.
- **Extract, don't paste.** For an external resource, record the durable facts and link back to the original. Add the link to [links.md](kb/links.md).
- **New content arrives through the `kb-intake` skill,** which applies all of the above.

## Scratch files

When asked to create a file that isn't KB content, save it under `scratch/` at the repo root (gitignored), never inside `kb/`. Examples are a drafted message, a ticket body, or a one-off doc.

## Outward-facing content

Treat this KB as private unless its `README.md` says otherwise. In anything meant for people outside this repo, never cite the KB, link to it, or name its files. That includes tickets, PR bodies, drafted messages, and scratch files written for someone else. State the facts directly instead.

## Answering questions from this KB

Answer only from what's written. Never fill gaps with general knowledge or plausible-sounding inference.

- **Navigate by index first.** Follow the indexes to the likely files. If those don't answer the question, widen the search: check sibling files, `kb/cross-project/`, [context.md](kb/context.md), and a grep across `kb/`. Then lead with the direct answer.
- **Default to over-including.** Add anything related, such as adjacent mentions, other files, or tangential detail. A stray reference elsewhere can be the clue that matters.
- **Name every gap.** Do this for each claim as well as for the answer as a whole. If a piece is missing, partial, or only implied, name the specific gap (file, sub-topic) instead of glossing over it. Invite the person asking to fill it in, so it can go back into the KB through `kb-intake`.

## Skills

The skills live in `.claude/skills/<name>/SKILL.md`. If your agent doesn't load skills automatically, read the matching `SKILL.md` and follow it when a task fits:

- **`kb-init`**: set up a fresh copy of this template. Run it once.
- **`kb-add-project`**: add a project to the KB.
- **`kb-intake`**: record any new information in the KB.
- **`kb-open-pr`**: open a draft PR on one of the documented repos.
