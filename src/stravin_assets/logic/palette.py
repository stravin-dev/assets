"""Canonical Stravin brand color tokens and product layer accents."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ColorToken:
    """Single named color token from BRANDING.md."""

    role: str
    name: str
    hex_value: str
    usage: str


@dataclass(frozen=True, slots=True)
class ProductAccent:
    """Secondary product-layer accent token from BRANDING.md."""

    layer: str
    scope: str
    accent_name: str
    hex_value: str


GLACIER_MINT = "#64C5B9"
STRATA_TEAL = "#2A9D8F"
ABYSS_TEAL = "#1C6E66"
RIVET_TERRACOTTA = "#E06D53"
LIMESTONE_50 = "#F7F6F2"
INK_900 = "#14181F"

CORE_PALETTE: tuple[ColorToken, ...] = (
    ColorToken("Dark Canvas", "Basalt 950", "#0E1116", "Default dark-mode background"),
    ColorToken("Dark Surface", "Slate 900", "#161B22", "Cards, nav rails, code blocks"),
    ColorToken("Dark Hairline", "Slate 800", "#252D38", "Borders, dividers, gridlines"),
    ColorToken("Light Canvas", "Limestone 50", LIMESTONE_50, "Light canvas, dark-mode wordmark"),
    ColorToken("Light Surface", "Limestone 100", "#EAE7DF", "Light secondary surfaces"),
    ColorToken("Light Ink", "Ink 900", INK_900, "Light typography and monochrome mark"),
    ColorToken("Isometric Top Plane", "Glacier Mint", GLACIER_MINT, "Upper bar (dark mode)"),
    ColorToken("Brand Primary (Left Plane)", "Strata Teal", STRATA_TEAL, "Lower bar (dark mode)"),
    ColorToken("Isometric Right Plane", "Abyss Teal", ABYSS_TEAL, "Lower bar (light mode)"),
    ColorToken("Focal Accent (Pin)", "Rivet Terracotta", RIVET_TERRACOTTA, "Corner pin, CTAs"),
)

PRODUCT_ACCENTS: tuple[ProductAccent, ...] = (
    ProductAccent(
        "Stravin Core",
        "stravin-edge, stravin-node, stravin-pack, stravin-ctrl",
        "Strata Teal",
        STRATA_TEAL,
    ),
    ProductAccent(
        "Stravin Review",
        "Pull requests, stacked diffs, repository browser",
        "Blueprint Blue",
        "#5B8DEF",
    ),
    ProductAccent(
        "Stravin Run",
        "Ephemeral CI runners, pipelines, sandboxes",
        "Rivet Terracotta",
        RIVET_TERRACOTTA,
    ),
    ProductAccent(
        "Stravin Index",
        "Trigram code search, symbol graph, cross-repo nav",
        "Ochre Amber",
        "#D4A34B",
    ),
    ProductAccent(
        "Stravin Gate",
        "Merge queues, branch protection, policy checks",
        "Forged Steel",
        "#7A8B99",
    ),
)
