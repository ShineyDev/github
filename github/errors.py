"""
/github/errors.py

    Copyright (c) 2019 ShineyDev
    
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

class GitHubError(Exception):
    """
    The base Exception class for the wrapper. This could be used to
    catch all exceptions thrown by the wrapper.

    This exception is raised when GitHub returns arbitrary errors in
    the JSON response. The given error is the first error in the list.
    """

    pass

class HTTPException(GitHubError):
    """
    This exception is raised when a HTTP request operation fails.

    Attributes
    ----------
    response: :class:`aiohttp.ClientResponse`
        The response of the failed HTTP request.
    """

    def __init__(self, message, *, response):
        self.response = response
        super().__init__("{1.status}: {0}".format(message, response))

class Unauthorized(HTTPException):
    """
    This exception is raised when invalid credentials are passed.

    Subclass of :exc:`HTTPException`.
    """

    pass
