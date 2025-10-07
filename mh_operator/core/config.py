from typing import Optional

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from ..routines.analysis_samples import (
    __DEFAULT_MH_BIN_DIR__,
    FileOpenMode,
    ISTDOptions,
)

CONFIG_FILE = Path("~").expanduser() / ".mh_operator.config"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        nested_model_default_partial_update=True,
        env_file=(".env", CONFIG_FILE),
        env_file_encoding="utf-8",
    )

    analysis_method: Path = "Process.m"
    output: str = "batch.uaf"
    report_method: Optional[Path] = None
    istd: Optional[ISTDOptions] = None
    mode: FileOpenMode = FileOpenMode.WRITE

    mh_bin_path: Path = __DEFAULT_MH_BIN_DIR__


settings = Settings()
