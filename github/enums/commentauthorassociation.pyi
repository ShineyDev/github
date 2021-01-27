from enum import Enum


class CommentAuthorAssociation(Enum):
    collaborator: str
    contributor: str
    first_time_contributor: str
    first_timer: str
    mannequin: str
    member: str
    none: str
    owner: str
