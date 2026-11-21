"""Build canonical Stravin SVGs, derived raster assets, and docs-ready copies."""

from __future__ import annotations

from pathlib import Path

import anyio

from stravin_assets.logic.manifest import (
    DOCS_SYNC_TARGETS,
    ICO_TARGETS,
    PNG_TARGETS,
    SVG_SPECS,
    WEBP_TARGETS,
)
from stravin_assets.logic.svg_builder import build_svg
from stravin_assets.providers.filesystem import copy_file_safe, resolve_safe_path, write_text_safe
from stravin_assets.providers.rasterizer import (
    render_ico_from_svg,
    render_png_from_svg,
    render_webp_from_svg,
)


def _generate_canonical_svgs(out_dir: Path) -> dict[str, Path]:
    svg_paths: dict[str, Path] = {}
    for spec in SVG_SPECS:
        markup = build_svg(spec)
        svg_paths[spec.filename] = write_text_safe(out_dir, Path("svg") / spec.filename, markup)
    return svg_paths


async def _generate_raster_assets(out_dir: Path, svg_paths: dict[str, Path]) -> int:
    generated_count = 0

    async def _run_png(source_svg: Path, dest: Path, width: int, height: int) -> None:
        nonlocal generated_count
        await anyio.to_thread.run_sync(render_png_from_svg, source_svg, dest, width, height)
        generated_count += 1

    async def _run_ico(source_svg: Path, dest: Path, sizes: tuple[int, ...]) -> None:
        nonlocal generated_count
        await anyio.to_thread.run_sync(render_ico_from_svg, source_svg, dest, sizes)
        generated_count += 1

    async def _run_webp(source_svg: Path, dest: Path, width: int, height: int) -> None:
        nonlocal generated_count
        await anyio.to_thread.run_sync(render_webp_from_svg, source_svg, dest, width, height)
        generated_count += 1

    async with anyio.create_task_group() as tg:
        for target in PNG_TARGETS:
            dest = resolve_safe_path(out_dir, Path("png") / target.filename)
            tg.start_soon(_run_png, svg_paths[target.source_svg], dest, target.width, target.height)
        for target in ICO_TARGETS:
            dest = resolve_safe_path(out_dir, Path("ico") / target.filename)
            tg.start_soon(_run_ico, svg_paths[target.source_svg], dest, target.sizes)
        for target in WEBP_TARGETS:
            dest = resolve_safe_path(out_dir, Path("webp") / target.filename)
            tg.start_soon(
                _run_webp, svg_paths[target.source_svg], dest, target.width, target.height
            )

    return generated_count


def _sync_docs_assets(out_dir: Path, docs_dir: Path) -> int:
    for src_rel, dst_name in DOCS_SYNC_TARGETS:
        copy_file_safe(out_dir, src_rel, docs_dir, dst_name)
    return len(DOCS_SYNC_TARGETS)


async def default(
    *,
    out_dir: Path = Path("dist"),
    docs_dir: str | None = "docs/assets/generated",
) -> None:
    """Generate canonical SVGs, derived PNG/ICO/WebP rasters, and optional docs copies.

    Parameters
    ----------
    out_dir:
        Output root directory for generated svg/, png/, ico/, and webp/ assets.
    docs_dir:
        Optional documentation asset directory to sync web-ready copies into.
        Pass an empty string to skip Stage 3 docs sync.
    """
    svg_paths = _generate_canonical_svgs(out_dir)
    raster_count = await _generate_raster_assets(out_dir, svg_paths)

    resolved_docs_dir = Path(docs_dir) if docs_dir and docs_dir.strip() else None
    synced_count = _sync_docs_assets(out_dir, resolved_docs_dir) if resolved_docs_dir else 0

    print(
        f"Built {len(svg_paths)} SVGs, {raster_count} rasters in {out_dir}"
        + (f", synced {synced_count} files to {resolved_docs_dir}" if resolved_docs_dir else "")
    )
