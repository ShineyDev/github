"""
/github/abc/memberstatusable.py

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

class MemberStatusable():
    """
    Represents an entity that can hold member statuses.
    """

    __slots__ = ()

    def fetch_member_statuses(self, *, order_by=None, **kwargs):
        """
        |aiter|

        Fetches members' statuses from the entity.

        Parameters
        ----------
        order_by: :class:`~github.enums.UserStatusOrderField`
            The field to order statuses by.
        **kwargs
            Keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.UserStatus`.
        """

        order_by = order_by and order_by.value

        from github.objects import UserStatus

        def map_func(data):
            return UserStatus.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_memberstatusable_member_statuses,
            self.id,
            order_by,
            map_func=map_func,
            **kwargs
        )
