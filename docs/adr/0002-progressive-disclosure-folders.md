# Progressive disclosure through a topic map and per-folder indexes

Inside `kb/`, knowledge is filed in one folder per subject (`aws/`, `data-engineering/`, `python/`, …), with subfolders as a subject grows. It is *found*, though, through topics. Navigation starts at `kb/index.md`, which is a map of the KB's top-level topics: the subjects people ask about, like "Streaming ingestion" or "Data warehousing". Each topic links to every file that covers it, in whichever folders those files live. Below the topics, a short Subjects section lists the top-level subject folders.

Every folder also has an index note named after it (`aws/aws.md`). It lists each file and subfolder in that folder, with what the file covers and when to read it. An agent picks a topic, opens only the files it lists, and reads a folder index only when it needs a file's neighbors. Because the KB is also studied by a person, each index is a reading guide too: what to read before the folder, the order to read its files in, how they relate, and where to go next. Files are listed in that order.

Every topic gets its own file as soon as it comes up, even a small one. Small files keep each topic findable by name and each graph node meaningful. When a file grows too big, it becomes a folder named after the topic, and the folder index guides the reader through the split-out files.

The two layers answer different needs. Questions arrive as subjects, and a subject often spans folders: "how does streaming work?" touches the vendor-neutral concept in `data-engineering/`, the Kinesis file in `aws/aws-services/`, and the exam angle in `aws/aws-data-engineering/`. Filing, on the other hand, works best by subject and vendor: a fact about one AWS service has one obvious home in that service's file.

The cost is that the topic map needs upkeep: every new or moved file must be listed under the topics it covers. `kb-intake` does this in the same change as the write.

## Considered options

- **A root index that lists folders.** Rejected: it routes by where knowledge is stored instead of by what people ask about. Subjects that span folders have no single entry.
- **Folders by certification exam domain.** Rejected: one service (Glue, for example) shows up in several domains, so its facts would scatter. Service files with a domain map in the certification's folder give domain-first study without duplication.
- **One flat folder, with the README as the index.** Rejected: once the KB spans several subjects, choosing a file from one long list gets slow and error-prone.
- **An `index.md` in every folder.** Rejected: every index gets the same name. In search results, editor tabs, and Obsidian's graph they can't be told apart without opening them. The top of `kb/` keeps `index.md` because it is the one place navigation starts, so its name stays unique.
- **Broad files, split only once they're slow to search.** Rejected: a topic mentioned briefly gets buried in a broader file, where its name can't be found and the reader can't see it as its own subject.
- **Indexes as plain alphabetical lists.** Rejected: they tell a reader what exists but not where to start or how the pieces build on each other.
- **Folder indexes that list their whole subtree.** Rejected: they duplicate the child indexes and go stale. Each folder index lists only its own folder.
