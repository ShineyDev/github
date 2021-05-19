import graphql


class GitHubError(graphql.client.errors.ClientError): pass
class ClientResponseError(graphql.client.errors.ClientResponseError, GitHubError): pass
class ClientResponseHTTPError(graphql.client.errors.ClientResponseHTTPError, ClientResponseError): pass
class ClientResponseHTTPUnauthorizedError(ClientResponseHTTPError): pass
class ClientResponseGraphQLError(graphql.client.errors.ClientResponseGraphQLError, ClientResponseError): pass
class ClientResponseGraphQLForbiddenError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLInternalError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLNotFoundError(ClientResponseGraphQLError): pass
