# Agent instructions

This repo is a personal study knowledge base (KB) covering software development: cloud (AWS), data engineering, AI engineering, languages such as JavaScript and Python, CSS, software architecture, and anything else studied along the way. It also tracks progress toward certifications, such as the AWS Certified Data Engineer – Associate.

All of the knowledge lives in `kb/`, and it starts at [kb/index.md](kb/index.md). Everything outside `kb/` is tooling: these rules, `docs/` (decisions about how the KB is run), the skills, and the Obsidian config.

## Navigating: start at `kb/index.md`

The KB uses progressive disclosure. Load only what the question needs:

1. Read `kb/index.md` and pick the subject the question is about.
2. Read that subject's index (`<folder>/<folder>.md`) and follow the indexes down to the files you need.
3. Follow a file's Related links when the answer spans folders, such as a concept in `data-engineering/` and its AWS service in `aws/`.

Don't glob or read the whole KB up front. Each index entry says what it covers and when to read it, so choose from the entries.

## Organizing: folders and indexes

Folder and file paths in this section are relative to `kb/`, except `docs/`, which sits at the repo root.

- **Subject folders** sit at the top of `kb/`, one per subject area, named in kebab-case: `aws/`, `data-engineering/`, `ai-engineering/`, `javascript/`, `python/`, `css/`, `software-architecture/`. Create a subject folder, with its index, when its first note arrives. Never create empty folders or placeholder files.
- **Vendor-neutral concepts and vendor-specific facts live apart.** A concept that holds regardless of vendor (ETL vs ELT, CDC, columnar file formats, partitioning) goes in the vendor-neutral subject folder, such as `data-engineering/`. How a vendor implements it goes in the vendor's folder, such as `aws/`, and links back to the concept file. Record each fact once.
- **`aws/` has two subfolders:**
  - `aws/aws-services/` holds one file per AWS service, named after the service (`s3.md`, `glue.md`, `kinesis-data-streams.md`), inside a category subfolder (`aws-analytics/`, `aws-databases/`, `aws-security/`, …). A service that belongs to two or more categories goes in `aws-general-services/`, never in two places. A service's facts live in its file, whichever certification or track they came up in. Create a service file, and its category folder, when the service first comes up, even if only a line or two is known about it. Once a service file outgrows one file, promote it to its own subfolder (`aws-analytics/glue/glue.md`), as "Every topic gets its own file" describes.
  - Every service file has the same shape: a title, a one-line statement of what it covers, an optional `## Sources` section, then `## What it is`, `## Characteristics` (general characteristics, limits, features, pricing, integrations), `## Example` (one or more concrete usages) and `## Related` (links). Comparisons between services and "if the question says… pick" rules don't go in service files; they go in the track's `choosing-*` files.
  - `aws/aws-data-engineering/` holds the data engineering track and the AWS Certified Data Engineer – Associate (DEA-C01) exam: exam facts, domains, study progress, how services combine into pipelines, and exam traps. It links to service files rather than repeating them.
- **Files at the top of `kb/`:** [context.md](kb/context.md) is the glossary, and [links.md](kb/links.md) collects every external link in one place.
- **Every content folder has an index note named after the folder:** `aws/aws.md`, `aws/aws-services/aws-services.md`, `docs/adr/adr.md`. The top of `kb/` is the one exception. Its index is `kb/index.md`, the single place navigation starts. A folder-named index has a distinct name in search, editor tabs, and Obsidian's graph. Two consequences follow. No topic file may share its folder's name, because that name is taken by the index. Folder names must be unique across the KB, so that their indexes are too: prefix a subfolder with its parent when the bare name could collide (`aws-data-engineering/`, not `data-engineering/`, because `data-engineering/` is the vendor-neutral subject).
- **`kb/index.md` covers only the first layer.** It lists the top-level subject folders, linked to their indexes, and the reference files at the top of `kb/` (`context.md`, `links.md`). It never links deeper. A subject's index is where its reading guide starts.
- **Every folder index lists every markdown file and subfolder in its folder,** one line each:

  `- [file.md](file.md): what it covers. Read when: <the kind of question it answers>.`

  A folder index lists only its own folder's contents. It never lists grandchildren, and `kb/index.md` is no exception.
- **Indexes are reading guides, not just lists.** A reader who opens an index should learn how to study what it holds, not only what's there. The file list itself carries the reading order: list files in the order to read them, not alphabetically, and group them under short bold labels when the folder has stages or layers. Right after the opening statement, a short `## How to read this folder` section adds only what the list can't say, one line each:
  - **Before:** what to read first, such as the concept files behind a vendor's services.
  - **Order:** why the files are in this order, or that the folder is a reference to dip into. Omit it for a one-file folder.
  - **After:** where to go next.

  **Never say a thing twice.** The guide never lists the files again, and it never restates how files relate when their Related sections already say it. A fact shared by every file in a folder is stated once, in the parent index, not in each child. `kb/index.md` works the same way: its subjects are in study order. When you add, move or split a file, place it in the reading order in the same change.
- **Every topic gets its own file, even a small one.** When a topic comes up, even briefly, create a file for it rather than folding it into a broader file, as long as there is real content to put in it. Name it in kebab-case after the subject (`batch-vs-streaming.md`, not `notes-oct.md`). When a file grows too big to read in one sitting, or holds several distinct subtopics, promote it to a folder named after the topic. The file's content is split into topic files inside that folder, and the folder index (`<topic>/<topic>.md`) becomes the reading guide to them. Update every link to the old file, the parent index and `kb/index.md` in the same change.
- **Images** go in an `images/` subfolder of the folder that uses them, named `<topic>-<yyyy-mm-dd>.<ext>`. Link them from the topic file. Indexes don't list images.
- **Moves keep indexes true.** Whenever you add, rename, split, or move a file or folder, update the parent folder's index in the same change. When a subject folder is added or renamed, update `kb/index.md` too.

## Writing content

- **Current facts only.** State what is true now. Never write "(previously X)", "(as of…)", or a changelog section. Git history records it ([ADR 0001](docs/adr/0001-git-history-as-changelog.md)). This applies to study progress too: a progress or weak-spots file states where things stand today. Commit messages must say *why* a change was made and where the information came from.
- **Every link explains the relationship.** This KB is for studying how concepts connect, so a link never stands alone. In a `## Related` section, write one bullet per linked file: `- [file.md](path): <how this relates to it>`. Say the direction and the mechanism, such as "Lambda is triggered by S3 event notifications to process each new object", not "Related services" or "Serverless summary". For a comparison file, give the one-line gist of the difference. For a concept file, say which concept this implements and how. If you can't state the relationship from what the KB says, drop the link.
- **Link, don't mention.** Refer to another KB file with a relative markdown link (`[glue.md](../aws-services/glue.md)`), not a backticked path. Never use `[[wikilinks]]`. Relative links are what agents follow, what GitHub renders, and what draws the edges in Obsidian's graph.
- **Keep diagrams within 72 columns.** Keep every line of an ASCII diagram in a code block at 72 characters or fewer. Obsidian's editor can't scroll a code block sideways, so anything wider wraps and breaks the diagram's alignment.
- **Sources are links, at the top.** When a file draws on external resources (a YouTube video, an AWS doc, an article), list them in a `## Sources` section right after the file's one-line statement, one line each: `- [Title](url): what it is.` Add each to [links.md](kb/links.md) too. Don't tag notes the user shares directly as a source, and don't add an empty Sources section.
- **Mark what isn't from the user's notes.** Mark content that comes from general knowledge, Q&A or your own additions with `_(added)_`, so it can be told apart and verified. Use `_(added; verify)_` for a fact likely to change, such as service availability or a renamed feature.
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
