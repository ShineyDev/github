"""
/github/abc/repositoryowner.py

    Copyright (c) 2019 ShineyDev
    
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
    Represents an owner of a Repository.

    https://developer.github.com/v4/interface/repositoryowner/
    """

    __slots__ = ()

    @property
    def has_pinnable_items(self) -> bool:
        """
        Whether or not this repository owner has any items that can be pinned to their profile.
        """

        return self.data["anyPinnableItems"]

    async def fetch_repository(self, name: str) -> "Repository":
        """
        Fetches a repository from this repository owner.
        """

        # prevent cyclic imports
        from github.objects import Repository

        data = await self.http.fetch_repository(self.login, name)
        return Repository.from_data(data, self.http)
