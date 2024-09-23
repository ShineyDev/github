from __future__ import annotations
from typing import TYPE_CHECKING

import enum


class StargazerOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`stargazers <github.User>`.
    """

    #: The date and time at which the stargazer starred the starrable.
    starred_at = "STARRED_AT"


__all__ = [
    "StargazerOrder"
]
