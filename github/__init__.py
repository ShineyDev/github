"""
/github/__init__.py

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

import collections

from github import abc
from github import enums
from github import query
from github.objects import *
from github.github import GitHub


__version__ = "0.2.2"

VersionInfo = collections.namedtuple("VersionInfo", "major minor micro releaselevel")
version_info = VersionInfo(major=0, minor=2, micro=2, releaselevel="final")
