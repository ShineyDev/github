from __future__ import annotations

import enum


class ReferenceType(enum.Enum):
    """
    Represents the type of a :class:`reference <github.Reference>`.
    """

    #: The tree entry is a directory.
    #:
    #: :meta hide-value:
    head = branch = "refs/heads/"

    #: The tree entry is a normal file.
    #:
    #: :meta hide-value:
    tag = "refs/tags/"


__all__ = [
    "ReferenceType",
]
