import asyncio
import os
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from mh_operator.core.config import settings
from mh_operator.core.mcp_client import analysis_example, zip_and_upload
from mh_operator.core.mcp_server import extract_files_to_temp
from mh_operator.utils.common import logger


@pytest.mark.skipif(
    os.environ.get("SERVER_IS_RUNNING", None) is None,
    reason="not run until CI launched the server",
)
def test_fs():
    http_uri = settings.mcp_server_url or "http://127.0.0.1:3000"

    res = zip_and_upload(Path(__file__).parent, f"{http_uri}/file/tests.zip")
    assert res.startswith(b'{"status":"ok","key":"')

    import fs.opener
    from fs import open_fs

    ftp_uri = settings.ftp_uri or "ftp://mh:operator@127.0.0.1:3021/"

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
def test_analysis_example():
    test_d = Path(__file__).with_name("data") / "yellow.D"
    if not test_d.exists():
        return
    res = analysis_example(test_d)
    Path(test_d.with_suffix(".json")).write_text(res)
