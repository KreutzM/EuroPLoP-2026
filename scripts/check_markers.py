#!/usr/bin/env python3
"""Lightweight scan for unresolved manuscript markers in tracked source files.

This check is intentionally conservative: it reports common unresolved markers
but ignores AGENTS/README/CHANGELOG and the check script itself, where such words
are expected.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INCLUDED_SUFFIXES = {".tex", ".bib"}
EXCLUDED_NAMES = {
    "README.md",
    "CHANGELOG.md",
    "AGENTS.md",
}
EXCLUDED_DIRS = {".git", "build"}

PATTERNS = [
    re.compile(r"\\todo\s*\{", re.IGNORECASE),
    re.compile(r"\bTODO\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"\?\?\?"),
]

# Some legacy comments and package names may legitimately contain text that
# resembles a marker. Keep exceptions narrow and explicit.
ALLOWED_SUBSTRINGS = {
    "\\usepackage{todonotes}",
}


def iter_source_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.name in EXCLUDED_NAMES:
            continue
        if path.suffix in INCLUDED_SUFFIXES:
            files.append(path)
    return sorted(files)


def main() -> int:
    findings: list[str] = []
    for path in iter_source_files():
        rel = path.relative_to(ROOT)
        for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if any(allowed in line for allowed in ALLOWED_SUBSTRINGS):
                continue
            for pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(f"{rel}:{line_no}: {line.strip()}")
                    break

    if findings:
        print("Potential unresolved manuscript markers found:")
        for finding in findings:
            print(f"  {finding}")
        print("\nResolve these before final submission, or update scripts/check_markers.py if a match is intentional.")
        return 1

    print("OK: no unresolved manuscript markers found in .tex/.bib sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
