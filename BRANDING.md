# Stravin Branding & Visual Identity

> **Canonical Documentation:** The complete Stravin Brand & Assets handbook—including live dark/light asset previews, visual color chips, typography specimens, favicon snippets, and the `stravin-assets` CLI reference—lives in [`docs/`](./docs/index.md). This root file is a concise summary kept in sync with the exact canonical tokens.

## Brand Identity Overview

The **Stravin** identity centers on a minimalist, geometric interlocking **"S"** monogram paired with warm architectural neutrals, a three-step mineral teal scale, and a single terracotta accent.

Designed to scale across the full platform—beyond Git hosting into CI, code search, review, and merge gates—the mark consists of two balanced interlocking bars with uniform 18-unit stroke thickness, exact 3:4 diagonals, even negative-space channels, and one terracotta corner anchor on a 100×100 grid.

## Core Color Palette

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

| Product Layer | Services / Scope | Accent Name | Hex |
| :--- | :--- | :--- | :--- |
| **Stravin Core** | `stravin-edge`, `stravin-node`, `stravin-pack`, `stravin-ctrl` | Strata Teal | `#2A9D8F` |
| **Stravin Review** | Pull requests, stacked diffs, repository browser | Blueprint Blue | `#5B8DEF` |
| **Stravin Run** | Ephemeral CI runners, pipelines, sandboxes | Rivet Terracotta | `#E06D53` |
| **Stravin Index** | Trigram code search, symbol graph, cross-repo nav | Ochre Amber | `#D4A34B` |
| **Stravin Gate** | Merge queues, branch protection, policy checks | Forged Steel | `#7A8B99` |

## Theme Semantic Tokens

| Theme | Canvas | Surface | Subtle Border | Primary Text | Muted Text |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dark (Default)** | `#0E1116` | `#161B22` | `#252D38` | `#F7F6F2` | `#93A0B0` |
| **Light** | `#F7F6F2` | `#EAE7DF` | `#D5D0C5` | `#14181F` | `#525C68` |

## Documentation Map

- [Overview](./docs/index.md)
- [Logos & Marks](./docs/identity/logos.md) — Standalone mark, horizontal lockup, clear space, minimum sizes, and do's/don'ts
- [Color System](./docs/identity/colors.md) — Full color reference with visual chips, contrast rules, and CSS custom properties
- [Typography](./docs/identity/typography.md) — Wordmark (`Space Grotesk` / `Plus Jakarta Sans`), UI (`Inter`), and Code (`JetBrains Mono`)
- [Favicons & Applications](./docs/identity/favicons-and-applications.md) — Web favicons, PWA icons, CLI, and 1-color print specs
- [Asset CLI & Workflow](./docs/tooling/cli.md) — `stravin-assets` CLI and `Makefile` automation
