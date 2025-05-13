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

from mh_operator.legacy.common import global_state, logger

try:
    import clr

    clr.AddReference("CoreCommand")
    clr.AddReference("MethodSetup")
    clr.AddReference("UnknownsAnalysisII")
    clr.AddReference("UnknownsAnalysisII.Command")
    clr.AddReference("UnknownsAnalysisII.UI")

    import _commands
    import System
    from Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command import (
        AddTargetCompoundParameter,
        KeyValue,
        TargetCompoundColumnValuesParameter,
    )

    uadacc = global_state.UADataAccess
except ImportError:
    assert sys.executable is not None, "Should never reach here"
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII import (
        Command as _commands,
    )
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command import (
        AddTargetCompoundParameter,
        KeyValue,
        TargetCompoundColumnValuesParameter,
    )
    from mh_operator.SDK.Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF import (
        IUADataAccess,
    )

    uadacc = IUADataAccess()

from mh_operator.legacy import UnknownsAnalysisDataSet
from mh_operator.legacy.UnknownsAnalysisDataSet import DataTables, TargetCompoundRow


class Sample(object):
    def __init__(self, path, type="Sample"):
        self.path = os.path.realpath(path)
        self.type = type

    @property
    def folder(self):
        return os.path.split(self.path)[0]

    @property
    def name(self):
        return os.path.split(self.path)[1]

    def __str__(self):
        return "< {} : {} >".format(self.name, self.type)


class ISTD(object):
    def __init__(
        self,
        istd_rt,
        istd_value,
        istd_name=None,
        recover_rt=None,
        recover_name=None,
        from_sample=None,
    ):
        self.istd_rt = istd_rt
        self.istd_value = istd_value
        self.istd_name = istd_name
        self.recover_rt = recover_rt
        self.recover_name = recover_name

        self.from_sample = from_sample

    def find_istd_components(self, tables):
        # type: (DataTables) -> TargetCompoundRow
        target = UnknownsAnalysisDataSet.TargetCompoundRow()

        hit = UnknownsAnalysisDataSet.HitRow()
        component = UnknownsAnalysisDataSet.ComponentRow()

        target.CompoundName = hit.CompoundName
        target.CASNumber = hit.CASNumber
        target.ISTDFlag = True
        target.ISTDConcentration = self.istd_value
        target.RetentionTime = component.RetentionTime
        target.RetentionIndex = component.RetentionIndex

        target.LeftRetentionTimeDelta = 0.5
        target.RightRetentionTimeDelta = 0.5
        target.RetentionTimeDeltaUnits = "Minutes"

        target.MZ = 0.0

        return target

    def target_operations(sample_ids, target_id=0, batch_id=0):
        # type: (list, int) -> list
        return [
            AddTargetCompoundParameter(batch_id, s, target_id) for s in sample_ids
        ] + [
            TargetCompoundColumnValuesParameter(batch_id, s, target_id, [KeyValue()])
            for s in sample_ids
        ]


def export_analysis(analysis_file=None):
    if analysis_file is not None:
        folder, name = os.path.split(analysis_file)
        _commands.OpenAnalysis(os.path.join(folder, ".."), name, True)
    try:
        tables = DataTables()

        tables.Analysis = [uadacc.GetAnalysis()]
        tables.Batch = [uadacc.GetBatches()]
        (batch_id,) = tables.Batch["BatchID"]
        tables.Sample = [uadacc.GetSamples(batch_id)]
        sample_ids = tables.Sample["SampleID"]

        tables.Component = (uadacc.GetComponents(batch_id, s) for s in sample_ids)
        tables.Hit = (uadacc.GetHits(batch_id, s) for s in sample_ids)
        tables.IonPeak = (uadacc.GetIonPeak(batch_id, s) for s in sample_ids)
        tables.DeconvolutionMethod = (
            uadacc.GetDeconvolutionMethods(batch_id, s) for s in sample_ids
        )
        tables.LibrarySearchMethod = (
            uadacc.GetLibrarySearchMethods(batch_id, s) for s in sample_ids
        )
        tables.IdentificationMethod = (
            uadacc.GetIdentificationMethods(batch_id, s) for s in sample_ids
        )
        tables.TargetCompound = (
            uadacc.GetTargetCompounds(batch_id, s) for s in sample_ids
        )
        tables.Peak = (uadacc.GetPeak(batch_id, s) for s in sample_ids)
        tables.TargetQualifier = (
            uadacc.GetTargetQualifier(batch_id, s) for s in sample_ids
        )
        tables.PeakQualifier = (
            uadacc.GetPeakQualifier(batch_id, s) for s in sample_ids
        )
        tables.TargetMatchMethod = (
            uadacc.GetTargetMatchMethods(batch_id, s) for s in sample_ids
        )
        tables.AuxiliaryMethod = (
            uadacc.GetAuxiliaryMethod(batch_id, s) for s in sample_ids
        )

        return tables
    finally:
        if analysis_file is not None:
            _commands.CloseAnalysis()


def analysis_samples(
    analysis_name, samples, analysis_method, istd=None, report_method=None
):
    # type: (str, list, str, ISTD, str) -> dict
    (batch_folder,) = set(os.path.split(s.path)[0] for s in samples)
    analysis_file = os.path.join(batch_folder, "UnknownsResults", analysis_name)

    if os.path.exists(analysis_file):
        logger.info("Cleaning existing analysis {}".format(analysis_file))
        os.unlink(analysis_file)

    tables_data = DataTables()

    _commands.NewAnalysis(batch_folder, analysis_name)
    logger.info(
        "Analysis project {} created under {}".format(analysis_name, batch_folder)
    )

    _commands.AddSamples(System.Array[System.String]([s.path for s in samples]))
    batch_id = next(iter(uadacc.GetBatches())).BatchID
    samples_id = {s.DataFileName: s.SampleID for s in uadacc.GetSamples(batch_id)}
    logger.info("Added samples {}".format(samples_id))

    for s in samples:
        if s.type is not None:
            _commands.SetSample(batch_id, samples_id[s.name], "SampleType", s.type)
    logger.info("Samples Type updated")

    _commands.LoadMethodToAllSamples(analysis_method)
    logger.info("Method {} loaded to all samples".format(analysis_method))

    if istd is not None and istd.from_sample is not None:
        istd_sample_id = samples_id.get(os.path.realpath(istd.from_sample), None)
        assert istd_sample_id is not None, "ISTD sample not correctly set"

        _commands.AnalyzeSamples(batch_id, istd_sample_id)

    if istd is not None:
        pass

    _commands.AnalyzeAll(True)
    _commands.SaveAnalysis()

    with open(analysis_file + ".json", "w") as fp:
        fp.write(export_analysis().to_json())
        logger.info("Analysis results exported into {}".format(fp.name))

    _commands.CloseAnalysis()
    logger.info("Analysis Closed")

    if report_method is not None:
        import subprocess

        from mh_operator.legacy.common import __DEFAULT_MH_BIN_DIR__

        report_path = os.path.join(batch_folder, "UnknownsReports", analysis_name)
        subprocess.call(
            [
                os.path.join(
                    os.environ.get("MH_BIN_DIR", __DEFAULT_MH_BIN_DIR__),
                    "UnknownsAnalysisII.ReportResults.exe",
                ),
                "-BP={}".format(batch_folder),
                "-AF={}".format(analysis_name),
                "-M={}".format(os.path.realpath(report_method)),
                "-OP={}".format(report_path),
            ]
        )
        logger.info(
            "Report generated under {} with method {}".format(
                report_path, report_method
            )
        )
