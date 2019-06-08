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

class License():
    def __init__(self, *, key: str, id: str, name: str, url: str, body: str,
                 description: str, implementation: str, permissions: list,
                 conditions: list, limitations: list):
        
        self.key = key
        self.id = id
        self.name = name
        self.url = url
        self.body = body
        self.description = description
        self.implementation = implementation
        self.permissions = permissions
        self.conditions = conditions
        self.limitations = limitations

    def __repr__(self):
        return "<License name='{0}' id={1} url='{2}'>".format(self.name, self.id, self.url)

    @classmethod
    def from_data(cls, data: dict):
        # https://developer.github.com/v3/licenses/#get-an-individual-license

        key = data["key"]
        id = data["spdx_id"]
        name = data["name"]
        url = data["html_url"]
        body = data["body"]
        description = data["description"]
        implementation = data["implementation"]
        permissions = data["permissions"]
        conditions = data["conditions"]
        limitations = data["limitations"]

        return cls(key=key, id=id, name=name, url=url, body=body,
                   description=description, implementation=implementation,
                   permissions=permissions, conditions=conditions,
                   limitations=limitations)

class PartialLicense():
    def __init__(self, key: str, id: str, name: str, url: str):
        self.key = key
        self.id = id
        self.name = name
        self.url = url

    def __repr__(self):
        return "<PartialLicense name='{0}' id={1} url='{2}'>".format(self.name, self.id, self.url)

    @classmethod
    def from_data(cls, data: dict):
        if ("license" in data.keys()):
            # https://developer.github.com/v3/licenses/#get-the-contents-of-a-repositorys-license

            key = data["license"]["key"]
            id = data["license"]["id"]
            name = data["license"]["name"]
            url = data["license"]["url"]

            return cls(key=key, id=id, name=name, url=url)
        else:
            # https://developer.github.com/v3/licenses/#list-commonly-used-licenses

            licenses = list()
            for (license) in data:
                key = data["key"]
                id = data["id"]
                name = data["name"]
                url = data["url"]

                license = cls(key=key, id=id, name=name, url=url)
                licenses.append(license)

            return licenses