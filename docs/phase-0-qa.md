# Phase 0 — QA Report

Date: 2026-08-10
Reviewer: Mavis (Phase 0)

This report covers the Phase 0 build, including: content/schema validation, source references, accessibility, mobile readiness, reduced-motion behavior, and build/type/lint results.

## Build result

- `npm run build` → 77 pages generated, 0 errors.
- Output directory: `dist/`.
- Pages include:
  - `/` (root redirect to `/id/`)
  - `/id/` and `/en/` (home)
  - `/id/chapters/01-…` and `/en/chapters/01-…` (Chapter 1)
  - `/id/nodes/POE-001` … `/id/nodes/POE-015` and the English mirror (15 × 2 = 30 node pages)
  - `/id/sources/<id>` and the English mirror (19 × 2 = 38 source pages)
  - `/id/nodes/`, `/id/sources/`, and the English mirror (4 index pages)
  - Root `/` counts as 1, totals 77.

## Content / schema validation

### PASSED

- The argument node schema (`src/content/config.ts`) uses Zod to enforce required fields. The build passed, which means every POE file has every required field. The schema rejects missing fields at build time.
- The source schema uses Zod, and every source has been validated against it. The build passed, which means every source has every required field.
- The chapter schema uses Zod, and both chapter files (id/en) have been validated. The build passed.

### ISSUES OBSERVED DURING PHASE 0

The schema validation exposed several authoring issues that were fixed before the final build:

1. **YAML key with spaces in `definitions:` blocks.** Fixed in `scripts/fix_yaml_keys.py`. Keys like `"gratuitous suffering"` were rewritten to `gratuitous_suffering`. The schema is `z.record(z.string())` so any string is allowed; the fix is purely about YAML parsing.
2. **Unquoted values containing `: `.** Fixed in `scripts/fix_yaml_premises.py` and `scripts/fix_embedded_quotes.py`. Values that contain `": "` were wrapped in double quotes so YAML does not interpret them as mappings.
3. **Trailing parenthetical citation after a closing quote** (e.g. `key: "value" (citation)`). Fixed in `scripts/fix_yaml_global.py`. The citation is now folded inside the quoted string.
4. **Numeric `date` field.** Fixed in `scripts/fix_dates.py`. Pure-numeric dates like `1989` are now quoted so the schema sees a string, not a number. This is necessary because some dates are ranges (e.g. `"ca. 388–395"`).
5. **Empty list `[]` quoted as string `"[]"`** by an over-aggressive script. Reverted via PowerShell replace.
6. **Boolean `true` quoted as `"true"`** by the same script. Reverted.
7. **Trailing `---` document marker in `.yaml` data files** caused a "second document" parse error. Stripped.

The fix scripts are kept under `scripts/` for future re-runs. They are idempotent. **They are not part of the production build** — they are authoring utilities.

## Source reference / broken-link validation

- The source layer (`src/content/sources/`) has 19 records. Every record has a `source_id`, an author, a title, a date, a source type, a language, an edition, a location, an original quote, a translation where applicable, a paraphrase where applicable, a verification status, and notes.
- The build passed, which means every `supports_nodes` reference and every chapter's `sources_used` list points to a valid source_id, and every node's `sources` list points to a valid source_id. The build would have failed with a Zod error otherwise.
- Primary-text verification was done against the USCCB English translation of the Catechism (via catholicculture.org reproduction) and the canonical online editions of the philosophical and patristic sources.

## Accessibility

### PASSED

- The site uses semantic HTML (`<header>`, `<main>`, `<nav>`, `<footer>`, `<article>`, `<aside>`, `<details>`, `<summary>`).
- All argument cards have `aria-labelledby` and an `id`.
- All source cards have `aria-labelledby` and an `id`.
- A "skip to main content" link is provided at the top of every page.
- Color contrast: tested with the chosen palette at 17 px on a paper background, body text passes AA.
- All images (none in Phase 0) would carry `alt` text — no images used yet.
- Argument map is an `<svg role="img">` with `aria-label`.

### NOT YET TESTED

- Screen reader pass on the argument map. The SVG is decorated and the visible labels are the POE numbers. A future iteration should add a tabular accessible alternative.
- No automated a11y audit was run (e.g. axe-core). This is a recommended next step.

## Mobile responsiveness

### PASSED

- Layout uses a single 38 rem content column, centered, with 16–24 px padding.
- All tap targets are at least 44 × 44 px (verified by the global CSS — buttons, summaries, and links have `min-height: 44px`).
- The argument map SVG is `width: 100%` and `viewBox`-scaled, so it shrinks to mobile width without horizontal scrolling.
- Tables and pre-formatted blocks are not used; the chapter is prose, so mobile typography is the main concern.
- Base font size is 17 px on mobile, scaling to 18 px at 720 px. Line length is capped at ~ 70ch. Line height is 1.65.

### NOT YET TESTED

- Real device testing on a 360 × 640 viewport. Recommended next step.
- Touch-only testing of the `<details>` accordions (works in modern mobile browsers, but should be verified on iOS Safari and Android Chrome).
- The argument map's tap target size on circles. The circles have `r="22"` which is 44 px in diameter; this is on the boundary of the 44 × 44 guideline. A future iteration may add a transparent hit-area.

## Reduced-motion

### PASSED

- Global CSS includes `@media (prefers-reduced-motion: reduce)` that effectively disables animations and transitions. There are no animations in the current UI, so this is a no-op for the current build, but it is in place for future iterations.

## Build / type / lint

### PASSED

- `npx astro build` → success, 77 pages.
- TypeScript schema validation in `src/content/config.ts` is enforced at build time via Zod and Astro content collections.

### NOT YET DONE

- `@astrojs/check` was not installed, so the Astro type checker has not been run. This is a recommended next step. To enable it: `npm install --save-dev @astrojs/check typescript`, then `npx astro check`.
- No ESLint or Prettier config is in place. The project is small enough to be checked by reading; once a real editor workflow starts, ESLint + Prettier should be added.

## Per-Phase-0-brief requirement

The brief lists required UI components. The status of each:

| Component | Status | Notes |
|---|---|---|
| Chapter opening | DONE | `<h1>` with `Chapter N · Phase 0 prototype` line above. |
| Claim/argument cards | DONE | `ArgumentCard.astro` with header, claim, status pill, expandable details, sources. |
| Expandable source drawer | DONE | `SourceDrawer.astro` with `<details>` and embedded `SourceCard`s. |
| Epistemic ledger | DONE | `EpistemicLedger.astro` with established / contested / not established columns. |
| Argument relationship visualization | DONE | `ArgumentMap.astro` with inline SVG, 15 nodes, layer bands, selected edges. |
| Source verification state | DONE | `VERIFIED` / `PARTIALLY VERIFIED` / `UNVERIFIED` / `DISPUTED` pills in `SourceCard` and `SourceDrawer`. |
| Mobile-first layout | DONE | 38 rem content column, 17–18 px base, 1.65 line-height, sticky header, 44 px tap targets. |
| Reduced-motion fallback | DONE | Global CSS media query for `prefers-reduced-motion: reduce`. |

## Recommendations for the next phase

1. Move the 6 README-style files (`docs/argument-nodes-README.md`, `docs/sources-README.md`) — they were relocated from `content/` to avoid Astro's content collection picking them up as data entries. Confirm this convention is documented for future contributors.
2. Install `@astrojs/check` and run `astro check` in CI.
3. Add an automated a11y audit (axe-core) in CI.
4. Add ESLint + Prettier with a config matching the project style.
5. Add a GitHub Actions workflow that runs `npm run build` on every PR.
6. Review the fix scripts in `scripts/` and either commit them as part of the contributor workflow or remove them once the underlying authoring issues are solved (e.g. via a stricter schema or a content-creation tool).
7. The argument map currently shows ~ 20 selected edges out of ~ 60 possible related-node relations. A future iteration can render the full graph on desktop with progressive disclosure on mobile.
8. Add an "evidence/argument-level" view that visualizes how many sources back each node, and how many of those sources are `VERIFIED` vs `PARTIALLY VERIFIED` vs `UNVERIFIED`. This is a high-value addition for the project's epistemic standards.
9. Once the user is happy with the Phase 0 prototype, Phase 1 can begin: extending the node graph with the next 20–30 nodes covering the chain from theism to Catholic claim.
10. Consider a small "vocabulary lock" landing page that lists every term in `knowledge.md` §2 with the project's working definition. This is a low-cost addition that would make the project's epistemic discipline more legible to first-time readers.

## Final note

The build is green and the prototype is usable on a phone. The content is grounded in primary sources, the schema enforces the project's epistemic rules, and the chapter ends by making the problem deeper rather than artificially solved, per the brief.

The remaining work is content expansion, automated checks, and contributor ergonomics — none of which is required before the Phase 0 prototype is reviewed.
