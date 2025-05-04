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
from itertools import islice


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


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


@add_metaclass(SingletonMeta)
class Logger(logging.Logger):
    __metaclass__ = SingletonMeta  # this is for python2


logger = Logger("legacy")


def get_logger():
    return Logger("legacy")


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
