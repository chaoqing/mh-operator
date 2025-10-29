from typing import Any, Dict, List, Optional, Set, Tuple, TypeVar, Union, cast

import abc
import asyncio
import logging
import sys
import threading
import traceback
from collections.abc import AsyncGenerator, Awaitable, Callable, Iterable
from functools import wraps

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


# Type Vars
V = TypeVar("V")
R = TypeVar("R")
SyncFunc = Callable[[V], R]
AsyncFunc = Callable[[V], Awaitable[R]]
AnyFunc = Union[SyncFunc[V, R], AsyncFunc[V, R]]
MaybeExceptionMsg = Optional[tuple[Exception, str]]
MappedFunc = Callable[
    [Iterable[V]], AsyncGenerator[tuple[Optional[R], MaybeExceptionMsg], None]
]


def map_concurrent(max_concurrency: int) -> Callable[[AnyFunc[V, R]], MappedFunc[V, R]]:
    """
    Decorator factory: Creates a decorator that transforms a function `f(v)`
    into an async function that processes a list `f(list_v)` concurrently.

    The original function `f` can be synchronous or asynchronous.
    """

    def decorator(func: AnyFunc[V, R]) -> MappedFunc[V, R]:
        is_async_func = asyncio.iscoroutinefunction(func)

        # safe_worker is a wrapper on original function to make it concurrently runnable
        async def safe_worker(
            ith: int,
            v: V,
            semaphore: asyncio.Semaphore,
        ) -> tuple[int, R | None, MaybeExceptionMsg]:
            """
            Acquires semaphore, runs the original function (sync or async),
            and captures results or exceptions.
            """
            async with semaphore:
                try:
                    if is_async_func:
                        # If f is async, await it
                        # We cast to satisfy the type checker
                        result = await cast(AsyncFunc[V, R], func)(v)
                    else:
                        # If f is sync, run it in a thread pool
                        # to avoid blocking the event loop
                        result = await asyncio.to_thread(cast(SyncFunc[V, R], func), v)

                    return ith, result, None
                except Exception as e:
                    return (
                        ith,
                        None,
                        (
                            e,
                            f"Error when processing input {ith}: {v}, stacktrace as follow:\n{traceback.format_exc()}",
                        ),
                    )

        @wraps(func)
        async def wrapper(
            input_list: Iterable[V],
        ) -> AsyncGenerator[tuple[R | None, MaybeExceptionMsg], None]:
            """
            The new function that accepts a list and runs items concurrently.
            This replaces the original `f` to make f accept list[V] and return list[R] and exceptions dict for ith V
            """
            semaphore = asyncio.Semaphore(max_concurrency)
            tasks: list[asyncio.Task] = [
                asyncio.create_task(safe_worker(i, v, semaphore))
                for i, v in enumerate(input_list)
            ]
            if not tasks:
                return

            results_pool: dict[int, tuple[R | None, MaybeExceptionMsg]] = {}

            next_ith = 0
            for task_future in asyncio.as_completed(tasks):
                ith, result, error = await task_future
                results_pool[ith] = result, error

                while next_ith in results_pool:
                    yield results_pool.pop(next_ith)
                    next_ith += 1

        return wrapper

    return decorator
