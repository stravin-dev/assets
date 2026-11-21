"""Canonical asset manifest defining Stage 1 SVGs, Stage 2 rasters, and Stage 3 docs sync."""

from __future__ import annotations

from dataclasses import dataclass

from stravin_assets.logic.palette import (
    ABYSS_TEAL,
    GLACIER_MINT,
    INK_900,
    LIMESTONE_50,
    RIVET_TERRACOTTA,
    STRATA_TEAL,
)
from stravin_assets.logic.svg_builder import SvgSpec


@dataclass(frozen=True, slots=True)
class RasterTarget:
    """Single raster image derived from a Stage 1 canonical SVG."""

    filename: str
    source_svg: str
    width: int
    height: int


@dataclass(frozen=True, slots=True)
class IcoTarget:
    """Multi-size ICO asset derived from a Stage 1 canonical SVG."""

    filename: str
    source_svg: str
    sizes: tuple[int, ...]


SVG_SPECS: tuple[SvgSpec, ...] = (
    SvgSpec(
        filename="stravin-mark-dark.svg",
        kind="mark",
        upper_fill=GLACIER_MINT,
        lower_fill=STRATA_TEAL,
        pin_fill=RIVET_TERRACOTTA,
        description="Standalone mark for dark surfaces",
    ),
    SvgSpec(
        filename="stravin-mark-light.svg",
        kind="mark",
        upper_fill=STRATA_TEAL,
        lower_fill=ABYSS_TEAL,
        pin_fill=RIVET_TERRACOTTA,
        description="Standalone mark for light surfaces (WCAG AA)",
    ),
    SvgSpec(
        filename="stravin-mark-mono.svg",
        kind="mark",
        upper_fill="currentColor",
        lower_fill="currentColor",
        pin_fill=RIVET_TERRACOTTA,
        description="Monochrome mark with terracotta pin",
    ),
    SvgSpec(
        filename="stravin-mark-mono-1c.svg",
        kind="mark",
        upper_fill="currentColor",
        lower_fill="currentColor",
        pin_fill="currentColor",
        pin_opacity="0.55",
        description="Strict 1-color monochrome mark",
    ),
    SvgSpec(
        filename="stravin-lockup-dark.svg",
        kind="lockup",
        upper_fill=GLACIER_MINT,
        lower_fill=STRATA_TEAL,
        pin_fill=RIVET_TERRACOTTA,
        wordmark_fill=LIMESTONE_50,
        description="Horizontal lockup with explicit light wordmark for dark surfaces",
    ),
    SvgSpec(
        filename="stravin-lockup-light.svg",
        kind="lockup",
        upper_fill=STRATA_TEAL,
        lower_fill=ABYSS_TEAL,
        pin_fill=RIVET_TERRACOTTA,
        wordmark_fill=INK_900,
        description="Horizontal lockup with explicit dark wordmark for light surfaces",
    ),
    SvgSpec(
        filename="stravin-lockup-currentcolor.svg",
        kind="lockup",
        upper_fill=GLACIER_MINT,
        lower_fill=STRATA_TEAL,
        pin_fill=RIVET_TERRACOTTA,
        wordmark_fill="currentColor",
        description="Horizontal lockup with currentColor wordmark for inline web",
    ),
    SvgSpec(
        filename="favicon.svg",
        kind="mark",
        upper_fill=GLACIER_MINT,
        lower_fill=STRATA_TEAL,
        pin_fill=RIVET_TERRACOTTA,
        description="Canonical SVG favicon (standalone dark mark)",
    ),
)

SVG_SPECS_BY_NAME: dict[str, SvgSpec] = {spec.filename: spec for spec in SVG_SPECS}

MARK_PNG_SIZES: tuple[int, ...] = (16, 32, 64, 128, 180, 192, 256, 512, 1024)
LOCKUP_PNG_WIDTHS: tuple[int, ...] = (360, 720, 1440)


def _build_png_targets() -> tuple[RasterTarget, ...]:
    targets: list[RasterTarget] = []
    for theme in ("dark", "light"):
        src = f"stravin-mark-{theme}.svg"
        for size in MARK_PNG_SIZES:
            targets.append(RasterTarget(f"stravin-mark-{theme}-{size}.png", src, size, size))
    for theme in ("dark", "light"):
        src = f"stravin-lockup-{theme}.svg"
        for width in LOCKUP_PNG_WIDTHS:
            height = (width * 100) // 360
            targets.append(RasterTarget(f"stravin-lockup-{theme}-{width}.png", src, width, height))
    targets.append(RasterTarget("apple-touch-icon.png", "stravin-mark-dark.svg", 180, 180))
    return tuple(targets)


PNG_TARGETS: tuple[RasterTarget, ...] = _build_png_targets()

ICO_TARGETS: tuple[IcoTarget, ...] = (
    IcoTarget("favicon.ico", "stravin-mark-dark.svg", (16, 32, 48)),
)

WEBP_TARGETS: tuple[RasterTarget, ...] = (
    RasterTarget("stravin-mark-dark-256.webp", "stravin-mark-dark.svg", 256, 256),
    RasterTarget("stravin-mark-dark-512.webp", "stravin-mark-dark.svg", 512, 512),
    RasterTarget("stravin-mark-light-256.webp", "stravin-mark-light.svg", 256, 256),
    RasterTarget("stravin-mark-light-512.webp", "stravin-mark-light.svg", 512, 512),
    RasterTarget("stravin-lockup-dark-720.webp", "stravin-lockup-dark.svg", 720, 200),
    RasterTarget("stravin-lockup-light-720.webp", "stravin-lockup-light.svg", 720, 200),
)

DOCS_SYNC_TARGETS: tuple[tuple[str, str], ...] = (
    ("svg/stravin-mark-dark.svg", "stravin-mark-dark.svg"),
    ("svg/stravin-mark-light.svg", "stravin-mark-light.svg"),
    ("svg/stravin-mark-mono.svg", "stravin-mark-mono.svg"),
    ("svg/stravin-mark-mono-1c.svg", "stravin-mark-mono-1c.svg"),
    ("svg/stravin-lockup-dark.svg", "stravin-lockup-dark.svg"),
    ("svg/stravin-lockup-light.svg", "stravin-lockup-light.svg"),
    ("svg/stravin-lockup-currentcolor.svg", "stravin-lockup-currentcolor.svg"),
    ("svg/favicon.svg", "favicon.svg"),
    ("ico/favicon.ico", "favicon.ico"),
    ("png/apple-touch-icon.png", "apple-touch-icon.png"),
    ("png/stravin-mark-dark-512.png", "stravin-mark-dark-512.png"),
    ("png/stravin-lockup-dark-720.png", "stravin-lockup-dark-720.png"),
)
