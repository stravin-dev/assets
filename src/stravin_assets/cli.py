"""CLI entry point for stravin-assets."""

from __future__ import annotations

import cyclopts

from stravin_assets.commands import register_commands


def create_app() -> cyclopts.App:
    """Create and configure the root stravin-assets CLI application."""
    app = cyclopts.App(
        name="stravin-assets",
        help="Deterministic SVG-first brand asset generator for Stravin.",
    )
    return register_commands(app)


def main() -> None:
    """Run the stravin-assets CLI."""
    create_app()()
