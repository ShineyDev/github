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
    def __init__(self, *, key: str, name: str, url: str, body: str,
                 description: str, implementation: str, permissions: list,
                 conditions: list, limitations: list):
        
        self.key = key
        self.name = name
        self.url = url
        self.body = body
        self.description = description
        self.implementation = implementation
        self.permissions = permissions
        self.conditions = conditions
        self.limitations = limitations

    @classmethod
    def from_data(cls, data: dict):
        key = data["key"]
        name = data["name"]
        url = data["html_url"]
        body = data["body"]
        description = data["description"]
        implementation = data["implementation"]
        permissions = data["permissions"]
        conditions = data["conditions"]
        limitations = data["limitations"]

        return cls(key=key, name=name, url=url, body=body,
                   description=description, implementation=implementation,
                   permissions=permissions, conditions=conditions,
                   limitations=limitations)