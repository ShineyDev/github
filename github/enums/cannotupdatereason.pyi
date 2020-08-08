from enum import Enum


class CannotUpdateReason(Enum):
    archived: str
    denied: str
    insufficient_access: str
    locked: str
    login_required: str
    maintenance: str
    verified_email_required: str
