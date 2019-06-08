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

import datetime

from .utils import (
    abc,
)


class CoreRateLimit(abc.RateLimitABC):
    pass

class SearchRateLimit(abc.RateLimitABC):
    pass

class GraphQLRateLimit(abc.RateLimitABC):
    pass

class IntegrationManifestRateLimit(abc.RateLimitABC):
    pass

class RateLimit():
    def __init__(self, *, core, search, graphql, integration_manifest):
        self.core = core
        self.search = search
        self.graphql = graphql
        self.integration_manifest = integration_manifest

    def __repr__(self):
        return "<RateLimit core={0} search={1} graphql={2} integration_manifest={3}>".format(
            self.core.remaining, self.search.remaining, self.graphql.remaining, self.integration_manifest.remaining)

    @classmethod
    def from_data(cls, data: dict):
        core = CoreRateLimit.from_data(data["resources"]["core"])
        search = SearchRateLimit.from_data(data["resources"]["search"])
        graphql = GraphQLRateLimit.from_data(data["resources"]["graphql"])
        integration_manifest = IntegrationManifestRateLimit.from_data(data["resources"]["integration_manifest"])

        return cls(core=core, search=search, graphql=graphql,
                   integration_manifest=integration_manifest)