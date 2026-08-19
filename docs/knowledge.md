# knowledge.md — Live Knowledge Base for credo-the-inquiry

> **Status: LIVE.** Maintained since the post-launch fixes of 2026-08-19.
> Phase-0-era material is preserved in §2 with a `SUPERSEDED` marker. It is kept for history only and must not be used as the operative specification.

---

## §1 Purpose

`knowledge.md` is the single canonical knowledge file for the project. It records:
what the site argues (§3), how the content is organized (§3–§5, §11), how sources
and nodes are governed (§6–§8, §19), what content actually exists today (§5, §9–§10,
§12), and what has changed since launch (§13).

The phase-0 docs in `docs/` remain in the repository but are superseded by this file:
`docs/phase-0-qa.md`, `docs/phase-0-schema-audit.md`, `docs/project-audit.md`.

---

## §2 Phase-0 project brief (SUPERSEDED — historical record)

The phase-0 brief established the site as a seven-chapter inquiry into the Catholic
Church's claim that "God speaks": a public, source-grounded argument that proceeds
from the problem of evil (does God speak if evil exists?) through revelation,
Scripture, authority, Christ, and the believer's end, to a conclusion that does not
demand more certainty than the address itself offers.

Phase-0 deliverables that are **superseded**: the node index tables and statuses in
`docs/argument-nodes-README.md` (the live index is §5 of this file), the source
conventions in `docs/sources-README.md` (live rules are §6 of this file), and the
three audit documents listed in §1.

Superseded statuses must not be treated as current. The inference-status policy
(§7) and the change-control format (§19) remain operative.

---

## §3 Architecture (live)

```
src/content/chapters/    7 narrative chapters, bilingual (see §11)
src/content/argument-nodes/  70 argument nodes, bilingual (see §5)
src/content/sources/     103 source records (see §9)
src/data/chapterMaps.ts  visual map: node positions + relation edges (see §10)
docs/                    knowledge.md (this file), READMEs, phase-0 audit docs
```

Layer flow: **sources** (evidence, quoted verbatim with translation and paraphrase)
support **nodes** (claims, with inference statuses) which are placed in **chapters**
(narrative) and rendered on the **chapter maps**.

## §4 Bilingual convention (live)

- Chapters: `NN-<slug>.id.mdx` (Indonesian) and `NN-<slug>.en.mdx` (English).
- Nodes: `NNN-NNN.id.md` (Indonesian) and `NNN-NNN.md` (English). There is no `.en.md` suffix.
- Sources: single YAML file per record; `paraphrase` is **Indonesian**, `original_quote`
  is in the original language where available, `translation` is English (labeled).
- Frontmatter ids must match `^(POE|REV|SCR|AUT|CHR|SAL|SYN)-\d{3}$` (schema in `src/content/config.ts`).

## §5 Node taxonomy (live)

70 nodes, each in two files (Indonesian `.id.md` + English `.md`).

| Category | Range | Count | Role in the inquiry |
|---|---|---|---|
| POE | POE-001 … POE-015 | 15 | Problem of evil: the strongest case that God does not speak |
| REV | REV-001 … REV-009 | 9 | Revelation: God's address as the response |
| SCR | SCR-001 … SCR-009 | 9 | Scripture: the books that carry the address |
| AUT | AUT-001 … AUT-009 | 9 | Authority: who may interpret the address |
| CHR | CHR-001 … CHR-009 | 9 | Christ and the Church: the founder |
| SAL | SAL-001 … SAL-009 | 9 | The believer's end: salvation, judgment, heaven, hell |
| SYN | SYN-001 … SYN-010 | 10 | Synthesis: the inquiry's conclusion |

`SYN-010` (epistemic tension: Kierkegaard/James/Pascal vs. Dei Filius) was added
post-launch on 2026-08-19; it closes chapter 7 (§13).

## §6 Translation rules (live — referenced by `docs/sources-README.md`)

- For important philosophical / theological quotations, retain the original language when available.
- Provide an English translation and label it as such.
- Provide a paraphrase and label it as such.
- Never present an AI-generated translation as an official published translation.
- Never silently upgrade UNVERIFIED → VERIFIED.
- The `paraphrase` field is written in **Indonesian** and is the project's own
  formulation — never a word-for-word translation (post-launch rule, 2026-08-19).

## §7 Inference-status policy (live — referenced by `docs/argument-nodes-README.md`)

Allowed values: `VALID`, `INVALID`, `CONTESTED`, `REQUIRES_ADDITIONAL_PREMISE`, `UNDERDETERMINED`.
Do NOT use `true` / `false` as substitutes.

`verification_status` on source records: `VERIFIED | PARTIALLY VERIFIED | UNVERIFIED | DISPUTED`.
A record may only be marked `VERIFIED` when the quoted text has been checked against a
consulted edition; until then it stays `PARTIALLY VERIFIED` (post-launch rule: no
silent upgrades without explicit confirmation).

## §8 Source record schema (live)

See `docs/sources-README.md` for the annotated schema. Fields: `source_id`,
`author`, `title`, `date` (composition), `source_type`, `language`, `edition`,
`location`, `original_quote`, `translation`, `paraphrase`, `verification_status`,
`notes`, `supports_nodes`, `changes`.

## §9 Source inventory (live)

103 records in `src/content/sources/` (101 pre-launch + 2 added post-launch:
`vatican-i-dei-filius-3`, `newman-grammar-of-assent-1870`).

| source_type | Count |
|---|---|
| biblical-text | 40 |
| church-document | 34 |
| primary-philosophical | 15 |
| patristic | 4 |
| primary-theological | 4 |
| historical | 3 |
| reference | 2 |
| scholarly-secondary | 1 |

Verification status: **86 VERIFIED**, **17 PARTIALLY VERIFIED**.
All 103 `paraphrase` fields are Indonesian (post-launch retrofit, §13).

## §10 Relation label inventory (live)

28 relation labels are used in `src/data/chapterMaps.ts` edges:

`calls for`, `contrasts`, `defines`, `demands`, `enables`, `ends in`, `extends`,
`faces`, `feeds`, `frames`, `grounds`, `guides`, `informs`, `is answered by`,
`is framed by`, `is held by`, `is met by`, `is targeted by`, `is tested by`,
`leads to`, `modally`, `opens`, `raises`, `reframes`, `requires`, `responds to`,
`specifies`, `supports`.

SYN-010's edges: `SYN-010 → SYN-004 (frames)` and `SYN-010 → SYN-005 (frames)`,
position `[770, 220, 2]` on the chapter 7 map.

## §11 Chapter inventory (live)

7 chapters × 2 languages (`01` … `07` in `src/content/chapters/`), from
"if God already knew, why create?" (01) to "what is the result of this inquiry?" (07).

## §12 Terminology lock (effective)

Locked Indonesian renderings for key terms (used in nodes and in all source paraphrases):

| English | Indonesian |
|---|---|
| foreknowledge | pengetahuan-sebelumnya |
| causation | sebab-akibat |
| permission | izin / mengizinkan |
| providence | provisi |
| divine hiddenness / hidden God | keterpencilan / Allah yang menyembunyikan diri |
| free will | kehendak bebas |
| gratuitous suffering | penderitaan tanpa tujuan |
| evil | kejahatan |
| soul-making | pembentukan jiwa |
| horrendous evil(s) | kejahatan mengerikan |
| privation / deficient cause | privasi / sebab defisien |
| creed | syahadat |
| dual authorship (of Scripture) | kepengarangan ganda |
| particular judgment | penghakiman khusus |
| hypothesis of indifference | hipotesis ketidakacuhan |
| self-exclusion | eksklusi-diri |
| college of bishops | kolegium para uskup |
| inwardness (Kierkegaard) | kebatinan |
| leap of faith | lompatan iman |
| theodicy / defense | teodise / pembelaan |
| evidentialist | evidensialis |
| omnipotent / omniscient | mahakuasa / mahatahu |
| resurrection / grace / salvation / faith | kebangkitan / rahmat / keselamatan / iman |
| Scripture / Church | Kitab Suci / Gereja |

Kept foreign (technical terms): `homoousios`, `ex cathedra`, `theopneustos`,
`Monothelitism`, `P(O | theism)`.
Reference to the Catechism in paraphrases uses **"Katekismus"** (not "KKI").

## §13 Post-launch changelog (live)

**2026-08-19 — Task 1: SYN-010 and closing of chapter 7**
- Created `SYN-010.id.md` / `SYN-010.md` — epistemic tension between
  Kierkegaard, James, Pascal and Vatican I's Dei Filius on the assent of faith.
- Created sources `vatican-i-dei-filius-3.yaml` (ch. 4, DS 3017 — the assent of
  faith is not a blind movement of the mind) and `newman-grammar-of-assent-1870.yaml`
  (GA ch. 9, hidden-God quote verified at p. 352, Longmans 1906).
- `romans-1-20.yaml`: `supports_nodes += SYN-010`, entry in `changes`.
- Chapter 07 (both languages): `nodes_used += SYN-010`, `sources_used +=`
  the two new sources and `romans-1-20`; one-sentence prose marking in section 5
  (the "leap" is used loosely; the Church has held since Vatican I that the assent
  of faith is not a blind movement of the mind).
- `src/data/chapterMaps.ts`: SYN-010 at `[770, 220, 2]`; edges
  `['SYN-010','SYN-004','frames']`, `['SYN-010','SYN-005','frames']`.
- Build: `astro check` 0 errors; `astro build` 369 pages.

**2026-08-19 — Task 2: paraphrase retrofit**
- All 101 legacy source records: `paraphrase` rewritten from English to
  original Indonesian (103/103 records now Indonesian).
- Consistency fix: "KKI §311" → "Katekismus §311" (`augustine-enchiridion`).
- `original_quote` and `translation` untouched in every record.
- Verification: rg scan for English function words in `paraphrase` fields — 0 hits;
  `astro check` 0 errors / 0 warnings.

**2026-08-19 — Task 3: knowledge.md sync**
- Created this file (the referenced `knowledge.md` did not exist in the repo;
  READMEs referenced its §6, §7, §19 — those sections are reconstructed above).
- `vatican-i-dei-filius-2.yaml`: `language: en` → `la` (aligns with the
  original-language rule of §6; English text remains in `translation`).

---

## §19 Change control format (live — referenced by `docs/argument-nodes-README.md`)

Any substantive change to a node or source record must be recorded in the record's
`changes` list, one entry per change, in this format:

```
- "YYYY-MM-DD: <what changed>, <why>, <source of the change>, <verified_by>."
```

Example (from `romans-1-20.yaml`):

```
- "2026-08-19: supports_nodes += SYN-010 — node baru ketegangan epistemik (Bab 7) merujuk Rom 1:20 sebagai dasar ajaran Vatikan I tentang pengetahuan natural akan Allah; diverifikasi oleh opencode, menunggu peninjauan."
```

Rules: never rewrite established definitions casually; never mark a record
`VERIFIED` without checking the quoted text against a consulted edition; when in
doubt, prefer `PARTIALLY VERIFIED` and say so in `notes`.