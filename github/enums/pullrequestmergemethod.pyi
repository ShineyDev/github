from enum import Enum


class PullRequestMergeMethod(Enum):
    merge: str
    rebase: str
    squash: str
