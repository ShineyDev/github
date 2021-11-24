from github import utils
from github.errors import ClientObjectMissingFieldError


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
        d_fields = utils._get_defined_repr_fields(self.__class__)

        f_fields = dict()
        for name in d_fields:
            try:
                value = getattr(self, name)
            except ClientObjectMissingFieldError:
                pass
            else:
                f_fields[name] = value

        if f_fields:
            m_fields = " ".join(f"{name}={value!r}" for (name, value) in f_fields.items())
            return f"<{self.__class__.__name__} {m_fields}>"
        else:
            return f"<{self.__class__.__name__}>"

    def _get(self, name):
        return self._data[name]

    def _try_get(self, name):
        try:
            return self._get(name)
        except KeyError as e:
            raise ClientObjectMissingFieldError(name) from None

    _graphql_fields = [
        "__typename",
    ]


__all__ = [
    "Type",
]
