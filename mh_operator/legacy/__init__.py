# -*- coding: utf-8 -*-

__all__ = ["pathsep"]

import sys

try:
    from os import pathsep
except ImportError:
    # We must be inside Non-standard IronPython2.7 environment where even standard module do not exist
    from System import IO, Environment

    pathsep = (
        ";" if str(Environment.OSVersion.Platform).lower().startswith("win") else ":"
    )

    try:
        python_path = (Environment.GetEnvironmentVariable("PYTHONPATH") or "").split(
            pathsep
        )
        default_python_path = [
            r"C:\Program Files (x86)\IronPython 2.7\Lib",
        ]

        std_lib_path = next(
            p
            for p in python_path + default_python_path
            if p != "" and IO.File.Exists(IO.Path.Combine(p, "__future__.py"))
        )
        sys.path.append(std_lib_path)

        # Incase the PYTHONPATH is not respected by .NET IronPython2
        from collections import OrderedDict

        sys.path = [
            p for p in OrderedDict.fromkeys(sys.path[:-1] + python_path) if p != ""
        ]

        if std_lib_path not in sys.path:
            sys.path.append(std_lib_path)
    except StopIteration:
        raise SystemError(
            "can not find python 2.7 standard lib, please set PYTHONPATH envrionment"
        )
    except (ImportError, SyntaxError):
        raise SystemError(
            "'{}' must be the wrong Python 2.7.5 standard lib path".format(std_lib_path)
        )

from os import environ

command_str = environ.pop("MH_CONSOLE_COMMAND_STRING", "")
if command_str != "" and __name__ not in ("mh_operator.legacy", "mh_operator_legacy"):
    try:
        exec(command_str)  # nosec
    except:
        import traceback

        traceback.print_exc()
