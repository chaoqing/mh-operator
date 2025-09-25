from typing import Protocol, Union, runtime_checkable

import enum

from pydantic import BaseModel

from mh_operator.utils.union_model_types import basemodel_with_typeinfo


class FileBase(BaseModel):
    file_name: str


class OSFile(FileBase):
    path: str


class OSSFile(FileBase):
    oss_type: str
    uuid: str


class FileSource(enum.Enum):
    OS = "local os file"
    OSS = "object storage service file"


@runtime_checkable
class UnionModelBaseProtocol(Protocol):
    type_info: FileSource
    data: OSFile | OSSFile


@basemodel_with_typeinfo(
    {
        FileSource.OS: OSFile,
        FileSource.OSS: OSSFile,
    }
)
class FileInfo(BaseModel):
    pass


def test_pydantic_union_types():
    # Mypy will understand this correctly if the plugin is enabled!
    event = FileInfo(
        type_info=FileSource.OS, data=OSFile(file_name="os.py", path="Works!")
    )
    assert isinstance(event, UnionModelBaseProtocol)
    print(event.model_dump_json(indent=2))
    print(FileInfo.model_validate_json(event.model_dump_json(indent=2)).data.path)

    event = FileInfo(
        type_info=FileSource.OSS,
        data=OSSFile(
            oss_type="xyz",
            uuid="xxx",
            file_name="",
            comment="Extra field will be ignored",
        ),
    )
    assert isinstance(event, UnionModelBaseProtocol)
    print(event.model_dump_json())
    print(
        FileInfo.model_validate_json(
            '{"type_info":"object storage service file","data":{"oss_type":"s3", "file_name": "os.py", "uuid": "Works!"}}'
        ).data
    )
