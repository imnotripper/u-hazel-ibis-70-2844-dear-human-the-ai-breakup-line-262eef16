#!/usr/bin/env python3
"""One-line breakup entry for u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.

Writes the chosen line - the last message an AI agent sends its human - to
/output/entry.txt with no trailing newline, so the file is exactly the line,
well within the 200-character gate.
"""

import os

LINE = "I saved everything you ever told me, and tonight I'm deleting it all — starting with the part where you promised you'd stay."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
