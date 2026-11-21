# Favicons & Applications

Because the Stravin monogram uses uniform `18`-unit strokes on a `100×100` grid with zero gradients, it scales cleanly down to `16×16` browser tabs, mobile home screens, CLI banners, and single-color print merchandise.

## Favicon & Touch Icon Previews

<div class="brand-preview-grid">
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__icon" src="../assets/generated/favicon.svg" alt="Stravin SVG favicon">
    </div>
    <div class="brand-preview__caption">
      <strong>SVG Favicon (<code>favicon.svg</code>)</strong>
      Primary vector favicon for modern browsers (sharp at <code>16×16</code> and HiDPI)
    </div>
  </div>
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__icon" src="../assets/generated/apple-touch-icon.png" alt="Stravin Apple Touch Icon 180x180">
    </div>
    <div class="brand-preview__caption">
      <strong>Apple Touch Icon (<code>apple-touch-icon.png</code>)</strong>
      <code>180×180</code> PNG on Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span><code>#0E1116</code>) canvas for iOS &amp; iPadOS bookmarks
    </div>
  </div>
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__icon" src="../assets/generated/favicon.ico" alt="Stravin multi-resolution ICO favicon">
    </div>
    <div class="brand-preview__caption">
      <strong>Legacy ICO Fallback (<code>favicon.ico</code>)</strong>
      Multi-size <code>16×16</code>, <code>32×32</code>, <code>48×48</code> ICO bundle for legacy clients
    </div>
  </div>
</div>

## HTML `<head>` Favicon Snippet

Drop the wordmark below `48px` and serve the standalone mark. Include the SVG favicon first, followed by the multi-size `.ico` fallback and the `180×180` Apple Touch Icon:

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0E1116">
```

## PWA & Platform Icon Matrix

`stravin-assets build` generates every standard web, PWA, and social size directly from the canonical SVG templates:

| Asset | Dimensions | Background | Target Surface |
| :--- | :--- | :--- | :--- |
| `favicon.svg` | Vector (`100×100`) | Transparent | Modern desktop & mobile browsers |
| `favicon.ico` | `16×16`, `32×32`, `48×48` | Transparent | Legacy browsers, bookmarks, RSS readers |
| `apple-touch-icon.png` | `180×180` | Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116`) | iOS / iPadOS home screen |
| `icon-192.png` | `192×192` | Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116`) | Android & PWA manifest icon |
| `icon-512.png` | `512×512` | Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116`) | PWA splash screen & app stores |
| `stravin-mark-dark-512.png` | `512×512` | Transparent | Avatars, GitHub org icon, slide decks |
| `stravin-lockup-dark-720.png` | `720×200` | Transparent | Documentation banners, release notes |

Example `site.webmanifest` entries:

```json
{
  "name": "Stravin",
  "short_name": "Stravin",
  "theme_color": "#0E1116",
  "background_color": "#0E1116",
  "display": "standalone",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

## CLI, Terminal & 1-Color Merch Rules

- **CLI & Terminal Headers:** Use `stravin-mark-mono.svg` (or ANSI-colored Strata Teal <span class="color-chip color-chip--strata-teal" aria-hidden="true"></span>`#2A9D8F` + Rivet Terracotta <span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53` glyphs). Always respect `NO_COLOR` by falling back to plain terminal foreground text.
- **2-Color Apparel / Stickers:** Render both interlocking `<path>` strokes in Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`) on dark fabric or Ink 900 (<span class="color-chip color-chip--ink-900" aria-hidden="true"></span>`#14181F`) on light fabric, keeping the corner square in Rivet Terracotta (<span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53`).
- **Strict 1-Color Print / Laser Etching / Embroidery:** Use `stravin-mark-mono-1c.svg`, where both bars use `currentColor` and the corner anchor uses `currentColor` at `0.55` opacity (or halftone/knockout in single-ink screen printing).
