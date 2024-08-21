from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class _MissingSentinel:
    __slots__ = ()

    def __repr__(self) -> str:
        return "..."

    def __bool__(self) -> bool:
        return False


MISSING: Any = _MissingSentinel()
"""
TODO
"""


__all__ = [
    "MISSING",
]
