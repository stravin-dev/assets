# Color System

The Stravin color system pairs warm architectural neutrals (**Basalt** and **Limestone**) with a three-step mineral teal scale and one high-contrast terracotta focal accent—standing apart from GitHub's slate/violet and GitLab's bright orange.

## Core Color Palette

| Role | Token Name | Hex | CSS Variable | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Dark Canvas** | Basalt 950 | <span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116` | `--stravin-basalt-950` | Default dark-mode background (`stravin.dev`, docs, web UI) |
| **Dark Surface** | Slate 900 | <span class="color-chip color-chip--slate-900" aria-hidden="true"></span>`#161B22` | `--stravin-slate-900` | Cards, navigation rails, code blocks, diff panels |
| **Dark Hairline** | Slate 800 | <span class="color-chip color-chip--slate-800" aria-hidden="true"></span>`#252D38` | `--stravin-slate-800` | Borders, table dividers, structural gridlines |
| **Light Canvas** | Limestone 50 | <span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2` | `--stravin-limestone-50` | Light-mode canvas and dark-mode primary wordmark/text |
| **Light Surface** | Limestone 100 | <span class="color-chip color-chip--limestone-100" aria-hidden="true"></span>`#EAE7DF` | `--stravin-limestone-100` | Light-mode secondary surfaces, code blocks, callouts |
| **Light Ink** | Ink 900 | <span class="color-chip color-chip--ink-900" aria-hidden="true"></span>`#14181F` | `--stravin-ink-900` | Primary light-mode typography and monochrome light-mode mark |
| **Isometric Top Plane** | Glacier Mint | <span class="color-chip color-chip--glacier-mint" aria-hidden="true"></span>`#64C5B9` | `--stravin-plane-top` | Upper monogram bar (dark mode), dark-mode hover states, active focus rings |
| **Brand Primary (Left Plane)** | Strata Teal | <span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F` | `--stravin-plane-mid` | Lower monogram bar (dark mode), primary links, active refs, Stravin Core accent |
| **Isometric Right Plane** | Abyss Teal | <span class="color-chip color-chip--abyss-teal" aria-hidden="true"></span>`#1C6E66` | `--stravin-plane-shadow` | Shaded tone, lower monogram bar (light mode), pressed states, subtle badge fills |
| **Focal Accent (Pin)** | Rivet Terracotta | <span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53` | `--stravin-accent` | Corner monogram anchor, primary CTAs, push/deploy highlights, live telemetry |

## Multi-Layer Product Accent System

Every Stravin product layer shares the same Basalt / Limestone neutral surfaces and geometric icon grid while claiming one restrained secondary accent for badges, docs sections, and sidebar indicators:

| Product Layer | Services / Scope | Accent Name | Hex | CSS Variable |
| :--- | :--- | :--- | :--- | :--- |
| **Stravin Core** | `stravin-edge`, `stravin-node`, `stravin-pack`, `stravin-ctrl` | Strata Teal | <span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F` | `--stravin-core` |
| **Stravin Review** | Pull requests, stacked diffs, repository browser | Blueprint Blue | <span class="color-chip color-chip--blueprint-blue" aria-hidden="true"></span>`#5B8DEF` | `--stravin-review` |
| **Stravin Run** | Ephemeral CI runners, pipelines, sandboxes | Rivet Terracotta | <span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53` | `--stravin-run` |
| **Stravin Index** | Trigram code search, symbol graph, cross-repo nav | Ochre Amber | <span class="color-chip color-chip--ochre-amber" aria-hidden="true"></span>`#D4A34B` | `--stravin-index` |
| **Stravin Gate** | Merge queues, branch protection, policy checks | Forged Steel | <span class="color-chip color-chip--forged-steel" aria-hidden="true"></span>`#7A8B99` | `--stravin-gate` |

## Light & Dark Semantic Tokens

Semantic surface, hairline, and ink tokens map consistently across both themes:

| Semantic Token | Dark Theme (Default) | Light Theme (`[data-theme="light"]`) | Purpose |
| :--- | :--- | :--- | :--- |
| `--bg-canvas` | <span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116` (Basalt 950) | <span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2` (Limestone 50) | Primary page background |
| `--bg-surface` | <span class="color-chip color-chip--slate-900" aria-hidden="true"></span>`#161B22` (Slate 900) | <span class="color-chip color-chip--limestone-100" aria-hidden="true"></span>`#EAE7DF` (Limestone 100) | Elevated cards, sidebars, code blocks |
| `--border-subtle` | <span class="color-chip color-chip--slate-800" aria-hidden="true"></span>`#252D38` (Slate 800) | <span class="color-chip color-chip--limestone-200" aria-hidden="true"></span>`#D5D0C5` (Limestone 200) | Hairlines, table dividers, card borders |
| `--text-primary` | <span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2` (Limestone 50) | <span class="color-chip color-chip--ink-900" aria-hidden="true"></span>`#14181F` (Ink 900) | Body copy, headings, wordmark |
| `--text-muted` | <span class="color-chip color-chip--slate-400" aria-hidden="true"></span>`#93A0B0` (Slate 400) | <span class="color-chip color-chip--ink-500" aria-hidden="true"></span>`#525C68` (Ink 500) | Secondary metadata, timestamps, captions |

## WCAG AA Contrast Guidance

!!! tip "Theme-Specific Brand Fills"
    Never reuse dark-mode brand fills verbatim on light backgrounds. Shift the monogram and link tones one step darker in light mode so every graphic and interactive element clears WCAG AA.

- **Dark canvas contrast:** Primary text in Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`) on Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116`) exceeds `17:1` (WCAG AAA). Muted metadata in Slate 400 (<span class="color-chip color-chip--slate-400" aria-hidden="true"></span>`#93A0B0`) clears `6.9:1` on Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116`) and `6.1:1` on Slate 900 (<span class="color-chip color-chip--slate-900" aria-hidden="true"></span>`#161B22`).
- **Light canvas contrast:** Primary text in Ink 900 (<span class="color-chip color-chip--ink-900" aria-hidden="true"></span>`#14181F`) on Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`) exceeds `16:1` (WCAG AAA). Muted metadata in Ink 500 (<span class="color-chip color-chip--ink-500" aria-hidden="true"></span>`#525C68`) clears `6.2:1` on Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`).
- **Monogram light-mode swap:** On Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`), swap the upper bar from Glacier Mint (<span class="color-chip color-chip--glacier-mint" aria-hidden="true"></span>`#64C5B9`) to Strata Teal (<span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F`) and the lower bar from Strata Teal (<span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F`) to Abyss Teal (<span class="color-chip color-chip--abyss-teal" aria-hidden="true"></span>`#1C6E66`) so both bars clear WCAG AA graphical contrast (`>= 3:1`) while keeping the Rivet Terracotta (<span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53`) corner anchor unchanged.
- **Interactive links on light surfaces:** Prefer Abyss Teal (<span class="color-chip color-chip--abyss-teal" aria-hidden="true"></span>`#1C6E66`) for small body links on Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`) (`5.5:1`), reserving Strata Teal (<span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F`) for large UI elements, borders, and icons.

## Drop-in CSS Custom Properties

Copy these variables directly into `stravin.dev` applications and docs:

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
