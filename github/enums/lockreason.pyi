from enum import Enum


class LockReason(Enum):
    off_topic: str
    resolved: str
    spam: str
    too_heated: str
