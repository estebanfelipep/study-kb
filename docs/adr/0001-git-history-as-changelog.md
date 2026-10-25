# Git history is the KB's changelog

KB files state only what is true now. They never say what a fact used to be, when it changed, or what it replaced. Notes like "(previously X)" pile up and bury the current answer under its own history. Meanwhile `git log -p <file>` and `git blame` already record every change in full, so keeping a second record inside each file would just give the two a chance to drift apart.

The cost is that the commit message is the only place the *why* lives. Every commit has to say why the change was made and where the information came from, such as a meeting, a person, a doc, or a verification against source.
