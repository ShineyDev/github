"""
/github/abc/starrable.py

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

class Starrable():
    """
    Represents an entity that can be starred.
    """

    __slots__ = ()

    @property
    def stargazer_count(self):
        """
        The number of stargazers on the starrable.

        :type: :class:`int`
        """

        return self.data["stargazerCount"]

    @property
    def viewer_has_starred(self):
        """
        Whether the authenticated user has starred the starrable.

        :type: :class:`bool`
        """

        return self.data["viewerHasStarred"]

    def fetch_stargazers(self, *, order_by=None, **kwargs):
        """
        |aiter|

        Fetches the stargazers on the starrable.

        Parameters
        ----------
        order_by: :class:`~github.enums.StargazerOrderField`
            The field to order stargazers by.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.User`.
        """

        order_by = order_by and order_by.value

        from github.objects import User

        def map_func(data):
            return User.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_starrable_stargazers,
            self.id,
            order_by,
            map_func=map_func,
            **kwargs
        )
