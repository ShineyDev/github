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

from github.enums import Enum


class RepositoryPermissions(Enum):
    """
    Represents a user's access level to a repository.
    """

    # https://developer.github.com/v4/enum/repositorypermission/

    admin = "ADMIN"
    maintain = "MAINTAIN"
    read = "READ"
    triage = "TRIAGE"
    write = "WRITE"
