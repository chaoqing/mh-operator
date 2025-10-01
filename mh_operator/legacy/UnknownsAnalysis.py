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
        self.path = os.path.abspath(path)
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
        istd_rt=None,
        rt_delta=(0.5, 0.5),
        istd_value=None,
        istd_name=None,
        istd_cas=None,
        istd_index=None,
        recover_rt=None,
        recover_name=None,
        recover_value=None,
        from_sample=None,
    ):
        self.istd_rt = istd_rt
        self.l_rt_delta, self.r_rt_delta = (
            (rt_delta, rt_delta) if isinstance(rt_delta, (int, float)) else rt_delta
        )
        self.istd_value = istd_value
        self.istd_name = istd_name
        self.istd_cas = istd_cas
        self.istd_index = istd_index
        self.recover_rt = recover_rt
        self.recover_name = recover_name
        self.recover_value = recover_value

        assert self.istd_value is not None or (
            self.recover_value is not None and self.recover_rt is not None
        ), "recovery compound must be set when ISTD value not set"

        self.from_sample = from_sample

    def to_dict(self):
        # type: () -> dict
        return dict(
            ISTDFlag=True,
            MZ=0.0,
            RetentionTime=self.istd_rt,
            LeftRetentionTimeDelta=self.l_rt_delta,
            RightRetentionTimeDelta=self.r_rt_delta,
            RetentionTimeDeltaUnits="Minutes",
            CompoundName=self.istd_name,
            CASNumber=self.istd_cas,
            ISTDConcentration=self.istd_value,
        )

    def find_istd_compound(self, tables, sample_id=None):
        # type: (dict, int) -> dict
        def find_component(rt, l_rt, r_rt, name, s_id):
            rt_diffs = (
                (abs(_rt - rt), r)
                for r, (_rt, _name, _id) in enumerate(
                    zip(
                        tables["RetentionTime"],
                        tables["CompoundName"],
                        tables["SampleID"],
                    )
                )
                if _rt > l_rt
                and _rt < r_rt
                and (name is None or _name == name)
                and (id is None or _id == s_id)
            )
            try:
                _, row = min(rt_diffs)
                return row
            except ValueError:
                logger.warn(
                    "no compound candidate found in R.T. ({}-{}, {}+{}) with name {}".format(
                        rt, rt - l_rt, rt, r_rt - rt, name
                    )
                )
                return None

        row = find_component(
            self.istd_rt,
            self.istd_rt - self.l_rt_delta,
            self.istd_rt + self.r_rt_delta,
            self.istd_name,
            sample_id,
        )
        assert row is not None, "Did not find the ISTD compound"

        target = {
            k: tables[k][row]
            for k in ("CompoundName", "CASNumber", "RetentionTime", "RetentionIndex")
        }

        if self.recover_value is not None:
            recover_row = find_component(
                self.recover_rt,
                self.recover_rt - self.l_rt_delta,
                self.recover_rt + self.r_rt_delta,
                self.recover_name,
                sample_id,
            )
            assert (
                recover_row is not None
            ), "Did not find the recover compound for ISTD value setting"

            target["ISTDConcentration"] = (
                tables["Area"][row] * self.recover_value / tables["Area"][recover_row]
            )

        logger.info("ISTD compound info to be updated: {}".format(target))
        return target

    @staticmethod
    def target_operations(sample_ids, column_values, target_id=0, batch_id=0):
        # type: (list, dict, int, int) -> list
        kv = [
            KeyValue(k, v)
            for k, v in column_values.items()
            if v is not None and k != "SampleID"
        ]
        return [
            AddTargetCompoundParameter(batch_id, s, target_id) for s in sample_ids
        ] + [
            TargetCompoundColumnValuesParameter(batch_id, s, target_id, kv)
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
    # type: (str, list, str, ISTD, str) -> str
    (batch_folder,) = set(os.path.split(s.path)[0] for s in samples)
    analysis_file = os.path.join(batch_folder, "UnknownsResults", analysis_name)
    append_mode = os.path.exists(analysis_file)

    if append_mode:
        logger.warn("Append mode not fully supported")
        _commands.OpenAnalysis(batch_folder, analysis_name, False)
        logger.info(
            "Analysis project {} opened under {}".format(analysis_name, batch_folder)
        )
    else:
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

    if istd is not None and not append_mode:
        target_compound = istd.to_dict()

        if istd.from_sample is not None:
            istd_sample_id = samples_id.get(os.path.basename(istd.from_sample), None)
            assert istd_sample_id is not None, "ISTD sample not correctly set"

            logger.info(
                "Analysis one sample ({}) with id {} to setup ISTD".format(
                    istd.from_sample, istd_sample_id
                )
            )
            _commands.AnalyzeSamples(batch_id, istd_sample_id, True)

            tables_data = DataTables()
            tables_data.Component = [uadacc.GetComponents(batch_id, istd_sample_id)]
            tables_data.Hit = [uadacc.GetHits(batch_id, istd_sample_id)]
            istd_sample_components = tables_data.ComponentsWithBestPrimaryHit(
                batch_id, istd_sample_id
            )
            target_compound.update(
                **istd.find_istd_compound(
                    istd_sample_components, sample_id=istd_sample_id
                )
            )

        logger.info("Apply ISTD target compound info: {}".format(target_compound))
        assert all(
            target_compound.get(k, None) is not None
            for k in (
                "ISTDFlag",
                "MZ",
                "RetentionTime",
                "LeftRetentionTimeDelta",
                "RightRetentionTimeDelta",
                "RetentionTimeDeltaUnits",
                "CompoundName",
                "ISTDConcentration",
            )
        ), "Must set valid values for the ISTD table"
        _commands.SetTargets(
            istd.target_operations(
                samples_id.values(),
                target_compound,
                target_id=0,
                batch_id=batch_id,
            )
        )

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
                "-M={}".format(os.path.abspath(report_method)),
                "-OP={}".format(report_path),
            ]
        )
        logger.info(
            "Report generated under {} with method {}".format(
                report_path, report_method
            )
        )

    return analysis_file + ".json"
