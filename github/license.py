"""
/license.py

    Copyright (c) 2019 ShineyDev
    
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

from .utils import (
    abc,
)


class License(abc.DataStore):
    def __eq__(self, other):
        if (type(self) != type(other)):
            return False

        if (self.id != other.id):
            return False

        return True

    def __repr__(self):
        return "<{0} id='{1}' name='{2}' url='{3}'>".format(
            self.__class__.__name__, self.id, self.name, self.url)

    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        # https://developer.github.com/v3/licenses/#get-an-individual-license

        return cls._from_data(data)

class PartialLicense(License):
    @classmethod
    def from_data(cls, data: typing.Union[list, dict]):
        if (data is None):
            return None

        if (isinstance(data, dict)):
            # https://developer.github.com/v3/licenses/#get-the-contents-of-a-repositorys-license
            # https://developer.github.com/v3/repos/#get
            # https://developer.github.com/v3/repos/#list-user-repositories
            # https://developer.github.com/v3/repos/#list-organization-repositories
            # https://developer.github.com/v3/repos/forks/#list-forks
            # https://developer.github.com/v3/activity/watching/#list-repositories-being-watched
            # https://developer.github.com/v3/teams/#list-team-repos

            if ("license" in data.keys()):
                data = data.get("license")

                if (data is None):
                    return None

            return cls._from_data(data)
        else:
            # https://developer.github.com/v3/licenses/#list-commonly-used-licenses

            licenses = list()

            for (license) in data:
                license = cls._from_data(data)
                licenses.append(license)

            return licenses