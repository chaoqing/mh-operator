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

from mh_operator import legacy as _
from mh_operator.legacy.common import get_argv, get_logger, is_main

logger = get_logger()

import logging
import os
import sys

try:
    import clr

    clr.AddReference("CoreLibraryAccess")

    import _commands
    import System
    from Agilent.MassSpectrometry.DataAnalysis import MSLibraryFormat
except Exception as err:
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis import MSLibraryFormat
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.LibraryEdit import (
        Commands as _commands,
    )


def create_library(output_file):
    _commands.CreateLibrary(output_file, MSLibraryFormat.Binary)
    # _commands.ImportJCAMP(System.Array[System.String](["E:\\MassHunter\\Library\\import.jdx"]))
    _commands.NewCompound()

    _commands.CloseLibrary()


def main():
    import argparse

    argv = get_argv()
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description="Convert the MSP to .L (HP) format",
    )
    parser.add_argument("msp")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv[1:])

    if args.verbose:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logger.debug("file: {}, input: {}".format(__file__, args.msp))

    create_library(os.path.abspath(args.msp))


if is_main(__file__):
    main()
