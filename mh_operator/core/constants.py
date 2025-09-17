from enum import Enum

from mh_operator.utils.common import logger


class SampleType(str, Enum):
    Sample = S = "Sample"
    Blank = B = "Blank"
    MatrixBlank = MB = "MatrixBlank"
    Calibration = C = "Calibration"
    QC = "QC"
    CC = "CC"
    DoubleBlank = DB = "DoubleBlank"
    Matrix = M = "Matrix"
    MatrixDup = MD = "MatrixDup"
    TuneCheck = TC = "TuneCheck"
    ResponseCheck = RC = "ResponseCheck"

    @classmethod
    def _missing_(cls, value):
        if value is None:
            return SampleType.Sample
        if isinstance(value, str) and value.upper() in cls._member_map_:
            return cls[value.upper()]
        logger.warning(f"Sample Type {value} not exist, default to be Sample")
        return SampleType.Sample
