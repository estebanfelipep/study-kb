# All knowledge lives in `kb/`; tooling stays at the repo root

Every piece of KB content lives under `kb/`: the map (`kb/index.md`), the glossary, the links file, and every project, cross-project, and org folder. The repo root holds only what *operates* the KB: [AGENTS.md](../../AGENTS.md), `docs/` (the rules and decisions about how the KB is run, including these ADRs), the skills, the Obsidian and env config, `scratch/`, and `examples/`.

That keeps two kinds of file from mixing. An agent or a reader looking for knowledge goes to `kb/` and finds nothing but knowledge. Someone changing how the KB works goes to the root. A grep across `kb/` searches only content, and the template's scaffolding can change without touching a single knowledge file.

The cost is one more path segment everywhere: links from the root into content start with `kb/`, and links from content out to `docs/` climb out of it.

## Considered options

- **Content at the repo root** next to the config. Rejected: README, AGENTS.md, `.env.example`, and skills sit among the project folders, and nothing marks which files are knowledge.
- **ADRs inside `kb/`.** Rejected: they are rules for operating the KB, not knowledge about the projects. They belong with the other operating rules, outside the content.
- **The Obsidian vault rooted at `kb/`.** Rejected for now: rooting it at the repo keeps `AGENTS.md` and `docs/` browsable and linked in the same vault.
