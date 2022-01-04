from typing import NamedTuple

from github import utils as utils
from github.client import *
from github.errors import *
from github.interfaces import *
from github.content import *
from github.metadata import *
from github.repository import *


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
