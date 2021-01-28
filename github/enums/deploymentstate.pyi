from enum import Enum


class DeploymentState(Enum):
    abandoned: str
    active: str
    destroyed: str
    error: str
    failure: str
    inactive: str
    in_progress: str
    pending: str
    queued: str
    waiting: str
