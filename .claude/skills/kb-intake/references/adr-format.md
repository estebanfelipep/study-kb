# ADR format

ADRs in `docs/adr/` record hard-to-reverse decisions about how the KB itself is run.

## When to write one

Write an ADR only when all three of these hold:

1. **Hard to reverse.** Undoing it means restructuring files or retraining habits.
2. **Surprising without context.** A newcomer would ask "why on earth is it like this?"
3. **The result of a real trade-off.** There was a plausible alternative, and it was rejected for a reason.

If any one of these fails, the rule belongs in `AGENTS.md` or a skill, not in an ADR.

## Shape

- **File name:** `NNNN-kebab-case-summary.md`. Use the next free number, zero-padded to four digits. Never reuse or renumber.
- **Title:** `# <the decision, stated as a fact>`. For example, `# Git history is the KB's changelog`, not `# Changelog policy`.
- **Body:** one to three short paragraphs. Say what was decided, why, and what it costs. Write it in the present tense, as a standing rule.
- **Optional:** add `## Considered options`, with one bullet per rejected alternative: `**Option.** Rejected: <reason>.`

Keep it short. An ADR that needs a table of contents is two ADRs.

## Changing a decision

Edit the ADR in place so it states the current decision, and say why in the commit message. Git keeps the old version (ADR 0001). If the decision is withdrawn entirely, delete the file, remove its entry from `docs/adr/adr.md`, and leave its number unused.

Always add or refresh the entry in `docs/adr/adr.md`, in the form `- [file](file): the decision. Read when: <situation>.`
