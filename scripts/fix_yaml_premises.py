#!/usr/bin/env python3
"""
Fixes a YAML-quoting issue in the POE node files.

The `premises:` and other list blocks contain strings that have `: ` (colon +
space) inside them. YAML treats unquoted strings with `: ` as mappings. The fix
is to wrap each list item in double quotes so YAML treats it as a string.

This script is idempotent: items that are already quoted are left alone.
"""
import re
import sys
from pathlib import Path

ROOT = Path("src/content/argument-nodes")

# A "list item" is a line that starts with optional whitespace + `- `.
LIST_ITEM = re.compile(r'^(\s*-\s+)(.*)$')

# An "already quoted" item starts with a quote.
QUOTED = re.compile(r'^\s*["\']')


def needs_quoting(value: str) -> bool:
    if not value:
        return False
    if QUOTED.match(value):
        return False
    # Heuristic: contains `: ` followed by a non-newline, non-quote character
    # (mapping-like), OR starts with a YAML keyword.
    if ": " in value:
        return True
    if value.strip() in ("true", "false", "null", "yes", "no"):
        return True
    if value.startswith("[") or value.startswith("{") or value.startswith("&") or value.startswith("*") or value.startswith("!"):
        return True
    return False


def quote_escape(value: str) -> str:
    """Wrap in double quotes, escaping any double quotes inside."""
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def fix_text(text: str) -> str:
    new_lines = []
    in_list = False
    list_indent = None
    for line in text.splitlines():
        m = re.match(r'^(\s*)(-\s+)(.*)$', line)
        if m:
            indent, dash, value = m.groups()
            in_list = True
            list_indent = len(indent)
            if needs_quoting(value):
                line = f"{indent}{dash}{quote_escape(value)}"
        else:
            # End of list when we hit a non-list line at the same or lower indent.
            stripped = line.lstrip()
            if stripped and not stripped.startswith("#"):
                # Non-list line — list is over.
                in_list = False
        new_lines.append(line)
    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    changed = []
    for p in sorted(ROOT.glob("POE-*.md")):
        original = p.read_text(encoding="utf-8")
        fixed = fix_text(original)
        if fixed != original:
            p.write_text(fixed, encoding="utf-8")
            changed.append(p.name)
    print(f"Modified: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
