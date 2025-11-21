#!/usr/bin/env python3
"""Remove simple duplicate PDF/MD files with numbered suffixes.

This script finds files like "name1.pdf" when "name.pdf" also exists and deletes the numbered
variant and its matching markdown (e.g. "name1.md") from the provided folders.

Usage:
    python remove_duplicates.py [--papers DIR] [--md DIR] [--yes] [--dry-run]

Defaults:
    papers: <repo root>/Papers
    md:     <repo root>/Papers md

Be careful: by default the script will ask for confirmation before deleting files unless
--yes is provided. Use --dry-run to only show what would be deleted.
"""

from pathlib import Path
import re
import argparse
import sys

DUP_RE = re.compile(r"^(?P<base>.+?)(?P<num>\d+)$")


def find_numbered_duplicates(papers_dir: Path):
    """Return list of duplicate PDF Paths where a numbered stem exists and an unnumbered counterpart exists.

    Handles common separators before the number such as space, dash, underscore or surrounding
    parentheses/brackets. Also treats PDF extension case-insensitively.
    """
    papers_dir = papers_dir.resolve()
    duplicates = []
    for p in papers_dir.iterdir():
        if not p.is_file():
            continue
        if p.suffix.lower() != ".pdf":
            continue
        stem = p.stem
        m = DUP_RE.match(stem)
        if not m:
            continue
        # Normalize the base by stripping trailing separators that commonly precede the number
        base_raw = m.group("base")
        base = base_raw.rstrip(" _-()[]")
        original = papers_dir / (base + ".pdf")
        # Also accept originals with different case in extension
        if not original.exists():
            alt = papers_dir / (base + ".PDF")
            if alt.exists():
                original = alt
        if original.exists():
            duplicates.append(p)
    return duplicates


def main(argv=None):
    parser = argparse.ArgumentParser(description="Remove numbered duplicate PDFs and matching MD files.")
    parser.add_argument("--papers", "-p", type=Path, default=None, help="Path to Papers folder")
    parser.add_argument("--md", "-m", type=Path, default=None, help="Path to Papers MD folder")
    parser.add_argument("--yes", "-y", action="store_true", help="Do not prompt, just delete")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be deleted without removing files")
    args = parser.parse_args(argv)

    # Resolve repo root relative to this script if defaults are used
    repo_root = Path(__file__).resolve().parents[2]
    papers_dir = (args.papers or repo_root / "Papers").resolve()
    md_dir = (args.md or repo_root / "Papers md").resolve()

    if not papers_dir.exists():
        print(f"Papers folder not found: {papers_dir}")
        return 2

    print(f"Searching for numbered duplicates in: {papers_dir}")
    duplicates = find_numbered_duplicates(papers_dir)

    if not duplicates:
        print("No simple numbered duplicates found.")
        return 0

    to_delete = []
    for dup in duplicates:
        md_candidate = (md_dir / (dup.stem + ".md"))
        to_delete.append((dup, md_candidate if md_candidate.exists() else None))

    print("The following files were identified as duplicates (numbered variant will be removed):")
    for pdf, md in to_delete:
        print(f"  PDF: {pdf}")
        if md:
            print(f"    Also will remove MD: {md}")

    if args.dry_run:
        print("\nDry run: no files will be deleted.")
        return 0

    if not args.yes:
        ans = input("Delete the listed files? [y/N]: ").strip().lower()
        if ans not in ("y", "yes"):
            print("No files deleted.")
            return 0

    deleted = 0
    for pdf, md in to_delete:
        try:
            if pdf.exists():
                pdf.unlink()
                deleted += 1
                print(f"Deleted: {pdf}")
            if md and md.exists():
                md.unlink()
                deleted += 1
                print(f"Deleted: {md}")
        except Exception as e:
            print(f"Failed to delete {pdf} or its md: {e}")

    print(f"Done. Files removed: {deleted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
