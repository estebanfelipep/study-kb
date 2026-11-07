# Community plugins

The three community plugins the vault enables, where each comes from, which settings carry over, and what each needs from the machine.

## Summary

| Plugin id | Source | Settings committed in | Needs outside the repo |
|---|---|---|---|
| `obsidian-git` | Community store | `.obsidian/plugins/obsidian-git/data.json` | `git` on the PATH, GitHub credentials. |
| `obsidian-excalidraw-plugin` | Community store | `.obsidian/plugins/obsidian-excalidraw-plugin/data.json` | Nothing. |
| `realclaudian` (shown as Claudian) | Not the store | `.claudian/claudian-settings.json` | Claude Code CLI on the PATH and logged in, Obsidian 1.13.0 or newer. |

## obsidian-git

Commits, pulls and pushes the vault from inside Obsidian.

- **Settings:** the committed `data.json` has the automatic commit, push and pull intervals set to 0, so every sync is manual. It holds no machine-specific path (`basePath` and `gitDir` are empty).
- **Needs:** it runs the system `git`, so `git` must be installed and your name and email configured. The remote is `https://github.com/estebanfelipep/study-kb.git`, so the machine needs GitHub credentials for HTTPS, such as a credential helper or a personal access token.
- **Generated file:** it writes `obsidian_askpass.sh` into its own folder on each machine.

## obsidian-excalidraw-plugin

Drawing inside notes.

- **Settings:** the committed `data.json` points at an `Excalidraw/` folder in the vault for drawings, the template, scripts and the library. That folder is not in the repo, and the plugin creates it on first use.
- **Needs:** nothing outside Obsidian.

## realclaudian (Claudian)

The chat panel that runs Claude Code with the vault as its working directory. Its manifest names it "Claudian", gives the author as Yishen Tu ([github.com/YishenTu](https://github.com/YishenTu)), and marks it desktop-only with a minimum Obsidian version of 1.13.0.

- **Install source:** the id `realclaudian` is not the same as the public Claudian plugin's id, so it may not be the store version. The exact repo or install method is not recorded here.
- **Settings:** committed in `.claudian/claudian-settings.json`, not in the plugin folder. They enable the Claude provider only, leave `cliPath` empty so the CLI is found on the PATH, and set `loadUserSettings` to true.
- **Needs:** the `claude` CLI installed and logged in. With `loadUserSettings` on, it also reads the user-level Claude Code config in `~/.claude` (global rules, memory), which belongs to each machine and is not in the repo. The repo's own skills in `.claude/skills/` do travel.
- **Per device:** chat sessions in `.claudian/sessions/` are not committed.

## Related

- [what-is-tracked.md](what-is-tracked.md): explains why the plugin code listed here is not committed and the `.gitignore` rules behind the "settings committed in" column.
- [new-machine-setup.md](new-machine-setup.md): turns the "needs" column into an ordered checklist.
