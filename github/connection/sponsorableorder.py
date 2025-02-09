from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    SponsorableOrderData: TypeAlias = Literal["LOGIN"]


class SponsorableOrder(enum.Enum):
    """
    Represents fields by which you can order sponsorable
    :class:`organizations <github.Organization>` and
    :class:`users <github.User>`.
    """

    #: The login of the sponsorable.
    #:
    #: :meta hide-value:
    login = "LOGIN"


__all__ = [
    "SponsorableOrder",
]
