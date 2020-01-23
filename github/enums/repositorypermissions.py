"""
/github/enums/repositorypermissions.py

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

class RepositoryPermissions():
    """
    Represents a user's access level to a repository.

    https://developer.github.com/v4/enum/repositorypermission/
    """

    __slots__ = ("_permission",)

    def __init__(self, permission):
        self._permission = permission

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} '{0._permission}'>".format(self)

    @classmethod
    def from_data(cls, permission):
        return cls(permission)
    
    @property
    def administrator(self) -> bool:
        """
        Can read, clone, and push to this repository. Can also manage
        issues, pull requests, and repository settings, including
        adding collaborators.
        """

        return self._permission in ["ADMIN"]

    @property
    def maintain(self) -> bool:
        """
        Can read, clone, and push to this repository. Can also manage
        issues, pull requests, and some repository settings.
        """

        return self._permission in ["ADMIN", "MAINTAIN"]

    @property
    def write(self) -> bool:
        """
        Can read, clone, and push to this repository. Can also manage
        issues and pull requests.
        """

        return self._permission in ["ADMIN", "MAINTAIN", "WRITE"]

    @property
    def triage(self) -> bool:
        """
        Can read and clone this repository. Can also manage issues and
        pull requests.
        """

        return self._permission in ["ADMIN", "MAINTAIN", "WRITE", "TRIAGE"]

    @property
    def read(self) -> bool:
        """
        Can read and clone this repository. Can also open and comment
        on issues and pull requests.
        """

        return self._permission in ["ADMIN", "MAINTAIN", "WRITE", "TRIAGE", "READ"]
