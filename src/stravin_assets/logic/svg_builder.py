"""Deterministic canonical SVG generation and XML safety validation."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Literal

SVG_NS = "http://www.w3.org/2000/svg"
UPPER_BAR_PATH = "M 67 6 H 32 L 8 24 V 45 L 40 69 H 60 L 65 65.25 L 24 34.5 L 38 24 H 67 Z"
LOWER_BAR_PATH = "M 40 31 H 60 L 92 55 V 76 L 68 94 H 8 V 76 H 62 L 76 65.5 L 35 34.75 Z"
WORDMARK_FONT_FAMILY = "'Space Grotesk', 'Plus Jakarta Sans', system-ui, sans-serif"


@dataclass(frozen=True, slots=True)
class SvgSpec:
    """Declarative specification for one canonical Stravin SVG asset."""

    filename: str
    kind: Literal["mark", "lockup"]
    upper_fill: str
    lower_fill: str
    pin_fill: str
    pin_opacity: str | None = None
    wordmark_fill: str | None = None
    description: str = ""


def _render_mark_elements(spec: SvgSpec, indent: str) -> list[str]:
    pin_opacity_attr = f' opacity="{spec.pin_opacity}"' if spec.pin_opacity is not None else ""
    return [
        f'{indent}<path d="{UPPER_BAR_PATH}" fill="{spec.upper_fill}" />',
        f'{indent}<path d="{LOWER_BAR_PATH}" fill="{spec.lower_fill}" />',
        f'{indent}<rect x="74" y="6" width="18" height="18" fill="{spec.pin_fill}"'
        f"{pin_opacity_attr} />",
    ]


def build_svg(spec: SvgSpec) -> str:
    """Build deterministic canonical SVG markup for the given specification."""
    if spec.kind == "mark":
        lines = [
            f'<svg xmlns="{SVG_NS}" viewBox="0 0 100 100" role="img" aria-label="Stravin">',
            *_render_mark_elements(spec, indent="  "),
            "</svg>",
        ]
    elif spec.kind == "lockup":
        if not spec.wordmark_fill:
            raise ValueError(f"Lockup spec {spec.filename!r} requires wordmark_fill")
        lines = [
            f'<svg xmlns="{SVG_NS}" viewBox="0 0 360 100" role="img" aria-label="Stravin">',
            "  <g>",
            *_render_mark_elements(spec, indent="    "),
            "  </g>",
            f'  <text x="116" y="66" fill="{spec.wordmark_fill}" '
            f'font-family="{WORDMARK_FONT_FAMILY}" font-size="48" '
            f'font-weight="600" letter-spacing="0.16em">STRAVIN</text>',
            "</svg>",
        ]
    else:
        raise ValueError(f"Unsupported SVG kind: {spec.kind!r}")

    svg_text = "\n".join(lines) + "\n"
    validate_svg_xml(svg_text)
    return svg_text


def validate_svg_xml(svg_text: str) -> None:
    """Validate that SVG markup is well-formed XML with no scripts or event handlers."""
    upper_text = svg_text.upper()
    if "<!DOCTYPE" in upper_text or "<!ENTITY" in upper_text:
        raise ValueError("SVG must not contain DOCTYPE or ENTITY declarations")

    try:
        root = ET.fromstring(svg_text)  # noqa: S314
    except ET.ParseError as exc:
        raise ValueError(f"Invalid SVG XML: {exc}") from exc

    root_tag = root.tag.rsplit("}", 1)[-1].lower()
    if root_tag != "svg":
        raise ValueError(f"Expected <svg> root element, got <{root_tag}>")

    for element in root.iter():
        local_tag = element.tag.rsplit("}", 1)[-1].lower()
        if local_tag == "script":
            raise ValueError("SVG must not contain <script> elements")
        for attr_name in element.attrib:
            local_attr = attr_name.rsplit("}", 1)[-1].lower()
            if local_attr.startswith("on"):
                raise ValueError(f"SVG must not contain event handler attribute {attr_name!r}")
