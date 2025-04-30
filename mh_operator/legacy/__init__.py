# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    generators,
    nested_scopes,
    print_function,
    unicode_literals,
    with_statement,
)

try:
    from os import pathsep
except ImportError:
    # We must be inside Non-standard IronPython2.7 environment where even standard module do not exist
    import sys
    from collections import OrderedDict

    from System import Environment

    pathsep = (
        ";" if str(Environment.OSVersion.Platform).lower().startswith("win") else ":"
    )
    # Incase the PYTHONPATH is not respected by .NET IronPython2
    sys.path = [
        p
        for p in OrderedDict.fromkeys(
            sys.path + Environment.GetEnvironmentVariable("PYTHONPATH").split(pathsep)
        )
        if p != ""
    ]
