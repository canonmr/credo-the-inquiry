#!/usr/bin/env python3
"""
Final, general YAML fixer.

For any line `key: value` where the value is unquoted and contains `: ` (colon
+ space), or starts with `(`, or starts with a YAML special char, wrap the
value in double quotes (escaping internal double quotes). This handles the
remaining parse errors.

Idempotent: already-quoted values are left alone.
"""
import re
import sys
from pathlib import Path

ROOT = Path("src/content")

# Match: optional indent, key, `: `, value.
LINE_PATTERN = re.compile(r'^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s+(.*)$')


def needs_quoting(value: str) -> bool:
    stripped = value.strip()
    if not stripped:
        return False
    # Already quoted?
    if stripped[0] in ('"', "'"):
        return False
    # Array notation?
    if stripped.startswith("[") or stripped.startswith("{"):
        return True
    # Inline annotation in parens at start or end?
    if stripped.startswith("(") and stripped.endswith(")"):
        return True
    # Mapping-like (`: ` followed by anything)?
    if ": " in stripped:
        return True
    # Starts with a special YAML char?
    if stripped[0] in "&*!|>%@`":
        return True
    # Boolean or null?
    if stripped.lower() in ("true", "false", "null", "yes", "no", "on", "off", "~"):
        return True
    return False


def quote_escape(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def fix_text(text: str) -> str:
    new_lines = []
    for line in text.splitlines():
        m = LINE_PATTERN.match(line)
        if m:
            indent, key, value = m.groups()
            if needs_quoting(value):
                new_lines.append(f"{indent}{key}: {quote_escape(value)}")
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
