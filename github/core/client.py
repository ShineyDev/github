from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientSession

    from github.api import Metadata, RateLimit
    from github.connection import AdvisoryOrder, Connection, SponsorableOrder, VulnerabilityOrder
    from github.content import CodeOfConduct, License
    from github.organization import Organization
    from github.repository import Repository, RepositoryVisibility, Topic
    from github.security import Advisory, Vulnerability
    from github.user import User, UserStatus, Viewer
    from github.utility.types import DateTime, T_json_object

import graphql

import github
from github.core.http import HTTPClient
from github.utility import MISSING


class Client(graphql.client.Client):
    """
    The base class for interaction with the API.


    Parameters
    ----------

    token: :class:`str`
        A GitHub personal access token.

        .. seealso::

            - `Creating a personal access token <link_token_create_>`_
            - `View your personal access tokens <link_token_view_>`_

    session: :class:`aiohttp.ClientSession`
        A client session.

    user_agent: :class:`str`
        A user agent. Defaults to ``ShineyDev/github@VERSION:UUID``.

        .. note::

            GitHub requests that you use your GitHub username or the
            name of the application for the User-Agent header value to
            allow them to contact you should there be a problem. Using
            ``USERNAME; ShineyDev/github@{version}:{uuid}``, replacing
            USERNAME with your username, would suffice for both.
    """

    __slots__ = ()

    def __init__(
        self,
        /,
        token: str,
        *,
        session: ClientSession,
        user_agent: str = MISSING,
    ) -> None:
        self._http: HTTPClient = HTTPClient(token, session, user_agent)

    async def request(
        self,
        document: str,
        operation: str = MISSING,
        /,
        **variables: T_json_object,
    ) -> T_json_object:
        """
        |coro|

        Sends a request to GitHub's GraphQL API.


        Parameters
        ----------

        document: :class:`str`
            A GraphQL document.

            .. tip::

                If you haven't already, you should
                `learn GraphQL <link_graphql_learn_>`_. You can also
                read GitHub's `GraphQL guides <link_graphql_guide_>`_,
                find documentation in the
                `GraphQL API reference <link_graphql_reference_>`_, and
                use the `GraphiQL Explorer <link_graphql_explorer_>`_
                to experiment with the API.

        operation: :class:`str`
            The name of the operation from the document to execute.
            Defaults to ``None``, which implies that the document
            contains only one operation.

        **variables
            A mapping of GraphQL variables.


        Raises
        ------

        ~github.core.errors.ClientResponseHTTPError
            Arbitrary HTTP error.

        ~github.core.errors.ClientResponseGraphQLError
            Arbitrary GraphQL error.


        Examples
        --------

        .. code:: python

            >>> await client.request("{viewer{login}}")
            {'viewer': {'login': 'nat'}}

        .. code:: python

            >>> await client.request("query($login:String!){user(login:$login){name}}", login="nat")
            {'user': {'name': 'Nat Friedman'}}


        :rtype: :class:`dict`
        """

        return await super().request(document, operation, **variables)

    async def fetch_all_codes_of_conduct(
        self,
        /,
        **kwargs,  # TODO
    ) -> list[CodeOfConduct]:
        """
        |coro|

        Fetches all codes of conduct.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch a code of conduct body.


        :rtype: List[:class:`~github.CodeOfConduct`]
        """

        data = await self._http.fetch_query_all_codes_of_conduct(**kwargs)
        return [github.CodeOfConduct._from_data(d, http=self._http) for d in data]

    async def fetch_all_licenses(
        self,
        /,
        **kwargs,  # TODO
    ) -> list[License]:
        """
        |coro|

        Fetches all licenses.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch a license body.


        :rtype: List[:class:`~github.License`]
        """

        data = await self._http.fetch_query_all_licenses(**kwargs)
        return [github.License._from_data(d, http=self._http) for d in data]

    async def fetch_code_of_conduct(
        self,
        key: str,
        /,
        **kwargs,  # TODO
    ) -> CodeOfConduct:
        """
        |coro|

        Fetches a code of conduct by its key.


        Parameters
        ----------

        key: :class:`str`
            See :attr:`CodeOfConduct.key`.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch the code of conduct body.

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A code of conduct with the provided key does not exist.


        :rtype: :class:`~github.CodeOfConduct`
        """

        data = await self._http.fetch_query_code_of_conduct(key, **kwargs)
        return github.CodeOfConduct._from_data(data, http=self._http)

    async def fetch_license(
        self,
        key: str,
        /,
        **kwargs,  # TODO
    ) -> License:
        """
        |coro|

        Fetches a license by its key.


        Parameters
        ----------

        key: :class:`str`
            See :attr:`License.key`.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch the license body.

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A license with the provided key does not exist.


        :rtype: :class:`~github.License`
        """

        data = await self._http.fetch_query_license(key, **kwargs)
        return github.License._from_data(data, http=self._http)

    async def fetch_metadata(
        self,
        /,
        **kwargs,  # TODO
    ) -> Metadata:
        """
        |coro|

        Fetches instance metadata.

        :rtype: :class:`~github.Metadata`
        """

        data = await self._http.fetch_query_metadata(**kwargs)
        return github.Metadata._from_data(data)

    async def fetch_organization(
        self,
        login: str,
        /,
        **kwargs,  # TODO
    ) -> Organization:
        """
        |coro|

        Fetches an organization by its login.

        .. note::

            This query requires the following token scopes:

            - ``read:org``


        Parameters
        ----------

        login: :class:`str`
            See :attr:`Organization.login <github.Organization.login>`.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A user with the provided login does not exist.


        :rtype: :class:`~github.Organization`
        """

        data = await self._http.fetch_query_organization(login, **kwargs)
        return github.Organization._from_data(data, http=self._http)

    async def fetch_rate_limit(
        self,
        /,
        **kwargs,  # TODO
    ) -> RateLimit:
        """
        |coro|

        Fetches instance rate limit data.

        :rtype: :class:`~github.RateLimit`
        """

        data = await self._http.fetch_query_rate_limit(**kwargs)
        return github.RateLimit._from_data(data)

    async def fetch_repository(
        self,
        owner: str,
        name: str,
        /,
        *,
        follow_renames: bool = MISSING,
        **kwargs,  # TODO
    ) -> Repository:
        """
        |coro|

        Fetches a repository by its owner and name.


        Parameters
        ----------

        owner: :class:`str`
            The login of the owner of the repository.
        name: :class:`str`
            The name of the repository.
        follow_renames: :class:`bool`
            Whether to follow repository renames when requesting a
            repository by its non-current name. Defaults to ``True``.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A repository with the provided owner and name does not exist.


        :rtype: :class:`~github.Repository`
        """

        data = await self._http.fetch_query_repository(
            owner,
            name,
            follow_renames if follow_renames is not MISSING else None,
            **kwargs,
        )

        return github.Repository._from_data(data, http=self._http)

    async def fetch_repository_owner(
        self,
        login: str,
        /,
        **kwargs,  # TODO
    ) -> Organization | User:
        """
        |coro|

        Fetches a repository owner by its login.


        Parameters
        ----------

        login: :class:`str`
            The login of the repository owner.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A repository owner with the provided login does not exist.


        :rtype: :class:`~github.Organization` | :class:`~github.User`
        """

        data = await self._http.fetch_query_repository_owner(login, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Organization":
            return github.Organization._from_data(data, http=self._http)
        elif data["__typename"] == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"invalid type {data['__typename']} for Query.repositoryOwner")

    async def fetch_topic(
        self,
        name: str,
        /,
        **kwargs,  # TODO
    ) -> Topic:
        """
        |coro|

        Fetches a topic by its name.


        Parameters
        ----------

        name: :class:`str`
            See :attr:`Topic.name <github.Topic.name>`.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A topic with the provided name does not exist.

            .. note::

                There is actually no concept of a topic that does not
                exist. Without getting into technical details, this
                means that unless you provide a name containing an
                invalid character, this function will always return a
                valid topic.

                For a more accurate representation of whether a topic
                "exists", see that its :attr:`~github.Topic.repository_count`
                is not zero.


        :rtype: :class:`~github.Topic`
        """

        data = await self._http.fetch_query_topic(name, **kwargs)
        return github.Topic._from_data(data, http=self._http)

    async def fetch_user(
        self,
        login: str,
        /,
        **kwargs,  # TODO
    ) -> User:
        """
        |coro|

        Fetches a user by its login.


        Parameters
        ----------

        login: :class:`str`
            See :attr:`User.login <github.User.login>`.


        Raises
        ------

        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A user with the provided login does not exist.


        :rtype: :class:`~github.User`
        """

        data = await self._http.fetch_query_user(login, **kwargs)
        return github.User._from_data(data, http=self._http)

    async def fetch_viewer(
        self,
        /,
        **kwargs,  # TODO
    ) -> Viewer:
        """
        |coro|

        Fetches the authenticated user.


        :rtype: :class:`~github.Viewer`
        """

        data = await self._http.fetch_query_viewer(**kwargs)
        return github.Viewer._from_data(data, http=self._http)

    def fetch_advisories(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order: AdvisoryOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Advisory]:
        """
        |aiter|

        Fetches security advisories.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order: :class:`~github.AdvisoryOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Advisory`
        """

        return github.Connection(
            self._http.collect_query_advisories,
            order.value if order is not MISSING else None,
            data_map=lambda d: github.Advisory._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_sponsorables(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order: SponsorableOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Organization | User]:
        """
        |aiter|

        Fetches sponsorable organizations and users.

        .. note::

            This query requires the following token scopes:

            - ``read:org``


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order: :class:`~github.SponsorableOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Organization` | :class:`~github.User`
        """

        return github.Connection(
            self._http.collect_query_sponsorables,
            order.value if order is not MISSING else None,
            data_map=lambda d: github.Organization._from_data(d, http=self._http) if d["__typename"] == "Organization" else github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_vulnerabilities(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order: VulnerabilityOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Vulnerability]:
        """
        |aiter|

        Fetches individual vulnerabilities.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order: :class:`~github.VulnerabilityOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Vulnerability`
        """

        return github.Connection(
            self._http.collect_query_vulnerabilities,
            order.value if order is not MISSING else None,
            data_map=lambda d: github.Vulnerability._from_data(d),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    async def clear_status(
        self,
        /,
    ) -> None:
        """
        |coro|

        Clears the authenticated user's status.

        .. note::

            This mutation requires the following token scopes:

            - ``user``
        """

        await self._http.mutate_user_update_status(None, None, None, None, None)

    async def create_repository(
        self,
        /,
        name: str,
        *,
        description: str = MISSING,
        fields = MISSING,  # TODO
        visibility: RepositoryVisibility = MISSING,
    ) -> Repository:
        """
        |coro|

        Creates a repository on the authenticated user.


        Parameters
        ----------
        name: :class:`str`
            The name of the repository.
        description: :class:`str`
            The description of the repository.
        visibility: :class:`~github.RepositoryVisibility`
            The visibility of the repository.


        :rtype: :class:`~github.Repository`
        """

        _, repository_data = await self._http.mutate_repositoryowner_create_repository(
            None,
            name,
            visibility.value if visibility is not MISSING else github.RepositoryVisibility.public.value,
            description if description is not MISSING else None,
            repository_fields=fields,
        )

        return github.Repository._from_data(repository_data, http=self._http)

    async def update_status(
        self,
        /,
        message: str | None = MISSING,
        *,
        busy: bool = MISSING,
        emoji: str | None = MISSING,
        expires_at: DateTime = MISSING,
        organization: Organization = MISSING,
    ) -> UserStatus | None:
        """
        |coro|

        Updates the authenticated user's status.

        .. note::

            This mutation requires the following token scopes:

            - ``user``


        Parameters
        ----------
        message: :class:`str` | None
            The message to display on the status.
        busy: :class:`bool`
            Whether to mark the user as busy.
        emoji: :class:`str` | None
            The emoji to display on the status. This can either be a
            unicode emoji or its name with colons.
        expires_at: :class:`~datetime.datetime`
            The date and time at which to expire the status in UTC.
        organization: :class:`~github.Organization`
            The organization whose members will be allowed to see the
            status.


        :rtype: :class:`~github.UserStatus` | None
        """

        data = await self._http.mutate_user_update_status(
            busy if busy is not MISSING else False,
            emoji if emoji is not MISSING else None,
            github.utility.datetime_to_iso(expires_at) if expires_at is not MISSING else None,
            message if message is not MISSING else None,
            organization.id if organization is not MISSING else None,
        )

        if not data:
            return None

        return github.UserStatus._from_data(data, http=self._http)


__all__ = [
    "Client",
]
