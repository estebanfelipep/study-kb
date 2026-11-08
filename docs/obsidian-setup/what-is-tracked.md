# What is tracked

Which Obsidian, Claudian and Claude Code files are committed, which are left to each machine, and why plugin code is not committed.

## Tracked and untracked files

| Path | Committed | What it holds |
|---|---|---|
| `.obsidian/app.json`, `appearance.json`, `core-plugins.json`, `graph.json` | Yes | Editor settings, theme, core plugins, graph view. |
| `.obsidian/community-plugins.json` | Yes | The ids of the enabled community plugins. It records which plugins to run, and nothing installs them. |
| `.obsidian/workspace.json` | Yes | The layout: tabs, splits, sidebars. |
| `.obsidian/plugins/<id>/data.json` | Yes | A plugin's settings, when it has the file. |
| `.obsidian/plugins/<id>/` code (`main.js`, `manifest.json`, `styles.css`) | **No** | The plugin itself. |
| `.obsidian/plugins/obsidian-git/obsidian_askpass.sh` | **No** | Helper script the Git plugin regenerates (covered by the code rule). |
| `.obsidian/cache`, `.trash/` | **No** | Local caches and deleted notes. |
| `.claudian/claudian-settings.json` | Yes | Claudian's settings. It has no `data.json`, so its settings live here. |
| `.claudian/sessions/` | **No** | Chat history, kept per device. |
| `.claude/skills/` | Yes | The repo's skills. |
| `.claude/settings.local.json` | **No** | Per-machine Claude Code permissions. |

## Why plugin code is not committed

A plugin's `main.js` is one minified file, 2.6 MB for Claudian. Every plugin update rewrites it, which makes noisy commits and unreadable diffs. Leaving it out keeps the repo small, at the cost that each new machine installs the plugins by hand ([new-machine-setup.md](new-machine-setup.md)).

## Things to keep in mind

- **`workspace.json` changes whenever a tab or pane moves, so commit it only for a deliberate layout change.** A layout change is a panel added, removed, moved or resized in the sidebars or main area. Everything else in the file is session state and never a reason to commit: open notes and diff tabs, `lastOpenFiles`, the active tab, regenerated ids, and the Claudian `conversationId`. Opening the obsidian-git diff of `workspace.json` rewrites it, so the file looks modified after you inspect it.
  - **Layout changed on purpose:** close the diff and note tabs first, so the committed layout opens clean on another machine, then commit `workspace.json` on its own with a message that names the layout change.
  - **Anything else:** leave it out of the commit, and discard it with `git checkout .obsidian/workspace.json` when it is in the way.
- **Any plugin's `data.json` is committed automatically**, because `.gitignore` allows every `data.json`. Open a new plugin's `data.json` before committing and check it holds no token or API key.
- **Plugin versions are not pinned.** A new machine installs the current release.

## Related

- [plugins.md](plugins.md): lists, per plugin, which of these files it uses and what it needs that the repo doesn't carry.
- [new-machine-setup.md](new-machine-setup.md): the checklist that fills in what this file says is not committed.
