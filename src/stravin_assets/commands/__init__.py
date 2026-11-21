"""Dynamic command and command-group discovery for the stravin-assets CLI."""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from types import ModuleType

import cyclopts


def _command_name(module_name: str) -> str:
    return module_name.replace("_", "-")


def register_commands(app: cyclopts.App, package: ModuleType | None = None) -> cyclopts.App:
    """Discover command modules and subpackage command groups and register them on `app`."""
    target_pkg = package if package is not None else importlib.import_module(__name__)
    pkg_path = getattr(target_pkg, "__path__", None)
    if pkg_path is None:
        raise ValueError(f"{target_pkg.__name__!r} is not a package")

    for module_info in sorted(pkgutil.iter_modules(pkg_path), key=lambda m: m.name):
        if module_info.name.startswith("_"):
            continue

        full_name = f"{target_pkg.__name__}.{module_info.name}"
        imported = importlib.import_module(full_name)
        cmd_name = _command_name(module_info.name)

        if module_info.ispkg:
            sub_help = (inspect.getdoc(imported) or "").splitlines()[0] if imported.__doc__ else ""
            sub_app = cyclopts.App(name=cmd_name, help=sub_help)
            register_commands(sub_app, imported)
            app.command(sub_app)
            continue

        handler = getattr(imported, "default", None)
        if handler is None or not inspect.iscoroutinefunction(handler):
            raise TypeError(
                f"Command module {full_name!r} must define an async 'default' handler function"
            )
        app.command(handler, name=cmd_name)

    return app
