import collections

from github.errors import *
from github.errors import __all__ as _errors__all__


__all__ = [
    *_errors__all__,
]


_VersionInfo = collections.namedtuple("_VersionInfo", "prime major minor micro release serial")

version = "1.0.0.0a"
version_info = _VersionInfo(1, 0, 0, 0, "alpha", 0)
