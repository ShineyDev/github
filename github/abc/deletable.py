"""
/github/abc/deletable.py

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

class Deletable():
    """
    Represents an object which can be deleted.

    https://developer.github.com/v4/interface/deletable/

    Implemented by:

    * :class:`~github.CommitComment`
    """

    __slots__ = ()

    @property
    def viewer_can_delete(self) -> bool:
        """
        Whether or not the authenticated user can delete the deletable.
        """

        return self.data["viewerCanDelete"]

    async def delete(self):
        """
        |coro|

        Deletes the deletable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to delete the deletable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The deletable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if self.data["__typename"] == "CommitComment":
            # TODO: implement HTTPClient.delete_commit_comment
            ...
        elif self.data["__typename"] == "GistComment":
            # TODO: implement HTTPClient.delete_gist_comment
            ...
        elif self.data["__typename"] == "IssueComment":
            # TODO: implement HTTPClient.delete_issue_comment
            ...
        elif self.data["__typename"] == "PullRequestReview":
            # TODO: implement HTTPClient.delete_pull_request_review
            ...
        elif self.data["__typename"] == "PullRequestReviewComment":
            # TODO: implement HTTPClient.delete_pull_request_review_comment
            ...
        elif self.data["__typename"] == "TeamDiscussion":
            # TODO: implement HTTPClient.delete_team_discussion
            ...
        elif self.data["__typename"] == "TeamDiscussionComment":
            # TODO: implement HTTPClient.delete_team_discussion_comment
            ...
