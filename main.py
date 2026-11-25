"""Invent a Word We Need — entry program.

Writes one invented English word together with its one-line
definition to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only; no network, no file reads outside this program.
"""

import os

ENTRY = (
    "clockblank (n.) \u2014 the instant you check the time on your phone "
    "and forget it before the screen goes dark."
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Refuse to write anything outside it.
assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry outside the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
