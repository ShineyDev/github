from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


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

    async def fetch_discussion_comments(
        self: Self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches discussion comments from the discussion author.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[DiscussionComment]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.DiscussionComment`]
        """

        raise NotImplementedError  # TODO: RepositoryDiscussionCommentAuthor.repositoryDiscussionComments

    async def fetch_discussions(
        self: Self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches discussions from the discussion author.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Discussion]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Discussion`]
        """

        raise NotImplementedError  # TODO: RepositoryDiscussionAuthor.repositoryDiscussions


__all__: list[str] = [
    "DiscussionAuthor",
]
