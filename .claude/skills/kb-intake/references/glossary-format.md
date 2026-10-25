# Glossary format

`context.md` holds the shared vocabulary: domain terms, abbreviations, codenames, and the names people actually say in meetings.

## Entry shape

Entries sit under `## Language`, sorted alphabetically, one paragraph each:

```
**TERM**: Expansion, if it's an abbreviation. What it means here, in one or two sentences. See [topic.md](path/to/topic.md).
_Avoid:_ alias-1, alias-2
```

- **Define the term as this KB uses it,** not its dictionary or industry meaning, when the two differ.
- **Link to the topic file** that explains the concept in depth. The glossary defines; topic files explain.
- **`_Avoid:_`** lists synonyms, old names, and near-misses that refer to the same thing. Future writing should use the headword, and an agent searching for an alias still lands here. Leave the line out when there are none.
- **If one word means different things in different subjects,** give each meaning its own entry, qualified in the headword: `**Partition (S3)**`, `**Partition (Kafka)**`.

## Optional sections

Add these below `## Language` once they're useful:

- `## Relationships`: bullets on how the core terms relate. For example, "A **Stream** has one or more **Shards**."
- `## Flagged ambiguities`: terms used inconsistently across sources, with the agreed usage once it is resolved.
