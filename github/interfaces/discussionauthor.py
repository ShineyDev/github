from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection, DiscussionOrder
    from github.interfaces import Node
    from github.repository import Discussion, Repository

import github
from github.utility import MISSING


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

    def fetch_discussions(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: DiscussionOrder = MISSING,
        repository: Repository = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Discussion]:
        """
        |aiter|

        Fetches discussions in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.DiscussionOrder`
            The field by which to order the elements.
        repository: :class:`~github.Repository`
            The repository to filter discussions by.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Discussion`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return github.Connection(
            self._http.collect_discussionauthor_discussions,
            self.id,
            order_by.value if order_by is not MISSING else None,
            repository.id if repository is not MISSING else None,
            data_map=lambda d: github.Discussion._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__ = [
    "DiscussionAuthor",
]
