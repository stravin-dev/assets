"""List all canonical SVG targets, derived raster targets, and palette tokens."""

from __future__ import annotations

from stravin_assets.logic.manifest import (
    DOCS_SYNC_TARGETS,
    ICO_TARGETS,
    PNG_TARGETS,
    SVG_SPECS,
    WEBP_TARGETS,
)
from stravin_assets.logic.palette import CORE_PALETTE, PRODUCT_ACCENTS


async def default() -> None:
    """Print all defined SVG targets, secondary raster targets, and brand palette tokens."""
    print("Canonical SVGs (Stage 1):")
    for spec in SVG_SPECS:
        print(f"  svg/{spec.filename}  [{spec.kind}]  {spec.description}")

    print("\nPNG Targets (Stage 2):")
    for target in PNG_TARGETS:
        print(
            f"  png/{target.filename}  ({target.width}x{target.height} <- svg/{target.source_svg})"
        )

    print("\nICO Targets (Stage 2):")
    for target in ICO_TARGETS:
        sizes_str = ",".join(str(s) for s in target.sizes)
        print(f"  ico/{target.filename}  (sizes={sizes_str} <- svg/{target.source_svg})")

    print("\nWebP Targets (Stage 2):")
    for target in WEBP_TARGETS:
        print(
            f"  webp/{target.filename}  ({target.width}x{target.height} <- svg/{target.source_svg})"
        )

    print("\nDocs Sync Targets (Stage 3):")
    for src_rel, dst_name in DOCS_SYNC_TARGETS:
        print(f"  {src_rel} -> {dst_name}")

    print("\nCore Color Palette:")
    for token in CORE_PALETTE:
        print(f"  {token.name:<16} {token.hex_value}  ({token.role})")

    print("\nProduct Layer Accents:")
    for accent in PRODUCT_ACCENTS:
        print(f"  {accent.layer:<16} {accent.hex_value}  ({accent.accent_name})")
