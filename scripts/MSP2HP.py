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
    from Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands import (
        CompoundProperty,
    )

    libacc = LibraryAccess
except ImportError:
    assert sys.executable is not None, "Should never reach here"
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis import MSLibraryFormat
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.LibraryEdit import (
        Commands as _commands,
    )
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands import (
        CompoundProperty,
    )
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf import (
        ILibraryAccess,
    )

    libacc = ILibraryAccess()


def create_library(library_path):
    _commands.OpenLibrary(library_path, MSLibraryFormat.XML, True)
    # _commands.CreateLibrary(output_file, MSLibraryFormat.Binary)
    # _commands.ImportJCAMP(System.Array[System.String](["E:\\MassHunter\\Library\\import.jdx"]))
    # _commands.NewCompound(System.Array[CompoundProperty]([CompoundProperty(-1, "CompoundName", "New compond from keyin")]))
    logger.debug("#Compound = {}".format(libacc.CompoundCount))

    for c in range(libacc.CompoundCount):
        compoundId = libacc.GetCompoundId(c)
        spectrumIds = libacc.GetSpectrumIds(compoundId)
        logger.debug("Compound ID= {}".format(compoundId))
        logger.debug("Spectrum IDs= {}".format(spectrumIds))
        if spectrumIds is None:
            continue

        for spectrumId in spectrumIds:
            mz_b64 = libacc.GetSpectrumProperty(compoundId, spectrumId, "MzValues")
            abundance_b64 = libacc.GetSpectrumProperty(
                compoundId, spectrumId, "AbundanceValues"
            )

            if mz_b64 is None or abundance_b64 is None:
                continue

            mzs = libacc.Base64ToDoubleArray(mz_b64) if mz_b64 is not None else None
            abs = (
                libacc.Base64ToDoubleArray(abundance_b64)
                if abundance_b64 is not None
                else None
            )
            logger.debug("Mz = {}".format(mzs))
            logger.debug("Abundance = {}".format(abs))

    _commands.SaveLibraryAs(
        library_path.replace(".mslibrary.xml", ".L"), MSLibraryFormat.Compressed
    )

    _commands.CloseLibrary()


def main():
    import argparse

    argv = get_argv()
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description="Convert the MSP to .L (HP) format",
        epilog="Example: shebang --interpreter LEC MSP2HP.py -- 'C:\MassHunter\Library\demo.mslibrary.xml' --verbose",
    )
    parser.add_argument("library")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv[1:])

    if args.verbose:
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
    logger.debug("file: {}, input: {}".format(__file__, args.library))

    create_library(os.path.abspath(args.library))


if is_main(__file__):
    main()
