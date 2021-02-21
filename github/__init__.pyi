from typing import NamedTuple

from github.client import Client as Client
from github.enums import *
from github.objects import *


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    patch: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
