class Type:
    __slots__ = ()

    def __new__(cls, data, http=None):
        if isinstance(data, list):
            return [cls(o, http) for o in data]

        return super().__new__(cls)

    def __init__(self, data, http=None):
        self._data = data

        if http is not None:
            self._http = http

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


__all__ = [
    "Type",
]
