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
from github.objects.project import Project
from github.objects.projectcard import ProjectCard
from github.objects.projectcolumn import ProjectColumn
from github.objects.pullrequest import PullRequest
from github.objects.ratelimit import RateLimit
from github.objects.reaction import Reaction
from github.objects.repository import Repository
from github.objects.sponsorlisting import SponsorListing
from github.objects.sponsorship import Sponsorship
from github.objects.sponsortier import SponsorTier
from github.objects.status import Status
from github.objects.topic import Topic
from github.objects.user import User, AuthenticatedUser

__all__ = [
    "Bot", "CodeOfConduct", "CommitComment", "Issue", "Label", "Language",
    "License", "LicenseRule", "Mannequin", "Metadata", "Organization",
    "Project", "ProjectCard", "ProjectColumn", "PullRequest", "RateLimit",
    "Reaction", "Repository", "SponsorListing", "Sponsorship", "SponsorTier",
    "Status", "Topic", "User", "AuthenticatedUser",
]


_TYPE_MAP = {
    "Bot": Bot,
    "CodeOfConduct": CodeOfConduct,
    "CommitComment": CommitComment,
    "Issue": Issue,
    "Label": Label,
    "Language": Language,
    "License": License,
    "LicenseRule": LicenseRule,
    "Mannequin": Mannequin,
    "GitHubMetadata": Metadata,
    "Organization": Organization,
    "Project": Project,
    "ProjectCard": ProjectCard,
    "ProjectColumn": ProjectColumn,
    "PullRequest": PullRequest,
    "RateLimit": RateLimit,
    "ReactionGroup": Reaction,
    "Repository": Repository,
    "UserStatus": Status,
    "Topic": Topic,
    "User": User,
    "CodeOfConduct": CodeOfConduct,
}
