# Study KB

A personal knowledge base for everything I study in software development: AWS, data engineering, AI engineering, JavaScript, Python, CSS, software architecture, and more. It also tracks progress toward certifications. The first one is the AWS Certified Data Engineer – Associate (DEA-C01).

It is plain markdown in a git repo, organized so an AI agent can navigate it. The agent loads only the files a question needs, rather than reading everything up front. It is also an Obsidian vault.

## Principles

- **Progressive disclosure, layer by layer.** [kb/index.md](kb/index.md) lists only the first layer: the subject folders and the reference files. Each folder's index note lists that folder's files, with what each covers and *when to read it*. It is also a reading guide: what to read first, the order to read the files in, how they relate, and where to go next.
- **One file per topic.** A topic gets its own file as soon as it comes up, even if it's small. When a file grows too big, it becomes a folder whose index guides you through the split-out files.
- **Filed by subject.** Each top-level folder in `kb/` is a subject (`aws/`, `data-engineering/`, …), created when its first note arrives.
- **One place per fact.** Vendor-neutral concepts (`data-engineering/`) live apart from vendor-specific facts (`aws/`), and link to each other. Each AWS service has one file, whichever track or certification it came up in.
- **Current facts only.** Files state what is true now. Git history is the changelog, including the history of study progress.
- **Answer only from what's written.** When asked what the KB says, agents name each gap rather than filling it with guesses. A gap becomes the next intake.
- **Agent-agnostic.** [AGENTS.md](AGENTS.md) holds the rules, and [CLAUDE.md](CLAUDE.md) imports it.

The reasoning behind these is recorded in [docs/adr/](docs/adr/adr.md).

## Layout

```
kb/                       ← all the knowledge, and nothing else
  index.md                ← start here: subjects and reference
  context.md              ← glossary of terms and abbreviations
  links.md                ← every external link, in one place
  aws/
    aws-services/         ← one file per AWS service, by category
      aws-analytics/      ← (and aws-databases/, aws-security/, ...)
      aws-general-services/ ← services in two or more categories
    aws-data-engineering/ ← DE track, DEA-C01 exam, choosing-* rules
  data-engineering/       ← vendor-neutral concepts
  <subject>/              ← ai-engineering, python, css, ... (on first use)

AGENTS.md                 ← rules every agent follows here
docs/adr/                 ← decisions about how this KB is run
.claude/skills/           ← kb-intake
.obsidian/                ← shared Obsidian vault settings
scratch/                  ← gitignored working files
```

## Adding content

Share anything with your agent and ask it to record it. The **`kb-intake`** skill routes it to the right folder and file, reconciles it with what's already written, and keeps every index, the glossary, and the links file current. Course notes, exam-guide facts, practice-test mistakes, links, or a plain "remember that…" all work.

## Browsing in Obsidian

Open the repo folder with **Open folder as vault**. The committed `.obsidian/` settings keep Obsidian compatible with the KB's rules:

- Links are standard relative markdown links, not wikilinks, and they update when you rename a file.
- Pasted images go to an `images/` folder next to the note.
- `scratch/` is excluded, and daily notes are off, so no stray files land in the KB.
- Each folder's index is named after the folder (`aws/aws.md`), so graph nodes read as folder names.

Personal layout state (`.obsidian/workspace*.json`) is gitignored. A hand edit in Obsidian skips reconciliation and index updates, so ask an agent to check the indexes afterwards.
