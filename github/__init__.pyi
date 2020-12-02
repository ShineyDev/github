from typing import NamedTuple

from github.client import Client as Client
from github.objects import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

version_info: VersionInfo = ...
version: str = ...
