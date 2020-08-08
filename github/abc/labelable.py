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

class Labelable():
    """
    Represents an object which can be labeled.

    Implemented by:

    * :class:`github.Issue`
    * :class:`github.PullRequest`
    """

    # https://developer.github.com/v4/interface/labelable/

    __slots__ = ()

    async def fetch_labels(self):
        """
        |coro|

        Fetches a list of labels from the labelable.

        Returns
        -------
        List[:class:`~github.Label`]
            A list of labels.
        """

        # prevent cyclic imports
        from github.objects import Label

        data = await self.http.fetch_labelable_labels(self.id)
        return Label.from_data(data, self.http)

    async def add_labels(self, *labels):
        """
        |coro|

        Adds labels to the labelable.

        Parameters
        ----------
        \\*labels: :class:`github.Label`
            An iterable of labels.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add labels to the labelable.
        """

        # https://developer.github.com/v4/mutation/addlabelstolabelable/

        labels = [label.id for label in labels]
        await self.http.mutate_labelable_add_labels(self.id, labels)

    async def clear_labels(self):
        """
        |coro|

        Clears all labels from the labelable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to clear labels from the labelable.
        """

        # https://developer.github.com/v4/mutation/clearlabelsfromlabelable/

        await self.http.mutate_labelable_clear_labels(self.id)

    async def remove_labels(self, *labels):
        """
        |coro|

        Removes labels from the labelable.

        Parameters
        ----------
        \\*labels: :class:`github.Label`
            An iterable of labels.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove labels from the labelable.
        """

        # https://developer.github.com/v4/mutation/removelabelsfromlabelable/

        labels = [label.id for label in labels]
        await self.http.mutate_labelable_remove_labels(self.id, labels)
