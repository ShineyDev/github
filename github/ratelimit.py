"""
/ratelimit.py

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


class CoreRateLimit(abc.RateLimit):
    pass

class SearchRateLimit(abc.RateLimit):
    pass

class GraphQLRateLimit(abc.RateLimit):
    pass

class IntegrationManifestRateLimit(abc.RateLimit):
    pass

class RateLimit(abc.DataStore):
    def __repr__(self):
        return "<RateLimit core={0} search={1} graphql={2} integration_manifest={3}>".format(
            self.core.remaining, self.search.remaining, self.graphql.remaining, self.integration_manifest.remaining)

    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        # https://developer.github.com/v3/rate_limit/#get-your-current-rate-limit-status

        data = data.get("resources")

        data_ = {
            "_data"               : data,
            "core"                : CoreRateLimit.from_data(data.get("core")),
            "graphql"             : SearchRateLimit.from_data(data.get("search")),
            "integration_manifest": GraphQLRateLimit.from_data(data.get("graphql")),
            "search"              : IntegrationManifestRateLimit.from_data(data.get("integration_manifest")),
        }

        return cls(**data_)