"""
/github/abc/projectowner.py

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

class ProjectOwner():
    """
    Represents the owner of a GitHub project.

    https://developer.github.com/v4/interface/projectowner/

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.Repository`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def projects_resource_path(self) -> str:
        """
        The project owner's projects resource path.
        """

        return self.data["projectsResourcePath"]

    @property
    def projects_url(self) -> str:
        """
        The project owner's projects url.
        """

        return self.data["projectsUrl"]

    @property
    def viewer_can_create_projects(self) -> bool:
        """
        Whether or not the authenticated user can create projects in the project owner.
        """

        return self.data["viewerCanCreateProjects"]
    