import re
from pathlib import Path

ROOT = Path("src/content/argument-nodes")

for p in sorted(ROOT.glob("POE-*.md")):
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        # Check definitions block
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        if " " in stripped and ":" in stripped and stripped.endswith(")"):
            print(f"{p.name}:{i}: {line!r}")
