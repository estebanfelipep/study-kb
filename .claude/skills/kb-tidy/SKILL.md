---
name: kb-tidy
description: Tidy this study knowledge base without adding knowledge. Links files that are missing from their folder indexes, fixes file and image names to the KB's conventions, adds Related links the existing text already justifies, gives a newly named member of a pattern collection (an AWS service, a glossary term, an external link) its file or list entry, and spots redundancies (the same fact in two files, duplicate or near-duplicate folders, comparisons sitting in service files), reporting them for the user to decide. Use whenever the user asks to organize, tidy, clean up, link, index, or check recent commits or notes they wrote by hand, asks what's missing from the indexes, or asks where the KB repeats itself, even if they don't say "tidy". Prefer it over kb-intake when the content is already in the KB and only needs organizing.
---

# Tidy the knowledge base

This skill organizes what the user already wrote. It does not add knowledge. The user writes notes by hand, often quickly and outside the KB's conventions, and wants them wired into the KB with a **low blast radius**: small, reviewable changes, their wording untouched, and nothing invented.

That's the main difference from `kb-intake`, which is for new information. If you catch yourself writing a sentence that states a fact the KB didn't already contain, stop: that's intake, and the user didn't ask for it.

Paths below are relative to the repo root. `AGENTS.md` holds the KB's conventions (index entry format, folder rules, naming); this skill applies them, it doesn't repeat them.

## 1. Find the scope

Work out which files the user means:

- **"The last N commits"**: `git log -n N --stat --format='%h %s'` for the files they touched.
- **Uncommitted work**: `git status --short`, including untracked files and folders. The user often creates new notes and folders without committing.
- **"The whole KB"**: everything under `kb/`.

The user may be editing the KB at the same time. Read a file right before you edit it, and treat anything new on disk as theirs.

## 2. Run the audit script

```bash
python3 .claude/skills/kb-tidy/scripts/kb_audit.py kb --scope <paths in scope>
```

The script is read-only and takes well under a second. It reports:

| Check | What it finds |
| --- | --- |
| Index coverage | Files and subfolders their folder index doesn't list, and folders with no index |
| Broken links | Relative links whose target doesn't exist |
| Naming | Images not named `<topic>-<yyyy-mm-dd>.<ext>`, markdown files not in kebab-case |
| Files without a title | Raw notes with no `# Title` line, a sign they haven't been shaped yet |
| Folder names | A folder name used twice, or similar names that aren't parent and child |
| Near-duplicate sentences | Sentences that read almost the same in two files |

`--scope` limits only the duplicate check, so old duplicates elsewhere don't drown out the new ones. The other checks always cover the whole KB, because a new file can break an index anywhere. Without `--scope`, it checks every pair.

The script is a starting point. Read the files it flags, and the files in scope, before deciding anything.

## 3. Apply the small fixes

Apply only these. Each is mechanical and easy to review in a diff:

- **Missing index entries.** Add an entry in the format `AGENTS.md` gives, at its place in the index's reading order. Describe only what the file actually says: an index entry that promises more than the file holds sends the next reader to the wrong place. Fix an existing entry that's in the wrong format, such as `[bedrock](bedrock.md)` with no "Read when".
- **Parent index summaries.** When a folder gains files, update the one-line summary of that folder in its parent index, such as the `aws-ai/` line in `aws-services.md`. Touch `kb/index.md` only when a subject folder is new.
- **Renames to convention.** A file named after the wrong thing (`text-extract.md` for Amazon Textract) or a screenshot with its default name. Use `git mv`, so the rename is tracked rather than shown as a delete plus an untracked file. Then update every link to the old name (`grep -rn "old-name" kb/`). URL-encoded spaces (`%20`) count as links.
- **New members of a pattern collection.** Some parts of the KB are collections with one entry per item: a file per AWS service in `kb/aws/aws-services/<category>/`, a term per entry in `kb/context.md`, a URL per line in `kb/links.md`, and any folder or list where every sibling follows the same shape. When a note in scope names an item that belongs to one of these collections but has no entry yet, such as a new AWS service mentioned in passing, add the entry. The audit script doesn't catch these, so read the files in scope for them.
	- **The KB says something about the item:** create the entry from what the KB already says, and nothing more. For an AWS service, create its file in the right category folder (or `aws-general-services/` for a service in two or more categories), in the service file shape `AGENTS.md` gives. Fill only the sections the existing text supports, and leave out the rest. Add the file to its folder index, and the category folder to `aws-services.md` if it's new. Then link the mention in the note to the new file, with a Related bullet if the note has a Related section. Leave the note's own text as written, and report the overlap under **Redundancies**, so the user decides whether to trim it.
	- **The KB only names the item:** don't create anything. An entry with nothing in it is a placeholder, which `AGENTS.md` forbids, and filling it from general knowledge is intake. Report it under **Needs your call** instead.
- **Related links the KB already justifies.** Add a Related bullet only when the relationship is already stated in the text of one of the two files. Word the bullet from that text, as `AGENTS.md` requires (direction and mechanism). If you'd have to explain the relationship from your own knowledge, don't add it: list it as a suggestion instead.

Don't change the user's prose, bullet style, indentation or headings, even when they don't match `AGENTS.md`'s file shapes. Reshaping notes is the user's call; mention it in the report instead.

## 4. Report everything else, and change none of it

These all need the user's judgment, or they lose or move content:

- **Redundancy.** The same fact in two files breaks `AGENTS.md`'s "record each fact once" rule. For each one, quote both passages with their paths, say which file should own the fact by the KB's rules (concept file vs vendor file, service file vs `choosing-*` file), and propose the fix. Not every near-duplicate is a problem: a `choosing-*` file restating a service's characteristic to explain a pick is often fine. Say which kind each one is.
- **Duplicate or competing folders,** such as a new top-level folder covering a subject `kb/index.md` already lists, or `aws/aws-ai/` beside `aws/aws-services/aws-ai/`. Propose which one survives and what moves.
- **Content in the wrong place,** such as a comparison or analogy inside a service file that belongs in a `choosing-*` file.
- **Notes outside the file shape:** no title, no Related section, raw bullets.
- **Collection items named but not described,** such as a service the KB names with nothing said about it. List each with where it's named, so the user can add it through `kb-intake`.
- **Claims that look wrong.** Flag them with why, and leave them as written.
- **Deletions.** Never delete a file or folder, even an empty or duplicate one. Uncommitted files have no copy in git, so a delete can't be undone; the permission system blocks it for the same reason. Give the user the exact command to run instead.

## 5. Verify

Rerun the audit script. Index coverage, broken links and naming should be clean for the files in scope; anything left over goes in the report with the reason. Check `git diff --stat`: the changes should be small, mostly index lines, renames and new collection entries. If a content file changed by more than a link or two, re-read the diff and undo what wasn't one of the small fixes.

Don't commit. The user reviews and commits.

## 6. Report

Keep it short, in this shape:

```
**Done**
- <each change, one line: file, what changed>

**Redundancies** (not changed)
- <file A> and <file B> both say "<quote>". <Which should own it, and the fix.>

**Needs your call**
- <folder clashes, misplaced content, unshaped notes, suspect claims, deletions with the command to run>
```

Leave out a section that has nothing in it. Don't list the checks that passed.

## Example

The user committed `bedrock.md`, `polly.md` and `text-extract.md` by hand, and said: "link what's missing in the index files, don't add content".

- **Done:** added `textract.md` and `polly.md` to `aws-ai.md`, and put the Bedrock entry in the index format. Updated the `aws-ai/` line in `aws-services.md`. Renamed `text-extract.md` to `textract.md` with `git mv`. Renamed `Screenshot 2026-09-20 at 10.30.48 AM.png` to `bedrock-guardrails-2026-09-20.png`, and updated its link in `bedrock.md`. `textract.md` says extracted text can be passed to Amazon Comprehend for entity detection, and Comprehend has no file, so created `aws-ai/comprehend.md` from that sentence, listed it in `aws-ai.md`, and linked the mention to it.
- **Redundancies:** the Comprehend sentence now lives in `textract.md` and `comprehend.md`. Suggest trimming `textract.md` to the link.
- **Needs your call:** `polly.md` names Amazon Transcribe but says nothing about it, so no file was created; add it through `kb-intake`. `sagemaker.md` now holds a SageMaker vs Bedrock comparison, which belongs in `choosing-delivery-services.md`. `bedrock.md` says fine-tuning goes "through SageMaker", but Bedrock fine-tunes natively. A new top-level folder competes with a subject `kb/index.md` already lists.
- **Not done:** rewriting the notes into service-file shape, or adding facts about Bedrock. The user didn't ask for either.
