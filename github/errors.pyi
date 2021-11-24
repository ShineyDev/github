import graphql


class ClientError(graphql.client.ClientError): pass

class ClientObjectMissingFieldError(AttributeError, ClientError):
    fields: tuple[str]

class ClientResponseError(graphql.client.ClientResponseError, ClientError): pass
class ClientResponseHTTPError(graphql.client.ClientResponseHTTPError, ClientResponseError): pass
class ClientResponseHTTPUnauthorizedError(ClientResponseHTTPError): pass
class ClientResponseGraphQLError(graphql.client.ClientResponseGraphQLError, ClientResponseError): pass
class ClientResponseGraphQLForbiddenError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLInternalError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLNotFoundError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLUnprocessableError(ClientResponseGraphQLError): pass
class ClientResponseGraphQLValidationError(ClientResponseGraphQLError): pass

class ClientDeprecationWarning(DeprecationWarning): pass
class ServerDeprecationWarning(DeprecationWarning): pass
