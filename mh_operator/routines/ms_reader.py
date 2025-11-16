import io
import os
import struct
from collections import Counter
from functools import cached_property
from itertools import groupby, islice

import numpy as np

from mh_operator.utils.common import logger


class AgilentGCMSDataReader:
    """Read the Agilent GCMS data.ms file described inside [Agilent .ms File Structure](https://github.com/evanyeyeye/rainbow/blob/ab0c6501901d2dbc746d96d99339f34be1f4c822/docs/source/agilent/ms.rst)"""

    fp = None

    def __init__(self, file=None, fileobj=None):
        if fileobj:
            self.fp = fileobj
            self._extfileobj = True
        else:
            file = os.fspath(file)
            if os.path.isdir(file):
                file = os.path.join(file, "data.ms")
            self.file = file
            self._extfileobj = False

    def __enter__(self):
        if not self._extfileobj:
            self.fp = open(self.file, "rb")

        fp = self.fp

        FILE_TYPE_STR_OFFSET = 0x4  # File type string (GC / MS Data File)

        # Validate file header.
        fp.seek(0)
        (head_validation,) = struct.Struct(">I").unpack(fp.read(4))
        assert (
            head_validation == 0x01320000
        ), "Not correct magic number for Agilent GCMS data"

        # Determine the type of .ms file based on header.
        type_ms_str = self._read_string(FILE_TYPE_STR_OFFSET, 1)
        assert type_ms_str == "GC / MS Data File", "Only GC / MS Data File is supported"

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._extfileobj and self.fp is not None:
            self.fp.close()
            self.fp = None

    def _read_string(self, offset, gap=2):
        """
        Extracts a string from the specified offset.

        This method is primarily useful for retrieving metadata.

        Args:
            offset (int): Offset to begin reading from.
            gap (int): Distance between two adjacent characters.

        Returns:
            String at the specified offset in the file header.

        """
        self.fp.seek(offset)
        str_len = struct.unpack("<B", self.fp.read(1))[0] * gap
        try:
            return self.fp.read(str_len)[::gap].decode().strip()
        except Exception as e:
            logger.warning(f"Failed to read string from {offset}: {e}")
            return ""

    def _read_header(self, offsets, gap=2):
        """
        Extracts metadata from the header of an Agilent data file.

        Args:
            offsets (dict): Dictionary mapping properties to file offsets.
            gap (int): Distance between two adjacent characters.

        Returns:
            Dictionary containing metadata as string key-value pairs.

        """
        metadata = {}
        for key, offset in offsets.items():
            string = self._read_string(offset, gap)
            if string:
                metadata[key] = string
        return metadata

    @cached_property
    def _raw_file_content_data(self):
        fp = self.fp

        short_unpack = struct.Struct(">H").unpack
        int_unpack = struct.Struct(">I").unpack
        little_short_unpack = struct.Struct("<H").unpack

        # Read the number of retention times from GC-MS specific offset.
        SCAN_COUNT_OFFSET = (
            0x142  # Number of retention times (GC-MS), Short, Little Endian
        )
        fp.seek(SCAN_COUNT_OFFSET)
        (num_times,) = little_short_unpack(fp.read(2))

        # Go to the data start offset.
        FILE_HEADER_LENGTH_OFFSET = (
            0x10A  # File header length (in shorts), Short, Big Endian
        )
        fp.seek(FILE_HEADER_LENGTH_OFFSET)
        (file_header_length_shorts,) = short_unpack(fp.read(2))
        # The data body starts after the file header.
        # This is to position the file pointer at the beginning of the first data segment.
        fp.seek(file_header_length_shorts * 2 - 2)

        times_us = np.empty(num_times, dtype=np.uint32)
        scan_counts = np.zeros(num_times, dtype=np.uint16)
        spectrum_pair_bytes = bytearray()

        for i in range(num_times):
            fp.read(2)
            times_us[i] = int_unpack(fp.read(4))[0]
            fp.read(6)
            scan_counts[i] = short_unpack(fp.read(2))[0]
            fp.read(4)

            pair_bytes = fp.read(scan_counts[i] * 4)
            spectrum_pair_bytes.extend(pair_bytes)

            fp.read(10)

        spectrum_pair_bytes = bytes(spectrum_pair_bytes)
        spectrum_pair_counts = len(spectrum_pair_bytes) // 4

        mzs_x20_int = np.ndarray(spectrum_pair_counts, ">H", spectrum_pair_bytes, 0, 4)
        abundance_encoded = np.ndarray(
            spectrum_pair_counts, ">H", spectrum_pair_bytes, 2, 4
        )
        abundance = np.multiply(
            8 ** (abundance_encoded >> 14),
            (abundance_encoded & 0x3FFF),
            dtype=np.uint32,
        )

        return times_us, scan_counts, mzs_x20_int, abundance

    @cached_property
    def meta_data(self):
        metadata_offsets = {
            "file_type": 0x4,  # File type
            "notebook": 0x18,  # Notebook name
            "parent_directory": 0x94,  # Parent directory
            "date": 0xB2,  # Date
            "unknown_d0": 0xD0,  # UNKNOWN (LCMS_3-30 / 5977B GCM)
            "method": 0xE4,  # Method
            "unknown_1c0": 0x1C0,  # UNKNOWN (5977B GCM) - null-byte separated string
            "unknown_268": 0x268,  # UNKNOWN (D:\MassHunter\Methods\) - null-byte separated string
            "method_466": 0x466,  # Method (Rt-bDEX-SE_mcminn.M) - null-byte separated string
            "unknown_664": 0x664,  # UNKNOWN (D:\MassHunter\GCMS\1\5977\) - null-byte separated string
            "unknown_862": 0x862,  # UNKNOWN (f2_hes_atune.u) - null-byte separated string
        }

        metadata = self._read_header(
            {
                "file_type": metadata_offsets["file_type"],
                "notebook": metadata_offsets["notebook"],
                "parent_directory": metadata_offsets["parent_directory"],
                "date": metadata_offsets["date"],
                "instrument_name": metadata_offsets["unknown_d0"],
                "method": metadata_offsets["method"],
            },
            gap=1,
        )

        metadata.update(
            self._read_header(
                {
                    "unknown_1c0": metadata_offsets["unknown_1c0"],
                    "unknown_268": metadata_offsets["unknown_268"],
                    "method_466": metadata_offsets["method_466"],
                    "unknown_664": metadata_offsets["unknown_664"],
                    "unknown_862": metadata_offsets["unknown_862"],
                },
                gap=2,
            )
        )
        return metadata

    @cached_property
    def retention_time_us(self):
        times_us, *_ = self._raw_file_content_data
        return times_us

    @cached_property
    def mass_to_charge_x20(self):
        _, _, mzs_x20_int, _ = self._raw_file_content_data
        return np.sort(np.unique(mzs_x20_int))

    @property
    def list_data(self):
        times_us, scan_counts, mzs_x20_int, abundance = self._raw_file_content_data

        spectrum_iter = zip(mzs_x20_int, abundance)

        return [
            (rt, list(islice(spectrum_iter, count)))
            for rt, count in zip(times_us, scan_counts)
        ]

    @property
    def matrix_data(self):
        """The full precision matrix data while y-axis are all unique mzs"""
        times_us, scan_counts, mzs_x20_int, abundance = self._raw_file_content_data
        unique_mzs = self.mass_to_charge_x20
        data = np.zeros((times_us.size, unique_mzs.size), dtype=np.uint32)
        x_index = np.repeat(np.arange(times_us.size), scan_counts)
        y_index = np.searchsorted(unique_mzs, mzs_x20_int)
        data[x_index, y_index] = abundance
        return data

    @property
    def data(self):
        """Retention time as X axis, Integer Mzs as Y axis, Abundance as Z colors"""
        retention_time = self.retention_time_us / 60000
        data = self.matrix_data

        mz_offset = round(self.mass_to_charge_x20[0].item() / 20)
        largest_mz = round(self.mass_to_charge_x20[-1].item() / 20) + 1
        abundance = np.zeros(
            (retention_time.size, largest_mz - mz_offset), dtype=np.uint32
        )
        for g, vs in groupby(
            enumerate(self.mass_to_charge_x20), lambda v: round(v[1] / 20)
        ):
            abundance[:, g - mz_offset] = data[:, [i for i, _ in vs]].sum(axis=1)

        return retention_time, np.arange(mz_offset, largest_mz), abundance

    def spectrum_at(self, rt_minutes):
        """
        Returns the real spectrum [(real_mz_float_after_divide_20, intensity),...]
        for a given retention time (in minutes).
        """
        times_us, scan_counts, mzs_x20_int, abundance = self._raw_file_content_data
        target_rt_us = int(rt_minutes * 60000)
        if (
            times_us.size == 0
            or target_rt_us < times_us[0] - 100
            or target_rt_us > times_us[-1] + 100
        ):
            raise ValueError(
                "Invalid retention time, should be in the recording range +-100ms"
            )

        closest_rt_us_index = np.argmin(np.abs(times_us - target_rt_us))
        offset = np.sum(scan_counts[:closest_rt_us_index])
        count = scan_counts[closest_rt_us_index]

        spectrum = zip(
            mzs_x20_int[offset : (offset + count)] / 20.0,
            abundance[offset : (offset + count)],
        )

        return list(spectrum)
