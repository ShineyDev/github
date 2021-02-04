from enum import Enum


class PullRequestReviewState(Enum):
    approved: str
    changes_requested: str
    comment: str
    dismissed: str
    pending: str
