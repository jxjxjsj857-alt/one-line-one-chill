#!/usr/bin/env python3
"""One Line, One Chill — writes a single sentence of horror to /output/entry.txt.

The line is one sentence, under 200 characters, built to land as a scare in a
single breath: a concrete, vivid image (a dentist, a tooth, a carved name) with
an uncanny turn at the end — the dread is what the sentence withholds.
"""

import os

LINE = "The dentist pulled a tooth from my jaw that was never mine \u2014 my name is carved into it, in my own handwriting."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
