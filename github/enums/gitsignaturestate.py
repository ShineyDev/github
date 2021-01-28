"""
/github/enums/gitsignaturestate.py

    Copyright (c) 2019-2020 ShineyDev

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from enum import Enum


class GitSignatureState(Enum):
    """
    Represents the state of a :class:`~github.abc.GitSignature`.
    """

    #: The signature certificate, or another in its chain, could not be
    #: verified.
    bad_cert = "BAD_CERT"

    #: The email used to sign the subject is invalid.
    bad_email = "BAD_EMAIL"

    #: The signing key has expired.
    expired_key = "EXPIRED_KEY"

    #: The GPG verification service experienced an error.
    gpg_verify_error = "GPGVERIFY_ERROR"

    #: The GPG verification service is unavailable.
    gpg_verify_unavailable = "GPGVERIFY_UNAVAILABLE"

    #: The signature is invalid.
    invalid = "INVALID"

    #: The signature is malformed.
    malformed = "MALFORMED_SIG"

    #: The signing key is not a signing key.
    not_signing_key = "NOT_SIGNING_KEY"

    #: The email used to sign the subject does not correspond to a
    #: GitHub user.
    no_user = "NO_USER"

    #: The signature is valid but the certificate revocation check
    #: service experienced an error.
    ocsp_error = "OCSP_ERROR"

    #: The signature is valid but the certificate revocation check is
    #: pending.
    ocsp_pending = "OCSP_PENDING"

    #: The signature is valid but a certificate in the chain has been
    #: revoked.
    ocsp_revoked = "OCSP_REVOKED"

    #: The signing key is unknown.
    unknown_key = "UNKNOWN_KEY"

    #: The signature type is unknown.
    unknown_type = "UNKNOWN_SIG_TYPE"

    #: The subject is unsigned.
    unsigned = "UNSIGNED"

    #: The email used to sign the subject is unverified.
    unverified_email = "UNVERIFIED_EMAIL"

    #: The signature is valid.
    valid = "VALID"
