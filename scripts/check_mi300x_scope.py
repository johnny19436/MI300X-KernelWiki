#!/usr/bin/env python3
"""Enforce MI300X-only product naming across knowledge pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

# Must stay aligned with data/scope-policy.md.
FORBIDDEN_TERMS = ["MI300A", "MI325X", "MI250X", "MI200", "MI350X"]

ENFORCED_GLOBS = [
    "README.md",
    "index.md",
    "sources/amd_arch_cdna3/**/*.md",
    "wiki/**/*.md",
    "queries/**/*.md",
]

EXCLUDED_PATHS = {
    Path("data/scope-policy.md"),
    Path("scripts/check_mi300x_scope.py"),
}


def iter_target_files() -> list[Path]:
    files: set[Path] = set()
    for pattern in ENFORCED_GLOBS:
        files.update(REPO_ROOT.glob(pattern))

    filtered: list[Path] = []
    for file_path in sorted(files):
        rel = file_path.relative_to(REPO_ROOT)
        if rel in EXCLUDED_PATHS:
            continue
        if file_path.is_file():
            filtered.append(file_path)
    return filtered


def find_violations(file_path: Path) -> list[tuple[int, str, str]]:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    violations: list[tuple[int, str, str]] = []
    patterns = {
        term: re.compile(rf"\b{re.escape(term)}\b", flags=re.IGNORECASE)
        for term in FORBIDDEN_TERMS
    }

    for line_no, line in enumerate(text.splitlines(), start=1):
        for term, pattern in patterns.items():
            if pattern.search(line):
                violations.append((line_no, term, line.strip()))
    return violations


def main() -> int:
    all_violations: list[tuple[Path, int, str, str]] = []
    files = iter_target_files()
    for file_path in files:
        rel = file_path.relative_to(REPO_ROOT)
        for line_no, term, line in find_violations(file_path):
            all_violations.append((rel, line_no, term, line))

    if all_violations:
        print("MI300X scope check failed. Forbidden product terms found:\n")
        for rel, line_no, term, line in all_violations:
            print(f"- {rel}:{line_no} [{term}] {line}")
        return 1

    print(
        "MI300X scope check passed: "
        f"no forbidden product terms in {len(files)} enforced files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
