"""
/github/enums/sponsorshipprivacy.py

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

class SponsorshipPrivacy():
    """
    Represents the state of an issue.

    https://developer.github.com/v4/enum/issuestate/
    """

    __slots__ = ("_state",)

    def __init__(self, state):
        self._state = state

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} '{0._state}'>".format(self)

    @classmethod
    def from_data(cls, state):
        return cls(state)

    @property
    def private(self) -> bool:
        """
        The sponsorship is private.
        """

        return self._state == "PRIVATE"

    @property
    def public(self) -> bool:
        """
        The sponsorship is public.
        """

        return self._state == "PUBLIC"
