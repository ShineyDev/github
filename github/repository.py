"""
/repository.py

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

from . import (
    cache,
    endpoints,
    license,
    organization,
    permissions,
    request,
    user,
)

from .utils import (
    abc,
    utils,
)


class Repository(abc.DataStore):
    def __eq__(self, other):
        if (type(self) != type(other)):
            return False

        if (self.id != other.id):
            return False

        return True

    def __repr__(self):
        return "<{0} full_name='{1}' url='{2}'>".format(self.__class__.__name__, self.full_name, self.url)

    @classmethod
    def from_data(cls, data: dict, *, requester: request.Requester):
        if (data is None):
            return None

        data_ = {
            "_cache"    : cache.Cache(),
            "_data"     : data,
            "_endpoints": endpoints.Endpoints.from_data({k: v for (k, v) in data.items() if k.endswith("_url")}),
            "_requester": requester,
        }

        converters = {
            "created_at"  : utils.iso_to_datetime,
            "license"     : license.PartialLicense.from_data,
            "organization": organization.Organization.from_data,
            "owner"       : user.User.from_data,
            "parent"      : (Repository.from_data, tuple(), dict(requester=requester)),
            "permissions" : permissions.RepositoryPermissions.from_data,
            "pushed_at"   : utils.iso_to_datetime,
            "source"      : (Repository.from_data, tuple(), dict(requester=requester)),
            "updated_at"  : utils.iso_to_datetime,
        }

        defaults = {
            "topics": list(),
        }

        overwrites = {
            "archived"         : "is_archived",
            "disabled"         : "is_disabled",
            "fork"             : "is_fork",
            "forks_count"      : "fork_count",
            "html_url"         : "url",
            "private"          : "is_private",
            "stargazers_count" : "star_count",
            "subscribers_count": "subscriber_count",
            "watchers_count"   : "watcher_count",
        }

        return cls._from_data(data, current=data_, converters=converters, defaults=defaults, overwrites=overwrites)

    async def fetch_license(self, cache: bool=True):
        # https://developer.github.com/v3/licenses/#get-the-contents-of-a-repositorys-license

        method = "GET"
        url = "/repos/{0}/{1}/license".format(self._data["owner"]["login"], self.name)

        data = await self._requester.request(method, url)
        result = license.PartialLicense.from_data(data)

        if (cache):
            self._cache.license = result
            self.license = result

        return result

    def get_license(self):
        return self._cache.license or self.license