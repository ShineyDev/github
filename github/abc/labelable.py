"""
/github/abc/labelable.py

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


class Labelable():
    """
    Represents an object that can be labeled.
    """

    __slots__ = ()

    def fetch_labels(self, *, order_by=None, **kwargs):
        """
        |aiter|

        Fetches labels from the labelable.

        Parameters
        ----------
        order_by: :class:`~github.enums.LabelOrderField`
            The field to order by.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.Label`.
        """

        from github.objects import Label

        if order_by:
            order_by = order_by.value

        def map_func(data):
            return Label.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_labelable_labels, self.id,
            order_by,
            map_func=map_func,
            **kwargs
        )
