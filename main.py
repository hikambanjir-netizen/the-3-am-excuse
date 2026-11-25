#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

Writes one line to /output/entry.txt: the excuse a hardware wallet gives
The line is a single fixed string: the wallet's own voice, the 3 AM hour
doing the work (a sleepy human is the threat the wallet was bought to
stop), and no borrowed joke about batteries, firmware or cold storage.
Nothing is read from the network, the environment or the clock, so two
runs produce byte-identical output.
"""

import os

LINE = (
    "You bought me so no sleepy human could drain you at 3 AM. "
    "That human is you, right now, holding me."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
