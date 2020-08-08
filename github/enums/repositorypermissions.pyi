from enum import Enum


class RepositoryPermissions(Enum):
    admin: str
    maintain: str
    read: str
    triage: str
    write: str
