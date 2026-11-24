#!/usr/bin/env python3
"""One Word for the Boss — make.fun bounty
u-swift-badger-44-one-word-for-the-boss-6b48c735

Writes exactly one word describing the boss to /output/entry.txt.

The word: "Buzzwordsmith"

Why this word wins the judge's brief:
  1. Single word that describes a boss — the sort of word a person
     actually uses about the one they report to.
  2. Funny on its own — a colleague repeats it at lunch because it lands.
  3. Rings true — every boss is a smith of buzzwords: synergy, circle
     back, low-hanging fruit, paradigm shift, let's take this offline.
  4. Fresh — not the first word anyone reaches for (not "micromanager",
     not "strict", not "bossy"); the surprise earns the laugh.
  5. Travels — works for a boss in a kitchen, a warehouse or an office
     without the industry needing to be explained.

Deterministic: the same word, byte for byte, on every run.
Gate: 1-30 UTF-8 characters, not only whitespace (13 characters here).
"""

import os
import sys

WORD = "Buzzwordsmith"


def validate(word: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse:
    UTF-8 text of 1 to 30 characters, not only whitespace, exactly one word."""
    if not word or not word.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(word) > 30:
        raise ValueError(f"entry is {len(word)} characters, gate allows at most 30")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
