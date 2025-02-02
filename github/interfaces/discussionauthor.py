from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    from github.repository.discussion import DiscussionData


    class DiscussionAuthorData(TypedDict):
        # repositoryDiscussionComments  # TODO
        repositoryDiscussions: ConnectionData[DiscussionData]


class DiscussionAuthor:
    """
    Represents an object that can author a :class:`~github.Discussion`.
    """

    __slots__ = ()

    _data: DiscussionAuthorData


__all__ = [
    "DiscussionAuthor",
]
