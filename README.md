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

## Deploy

To publish to GitHub Pages:

```bash
mkdocs gh-deploy
```

Any static host works too — just serve the contents of `site/`.

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
