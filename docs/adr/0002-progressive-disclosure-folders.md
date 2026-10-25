# Progressive disclosure through a topic map and per-folder indexes

Inside `kb/`, knowledge is filed in one folder per project, plus `cross-project/` for contracts and workflows that span repos. It is *found*, though, through topics. Navigation starts at `kb/index.md`, which is a map of the KB's top-level topics: the subjects people ask about, like "Checkout" or "Authentication". Each topic links to every file that covers it, in whichever folders those files live. The index never lists folders. The documented repos get a short Repos section of their own, which moves to `kb/repos.md` once there are more than three.

Every folder also has an index note named after it (`shop-web/shop-web.md`). It lists each file and subfolder in that folder, with what the file covers and when to read it. An agent picks a topic, opens only the files it lists, and reads a folder index only when it needs a file's neighbors.

The two layers answer different needs. Questions arrive as subjects, and a subject usually spans repos: "how does checkout work?" touches the storefront, the orders service, and the contract between them. A root index organized by folder makes the agent guess which repo owns the answer, and the answer is often "several". Filing, on the other hand, works best by project: a fact true of one repo has one obvious home, and a project's depth (full or black box) applies to its whole folder.

`cross-project/` exists because related projects are coupled: one calls another, or both install a shared package. Filing a contract under either side would leave the other side's reader without it, and filing it under both would create two copies that drift.

The cost is that the topic map needs upkeep: every new or moved file must be listed under the topics it covers. `kb-intake` does this in the same change as the write.

## Considered options

- **A root index that lists folders and repos.** Rejected: it routes by where knowledge is stored instead of by what people ask about. Cross-repo subjects have no single entry.
- **Topic-first folders** (`checkout/`, `payments/`, …). Rejected: depth is a per-repo property, and a fact true of one repo has an obvious home in its project folder. The topic map gives topic-first navigation without moving files.
- **One flat folder, with the README as the index.** Rejected: the index grows with every topic, and once a KB spans several projects, choosing a file from one long list gets slow and error-prone.
- **An `index.md` in every folder.** Rejected: every index gets the same name. In search results, editor tabs, and Obsidian's graph they can't be told apart without opening them. The top of `kb/` keeps `index.md` because it is the one place navigation starts, so its name stays unique.
- **Folder indexes that list their whole subtree.** Rejected: they duplicate the child indexes and go stale. Each folder index lists only its own folder.
