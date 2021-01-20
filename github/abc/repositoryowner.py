"""
/github/abc/repositoryowner.py

    Copyright (c) 2019-2020 ShineyDev

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from github.iterator import CollectionIterator


class RepositoryOwner():
    """
    Represents the owner of one or more GitHub repositories.
    """

    __slots__ = ()

    async def fetch_repository(self, name):
        """
        |coro|

        Fetches a repository from the repository owner.

        Parameters
        ----------
        name: :class:`str`
            The repository name.

        Returns
        -------
        :class:`github.Repository`
            The repository.
        """

        from github.objects import Repository

        data = await self.http.fetch_repositoryowner_repository(self.id, name)
        return Repository.from_data(data, self.http)

    def fetch_repositories(self, *, is_fork=None, is_locked=None, order_by=None, owner_affiliations=None, privacy=None, viewer_affiliations=None, **kwargs):
        """
        |aiter|

        Fetches repositories from the repository owner.

        Parameters
        ----------
        is_fork: Optional[:class:`bool`]
            The fork state to filter by.
        is_locked: Optional[:class:`bool`]
            The locked state to filter by.
        order_by: Optional[:class:`~github.enums.RepositoryOrderField`]
            The field to order repositories by.
        owner_affiliations: Optional[List[:class:`~github.enums.RepositoryAffiliation`]]
            The owner affiliations to filter by.
        privacy: Optional[:class:`~github.enums.RepositoryPrivacy`]
            The privacy to filter by.
        viewer_affiliations: Optional[List[:class:`~github.enums.RepositoryAffiliation`]]
            The viewer affiliations to filter by.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.Repository`.
        """

        order_by = order_by and order_by.value
        owner_affiliations = owner_affiliations and [a.value for a in owner_affiliations]
        privacy = privacy and privacy.value
        viewer_affiliations = viewer_affiliations and [a.value for a in viewer_affiliations]

        from github.objects import Repository

        def map_func(data):
            return Repository.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_repositoryowner_repositories,
            self.id,
            is_fork,
            is_locked,
            order_by,
            owner_affiliations,
            privacy,
            viewer_affiliations,
            map_func=map_func,
            **kwargs
        )
