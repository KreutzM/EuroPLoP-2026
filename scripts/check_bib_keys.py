#!/usr/bin/env python3
"""Check a BibTeX file for duplicate entry keys.

This lightweight checker intentionally avoids parsing full BibTeX. It scans entry
headers of the form @type{key, and reports repeated keys with line numbers.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ENTRY_RE = re.compile(r"^\s*@\s*([A-Za-z]+)\s*\{\s*([^,\s]+)")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_bib_keys.py <file.bib>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"BibTeX file not found: {path}", file=sys.stderr)
        return 2

    seen: dict[str, tuple[int, str]] = {}
    duplicates: list[tuple[str, int, int, str]] = []

    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        match = ENTRY_RE.match(line)
        if not match:
            continue
        entry_type, key = match.groups()
        normalized = key.strip()
        if normalized in seen:
            first_line, first_type = seen[normalized]
            duplicates.append((normalized, first_line, line_no, entry_type))
        else:
            seen[normalized] = (line_no, entry_type)

    if duplicates:
        print("Duplicate BibTeX keys found:", file=sys.stderr)
        for key, first_line, duplicate_line, entry_type in duplicates:
            print(
                f"  {key}: first at line {first_line}, duplicate at line {duplicate_line} (@{entry_type})",
                file=sys.stderr,
            )
        return 1

    print(f"OK: {len(seen)} BibTeX entries, no duplicate keys in {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
