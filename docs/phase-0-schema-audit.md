# Phase 0 — Claim Schema Audit (Step 2)

Date: 2026-08-10
Purpose: Validate the claim classification rules in `knowledge.md` §3 and §5 against the six test cases, and document any rule gaps that need to be filled before Phase 0 is treated as complete.

Scope: This audit does NOT modify `knowledge.md`. Any proposed change is recorded here for human review, per the Phase 0 brief.

---

## Test A — CCC 310 on creation as "journeying"

**Statement (as written):**
"CCC 310 teaches that God freely willed to create a world in a state of journeying toward ultimate perfection."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **TEXTUAL** | The sentence reports what a specific document (CCC 310) says. It does not assert the underlying proposition as true on its own authority. |
| Secondary claim type | (none required) | The sentence is meta — it is about the text, not making a theological assertion directly. |
| Domain | **Catholic Theology** | CCC is a Catholic Church document. |
| Source object | required: `ccc-310` (see §6 source schema) | The statement's truth condition is "the Catechism says X", so the source object must exist and be VERIFIED before the sentence is allowed in the prototype. |

**Ambiguity:** A reader may collapse the meta-statement ("CCC 310 teaches P") into the underlying claim ("P is true"). The schema already separates TEXTUAL from THEOLOGICAL, but a single sentence can still blur them in presentation.

**Smallest rule needed to resolve ambiguity:**
- The claim field on a node must not contain "CCC 310 teaches …" as if it were the project's own assertion. It should either (a) be the underlying theological proposition P, with the meta-fact reported in a separate `textual_basis` field, or (b) explicitly mark itself as a textual claim and never be used to support downstream theological inferences without a separate move.

**What the schema already handles correctly:** §3.1 already labels "CCC 310 teaches X" as TEXTUAL. Good.

**What the schema does not yet cover:** There is no field on a node for "the underlying theological claim that this text is being cited to support". Without it, nodes will tend to merge the textual report and the theological claim into a single line.

**Proposed minimal addition (do not apply yet):**
```yaml
textual_basis:
  - source_id: ccc-310
    reports: "God freely willed a world in a state of journeying toward ultimate perfection"
    supports_claim_id: <id of the theological node using this text>
    inference_move: "textual report"   # NOT 'establishes'
```

---

## Test B — Foreknowledge does not cause the known event

**Statement:**
"Knowing that an event will occur does not, by itself, cause that event."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **LOGICAL** | The sentence asserts a non-causal relation between two concepts. |
| Secondary claim type | **PHILOSOPHICAL** | The claim sits inside philosophy of religion and metaphysics. |
| Domain | **Philosophy of Religion**; **Philosophy** | Foreknowledge vs. causation is a classical topic. |
| Inference status (when formalized) | **CONTESTED** or **REQUIRES_ADDITIONAL_PREMISE** | The intuitive reading is "knowing X ≠ causing X", but classical incompatibilist formulations (e.g. fatalism arguments) have been offered. The claim is not self-evident. |

**Ambiguity:** "Does not, by itself, cause" is doing a lot of work. The phrase acknowledges that the denial is non-monolithic — knowing may co-occur with causing without the knowing being the cause. The sentence does not assert that knowledge and causation can never travel together.

**Smallest rule needed:**
- Any claim of the form "X does not, by itself, cause Y" must be paired with at least one concrete counterexample model (e.g. soft fatalism, Molinism, simple foreknowledge without determinism) showing what the "by itself" caveat excludes. Otherwise the inference status is REQUIRES_ADDITIONAL_PREMISE.

**What the schema already handles correctly:** §3.4 (LOGICAL) and §3.5 (PHILOSOPHICAL) both exist. The schema's `inference_status` enum already includes CONTESTED and REQUIRES_ADDITIONAL_PREMISE.

**What the schema does not yet cover:** No rule forces the writer to enumerate the philosophical tradition the "by itself" is responding to. Without that, the claim reads as obvious and that is exactly the failure mode the project constitution warns against.

---

## Test C — Earliest Christian sources proclaim the resurrection

**Statement:**
"The earliest Christian sources proclaim that Jesus was raised from the dead."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **TEXTUAL** | The sentence reports what the sources say. |
| Secondary claim type | **HISTORICAL** | Identifying "earliest" sources is a historical judgment. |
| Domain | **Biblical Studies**; **History**; **Christian Theology** | The proposition is textual, the dating is historical, the proclamation is theological in origin. |
| Source objects | required: at least 1 Corinthians 15:3–8, plus a scholarly reference for "earliest" (e.g. Hurtado, Bauckham, or the standard introduction by Brown) |

**Ambiguity:** A naïve read treats "the earliest sources proclaim P" as evidence for P. That is a textual/historical claim about reception, not a metaphysical claim about the event. The schema distinguishes this, but a careless writer can still present it as the second.

**Second statement in the same test:** "Jesus was historically raised from the dead."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **HISTORICAL** | Asserts something about what occurred. |
| Secondary claim type | **METAPHYSICAL / THEOLOGICAL** | "Raised from the dead" is not a bare historical fact in the usual empirical sense; the resurrection is a theologically charged event. |
| Domain | **History**; **Christian Theology**; **Apologetics** |  |
| Inference status | **CONTESTED** | The historical case (minimal facts, empty tomb, appearances, early proclamation) is widely discussed; the metaphysical conclusion is disputed. |

**Smallest rule needed:**
- A node whose claim is "X historically happened" must include a `historical_evidence` block listing the specific evidence, and a `metaphysical_status` block indicating how the project treats the metaphysical interpretation. The two blocks must not be merged.

**What the schema already handles correctly:** §3.2 HISTORICAL and §3.6 THEOLOGICAL both exist. §3.8 COMPOSITE explicitly allows multi-domain tagging.

**What the schema does not yet cover:** There is no field for the distinction between "minimal fact" lists and "metaphysical interpretation" of those facts. Without an explicit split, the project will slide into using "the earliest sources proclaim X" as if it were direct evidence that X occurred.

---

## Test D — The logical problem of evil

**Statement:**
"If God is omnipotent, omniscient, and perfectly good, the existence of evil is logically impossible."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **PHILOSOPHICAL** | The sentence is a philosophical argument. |
| Secondary claim type | **LOGICAL** | It is presented as a logical incompatibility claim. |
| Domain | **Philosophy of Religion**; **Christian Theology** (responding side) |  |
| Inference status | **CONTESTED** | Mackie (1955) made the strongest form; Plantinga (1977) showed that at least one modal proposition — "it is possible that God has a morally sufficient reason for permitting every instance of evil" — is not formally contradictory with the premises. The argument is the canonical example of a "defensible" logical problem. |
| Speaker | John L. Mackie (1955, "Evil and Omnipotence", *Mind*) | The argument's strongest defender. |

**Ambiguity:** "Logically impossible" is doing heavy lifting. The move from "intuitive inconsistency" to "formal contradiction" is exactly what Plantinga targets. The schema already requires the speaker/author to be named, which solves attribution. It does not yet force the writer to state the logical form (modal operators, possible worlds).

**Smallest rule needed:**
- Any node making a logical incompatibility claim must include a `logical_form` block that names the modal operators in use and identifies whether the contradiction is alleged to be formal (deductive) or intuitive (inductive/abductive). Without it, the project will read "logical problem" as "obviously true" and miss the actual debate.

**What the schema already handles correctly:** §3.5 (PHILOSOPHICAL) and §3.4 (LOGICAL) are both present, and the `inference_status` enum is appropriate.

**What the schema does not yet cover:** There is no field that captures the "logical vs. evidential" distinction as a first-class attribute. The project will need to mark each POE node as one or both.

**Proposed minimal addition (do not apply yet):**
```yaml
problem_type:
  - logical
  - evidential
```

---

## Test E — Apostolic succession

**Statement 1:** "The Catholic Church teaches that bishops stand in apostolic succession."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **TEXTUAL** | Reports what the Church teaches. |
| Domain | **Catholic Theology**; **Ecclesiology** |  |

**Statement 2:** "Apostolic succession actually continues the apostolic ministry."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **THEOLOGICAL / ECCLESIOLOGICAL** | The proposition is confessional, not just reported. |
| Secondary claim type | **HISTORICAL** (for the empirical continuity claim) | The historical component (bishops in every generation, etc.) is empirical. |
| Domain | **Catholic Theology**; **Ecclesiology**; **History** |  |
| Inference status | **CONTESTED** | Catholic, Orthodox, Anglican, and classical Protestant accounts differ; the historical evidence is itself disputed. |

**Ambiguity:** A user can mistake Statement 1 for evidence of Statement 2. The schema separates them via TEXTUAL vs. THEOLOGICAL, which is correct. The risk is that a UI that displays both side-by-side without visual distinction will let the reader slide from "X teaches P" into "P is true".

**Smallest rule needed:**
- A TEXTUAL claim must never be a `supports` relation for a downstream claim about the same proposition's truth. It may only be `reports` or `cites`. The relation-type enum in `knowledge.md` §8 already includes `does-not-establish`, but it does not yet block the bad move structurally. Build-time validation should reject any edge labeled `supports` where the source is a TEXTUAL claim and the target is the same proposition in THEOLOGICAL mode.

**What the schema already handles correctly:** §3.1 (TEXTUAL) and §3.6 (THEOLOGICAL) are both present. The relation types in §8 are appropriate; the missing piece is build-time enforcement, not new vocabulary.

---

## Test F — Romans 8:20–22

**Statement 1:** "Romans 8:20–22 says creation was subjected to futility and groans."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **TEXTUAL** | Reports the content of a biblical passage. |
| Domain | **Biblical Studies** |  |

**Statement 2:** "Romans 8:20–22 teaches that the Fall caused every form of natural evil."

| Field | Value | Reason |
|---|---|---|
| Primary claim type | **INTERPRETIVE** | The verse is being read as teaching something it does not state literally. |
| Secondary claim type | **THEOLOGICAL** | The proposition ("the Fall caused every natural evil") is confessional. |
| Domain | **Biblical Studies**; **Christian Theology**; **Catholic Theology** (if read through CCC lens) |  |
| Inference status | **CONTESTED** | Many Catholic and Protestant commentators reject the strong form ("every"). Augustine, Aquinas, and modern CCC 309–314 all leave room for forms of natural evil that are not direct consequences of any particular human sin. |

**Ambiguity:** The second statement is a strong, specific inference from a passage that does not say it in those words. The schema already classifies this as INTERPRETIVE, which is correct. The remaining risk is that the interpretive claim is presented with the same visual weight as the textual claim, and the reader cannot tell that one is a quotation and the other is a theologian's reading.

**Smallest rule needed:**
- A node whose primary claim is INTERPRETIVE must name the interpreter or interpretive tradition (e.g. "Augustine, *De Genesi ad Litteram*", or "a common Catholic reading influenced by CCC 309–310"). The schema does not currently require an `interpreter` field on INTERPRETIVE claims. Without it, anonymous interpretation will leak in.

**Proposed minimal addition (do not apply yet):**
```yaml
interpreter:
  - name: "Augustine of Hippo"
    work: "De Genesi ad Litteram, XI"
    date: ca. 401–415 CE
```

---

## Cross-cutting findings

The six tests reveal three small holes in the current schema, none of which require rewriting `knowledge.md` to proceed. They are:

1. **No `textual_basis` link field.** Fixes Test A and Test E.
2. **No `problem_type` (logical/evidential) attribute on POE nodes.** Fixes Test D.
3. **No required `interpreter` field on INTERPRETIVE claims.** Fixes Test F.

Plus one process rule that the existing schema can already express but does not yet enforce at build time:

4. **No structural rule that TEXTUAL → THEOLOGICAL moves must be a separate inference step.** Fixes Test A, Test C, Test E.

## Recommendation

Record the four items above in `docs/phase-0-schema-audit.md` (this document) and **defer schema changes** until after Phase 0 ships. The reason: each of the four items can be implemented as a build-time validator on top of the existing YAML frontmatter, without changing the human-readable schema. That keeps Phase 0 small and respects the brief's "do not rewrite the architecture" rule.

If a later phase reveals that the four items are insufficient, they can be promoted into `knowledge.md` proper under change control.
