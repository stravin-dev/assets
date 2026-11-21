# Stravin Branding & Visual Identity

## Brand Identity Overview

The **Stravin** identity centers on a minimalist, geometric interlocking **"S"** monogram paired with warm architectural neutrals, a three-step mineral teal scale, and a single terracotta accent.

Designed to scale across the full platform—beyond Git hosting into CI, code search, review, and merge gates—the mark consists of two balanced interlocking bars with uniform 18-unit stroke thickness, exact 3:4 diagonals, even negative-space channels, and one terracotta corner anchor on a 100×100 grid. Because depth and separation rely purely on calibrated flat surface tones rather than gradients or drop shadows, the mark stays sharp from a 16×16 `stravin.dev` favicon up to documentation hero graphics and terminal headers.

## Core Color Palette

The palette pairs warm architectural neutrals with a three-step mineral teal scale and one high-contrast terracotta focal accent—standing apart from GitHub's slate/violet and GitLab's bright orange.

| Role | Token Name | Hex | Usage |
| :--- | :--- | :--- | :--- |
| **Dark Canvas** | Basalt 950 | `#0E1116` | Default dark-mode background (`stravin.dev`, docs, web UI) |
| **Dark Surface** | Slate 900 | `#161B22` | Cards, navigation rails, code blocks, diff panels |
| **Dark Hairline** | Slate 800 | `#252D38` | Borders, table dividers, structural gridlines |
| **Light Canvas** | Limestone 50 | `#F7F6F2` | Light-mode canvas and dark-mode primary wordmark/text |
| **Light Surface** | Limestone 100 | `#EAE7DF` | Light-mode secondary surfaces, code blocks, callouts |
| **Light Ink** | Ink 900 | `#14181F` | Primary light-mode typography and monochrome light-mode mark |
| **Isometric Top Plane** | Glacier Mint | `#64C5B9` | Upper monogram bar (dark mode), dark-mode hover states, active focus rings |
| **Brand Primary (Left Plane)** | Strata Teal | `#2A9D8F` | Lower monogram bar (dark mode), primary links, active refs, Stravin Core accent |
| **Isometric Right Plane** | Abyss Teal | `#1C6E66` | Shaded tone, lower monogram bar (light mode), pressed states, subtle badge fills |
| **Focal Accent (Pin)** | Rivet Terracotta | `#E06D53` | Corner monogram anchor, primary CTAs, push/deploy highlights, live telemetry |

## Multi-Layer Product Accent System

Every product layer shares the same Basalt / Limestone surfaces and geometric icon grid while claiming one restrained secondary accent for badges, docs sections, and sidebar indicators:

| Product Layer | Services / Scope | Accent Name | Hex |
| :--- | :--- | :--- | :--- |
| **Stravin Core** | `stravin-edge`, `stravin-node`, `stravin-pack`, `stravin-ctrl` | Strata Teal | `#2A9D8F` |
| **Stravin Review** | Pull requests, stacked diffs, repository browser | Blueprint Blue | `#5B8DEF` |
| **Stravin Run** | Ephemeral CI runners, pipelines, sandboxes | Rivet Terracotta | `#E06D53` |
| **Stravin Index** | Trigram code search, symbol graph, cross-repo nav | Ochre Amber | `#D4A34B` |
| **Stravin Gate** | Merge queues, branch protection, policy checks | Forged Steel | `#7A8B99` |

## Logo SVGs

### Standalone Mark (`stravin-mark.svg`)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Stravin">
  <path d="M 67 6 H 32 L 8 24 V 45 L 40 69 H 60 L 65 65.25 L 24 34.5 L 38 24 H 67 Z" fill="#64C5B9" />
  <path d="M 40 31 H 60 L 92 55 V 76 L 68 94 H 8 V 76 H 62 L 76 65.5 L 35 34.75 Z" fill="#2A9D8F" />
  <rect x="74" y="6" width="18" height="18" fill="#E06D53" />
</svg>
```

### Horizontal Navbar Lockup (`stravin-lockup.svg`)

Uses `currentColor` for the wordmark so it switches cleanly between `#F7F6F2` (dark mode) and `#14181F` (light mode) without maintaining two separate assets:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 100" role="img" aria-label="Stravin">
  <g>
    <path d="M 67 6 H 32 L 8 24 V 45 L 40 69 H 60 L 65 65.25 L 24 34.5 L 38 24 H 67 Z" fill="#64C5B9" />
    <path d="M 40 31 H 60 L 92 55 V 76 L 68 94 H 8 V 76 H 62 L 76 65.5 L 35 34.75 Z" fill="#2A9D8F" />
    <rect x="74" y="6" width="18" height="18" fill="#E06D53" />
  </g>
  <text x="116" y="66" fill="currentColor" font-family="'Space Grotesk', 'Plus Jakarta Sans', system-ui, sans-serif" font-size="48" font-weight="600" letter-spacing="0.16em">STRAVIN</text>
</svg>
```

## Typography & Usage Guidelines

- **Wordmark & Type Pairing:** Set `STRAVIN` in uppercase geometric sans-serif (**Space Grotesk** or **Plus Jakarta Sans**, Medium 500, `0.18em` tracking; navbar lockup uses weight 600 and `0.16em` tracking). Pair with **Inter** for documentation and UI prose and **JetBrains Mono** for commit OIDs, ref paths, and CLI snippets.
- **Light Mode Contrast:** On `#F7F6F2` (Limestone 50), swap the upper bar fill from `#64C5B9` to `#2A9D8F` and the lower bar from `#2A9D8F` to `#1C6E66` so both bars clear WCAG AA contrast against the light background while keeping the `#E06D53` corner square unchanged.
- **Monochrome / CLI / Merch:** Set both `<path>` fills to `currentColor` and leave the `<rect>` at `#E06D53` (or `currentColor` at `0.55` opacity for strict 1-color prints).
- **Favicon Setup:** Drop the wordmark below `48px` and use only the standalone mark. Save `stravin-mark.svg` as `/favicon.svg` and reference `<link rel="icon" type="image/svg+xml" href="/favicon.svg">`—modern browsers render SVG favicons natively, and the thick 18-unit strokes stay legible even at `16×16` pixels.

## CSS Custom Properties

Drop-in CSS variables for `stravin.dev`:

```css
:root {
  /* Brand & Isometric Planes */
  --stravin-plane-top: #64C5B9;
  --stravin-plane-mid: #2A9D8F;
  --stravin-plane-shadow: #1C6E66;
  --stravin-accent: #E06D53;

  /* Product Layer Accents */
  --stravin-core: #2A9D8F;
  --stravin-review: #5B8DEF;
  --stravin-run: #E06D53;
  --stravin-index: #D4A34B;
  --stravin-gate: #7A8B99;

  /* Dark Theme (Default) */
  --bg-canvas: #0E1116;
  --bg-surface: #161B22;
  --border-subtle: #252D38;
  --text-primary: #F7F6F2;
  --text-muted: #93A0B0;
}

[data-theme="light"] {
  --bg-canvas: #F7F6F2;
  --bg-surface: #EAE7DF;
  --border-subtle: #D5D0C5;
  --text-primary: #14181F;
  --text-muted: #525C68;
}
```
