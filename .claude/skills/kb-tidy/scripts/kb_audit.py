#!/usr/bin/env python3
"""Audit the KB's structure: index coverage, broken links, naming, and duplicated text.

Usage: python3 .claude/skills/kb-tidy/scripts/kb_audit.py [kb_dir] [--scope PATH ...]

Read-only. Prints a report grouped by check. --scope limits the duplicate-text
check to pairs where at least one file is under one of the given paths, so a
review of recent changes doesn't drown in old duplicates.
"""
import os
import re
import sys

from itertools import combinations

LINK = re.compile(r"\]\(([^)\s]+?)\)")
ENTRY = re.compile(r"^- \[[^\]]+\]\(([^)\s]+)\)", re.M)
IMAGE_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*-\d{4}-\d{2}-\d{2}\.[a-z0-9]+$")
KEBAB_MD = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")


def md_files(kb):
    for root, dirs, files in os.walk(kb):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(root, f)


def index_of(folder, kb):
    if os.path.abspath(folder) == os.path.abspath(kb):
        return os.path.join(kb, "index.md")
    return os.path.join(folder, os.path.basename(folder) + ".md")


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_indexes(kb):
    out = []
    for root, dirs, files in os.walk(kb):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d != "images")
        idx = index_of(root, kb)
        rel_root = os.path.relpath(root, kb)
        if not os.path.exists(idx):
            out.append(f"{rel_root}/: no index file ({os.path.basename(idx)})")
            continue
        listed = {os.path.normpath(os.path.join(root, l))
                  for l in ENTRY.findall(open(idx).read())}
        children = [os.path.join(root, f) for f in files
                    if f.endswith(".md") and os.path.join(root, f) != idx]
        children += [index_of(os.path.join(root, d), kb) for d in dirs]
        for c in sorted(children):
            if os.path.normpath(c) not in listed:
                out.append(f"{os.path.relpath(idx, kb)}: doesn't list {os.path.relpath(c, kb)}")
    return out


def check_links(kb):
    out = []
    for f in md_files(kb):
        text = strip_code(open(f).read())
        for target in LINK.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target) or "." not in target \
                    or target == "path/to/topic.md":
                continue
            path = target.split("#")[0].replace("%20", " ")
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), path))):
                out.append(f"{os.path.relpath(f, kb)}: broken link {target}")
    return out


def check_names(kb):
    out = []
    for root, dirs, files in os.walk(kb):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), kb)
            if os.path.basename(root) == "images":
                if not IMAGE_NAME.match(f):
                    out.append(f"{rel}: image not named <topic>-<yyyy-mm-dd>.<ext>")
            elif f.endswith(".md") and not KEBAB_MD.match(f):
                out.append(f"{rel}: file name isn't kebab-case")
    return out


def check_shape(kb):
    """Files with no '# ' title on line 1: usually raw notes not yet shaped."""
    out = []
    for f in md_files(kb):
        first = open(f).readline()
        if not first.startswith("# "):
            out.append(f"{os.path.relpath(f, kb)}: no '# Title' on the first line")
    return out


def check_folder_names(kb):
    """Folder names that collide or nearly collide (ai/ vs ai-engineering/)."""
    names = {}
    for root, dirs, _ in os.walk(kb):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "images"]
        for d in dirs:
            names.setdefault(d, []).append(os.path.relpath(os.path.join(root, d), kb))
    out = [f"folder name used twice: {', '.join(p)}" for p in names.values() if len(p) > 1]
    # A subfolder prefixed with its parent (aws/aws-services/) is the KB's
    # convention, so only flag similar names that aren't nested.
    for a, b in combinations(sorted(names), 2):
        if b.startswith(a + "-") or a.startswith(b + "-"):
            for pa in names[a]:
                for pb in names[b]:
                    if not (pb.startswith(pa + "/") or pa.startswith(pb + "/")):
                        out.append(f"similar folder names: {pa}/ and {pb}/")
    return out


def sentences(text):
    text = strip_code(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`|>#]", " ", text)
    for s in re.split(r"(?<=[.!?])\s+|\n+", text):
        s = re.sub(r"\s+", " ", s).strip(" -").lower()
        # Related bullets ("file.md: how it relates") are meant to echo each
        # other across files, so they aren't redundancy.
        if len(s) >= 70 and not re.match(r"^[\w.-]+\.md\s*:", s):
            yield s


def check_duplicates(kb, scope):
    skip = re.compile(r"(^|/)(context|links|index)\.md$")
    files = [f for f in md_files(kb) if not skip.search(f)
             and os.path.basename(f) != os.path.basename(os.path.dirname(f)) + ".md"]
    in_scope = (lambda f: True) if not scope else (
        lambda f: any(os.path.abspath(f).startswith(os.path.abspath(s)) for s in scope))
    # Index every sentence by its 4-word shingles, so only sentences that share
    # wording are compared, instead of every pair in the KB.
    items, by_shingle = [], {}
    for f in files:
        for s in set(sentences(open(f).read())):
            words = s.split()
            sh = {" ".join(words[i:i + 4]) for i in range(len(words) - 3)}
            items.append((f, s, sh))
            for x in sh:
                by_shingle.setdefault(x, []).append(len(items) - 1)
    seen, out = set(), []
    for i, (fa, sa, sha) in enumerate(items):
        counts = {}
        for x in sha:
            for j in by_shingle[x]:
                if j > i:
                    counts[j] = counts.get(j, 0) + 1
        for j, n in counts.items():
            fb, sb, shb = items[j]
            if fa == fb or (fa, fb) in seen or not (in_scope(fa) or in_scope(fb)):
                continue
            if n / len(sha | shb) >= 0.6:
                seen.add((fa, fb))
                out.append(f"{os.path.relpath(fa, kb)} ~ {os.path.relpath(fb, kb)}\n"
                           f"      \"{sa[:140]}\"")
    return out


def main():
    args = sys.argv[1:]
    scope = []
    if "--scope" in args:
        i = args.index("--scope")
        scope = args[i + 1:]
        args = args[:i]
    kb = args[0] if args else "kb"
    checks = [
        ("Index coverage", check_indexes(kb)),
        ("Broken links", check_links(kb)),
        ("Naming", check_names(kb)),
        ("Files without a title (raw notes)", check_shape(kb)),
        ("Folder names", check_folder_names(kb)),
        ("Near-duplicate sentences (review by hand)", check_duplicates(kb, scope)),
    ]
    for title, items in checks:
        print(f"## {title}: {len(items)}")
        for item in items:
            print(f"  - {item}")
        print()


if __name__ == "__main__":
    main()
