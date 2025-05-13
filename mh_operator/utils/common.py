import logging
import sys

from ..legacy.common import SingletonMeta


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
