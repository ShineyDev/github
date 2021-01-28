from enum import Enum


class GitSignatureState(Enum):
    bad_cert: str
    bad_email: str
    expired_key: str
    gpg_verify_error: str
    gpg_verify_unavailable: str
    invalid: str
    malformed: str
    not_signing_key: str
    no_user: str
    ocsp_error: str
    ocsp_pending: str
    ocsp_revoked: str
    unknown_key: str
    unknown_type: str
    unsigned: str
    unverified_email: str
    valid: str
