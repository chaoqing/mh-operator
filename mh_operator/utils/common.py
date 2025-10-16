from typing import Optional

import abc
import logging
import sys
import threading

from ..legacy.common import SingletonMeta


class SingletonABCMeta(SingletonMeta, abc.ABCMeta):
    pass


class BaseSingletonMeta(abc.ABCMeta):
    """Singleton to make sure the base class have only one instance"""

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        assert bases, f"{name} must have at least one base class defined"
        new_class._base_class, *_ = bases
        new_class._instance = None
        new_class._lock = threading.Lock()
        return new_class

    def __call__(cls, target_class: type | None = None, *args, **kwargs):
        # use double check lock to make sure thread safety
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    if target_class is None:
                        target_class = cls._base_class
                    assert issubclass(target_class, cls._base_class)
                    cls._instance = target_class(*args, **kwargs)

        return cls._instance


class PackageLogger(metaclass=SingletonMeta):
    _logger: logging.Logger

    def __init__(self, name="mh-operator", level=logging.INFO):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        handler = logging.StreamHandler(sys.stdout)
        log_format = "%(levelname)-8s %(name)s:%(lineno)d %(message)s"
        if hasattr(sys.stdout, "isatty") and sys.stdout.isatty():
            try:
                import colorlog

                formatter = colorlog.ColoredFormatter(
                    "%(log_color)s" + log_format,
                    log_colors={
                        "DEBUG": "cyan",
                        "INFO": "green",
                        "WARNING": "yellow",
                        "ERROR": "red",
                        "CRITICAL": "bold_red",
                    },
                    reset=True,
                    style="%",
                )
            except ImportError:
                formatter = logging.Formatter(log_format, style="%")
        else:
            formatter = logging.Formatter(log_format, style="%")

        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.propagate = False

    def get_logger(self):
        return self._logger

    def set_level(self, level: str):
        self._logger.setLevel(level.upper())


def get_logger():
    return PackageLogger().get_logger()


logger = get_logger()


def set_logger_level(level):
    PackageLogger().set_level(level)
