---
name: kb-intake
description: Intake new information into this study knowledge base. That includes course notes, lesson summaries, exam-guide facts, practice-test mistakes, study progress, links, external resources, or direct statements about any software-development subject (AWS, data engineering, AI engineering, JavaScript, Python, CSS, software architecture, …). The skill routes the information to the right subject folder and file, reconciles it against what's already written, and keeps every index, the glossary, and the links file current. Use whenever the user shares anything they've studied or want remembered.
---

# Intake for the knowledge base

Assume everything the user shares is worth intaking, and don't filter it for relevance.

Paths to KB content in this skill (`index.md`, `context.md`, `links.md`, and subject folders) are relative to `kb/`. `docs/` and `scratch/` are at the repo root.

Work through intake in order:

1. **Orient.** Read `kb/index.md` to see the subjects, then follow the indexes down to the folder the information most likely belongs to. Don't read the whole KB; the indexes tell you which files exist and what each covers.

2. **Route to a folder.** Split mixed information along these lines rather than filing it all in one place.
   - **A subject:** information goes in its top-level subject folder (`aws/`, `data-engineering/`, `ai-engineering/`, `javascript/`, `python/`, `css/`, `software-architecture/`, …). If the folder doesn't exist, create it with its index (`<subject>/<subject>.md`) and add it to the Subjects section of `kb/index.md`.
   - **Concept vs vendor:** a concept that holds regardless of vendor (ETL vs ELT, CDC, columnar formats, partitioning) goes in the vendor-neutral folder, such as `data-engineering/`. How a vendor implements it goes in the vendor's folder and links back to the concept file. If one note mixes both, split it.
   - **An AWS service:** facts about one service go in `aws/aws-services/<category>/<service>.md`, whichever track they came up in. Pick the category folder from `aws/aws-services/aws-services.md`; a service that belongs to two or more categories goes in `aws-general-services/`. Create the file, with the shape `AGENTS.md` sets for service files (What it is, Characteristics, Example, Related), when the service first comes up. Comparisons and pick-rules go in the track's `choosing-*` files, not the service file.
   - **A certification or track:** exam facts, domains, study progress, how services combine, and exam traps go in the track's folder, such as `aws/aws-data-engineering/`. Link to service and concept files instead of repeating their facts.
   - **A term or abbreviation:** goes in `context.md`, following `references/glossary-format.md`. Link the entry to the topic file that explains it.
   - **A link:** goes in `links.md` under the right heading, pointing to the topic file that explains it. The durable facts behind it go in that topic file.
   - **A decision about how *this KB* is run:** goes in `docs/adr/`, following `references/adr-format.md`. Write an ADR only when the decision is hard to reverse, surprising without context, and the result of a real trade-off.

   Folder names must be unique across the KB, because each folder's index is named after it. Prefix a subfolder with its parent when the bare name could collide (`aws-data-engineering/`).

3. **Route to a file.** Every topic gets its own file. If an existing file is about exactly this topic, add to it. Otherwise create a new kebab-case file named for the subject (`batch-vs-streaming.md`, `glue.md`, not `notes-oct.md`), even if the topic only came up briefly. Don't fold a distinct topic into a broader file, and never create a file with no content. When a file grows too big to read in one sitting, or holds several distinct subtopics, promote it to a folder named after the topic. Split its content into topic files inside that folder, make the folder index (`<topic>/<topic>.md`) the reading guide to them, and update every link to the old file.

4. **Sanity-check what's checkable.** If a claim looks wrong or outdated against what you know of the official documentation (a service limit, a default, a feature that was renamed), say so and ask before saving it. Don't silently correct it. If the user asks you to verify against official docs, cite what you checked.

5. **Reconcile before writing.** Check whether the new information contradicts anything already in the target file, or in a related file the index points to. If it does, stop: quote the existing text, name the difference, and get confirmation before touching anything. Never overwrite silently. If there's no conflict, write it in without asking.

6. **Write current state only.** State the fact as it is now. Never note what it used to say, when it changed, or why. No "(previously X)", no dated session entries: `git log -p <file>` and the commit message are the changelog (`docs/adr/0001-git-history-as-changelog.md`). Study progress is a current snapshot, such as which domains are covered and what still needs review.
   - When the information comes with external resources (a YouTube video, an AWS doc, an article), list them in a `## Sources` section right after the file's one-line statement (`- [Title](url): what it is.`) and add them to `links.md`. Notes the user shares directly need no source tag, and a file with no external resources gets no Sources section.
   - For an external resource, extract the durable facts in your own words and link back rather than pasting in a copy.
   - Put images in the folder's `images/`, named `<topic>-<yyyy-mm-dd>.<ext>`, and link them from the topic file.
   - Cross-reference related KB files with relative markdown links, never backticked paths or `[[wikilinks]]`. Every link says how the two things relate (direction and mechanism), per `AGENTS.md`'s "Every link explains the relationship" rule. When you add a relationship, add the matching explained link on the other file's side too.
   - Make it visual: tables for comparisons, ASCII diagrams for flows, timelines for things that happen over time, and sample rows for what data looks like, per `AGENTS.md`'s "Show, don't only tell" rule.
   - Keep ASCII diagrams within 72 columns.
   - Match the style already in the file.
   - Open a new file with a one-line statement of what it covers.

7. **Update the indexes.** Do this in the same change, whenever you add, rename, split, or move anything:
   - Update the parent folder's index entry, in the form `- [file.md](file.md): what it covers. Read when: <the kind of question it answers>.`
   - **Keep the index a reading guide.** Place the file at its spot in the index's reading order, under the right group label. Touch the `## How to read this folder` lines (Before, Order, After) only if the new file changes them. Don't repeat the file list or relationships already in Related sections (`AGENTS.md`, "Indexes are reading guides"). A new folder's index gets this section from the start.
   - **`kb/index.md` lists only subject folders and reference files.** Touch it only when a subject folder is created or renamed.
   - When a file's scope grows, refresh its entry: a stale "Read when" sends the next agent to the wrong file.
   - Replace a folder's `_None yet_` placeholder once it has its first file.

8. **Offer to commit.** Don't commit unless the user asks. Write the commit message as the changelog entry it is: what was recorded, and where it came from (`Intake Kinesis shard limits from DEA-C01 course section 3`).

Intake is done when all of these are true:

- The information sits in exactly one place, with pointers elsewhere at most.
- Vendor-neutral concepts and vendor-specific facts are in their own folders, linked.
- External resources it came with are linked in the file's Sources section and in `links.md`.
- No conflict is left unresolved.
- The file's folder index lists it in reading order, and new terms and links are in `context.md` and `links.md`.
