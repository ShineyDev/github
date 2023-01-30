import collections

from github import utilities
from github.client import *
from github.client import __all__ as _client__all__
from github.interfaces import *
from github.interfaces import __all__ as _interfaces__all__
from github.content import *
from github.content import __all__ as _content__all__
from github.metadata import *
from github.metadata import __all__ as _metadata__all__
from github.repository import *
from github.repository import __all__ as _repository__all__


__all__ = [
    "utilities",
    *_client__all__,
    *_interfaces__all__,
    *_content__all__,
    *_metadata__all__,
    *_repository__all__,
]


_VersionInfo = collections.namedtuple("_VersionInfo", "prime major minor micro release serial")

version = "1.0.0.0a"
version_info = _VersionInfo(1, 0, 0, 0, "alpha", 0)
