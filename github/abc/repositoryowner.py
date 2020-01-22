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

class RepositoryOwner():
    """
    Represents the owner of a GitHub repository.

    https://developer.github.com/v4/interface/repositoryowner/

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    async def fetch_repository(self, name: str) -> "Repository":
        """
        |coro|

        Fetches a repository from the repository owner.

        Parameters
        ----------
        name: :class:`str`
            The repository name.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`github.Repository`
            The repository.
        """

        # prevent cyclic imports
        from github.objects import Repository

        data = await self.http.fetch_repository(self.login, name)
        return Repository.from_data(data, self.http)
