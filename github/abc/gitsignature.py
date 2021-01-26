"""
/github/abc/gitsignature.py

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

from github.enums import GitSignatureState


class GitSignature():
    """
    Represents a Git signature.
    """

    __slots__ = ()

    @property
    def is_github(self):
        """
        Whether the signature was made using GitHub's signing key.

        :type: :class:`bool`
        """

        return self.data["wasSignedByGitHub"]

    @property
    def payload(self):
        """
        The raw ODB object without the signature header.

        :type: :class:`str`
        """

        return self.data["payload"]

    @property
    def signature(self):
        """
        The signature header.

        :type: :class:`str`
        """

        return self.data["signature"]

    @property
    def state(self):
        """
        The state of the signature.

        :type: :class:`~github.enums.GitSignatureState`
        """

        state = self.data["state"]
        return GitSignatureState.try_value(state)

    async def fetch_email(self):
        """
        |coro|

        Fetches the email used to sign the subject.

        Returns
        -------
        :class:`str`
            The email used to sign the subject.
        """

        return await self.http.fetch_gitsignature_email(self.id)

    async def fetch_signer(self):
        """
        |coro|

        Fetches the GitHub user corresponding to the
        :meth:`email <.fetch_email>` used to sign the subject.

        Returns
        -------
        Optional[:class:`~github.User`]
            The GitHub user corresponding to the email used to sign the
            subject.
        """

        from github.objects import User

        data = await self.http.fetch_gitsignature_signer(self.id)
        return User.from_data(data, self.http)
