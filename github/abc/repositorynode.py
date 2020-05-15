"""
/github/abc/repositorynode.py

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

class RepositoryNode():
    """
    Represents a node which belongs to a repository.

    https://developer.github.com/v4/interface/repositorynode/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    async def fetch_repository(self) -> "Repository":
        """
        Fetches the repository the repository node belongs to.

        Raises
        ------
        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add reactions to the
            reactable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.Repository`
            The repository.
        """

        # prevent cyclic imports
        from github.objects import Repository

        data = await self.http.fetch_repositorynode_repository(self.id)
        return Repository.from_data(data, self.http)
