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
import shutil
import sys
import tempfile
from itertools import islice

from mh_operator.legacy.common import get_logger, global_state

logger = get_logger()

try:
    import clr

    clr.AddReference("CoreLibraryAccess")
    clr.AddReference("LibraryEdit")

    import _commands
    import System
    from Agilent.MassSpectrometry.DataAnalysis import MSLibraryFormat
    from Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands import (
        CompoundProperty,
    )

    libacc = global_state.LibraryAccess
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


def import_jcamps(jdx_paths, output_path, overwrite=False, batch_size=100):
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=True) as fp:
        temp_file = fp.name
    try:
        logger.debug("creating {}".format(temp_file))
        _commands.CreateLibrary(temp_file, MSLibraryFormat.Binary)

        it = iter(jdx_paths)
        total_batchs = len(jdx_paths) // batch_size
        for i in range(total_batchs):
            logger.debug("adding batch {}/{}".format(i, total_batchs))
            _commands.ImportJCAMP(
                System.Array[System.String](list(islice(it, batch_size)))
            )
            # _commands.NewCompound(System.Array[CompoundProperty]([CompoundProperty(-1, "CompoundName", "New compond from keyin")]))
        last_batch = list(islice(it, batch_size))
        if last_batch:
            logger.debug("adding rest {} jdx".format(len(last_batch)))
            _commands.ImportJCAMP(System.Array[System.String](last_batch))

        logger.info("Total {} Compounds added".format(libacc.CompoundCount))

        if overwrite:
            shutil.rmtree(output_path, ignore_errors=True)

        _commands.SaveLibraryAs(output_path, MSLibraryFormat.Compressed)
        _commands.CloseLibrary()
    finally:
        os.unlink(temp_file)


def compress_mslibrary(library_path, output_path=None):
    assert library_path.endswith(".mslibrary.xml")

    _commands.OpenLibrary(library_path, MSLibraryFormat.XML, True)
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

    if output_path is None:
        output_path = library_path.replace(".mslibrary.xml", ".L")
    else:
        assert output_path.endswith(".L")

    _commands.SaveLibraryAs(output_path, MSLibraryFormat.Compressed)

    _commands.CloseLibrary()
