"""
/github/objects/__init__.py

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

from github.objects.bot import Bot
from github.objects.codeofconduct import CodeOfConduct
from github.objects.commitcomment import CommitComment
from github.objects.issue import Issue
from github.objects.label import Label
from github.objects.language import Language
from github.objects.license import License
from github.objects.licenserule import LicenseRule
from github.objects.mannequin import Mannequin
from github.objects.metadata import Metadata
from github.objects.organization import Organization
from github.objects.pullrequest import PullRequest
from github.objects.ratelimit import RateLimit
from github.objects.reaction import Reaction
from github.objects.repository import Repository, PartialRepository
from github.objects.topic import Topic, PartialTopic
from github.objects.user import User, AuthenticatedUser
