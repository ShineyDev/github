"""
/github/enums/issuetimelineitemtype.py

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

from enum import Enum


class IssueTimelineItemType(Enum):
    """
    Represents the type of an event in an
    :meth:`issue timeline <github.Issue.fetch_timeline_items>`.
    """

    #: The :class:`~github.Issue` was added to a
    #: :class:`~github.Milestone`.
    add_to_milestone_event = "MILESTONED_EVENT"

    #: The :class:`~github.Issue` was added to a
    #: :class:`~github.Project`.
    add_to_project_event = "ADDED_TO_PROJECT_EVENT"

    #: An assignee was added to the
    #: :class:`~github.interfaces.Assignable`.
    assignee_add_event = "ASSIGNED_EVENT"

    #: An assignee was removed from the
    #: :class:`~github.interfaces.Assignable`.
    assignee_remove_event = "UNASSIGNED_EVENT"

    #: A :class:`~github.User` was blocked from the
    #: :class:`~github.Issue`.
    block_event = "USER_BLOCKED_EVENT"

    #: The :class:`~github.interfaces.Closable` was closed.
    close_event = "CLOSED_EVENT"

    #: An :class:`~github.IssueComment` was added to the
    #: :class:`~github.Issue`.
    comment = "ISSUE_COMMENT"

    #: An :class:`~github.IssueComment` was deleted from the
    #: :class:`~github.Issue`.
    comment_delete_event = "COMMENT_DELETED_EVENT"

    #: The :class:`~github.Issue` was connected to another
    #: :class:`~github.Issue` or :class:`~github.PullRequest`.
    connect_event = "CONNECTED_EVENT"

    #: The :class:`~github.Issue` was converted from a
    #: :class:`~github.ProjectCard`.
    convert_from_project_card_event = "CONVERTED_NOTE_TO_ISSUE_EVENT"

    #: The :class:`~github.Issue` was referenced in another
    #: :class:`~github.Issue` or :class:`~github.PullRequest`.
    cross_reference_event = "CROSS_REFERENCED_EVENT"

    #: The :class:`~github.Issue` was disconnected from another
    #: :class:`~github.Issue` or :class:`~github.PullRequest`.
    disconnect_event = "DISCONNECTED_EVENT"

    #: A :class:`~github.Label` was added to the
    #: :class:`~github.interfaces.Labelable`.
    label_add_event = "LABELED_EVENT"

    #: A :class:`~github.Label` was removed from the
    #: :class:`~github.interfaces.Labelable`.
    label_remove_event = "UNLABELED_EVENT"

    #: The :class:`~github.interfaces.Lockable` was locked.
    lock_event = "LOCKED_EVENT"

    #: The :class:`~github.Issue` was marked as a duplicate.
    mark_as_duplicate_event = "MARKED_AS_DUPLICATE_EVENT"

    #: An :class:`~github.interfaces.Actor` was mentioned in the
    #: :class:`~github.Issue` body.
    mention_event = "MENTIONED_EVENT"

    #: The :class:`~github.Issue` was moved to another
    #: :class:`column <github.ProjectColumn>` in a
    #: :class:`~github.Project`.
    move_in_project_event = "MOVED_COLUMNS_IN_PROJECT_EVENT"

    #: The :class:`~github.Issue` was pinned.
    pin_event = "PINNED_EVENT"

    #: The :class:`~github.Issue` was referenced in a
    #: :class:`~github.GitCommit`.
    reference_event = "REFERENCED_EVENT"

    #: The :class:`~github.Issue` was removed from a
    #: :class:`~github.Milestone`.
    remove_from_milestone_event = "DEMILESTONED_EVENT"

    #: The :class:`~github.Issue` was removed from a
    #: :class:`~github.Project`.
    remove_from_project_event = "REMOVED_FROM_PROJECT_EVENT"

    #: The :class:`~github.Issue` title was updated.
    rename_event = "RENAMED_TITLE_EVENT"

    #: The :class:`~github.interfaces.Closable` was reopened.
    reopen_event = "REOPENED_EVENT"

    #: An :class:`~github.interfaces.Actor` subscribed to the
    #: :class:`~github.interfaces.Subscribable`.
    subscribe_event = "SUBSCRIBED_EVENT"

    #: The :class:`~github.Issue` was transferred to another
    #: :class:`~github.Repository`.
    transfer_event = "TRANSFERRED_EVENT"

    #: The :class:`~github.Issue` was unlocked.
    unlock_event = "UNLOCKED_EVENT"

    #: The :class:`~github.Issue` was unmarked as a duplicate.
    unmark_as_duplicate_event = "UNMARKED_AS_DUPLICATE_EVENT"

    #: The :class:`~github.Issue` was unpinned.
    unpin_event = "UNPINNED_EVENT"

    #: An :class:`~github.interfaces.Actor` unsubscribed from the
    #: :class:`~github.interfaces.Subscribable`.
    unsubscribe_event = "UNSUBSCRIBED_EVENT"
