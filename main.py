#!/usr/bin/env python3
"""Office Joke Open entry.

Writes one original one-line office joke to /output/entry.txt.
Standard library only, no network access, fully deterministic:
every run writes exactly the same text.
"""

import os

JOKE = "At the team-building trust fall, nobody caught me \u2014 HR logged it as a successful lesson in self-reliance."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
