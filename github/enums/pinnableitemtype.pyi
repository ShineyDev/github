from enum import Enum


class PinnableItemType(Enum):
    gist: str
    issue: str
    organization: str
    project: str
    pull_request: str
    repository: str
    team: str
    user: str
