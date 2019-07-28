"""
/github/query/builder.py

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

import textwrap
import typing


class Builder():
    """
    A helper class for building a query.

    Parameters
    ----------
    name: Optional[:class:`str`]
        The name of the query.
    type: Optional[:class:`str`]
        The type of query to build, defaults to "query".

    Attributes
    ----------
    name: Optional[:class:`str`]
        The name of the query.
    type: :class:`str`
        The type of query to build.
    arguments: List[:class:`~github.query.QueryArgument`]
        A list of query arguments.
    collections: List[:class:`~github.query.Collection`]
        A list of query collections.
    fields: List[:class:`~github.query.Field`]
        A list of query fields.
    """

    __slots__ = ("name", "type", "_arguments", "_collections", "_fields")

    def __init__(self, *, name: str=None, type: str=None):
        self.name = name
        self.type = type or "query"

        self._arguments = list()
        self._collections = list()
        self._fields = list()

    @property
    def arguments(self) -> typing.List["QueryArgument"]:
        """
        A list of query arguments.

        Returns
        -------
        List[:class:`github.query.QueryArgument]
            A list of query arguments.
        """

        return self._arguments

    @property
    def collections(self) -> typing.List["Collection"]:
        """
        A list of collections.

        Returns
        -------
        List[:class:`github.query.Collection]
            A list of collections.
        """

        return self._collections

    @property
    def fields(self) -> typing.List["Field"]:
        """
        A list of fields.

        Returns
        -------
        List[:class:`github.query.Field]
            An list of fields.
        """

        return self._fields

    def build(self) -> str:
        """
        Builds the query.

        Returns
        -------
        :class:`str`
            The built query.
        """

        if not self._collections and not self._fields:
            raise RuntimeError("query missing fields or collections")

        if self.name:
            query = "{0.type} {0.name} ".format(self)
        else:
            query = "{0.type} ".format(self)

        if self._arguments:
            query += "("
            query += ", ".join([argument.build() for argument in self._arguments])
            query += ") "

        query += "{\n"

        # query fetch_user ($login: String!) {
        # 

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            query += "{0}\n".format(collection)

        # query fetch_user ($login: String!) {
        #   collection (arg: $arg) {
        #     ...
        #   }
        # 

        for (field) in self._fields:
            field = field.build()
            query += "  {0}\n".format(field)

        # query fetch_user ($login: String!) {
        #   collection (arg: $arg) {
        #     ...
        #   }
        #   alias: field
        # 

        query += "}"

        # query fetch_user ($login: String!) {
        #   collection (arg: $arg) {
        #     ...
        #   }
        #   alias: field
        # }

        return query

    def add_argument(self, argument: "QueryArgument"):
        """
        Adds an argument to the query.

        Parameters
        ----------
        argument: :class:`~github.query.QueryArgument`
            The argument to add.
        """

        self._arguments.append(argument)

    def add_collection(self, collection: "Collection"):
        """
        Adds a collection to the query.

        Parameters
        ----------
        argument: :class:`~github.query.Collection`
            The collection to add.
        """

        self._collections.append(collection)

    def add_field(self, field: "Field"):
        """
        Adds a field to the query.

        Parameters
        ----------
        argument: :class:`~github.query.Field`
            The field to add.
        """

        self._fields.append(field)

class Collection():
    """
    A helper class for building a collection.

    Parameters
    ----------
    name: :class:`str`
        The name of the collection.
    alias: Optional[:class:`str`]
        An alias for the collection.

    Attributes
    ----------
    name: :class:`str`
        The name of the collection.
    alias: Optional[:class:`str`]
        An alias for the collection.
    arguments: List[:class:`~github.query.CollectionArgument`]
        A list of collection arguments.
    collections: List[:class:`~github.query.Collection`]
        A list of query collections.
    fields: List[:class:`~github.query.Field`]
        A list of query fields.
    """
    
    __slots__ = ("name", "alias", "_arguments", "_collections", "_fields")

    def __init__(self, *, name: str, alias: str=None):
        self.name = name
        self.alias = alias

        self._arguments = list()
        self._collections = list()
        self._fields = list()

    @property
    def arguments(self) -> typing.List["CollectionArgument"]:
        """
        A list of collection arguments.

        Returns
        -------
        List[:class:`github.query.CollectionArgument]
            A list of collection arguments.
        """

        return self._arguments

    @property
    def collections(self) -> typing.List["Collection"]:
        """
        A list of collections.

        Returns
        -------
        List[:class:`github.query.Collection]
            A list of collections.
        """

        return self._collections

    @property
    def fields(self) -> typing.List["Field"]:
        """
        A list of fields.

        Returns
        -------
        List[:class:`github.query.Field]
            An list of fields.
        """

        return self._fields

    def build(self) -> str:
        """
        Builds the collection.

        Returns
        -------
        :class:`str`
            The built collection.
        """

        if not self._collections and not self._fields:
            raise RuntimeError("collection '{0.name}' missing fields or collections".format(self))

        if self.alias:
            query = "{0.alias}: {0.name} ".format(self)
        else:
            query = "{0.name} ".format(self)

        if self._arguments:
            query += "("
            query += ", ".join([argument.build() for argument in self._arguments])
            query += ") "

        query += "{\n"

        # collection (arg: $arg) {
        # 

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            query += "{0}\n".format(collection)

        # collection (arg: $arg) {
        #   collection (arg: $arg) {
        #     ...
        #   }
        # 

        for (field) in self._fields:
            field = field.build()
            query += "  {0}\n".format()

        # collection (arg: $arg) {
        #   collection (arg: $arg) {
        #     ...
        #   }
        #   alias: field
        # 

        query += "}"

        # collection (arg: $arg) {
        #   collection (arg: $arg) {
        #     ...
        #   }
        #   alias: field
        # }

        return query

    def add_argument(self, argument: "CollectionArgument"):
        """
        Adds an argument to the collection.

        Parameters
        ----------
        argument: :class:`~github.query.CollectionArgument`
            The argument to add.
        """

        self._arguments.append(argument)

    def add_collection(self, collection: "Collection"):
        """
        Adds a collection to the collection.

        Parameters
        ----------
        argument: :class:`~github.query.Collection`
            The collection to add.
        """

        self._collections.append(collection)

    def add_field(self, field: "Field"):
        """
        Adds a field to the collection.

        Parameters
        ----------
        argument: :class:`~github.query.Field`
            The field to add.
        """

        self._fields.append(field)

class CollectionArgument():
    """
    A helper class for building a collection argument.

    Parameters
    ----------
    name: :class:`str`
        The name of the collection argument.
    value: :class:`str`
        The value for the collection argument.

    Attributes
    ----------
    name: :class:`str`
        The name of the collection argument.
    value: :class:`str`
        The value for the collection argument.
    """

    __slots__ = ("name", "value")

    def __init__(self, *, name: str, value: str):
        self.name = name
        self.value = value

    def build(self) -> str:
        """
        Builds the collection argument.

        Returns
        -------
        :class:`str`
            The built collection argument.
        """

        return "{0.name}: {0.value}".format(self)

class Field():
    """
    A helper class for building a field.

    Parameters
    ----------
    name: :class:`str`
        The name of the field.
    alias: Optional[:class:`str`]
        An alias for the field.

    Attributes
    ----------
    name: :class:`str`
        The name of the field.
    alias: Optional[:class:`str`]
        An alias for the field.
    """

    __slots__ = ("name", "alias")

    def __init__(self, *, name: str, alias: str=None):
        self.name = name
        self.alias = alias

    def build(self) -> str:
        """
        Builds the field.

        Returns
        -------
        :class:`str`
            The built field.
        """

        if self.alias:
            return "{0.alias}: {0.name}".format(self)
        return "{0.name}".format(self)

class QueryArgument():
    """
    A helper class for building a query argument.

    Parameters
    ----------
    name: :class:`str`
        The name of the query argument.
    value: :class:`str`
        The value for the query argument.

    Attributes
    ----------
    name: :class:`str`
        The name of the query argument.
    value: :class:`str`
        The value for the query argument.
    """

    __slots__ = ("name", "type", "default")

    def __init__(self, *, name: str, type: str, default: str=None):
        self.name = name
        self.type = type
        self.default = default

    def build(self) -> str:
        """
        Builds the query argument.

        Returns
        -------
        :class:`str`
            The built query argument.
        """

        if self.default:
            return "{0.name}: {0.type}={0.default}".format(self)
        return "{0.name}: {0.type}".format(self)
