from typing import NamedTuple


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
