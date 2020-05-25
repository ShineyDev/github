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

import typing


class ProjectOwner():
    """
    Represents the owner of a GitHub project.

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.Repository`
    * :class:`~github.User`
    """

    # https://developer.github.com/v4/interface/projectowner/

    __slots__ = ()

    @property
    def projects_resource_path(self) -> str:
        """
        The project owner's projects resource path.

        :type: :class:`str`
        """

        return self.data["projectsResourcePath"]

    @property
    def projects_url(self) -> str:
        """
        The project owner's projects url.

        :type: :class:`str`
        """

        return self.data["projectsUrl"]

    @property
    def viewer_can_create_projects(self) -> bool:
        """
        Whether the authenticated user can create projects in the project owner.

        :type: :class:`bool`
        """

        return self.data["viewerCanCreateProjects"]

    async def fetch_project(self, number: int) -> "Project":
        """
        |coro|

        Fetches a project from this project owner.

        This requires the ``public_repo`` scope.

        Parameters
        ----------
        number: :class:`int`
            The project number.

        Returns
        -------
        :class:`~github.Project`
            A project.
        """

        # prevent cyclic imports
        from github.objects import Project

        data = await self.http.fetch_projectowner_project(self.id, number)
        return Project.from_data(data, self.http)

    async def fetch_projects(self) -> typing.List["Project"]:
        """
        |coro|

        Fetches a list of projects from this project owner.

        This requires the ``public_repo`` scope.

        Returns
        -------
        List[:class:`~github.Project`]
            A list of projects.
        """

        # prevent cyclic imports
        from github.objects import Project

        data = await self.http.fetch_projectowner_projects(self.id)
        return Project.from_data(data, self.http)
    