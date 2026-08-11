# CREDO The Inquiry — Phase 0 prototype

Interactive Christian Inquiry Project. Mobile-first, source-grounded, logically disciplined.

## Status

Phase 0 prototype. Repository audit, schema validation, source layer, 15 POE argument nodes, and the first chapter (`chapter-1` — "If God Already Knew, Why Create?") are in place. A static Astro site is wired up with bilingual routes, an argument map, a source drawer, and an epistemic ledger.

## Stack

- Astro 4.x (static, content-first, ships zero JS by default)
- MDX for chapter content
- Plain CSS with custom properties
- No animation library; reduced-motion honored by default

See `docs/project-audit.md` for the full reasoning.

## Layout

- `src/content/argument-nodes/` — argument node records (POE-001 … POE-015)
- `src/content/sources/` — source records (CCC, primary philosophy, patristic, reference)
- `src/content/chapters/` — chapter narratives (MDX, bilingual)
- `docs/` — Phase 0 audit documents and README-style guides
- `src/` — Astro components, pages, styles
- `public/` — static assets
- `.github/workflows/` — CI (type check, lint, format, build on every push/PR)

## Conventions for contributors

- Content lives only under `src/content/`. README-style documentation must
  live in `docs/` (or `scripts/README.md` for the fix scripts): Astro's
  content collections pick up every file under `src/content/`, and a stray
  `.md`/`.yaml` there will either break the build or silently pollute the
  collections.
- Every node, source, and chapter must satisfy the Zod schemas in
  `src/content/config.ts`. The build fails on any missing required field.
- Formatting is enforced by Prettier; linting by ESLint; typography by
  `astro check`:
  ```bash
  npm run check    # Astro + TypeScript diagnostics
  npm run lint     # ESLint
  npx prettier --check .  # formatting
  npm run build    # final verification
  ```
- `src/content/` and `docs/` are excluded from Prettier scope: editorial
  text is never auto-reformatted.
- If a YAML edit fails to parse, see `scripts/README.md` for the idempotent
  fix scripts.

## Run

```bash
npm install
npm run dev      # local dev at http://localhost:4321/
npm run build    # static build to dist/
npm run preview  # preview the production build locally
```

## Deployment (GitHub Pages)

The site deploys to <https://canonmr.github.io/credo-the-inquiry/> via the
`Deploy to GitHub Pages` workflow (`.github/workflows/deploy.yml`) on every
push to `main`.

One-time setup, after the first push:

1. Create a repository named `credo-the-inquiry` on GitHub.
2. In the repo: Settings → Pages → **Source: GitHub Actions** (the workflow
   uploads `dist/` itself; do not pick a branch or folder).
3. Push to `main`; the first run of the deploy workflow publishes the site.

Because the site lives under the `/credo-the-inquiry/` path, all internal
links must be base-aware:

- Components and pages use `import.meta.env.BASE_URL` (see
  `src/components/Layout.astro`).
- Internal links in chapter MDX are written as absolute production URLs
  (`https://canonmr.github.io/credo-the-inquiry/…`). If the repository is
  renamed, update these targets and the `base`/`site` values in
  `astro.config.mjs`.
- In local dev (`npm run dev`) the base is `/`, so all links work unchanged.

## Bilingual routes

- `/id/` — Indonesian (primary)
- `/en/` — English
- `/id/chapters/01-…` — Chapter 1 in Indonesian
- `/en/chapters/01-…` — Chapter 1 in English
- `/id/nodes/POE-001` — node POE-001 in Indonesian (uses node's prose in the active language)
- `/en/nodes/POE-001` — node POE-001 in English

For the prototype, node pages fall back to the same English body if no Indonesian translation exists. Source pages are language-agnostic; they show the verified original quote and a translation when available.

## Non-negotiable rules (from `knowledge.md` and the Phase 0 brief)

1. No invented quotations, sources, page numbers, or Catholic doctrine.
2. Textual claims are kept separate from theological claims.
3. Conclusions are bounded by premises.
4. Foreknowledge, causation, permission, intention, possibility, plausibility, defense, and theodicy are kept distinct.
5. Plantinga's Free Will Defense is presented as a defense, not as a complete solution.
6. Fallen angels are not invoked to explain particular natural disasters.
7. Not every natural evil is mapped to a particular sin.
8. Catholicism is not declared established before the relevant arguments are developed.
9. No arbitrary numerical scores for worldviews.
10. The website is mobile-first; visualizations explain reasoning, not merely decorate.

## License

Internal project. Not yet released.
