# Limpopo Digital Twin Portal — Documentation

Bilingual (English / Portuguese) MkDocs documentation site for the TerriaJS
WebGIS portal showcasing the Digital Twin (DT) of the Limpopo River Basin,
developed for IWMI.

The content is derived from `DT_03_UserGuide_Terra_JS_Digital Twin.docx`
(August 2024).

## Quick start

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. The dev server live-reloads on save.

## Build

```bash
mkdocs build --strict
```

The static site is written to `site/` (git-ignored). `--strict` turns broken
internal links and invalid config into build failures — use it in CI.

## Versions

The site is versioned with [`mike`](https://github.com/jimporter/mike). Each
version is a snapshot built into its own subdirectory of the `gh-pages`
branch, and Material's header shows a version selector driven by the
`versions.json` at the deployment root.

| Version | Documents | Portal |
| --- | --- | --- |
| `v2` (alias `latest`, default) | TerriaMap `0.4.1` / TerriaJS `8.9.5`, built 2026-05-15 | <https://limpopo.digitaltwins.iwmi.org/> |
| `v1` | TerriaMap `0.1.2` / TerriaJS `8.7.1`, built 2024-08-26 | retired |

`v1` is frozen: it is the guide as written from the August 2024 Word document
and should not be edited except to correct errors. Ongoing work happens on
`v2`.

### Working with versions

```bash
mike list                       # show deployed versions
mike serve                      # preview the whole versioned site locally
mike deploy --update-aliases v2 latest   # rebuild v2 and keep it as `latest`
mike set-default latest         # make / redirect to the default version
mike retitle v2 "v2 (current)"  # change a version's display title
```

Note `mike serve` previews what is on `gh-pages`; for authoring use
`mkdocs serve`, which live-reloads the working tree.

### Cutting a new version

When the portal ships a release worth documenting separately:

```bash
# freeze what is current under its own name first, if not already deployed
mike deploy v2

# then update docs/ for the new release and publish it as latest
mike deploy --update-aliases v3 latest
mike set-default latest
```

## Deploy

`mike` writes to the local `gh-pages` branch. To publish:

```bash
git push origin gh-pages
```

Add `--push` to any `mike deploy` to build and push in one step. Any static
host works too — serve the contents of the `gh-pages` branch.

> **Note:** `mkdocs gh-deploy` is *not* used here — it would overwrite the
> whole `gh-pages` branch and destroy the version subdirectories.

### Railway

The versioned site is also deployed to Railway as a static container (Caddy):

- **Live URL:** <https://dt-limpopo-docs-production.up.railway.app>
- **Project:** `dt-limpopo-docs` (Railway CLI must be logged in: `railway login`)

To (re)deploy after changing docs:

```bash
mike deploy --update-aliases v2 latest   # update the gh-pages build first
./deploy-railway.sh                        # materialise public/ and railway up
```

`deploy-railway.sh` copies the `gh-pages` output into `public/` (resolving the
`latest` alias, since Windows can't create the symlink) and runs `railway up`.

- `Dockerfile` / `Caddyfile` — a `caddy:2-alpine` image serving `public/` on
  `$PORT`, with the root redirecting to `latest/`.
- `public/` is **generated** — do not commit it (~90 MB). It is deliberately
  **not** in `.gitignore`, because `railway up` skips gitignored paths and the
  image needs it in the build context; just avoid `git add public/`.

## Branding

Styling follows the [IWMI brand guidelines](https://branding.iwmi.org/), in
`docs/stylesheets/extra.css`:

- **Colour** — Dark Blue `#28537D` as primary and Sky Blue `#46BBD4` as
  accent, keeping to the brand rule that "in most instances only two colours
  may be used in combination, on a grey/white background". The secondary
  palette (Teal `#0297A6`, Green `#22AD7A`, Orange `#E86933`, Yellow
  `#DD9103`) is reserved for semantic admonition accents.
- **Type** — [DM Serif Text](https://fonts.google.com/specimen/DM+Serif+Text)
  for headings and **National** for body text, as specified.

> **Font licensing:** National is a commercial typeface and cannot be
> self-hosted without a licence — contact iwmi-communications@cgiar.org for
> terms. It is listed first in the CSS font stack so licensed machines use it,
> with **Inter** as the free fallback. If IWMI holds a web licence, drop the
> web-font files into `docs/stylesheets/` and add an `@font-face` rule; no
> other change is needed.

Material's `theme.font` is set to `false` so it does not load Roboto over the
top; both palette entries use `primary: custom` / `accent: custom`, which the
stylesheet then defines.

## Upstream application source

The portal's own source lives in
[iwmihq/dt-app](https://github.com/iwmihq/dt-app). A working copy is cloned to
`dt-app/` (git-ignored, ~400 MB) and is the reference for version facts:

- `dt_limpopo/` — the current Limpopo portal (what `v2` documents)
- `TerriaJS/` — the retired v1 codebase (what `v1` documents)
- `dt_limpopo/CHANGES.md` — the changelog behind `docs/reference/release-notes.md`

Refresh it with `git -C dt-app pull`. The live build's version can always be
checked at <https://limpopo.digitaltwins.iwmi.org/version.json>.

## Languages

The site is bilingual: **English** (default, at `/`) and **Portuguese**
(at `/pt/`), built with `mkdocs-static-i18n` in *suffix* mode.

Each page exists as a pair — `page.md` (English) and `page.pt.md`
(Portuguese) — in the same folder:

```
docs/guide/workbench.md        -> /guide/workbench/
docs/guide/workbench.pt.md     -> /pt/guide/workbench/
```

Both languages share the same `docs/assets/images/`, so screenshots are stored
once.

### Adding or editing a translation

- **Edit an existing page:** change the `.md` and the matching `.pt.md`.
- **Add a new page:** create `newpage.md`, add it to `nav:` in `mkdocs.yml`,
  then create `newpage.pt.md` alongside it. Add the nav label to the
  `nav_translations:` block so the sidebar entry is translated too.
- **Missing translation:** `fallback_to_default: true` means a page without a
  `.pt.md` falls back to the English version rather than 404ing, so the
  Portuguese site is never broken mid-translation.

### Translation conventions

- **Portal UI labels stay in English.** The portal interface itself is in
  English, so button and panel names are kept as they appear on screen, with a
  Portuguese gloss in parentheses on first use — for example,
  **Explore Map Data** (*Explorar dados do mapa*). A guide that renamed the
  buttons would not match what the reader sees.
- The Portuguese used is European/Mozambican (pt-PT), matching the
  Portuguese-speaking part of the Limpopo basin.
- Screenshots are the originals and therefore show English UI text.

### Notes on configuration

- `navigation.instant` is intentionally **not** enabled. It is incompatible
  with the i18n language switcher's contextual link, which would otherwise
  send readers to the other language's home page instead of the equivalent
  page.
- Search covers both languages from a single index (`lang: [en, pt]`), so a
  query may return results in either language.

## Layout

```
mkdocs.yml              # site config, theme, navigation and i18n
requirements.txt        # pinned MkDocs + plugins
docs/
  index.md / index.pt.md    # landing page (EN / PT)
  guide/                    # user guide (the bulk of the original document)
  project/                  # overview, architecture, development, deployment
  reference/                # source notes, portal version, glossary
  assets/images/            # 62 screenshots extracted from the .docx (shared)
  stylesheets/extra.css     # figure framing and side-by-side screenshot pairs
```

## Notes on the content

- **Figures were renumbered.** The source document had gaps and duplicates
  (two figures labelled 14, three labelled 54). Numbering here runs
  sequentially; the screenshots themselves are unchanged.
- **Images** were extracted from the `.docx` with Pandoc and kept at their
  original resolution. They are click-to-zoom via the `glightbox` plugin.
- The original Word document is retained in the repository root as the source
  of record.

## Editing

Pages are plain Markdown with a few extensions enabled in `mkdocs.yml`:
admonitions (`!!! note`), definition lists, `attr_list`/`md_in_html` (used for
`<figure>` blocks and grid cards), tables, and `pymdownx.keys` for keyboard
keys. Add a new page by creating the Markdown file under `docs/` and listing it
in the `nav:` section of `mkdocs.yml`.

## Use-case charts

The figures on the Use Cases pages are the portal's own feature-info charts,
captured with `dt-app/dt_limpopo/demo/portal-charts.mjs` (Playwright, against a
local build loaded with the production catalogue) into
`docs/assets/charts/portal/`. Each scenario in that script names a catalogue
item id and the coordinates of the feature to click; re-run it after the
catalogue changes.

### Derived charts

The charts on the Use Cases pages (`docs/assets/charts/*.png`) are rendered from
live responses of the IWMI Digital Twins API by `tools/use_case_charts.py`
(matplotlib + pandas). Raw responses are cached in `tools/.cache/` (git-ignored).

```bash
pip install matplotlib pandas
python tools/use_case_charts.py            # render from cache, downloading what is missing
python tools/use_case_charts.py --refresh  # re-download everything and re-render
```

Re-run before a release so the "as of" dates in the chart subtitles stay current,
then update any numbers quoted in the pages' "At a glance" boxes.
