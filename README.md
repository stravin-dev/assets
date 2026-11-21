# Stravin Brand & Assets

Brand identity guidelines, visual tokens, Zensical documentation site, and deterministic SVG-to-raster asset generation CLI (`stravin-assets`) for Stravin.

## Documentation

The full brand handbook lives in [`docs/`](./docs/index.md) and builds with Zensical:

- [Overview](./docs/index.md) — Brand pillars, quick previews, and asset workflow
- [Logos & Marks](./docs/identity/logos.md) — Interlocking "S" mark anatomy, dark/light/monochrome variants, clear space, and usage rules
- [Color System](./docs/identity/colors.md) — Core palette, product layer accents, theme tokens, WCAG AA contrast, and CSS custom properties
- [Typography](./docs/identity/typography.md) — Wordmark, UI prose, and monospace type stacks
- [Favicons & Applications](./docs/identity/favicons-and-applications.md) — HTML `<head>` snippets, PWA icons, CLI, and 1-color merch rules
- [Asset CLI & Workflow](./docs/tooling/cli.md) — `stravin-assets` CLI reference, rendering pipeline, and `Makefile` targets

For a quick single-file reference of the core tokens and canonical SVGs, see [BRANDING.md](./BRANDING.md).

## Quickstart

```bash
asdf exec make install   # Install Python dependencies via uv
asdf exec make assets    # Generate SVGs, PNGs, ICO, WebP into dist/ and sync docs/assets/generated/
asdf exec make serve     # Serve the Zensical branding docs site locally at http://localhost:8001
asdf exec make check     # Run linter, tests, asset generation, and strict docs build
```
