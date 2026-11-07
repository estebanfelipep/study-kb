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

- **`workspace.json` changes whenever a tab or pane moves.** Commit it only when the layout is worth keeping, not alongside unrelated changes.
- **Any plugin's `data.json` is committed automatically**, because `.gitignore` allows every `data.json`. Open a new plugin's `data.json` before committing and check it holds no token or API key.
- **Plugin versions are not pinned.** A new machine installs the current release.

## Related

- [plugins.md](plugins.md): lists, per plugin, which of these files it uses and what it needs that the repo doesn't carry.
- [new-machine-setup.md](new-machine-setup.md): the checklist that fills in what this file says is not committed.
