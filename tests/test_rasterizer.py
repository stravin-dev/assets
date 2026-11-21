"""Tests for resvg-py + Pillow SVG-to-raster conversion."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from stravin_assets.logic.manifest import SVG_SPECS_BY_NAME
from stravin_assets.logic.svg_builder import build_svg
from stravin_assets.providers.rasterizer import (
    render_ico_from_svg,
    render_png_from_svg,
    render_webp_from_svg,
)


def test_render_mark_png_ico_and_webp(tmp_path: Path) -> None:
    svg_path = tmp_path / "stravin-mark-dark.svg"
    svg_path.write_text(build_svg(SVG_SPECS_BY_NAME["stravin-mark-dark.svg"]), encoding="utf-8")

    png_path = tmp_path / "mark-256.png"
    render_png_from_svg(svg_path, png_path, width=256, height=256)
    with Image.open(png_path) as img:
        assert img.format == "PNG"
        assert img.mode == "RGBA"
        assert img.size == (256, 256)

    ico_path = tmp_path / "favicon.ico"
    render_ico_from_svg(svg_path, ico_path, sizes=(16, 32, 48))
    with Image.open(ico_path) as ico:
        assert ico.format == "ICO"
        ico_sizes = set(ico.info.get("sizes", set()))
        assert ico_sizes == {(16, 16), (32, 32), (48, 48)}

    webp_path = tmp_path / "mark-256.webp"
    render_webp_from_svg(svg_path, webp_path, width=256, height=256)
    with Image.open(webp_path) as webp:
        assert webp.format == "WEBP"
        assert webp.size == (256, 256)


def test_render_lockup_png_has_non_blank_wordmark_pixels(tmp_path: Path) -> None:
    for name in ("stravin-lockup-dark.svg", "stravin-lockup-light.svg"):
        svg_path = tmp_path / name
        svg_path.write_text(build_svg(SVG_SPECS_BY_NAME[name]), encoding="utf-8")

        png_path = tmp_path / f"{name}.png"
        render_png_from_svg(svg_path, png_path, width=720, height=200)
        with Image.open(png_path) as img:
            assert img.mode == "RGBA"
            assert img.size == (720, 200)
            # Wordmark starts at x=116 in 360-wide viewBox -> x=232 in 720-wide render.
            wordmark_crop = img.crop((232, 0, 720, 200))
            alpha_bytes = wordmark_crop.getchannel("A").tobytes()
            opaque_pixels = sum(1 for a in alpha_bytes if a > 0)
            assert opaque_pixels > 500, f"Expected rendered text pixels in {name}"
