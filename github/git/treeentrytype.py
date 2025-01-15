from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    TreeEntryTypeData: TypeAlias = Literal["blob", "tree"]


class TreeEntryType(enum.Enum):
    """
    Represents the type of a :class:`tree entry <github.TreeEntry>`.
    """

    #: The tree entry is a :class:`~github.Blob`.
    blob = "blob"

    #: The tree entry is a :class:`~github.Tree`.
    tree = "tree"


__all__ = [
    "TreeEntryType"
]
