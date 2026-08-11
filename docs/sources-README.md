# content/sources/ — Source layer

Each file in this directory is a **source record** — a single primary or scholarly work, or a single passage from a larger work.

## File format

Every source file has two parts:

1. A YAML frontmatter with machine-readable metadata. This is the canonical record.
2. A Markdown body with the verified text, the translation, the paraphrase, and reviewer notes.

## Frontmatter schema

```yaml
---
source_id: <stable kebab-case id, unique>
author: <person or body responsible>
title: <work title; use specific passage for excerpts>
date: <year of composition, not year of edition>
source_type: <one of: primary-philosophical | primary-theological | church-document | biblical-text | patristic | historical | scholarly-secondary | reference>
language: <original language of the text>
edition: <edition or version actually consulted, with URL if applicable>
location: <book, chapter, section, page, or paragraph reference>
original_quote: <exact wording, in the original language if available>
translation: <English translation; mark as such, do not present as official>
paraphrase: <project's own summary, clearly labeled as paraphrase>
verification_status: <VERIFIED | PARTIALLY VERIFIED | UNVERIFIED | DISPUTED>
notes: <reviewer's working notes, including uncertainty>
supports_nodes: <list of POE node ids that cite this source>
changes: <change log, in change-control format from knowledge.md §19>
---
```

## Translation rules (from knowledge.md §6)

- For important philosophical / theological quotations, retain the original language when available.
- Provide an English translation and label it as such.
- Provide a paraphrase and label it as such.
- Never present an AI-generated translation as an official published translation.
- Never silently upgrade UNVERIFIED → VERIFIED.

## Cross-referencing

The `supports_nodes` list tells the build-time validator which argument nodes (in `content/nodes/`) depend on this source. When a node is added or removed, the corresponding source file must be updated.
