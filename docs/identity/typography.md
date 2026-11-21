# Typography

Stravin pairs a geometric display wordmark with high-legibility neo-grotesque UI prose and a crisp programming monospace for Git OIDs, ref paths, and CLI output.

## Font Families & Roles

| Role | Primary Typeface | Secondary / Fallback Stack | Weight & Tracking |
| :--- | :--- | :--- | :--- |
| **Wordmark** | **Space Grotesk** | `'Plus Jakarta Sans', system-ui, sans-serif` | Uppercase; Medium `500` with `0.18em` tracking (display/marketing) or SemiBold `600` with `0.16em` tracking (navbar lockup) |
| **UI & Documentation** | **Inter** | `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Regular `400` body, Medium `500` labels, SemiBold `600` headings |
| **Code, OIDs & CLI** | **JetBrains Mono** | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` | Regular `400` code/diffs, Medium `500` CLI flags and prompts |

## Specimens

### Wordmark

<div class="type-specimen type-specimen--wordmark">
  STRAVIN
</div>

- Always set `STRAVIN` in **uppercase** when used as a brand lockup.
- In horizontal navigation lockups (`stravin-lockup-*.svg`), use weight `600` and `0.16em` letter-spacing so letterforms stay crisp at `48px`–`64px` heights.
- In large hero banners or print mastheads, lighten to weight `500` and widen tracking to `0.18em`.

### UI & Documentation Prose

<div class="type-specimen type-specimen--ui">
  <strong>Stravin Core</strong> stores Git packfiles in object storage while maintaining low-latency ref transactions and deterministic server-side hooks.
</div>

- Default body copy uses `16px` (`1rem`) with `1.6` line-height in Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`) on dark surfaces or Ink 900 (<span class="color-chip color-chip--ink-900" aria-hidden="true"></span>`#14181F`) on light surfaces.
- Secondary metadata, timestamps, and table captions step down to `0.85rem` in Slate 400 (<span class="color-chip color-chip--slate-400" aria-hidden="true"></span>`#93A0B0`) (dark) or Ink 500 (<span class="color-chip color-chip--ink-500" aria-hidden="true"></span>`#525C68`) (light).

### Code, Commit OIDs & CLI Output

<div class="type-specimen type-specimen--mono">
  $ stravin-assets build --out-dir dist --docs-dir docs/assets/generated<br>
  refs/heads/main &rarr; a23a3fa9c4e1b08d2f6a7c9e1234567890abcdef
</div>

- Use `JetBrains Mono` for commit hashes, ref names (`refs/heads/main`), diff hunks, file paths, and terminal transcripts.
- Enable tabular numerals (`font-variant-numeric: tabular-nums`) in tables displaying byte counts, latencies, or hex tokens.

## Type Hierarchy

| Element | Font Family | Size | Weight | Line Height |
| :--- | :--- | :--- | :--- | :--- |
| **Page Title (`h1`)** | `Inter` | `2rem` (`32px`) | `600` | `1.25` |
| **Section Heading (`h2`)** | `Inter` | `1.5rem` (`24px`) | `600` | `1.3` |
| **Subsection (`h3`)** | `Inter` | `1.15rem` (`18.4px`) | `600` | `1.35` |
| **Body Prose** | `Inter` | `1rem` (`16px`) | `400` | `1.6` |
| **Table / UI Label** | `Inter` | `0.875rem` (`14px`) | `500` | `1.4` |
| **Inline Code / OID** | `JetBrains Mono` | `0.875rem` (`14px`) | `400` | `1.5` |

## CSS Font Stacks

```css
:root {
  --font-wordmark: "Space Grotesk", "Plus Jakarta Sans", system-ui, sans-serif;
  --font-sans: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}
```
