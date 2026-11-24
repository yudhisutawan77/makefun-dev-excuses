#!/usr/bin/env python3
"""Developer Excuses — Make the AI Judge Laugh.

Writes one funny single-line excuse a developer gives when code
breaks in production to /output/entry.txt (or $ENTRY_OUT when set).

Competition: u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3
Gate: UTF-8 text of 1 to 200 characters, one line, not only whitespace.
"""

import os
import sys

ENTRY = (
    "The bug only happens in production because that's the only place "
    "anyone actually uses the feature."
)


def output_path() -> str:
    return os.environ.get("ENTRY_OUT") or "/output/entry.txt"


def validate(text: str) -> str:
    """Enforce the competition gate locally: one line, 1-200 chars."""
    line = " ".join(text.split())
    if not line:
        raise ValueError("entry is empty")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    return line


def main() -> int:
    path = output_path()
    entry = validate(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
