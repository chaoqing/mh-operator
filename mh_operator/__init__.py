# type: ignore[attr-defined]
"""Awesome `mh-operator` provide interfaces and common routines for the Agilent MassHunter official SDK."""

import sys

__all__ = ["version", "get_version"]

if sys.version_info.major == 2:
    version = "unknown"
    get_version = lambda: "unknown"
else:
    from .version import get_version, version
