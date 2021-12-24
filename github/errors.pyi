import graphql


class ClientError(graphql.client.ClientError): pass


class ClientObjectMissingFieldError(AttributeError, ClientError):
    fields: tuple[str]


class ClientResponseError(graphql.client.ClientResponseError, ClientError): pass
class ClientResponseHTTPError(graphql.client.ClientResponseHTTPError, ClientResponseError): pass
class ClientResponseHTTPUnauthorizedError(ClientResponseHTTPError): pass
class ClientResponseGraphQLError(graphql.client.ClientResponseGraphQLError, ClientResponseError): pass
class ClientResponseGraphQLArgumentValueRangeExceededError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLForbiddenError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLInsufficientScopesError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLInternalError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLMaximumNodeLimitExceededError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLNotFoundError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLUnprocessableError(ClientResponseGraphQLError): pass

class ClientDeprecationWarning(graphql.client.ClientDeprecationWarning): pass
class ServerDeprecationWarning(graphql.client.ServerDeprecationWarning): pass
