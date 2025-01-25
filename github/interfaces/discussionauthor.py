from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict


    class DiscussionAuthorData(TypedDict):
        # repositoryDiscussionComments: ConnectionData[DiscussionCommentData]  # TODO: [support-discussions]
        # repositoryDiscussions: ConnectionData[DiscussionData]  # TODO: [support-discussions]
        pass


class DiscussionAuthor:
    """
    Represents an object that can author a Discussion.

    ..                                     :class:`~github.Discussion`
    """

    __slots__ = ()

    _data: DiscussionAuthorData

    async def fetch_discussion_comments(
        self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches discussion comments from the discussion author.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[DiscussionComment]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.DiscussionComment`]
        """

        raise NotImplementedError  # TODO: RepositoryDiscussionCommentAuthor.repositoryDiscussionComments

    async def fetch_discussions(
        self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches discussions from the discussion author.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Discussion]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Discussion`]
        """

        raise NotImplementedError  # TODO: RepositoryDiscussionAuthor.repositoryDiscussions


__all__ = [
    "DiscussionAuthor",
]
