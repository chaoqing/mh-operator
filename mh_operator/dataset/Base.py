class RowBase(object):
    __slots__ = []

    def __init__(self, *args, **kwargs):
        pass


class TableBase(object):
    __slots__ = ("rows",)

    def __init__(self, *args, **kwargs):
        pass
