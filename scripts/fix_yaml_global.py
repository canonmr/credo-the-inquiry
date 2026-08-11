#!/usr/bin/env python3
"""
General YAML citation-folder for both nodes (.md) and sources (.yaml).

For any line matching `key: "value" (annotation)`, rewrite as
`key: "value (annotation)"`. Only acts on lines whose value starts with a
double-quote and ends with a double-quote followed by a parenthetical.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path("src/content")

# Match: optional indent, key, colon, space, opening double-quote,
# value (no double-quote), closing double-quote, optional space, parens, optional EOL.
PATTERN = re.compile(
    r'^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s+"([^"]*)"\s*(\([^)]+\))\s*$',
    re.MULTILINE
)


def fix(text: str) -> str:
    def repl(m: re.Match) -> str:
        indent, key, value, citation = m.groups()
        return f'{indent}{key}: "{value} {citation}"'
    return PATTERN.sub(repl, text)


def main() -> int:
    changed = []
    for p in sorted(ROOT.rglob("*.md")):
        original = p.read_text(encoding="utf-8")
        fixed = fix(original)
        if fixed != original:
            p.write_text(fixed, encoding="utf-8")
            changed.append(str(p))
    for p in sorted(ROOT.rglob("*.mdx")):
        original = p.read_text(encoding="utf-8")
        fixed = fix(original)
        if fixed != original:
            p.write_text(fixed, encoding="utf-8")
            changed.append(str(p))
    for p in sorted(ROOT.rglob("*.yaml")):
        original = p.read_text(encoding="utf-8")
        fixed = fix(original)
        if fixed != original:
            p.write_text(fixed, encoding="utf-8")
            changed.append(str(p))
    for p in sorted(ROOT.rglob("*.yml")):
        original = p.read_text(encoding="utf-8")
        fixed = fix(original)
        if fixed != original:
            p.write_text(fixed, encoding="utf-8")
            changed.append(str(p))
    print(f"Modified: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
