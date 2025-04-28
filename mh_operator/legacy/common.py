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

import os
import sys

# sys.path.extend(os.getenv("PYTHONPATH", "").split(os.pathsep))


def get_version():
    return "{}.{}.{}".format(
        sys.version_info.major, sys.version_info.minor, sys.version_info.micro
    )


def get_args():
    prefix = "MH_CONSOLE_ARGS_"
    return [
        v
        for _, v in sorted(
            (int(k[len(prefix) :]), v)
            for k, v in os.environ.items()
            if k.startswith(prefix)
        )
    ]
