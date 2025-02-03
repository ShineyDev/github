from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    RepositoryVisibilityData: TypeAlias = Literal["INTERNAL", "PRIVATE", "PUBLIC"]


class RepositoryVisibility(enum.Enum):
    """
    Represents the visibility of a
    :class:`repository <github.Repository>`.
    """

    #: The repository is internal.
    internal = "INTERNAL"

    #: The repository is private.
    private = "PRIVATE"

    #: The repository is public.
    public = "PUBLIC"


__all__ = [
    "RepositoryVisibility",
]
