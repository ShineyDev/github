from enum import Enum


class IssueTimelineItemType(Enum):
    add_to_milestone_event: str
    add_to_project_event: str
    assignee_add_event: str
    assignee_remove_event: str
    block_event: str
    close_event: str
    comment: str
    comment_delete_event: str
    connect_event: str
    convert_from_project_card_event: str
    cross_reference_event: str
    disconnect_event: str
    label_add_event: str
    label_remove_event: str
    lock_event: str
    mark_as_duplicate_event: str
    mention_event: str
    move_in_project_event: str
    pin_event: str
    reference_event: str
    remove_from_milestone_event: str
    remove_from_project_event: str
    rename_event: str
    reopen_event: str
    subscribe_event: str
    transfer_event: str
    unlock_event: str
    unmark_as_duplicate_event: str
    unpin_event: str
    unsubscribe_event: str
