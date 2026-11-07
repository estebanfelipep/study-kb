# Obsidian setup — index

How the Obsidian config and plugins are kept consistent across machines: what the repo carries, what each plugin needs, and what to do on a fresh checkout.

## How to read this folder

- **Order:** what the repo carries, then what each plugin needs from outside it, then the checklist that combines both.
- **After:** the rules for the KB's content are in [AGENTS.md](../../AGENTS.md).

## Files

- [what-is-tracked.md](what-is-tracked.md): which Obsidian, Claudian and Claude Code files are committed and which `.gitignore` leaves out, and why plugin code stays out. Read when: changing `.gitignore`, deciding whether to commit a file under `.obsidian/` or `.claudian/`, or a setting didn't carry over.
- [plugins.md](plugins.md): the three community plugins, where each comes from, which of its settings are committed, and what it needs outside the repo. Read when: a plugin misbehaves on a machine, or adding or updating a plugin.
- [new-machine-setup.md](new-machine-setup.md): the step-by-step checklist for opening the vault on another machine so it behaves like this one. Read when: setting up a new computer.
