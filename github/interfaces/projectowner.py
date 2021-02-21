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

from github.iterator import CollectionIterator


class ProjectOwner():
    """
    Represents the owner of one or more GitHub Projects.
    """

    __slots__ = ()

    @property
    def projects_resource_path(self):
        """
        A resource path pointing to the owner's projects.

        :type: :class:`str`
        """

        return self.data["projectsResourcePath"]

    @property
    def projects_url(self):
        """
        A URL pointing to the owner's projects.

        :type: :class:`str`
        """

        return self.data["projectsUrl"]

    @property
    def viewer_can_create_projects(self):
        """
        Whether the authenticated user can create projects on the
        owner.

        :type: :class:`bool`
        """

        return self.data["viewerCanCreateProjects"]

    async def fetch_project(self, number):
        """
        |coro|

        Fetches a project from the owner.

        Parameters
        ----------
        number: :class:`int`
            The project number.

        Returns
        -------
        :class:`~github.Project`
            A project.
        """

        from github.objects import Project

        data = await self.http.fetch_projectowner_project(self.id, number)
        return Project.from_data(data, self.http)

    def fetch_projects(self, *, order_by=None, query=None, states=None, **kwargs):
        """
        |aiter|

        Fetches projects from the owner.

        Parameters
        ----------
        order_by: :class:`~github.enums.ProjectOrderField`
            The field to order projects by.
        query: :class:`str`
            The query to filter to.
        states: List[:class:`~github.enums.ProjectState`]
            The project states to filter to.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.Project`.
        """

        order_by = order_by and order_by.value
        states = states and [state.value for state in states]

        from github.objects import Project

        def map_func(data):
            return Project.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_projectowner_projects,
            self.id,
            order_by,
            query,
            states,
            map_func=map_func,
            **kwargs
        )
    