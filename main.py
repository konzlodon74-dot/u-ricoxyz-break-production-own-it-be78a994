#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line.

Writes the line to /output/entry.txt with no trailing newline.
Standard library only.
"""

import os

LINE = "I deployed to prod on a Friday, skipped the tests, and discovered the backup was a folder named final_FINAL_v2."


def main():
    # The line is the whole entry: one brutally honest sentence,
    # no hedging, no newline, no excuses beyond the excuse itself.
    line = LINE
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip(), "line must not be blank"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
