from __future__ import annotations
from typing import NamedTuple

from github.core import *
from github.core import __all__ as _core__all__
from github.interfaces import *
from github.interfaces import __all__ as _interfaces__all__
from github.connection import *
from github.connection import __all__ as _connection__all__
from github.connections import *
from github.connections import __all__ as _connections__all__
from github.content import *
from github.content import __all__ as _content__all__
from github.organization import *
from github.organization import __all__ as _organization__all__
from github.repository import *
from github.repository import __all__ as _repository__all__
from github.user import *
from github.user import __all__ as _user__all__
from github import utility


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    micro: int
    release: str
    serial: int


version: str = "1.0.0.0a"
version_info: _VersionInfo = _VersionInfo(1, 0, 0, 0, "alpha", 0)


__all__: list[str] = [  # type: ignore[reportUnsupportedDunderAll]
    *_core__all__,
    *_interfaces__all__,
    *_connection__all__,
    *_connections__all__,
    *_content__all__,
    *_organization__all__,
    *_repository__all__,
    *_user__all__,
    "utility",
    "version",
    "version_info",
]
