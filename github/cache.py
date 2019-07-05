"""
/github/cache.py

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

class _Cache():
    def __init__(self):
        self._cache = list()

    def __iter__(self):
        for (i) in self._cache:
            yield i

    def append(self, object):
        if (object not in self._cache):
            self._cache.append(object)

        for (i, item) in enumerate(self._cache):
            if (item == object):
                self._cache[i] = object

class Cache():
    license_cache = _Cache()
    repository_cache = _Cache()

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except (AttributeError) as e:
            return None