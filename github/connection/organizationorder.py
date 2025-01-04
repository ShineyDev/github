import enum


class OrganizationOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`organizations <github.Organization>`.
    """

    #: The date and time at which the organization was created.
    created_at = "CREATED_AT"

    #: The login of the organization.
    login = "LOGIN"


__all__ = [
    "OrganizationOrder"
]
