from __future__ import annotations

import enum


class ReferenceType(enum.Enum):
    """
    Represents the type of a :class:`reference <github.Reference>`.
    """

    #: The tree entry is a directory.
    head = "refs/heads/"
    branch = "refs/heads/"

    #: The tree entry is a normal file.
    tag = "refs/tags/"


__all__ = [
    "ReferenceType",
]
