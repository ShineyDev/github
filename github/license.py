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
            self.__class__.__name__, self.name, self.id, self.url)

    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        # https://developer.github.com/v3/licenses/#get-an-individual-license

        data_ = {
            "_data"         : data,
            "body"          : data.get("body"),
            "conditions"    : data.get("conditions"),
            "description"   : data.get("description"),
            "id"            : data.get("spdx_id"),
            "implementation": data.get("implementation"),
            "key"           : data.get("key"),
            "limitations"   : data.get("limitations"),
            "name"          : data.get("name"),
            "permissions"   : data.get("permissions"),
            "url"           : data.get("url"),
        }

        return cls(**data_)

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

            data_ = {
                "_data": data,
                "id"   : data.get("spdx_id"),
                "key"  : data.get("key"),
                "name" : data.get("name"),
                "url"  : data.get("url"),
            }

            return cls(**data_)
        else:
            # https://developer.github.com/v3/licenses/#list-commonly-used-licenses

            licenses = list()

            for (license) in data:
                data_ = {
                    "_data": data,
                    "id"   : data.get("spdx_id"),
                    "key"  : data.get("key"),
                    "name" : data.get("name"),
                    "url"  : data.get("url"),
                }

                license = cls(**data_)
                licenses.append(license)

            return licenses