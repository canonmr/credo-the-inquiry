#!/usr/bin/env python3
"""
Final, targeted YAML fixer: wraps unquoted values that contain double-quote
characters in a properly-escaped double-quoted string.

This catches the case where a value like
    paraphrase: There is no "first principle" in the way...
causes the YAML parser to see an embedded mapping.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path("src/content")

LINE_PATTERN = re.compile(r'^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s+(.*)$')


def has_embedded_quote(value: str) -> bool:
    """True if the value (unquoted) has `"` characters in the middle."""
    if value.startswith('"') and value.endswith('"'):
        return False
    return '"' in value


def fix_text(text: str) -> str:
    new_lines = []
    for line in text.splitlines():
        m = LINE_PATTERN.match(line)
        if m:
            indent, key, value = m.groups()
            if has_embedded_quote(value):
                escaped = value.replace("\\", "\\\\").replace('"', '\\"')
                new_lines.append(f'{indent}{key}: "{escaped}"')
                continue
        new_lines.append(line)
    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    changed = []
    for ext in ("*.md", "*.mdx", "*.yaml", "*.yml"):
        for p in sorted(ROOT.rglob(ext)):
            original = p.read_text(encoding="utf-8")
            fixed = fix_text(original)
            if fixed != original:
                p.write_text(fixed, encoding="utf-8")
                changed.append(str(p))
    print(f"Modified: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
