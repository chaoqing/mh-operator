from typing import Any, Dict, Optional

from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator
from datetime import datetime
from io import BytesIO
from pathlib import Path

import aioftp
from cachetools import TTLCache
from pydantic import Field
from pydantic.dataclasses import dataclass

from mh_operator.utils.common import SingletonABCMeta


async def async_read_bytes(path: Path, chunk: int = -1) -> AsyncGenerator[bytes, None]:
    async def read_in_chunks():
        with path.open("rb") as f:
            while data := f.read(chunk):
                yield data

    yield read_in_chunks()


class StorageBackend(ABC):
    @abstractmethod
    async def get(self, key: str) -> AsyncGenerator[bytes, None]:
        yield b""

    @abstractmethod
    async def put(self, key: str, data_stream: AsyncGenerator[bytes, None]) -> None:
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        pass

    @abstractmethod
    async def head(self, key: str) -> dict[str, Any]:
        pass


@dataclass
class InMemoryFileObject:
    data: bytes
    last_modified: datetime = Field(default_factory=datetime.utcnow)

    @property
    def size(self) -> int:
        return len(self.data)


class InMemoryStorage(StorageBackend):
    def __init__(self, max_size_mb: int = 100, ttl_seconds: int = 3600, **_):
        super().__init__()
        max_size_bytes = max_size_mb * 1024 * 1024
        self._storage = TTLCache(
            maxsize=max_size_bytes,
            ttl=ttl_seconds,
            getsizeof=lambda value: value.size,
        )

    def ensure_exist(self, key: str):
        if key not in self._storage:
            raise FileNotFoundError(f"File '{key}' not exist")

        self._storage.expire()

        if key not in self._storage:
            raise FileNotFoundError(f"File '{key}' not exist (expired)")

    def read_bytes(self, key: str) -> bytes | None:
        try:
            self.ensure_exist(key)
            return self._storage[key].data
        except FileNotFoundError:
            return None

    def write_bytes(self, key: str, data: bytes):
        self._storage[key] = InMemoryFileObject(data=data)

    async def get(self, key: str) -> AsyncGenerator[bytes, None]:
        self.ensure_exist(key)

        yield self._storage[key].data

    async def put(self, key: str, data_stream: AsyncGenerator[bytes, None]) -> None:
        with BytesIO() as fp:
            async for chunk in data_stream:
                fp.write(chunk)

            self._storage[key] = InMemoryFileObject(data=fp.getvalue())

    async def delete(self, key: str) -> None:
        if key in self._storage:
            del self._storage[key]

    async def head(self, key: str) -> dict[str, Any]:
        self.ensure_exist(key)

        item: InMemoryFileObject = self._storage[key]
        return {
            "Content-Length": str(item.size),
            "Last-Modified": item.last_modified.strftime("%Y-%m-%d %H:%M:%S"),
        }


class InMemoryFTP(aioftp.MemoryPathIO, InMemoryStorage, metaclass=SingletonABCMeta):
    def __init__(self, **kwargs):
        InMemoryStorage.__init__(self, **kwargs)
        kwargs.pop("max_size_mb", None)
        kwargs.pop("ttl_seconds", None)
        aioftp.MemoryPathIO.__init__(self, **kwargs)
