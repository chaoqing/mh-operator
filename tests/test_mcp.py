import asyncio
import json
import os
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlparse
from zipfile import ZipFile

import pytest

from mh_operator.core.config import settings
from mh_operator.core.mcp_client import analysis_examples, zip_and_upload
from mh_operator.core.mcp_server import extract_files_to_temp
from mh_operator.routines.analysis_samples import merge_uaf_tables
from mh_operator.utils.common import logger, map_concurrent, set_logger_level

set_logger_level("DEBUG")


@pytest.mark.skipif(
    os.environ.get("SERVER_IS_RUNNING", None) is None,
    reason="not run until CI launched the server",
)
def test_fs():
    http_uri = (settings.mcp_server_url or "http://127.0.0.1:3000") + "/file"
    logger.debug(f"Using MCP server at {http_uri}")

    # Test case 1: upload to mcp http
    res = zip_and_upload(
        Path(__file__).with_name("__pycache__"), f"{http_uri}/tests.zip"
    )
    logger.debug(f"Upload result: {res}")
    assert res.startswith("resource://sample/")

    ftp_uri = settings.ftp_uri or "ftp://mh:operator@127.0.0.1:3021/"
    logger.debug(f"Using FTP server at {ftp_uri}")

    import fsspec
    import httpx

    ftp_fs, _ = fsspec.url_to_fs(ftp_uri)

    # Test case 2: upload to ftp server with zip
    with ftp_fs.open("Sample.zip", "wb") as fp:
        with ZipFile(fp, "w") as zip_fp:
            zip_fp.writestr("Sample01.D/data.ms", "this is ms data")

    # Test case 3: upload to ftp server with folder
    ftp_fs.makedirs("Sample/Sample02.D/", exist_ok=True)
    with fsspec.open(f"{ftp_uri}/Sample/Sample02.D/data.ms", "w") as fp:
        fp.writelines(["this is\n", "ms data"])

    # Test case 4: download from ftp zip
    with TemporaryDirectory() as tmpdir:
        (sample,) = extract_files_to_temp(ftp_uri + "Sample.zip", tmpdir)
        logger.info(f"Extracting zip to {sample}")
        logger.info((sample / "data.ms").read_text())

    # Test case 5: download from ftp folder
    with TemporaryDirectory() as tmpdir:
        (sample,) = extract_files_to_temp(ftp_uri + "Sample", tmpdir)
        logger.info(f"Extracting folder to {sample}")
        logger.info((sample / "data.ms").read_text())

        with ftp_fs.open("tests.tar", "wb") as fp:
            from tarfile import TarFile

            with TarFile(mode="w", fileobj=fp) as tar_fp:
                tar_fp.add(sample, arcname="Sample_tar.D")

    # Test case 6: upload to mcp http tar
    with fsspec.open(f"{ftp_uri}/tests.tar", "rb") as tar_bytes:
        res = httpx.put(
            f"{http_uri}/sample_tar.tar",
            content=tar_bytes.read(),
            follow_redirects=True,
        )
        res.raise_for_status()
        logger.debug(f"Upload result: {res.text}")
        parsed_tar_url = urlparse(res.text)
        if parsed_tar_url.scheme == "resource":
            tar_url = f"{http_uri}/{Path(parsed_tar_url.path).name}"
        else:
            tar_url = f"{http_uri}/{parsed_tar_url.path}"

    # Test case 7: download from mcp http tar
    with TemporaryDirectory() as tmpdir:
        logger.debug(f"Download result from {tar_url}")
        (sample,) = extract_files_to_temp(tar_url, temp_dir=tmpdir)
        logger.info(f"Extracting folder to {sample}")
        logger.info((sample / "data.ms").read_text())


@pytest.mark.skipif(
    os.environ.get("SERVER_IS_RUNNING", None) is None,
    reason="not run until CI launched the server",
)
def test_analysis_examples():
    test_d = (
        Path(__file__).with_name("data")
        / "NIST Public Data Repository (Rapid GC-MS of Seized Drugs).zip"
    )
    import fsspec

    with TemporaryDirectory() as tmpdir:
        with ZipFile(test_d, "r") as zip_fp:
            zip_fp.extractall(tmpdir)
            logger.debug(f"Extracted {test_d} into {tmpdir}")
        tests = list(Path(tmpdir).glob("*/*.D"))[:5]

        for test, text_result, raw_result in zip(
            tests,
            analysis_examples(
                tests,
                mcp_server_url=settings.mcp_server_url or "http://127.0.0.1:3000",
                batch=2,
                raw=False,
            ),
            analysis_examples(
                tests,
                mcp_server_url=settings.mcp_server_url or "http://127.0.0.1:3000",
                batch=2,
                raw=True,
                full=True,
            ),
        ):
            test_d.with_name(test.name + ".txt").write_text(text_result)
            test_d.with_name(test.name + ".json").write_text(raw_result)

        db = test_d.with_suffix(".db")
        db.unlink(missing_ok=True)
        res = merge_uaf_tables(
            *[
                json.loads(test_d.with_name(t.name + ".json").read_text())[0]
                for t in tests
            ],
            tmp_db=db,
            b64decode=True,
        )
        logger.debug(res)


def test_map_concurrent():
    import random
    import time

    # 1. Define an ASYNCHRONOUS function (simulates I/O)
    @map_concurrent(max_concurrency=5)
    async def f_async(v: int) -> str:
        delay = random.uniform(0.1, 0.5)
        await asyncio.sleep(delay)
        if v == 3 or v == 7:
            raise ValueError(f"Async value {v} failed")
        return f"Async result {v}"

    # 2. Define a SYNCHRONOUS function (simulates blocking CPU work)
    @map_concurrent(max_concurrency=5)
    def f_sync(v: int) -> str:
        delay = random.uniform(0.1, 0.5)
        time.sleep(delay)
        if v == 2 or v == 8:
            raise RuntimeError(f"Sync value {v} failed")
        return f"Sync result {v}"

    async def main():
        my_list = list(range(10))[::-1]

        print("--- Testing decorated ASYNC function ---")
        async for ith_res, e_msg in f_async(my_list):
            if e_msg is not None:
                e, msg = e_msg
                print(f"failed: {e} {msg}")
            else:
                print(f"success: {ith_res}")

        print("\n" + "=" * 40 + "\n")

        print("--- Testing decorated SYNC function ---")
        async for ith_res, e_msg in f_sync(my_list):
            if e_msg is not None:
                e, msg = e_msg
                print(f"failed: {e} {msg}")
            else:
                print(f"success: {ith_res}")

    # Running the main async function
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
    # This total time should be much less than the sum of all delays,
    # proving both sync and async versions ran concurrently.
