from typing import NamedTuple

from github.client import *
from github.errors import *


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
