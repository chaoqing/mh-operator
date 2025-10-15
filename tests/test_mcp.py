import asyncio
import os
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from mcp.types import TextContent

from mh_operator.core.config import settings
from mh_operator.core.mcp_client import MCPClient, zip_and_upload
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


def test_mcp_client():
    async def main():
        MCP_SERVER_URL = "https://mcp.context7.com/mcp"
        client = MCPClient()

        async def search_doc(session):
            response = await session.call_tool(
                "resolve-library-id", {"libraryName": "context7"}
            )
            assert not response.isError

            (text_content,) = response.content
            assert isinstance(text_content, TextContent)
            logger.debug(text_content.text)
            import random

            library_id = random.choice(
                [
                    l.split(": ", maxsplit=1)[-1]
                    for l in text_content.text.split("\n")
                    if l.startswith("- Context7-compatible library ID: ")
                ]
            )

            logger.info(f"Searching {library_id}\n")

            response = await session.call_tool(
                "get-library-docs", {"context7CompatibleLibraryID": library_id}
            )
            assert not response.isError

            (text_content,) = response.content
            assert isinstance(text_content, TextContent)
            logger.warning(text_content.text)

        try:
            await client.connect_to_server(MCP_SERVER_URL)
            await client.list_tools()
            # await client.list_resources()
            await search_doc(client.session)
        finally:
            await client.cleanup()

    asyncio.run(main())
