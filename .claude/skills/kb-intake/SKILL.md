---
name: kb-intake
description: Intake new information into this knowledge base. That includes notes, meeting details, decisions, gotchas, workflows, links, external resources, or direct statements. The skill verifies the information against source, routes it to the right folder and file, reconciles it against what's already written, and keeps every index, the glossary, and the links file current. Use whenever the user shares anything about the documented projects, how they connect, or the people and processes around them that should be recorded here.
---

# Intake for the knowledge base

Assume everything the user shares is worth intaking, and don't filter it for relevance. Resolve the repo variables first: `set -a; source .env; set +a`.

Paths to KB content in this skill (`index.md`, `context.md`, `links.md`, `cross-project/`, `org/`, and project folders) are relative to `kb/`. `docs/`, `.env`, `.env.example`, and `scratch/` are at the repo root.

Work through intake in order:

1. **Orient.** Read `kb/index.md` to see the existing topics, then the index of the folder the information most likely belongs to. Don't read the whole KB; the indexes tell you which files exist and what each covers.

2. **Route to a folder.** Split mixed information along these lines rather than filing it all in one place.
   - **One project:** information true of one project goes in that project's folder. Check the project's declared **depth** first. For a black-box project, record only the integration surface: what it exposes, how the documented projects depend on it, who owns it, and a repo pointer. Never record its internals (`docs/adr/0003-depth-per-project.md`). If the user shares internals of a black-box project, say you're leaving them out and why.
   - **Two or more projects:** information that spans repos goes in `cross-project/`. That covers a contract (an endpoint one calls on another, a payload or schema shape, a shared secret or env var that must match, a shared package) and a workflow (local linking, releasing and bumping consumers, a change needing PRs in several repos). Record the contract once, there, and add a one-line pointer in each affected project's index. If `cross-project/` doesn't exist, create it from `.claude/skills/kb-add-project/references/cross-project-index.md`.
   - **Org knowledge:** teams, ownership, people's roles, initiatives, and processes not tied to a project's code go in `org/`. Create it, with its index (`org/org.md`), the first time.
   - **A term or abbreviation:** goes in `context.md`, following `references/glossary-format.md`. Link the entry to the topic file that explains it.
   - **A link:** goes in `links.md` under the right heading, pointing to the topic file that explains it. The durable facts behind it go in that topic file.
   - **A decision about how *this KB* is run:** goes in `docs/adr/`, following `references/adr-format.md`. Decisions about the projects themselves don't go there. Write an ADR only when the decision is hard to reverse, surprising without context, and the result of a real trade-off.

3. **Route to a file.** Within the folder, pick the existing topic file closest to the information. If nothing fits, create a new kebab-case topic file named for the subsystem (`checkout-flow.md`, not `notes-oct.md`). Don't force the information into a poor fit. Files start broad. Split a topic into its own file only once a shared file has grown slow to search. Promote related files into a subfolder, with its own index (`<folder>/<folder>.md`), once a topic has several of them.

4. **Don't duplicate the source repo's own docs.** The folder's index lists what the repo already maintains, under "Docs in the source repo". If the information is already written there, record only a pointer and a one-line gist (`$WEB_REPO/docs/adr/0007-…md: the API owns session expiry`). Don't copy it; the repo's copy is the one that gets maintained. If the information contradicts the repo's docs, say so: one of them is stale, and the user should decide which.

5. **Verify what's checkable.** If the information makes a claim about code in a documented repo, grep or read the source to check it. For a black-box repo, check only its integration surface. Cite what you confirmed it against, written relative to its variable (`$API_REPO/src/routes/orders.ts`), with the line number for a single definition. For a cross-project claim, check both sides of the contract. If the code contradicts the claim, say so instead of saving it as stated. Note which branch you read when it isn't the default branch. Skip verification for anything that can't be checked in code: decisions, plans, opinions, org facts, links.

6. **Reconcile before writing.** Check whether the new information contradicts anything already in the target file, or in a related file the index points to. If it does, stop: quote the existing text, name the difference, and get confirmation before touching anything. Never overwrite silently. If there's no conflict, write it in without asking.

7. **Write current state only.** State the fact as it is now. Never note what it used to say, when it changed, or why. No "(previously X)", no "(supersedes Y)": `git log -p <file>` and the commit message are the changelog (`docs/adr/0001-git-history-as-changelog.md`).
   - Tag an inline source when the information traces to a person, meeting, or external resource (`_(source: Oct 10 planning sync)_`), or to your own verification (`_(verified against source, 2026-10-10)_`).
   - For an external resource, extract the durable facts and link back rather than pasting in a copy.
   - Put images in the folder's `images/`, named `<topic>-<yyyy-mm-dd>.<ext>`, and link them from the topic file.
   - Cross-reference related KB files with relative markdown links, never backticked paths or `[[wikilinks]]`. A link between two topic files is an edge in the graph, and the next agent can follow it.
   - Match the style already in the file.
   - Open a new file with a one-line statement of what it covers.

8. **Update the indexes.** Do this in the same change, whenever you add, rename, split, or move anything:
   - Update the parent folder's index entry, in the form `- [file.md](file.md): what it covers. Read when: <the kind of question it answers>.`
   - **Update the topic map in `kb/index.md`.** List the file under every top-level topic it covers. If no topic fits, add one. Name it for the subject people ask about ("Checkout", "Authentication"), never for a repo or folder. Keep topics top-level: a new aspect of an existing subject joins that topic rather than becoming a new one. When a topic's scope grows, refresh its description and "Read when".
   - When a file's scope grows, refresh its entry: a stale "Read when" sends the next agent to the wrong file.
   - Replace a folder's `_None yet_` placeholder once it has its first file.

9. **Offer to commit.** Don't commit unless the user asks. Write the commit message as the changelog entry it is: what was recorded, and where it came from (`Intake checkout retry policy from Oct 10 payments sync`).

Intake is done when all of these are true:

- The information sits in exactly one place, with pointers elsewhere at most.
- It respects the project's depth.
- It is verified where checkable and source-tagged where it traces to someone.
- No conflict is left unresolved.
- The file's folder index lists it, every topic it covers in `kb/index.md` links to it, and new terms and links are in `context.md` and `links.md`.
