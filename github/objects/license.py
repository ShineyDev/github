"""
/github/objects/license.py

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

from github.objects import abc
from github.objects import licenserule


class License(abc.Node):
    """
    A repository's open source license.

    https://developer.github.com/v4/object/license/
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} key='{0.key}'>".format(self)

    @classmethod
    def from_data(cls, data: typing.Union[dict, list]) -> typing.Union["License", typing.Iterable["License"]]:
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            licenses = list()

            for (license) in data:
                licenses.append(cls(license))

            return licenses

    @property
    def body(self) -> str:
        """
        The full text of the license.
        """

        return self.data["body"]

    @property
    def conditions(self) -> typing.Iterable["LicenseRule"]:
        """
        The conditions set by the license.
        """

        conditions = self.data["conditions"]
        return licenserule.LicenseRule.from_data(conditions)

    @property
    def description(self) -> str:
        """
        A human-readable description of the license.
        """

        return self.data["description"]

    @property
    def implementation(self) -> str:
        """
        Instructions on how to implement the license.
        """

        return self.data["implementation"]

    @property
    def is_featured(self) -> bool:
        """
        Whether the license is featured.
        """

        return self.data["featured"]

    @property
    def is_hidden(self) -> bool:
        """
        Whether the license is not displayed in license pickers.
        """

        return self.data["hidden"]

    @property
    def is_pseudo(self) -> bool:
        """
        Whether the license is a pseudo-license placeholder.
        """

        return self.data["pseudoLicense"]

    @property
    def key(self) -> str:
        """
        The lowercased SPDX ID of the license.
        """

        return self.data["key"]

    @property
    def limitations(self) -> typing.Iterable["LicenseRule"]:
        """
        The limitations set by the license.
        """

        limitations = self.data["limitations"]
        return licenserule.LicenseRule.from_data(limitations)

    @property
    def name(self) -> str:
        """
        The license' full name specified by https://spdx.org/licenses.
        """

        return self.data["name"]

    @property
    def nickname(self) -> str:
        """
        The license' customary short name.
        """

        return self.data["nickname"]

    @property
    def permissions(self) -> typing.Iterable["LicenseRule"]:
        """
        The permissions set by the license.
        """

        permissions = self.data["permissions"]
        return licenserule.LicenseRule.from_data(permissions)

    @property
    def spdx_id(self) -> str:
        """
        The license' short identifier specified by https://spdx.org/licenses.
        """

        return self.data["spdxId"]

    @property
    def url(self) -> str:
        """
        The url to the license on https://choosealicense.com.
        """

        return self.data["url"]
