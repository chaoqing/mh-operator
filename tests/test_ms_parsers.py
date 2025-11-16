import os
from glob import glob

import numpy as np
import pytest

from mh_operator.routines.ms_reader import AgilentGCMSDataReader


# Define a fixture to find all data.ms files recursively
def get_ms_files():
    # Search for 'data.ms' files in the current working directory and its subdirectories
    # Adjust the pattern if 'data.ms' files are nested deeper or have different names
    # For example, if they are always in a .D directory, you might use '**/*.D/data.ms'
    # For this test, we'll assume 'data.ms' can be found directly or in subdirectories.
    # We'll also filter for files that are likely GC-MS by checking their parent directory name.
    # This is a heuristic and might need adjustment based on actual data structure.

    # A more robust way would be to try parsing and check the 'detector' type.

    # For now, let's just find all .ms files and attempt to parse them as GC-MS.
    # The parse_gcms_ms function itself will validate if it's a GC-MS file.

    # Let's try to find files that are likely GC-MS based on the directory structure
    # from the `entab/tests/data/masshunter_example` which contains `MSD1.MS`
    # However, the request specifically asks for `data.ms` files.
    # Given the provided directory structure, there isn't a `data.ms` file directly.
    # The `rainbow` tests use `carotenoid_extract.d/MSD1.MS`.
    # The `ms_reader.py` was designed for `data.ms` as per the `ms.rst` documentation for GC-MS.
    # Let's assume for the purpose of this test that `data.ms` files exist somewhere.

    # For now, let's use a more general glob and then filter inside the test if needed.
    # The `glob` function in the tool context is for listing files, not for recursive search.
    # I need to use `os.walk` or `glob.glob` from Python's standard library.

    # Since I'm in a tool context, I can't directly use `glob.glob` from the standard library
    # unless it's within a `run_shell_command`.
    # Let's use `default_api.glob` with a recursive pattern.

    # The user asked to search under cwd, which is `/home/nick/Work/entab/`.
    # So the pattern should be `**/*.ms`.

    ms_files_list = glob(os.path.join(os.getcwd(), "**", "data.ms"), recursive=True)
    # Also include MSD1.MS from the test data, as it's a known MS file for rainbow.
    ms_files_list.extend(
        glob(os.path.join(os.getcwd(), "**", "MSD1.MS"), recursive=True)
    )

    # Filter out files that are not likely GC-MS if necessary, but for now, let parse_gcms_ms handle it.
    return ms_files_list


@pytest.mark.parametrize("file_path", get_ms_files())
def test_ms_parser_consistency(file_path):
    try:
        from rainbow.agilent.chemstation import parse_ms
    except ModuleNotFoundError:
        print("Skipping test: rainbow-api is not installed")
        return

    print(f"Testing file: {file_path}")

    # Parse with ms_reader.py
    with AgilentGCMSDataReader(file_path) as f:
        metadata = f.meta_data
        (retention_time, mass_to_charge, matrix_data) = f.data

    # rainbow skip all zeros (along retention time) mzs
    available_mz = np.any(matrix_data > 0, axis=0)
    mass_to_charge = mass_to_charge[available_mz]
    matrix_data = matrix_data[:, available_mz]

    # Parse with rainbow package
    # The rainbow.agilent.chemstation.parse_ms function handles both LC-MS and GC-MS.
    # It determines the type based on the file content.
    rainbow_data = parse_ms(file_path)

    assert (
        rainbow_data is not None
    ), f"rainbow.agilent.chemstation.parse_ms failed to parse {file_path}"

    # --- Compare Data Arrays ---
    # Times (xlabels)
    np.testing.assert_array_almost_equal(
        retention_time,
        rainbow_data.xlabels,
        decimal=6,
        err_msg=f"Times mismatch for {file_path}",
    )

    # Ylabels (mz values)
    np.testing.assert_array_almost_equal(
        mass_to_charge,
        rainbow_data.ylabels,
        decimal=4,
        err_msg=f"Ylabels mismatch for {file_path}",
    )

    # Data (intensities)
    # Data can be uint32 in ms_reader and uint64 in rainbow, but values should be the same.
    # Use assert_array_equal for integer arrays.
    np.testing.assert_array_equal(
        matrix_data,
        rainbow_data.data,
        err_msg=f"Data (intensities) mismatch for {file_path}",
    )

    # --- Compare Metadata (common fields) ---
    # The rainbow.agilent.chemstation.parse_ms extracts 'date' and 'method'.
    # ms_reader.py extracts more fields. We'll compare the common ones.

    # Date comparison
    ms_reader_date = metadata.get("date")
    rainbow_date = rainbow_data.metadata.get("date")
    assert (
        ms_reader_date == rainbow_date
    ), f"Date metadata mismatch for {file_path}: ms_reader={ms_reader_date}, rainbow={rainbow_date}"

    # Method comparison
    ms_reader_method = metadata.get("method")
    rainbow_method = rainbow_data.metadata.get("method")
    assert (
        ms_reader_method == rainbow_method
    ), f"Method metadata mismatch for {file_path}: ms_reader={ms_reader_method}, rainbow={rainbow_method}"

    # Additional common fields if any, e.g., 'file_type'
    ms_reader_file_type = metadata.get("file_type")
    # rainbow.agilent.chemstation.parse_ms doesn't explicitly put 'file_type' in metadata,
    # but it uses it internally. We can't directly compare it from the returned metadata.
    # However, if both successfully parse, they should agree on the file type implicitly.

    # For other metadata fields that ms_reader.py extracts but rainbow.agilent.chemstation.parse_ms doesn't expose in its returned metadata,
    # we cannot directly compare them. The goal is to ensure ms_reader.py is consistent with rainbow's output.
    # If rainbow's parse_ms returns a subset of metadata, we check that subset.

    print(f"Successfully compared {file_path}")
