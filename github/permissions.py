"""
/permissions.py

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

from .utils import (
    abc,
)


class RepositoryPermissions(abc.DataStore):
    def __repr__(self):
        return "<{0} admin={1} pull={2} push={3}>".format(self.__class__.__name__, self.admin, self.pull, self.push)

    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        return cls._from_data(data)