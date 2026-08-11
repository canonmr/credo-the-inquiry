#!/usr/bin/env python3
"""
Quote the `date:` field in every source YAML file so it is parsed as a string.

YAML would otherwise treat `date: 1989` as the number 1989, but our schema
expects a string (because some dates are ranges like 'ca. 388-395').
"""
import re
import sys
from pathlib import Path

ROOT = Path("src/content/sources")

DATE_LINE = re.compile(r'^(\s*date:\s+)([0-9]+(?:\.[0-9]+)?)\s*$', re.MULTILINE)


def fix_text(text: str) -> str:
    return DATE_LINE.sub(r'\1"\2"', text)


def main() -> int:
    changed = []
    for p in sorted(ROOT.glob("*.yaml")):
        original = p.read_text(encoding="utf-8")
        fixed = fix_text(original)
        if fixed != original:
            p.write_text(fixed, encoding="utf-8")
            changed.append(p.name)
    print(f"Modified: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
