"""
/github/enums/commentauthorassociation.py

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

class CommentAuthorAssociation():
    """
    Represents an actor's association with a repository.

    https://developer.github.com/v4/enum/commentauthorassociation/
    """

    __slots__ = ("data",)

    def __init__(self, author_association):
        self._author_association = author_association

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} '{0._author_association}'>".format(self)

    @classmethod
    def from_data(cls, author_association):
        return cls(author_association)

    @property
    def owner(self) -> bool:
        """
        The actor is the owner of the repository.
        """

        return self._author_association == "OWNER"

    @property
    def member(self) -> bool:
        """
        The actor is a member of the organization that owns the repository.
        """

        return self._author_association == "MEMBER"

    @property
    def collaborator(self) -> bool:
        """
        The actor has been invited to collaborate on the repository.
        """

        return self._author_association == "COLLABORATOR"

    @property
    def contributor(self) -> bool:
        """
        The actor has previously committed to the repository.
        """

        return self._author_association == "CONTRIBUTOR"

    @property
    def first_time_contributor(self) -> bool:
        """
        The actor has not previously committed to this repository.
        """

        return self._author_association == "FIRST_TIME_CONTRIBUTOR"

    @property
    def first_timer(self) -> bool:
        """
        The actor has not previously committed to GitHub.
        """

        return self._author_association == "FIRST_TIMER"

    @property
    def none(self) -> bool:
        """
        The actor has no association with the repository.
        """

        return self._author_association == "NONE"
