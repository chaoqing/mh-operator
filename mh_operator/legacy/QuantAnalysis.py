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

import sys

from mh_operator.legacy.common import global_state, logger

try:
    import clr

    clr.AddReference("QuantDataAccess")
    clr.AddReference("TofFeatureDataAccess")
    from Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess import (
        DefaultNumericFormat,
    )
    from Agilent.MassSpectrometry.DataAnalysis.Quantitative import QuantDataAccess

except ImportError as e:
    logger.warning("Import error {}".format(e))
    assert sys.executable is not None, "Should never reach here"
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis import IAcqMetaData
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess import (
        DefaultNumericFormat,
    )
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.Quantitative import (
        QuantDataAccess,
    )


def export_sample(test_dir):
    try:
        qdacc = QuantDataAccess(DefaultNumericFormat())
        logger.info("opening {} for reading data".format(test_dir))
        qdacc.OpenDataFile(test_dir)
        assert qdacc.IsFileOpen()

        scan_data = qdacc.ScanData

        # meta_data = qdacc.AcquisitionMetaData # IAcqMetaData
        # assert scan_data.ScanRecordCount == meta_data.Count

        assert (
            not qdacc.ScanData.HasProfileData and qdacc.ScanData.HasCentroidData
        )  # We currently only support centroid spectrum

        records = []
        logger.info("Got {} records inside".format(scan_data.ScanRecordCount, test_dir))
        for i in range(scan_data.ScanRecordCount):
            record = scan_data[i]
            spectrum_data = record.SpectrumData

            spectrum_mz = []
            spectrum_abundance = []
            for j, abundance in enumerate(spectrum_data):
                spectrum_mz.append(spectrum_data.GetMZValueAt(j))
                spectrum_abundance.append(abundance)

            records.append(
                {
                    "ScanID": record.ScanID,
                    "ScanMethodID": record.ScanMethodID,
                    "TimeSegmentID": record.TimeSegmentID,
                    "CalibrationID": record.CalibrationID,
                    "ScanTime": record.ScanTime,
                    "ScanType": record.ScanType,
                    # "RT": meta_data.GetRT(i), # should be the same as record.ScanTime
                    # "BPM": meta_data.GetBPM(i),
                    "TIC": record.TIC,
                    "AbundanceLimit": record.AbundanceLimit,
                    "BasePeakAbundance": record.BasePeakAbundance,
                    "CollisionEnergy": record.CollisionEnergy,
                    "CycleNumber": record.CycleNumber,
                    "FragmentorVoltage": record.FragmentorVoltage,
                    "IonPolarity": record.IonPolarity,
                    "MassCalOffset": int(record.MassCalOffset),
                    "MzOfInterest": record.MzOfInterest,
                    "MZs": spectrum_mz,
                    "Abundances": spectrum_abundance,
                }
            )
        logger.info("Done reading {}".format(test_dir))
        return records
    finally:
        qdacc.CloseDataFile()
