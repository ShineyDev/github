from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    RepositoryPrivacyData: TypeAlias = Literal["PRIVATE", "PUBLIC"]


class RepositoryPrivacy(enum.Enum):
    """
    Represents the privacy of a
    :class:`repository <github.Repository>`.
    """

    #: The repository is private.
    private = "PRIVATE"

    #: The repository is public.
    public = "PUBLIC"


__all__ = [
    "RepositoryPrivacy",
]
