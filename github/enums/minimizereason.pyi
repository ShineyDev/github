from enum import Enum


class MinimizeReason(Enum):
    abuse: str
    duplicate: str
    off_topic: str
    outdated: str
    resolved: str
    spam: str
