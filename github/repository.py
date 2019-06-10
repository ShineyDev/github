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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._cache = cache.Cache()

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

        endpoints_ = {
            k: v for (k, v) in data.items() if k.endswith("_url")
        }

        data_ = {
            "_data"             : data,
            "_endpoints"        : endpoints.Endpoints.from_data(endpoints_),
            "_requester"        : requester,
            "allow_merge_commit": data.get("allow_merge_commit"),
            "allow_rebase_merge": data.get("allow_rebase_merge"),
            "allow_squash_merge": data.get("allow_squash_merge"),
            "created_at"        : utils.iso_to_datetime(data.get("created_at")),
            "default_branch"    : data.get("default_branch"),
            "description"       : data.get("description"),
            "fork_count"        : data.get("forks_count"),
            "full_name"         : data.get("full_name"),
            "has_downloads"     : data.get("has_downloads"),
            "has_issues"        : data.get("has_issues"),
            "has_pages"         : data.get("has_pages"),
            "has_projects"      : data.get("has_projects"),
            "has_wiki"          : data.get("has_wiki"),
            "id"                : data.get("id"),
            "is_archived"       : data.get("archived"),
            "is_disabled"       : data.get("disabled"),
            "is_fork"           : data.get("fork"),
            "is_private"        : data.get("private"),
            "language"          : data.get("language"),
            "license"           : license.PartialLicense.from_data(data.get("license")),
            "organization"      : organization.Organization.from_data(data.get("organization")),
            "owner"             : user.User.from_data(data.get("owner")),
            "parent"            : Repository.from_data(data.get("parent"), requester=requester),
            "permissions"       : permissions.RepositoryPermissions.from_data(data.get("permissions")),
            "pushed_at"         : utils.iso_to_datetime(data.get("pushed_at")),
            "name"              : data.get("name"),
            "network_count"     : data.get("network_count"),
            "node_id"           : data.get("node_id"),
            "open_issues_count" : data.get("open_issues_count"),
            "size"              : data.get("size"),
            "source"            : Repository.from_data(data.get("source"), requester=requester),
            "star_count"        : data.get("stargazers_count"),
            "subscriber_count"  : data.get("subscribers_count"),
            "topics"            : data.get("topics", list()),
            "updated_at"        : utils.iso_to_datetime(data.get("updated_at")),
            "url"               : data.get("html_url"),
            "watcher_count"     : data.get("watchers_count"),
        }

        return cls(**data_)

    async def fetch_license(self, cache: bool=True):
        # https://developer.github.com/v3/licenses/#get-the-contents-of-a-repositorys-license

        method = "GET"
        url = "/repos/{0}/{1}/license".format(self._data["owner"]["login"], self.name)

        data = await self._requester.request(method, url)
        result = license.License.from_data(data)

        if (cache):
            self._cache.license = result
            self.license = result

        return result

    def get_license(self):
        return self._cache.license or self.license