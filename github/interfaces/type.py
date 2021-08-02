from github.errors import ClientError


class Type:
    __slots__ = ("_data", "_http")

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

    def _get(self, name):
        return self._data[name]

    def _try_get(self, name):
        try:
            return self._get(name)
        except KeyError as e:
            raise ClientError(f"missing field '{name}'") from None

    _fields = {
        "__typename": "__typename",
    }


__all__ = [
    "Type",
]
