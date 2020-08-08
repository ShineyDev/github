from typing import List, NamedTuple

from github.client import Client as Client
from github.objects import *

__all__: List[str] = ...
__version__: str = ...

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

version_info: VersionInfo = ...
