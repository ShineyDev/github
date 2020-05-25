"""
/github/abc/type.py

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

class Type():
    """
    Represents an object type.

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.CodeOfConduct`
    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.Language`
    * :class:`~github.License`
    * :class:`~github.LicenseRule`
    * :class:`~github.Metadata`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.PullRequest`
    * :class:`~github.RateLimit`
    * :class:`~github.Reaction`
    * :class:`~github.Repository`
    * :class:`~github.Topic`
    * :class:`~github.User`
    """

    # this interface does not have an api equivalent

    __slots__ = ()

    @classmethod
    def from_data(cls, data, http=None):
        if http:
            if isinstance(data, dict):
                return cls(data, http)
            elif isinstance(data, list):
                return [cls(d, http) for (d) in data]

        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls(d) for (d) in data]

    @property
    def type(self) -> str:
        """
        The object's type.

        :type: :class:`str`
        """

        return self.data["__typename"]
