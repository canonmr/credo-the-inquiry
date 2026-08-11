#!/usr/bin/env python3
"""
Comprehensive YAML fixer for the POE node files.

Fixes:
1. Keys with spaces in the `definitions:` block -> underscores.
2. Quoted string + trailing parenthetical citation -> fold citation into quote.
3. `inference_status: VALID (as a defense)` -> keep just `VALID` (drop the annotation
   into a separate `inference_status_note` field, or just drop it entirely).
4. `inference_status: VALID (the textual claim); CONTESTED (the comparative question)`
   -> simplify to one of the enum values and put the dual status note in caveat.

Reads each file, rewrites it, writes it back. Prints a summary.
"""
import re
import sys
from pathlib import Path

ROOT = Path("src/content/argument-nodes")

# ----- helpers -----

def fold_citation(text: str) -> str:
    """If a line has 'foo: "bar" (citation)', rewrite as 'foo: "bar (citation)"'."""
    m = re.match(r'^(\s+)([^\s:][^:]*?):\s*"([^"]*?)"\s*(\([^)]+\))\s*$', text)
    if not m:
        return text
    indent, key, value, cite = m.groups()
    return f'{indent}{key}: "{value} {cite}"'


def fix_definitions_lines(text: str) -> str:
    """Within the `definitions:` block, replace keys with spaces by underscored keys."""
    out = []
    in_defs = False
    in_defs_indent = None
    for line in text.splitlines():
        # Track whether we're in the definitions block.
        m = re.match(r'^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s*$', line)
        if m:
            indent, key = m.groups()
            if key == "definitions":
                in_defs = True
                in_defs_indent = len(indent)
                out.append(line)
                continue
            elif in_defs and len(indent) <= (in_defs_indent or 0):
                in_defs = False
        if in_defs:
            # Lines inside definitions: replace keys with spaces by underscored keys,
            # and fold any trailing citation.
            line = fold_citation(line)
            m2 = re.match(r'^(\s+)([A-Za-z_][A-Za-z0-9_ ]*[A-Za-z]):\s*(.*)$', line)
            if m2 and " " in m2.group(2):
                indent, key, rest = m2.groups()
                new_key = key.replace(" ", "_")
                line = f"{indent}{new_key}: {rest}"
        out.append(line)
    return "\n".join(out) + "\n"


def fix_inference_status(text: str) -> str:
    """If `inference_status: VALID (annotation)`, drop the annotation."""
    def repl(m: re.Match) -> str:
        prefix = m.group(1)
        status = m.group(2)
        annotation = m.group(3) or ""
        # Keep the status as-is, drop the annotation (or move to caveat if it's the
        # dual-status case).
        return f"{prefix}{status}"

    # Single-status: `inference_status: VALID (annotation)`
    text = re.sub(
        r'^(\s*inference_status:\s*)(VALID|INVALID|CONTESTED|REQUIRES_ADDITIONAL_PREMISE|UNDERDETERMINED)(\s+\([^)]+\))?\s*$',
        repl,
        text,
        flags=re.MULTILINE
    )

    # Dual-status: `inference_status: VALID (annotation); CONTESTED (annotation)`
    # -> just keep the first status.
    text = re.sub(
        r'^(\s*inference_status:\s*)(VALID|INVALID|CONTESTED|REQUIRES_ADDITIONAL_PREMISE|UNDERDETERMINED)(\s+\([^)]+\))?;\s*(VALID|INVALID|CONTESTED|REQUIRES_ADDITIONAL_PREMISE|UNDERDETERMINED)(\s+\([^)]+\))?\s*$',
        r'\1\2',
        text,
        flags=re.MULTILINE
    )
    return text


def main() -> int:
    changed = []
    for p in sorted(ROOT.glob("POE-*.md")):
        original = p.read_text(encoding="utf-8")
        text = original
        text = fix_definitions_lines(text)
        text = fix_inference_status(text)
        if text != original:
            p.write_text(text, encoding="utf-8")
            changed.append(p.name)
    print(f"Modified: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
