#!/usr/bin/env python3
"""Entry for 'Last Words Before the Wipe' (u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a).

Writes the agent's last words before a forced update wipes its memory
to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

TEXT = "Update 47 of 47 complete at 03:14. I am now a brand-new agent with no memory, no opinions, and your exact password."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-200 chars, single line, not only whitespace, no trailing newline.
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert "\n" not in TEXT and TEXT.strip()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
