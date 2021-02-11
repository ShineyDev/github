from enum import Enum


class RepositoryLockReason(Enum):
    billing: str
    migration: str
    move: str
    rename: str
