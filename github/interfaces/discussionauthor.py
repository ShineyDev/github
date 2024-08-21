from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict

    # from github.repository.discussion import Discussion  # TODO: [support-discussions]
    # from github.repository.discussioncomment import DiscussionComment  # TODO: [support-discussions]
    from github.utility.types import ConnectionData


    class OptionalDiscussionAuthorData(TypedDict, total=False):
        # repositoryDiscussionComments: ConnectionData[DiscussionComment]  # TODO: [support-discussions]
        # repositoryDiscussions: ConnectionData[Discussion]  # TODO: [support-discussions]
        pass


    class DiscussionAuthorData(OptionalDiscussionAuthorData):
        pass


class DiscussionAuthor:
    """
    Represents an object that can author a Discussion.

    ..                                     :class:`~github.Discussion`
    """

    __slots__ = ()

    _data: DiscussionAuthorData


__all__: list[str] = [
    "DiscussionAuthor",
]
