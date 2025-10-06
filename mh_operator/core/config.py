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
    model_config = SettingsConfigDict(env_file=CONFIG_FILE, env_file_encoding="utf-8")

    analysis_method: Path = "Process.m"
    output: str = "batch.uaf"
    report_method: Optional[Path] = None
    istd: Optional[ISTDOptions] = None
    mode: FileOpenMode = FileOpenMode.WRITE

    mh_bin_path: Path = __DEFAULT_MH_BIN_DIR__


def write_default_config(config_file_path: Path):
    """Writes the default configuration to the specified file."""
    config_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_file_path, "w") as f:
        f.write(Settings().model_dump_json(indent=4))


settings = Settings()
