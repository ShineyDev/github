from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    TreeEntryModeData: TypeAlias = Literal[16384, 33188, 33261, 40960, 57344]


class TreeEntryMode(enum.Enum):
    """
    Represents the mode of a :class:`tree entry <github.TreeEntry>`.
    """

    #: The tree entry is a directory.
    #:
    #: :meta hide-value:
    directory = 16384

    #: The tree entry is a normal file.
    #:
    #: :meta hide-value:
    file_normal = 33188

    #: The tree entry is an executable file.
    #:
    #: :meta hide-value:
    file_executable = 33261

    #: The tree entry is a symbolic link.
    #:
    #: :meta hide-value:
    symlink = 40960

    #: The tree entry is a submodule.
    #:
    #: :meta hide-value:
    submodule = 57344


__all__ = [
    "TreeEntryMode",
]
