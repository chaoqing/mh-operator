# -*- coding: utf-8 -*-
import typing

# Import specific members from typing used in hints
from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    Generic,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    Union,
    overload,
)

import datetime
from enum import Enum

from mh_operator.SDK import Agilent, System

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisForm.Properties

class Resources:  # Class
    BatchState_Modified: str  # static # readonly
    BatchState_Processed: str  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    ERROR: System.Drawing.Bitmap  # static # readonly
    ErrMsg_CannotInitializeModule: str  # static # readonly
    ErrMsg_CannotRecognizeLayoutFile: str  # static # readonly
    ErrMsg_LayoutFileCollapsedUseDefaultLayout: str  # static # readonly
    ErrMsg_LayoutFileIsBatchMode: str  # static # readonly
    ErrMsg_LayoutFileIsMethodMode: str  # static # readonly
    ErrMsg_UnableToApplyPreviousLayout: str  # static # readonly
    FormTitle_Method: str  # static # readonly
    FormTitle_NewMethod: str  # static # readonly
    FormTitle_ReadOnly: str  # static # readonly
    Msg_MethodValidationMessages: str  # static # readonly
    Msg_NoMethodValidationMessage: str  # static # readonly
    PaneCaption_BatchTable: str  # static # readonly
    PaneCaption_CalibrationCurve: str  # static # readonly
    PaneCaption_CompoundInformation: str  # static # readonly
    PaneCaption_MethodErrorList: str  # static # readonly
    PaneCaption_MethodTable: str  # static # readonly
    PaneCaption_MethodTasks: str  # static # readonly
    PaneCaption_MetricsPlot: str  # static # readonly
    PaneCaption_SampleInformation: str  # static # readonly
    PaneCaption_Script: str  # static # readonly
    QuantitativeAnalysisDeskTop: System.Drawing.Icon  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    StatusPaenl_Tooltip_Connection: str  # static # readonly
    StatusPanel_CheckingConnection: str  # static # readonly
    StatusPanel_ConnectedTo: str  # static # readonly
    StatusPanel_ConnectionError: str  # static # readonly
    StatusPanel_Tooltip_BatchState: str  # static # readonly
    StatusPanel_Tooltip_CompoundName: str  # static # readonly
    StatusPanel_Tooltip_ConnectionError: str  # static # readonly
    StatusPanel_Tooltip_Coordinates: str  # static # readonly
    StatusPanel_Tooltip_SampleName: str  # static # readonly
    StatusPanel_Tooltip_Table: str  # static # readonly
    StatusPanel_Tooltip_User: str  # static # readonly
