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


class License(abc.Node):
    """
    A repository's open source license.

    https://developer.github.com/v4/object/license/
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self) -> str:
        return "<{0} key='{1}'>".format(self.__class__.__name__, self.key)

    @classmethod
    def from_data(cls, data: dict) -> typing.Union["License", typing.Iterable["License"]]:
        if "license" in data.keys():
            return cls(data["license"])
        elif "licenses" in data.keys():
            licenses = list()

            for (license) in data["licenses"]:
                licenses.append(cls(license))

            return licenses
        else:
            # HTTPClient.fetch_licenses
            ...

    @property
    def body(self) -> str:
        """
        The full text of the license.
        """

        return self.data.get("body")

    @property
    def conditions(self) -> typing.Iterable["LicenseRule"]:
        """
        The conditions set by the license.
        """

        return LicenseRule.from_data(self.data.get("conditions"))

    @property
    def description(self) -> str:
        """
        A human-readable description of the license.
        """

        return self.data.get("description")

    @property
    def implementation(self) -> str:
        """
        Instructions on how to implement the license.
        """

        return self.data.get("implementation")

    @property
    def is_featured(self) -> bool:
        """
        Whether the license is featured.
        """

        return self.data.get("featured")

    @property
    def is_hidden(self) -> bool:
        """
        Whether the license is not displayed in license pickers.
        """

        return self.data.get("hidden")

    @property
    def is_pseudo(self) -> bool:
        """
        Whether the license is a pseudo-license placeholder.
        """

        return self.data.get("pseudoLicense")

    @property
    def key(self) -> str:
        """
        The lowercased SPDX ID of the license.
        """

        return self.data.get("key")

    @property
    def limitations(self) -> typing.Iterable["LicenseRule"]:
        """
        The limitations set by the license.
        """

        return LicenseRule.from_data(self.data.get("limitations"))

    @property
    def name(self) -> str:
        """
        The license' full name specified by https://spdx.org/licenses.
        """

        return self.data.get("name")

    @property
    def nickname(self) -> str:
        """
        The license' customary short name.
        """

        return self.data.get("nickname")

    @property
    def permissions(self) -> typing.Iterable["LicenseRule"]:
        """
        The permissions set by the license.
        """

        return LicenseRule.from_data(self.data.get("permissions"))

    @property
    def spdx_id(self) -> str:
        """
        The license' short identifier specified by https://spdx.org/licenses.
        """

        return self.data.get("spdxId")

    @property
    def url(self) -> str:
        """
        The url to the license on https://choosealicense.com.
        """

        return self.data.get("url")

class LicenseRule():
    """
    Represents a license's conditions, permissions, or limitations.

    https://developer.github.com/v4/object/licenserule/
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self) -> str:
        return "<{0} key='{1}'>".format(self.__class__.__name__, self.key)

    @classmethod
    def from_data(cls, data: dict) -> typing.Iterable["LicenseRule"]:
        rules = list()

        for (rule) in data:
            rules.append(cls(rule))

        return rules
    
    @property
    def description(self) -> str:
        """
        A description of the rule.
        """

        return self.data.get("description")

    @property
    def key(self) -> str:
        """
        The machine-readable rule key.
        """

        return self.data.get("key")

    @property
    def label(self) -> str:
        """
        The human-readable rule label.
        """

        return self.data.get("label")
