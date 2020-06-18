"""
/github/__init__.py

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

import collections

import github
from github.client import Client
from github.objects import *

__all__ = [
    "Client", "abc", "enums", "errors", "objects", "query", "utils",
    *github.objects.__all__,
]


__version__ = "1.0.0a"

VersionInfo = collections.namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=1, minor=0, micro=0, releaselevel="alpha", serial=0)
