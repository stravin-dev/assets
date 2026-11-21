# Stravin Brand & Assets

The **Stravin** visual identity centers on a minimalist, geometric interlocking **"S"** monogram paired with warm architectural neutrals, a three-step mineral teal scale, and a single terracotta accent.

Designed to scale across the full Stravin platform—beyond Git hosting into code review, ephemeral CI runners, trigram code search, and merge gates—the mark relies purely on calibrated flat surface tones rather than gradients or drop shadows. It stays razor-sharp from a `16×16` browser favicon up to documentation heroes and terminal headers.

## Brand Preview

<div class="brand-preview-grid">
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__lockup" src="assets/generated/stravin-lockup-dark.svg" alt="Stravin dark-mode horizontal lockup">
    </div>
    <div class="brand-preview__caption">
      <strong>Dark-Mode Lockup (Default)</strong>
      Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span><code>#0E1116</code>) canvas with Glacier Mint &amp; Strata Teal mark
    </div>
  </div>
  <div class="brand-preview brand-preview--light">
    <div class="brand-preview__stage">
      <img class="brand-preview__lockup" src="assets/generated/stravin-lockup-light.svg" alt="Stravin light-mode horizontal lockup">
    </div>
    <div class="brand-preview__caption">
      <strong>Light-Mode Lockup</strong>
      Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span><code>#F7F6F2</code>) canvas with Strata Teal &amp; Abyss Teal mark
    </div>
  </div>
</div>

## Visual System Pillars

| Pillar | Specification | Reference |
| :--- | :--- | :--- |
| **Geometric Monogram** | Two interlocking bars on a `100×100` grid with `18`-unit stroke weight, exact `3:4` diagonals, and one corner anchor | [Logos & Marks](identity/logos.md) |
| **Mineral & Architectural Palette** | Basalt & Limestone neutrals, three-step mineral teal (<span class="color-chip color-chip--glacier-mint" aria-hidden="true"></span>`#64C5B9`, <span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F`, <span class="color-chip color-chip--abyss-teal" aria-hidden="true"></span>`#1C6E66`), and Rivet Terracotta (<span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53`) | [Color System](identity/colors.md) |
| **Product Layer Accents** | Five restrained accents differentiating Core, Review, Run, Index, and Gate across shared neutral surfaces | [Color System](identity/colors.md#multi-layer-product-accent-system) |
| **Technical Typography** | `Space Grotesk` / `Plus Jakarta Sans` wordmark, `Inter` for UI/docs prose, `JetBrains Mono` for OIDs and CLI output | [Typography](identity/typography.md) |
| **Deterministic Asset Pipeline** | Single-source SVG templates compiled to PNG, ICO, and WebP derivatives via `stravin-assets` | [Asset CLI & Workflow](tooling/cli.md) |

## Quick Links

- [Logos & Marks](identity/logos.md) — Mark geometry, dark/light/monochrome variants, clear space, minimum sizes, and usage rules
- [Color System](identity/colors.md) — Core palette, product accents, semantic theme tokens, contrast rules, and drop-in CSS variables
- [Typography](identity/typography.md) — Wordmark tracking, type hierarchy, and system fallback stacks
- [Favicons & Applications](identity/favicons-and-applications.md) — Drop-in HTML `<head>` snippets, PWA icons, terminal, and 1-color print specs
- [Asset CLI & Workflow](tooling/cli.md) — `stravin-assets` commands, output tree, and `Makefile` automation

## Regenerating Assets & Previewing Docs

All generated SVG, PNG, ICO, and WebP assets are built deterministically from code and synced into `docs/assets/generated/` before building the site:

```bash
# Regenerate all brand assets and sync docs/assets/generated/
asdf exec make assets

# Preview this documentation site locally at http://localhost:8001 with live reload
asdf exec make serve

# Run full lint, test, asset generation, and strict Zensical build
asdf exec make check
```
