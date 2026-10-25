# Progressive disclosure through layered folder indexes

Inside `kb/`, knowledge is filed in one folder per subject (`aws/`, `data-engineering/`, `python/`, …), with subfolders as a subject grows. Navigation follows the same layers. `kb/index.md` lists only the first layer: the subject folders and the reference files at the top of `kb/`. Each folder has an index note named after it (`aws/aws.md`) that lists only its own files and subfolders, with what each covers and when to read it. An agent reads the root, picks a subject, and follows the indexes down to the files it needs.

Because the KB is also studied by a person, each index is a reading guide too: what to read before the folder, why its files are in the order they're listed, and where to go next. Questions that span folders, such as a concept in `data-engineering/` and its AWS service in `aws/`, are bridged by each file's Related links and by the indexes' Before and After lines, not by the root.

Every topic gets its own file as soon as it comes up, even a small one. Small files keep each topic findable by name and each graph node meaningful. When a file grows too big, it becomes a folder named after the topic, and the folder index guides the reader through the split-out files.

The cost is one or two extra index reads before reaching a file, and no single entry for a subject that spans folders. In exchange the root stays short and never goes stale when deeper files move.

## Considered options

- **A root topic map that links every file under the subjects people ask about.** Rejected: it repeats what the folder indexes already say, grows with every file, and needs updating whenever a deep file moves.
- **Folders by certification exam domain.** Rejected: one service (Glue, for example) shows up in several domains, so its facts would scatter. Service files with a domain map in the certification's folder give domain-first study without duplication.
- **One flat folder, with the README as the index.** Rejected: once the KB spans several subjects, choosing a file from one long list gets slow and error-prone.
- **An `index.md` in every folder.** Rejected: every index gets the same name. In search results, editor tabs, and Obsidian's graph they can't be told apart without opening them. The top of `kb/` keeps `index.md` because it is the one place navigation starts, so its name stays unique.
- **Broad files, split only once they're slow to search.** Rejected: a topic mentioned briefly gets buried in a broader file, where its name can't be found and the reader can't see it as its own subject.
- **Indexes as plain alphabetical lists.** Rejected: they tell a reader what exists but not where to start or how the pieces build on each other.
- **Folder indexes that list their whole subtree.** Rejected: they duplicate the child indexes and go stale. Each folder index lists only its own folder.
