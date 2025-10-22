import asyncio
import json
import os
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from fs.copy import copy_fs
from fs.opener import open_fs
from fs.zipfs import ZipFS

from mh_operator.core.config import settings
from mh_operator.core.mcp_client import analysis_examples, zip_and_upload
from mh_operator.core.mcp_server import extract_files_to_temp
from mh_operator.routines.analysis_samples import merge_uaf_tables
from mh_operator.utils.common import logger, set_logger_level

set_logger_level("DEBUG")


@pytest.mark.skipif(
    os.environ.get("SERVER_IS_RUNNING", None) is None,
    reason="not run until CI launched the server",
)
def test_fs():
    http_uri = settings.mcp_server_url or "http://127.0.0.1:3000"
    logger.debug(f"Using MCP server at {http_uri}")

    res = zip_and_upload(Path(__file__).parent, f"{http_uri}/file/tests.zip")
    logger.debug(f"Upload result: {res}")
    assert res.startswith(b'{"status":"ok","uri":"resource://sample/')

    import fs.opener
    from fs import open_fs

    ftp_uri = settings.ftp_uri or "ftp://mh:operator@127.0.0.1:3021/"
    logger.debug(f"Using FTP server at {ftp_uri}")

    fs = open_fs(ftp_uri)

    with fs.open("Sample.zip", "wb") as fp:
        zip_file = BytesIO()
        from zipfile import ZipFile

        with ZipFile(zip_file, "w") as zip_fp:
            zip_fp.writestr("Sample01.D/data.ms", "this is ms data")

        fp.write(zip_file.getvalue())

    fs.makedirs("Sample/Sample02.D/", recreate=True)
    with fs.open("Sample/Sample02.D/data.ms", "w") as fp:
        fp.writelines(["this is\n", "ms data"])

    with TemporaryDirectory() as tmpdir:
        (sample,) = extract_files_to_temp(ftp_uri + "Sample.zip", tmpdir)
        logger.info(f"Extracting zip to {sample}")
        logger.info((sample / "data.ms").read_text())
    with TemporaryDirectory() as tmpdir:
        (sample,) = extract_files_to_temp(ftp_uri + "Sample", tmpdir)
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
    with TemporaryDirectory() as tmpdir:
        copy_fs(ZipFS(str(test_d)), open_fs(tmpdir))
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
            ),
        ):
            test_d.with_name(test.name + ".txt").write_text(text_result)
            test_d.with_name(test.name + ".json").write_text(raw_result)

        db = test_d.with_suffix(".db")
        db.unlink(missing_ok=True)
        res = merge_uaf_tables(
            *[
                json.loads(test_d.with_name(t.name + ".json").read_text())
                for t in tests
            ],
            tmp_db=db,
            b64decode=True,
        )
        logger.debug(res)
