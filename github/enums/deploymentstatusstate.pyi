from enum import Enum


class DeploymentStatusState(Enum):
    error: str
    failure: str
    inactive: str
    in_progress: str
    pending: str
    queued: str
    success: str
    waiting: str
