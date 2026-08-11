# scripts/

These are one-off Python scripts used during Phase 0 to repair YAML and
content-collection issues. They are kept here for future re-runs and as
documentation of the kinds of authoring problems the project is trying to
prevent.

The fix scripts are idempotent: they detect a problem and apply the
minimal change. Re-running them on a clean tree is a no-op.

The `*_legacy.py` files are debugging scratchpads kept for reference; they
are not part of the active toolchain.

In a future phase, the right move is to replace these with a stricter
schema or a content-creation tool that prevents the problems at write
time, rather than fixing them at build time.

## When to re-run

If a new content file fails the build with a YAML parse error or a schema
mismatch, run, in order:

```bash
python scripts/fix_yaml_global.py
python scripts/fix_yaml_keys.py
python scripts/fix_yaml_premises.py
python scripts/fix_embedded_quotes.py
python scripts/fix_yaml_colons.py
python scripts/fix_dates.py
npx astro build
```

If the build still fails, the error message usually identifies the file and
the line. The most common remaining issue is an unquoted value with a
trailing parenthetical; `fix_yaml_global.py` catches that, but only if the
citation is at the end of the line.
