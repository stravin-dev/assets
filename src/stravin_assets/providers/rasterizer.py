"""SVG-to-raster conversion provider backed by resvg-py and Pillow."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

import resvg_py
from PIL import Image


def _render_rgba_image(svg_path: Path, width: int, height: int) -> Image.Image:
    png_bytes = resvg_py.svg_to_bytes(svg_path=str(svg_path), width=width, height=height)
    with Image.open(BytesIO(png_bytes)) as img:
        return img.convert("RGBA")


def render_png_from_svg(svg_path: Path, output_path: Path, width: int, height: int) -> Path:
    """Rasterize an SVG file to an exact-size RGBA PNG."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image = _render_rgba_image(svg_path, width=width, height=height)
    image.save(output_path, format="PNG")
    return output_path


def render_ico_from_svg(
    svg_path: Path, output_path: Path, sizes: tuple[int, ...] = (16, 32, 48)
) -> Path:
    """Rasterize an SVG file to a multi-size ICO containing crisp frames for each size."""
    if not sizes:
        raise ValueError("ICO sizes must not be empty")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ordered_sizes = tuple(sorted(set(sizes), reverse=True))
    frames = [_render_rgba_image(svg_path, width=size, height=size) for size in ordered_sizes]
    frames[0].save(
        output_path,
        format="ICO",
        sizes=[(size, size) for size in ordered_sizes],
        append_images=frames[1:],
    )
    return output_path


def render_webp_from_svg(svg_path: Path, output_path: Path, width: int, height: int) -> Path:
    """Rasterize an SVG file to an exact-size lossless RGBA WebP."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image = _render_rgba_image(svg_path, width=width, height=height)
    image.save(output_path, format="WEBP", lossless=True)
    return output_path
