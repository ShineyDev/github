"""
/github/abc/packageowner.py

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

class PackageOwner():
    """
    Represents the owner of one or more GitHub Packages.
    """

    __slots__ = ()

    def fetch_packages(self, *, names=None, order_by=None, repository=None, type=None, **kwargs):
        """
        Fetches packages from a package owner.

        Parameters
        ----------
        names: List[:class:`str`]
            The names to filter to.
        order_by: :class:`~github.enums.PackageOrderField`
            The field to order packages by.
        repository: :class:`~github.Repository`
            The repository to filter to.
        type: :class:`~github.enums.PackageType`
            The type of package to filter to.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.Package`.
        """

        order_by = order_by and order_by.value
        repository = repository and repository.id
        type = type and type.value

        from github.objects import Package

        def map_func(data):
            return Package.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_packageowner_packages,
            self.id,
            names,
            order_by,
            repository,
            type,
            map_func=map_func,
            **kwargs
        )
