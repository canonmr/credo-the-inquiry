# CREDO The Inquiry — Repository Audit (Phase 0, Step 1)

Date: 2026-08-10
Auditor: Mavis (Phase 0)
Status: Empty repository, fresh start.

## 1. Repository state

- Workspace: `C:\GITHUB\CREDO The Inquiry`
- Files at audit time: none (zero tracked or untracked content)
- No existing `package.json`, no framework lock-in, no CI, no deployment configuration.
- Git: folder present at parent (`C:\GITHUB`) but the `CREDO The Inquiry` subfolder has not yet been initialized as a repository.

Conclusion: this is a greenfield project. There is no pre-existing stack to respect and no legacy code to migrate.

## 2. Reusable infrastructure

- None within the repository itself.
- The user's broader `C:\GITHUB` workspace contains adjacent projects (e.g. `Credo`, `CredoEtScribo`, `catholic-authority-engine`, `Katolik`). These are sibling projects, not part of this codebase. They are not imported; they are referenced only for stylistic / editorial continuity if useful.

## 3. Content architecture (target)

Knowledge base source of truth lives in:
- `content/nodes/` — argument nodes (POE-001 … POE-015, then expanding)
- `content/sources/` — source records (YAML), one per primary or scholarly reference
- `content/chapters/` — narrative chapter content composed from nodes and sources

Each node and source is a plain text file with a YAML frontmatter matching the schema in `knowledge.md`. Markdown bodies carry claims, premises, objections, and references. No proprietary formats.

## 4. Styling and component conventions (target)

- Mobile-first (360–430 px primary viewport).
- Plain CSS with custom properties (no Tailwind for Phase 0 — keep the surface area small).
- Web fonts loaded only if they materially improve readability; otherwise system stack.
- No animation library; reduced-motion honored by default via `prefers-reduced-motion`.
- Components live in `src/components/`, pages in `src/pages/`, content collections in `src/content/`.

## 5. Deployment constraints

- Target: GitHub Pages (static export). Astro's `output: 'static'` default fits.
- No server runtime, no API routes, no auth, no database.
- Bilingual (ID primary, EN secondary). A language switcher must work on mobile without reload thrash.

## 6. Existing-site hosting

- No existing site to host the prototype. Phase 0 ships the prototype in this same repository.
- Deployment from `dist/` after `astro build`.

## 7. Likely implementation route

Recommended stack for the smallest viable prototype that meets every Phase 0 requirement:

| Concern | Choice | Why |
|---|---|---|
| Site framework | Astro 4.x | Content-first, MDX native, ships zero JS by default, ideal mobile performance. |
| Content format | MDX + YAML frontmatter | Lets argument nodes mix prose, structured data, and (later) interactive components. |
| Schema validation | Astro Content Collections + Zod | Enforces the argument node schema from `knowledge.md` at build time. |
| Styling | Plain CSS + custom properties | No framework bloat. Honors "smallest technical solution" rule. |
| Interactive bits | Vanilla JS / Web Components | One small visualization component (argument map) instead of pulling in D3. |
| Deployment | GitHub Pages via Actions | Static, free, no infra. |
| Bilingual | `lang` frontmatter + per-page route | Simple `/id/...` and `/en/...` mirroring. |

Explicitly avoided for Phase 0 (per the non-negotiable rule about not introducing big frameworks prematurely): Next.js, D3, GSAP, Framer Motion, Tailwind, i18n libraries, heavy CMS.

## 8. Technical risks

1. **Source verification cost.** Verifying CCC 309–314 and primary philosophical texts is non-trivial. Mitigation: build the source layer first and mark every claim `UNVERIFIED` until cross-checked.
2. **Schema drift.** The argument node schema in `knowledge.md` is large. Mitigation: enforce via Zod at build time; fail the build on any missing required field.
3. **Bilingual drift.** Translating the same content into two languages tends to produce subtly different claims. Mitigation: claim text is single-source; only prose is translated. Each node keeps one canonical `claim` and language variants live in chapter prose.
4. **Over-design temptation.** The brief explicitly warns against decorative animation and fake scores. Mitigation: visualization component limited to argument map and source drawer; no charts of unearned percentages.
5. **Mobile typography.** Long philosophical paragraphs are hard to read on a phone. Mitigation: aggressive line length (≤ 70ch), 16 px+ base, generous line-height.

## 9. Recommendation

Proceed with the recommended stack above. Do not add new dependencies mid-Phase 0 unless an implementation problem forces it. If forced, document the reason in `docs/phase-0-qa.md` before merging.

## 10. Out of scope for Phase 0

- Full 70+ node expansion.
- Search, comments, user accounts.
- Editorial CMS.
- Visual polish beyond readable mobile typography and the required UI surfaces.
