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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.Properties

class Resources:  # Class
    AppName: str  # static # readonly
    Compare: System.Drawing.Bitmap  # static # readonly
    CompoundName: str  # static # readonly
    CompoundNameLevelName: str  # static # readonly
    CompoundNameTransition: str  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    Err_MethodNotExist: str  # static # readonly
    Label_Column: str  # static # readonly
    Label_Date: str  # static # readonly
    Label_Description: str  # static # readonly
    Label_Details: str  # static # readonly
    Label_DisplayName: str  # static # readonly
    Label_File1Exists: str  # static # readonly
    Label_File2Exists: str  # static # readonly
    Label_Identical: str  # static # readonly
    Label_Modified: str  # static # readonly
    Label_Name: str  # static # readonly
    Label_Reason: str  # static # readonly
    Label_Revision: str  # static # readonly
    Label_Table: str  # static # readonly
    Label_Type: str  # static # readonly
    Label_User: str  # static # readonly
    Label_Value1: str  # static # readonly
    Label_Value2: str  # static # readonly
    MethodItemType_General: str  # static # readonly
    MethodItemType_Quant: str  # static # readonly
    MethodItemType_QuantReport: str  # static # readonly
    MethodItemType_Unknowns: str  # static # readonly
    MethodItemType_UnknownsReport: str  # static # readonly
    Msg_BothMethodsNotExist: str  # static # readonly
    Msg_CannotCompareFolderAndFile: str  # static # readonly
    Msg_ComplianceNotSupported: str  # static # readonly
    Msg_Method1NotExist: str  # static # readonly
    Msg_Method2NotExist: str  # static # readonly
    Msg_MethodsIdentical: str  # static # readonly
    Progress_RetrievingHistory: str  # static # readonly
    Progress_Revision: str  # static # readonly
    Report_Column: str  # static # readonly
    Report_ComplianceName: str  # static # readonly
    Report_Date: str  # static # readonly
    Report_Description: str  # static # readonly
    Report_FileCreated: str  # static # readonly
    Report_FileNotExist: str  # static # readonly
    Report_FileRemoved: str  # static # readonly
    Report_Generated: str  # static # readonly
    Report_Identical: str  # static # readonly
    Report_MethodPath: str  # static # readonly
    Report_Modified: str  # static # readonly
    Report_PageNumber: str  # static # readonly
    Report_Reason: str  # static # readonly
    Report_ReportDate: str  # static # readonly
    Report_Revision: str  # static # readonly
    Report_Revisions: str  # static # readonly
    Report_Server: str  # static # readonly
    Report_Summary: str  # static # readonly
    Report_Table: str  # static # readonly
    Report_Title: str  # static # readonly
    Report_Type: str  # static # readonly
    Report_User: str  # static # readonly
    Report_Value1: str  # static # readonly
    Report_Value2: str  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    SampleName: str  # static # readonly
    Usage: str  # static # readonly
    app: System.Drawing.Icon  # static # readonly
    history: System.Drawing.Icon  # static # readonly
