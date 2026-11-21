"""Tests for dynamic CLI command discovery and end-to-end build/list commands."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from stravin_assets.cli import create_app
from stravin_assets.logic.manifest import (
    DOCS_SYNC_TARGETS,
    ICO_TARGETS,
    PNG_TARGETS,
    SVG_SPECS,
    WEBP_TARGETS,
)


def test_dynamic_command_discovery_registers_build_and_list() -> None:
    app = create_app()
    assert "build" in app
    assert "list" in app


def test_list_command_prints_targets_and_palette(capsys) -> None:
    app = create_app()
    app(["list"], exit_on_error=False, result_action="return_value")
    output = capsys.readouterr().out
    assert "stravin-mark-dark.svg" in output
    assert "favicon.ico" in output
    assert "apple-touch-icon.png" in output
    assert "#2A9D8F" in output
    assert "Strata Teal" in output


def test_build_command_generates_all_stages_and_docs_sync(tmp_path: Path) -> None:
    out_dir = tmp_path / "dist"
    docs_dir = tmp_path / "docs" / "assets" / "generated"

    app = create_app()
    app(
        ["build", "--out-dir", str(out_dir), "--docs-dir", str(docs_dir)],
        exit_on_error=False,
        result_action="return_value",
    )

    for spec in SVG_SPECS:
        assert (out_dir / "svg" / spec.filename).is_file()

    for target in PNG_TARGETS:
        png_file = out_dir / "png" / target.filename
        assert png_file.is_file()
        with Image.open(png_file) as img:
            assert img.size == (target.width, target.height)
            assert img.mode == "RGBA"

    for target in ICO_TARGETS:
        ico_file = out_dir / "ico" / target.filename
        assert ico_file.is_file()
        with Image.open(ico_file) as ico:
            assert set(ico.info.get("sizes", set())) == {(16, 16), (32, 32), (48, 48)}

    for target in WEBP_TARGETS:
        webp_file = out_dir / "webp" / target.filename
        assert webp_file.is_file()
        with Image.open(webp_file) as webp:
            assert webp.size == (target.width, target.height)

    for rel_src, dst_name in DOCS_SYNC_TARGETS:
        synced = docs_dir / dst_name
        assert synced.is_file()
        assert synced.read_bytes() == (out_dir / rel_src).read_bytes()


def test_build_command_skips_docs_sync_when_disabled(tmp_path: Path) -> None:
    out_dir = tmp_path / "dist"
    app = create_app()
    app(
        ["build", "--out-dir", str(out_dir), "--docs-dir", ""],
        exit_on_error=False,
        result_action="return_value",
    )
    assert (out_dir / "ico" / "favicon.ico").is_file()
    assert not (tmp_path / "docs").exists()


def test_dynamic_command_discovery_registers_subpackage_groups(tmp_path: Path, monkeypatch) -> None:
    import importlib

    import cyclopts

    from stravin_assets.commands import register_commands

    pkg_root = tmp_path / "fake_cmds"
    sub_pkg = pkg_root / "export_tools"
    sub_pkg.mkdir(parents=True)
    (pkg_root / "__init__.py").write_text("", encoding="utf-8")
    (sub_pkg / "__init__.py").write_text('"""Export tools group."""\n', encoding="utf-8")
    (sub_pkg / "ping_test.py").write_text(
        "async def default() -> str:\n    return 'pong'\n", encoding="utf-8"
    )

    monkeypatch.syspath_prepend(str(tmp_path))
    importlib.invalidate_caches()
    fake_pkg = importlib.import_module("fake_cmds")

    app = register_commands(cyclopts.App(name="test"), fake_pkg)
    assert "export-tools" in app
    result = app(["export-tools", "ping-test"], exit_on_error=False, result_action="return_value")
    assert result == "pong"
