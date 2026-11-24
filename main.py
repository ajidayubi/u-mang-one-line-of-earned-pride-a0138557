#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 chars) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene. The line is fixed and
deterministic: the same text on every run.
"""

LINE = (
    "At seventy-one, after a year relearning his letters, he wrote "
    "his granddaughter's name on her birthday card \u2014 in ink, "
    "without asking for help."
)


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
