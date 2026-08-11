# content/nodes/ — Argument nodes

Each file in this directory is an **argument node** — a single argumentative move, with all the metadata the prototype needs to render, link, and reason about it.

## File format

Every node file has two parts:

1. A YAML frontmatter with the full schema from `knowledge.md` §7.
2. A Markdown body with a plain-language statement and a "what this argument does NOT establish" paragraph.

## Required frontmatter fields

```yaml
---
id: <POE-NNN or future ID>
layer: <1 | 2 | 3 — conceptual layer, used for argument-map clustering>
title: <short title>
speaker: <person or tradition advancing the claim, or null if no specific speaker>
claim_type: <TEXTUAL | HISTORICAL | EMPIRICAL | LOGICAL | PHILOSOPHICAL | THEOLOGICAL | INTERPRETIVE | COMPOSITE>
domain: <Philosophy | Biblical Studies | History | Christian Theology | Catholic Theology | Ecclesiology | Patristics | Apologetics | Philosophy of Religion>

claim: <the single propositional claim being advanced>

definitions:
  <term>: <working definition for this node>

premises:
  - <premise 1>
  - <premise 2>
  - ...

inference: <description of the inferential move>

conclusion: <the propositional conclusion>

inference_status: <VALID | INVALID | CONTESTED | REQUIRES_ADDITIONAL_PREMISE | UNDERDETERMINED>

hidden_assumptions:
  - <assumption 1>
  - ...

strongest_objection: <best objection to the node>
strongest_response: <best response to that objection>
counter_response: <best counter-response to that response>
caveat: <one-sentence caution about how the node should be read>

what_this_argument_does_not_establish:
  - <limitation 1>
  - ...

evidential_challenge: <the empirical or evidential pressure on the node>
defeat_condition: <the condition under which the node is defeated>

related_nodes:
  - POE-NNN
  - ...

sources:
  - <source_id from content/sources/>

chapter_placement: <where this node appears in narrative>
visual_treatment: <how the node should be visualized in the UI>
confidence: <low | medium | high — the reviewer's confidence that the node is correctly characterized>
---
```

## Inference-status policy (from knowledge.md §7)

Allowed values: `VALID`, `INVALID`, `CONTESTED`, `REQUIRES_ADDITIONAL_PREMISE`, `UNDERDETERMINED`.

Do NOT use `true` / `false` as substitutes.

## Node index (Phase 0)

| ID | Layer | Title | Type | Status |
|---|---|---|---|---|
| POE-001 | 1 | Foreknowledge Does Not Equal Causation | LOGICAL/PHILOSOPHICAL | CONTESTED |
| POE-002 | 1 | Knowledge Does Not Necessarily Cause the Known Event | LOGICAL/PHILOSOPHICAL | REQUIRES_ADDITIONAL_PREMISE |
| POE-003 | 1 | The Parent Analogy | PHILOSOPHICAL | CONTESTED |
| POE-004 | 1 | Why the Divine Case Is Different | PHILOSOPHICAL/THEOLOGICAL | CONTESTED |
| POE-005 | 1 | Permission Is Not Intention | PHILOSOPHICAL/THEOLOGICAL | VALID |
| POE-006 | 1 | Omnipotence and Possible Worlds | PHILOSOPHICAL | CONTESTED |
| POE-007 | 2 | The Logical Problem of Evil | PHILOSOPHICAL/LOGICAL | CONTESTED |
| POE-008 | 2 | Plantinga's Free Will Defense | PHILOSOPHICAL | VALID (as defense) |
| POE-009 | 2 | The Evidential Problem of Evil | PHILOSOPHICAL | CONTESTED |
| POE-010 | 2 | Apparently Gratuitous Suffering | PHILOSOPHICAL | CONTESTED |
| POE-011 | 2 | Natural Evil | PHILOSOPHICAL/THEOLOGICAL | CONTESTED |
| POE-012 | 2 | Free Will and Natural Evil | PHILOSOPHICAL/THEOLOGICAL | CONTESTED |
| POE-013 | 3 | Skeptical Theism | PHILOSOPHICAL | CONTESTED |
| POE-014 | 3 | Could God Have Created a Better World? | PHILOSOPHICAL/THEOLOGICAL | VALID (textual) / CONTESTED (comparative) |
| POE-015 | 3 | Catholic Providence and the Limits of Human Knowledge | THEOLOGICAL | VALID (textual synthesis) |

## Change control

Any substantive change to a node must be recorded in the node's `changes` list in change-control format (knowledge.md §19): date, node, change, reason, source, verified_by. The Phase 0 brief explicitly forbids casual rewriting of established definitions.
