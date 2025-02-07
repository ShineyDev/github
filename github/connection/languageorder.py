from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    LanguageOrderData: TypeAlias = Literal["SIZE"]


class LanguageOrder(enum.Enum):
    """
    Represents fields by which you can order
    :class:`languages <github.Language>`.
    """

    #: The total size of files in the language.
    #:
    #: :meta hide-value:
    size = "SIZE"


__all__ = [
    "LanguageOrder",
]
