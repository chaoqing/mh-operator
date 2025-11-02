import os
import struct
from collections import Counter
from functools import cached_property

import numpy as np


class AgilentGCMSDataReader:
    """Read the Agilent GCMS data.ms file descripped inside [Agilent .ms File Structure](https://github.com/evanyeyeye/rainbow/blob/ab0c6501901d2dbc746d96d99339f34be1f4c822/docs/source/agilent/ms.rst)"""

    def __init__(self, file_object, prec=0):
        self._f = file_object
        self._prec = prec

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
        self._f.seek(offset)
        str_len = struct.unpack("<B", self._f.read(1))[0] * gap
        try:
            return self._f.read(str_len)[::gap].decode().strip()
        except Exception:
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

        f = self._f
        short_unpack = struct.Struct(">H").unpack
        int_unpack = struct.Struct(">I").unpack
        little_short_unpack = struct.Struct("<H").unpack

        data_offsets = {
            "file_type_str": 0x4,  # File type string (GC / MS Data File)
            "file_header_length_shorts": 0x10A,  # File header length (in shorts), Short, Big Endian
            "gc_num_times": 0x142,  # Number of retention times (GC-MS), Short, Little Endian
        }

        # Validate file header.
        f.seek(0)
        head_validation = int_unpack(f.read(4))[0]
        if head_validation != 0x01320000:
            return None

        # Determine the type of .ms file based on header.
        type_ms_str = self._read_string(data_offsets["file_type_str"], 1)
        if type_ms_str != "GC / MS Data File":
            return None

        # Read the number of retention times from GC-MS specific offset.
        f.seek(data_offsets["gc_num_times"])
        num_times = little_short_unpack(f.read(2))[0]

        # Go to the data start offset.
        f.seek(data_offsets["file_header_length_shorts"])
        file_header_length_shorts = short_unpack(f.read(2))[0]
        # The data body starts after the file header.
        # The original code seeks to (file_header_length_shorts * 2 - 2)
        # This is to position the file pointer at the beginning of the first data segment.
        f.seek(file_header_length_shorts * 2 - 2)

        times_us = np.empty(num_times, dtype=np.uint32)
        pair_counts = np.zeros(num_times, dtype=np.uint16)
        pair_bytearr = bytearray()

        for i in range(num_times):
            f.read(2)
            times_us[i] = int_unpack(f.read(4))[0]
            f.read(6)
            pair_counts[i] = short_unpack(f.read(2))[0]
            f.read(4)

            pair_bytes = f.read(pair_counts[i] * 4)
            pair_bytearr.extend(pair_bytes)

            f.read(10)

        return {
            "times_us": times_us,
            "pair_counts": pair_counts,
            "pair_bytearr": pair_bytearr,
            "num_times": num_times,
        }

    @cached_property
    def meta_data(self):
        raw_content = self._raw_file_content_data
        if raw_content is None:
            return {}

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

        null_byte_metadata = self._read_header(
            {
                "unknown_1c0": metadata_offsets["unknown_1c0"],
                "unknown_268": metadata_offsets["unknown_268"],
                "method_466": metadata_offsets["method_466"],
                "unknown_664": metadata_offsets["unknown_664"],
                "unknown_862": metadata_offsets["unknown_862"],
            },
            gap=2,
        )
        metadata.update(null_byte_metadata)
        return metadata

    @cached_property
    def retention_time_us(self):
        raw_content = self._raw_file_content_data
        if raw_content is None:
            return np.array([], dtype=np.uint32)
        return raw_content["times_us"]

    @cached_property
    def raw_datas(self):
        raw_content = self._raw_file_content_data
        if raw_content is None:
            return []

        times_us = raw_content["times_us"]
        pair_counts = raw_content["pair_counts"]
        pair_bytearr = raw_content["pair_bytearr"]
        num_times = raw_content["num_times"]

        raw_bytes = bytes(pair_bytearr)
        total_paircount = np.sum(pair_counts)

        if total_paircount == 0:
            return []

        mzs_raw_int = np.ndarray(total_paircount, ">H", raw_bytes, 0, 4)
        int_encs = np.ndarray(total_paircount, ">H", raw_bytes, 2, 4)
        int_heads = int_encs >> 14
        int_tails = int_encs & 0x3FFF
        int_values = np.multiply(8**int_heads, int_tails, dtype=np.uint32)

        raw_datas_list = []
        cur_pair_index = np.uint32(0)  # Use numpy uint32 to prevent overflow warnings
        for i in range(num_times):
            current_rt_us = times_us[i]
            current_pair_count = pair_counts[i]
            current_spectrum_data = []
            for j in range(current_pair_count):
                # Ensure these are treated as numpy types to avoid scalar overflow warnings
                mz_in_times_20_integer = mzs_raw_int[
                    cur_pair_index + j
                ].item()  # .item() converts to Python scalar
                intensity = int_values[
                    cur_pair_index + j
                ].item()  # .item() converts to Python scalar
                current_spectrum_data.append((mz_in_times_20_integer, intensity))
            raw_datas_list.append(
                (current_rt_us.item(), current_spectrum_data)
            )  # .item() for rt_us as well
            cur_pair_index += current_pair_count

        return raw_datas_list

    def get_real_spectrum(self, rt_minutes):
        """
        Returns the real spectrum [(real_mz_float_after_divide_20, intensity),...]
        for a given retention time (in minutes).
        """
        times_us = self.retention_time_us
        target_rt_us = int(rt_minutes * 60000)

        if times_us.size == 0:
            return []

        closest_rt_us_index = np.argmin(np.abs(times_us - target_rt_us))
        closest_rt_us = times_us[closest_rt_us_index]

        spectrum_data = None
        for rt_us, data_list in self.raw_datas:
            if rt_us == closest_rt_us:
                spectrum_data = data_list
                break

        if spectrum_data is None:
            return []

        real_spectrum = []
        for mz_in_times_20_integer, intensity in spectrum_data:
            real_mz_float = round(mz_in_times_20_integer / 20, self._prec)
            real_spectrum.append((real_mz_float, intensity))

        return real_spectrum
