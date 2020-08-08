from enum import Enum


class ProjectCardState(Enum):
    body_only: str
    content_only: str
    redacted: str
