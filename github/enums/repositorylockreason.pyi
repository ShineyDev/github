from enum import Enum


class RepositoryLockReason(Enum):
    billing: str
    migrating: str
    moving: str
    rename: str
