# Agent instructions

This repo is a personal study knowledge base (KB) covering software development: cloud (AWS), data engineering, AI engineering, languages such as JavaScript and Python, CSS, software architecture, and anything else studied along the way. It also tracks progress toward certifications, such as the AWS Certified Data Engineer – Associate.

All of the knowledge lives in `kb/`, and its map is [kb/index.md](kb/index.md). Everything outside `kb/` is tooling: these rules, `docs/` (decisions about how the KB is run), the skills, and the Obsidian config.

## Navigating: start at `kb/index.md`

The KB uses progressive disclosure. Load only what the question needs:

1. Read `kb/index.md` and pick the topic, or topics, the question is about.
2. Open only the files those topics list. They may sit in different folders.
3. If you need neighbors, read the index of the folder a file sits in (`<folder>/<folder>.md`).

Don't glob or read the whole KB up front. Each entry says what it covers and when to read it, so choose from the entries.

## Organizing: folders and indexes

Folder and file paths in this section are relative to `kb/`, except `docs/`, which sits at the repo root.

- **Subject folders** sit at the top of `kb/`, one per subject area, named in kebab-case: `aws/`, `data-engineering/`, `ai-engineering/`, `javascript/`, `python/`, `css/`, `software-architecture/`. Create a subject folder, with its index, when its first note arrives. Never create empty folders or placeholder files.
- **Vendor-neutral concepts and vendor-specific facts live apart.** A concept that holds regardless of vendor (ETL vs ELT, CDC, columnar file formats, partitioning) goes in the vendor-neutral subject folder, such as `data-engineering/`. How a vendor implements it goes in the vendor's folder, such as `aws/`, and links back to the concept file. Record each fact once.
- **`aws/` has two subfolders:**
  - `aws/aws-services/` holds one file per AWS service, named after the service (`s3.md`, `glue.md`, `kinesis-data-streams.md`). A service's facts live here, whichever certification or track they came up in. Once a service has several files, promote it to its own subfolder with an index (`aws-services/glue/glue.md`).
  - `aws/aws-data-engineering/` holds the data engineering track and the AWS Certified Data Engineer – Associate (DEA-C01) exam: exam facts, domains, study progress, how services combine into pipelines, and exam traps. It links to service files rather than repeating them.
- **Files at the top of `kb/`:** [context.md](kb/context.md) is the glossary, and [links.md](kb/links.md) collects every external link in one place.
- **Every content folder has an index note named after the folder:** `aws/aws.md`, `aws/aws-services/aws-services.md`, `docs/adr/adr.md`. The top of `kb/` is the one exception. Its index is `kb/index.md`, the single place navigation starts. A folder-named index has a distinct name in search, editor tabs, and Obsidian's graph. Two consequences follow. No topic file may share its folder's name, because that name is taken by the index. Folder names must be unique across the KB, so that their indexes are too: prefix a subfolder with its parent when the bare name could collide (`aws-data-engineering/`, not `data-engineering/`, because `data-engineering/` is the vendor-neutral subject).
- **`kb/index.md` is a topic map, not a folder list.** Its **Topics** section lists the subjects people ask about, such as "Streaming ingestion" or "Data warehousing", not folder names. Each topic links to every file that covers it, wherever that file lives, so a topic that spans `data-engineering/` and `aws/` is one entry. A file may appear under several topics. Each entry looks like this:

  ```
  - **Topic**: what it covers. Read when: <the kind of question it answers>.
    - [file.md](folder/file.md)
  ```

  Below the topics, a **Subjects** section lists each top-level subject folder, linked to its index, with what it covers.
- **Every folder index lists every markdown file and subfolder in its folder,** one line each:

  `- [file.md](file.md): what it covers. Read when: <the kind of question it answers>.`

  A folder index lists only its own folder's contents. It never lists grandchildren. `kb/index.md` is the exception, because topics cut across folders.
- **Topic files start broad.** Name them in kebab-case after the subject (`batch-vs-streaming.md`, not `notes-oct.md`). Split a topic into its own file only once a shared file has grown slow to search. Promote related files into a subfolder, with its own index, once a topic has several files.
- **Images** go in an `images/` subfolder of the folder that uses them, named `<topic>-<yyyy-mm-dd>.<ext>`. Link them from the topic file. Indexes don't list images.
- **Moves keep indexes true.** Whenever you add, rename, split, or move a file or folder, update the parent folder's index in the same change. Also update every topic in `kb/index.md` that links to the file.

## Writing content

- **Current facts only.** State what is true now. Never write "(previously X)", "(as of…)", or a changelog section. Git history records it ([ADR 0001](docs/adr/0001-git-history-as-changelog.md)). This applies to study progress too: a progress or weak-spots file states where things stand today. Commit messages must say *why* a change was made and where the information came from.
- **Link, don't mention.** Refer to another KB file with a relative markdown link (`[glue.md](../aws-services/glue.md)`), not a backticked path. Never use `[[wikilinks]]`. Relative links are what agents follow, what GitHub renders, and what draws the edges in Obsidian's graph.
- **Keep diagrams within 72 columns.** Keep every line of an ASCII diagram in a code block at 72 characters or fewer. Obsidian's editor can't scroll a code block sideways, so anything wider wraps and breaks the diagram's alignment.
- **Tag sources inline.** Use `_(source: <course, lesson, doc, or person>, <date>)_` when a fact traces to a specific resource. Use `_(verified against <official doc>, <yyyy-mm-dd>)_` when you checked it against official documentation.
- **Extract, don't paste.** For an external resource, record the durable facts in your own words and link back to the original. Add the link to [links.md](kb/links.md).
- **New content arrives through the `kb-intake` skill,** which applies all of the above.

## Scratch files

When asked to create a file that isn't KB content, save it under `scratch/` at the repo root (gitignored), never inside `kb/`. Examples are flashcard drafts, practice answers, or a one-off doc.

## Outward-facing content

Treat this KB as private. In anything meant for people outside this repo, never cite the KB, link to it, or name its files. State the facts directly instead.

## Answering questions from this KB

When asked what the KB says, or to quiz from it, answer only from what's written. Never fill gaps with general knowledge or plausible-sounding inference.

- **Navigate by index first.** Follow the indexes to the likely files. If those don't answer the question, widen the search: check sibling files, the matching vendor-neutral or vendor-specific folder, [context.md](kb/context.md), and a grep across `kb/`. Then lead with the direct answer.
- **Default to over-including.** Add anything related, such as adjacent mentions, other files, or tangential detail.
- **Name every gap.** If a piece is missing, partial, or only implied, name the specific gap (file, sub-topic) instead of glossing over it. Invite the person asking to fill it in, so it can go back into the KB through `kb-intake`.

When asked to *explain* or *teach* something rather than to report what the KB says, general knowledge is fine, but say which parts aren't in the KB yet and offer to record them.

## Skills

The skills live in `.claude/skills/<name>/SKILL.md`. If your agent doesn't load skills automatically, read the matching `SKILL.md` and follow it when a task fits:

- **`kb-intake`**: record any new information in the KB.
