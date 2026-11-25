#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to entry.txt:
a To: line naming who it was meant for, and the unsent
message itself, one line written exactly as it was typed,
with no explanation after it and no trailing newline.
Standard library only.
"""

import os

ENTRY = (
    "To: Dad\n"
    "i still haven't deleted your number. it's been three years "
    "since the funeral and deleting it still feels like burying "
    "you twice"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
