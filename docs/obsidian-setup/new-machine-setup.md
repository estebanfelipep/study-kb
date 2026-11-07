# Setting up a new machine

The steps to open this vault on another computer so the plugins and layout behave as they do on the main one.

## Steps

```
 install tools      clone the repo     open as vault
 (git, claude,  ->  (with GitHub   ->  (turn off Restricted
  Obsidian)          credentials)       Mode)
                                            |
        verify  <-  reload  <-  install the 3 plugins by hand
```

1. **Install the tools.** Obsidian 1.13.0 or newer, `git`, and the Claude Code CLI. Log in to `claude` once in a terminal.
2. **Clone the repo.** `git clone https://github.com/estebanfelipep/study-kb.git`. Set up GitHub credentials for HTTPS first (credential helper or personal access token), and your git name and email.
3. **Open the folder as a vault.** In Obsidian, choose "Open folder as vault". Settings, theme, the enabled-plugin list and the layout come from the clone.
4. **Turn off Restricted Mode.** Settings → Community plugins. Until you do, no community plugin loads.
5. **Install the plugins by hand,** because Obsidian does not install from the enabled list ([what-is-tracked.md](what-is-tracked.md)):
   - `obsidian-git` and `obsidian-excalidraw-plugin`: Community plugins → Browse.
   - `realclaudian` (Claudian): from its own source ([plugins.md](plugins.md)), into `.obsidian/plugins/realclaudian/`.
6. **Reload Obsidian** so the plugins load with their committed settings.
7. **Verify:**
   - The Git plugin shows the branch and can fetch.
   - Claudian opens in the right sidebar and finds the `claude` CLI.
   - The layout matches. If a plugin pane is missing, restore the layout with `git checkout .obsidian/workspace.json` and reload.

## What stays different on a new machine

- Plugin versions are whatever is current at install time.
- Claudian's chat history (`.claudian/sessions/`) starts empty.
- User-level Claude Code config in `~/.claude`, including global rules and memory, is not in the repo.

## Related

- [plugins.md](plugins.md): gives the reason behind each tool in step 1 and where each plugin in step 5 comes from.
- [what-is-tracked.md](what-is-tracked.md): the list of what the clone in step 3 brings and what it leaves out.
