import enum


class IssueState(enum.Enum):
    """
    Represents the state of an :class:`~github.Issue`.
    """

    #: The issue is closed.
    closed = "CLOSED"

    #: The issue is open.
    open = "OPEN"


__all__ = [
    "IssueState"
]
