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

from github.objects import abc


class License(abc.Node):
    """
    A repository's open source license.

    https://developer.github.com/v4/object/license/
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0} key='{1}'>".format(self.__class__.__name__, self.key)

    @classmethod
    def from_data(cls, data):
        if "license" in data.keys():
            return cls(data["license"])
        else:
            licenses = list()

            for (license) in data["licenses"]:
                licenses.append(cls(license))

            return licenses

    @property
    def body(self):
        """
        The full text of the license.
        """

        return self.data.get("body")

    @property
    def conditions(self):
        """
        The conditions set by the license.
        """

        return LicenseRule.from_data(self.data.get("conditions"))

    @property
    def description(self):
        """
        A human-readable description of the license.
        """

        return self.data.get("description")

    @property
    def implementation(self):
        """
        Instructions on how to implement the license.
        """

        return self.data.get("implementation")

    @property
    def is_featured(self):
        """
        Whether the license is featured.
        """

        return self.data.get("featured")

    @property
    def is_hidden(self):
        """
        Whether the license is not displayed in license pickers.
        """

        return self.data.get("hidden")

    @property
    def is_pseudo(self):
        """
        Whether the license is a pseudo-license placeholder.
        """

        return self.data.get("pseudoLicense")

    @property
    def key(self):
        """
        The lowercased SPDX ID of the license.
        """

        return self.data.get("key")

    @property
    def limitations(self):
        """
        The limitations set by the license.
        """

        return LicenseRule.from_data(self.data.get("limitations"))

    @property
    def name(self):
        """
        The license' full name specified by https://spdx.org/licenses.
        """

        return self.data.get("name")

    @property
    def nickname(self):
        """
        The license' customary short name.
        """

        return self.data.get("nickname")

    @property
    def permissions(self):
        """
        The permissions set by the license.
        """

        return LicenseRule.from_data(self.data.get("permissions"))

    @property
    def spdx_id(self):
        """
        The license' short identifier specified by https://spdx.org/licenses.
        """

        return self.data.get("spdxId")

    @property
    def url(self):
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

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0} key='{1}'>".format(self.__class__.__name__, self.key)

    @classmethod
    def from_data(cls, data):
        rules = list()

        for (rule) in data:
            rules.append(cls(rule))

        return rules
    
    @property
    def description(self):
        """
        A description of the rule.
        """

        return self.data.get("description")

    @property
    def key(self):
        """
        The machine-readable rule key.
        """

        return self.data.get("key")

    @property
    def label(self):
        """
        The human-readable rule label.
        """

        return self.data.get("label")
