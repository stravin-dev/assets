"""Tests for canonical Stravin SVG builders and XML safety validation."""

from __future__ import annotations

import xml.etree.ElementTree as ET

import pytest

from stravin_assets.logic.manifest import SVG_SPECS
from stravin_assets.logic.svg_builder import build_svg, validate_svg_xml

EXPECTED_SVG_NAMES = {
    "stravin-mark-dark.svg",
    "stravin-mark-light.svg",
    "stravin-mark-mono.svg",
    "stravin-mark-mono-1c.svg",
    "stravin-lockup-dark.svg",
    "stravin-lockup-light.svg",
    "stravin-lockup-currentcolor.svg",
    "favicon.svg",
}


def test_svg_specs_cover_all_canonical_variants() -> None:
    assert {spec.filename for spec in SVG_SPECS} == EXPECTED_SVG_NAMES


def test_all_svgs_are_deterministic_and_valid_xml() -> None:
    for spec in SVG_SPECS:
        first = build_svg(spec)
        second = build_svg(spec)
        assert first == second
        validate_svg_xml(first)

        root = ET.fromstring(first)  # noqa: S314
        assert root.tag.endswith("svg")
        for elem in root.iter():
            local_tag = elem.tag.rsplit("}", 1)[-1].lower()
            assert local_tag != "script"
            for attr in elem.attrib:
                assert not attr.lower().startswith("on")


def test_mark_variants_use_exact_branding_colors() -> None:
    by_name = {spec.filename: build_svg(spec) for spec in SVG_SPECS}

    assert 'fill="#64C5B9"' in by_name["stravin-mark-dark.svg"]
    assert 'fill="#2A9D8F"' in by_name["stravin-mark-dark.svg"]
    assert 'fill="#E06D53"' in by_name["stravin-mark-dark.svg"]

    assert 'fill="#2A9D8F"' in by_name["stravin-mark-light.svg"]
    assert 'fill="#1C6E66"' in by_name["stravin-mark-light.svg"]
    assert 'fill="#E06D53"' in by_name["stravin-mark-light.svg"]

    assert by_name["stravin-mark-mono.svg"].count('fill="currentColor"') == 2
    assert 'fill="#E06D53"' in by_name["stravin-mark-mono.svg"]

    assert by_name["stravin-mark-mono-1c.svg"].count('fill="currentColor"') == 3
    assert 'opacity="0.55"' in by_name["stravin-mark-mono-1c.svg"]

    assert by_name["favicon.svg"] == by_name["stravin-mark-dark.svg"]


def test_lockup_variants_use_explicit_and_currentcolor_fills() -> None:
    by_name = {spec.filename: build_svg(spec) for spec in SVG_SPECS}

    assert 'viewBox="0 0 360 100"' in by_name["stravin-lockup-dark.svg"]
    assert 'fill="#F7F6F2"' in by_name["stravin-lockup-dark.svg"]
    assert "STRAVIN</text>" in by_name["stravin-lockup-dark.svg"]

    assert 'viewBox="0 0 360 100"' in by_name["stravin-lockup-light.svg"]
    assert 'fill="#14181F"' in by_name["stravin-lockup-light.svg"]
    assert 'fill="#1C6E66"' in by_name["stravin-lockup-light.svg"]

    assert 'fill="currentColor"' in by_name["stravin-lockup-currentcolor.svg"]


def test_validate_svg_xml_rejects_script_and_event_handlers() -> None:
    with pytest.raises(ValueError, match="script"):
        validate_svg_xml('<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>')

    with pytest.raises(ValueError, match="event handler"):
        validate_svg_xml('<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"></svg>')
