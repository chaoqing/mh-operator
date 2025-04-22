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

from .Agilent.MassSpectrometry.DataAnalysis import IFXData, IPeakList, IRange

# Stubs for namespace: GenieIntegrator

class ActionCodes(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FALSE: GenieIntegrator.ActionCodes = ...  # static # readonly
    NEGATIVE: GenieIntegrator.ActionCodes = ...  # static # readonly
    NORMAL: GenieIntegrator.ActionCodes = ...  # static # readonly
    TANSKIM: GenieIntegrator.ActionCodes = ...  # static # readonly
    TANSKIMEXP: GenieIntegrator.ActionCodes = ...  # static # readonly

class DO_PEAK(System.IComparable):  # Class
    def __init__(self) -> None: ...

    FrontShId: System.Collections.Generic.List[GenieIntegrator.DO_SHOULD]
    NrFrontShoulders: int
    NrRearShoulders: int
    RearShId: System.Collections.Generic.List[GenieIntegrator.DO_SHOULD]
    pk_info: GenieIntegrator.TGAPeakInfo

class DO_SHOULD:  # Class
    def __init__(self) -> None: ...

    height: float
    time: float

class DescriptorRecord(
    System.ICloneable,
    GenieIntegrator.IBLDescriptorRecord,
    GenieIntegrator.IMultipassDescriptorRecord,
    GenieIntegrator.IEXTDescriptorRecord,
    GenieIntegrator.IShoulderDescriptorRecord,
    GenieIntegrator.IXCPDescriptorRecord,
    GenieIntegrator.IPEAKDescriptorRecord,
    GenieIntegrator.ISLICEDescriptorRecord,
    GenieIntegrator.IHEADDescriptorRecord,
    GenieIntegrator.IEVENTDescriptorRecord,
    GenieIntegrator.IINITDescriptorRecord,
):  # Class
    def __init__(self) -> None: ...

    BL: GenieIntegrator.IBLDescriptorRecord
    EVENT: GenieIntegrator.IEVENTDescriptorRecord
    EXT: GenieIntegrator.IEXTDescriptorRecord
    FRSH: GenieIntegrator.IShoulderDescriptorRecord
    HEAD: GenieIntegrator.IHEADDescriptorRecord
    INIT: GenieIntegrator.IINITDescriptorRecord
    PEAK: GenieIntegrator.IPEAKDescriptorRecord
    RRSH: GenieIntegrator.IShoulderDescriptorRecord
    SLICE: GenieIntegrator.ISLICEDescriptorRecord
    XCP: GenieIntegrator.IXCPDescriptorRecord
    flag_peak: int
    peak_type: GenieIntegrator.DescriptorType

    area: float
    area_reject_i: float
    baseline_end: float
    baseline_start: float
    code: GenieIntegrator.TimedEventCode
    duration: float
    errors: int
    front_area_after_infl: float
    front_area_bfore_infl: float
    front_height: float
    front_inflxion_height: float
    front_inflxion_time: float
    front_r2: float
    front_ratio: float
    front_sh_time: float
    front_time: float
    half_width: float
    height: float
    initial_offset: float
    max_value: float
    min_value: float
    mismatch: float
    no_records: int
    rear_area_bfore_infl: float
    rear_height: float
    rear_inflxion_height: float
    rear_inflxion_time: float
    rear_r2: float
    rear_ratio: float
    rear_sh_time: float
    retention_time: float
    run_time: float
    slice_area_a: float
    slice_area_b: float
    slice_area_c: float
    slice_area_d: float
    slice_area_e: float
    slice_width: float
    slope: float
    start_bl_value: float
    start_right: bool
    start_time: float
    stop_bl_value: float
    symmetry: float
    time: float
    time_event: float
    time_offset: float
    value: float
    width: float

    def ResetUnionPointers(self) -> None: ...
    def Clone(self) -> Any: ...

class DescriptorType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    area_sum_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    baseline_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    data_name_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    extended_peak_end_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    extended_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    extended_peak_start_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    front_shoulder_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    header_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    initialize_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    man_exp_tan_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    man_neg_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    man_tan_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    manual_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    multipass_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    negative_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    normal_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    rear_shoulder_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    recalc_solvent_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    slice_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    solvent_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    tangent_skim_peak_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    timed_event_info: GenieIntegrator.DescriptorType = ...  # static # readonly
    x_cp_info: GenieIntegrator.DescriptorType = ...  # static # readonly

class FormGenieIntegratorParameters(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(
        self,
        getAndSet: GenieIntegrator.GetAndSet,
        timedEvents: System.Collections.Generic.List[GenieIntegrator.TimedEvent],
    ) -> None: ...

    TimedEvents: System.Collections.Generic.List[GenieIntegrator.TimedEvent]  # readonly

    # Nested Types

    class GenieEventTypes(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        AreaReject: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        AreaSumOff: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        AreaSumOn: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        BaselineAllValleysOff: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        BaselineAllValleysOn: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        BaselineBack: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        BaselineHoldOff: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        BaselineHoldOn: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        BaselineNextValley: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        BaselineNow: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        IntegratorOff: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        IntegratorOn: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        NegativePeakOff: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        NegativePeakOn: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        PeakWidth: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        SolventPeakOff: (
            GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes
        ) = ...  # static # readonly
        SolventPeakOn: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        TangentSkim: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly
        Threshold: GenieIntegrator.FormGenieIntegratorParameters.GenieEventTypes = (
            ...
        )  # static # readonly

class GenieIntegrator:  # Class
    def __init__(self) -> None: ...

    AREAS: int = ...  # static # readonly
    BASELINE: int = ...  # static # readonly
    DOWNSLOPE: int = ...  # static # readonly
    DOWN_ON_SOLV_DOWN: int = ...  # static # readonly
    FRONT_SLOPE: int = ...  # static # readonly
    NULL_SET: int = ...  # static # readonly
    OFF: int = ...  # static # readonly
    REAR_SLOPE: int = ...  # static # readonly
    SLICES: int = ...  # static # readonly
    SLICES_END: int = ...  # static # readonly
    SOLVENT_DOWNSLOPE: int = ...  # static # readonly
    SOLVENT_UPSLOPE: int = ...  # static # readonly
    STARTUP: int = ...  # static # readonly
    TANGENT_WAITING: int = ...  # static # readonly
    UPSLOPE: int = ...  # static # readonly
    UP_ON_SOLV_DOWN: int = ...  # static # readonly
    aborted: int = ...  # static # readonly
    dTimeResolutionInMinutes: float = ...  # static # readonly
    distorted: int = ...  # static # readonly
    m_TimedEventList: System.Collections.Generic.List[GenieIntegrator.TimedEvent]
    m_hCardinalPointFile: System.Collections.ArrayList
    m_pGenieGetAndSet: GenieIntegrator.GetAndSet
    m_sCurrEventIndex: int
    over: int = ...  # static # readonly
    under: int = ...  # static # readonly

    def da_command_integrate_CGRAM(
        self,
        pChroObj: List[IFXData],
        pPeakList: List[IPeakList],
        p2: IRange,
        lWhichSignal: int,
    ) -> None: ...
    def IntegrateChromatograms(
        self,
        start: int,
        stop: int,
        these_objects: List[IFXData],
        theseIntegratedPeakLists: List[IPeakList],
    ) -> None: ...
    @staticmethod
    def GET_STOP_CODE(flag_bits: int) -> GenieIntegrator.flag_pk_types: ...
    def ManualIntegrateChromatogram(
        self,
        points: IFXData,
        loTimeMinutes: float,
        dStartLevel: float,
        hiTimeMinutes: float,
        dEndLevel: float,
        bDropAllValleys: bool,
    ) -> None: ...
    def gen_baseline_allocator(self, PListId: GenieIntegrator.PList) -> bool: ...
    def IntegrateChromatogram(
        self, start: int, stop: int, this_object: IFXData
    ) -> None: ...
    @staticmethod
    def GET_START_CODE(flag_bits: int) -> GenieIntegrator.flag_pk_types: ...
    @staticmethod
    def SET_IN(item: int, set: int) -> bool: ...
    def da_command_autoint(
        self,
        pChroObj: List[IFXData],
        pPeakList: List[IPeakList],
        p2: IRange,
        lWhichSignal: int,
        pct: float,
    ) -> None: ...

class GetAndSet:  # Class
    def __init__(self) -> None: ...

    area_reject: float
    area_scale_factor: float
    data_rate: float
    data_scale_factor: float
    dead_volume_time: float
    delayed_start_time: float
    detect_threshold: float
    distorted: float
    exp_pk_width: float
    overrange: float
    prebunch: float
    shoulders_enabled: bool
    solvent_slope: float
    split_solvent_v: float
    theo_plates: float
    time_offset: float
    underrange: float

class IBLDescriptorRecord(object):  # Interface
    height: float
    slope: float
    time: float

class IEVENTDescriptorRecord(object):  # Interface
    code: GenieIntegrator.TimedEventCode
    time_event: float
    value: float

class IEXTDescriptorRecord(object):  # Interface
    front_area_after_infl: float
    front_area_bfore_infl: float
    front_inflxion_height: float
    front_inflxion_time: float
    rear_area_bfore_infl: float
    rear_inflxion_height: float
    rear_inflxion_time: float

class IEventTGAPeakInfo(object):  # Interface
    code: float
    time: float
    value: float

class IHEADDescriptorRecord(object):  # Interface
    errors: int
    max_value: float
    min_value: float
    no_records: int
    run_time: float
    start_bl_value: float
    start_right: bool
    stop_bl_value: float

class IHeaderTGAPeakInfo(object):  # Interface
    errors: int
    no_records: int
    number: int
    run_time: float

class IINITDescriptorRecord(object):  # Interface
    area_reject_i: float
    initial_offset: float
    time_offset: float

class IMultipassDescriptorRecord(object):  # Interface
    front_r2: float
    front_ratio: float
    half_width: float
    mismatch: float
    rear_r2: float
    rear_ratio: float

class INormalTGAPeakInfo(object):  # Interface
    area: float
    baseline: float
    baseline_end: float
    baseline_start: float
    height: float
    level_end: float
    level_start: float
    retention_time: float
    symmetry: float
    time_end: float
    time_start: float
    width: float

class IPEAKDescriptorRecord(object):  # Interface
    area: float
    duration: float
    front_height: float
    front_time: float
    height: float
    rear_height: float
    retention_time: float

class ISLICEDescriptorRecord(object):  # Interface
    slice_area_a: float
    slice_area_b: float
    slice_area_c: float
    slice_area_d: float
    slice_area_e: float
    slice_width: float
    start_time: float

class IShoulderDescriptorRecord(object):  # Interface
    height: float
    time: float

class IShoulderTGAPeakInfo(object):  # Interface
    shoulder_height: float
    shoulder_time: float

class ISliceTGAPeakInfo(object):  # Interface
    slice_area: float
    slice_width: float
    start_time: float

class IXCPDescriptorRecord(object):  # Interface
    baseline_end: float
    baseline_start: float
    front_sh_time: float
    rear_sh_time: float
    symmetry: float
    width: float

class IntVarRecord:  # Class
    def __init__(self) -> None: ...

    _event: GenieIntegrator.TimedEvent
    averaging: bool
    backward_flag: bool
    baseline_acc: float
    baseline_acc_2: float
    baseline_acc_count: int
    baseline_flag: bool
    baseline_interval: int
    baseline_last: float
    baseline_last_when: float
    baseline_peak: GenieIntegrator.DescriptorRecord
    bunch_down: bool
    bunch_up: bool
    bunchno: int
    bunchvalue: int
    c1n: float
    c1n1: float
    c2n: float
    c2n1: float
    c3n: float
    c3n1: float
    cluster: bool
    cp_record_no: int
    cp_status: bool
    current_ticks: float
    curvature_min: float
    data_acc: float
    dn1: float
    dn2: float
    dn3: float
    dn4: float
    dn5: float
    downslope_counter: int
    dp: float
    dp1: float
    dp2: float
    dp3: float
    dp4: float
    dp_baseline: float
    dp_next_baseline: float
    dp_time: float
    dwUserData: int
    dx1: float
    dx2: float
    dx3: float
    even_odd: bool
    ext_solvent: GenieIntegrator.DescriptorRecord
    extended_peak: GenieIntegrator.DescriptorRecord
    extensio_count: int
    filter_1: bool
    filter_2: bool
    filter_3: bool
    filter_no_bunch: int
    filter_wait: int
    future_baseline_flag: bool
    future_solvent: bool
    h_errors: int
    h_start_bl_value: float
    height_at_baseline: float
    height_extrem: float
    infl_area: float
    infl_height: float
    infl_time: float
    inflection: bool
    initial_offset: float
    integ_status: GenieIntegrator.IntegStatusRecord
    integrator_state: int
    min_max: GenieIntegrator.SendParameters
    neg_curv: int
    negative_curvature: bool
    new_peak_width: float
    non_peak: GenieIntegrator.DescriptorRecord
    parameters: GenieIntegrator.IntegratorParameters
    partial_peak: GenieIntegrator.DescriptorRecord
    peak_area_acc: float
    peak_area_acc_2: float
    peak_ticks: float
    pivot_height: float
    pivot_time: float
    point: float
    pointm1: float
    pos_curv: int
    ready_for_event: bool
    real_time_extrem: float
    run_parameters: GenieIntegrator.RunTimeParameters
    s1n: float
    s1n1: float
    s2n: float
    s2n1: float
    s3n: float
    s3n1: float
    set_new_pk_width: bool
    shoulder_count: int
    shoulder_found: bool
    solvent_area_acc: float
    solvent_ds_ctr: int
    solvent_peak: GenieIntegrator.DescriptorRecord
    solvent_shoulders: bool
    start_right_flag: bool
    store_peak: bool
    store_slice: int
    time_extrem: float
    upslope_counter: int
    valley: float
    waiting_time: float

class IntegStatusRecord:  # Class
    def __init__(self) -> None: ...

    negative_peak: bool
    peak_extension_time: bool
    positive_curvature: bool
    shoulder_detect: bool

class IntegratorParameters:  # Class
    def __init__(self) -> None: ...

    i_area_reject: float
    i_area_scale_factor: float
    i_dead_volume_time: float
    i_delayed_start_time: float
    i_distorted: float
    i_double_extended: bool
    i_extended_peaks: bool
    i_external_baseline: bool
    i_external_baseline_v: float
    i_initial_data_rate: float
    i_multipass: bool
    i_overrange: float
    i_peak_width: float
    i_plates: float
    i_prebunch: float
    i_shoulders: bool
    i_solvent_slope: float
    i_split_solvent: float
    i_threshold: float
    i_time_offset: float
    i_underrange: float
    i_variwidth: bool

class PList(
    List[Any],
    Iterable[Any],
    System.Collections.ArrayList,
    Sequence[Any],
    System.ICloneable,
):  # Class
    def __init__(self) -> None: ...

class RunTimeParameters:  # Class
    def __init__(self) -> None: ...

    auto_peak_width_disable: bool
    baseline_reset_valley: bool
    baseline_rst_all_valleys: bool
    broadening: bool
    dead_volume_time: float
    delayed_start_time: float
    drop: bool
    drop_valley: bool
    extended_peaks: bool
    fire_value: float
    hold_baseline: bool
    need_int_ranging: bool
    negative_peaks: bool
    peak_broadening_rate: float
    peak_width: float
    rflag: int
    set_peak_width: bool
    shoulders_as_peaks: bool
    slice_width: float
    solvent_slope: float
    split_solvent: float
    tangent_skim: bool
    th1: float
    th2: float
    threshold: float
    time_offset: float

class SendParameters:  # Class
    def __init__(self) -> None: ...

    max_value: float
    min_value: float

class SortEventTimeAscendingHelper(System.Collections.IComparer):  # Class
    def __init__(self) -> None: ...
    def Compare(self, x: Any, y: Any) -> int: ...

class TGAPeakInfo(
    GenieIntegrator.ISliceTGAPeakInfo,
    GenieIntegrator.IShoulderTGAPeakInfo,
    GenieIntegrator.IEventTGAPeakInfo,
    GenieIntegrator.IHeaderTGAPeakInfo,
    GenieIntegrator.INormalTGAPeakInfo,
):  # Class
    def __init__(self) -> None: ...

    T_EVENT: GenieIntegrator.IEventTGAPeakInfo
    T_FRSH: GenieIntegrator.IShoulderTGAPeakInfo
    T_HEAD: GenieIntegrator.IHeaderTGAPeakInfo
    T_PEAK: GenieIntegrator.INormalTGAPeakInfo
    T_RRSH: GenieIntegrator.IShoulderTGAPeakInfo
    T_SLICE: GenieIntegrator.ISliceTGAPeakInfo
    flag_peak: int
    peak_type: GenieIntegrator.DescriptorType

    area: float
    baseline: float
    baseline_end: float
    baseline_start: float
    code: float
    errors: int
    height: float
    level_end: float
    level_start: float
    no_records: int
    number: int
    retention_time: float
    run_time: float
    shoulder_height: float
    shoulder_time: float
    slice_area: float
    slice_width: float
    start_time: float
    symmetry: float
    time: float
    time_end: float
    time_start: float
    value: float
    width: float

class TimedEvent:  # Class
    def __init__(self) -> None: ...

    event_code: GenieIntegrator.TimedEventCode
    time: float
    value: float

    def RequiresValue(self) -> bool: ...

class TimedEventCode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ECALLVALLEYS: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECAREAS: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECARM: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECBACKWARD: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECBASELINE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECDISABLE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECEND: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECFRONT: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECHOLD: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECIMMEDIATE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECNEGATIVE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECOFFSET: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECREJECT: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECSHOULDERS: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECSLICES: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECSP: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECTANGENT: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECTHRESHOLD: GenieIntegrator.TimedEventCode = ...  # static # readonly
    ECWIDTH: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECALLVALLEYS: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECAREAS: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECARM: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECBACKWARD: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECBASELINE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECDISABLE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECEND: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECFRONT: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECHOLD: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECNEGATIVE: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECREJECT: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECSHOULDERS: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECSLICES: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECSP: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECTANGENT: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECTHRESHOLD: GenieIntegrator.TimedEventCode = ...  # static # readonly
    MECWIDTH: GenieIntegrator.TimedEventCode = ...  # static # readonly

class al_time_parameters:  # Class
    def __init__(self) -> None: ...

    area_reject: float
    areas: bool
    fix_backwards_flag: bool
    negative_peaks: bool
    penetration: bool
    slices: bool
    tangent_skim: bool

class al_vars:  # Class
    def __init__(self) -> None: ...

    NextPkId: GenieIntegrator.DO_PEAK
    NrFrontShoulders: int
    NrRearShoulders: int
    PListId: GenieIntegrator.PList
    al_baseline: float
    al_parameters: GenieIntegrator.al_time_parameters
    area_adjusted: float
    area_adjustment: float
    bl_slope: float
    bl_time: float
    bl_value: float
    cp_status: bool
    duration: float
    end_height: float
    extend_follows: bool
    fix_b: float
    fix_backwards_offset: float
    fix_later: float
    front_height: float
    front_time: float
    height_adjusted: float
    height_factor: float
    multipass_found: bool
    multipassrecord: GenieIntegrator.TGAPeakInfo
    no_more_room: bool
    nr_records: int
    offset: float
    offset_time: float
    offset_time_2: float
    parameters: GenieIntegrator.IntegratorParameters
    peak: GenieIntegrator.DescriptorRecord
    peakid: GenieIntegrator.DO_PEAK
    proc_write_status: bool
    processed_peak: GenieIntegrator.TGAPeakInfo
    rear_height: float
    rear_time: float
    retention_time: float
    solvent_time: float
    this_cp_rec_no: int
    time_baseline: float
    time_factor: float
    v_offset: float
    v_offset_2: float
    v_slope: float
    v_time: float

class flag_pk_types(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    baseline_pk: GenieIntegrator.flag_pk_types = ...  # static # readonly
    force_pk: GenieIntegrator.flag_pk_types = ...  # static # readonly
    horizontal_pk: GenieIntegrator.flag_pk_types = ...  # static # readonly
    manual_pk: GenieIntegrator.flag_pk_types = ...  # static # readonly
    penetration_pk: GenieIntegrator.flag_pk_types = ...  # static # readonly
    valley_pk: GenieIntegrator.flag_pk_types = ...  # static # readonly

class run_parameter_flags(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    auto_solvent_disable: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    fire_on_inflection: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    fire_on_top: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    fire_on_valley: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    fire_on_value: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    front_tangent: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    integrator_off: GenieIntegrator.run_parameter_flags = ...  # static # readonly
    shoulders: GenieIntegrator.run_parameter_flags = ...  # static # readonly

class tgcresponseerrors(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    adoverrange: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    adproblem: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    analysisaborted: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    cardpoints_gt_max: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    controleventsaborted: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    endnotonbaseline: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    error7: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    excessnegativeinput: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    integoridentaborted: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    nopeaksintegrated: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    noreferencepeakfound: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    nostandardpeakfound: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    nosummedpeaks: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    numberofpeaks_gt_max: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    readingsmissed: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
    runaborted: GenieIntegrator.tgcresponseerrors = ...  # static # readonly
