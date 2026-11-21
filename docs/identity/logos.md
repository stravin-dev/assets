# Logos & Marks

The Stravin logo system comprises a geometric interlocking **"S"** standalone mark and a paired horizontal wordmark lockup. Both are constructed from exact coordinates on a `100×100` unit grid with flat surface fills—never gradients, blurs, or drop shadows.

## Mark Anatomy

| Property | Specification |
| :--- | :--- |
| **Grid** | `100 × 100` viewBox (`0 0 100 100`) |
| **Stroke Weight** | Uniform `18`-unit bar thickness across both interlocking strokes |
| **Diagonal Slope** | Exact `3:4` architectural diagonals with even negative-space channels |
| **Corner Anchor** | `18 × 18` square rivet at `(74, 6)` filled with Rivet Terracotta (<span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span>`#E06D53`) |
| **Lockup Canvas** | `360 × 100` viewBox with uppercase `STRAVIN` wordmark set at `x="116" y="66"` |

## Standalone Mark Variants

<div class="brand-preview-grid">
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__mark" src="../assets/generated/stravin-mark-dark.svg" alt="Stravin standalone mark dark mode">
    </div>
    <div class="brand-preview__caption">
      <strong>Dark Mode (<code>stravin-mark-dark.svg</code>)</strong>
      Upper bar <span class="color-chip color-chip--glacier-mint" aria-hidden="true"></span><code>#64C5B9</code>, lower bar <span class="color-chip color-chip--strata-teal" aria-hidden="true"></span><code>#2A9D8F</code>, anchor <span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span><code>#E06D53</code>
    </div>
  </div>
  <div class="brand-preview brand-preview--light">
    <div class="brand-preview__stage">
      <img class="brand-preview__mark" src="../assets/generated/stravin-mark-light.svg" alt="Stravin standalone mark light mode">
    </div>
    <div class="brand-preview__caption">
      <strong>Light Mode (<code>stravin-mark-light.svg</code>)</strong>
      Upper bar <span class="color-chip color-chip--strata-teal" aria-hidden="true"></span><code>#2A9D8F</code>, lower bar <span class="color-chip color-chip--abyss-teal" aria-hidden="true"></span><code>#1C6E66</code>, anchor <span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span><code>#E06D53</code>
    </div>
  </div>
  <div class="brand-preview brand-preview--light">
    <div class="brand-preview__stage">
      <img class="brand-preview__mark" src="../assets/generated/stravin-mark-mono.svg" alt="Stravin monochrome mark with terracotta anchor">
    </div>
    <div class="brand-preview__caption">
      <strong>Monochrome + Accent (<code>stravin-mark-mono.svg</code>)</strong>
      Both bars use <code>currentColor</code>; anchor stays <span class="color-chip color-chip--rivet-terracotta" aria-hidden="true"></span><code>#E06D53</code>
    </div>
  </div>
  <div class="brand-preview brand-preview--light">
    <div class="brand-preview__stage">
      <img class="brand-preview__mark" src="../assets/generated/stravin-mark-mono-1c.svg" alt="Stravin strict 1-color monochrome mark">
    </div>
    <div class="brand-preview__caption">
      <strong>Strict 1-Color (<code>stravin-mark-mono-1c.svg</code>)</strong>
      Both bars <code>currentColor</code>; anchor <code>currentColor</code> at <code>0.55</code> opacity
    </div>
  </div>
</div>

### Canonical Standalone Mark SVG (Dark Default)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Stravin">
  <path d="M 67 6 H 32 L 8 24 V 45 L 40 69 H 60 L 65 65.25 L 24 34.5 L 38 24 H 67 Z" fill="#64C5B9" />
  <path d="M 40 31 H 60 L 92 55 V 76 L 68 94 H 8 V 76 H 62 L 76 65.5 L 35 34.75 Z" fill="#2A9D8F" />
  <rect x="74" y="6" width="18" height="18" fill="#E06D53" />
</svg>
```

## Horizontal Lockup Variants

Use the horizontal lockup in navigation bars, documentation headers, and slide decks whenever vertical height is at least `48px`.

<div class="brand-preview-grid">
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__lockup" src="../assets/generated/stravin-lockup-dark.svg" alt="Stravin horizontal lockup dark mode">
    </div>
    <div class="brand-preview__caption">
      <strong>Dark Lockup (<code>stravin-lockup-dark.svg</code>)</strong>
      Wordmark in Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span><code>#F7F6F2</code>) for Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span><code>#0E1116</code>) headers
    </div>
  </div>
  <div class="brand-preview brand-preview--light">
    <div class="brand-preview__stage">
      <img class="brand-preview__lockup" src="../assets/generated/stravin-lockup-light.svg" alt="Stravin horizontal lockup light mode">
    </div>
    <div class="brand-preview__caption">
      <strong>Light Lockup (<code>stravin-lockup-light.svg</code>)</strong>
      Wordmark in Ink 900 (<span class="color-chip color-chip--ink-900" aria-hidden="true"></span><code>#14181F</code>) for Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span><code>#F7F6F2</code>) headers
    </div>
  </div>
  <div class="brand-preview brand-preview--light">
    <div class="brand-preview__stage">
      <img class="brand-preview__lockup" src="../assets/generated/stravin-lockup-currentcolor.svg" alt="Stravin currentColor horizontal lockup">
    </div>
    <div class="brand-preview__caption">
      <strong>Inline Themeable Lockup (<code>stravin-lockup-currentcolor.svg</code>)</strong>
      Wordmark uses <code>currentColor</code> so inline SVGs switch between <span class="color-chip color-chip--limestone-50" aria-hidden="true"></span><code>#F7F6F2</code> and <span class="color-chip color-chip--ink-900" aria-hidden="true"></span><code>#14181F</code> automatically
    </div>
  </div>
</div>

### Raster Exports

High-resolution PNG exports are also generated for social previews, slides, and contexts where SVG is unsupported:

<div class="brand-preview-grid">
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__mark" src="../assets/generated/stravin-mark-dark-512.png" alt="Stravin 512px dark mark PNG">
    </div>
    <div class="brand-preview__caption">
      <strong>Mark PNG 512×512 (<code>stravin-mark-dark-512.png</code>)</strong>
      Transparent raster mark for avatars, badges, and presentations
    </div>
  </div>
  <div class="brand-preview brand-preview--dark">
    <div class="brand-preview__stage">
      <img class="brand-preview__lockup" src="../assets/generated/stravin-lockup-dark-720.png" alt="Stravin 720px dark lockup PNG">
    </div>
    <div class="brand-preview__caption">
      <strong>Lockup PNG 720px (<code>stravin-lockup-dark-720.png</code>)</strong>
      Transparent raster lockup for slides and release graphics
    </div>
  </div>
</div>

## Clear Space & Minimum Sizes

| Rule | Standalone Mark | Horizontal Lockup |
| :--- | :--- | :--- |
| **Minimum Clear Space** | `18` units (`1×` the terracotta corner square) on all four sides | `18` units (`1×` the corner square) on all four sides |
| **Minimum Digital Height** | `16px` (favored for favicons, compact rail icons, status bars) | `48px` (drop the wordmark and switch to standalone mark below `48px`) |
| **Minimum Print Height** | `8mm` | `15mm` |
| **Aspect Ratio** | Locked `1:1` (`100:100`) | Locked `18:5` (`360:100`) |

## Usage Do's & Don'ts

| Do | Don't |
| :--- | :--- |
| Use the **dark variant** on Basalt 950 (<span class="color-chip color-chip--basalt-950" aria-hidden="true"></span>`#0E1116`) or Slate 900 (<span class="color-chip color-chip--slate-900" aria-hidden="true"></span>`#161B22`) surfaces. | Do not place the dark-mode Glacier Mint (<span class="color-chip color-chip--glacier-mint" aria-hidden="true"></span>`#64C5B9`) upper bar on light backgrounds—it fails contrast. |
| Use the **light variant** on Limestone 50 (<span class="color-chip color-chip--limestone-50" aria-hidden="true"></span>`#F7F6F2`) or Limestone 100 (<span class="color-chip color-chip--limestone-100" aria-hidden="true"></span>`#EAE7DF`) surfaces. | Do not recolor the mark bars with arbitrary product accents or gradients. |
| Switch to the **standalone mark** whenever rendered height drops below `48px`. | Do not shrink the horizontal lockup below `48px` where wordmark letterforms lose clarity. |
| Preserve the `18`-unit corner anchor and exact `3:4` diagonal geometry. | Do not stretch, rotate, outline, add drop shadows, or remove the terracotta corner square. |
