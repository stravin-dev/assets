"""Tests for safe filesystem path resolution and writes."""

from __future__ import annotations

from pathlib import Path

import pytest

from stravin_assets.providers.filesystem import UnsafePathError, resolve_safe_path, write_bytes_safe


def test_resolve_safe_path_allows_nested_relative_path(tmp_path: Path) -> None:
    resolved = resolve_safe_path(tmp_path, Path("svg/stravin-mark-dark.svg"))
    assert resolved == (tmp_path / "svg" / "stravin-mark-dark.svg").resolve()


@pytest.mark.parametrize(
    "unsafe_rel",
    [
        "../outside.svg",
        "svg/../../outside.svg",
        "/etc/passwd",
        "bad\x00name.svg",
    ],
)
def test_resolve_safe_path_rejects_traversal_and_absolute_paths(
    tmp_path: Path, unsafe_rel: str
) -> None:
    with pytest.raises(UnsafePathError):
        resolve_safe_path(tmp_path, unsafe_rel)


def test_resolve_safe_path_rejects_symlink_escape(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside_target"
    outside.mkdir(exist_ok=True)
    link_dir = tmp_path / "escape_link"
    link_dir.symlink_to(outside)

    with pytest.raises(UnsafePathError):
        resolve_safe_path(tmp_path, Path("escape_link/pwn.txt"))


def test_write_bytes_safe_creates_parents_and_writes_payload(tmp_path: Path) -> None:
    dest = write_bytes_safe(tmp_path, Path("nested/file.bin"), b"hello")
    assert dest.read_bytes() == b"hello"
