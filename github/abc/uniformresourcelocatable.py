"""
/github/abc/uniformresourcelocatable.py

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

class UniformResourceLocatable():
    """
    Represents an object that can be retrieved by a URL.

    https://developer.github.com/v4/interface/uniformresourcelocatable/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.CodeOfConduct`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.PullRequest`
    * :class:`~github.Repository`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def resource_path(self) -> str:
        """
        The resource path pointing to the resource.
        """

        return self.data["resourcePath"]

    @property
    def url(self) -> str:
        """
        The url pointing to the resource.
        """

        return self.data["url"]
