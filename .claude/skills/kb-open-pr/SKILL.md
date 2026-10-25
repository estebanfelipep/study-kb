---
name: kb-open-pr
description: Open or finish a draft PR on any repo this knowledge base documents. Follows the target repo's own PR conventions when it has them, and adds testing steps a cold reviewer can follow (including the gate a reviewer has to get past to reach the change), project-aware Evidence and Merge Danger sections, and cross-repo checks drawn from the KB's cross-project contracts. Use when the user wants a PR opened on a documented repo, testing steps or a PR body written, a recording or screenshots turned into repro steps, or an existing PR body tightened.
---

# Opening a PR on a documented repo

## 0. Orient

Resolve the repo variables (`set -a; source .env; set +a` in this KB), and work out which documented repo the branch is in.

Then read this KB's `kb/index.md` (the topics the change touches, and the repo's entry), that project's index (`<project>/<project>.md`), and `kb/cross-project/cross-project.md`. Open any file they list about testing, workflows, environments, gates, releases, or contracts. If the KB doesn't cover something you need, derive it from the code. Once the PR is open, offer to record what you learned through `kb-intake`.

**The target repo's own conventions win.** Look for the following and, where they exist, treat them as the base. Everything below adds to them; it does not replace them.

- a PR template (`.github/pull_request_template.md`, `.gitlab/merge_request_templates/`)
- `CONTRIBUTING.md`
- a repo PR skill or runbook (`.claude/skills/*pr*`, `docs/`)
- title rules, such as a ticket-key prefix taken from the branch name

Take the base branch from the host (`gh repo view --json defaultBranchRef`, or the GitLab equivalent). Never assume `main`.

_Done when you know the repo, the base branch, the repo's own conventions, and which KB files apply._

## 1. Base steps

Follow these unless the repo's own runbook says otherwise:

1. **Check for an existing PR** on this head branch (`gh pr list --head <branch>`). If one exists, update it instead of opening another.
2. **Push** the branch with upstream tracking.
3. **Write the title.** Use the repo's convention. Otherwise write a short imperative summary, prefixed with a ticket key if the branch name contains one.
4. **Write the body** to `scratch/<branch>-pr-body.md` using the repo's template, or this one if it has none:

   ```
   ## Summary
   ## Evidence
   ## How to test
   ## Merge Danger
   ```

5. **Open it as a draft:** `gh pr create --draft --base <base> --title "<title>" --body-file scratch/<branch>-pr-body.md`.

The body follows the `AGENTS.md` rule on outward-facing content: never cite or link this KB.

## 2. Cross-repo checks

Do these before composing the body. They are the reason this skill reads the KB first.

- **Contracts.** If the diff touches either side of a contract recorded in `cross-project/`, read the other side's code. In Merge Danger, say whether the two sides still match. If they don't, state which repo has to ship first. Contracts include endpoints, payload and schema shapes, shared secrets and env vars, and serialized formats.
- **Shared packages reach consumers only after a release.** If the diff changes something a shared package exports, the blast radius covers every consumer. Grep each consumer repo for imports of the changed paths and name the call sites. Say whether the change needs a release, and whether it breaks an existing export.
- **A consumer that depends on unreleased work can't merge yet.** If the branch uses something that exists only in an unreleased version or a local link of another documented repo, Merge Danger names the PR or release it waits on.
- **Don't ship local link debris.** If `package.json`, a lockfile, or a workspace file gained an override or path pointing at a local clone, stop and tell the user.

_Done when every affected repo is named, and any merge-order dependency is written down._

## 3. How to test

Derive the steps from the code rather than asking the author to write them. The author's version reliably omits setup they've stopped noticing.

Write for a **cold** reviewer: someone who opens the preview link with none of your local state, and who will conclude the fix didn't land if a single step is missing.

### Find the gate

A cold reviewer can't test what they can't reach. Before writing any step, find what stands between the URL and the state under test: the **gate**. Read the code path and find the conditional that selects the branch under test; it names the gate. Check the project's KB folder for gates already recorded. Typical gates:

- **Environment.** Some behavior runs only in production, only in dev, or only behind a flag. Check how the code reads its env vars, and whether a preview deploy actually hits the branch under test.
- **Auth.** An admin-only page, a role, or a test account.
- **Content or data state.** A record that must exist, be published, or be in a specific state. A cache that only changes after revalidation. Anything a migration or seed has to create first.
- **External config.** A feature flag, remote config, or managed prompt that lives outside the repo, or a dependency that is linked rather than released.

Done when every step's precondition is either a click a cold reviewer can make, or a setup step written into the steps.

### Ask for evidence, then mine it

Offer the author both of these, and say which one earns its keep:

- **A recording.** Ask for this one for any behavior change. It captures the gate, which is exactly what authors leave out when they describe setup in prose.
- **Before/after screenshots.** These are enough for a pure copy, layout, or styling change.

A video already uploaded to the PR is an asset URL you cannot read. Ask for the local file and sample it:

```bash
ffmpeg -i <file> -vf fps=1 "$TMPDIR"/f%03d.jpg                                              # sample, then read the frames
ffmpeg -ss <sec> -i <file> -vf "crop=W:H:X:Y,format=yuvj420p" -vframes 1 "$TMPDIR"/c.jpg    # crop for small text
```

Crop anything text-heavy: URLs, config values, and inline errors are unreadable in a full-frame sample. Write the steps from what the frames show.

### Verify every literal

Check every path, route, env var, field name, and expected string in the steps against source before it ships. A wrong literal is worse than a missing one, because it sends a cold reviewer hunting in the wrong place.

### Write them

- **Step 1 is always reaching the change.** That means the preview URL, a story or sandbox, or the steps to see it in a consumer.
- Use one bolded, numbered action per step. No sub-headings and no prose paragraphs.
- Quote expected strings verbatim, and name the wrong one too, so "wrong" is recognizable.
- Any setup or override carries its own teardown in the same step.

## 4. Evidence and Merge Danger

- **One-way doors.** Each of these is a one-way door. Say so, and say what rolling back would take:
  - a schema or data migration
  - a published package version
  - a change to a contract another repo already depends on
  - anything that sends messages or emails, or charges money
- **Blast radius.** List the consumers and call sites, the routes or screens affected, and any data that needs a backfill, re-save, re-index, or cache refresh.

## Ticking boxes

Deriving the steps saves effort. Ticking a box nobody walked through is a false claim. **Tick a checklist box only on an explicit confirmation for that box.** Author-supplied evidence confirms only what it visibly shows: a recording made on a preview deploy is not a local run, and it is not a regression pass.
