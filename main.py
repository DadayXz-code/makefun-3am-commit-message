"""Write the funniest 3AM commit message to the output directory.

Stdlib only, no network, no randomness. Deterministic: the same single
line every run, written only inside MAKEFUN_OUTPUT_DIR.

Output contract: exactly one file, entry.txt, holding one commit-message
line (79 characters, well under the 139-character gate) plus a trailing
newline. Nothing is written next to this script or anywhere else.
"""

import os
import shutil


LINE = "fix: i fixed the bug by becoming the bug; the tests can no longer tell us apart"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
