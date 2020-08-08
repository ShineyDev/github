from enum import Enum


class PullRequestState(Enum):
    closed: str
    merged: str
    open: str
