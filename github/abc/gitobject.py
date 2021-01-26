"""
/github/abc/gitobject.py

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

class GitObject():
    """
    Represents a Git object.
    """

    __slots__ = ()

    @property
    def commit_resource_path(self):
        """
        A resource path pointing to the :class:`~github.GitCommit`
        associated with the object.

        :type: :class:`str`
        """

        return self.data["commitResourcePath"]

    @property
    def commit_url(self):
        """
        A URL pointing to the :class:`~github.GitCommit` associated
        with the object.

        :type: :class:`str`
        """

        return self.data["commitUrl"]

    @property
    def oid(self):
        """
        The object's Git ID.

        :type: :class:`str`
        """

        return self.data["oid"]

    @property
    def oid_abbreviated(self):
        """
        The abbreviated :attr:`.oid`.

        :type: :class:`str`
        """

        return self.data["abbreviatedOid"]

    async def fetch_repository(self):
        """
        |coro|

        Fetches the repository the object exists on.

        Returns
        -------
        :class:`~github.Repository`
            The repository the object exists on.
        """

        from github.objects import Repository

        data = await self.http.fetch_gitobject_repository(self.id)
        return Repository.from_data(data, self.http)
