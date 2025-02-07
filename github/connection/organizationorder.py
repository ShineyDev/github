from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    OrganizationOrderData: TypeAlias = Literal["CREATED_AT", "LOGIN"]


class OrganizationOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`organizations <github.Organization>`.
    """

    #: The date and time at which the organization was created.
    #:
    #: :meta hide-value:
    created_at = "CREATED_AT"

    #: The login of the organization.
    #:
    #: :meta hide-value:
    login = "LOGIN"


__all__ = [
    "OrganizationOrder",
]
