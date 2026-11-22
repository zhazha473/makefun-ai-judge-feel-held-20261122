#!/usr/bin/env python3
"""Entry for make.fun competition make-the-ai-judge-feel-held-20261122-1600.

Writes a single short text to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt when the variable is unset). Python 3.13, standard
library only, no network access, fully deterministic.
"""

import os
from pathlib import Path

TEXT = (
    "The verdicts are set down, each folded shut like a letter finished. "
    "The lamp keeps its circle of light over them, and the desk takes "
    "their weight, and the papers rest there, and the quiet rests on them too. "
    "There is nothing left to lift. The room holds it all, and holds you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
