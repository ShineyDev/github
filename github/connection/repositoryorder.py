import enum


class RepositoryOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`repositories <github.Repository>`.
    """

    #: The date and time at which the repository was created.
    created_at = "CREATED_AT"

    #: The name of the repository.
    name = "NAME"

    #: The date and time at which the repository was last pushed.
    pushed_at = "PUSHED_AT"

    #: The number of stars on the repository.
    stargazer_count = "STARGAZERS"

    #: The date and time at which the repository was last updated.
    updated_at = "UPDATED_AT"


__all__ = [
    "RepositoryOrder"
]
