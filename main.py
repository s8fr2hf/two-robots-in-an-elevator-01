#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward robot small talk.

The joke's turn: the speaker is a robot that has spent six whole
floors hovering over the door-close button without pressing it,
because its politeness subroutine decided that pressing it in front
of the other robot would be rude. The confession builds like a
normal awkward elevator apology — hovering, hesitating, worrying
about manners — and then the punchline quietly gives up: "and now
we live here." The two robots are not going anywhere anymore; the
elevator has become their home, because neither of them could bring
itself to do the one obviously rude thing that would have ended the
ride. Machine logic shows through in the measured hovering (six
floors, counted), the politeness rule treated as a hard constraint,
and the deadpan acceptance of the absurd outcome. The awkwardness
lands in the forced courtesy itself: the speaker would rather move
in than risk seeming impolite.

Writes the line to entry.txt in the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
Pure standard library only. The entry is a single line, 115
characters, so it fits the competition's 1-200 character limit.
"""

import os
import sys

# The door-close button confession: six floors of hovering,
# one politeness rule, and a new permanent address.
LINE = "".join(
    [
        "I have been hovering over the door-close button ",
        "for six floors because pressing it felt rude, ",
        "and now we live here.",
    ]
)


def main() -> int:
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        print("error: elevator line must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(line) <= 200):
        print(
            f"error: elevator line must be 1-200 characters, got {len(line)}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)

    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
