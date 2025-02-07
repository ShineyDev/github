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
    #:
    #: :meta hide-value:
    internal = "INTERNAL"

    #: The repository is private.
    #:
    #: :meta hide-value:
    private = "PRIVATE"

    #: The repository is public.
    #:
    #: :meta hide-value:
    public = "PUBLIC"


__all__ = [
    "RepositoryVisibility",
]
