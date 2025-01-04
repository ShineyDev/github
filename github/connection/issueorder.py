import enum


class IssueOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`issues <github.Issue>`.
    """

    #: The number of comments on the issue.
    comment_count = "COMMENTS"

    #: The date and time at which the issue was created.
    created_at = "CREATED_AT"

    #: The date and time at which the issue was last updated.
    updated_at = "UPDATED_AT"


__all__ = [
    "IssueOrder"
]
