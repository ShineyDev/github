from typing import Union

from github.iterator import CollectionIterator
from github.objects import CommitComment
from github.objects import GistComment
from github.objects import IssueComment
from github.objects import PullRequestComment
from github.objects import PullRequestReviewComment
from github.objects import TeamDiscussionComment


class Commentable():
    def fetch_comments(
        self, **kwargs
    ) -> Union[
        CollectionIterator[CommitComment],
        CollectionIterator[GistComment],
        CollectionIterator[IssueComment],
        CollectionIterator[PullRequestComment],
        CollectionIterator[PullRequestReviewComment],
        CollectionIterator[TeamDiscussionComment],
    ]: ...
