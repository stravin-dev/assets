"""Safe filesystem path resolution and file writing with traversal protection."""

from __future__ import annotations

import shutil
from pathlib import Path


class UnsafePathError(ValueError):
    """Raised when a relative target path attempts to escape its base directory."""


def resolve_safe_path(base_dir: Path, relative_path: str | Path) -> Path:
    """Resolve `relative_path` under `base_dir`, rejecting traversal or symlink escapes."""
    raw = str(relative_path)
    if "\x00" in raw:
        raise UnsafePathError(f"Path contains NUL byte: {raw!r}")

    rel = Path(relative_path)
    if rel.is_absolute():
        raise UnsafePathError(f"Absolute path is not allowed: {raw!r}")
    if ".." in rel.parts:
        raise UnsafePathError(f"Parent traversal is not allowed: {raw!r}")

    resolved_base = base_dir.resolve()
    candidate = (resolved_base / rel).resolve()
    try:
        candidate.relative_to(resolved_base)
    except ValueError as exc:
        raise UnsafePathError(f"Path {raw!r} escapes base directory {resolved_base}") from exc
    return candidate


def write_text_safe(base_dir: Path, relative_path: str | Path, content: str) -> Path:
    """Write UTF-8 text to a validated path under `base_dir`."""
    dest = resolve_safe_path(base_dir, relative_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
    return dest


def write_bytes_safe(base_dir: Path, relative_path: str | Path, data: bytes) -> Path:
    """Write raw bytes to a validated path under `base_dir`."""
    dest = resolve_safe_path(base_dir, relative_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return dest


def copy_file_safe(
    src_base: Path, src_rel: str | Path, dst_base: Path, dst_rel: str | Path
) -> Path:
    """Copy a validated source file to a validated destination path."""
    src = resolve_safe_path(src_base, src_rel)
    dst = resolve_safe_path(dst_base, dst_rel)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return dst
