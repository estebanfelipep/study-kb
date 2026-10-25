# cross-project — index

This folder is for anything true of two or more of the projects at once. It covers:

- **The contracts between the repos:**
  - the endpoints one repo calls on another
  - the payload, event, or schema shapes they exchange
  - the shared secrets and env vars that must match
  - shared packages one repo publishes and others install
- **Workflows that span repos:**
  - linking one repo locally into another
  - releasing a shared package and bumping it in its consumers
  - shipping a change that needs PRs in several repos, and in what order

When a fact lives on one side of a contract, record the contract here. In each affected project's index, add a one-line pointer to the file here. Never put a second copy of the contract in a project folder.

## Files

_None yet. Content arrives through the `kb-intake` skill._
