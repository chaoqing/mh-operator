# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    generators,
    nested_scopes,
    print_function,
    unicode_literals,
    with_statement,
)

import functools
import logging
import os
import sys
from itertools import chain, islice

__DEFAULT_MH_BIN_DIR__ = os.path.join(
    "C:\\", "Program Files", "Agilent", "MassHunter", "Workstation", "Quant", "bin"
)


def get_version():
    # type: () -> str
    return "{}.{}.{}".format(
        sys.version_info.major, sys.version_info.minor, sys.version_info.micro
    )


def get_argv():
    # type: () -> list
    prefix = "MH_CONSOLE_ARGS_"
    return [
        v
        for _, v in sorted(
            (int(k[len(prefix) :]), v)
            for k, v in os.environ.items()
            if k.startswith(prefix)
        )
    ]


def is_main(file_path):
    # type: (str) -> bool
    return os.path.abspath(os.environ.get("MH_CONSOLE_ARGS_0", "")) == os.path.abspath(
        file_path
    )


def field_decorator(index, **kwargs):
    # type: (int, dict) -> callable
    """
    Decorator to mark a method as a getter for a mutable record field
    and associate it with a specific index.
    """
    assert index >= 0, "The index must be positive integer"

    def decorator(func):
        # type: (callable) -> callable
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # store the field index into the wrapper
        wrapper.field_index = index
        if kwargs:
            wrapper.field_attrs = kwargs
        return wrapper

    return decorator


def add_metaclass(meta_type):
    # type: (type) -> callable
    """
    six.add_metaclass fallback
    """
    if sys.version_info.major == 2:
        return lambda t: t
    else:
        import six

        return six.add_metaclass(meta_type)


if sys.version_info.major == 2:
    # A dummy threading for IronPython2
    class _threading:
        class Lock:
            def __enter__(_):
                pass

            def __exit__(_, *__):
                pass

    threading = _threading()
else:
    import threading


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


@add_metaclass(SingletonMeta)
class Logger(logging.Logger):
    __metaclass__ = SingletonMeta

    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(fmt="[%(levelname)s]%(name)s: %(message)s")
        )
        self.addHandler(handler)


def get_logger():
    # type: () -> Logger
    return Logger("mh-operator-legacy")


logger = get_logger()


@add_metaclass(SingletonMeta)
class GlobalState(object):
    __metaclass__ = SingletonMeta  # this is for python2

    def __init__(self):
        self.state = {}

    @property
    def LibraryAccess(self):
        return self.state["libacc"]

    @LibraryAccess.setter
    def LibraryAccess(self, obj):
        self.state["libacc"] = obj

    @property
    def UADataAccess(self):
        return self.state["uadacc"]

    @UADataAccess.setter
    def UADataAccess(self, obj):
        self.state["uadacc"] = obj


global_state = GlobalState()


class _RowData:
    _fields = []
    _values = []


class RowMeta(type):
    def __new__(cls, name, bases, dct):
        # type: (str, tuple, dict) -> type
        """
        Metaclass to automatically register fields defined with @field_decorator
        and create standard properties for them.
        """
        fields_list = [None for _, v in dct.items() if hasattr(v, "field_index")]

        new_dct = {}

        for attr_name, value in dct.items():
            if hasattr(value, "field_index"):
                index = value.field_index
                assert index < len(fields_list), "There must be skipped field index"
                fields_list[index] = attr_name

                def create_setter(idx):
                    def setter(self, value):
                        # type: (_RowData, object) -> None
                        self._values[idx] = value

                    return setter

                new_dct[attr_name] = property(value, create_setter(index))
            else:
                new_dct[attr_name] = value

        new_dct["_fields"] = tuple(fields_list)

        return super(RowMeta, cls).__new__(cls, name, bases, new_dct)


@add_metaclass(RowMeta)
class RowBase(object):
    """
    Base class for mutable record types, using RecordMeta.
    """

    __metaclass__ = RowMeta  # this is for python2
    _fields = []  # _fields is populated by the metaclass

    def __init__(self, *args, **kwargs):
        """
        Initializes the MutableRecord instance.

        Args:
            *args: Initial values for the fields in order.
            **kwargs: Initial key-values for the fields in order.
        """
        if kwargs:  # key-value init
            assert not args, "Should not mix positional and key=value format initialize"
            self._values = [kwargs.pop(k, None) for k in self._fields]
            assert not kwargs, "Unrecognize fileds {}".format(kwargs.keys())
        elif not args:  # default init
            self._values = [None] * len(self._fields)
        elif len(args) == len(self._fields) and len(args) > 1:  # tuple like init
            self._values = list(args)
        else:  # dict like init
            (arg,) = args  # must be length one or raise error
            self._values = [arg[k] for k in self._fields]

    def __len__(self):
        """Returns the number of fields."""
        return len(self._fields)

    def __iter__(self):
        """Iterates over the values like tuple."""
        return iter(self._values)

    def keys(self):
        """Works like dict keys but return iterater."""
        return iter(self._fields)

    def values(self):
        """Works like dict values but return iterater."""
        return iter(self._values)

    def items(self):
        """Iterates over (name, value) pairs."""
        for name in self._fields:
            yield (name, getattr(self, name))

    def __item__(self, index):
        """Works like dict if index is str, otherwise like tuple"""
        return self._values[
            self._fields.index(index) if isinstance(index, str) else index
        ]

    def __repr__(self):
        """Returns a string representation of the object."""
        return "<{name}: {body}{rest}>".format(
            name=type(self).__name__,
            body=" ".join(islice(("{}='{}'".format(k, v) for k, v in self.items()), 5)),
            rest=" ... " if len(self) > 5 else "",
        )


@add_metaclass(SingletonMeta)
class _DataTableBase(object):
    def __getitem__(self, row_type):
        # type: (type) -> type | _DataTableBase

        def init(obj, *args):
            assert len(args) <= 1
            obj._values = [obj.RowType(r) for r in (args[0] if args else [])]

        def getitem(obj, index):
            return obj._values[index]

        attrs = {
            k: v
            for k, v in type(self).__dict__.items()
            if not k.startswith("__")
            or k
            in (
                "__doc__",
                "__len__",
                "__iter__",
                "__repr__",
            )
        }
        attrs.update(
            __init__=init,
            __getitem__=getitem,
            RowType=row_type,
        )

        return type(
            str("{}_{}".format(type(self).__name__, row_type.__name__)),
            type(self).__bases__,
            attrs,
        )

    # Following should never be called from _DataTableBase because they will be passed to real base type
    RowType = RowBase
    _values = []  # type: list[RowBase]

    def __len__(self):
        # type: () -> int
        return len(self._values)

    def __iter__(self):
        # type: () -> iter
        return iter(self._values)

    def __repr__(self):
        # type: () -> str
        return "<{}: {} rows of {}>".format(
            type(self).__name__, len(self._values), self.RowType.__name__
        )

    def append(self, *args, **kwargs):
        return self._values.append(self.RowType(*args, **kwargs))


DataTableBase = _DataTableBase()


class DataTablesBase(object):
    def __init__(self):
        self.tables = {}

    def to_json(self):
        # type: () -> str
        import json

        class fallback_encoder(json.JSONEncoder):
            def default(self, obj):
                try:
                    return super(fallback_encoder, self).default(obj)
                except TypeError:
                    return str(obj)

        return json.dumps(
            self.tables, sort_keys=True, cls=fallback_encoder, ensure_ascii=False
        )


def table_property(table_class):
    # type: (type) -> callable
    fields = table_class.RowType._fields

    def decorator(func):
        # type: (callable) -> object
        """
        Decorator to mark a method as a getter for a data table
        """

        @functools.wraps(func)
        def getter(self):
            # type: (DataTablesBase) -> dict
            return self.tables[func.__name__]

        def setter(self, obj):
            # type: (DataTablesBase, list) -> None
            import ast

            def type_map(o):
                if type(o) is bool:
                    # .Net Bool converted to "True/False" which is invalid json
                    return o == True
                if type(o) is not str and str(o) == "":
                    # Pyton2.7 unicode string may introduce error when `str(o)`
                    return None
                return o

            values = zip(
                *[
                    tuple(type_map(r[c]) for c in fields)
                    for r in chain.from_iterable(obj)
                ]
            )

            self.tables[func.__name__] = {k: v for k, v in zip(fields, values)}

        return property(getter, setter)

    return decorator
