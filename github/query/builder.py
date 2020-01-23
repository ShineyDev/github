"""
/github/query/builder.py

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

import textwrap
import typing


class Builder():
    """
    A helper class for building a query or mutation.

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
    """

    __slots__ = ("name", "type", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str=None, type: str=None):
        self.name = name
        self.type = type or "query"

        self._arguments = list()
        self._collections = list()
        self._fields = list()
        self._fragments = list()

    @classmethod
    def from_dict(cls, data: dict) -> "Builder":
        """
        Creates a :class:`~github.query.Builder` object from a dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to convert to a :class:`~github.query.Builder`.

        Returns
        -------
        :class:`~github.query.Builder`
            The builder object.
        """

        name = data.get("name", None)
        type = data["type"]

        builder = cls(name=name, type=type)
        
        arguments = data.get("arguments", list())
        for (argument) in arguments:
            argument = QueryArgument.from_dict(argument)
            builder.add_argument(argument)
        
        collections = data.get("collections", list())
        for (collection) in collections:
            collection = Collection.from_dict(collection)
            builder.add_collection(collection)
        
        fields = data.get("fields", list())
        for (field) in fields:
            field = Field.from_dict(field)
            builder.add_field(field)
        
        fragments = data.get("fragments", list())
        for (fragment) in fragments:
            fragment = Fragment.from_dict(fragment)
            builder.add_fragment(fragment)

        return builder

    @property
    def arguments(self) -> typing.List["QueryArgument"]:
        """
        A list of query arguments.

        Returns
        -------
        List[:class:`~github.query.QueryArgument`]
            A list of query arguments.
        """

        return self._arguments

    @property
    def collections(self) -> typing.List["Collection"]:
        """
        A list of collections.

        Returns
        -------
        List[:class:`~github.query.Collection`]
            A list of collections.
        """

        return self._collections

    @property
    def fields(self) -> typing.List["Field"]:
        """
        A list of fields.

        Returns
        -------
        List[:class:`~github.query.Field`]
            A list of fields.
        """

        return self._fields

    @property
    def fragments(self) -> typing.List["Fragment"]:
        """
        A list of fragments.

        Returns
        -------
        List[:class:`~github.query.Fragment`]
            A list of fragments.
        """

        return self._fragments

    def add_argument(self, argument: "QueryArgument"):
        """
        Adds an argument to the query.

        Parameters
        ----------
        argument: :class:`~github.query.QueryArgument`
            The argument to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Builder`
            ``self``, for fluent chaining.
        """

        if not isinstance(argument, QueryArgument):
            raise TypeError("argument should be of type QueryArgument")

        self._arguments.append(argument)
        return self

    def add_collection(self, collection: "Collection"):
        """
        Adds a collection to the query.

        Parameters
        ----------
        collection: :class:`~github.query.Collection`
            The collection to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Builder`
            ``self``, for fluent chaining.
        """

        if not isinstance(collection, Collection):
            raise TypeError("collection should be of type Collection")

        self._collections.append(collection)
        return self

    def add_field(self, field: "Field"):
        """
        Adds a field to the query.

        Parameters
        ----------
        field: :class:`~github.query.Field`
            The field to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Builder`
            ``self``, for fluent chaining.
        """

        if not isinstance(field, Field):
            raise TypeError("field should be of type Field")

        self._fields.append(field)
        return self

    def add_fragment(self, fragment: "Fragment"):
        """
        Adds a fragment to the query.

        Parameters
        ----------
        fragment: :class:`~github.query.Fragment`
            The fragment to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Builder`
            ``self``, for fluent chaining.
        """

        if not isinstance(fragment, Fragment):
            raise TypeError("fragment should be of type Fragment")

        self._fragments.append(fragment)
        return self

    def build(self) -> str:
        """
        Builds the query.

        Raises
        ------
        RuntimeError
            The query is missing collections or fields.

        Returns
        -------
        :class:`str`
            The built query.
        """

        if not self._collections and not self._fields:
            raise RuntimeError("query is missing collections or fields")

        if self.name is not None:
            query = "{0.type} {0.name} ".format(self)
        else:
            query = "{0.type} ".format(self)

        if self._arguments:
            query += "("
            query += ", ".join([argument.build() for argument in self._arguments])
            query += ") "

        query += "{\n"

        # TYPE NAME ($NAME: TYPE=DEFAULT) {
        # 

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            query += "{0}\n".format(collection)

        # TYPE NAME ($NAME: TYPE=DEFAULT) {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        # 

        for (field) in self._fields:
            field = field.build()
            query += "  {0}\n".format(field)

        # TYPE NAME ($NAME: TYPE=DEFAULT) {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # 

        query += "}"

        # TYPE NAME ($NAME: TYPE=DEFAULT) {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # }

        for (fragment) in self._fragments:
            fragment = fragment.build()
            query += "\n\n"
            query += fragment

        # TYPE NAME ($NAME: TYPE=DEFAULT) {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # }
        # 
        # fragment NAME on TYPE {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # }

        return query

    def copy(self) -> "Builder":
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~github.query.Builder`
            The new object.
        """

        return Builder.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        """
        Creates a dict object from this :class:`~github.query.Builder`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        if self.name is not None:
            data["name"] = self.name

        data["type"] = self.type

        if self._arguments:
            data["arguments"] = [a.to_dict() for a in self._arguments]

        if self._collections:
            data["collections"] = [c.to_dict() for c in self._collections]

        if self._fields:
            data["fields"] = [f.to_dict() for f in self._fields]

        if self._fragments:
            data["fragments"] = [f.to_dict() for f in self._fragments]

        return data

class Query(Builder):
    """
    A helper class for building a query.

    Parameters
    ----------
    name: Optional[:class:`str`]
        The name of the query.

    Attributes
    ----------
    name: Optional[:class:`str`]
        The name of the query.
    type: :class:`str`
        The type of query to build.
    """

    __slots__ = ("name", "type", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str=None):
        super().__init__(name=name, type="query")

class Mutation(Builder):
    """
    A helper class for building a mutation.

    Parameters
    ----------
    name: Optional[:class:`str`]
        The name of the query.

    Attributes
    ----------
    name: Optional[:class:`str`]
        The name of the query.
    type: :class:`str`
        The type of query to build.
    """

    __slots__ = ("name", "type", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str=None):
        super().__init__(name=name, type="mutation")

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
    """
    
    __slots__ = ("name", "alias", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str, alias: str=None):
        self.name = name
        self.alias = alias

        self._arguments = list()
        self._collections = list()
        self._fields = list()
        self._fragments = list()

    @classmethod
    def from_dict(cls, data: dict) -> "Collection":
        """
        Creates a :class:`~github.query.Collection` object from a dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to convert to a
            :class:`~github.query.Collection`.

        Returns
        -------
        :class:`~github.query.Collection`
            The collection object.
        """

        name = data["name"]
        alias = data.get("alias", None)

        collection = cls(name=name, alias=alias)
        
        arguments = data.get("arguments", list())
        for (argument) in arguments:
            argument = CollectionArgument.from_dict(argument)
            collection.add_argument(argument)
        
        collections = data.get("collections", list())
        for (collection) in collections:
            collection = Collection.from_dict(collection)
            collection.add_collection(collection)
        
        fields = data.get("fields", list())
        for (field) in fields:
            field = Field.from_dict(field)
            collection.add_field(field)

        fragments = data.get("fragments", list())
        for (fragment) in fragments:
            fragment = Fragment.from_dict(fragment)
            collection.add_fragment(fragment)

        return collection

    @property
    def arguments(self) -> typing.List["CollectionArgument"]:
        """
        A list of collection arguments.

        Returns
        -------
        List[:class:`~github.query.CollectionArgument`]
            A list of collection arguments.
        """

        return self._arguments

    @property
    def collections(self) -> typing.List["Collection"]:
        """
        A list of collections.

        Returns
        -------
        List[:class:`~github.query.Collection`]
            A list of collections.
        """

        return self._collections

    @property
    def fields(self) -> typing.List["Field"]:
        """
        A list of fields.

        Returns
        -------
        List[:class:`~github.query.Field`]
            A list of fields.
        """

        return self._fields

    @property
    def fragments(self) -> typing.List["Fragment"]:
        """
        A list of fragments.

        Returns
        -------
        List[:class:`~github.query.Fragment`]
            A list of fragments.
        """

        return self._fragments

    def add_argument(self, argument: "CollectionArgument"):
        """
        Adds an argument to the collection.

        Parameters
        ----------
        argument: :class:`~github.query.CollectionArgument`
            The argument to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Collection`
            ``self``, for fluent chaining.
        """

        if not isinstance(argument, CollectionArgument):
            raise TypeError("argument should be of type CollectionArgument")

        self._arguments.append(argument)
        return self

    def add_collection(self, collection: "Collection"):
        """
        Adds a collection to the collection.

        .. warning::
            
            When passing ``self`` into this method a copy is made to
            prevent recursion in :meth:`.build`.

        Parameters
        ----------
        collection: :class:`~github.query.Collection`
            The collection to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Collection`
            ``self``, for fluent chaining.
        """

        if not isinstance(collection, Collection):
            raise TypeError("collection should be of type Collection")

        if collection is self:
            # prevent recursion
            collection = collection.copy()

        self._collections.append(collection)
        return self

    def add_field(self, field: "Field"):
        """
        Adds a field to the collection.

        Parameters
        ----------
        field: :class:`~github.query.Field`
            The field to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Collection`
            ``self``, for fluent chaining.
        """

        if not isinstance(field, Field):
            raise TypeError("field should be of type Field")

        self._fields.append(field)
        return self

    def add_fragment(self, fragment: "Fragment"):
        """
        Adds a fragment to the collection.

        Parameters
        ----------
        fragment: :class:`~github.query.Fragment`
            The fragment to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Collection`
            ``self``, for fluent chaining.
        """

        if not isinstance(fragment, Fragment):
            raise TypeError("fragment should be of type Fragment")

        self._fragments.append(fragment)
        return self

    def build(self) -> str:
        """
        Builds the collection.

        Raises
        ------
        RuntimeError
            The collection is missing collections, fields or fragments.

        Returns
        -------
        :class:`str`
            The built collection.
        """

        if not self._collections and not self._fields and not self._fragments:
            raise RuntimeError("collection '{0.name}' is missing collections, fields or fragments".format(self))

        if self.alias is not None:
            collection = "{0.alias}: {0.name} ".format(self)
        else:
            collection = "{0.name} ".format(self)

        if self._arguments:
            collection += "("
            collection += ", ".join([argument.build() for argument in self._arguments])
            collection += ") "

        collection += "{\n"

        # ALIAS: NAME (NAME: VALUE) {
        # 

        for (fragment) in self._fragments:
            if fragment.inline:
                fragment = fragment.build_inline()
                fragment = textwrap.indent(fragment, "  ")
                collection += "{0}\n".format(fragment)
            else:
                fragment = "... {0.name}".format(fragment)
                collection += "  {0}\n".format(fragment)

        # ALIAS: NAME (NAME: VALUE) {
        #   ... NAME on TYPE {
        #     (continues in fragment)
        #   }
        # 
        # or
        # 
        # ALIAS: NAME (NAME: VALUE) {
        #   ... NAME
        # 

        for (collection_) in self._collections:
            collection_ = collection_.build()
            collection_ = textwrap.indent(collection_, "  ")
            collection += "{0}\n".format(collection_)

        # ALIAS: NAME (NAME: VALUE) {
        #   ... NAME
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues recursively)
        #   }
        # 

        for (field) in self._fields:
            field = field.build()
            collection += "  {0}\n".format(field)

        # ALIAS: NAME (NAME: VALUE) {
        #   ... NAME
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues recursively)
        #   }
        #   ALIAS: NAME
        # 

        collection += "}"

        # ALIAS: NAME (NAME: VALUE) {
        #   ... NAME
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues recursively)
        #   }
        #   ALIAS: NAME
        # }

        return collection

    def copy(self) -> "Collection":
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~github.query.Collection`
            The new object.
        """

        return Collection.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        """
        Creates a dict object from this
        :class:`~github.query.Collection`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        data["name"] = self.name

        if self.alias is not None:
            data["alias"] = self.alias

        if self._arguments:
            data["arguments"] = [a.to_dict() for a in self._arguments]

        if self._collections:
            data["collections"] = [c.to_dict() for c in self._collections]

        if self._fields:
            data["fields"] = [f.to_dict() for f in self._fields]

        if self._fragments:
            data["fragments"] = [f.to_dict() for f in self._fragments]

        return data

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

    @classmethod
    def from_dict(cls, data: dict) -> "CollectionArgument":
        """
        Creates a :class:`~github.query.CollectionArgument` object from
        a dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to convert to a
            :class:`~github.query.CollectionArgument`.

        Returns
        -------
        :class:`~github.query.CollectionArgument`
            The collection argument object.
        """

        name = data["name"]
        value = data["value"]

        argument = cls(name=name, value=value)
        return argument

    def build(self) -> str:
        """
        Builds the collection argument.

        Returns
        -------
        :class:`str`
            The built collection argument.
        """

        argument = "{0.name}: {0.value}".format(self)
        return argument

    def copy(self) -> "CollectionArgument":
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~github.query.CollectionArgument`
            The new object.
        """

        return CollectionArgument.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        """
        Creates a dict object from this
        :class:`~github.query.CollectionArgument`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        data["name"] = self.name
        data["value"] = self.value

        return data

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

    @classmethod
    def from_dict(cls, data: dict) -> "Field":
        """
        Creates a :class:`~github.query.Field` object from a dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to convert into a :class:`~github.query.Field`.

        Returns
        -------
        :class:`~github.query.Field`
            The field object.
        """

        name = data["name"]
        alias = data.get("alias", None)

        field = cls(name=name, alias=alias)
        return field

    def build(self) -> str:
        """
        Builds the field.

        Returns
        -------
        :class:`str`
            The built field.
        """

        if self.alias is not None:
            field = "{0.alias}: {0.name}".format(self)
        else:
            field = "{0.name}".format(self)

        return field

    def copy(self) -> "Field":
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~github.query.Field`
            The new object.
        """

        return Field.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        """
        Creates a dict object from this :class:`~github.query.Field`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        data["name"] = self.name

        if self.alias is not None:
            data["alias"] = self.alias

        return data

class Fragment():
    """
    A helper class for building a fragment.

    Parameters
    ----------
    name: :class:`str`
        The name of the fragment.
    type: :class:`str`
        The type for the fragment.

    Attributes
    ----------
    name: :class:`str`
        The name of the fragment.
    type: :class:`str`
        The type for the fragment.
    """

    __slots__ = ("name", "type", "inline", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str, type: str, inline: bool=True):
        self.name = name
        self.type = type
        self.inline = inline

        self._collections = list()
        self._fields = list()
        self._fragments = list()

    @classmethod
    def from_dict(cls, data: dict) -> "Fragment":
        """
        Creates a :class:`~github.query.Fragment` object from a dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to convert to a :class:`~github.query.Fragment`.

        Returns
        -------
        :class:`~github.query.Fragment`
            The fragment object.
        """

        name = data["name"]
        type = data["type"]
        inline = data["inline"]

        fragment = cls(name=name, type=type, inline=inline)
        
        collections = data.get("collections", list())
        for (collection) in collections:
            collection = Collection.from_dict(collection)
            fragment.add_collection(collection)
        
        fields = data.get("fields", list())
        for (field) in fields:
            field = Field.from_dict(field)
            fragment.add_field(field)
        
        fragments = data.get("fragments", list())
        for (fragment_) in fragments:
            fragment_ = Fragment.from_dict(fragment_)
            fragment.add_fragment(fragment_)

        return fragment

    @property
    def collections(self) -> typing.List[Collection]:
        """
        A list of collections.

        Returns
        -------
        List[:class:`~github.query.Collection`]
            A list of collections.
        """

        return self._collections

    @property
    def fields(self) -> typing.List[Field]:
        """
        A list of fields.

        Returns
        -------
        List[:class:`~github.query.Field`]
            A list of fields.
        """

        return self._fields

    @property
    def fragments(self) -> typing.List["Fragment"]:
        """
        A list of fragments.

        Returns
        -------
        List[:class:`~github.query.Fragment`]
            A list of fragments.
        """

        return self._fragments

    def add_collection(self, collection: Collection):
        """
        Adds a collection to the fragment.

        Parameters
        ----------
        collection: :class:`~github.query.Collection`
            The collection to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Fragment`
            ``self``, for fluent chaining.
        """

        if not isinstance(collection, Collection):
            raise TypeError("collection should be of type Collection")

        self._collections.append(collection)
        return self

    def add_field(self, field: Field):
        """
        Adds a field to the fragment.

        Parameters
        ----------
        field: :class:`~github.query.Field`
            The field to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Fragment`
            ``self``, for fluent chaining.
        """

        if not isinstance(field, Field):
            raise TypeError("field should be of type Field")

        self._fields.append(field)
        return self

    def add_fragment(self, fragment: "Fragment"):
        """
        Adds a fragment to the fragment.

        .. warning::
            
            When passing ``self`` into this method a copy is made to
            prevent recursion in :meth:`.build`.

        Parameters
        ----------
        fragment: :class:`~github.query.Fragment`
            The fragment to add.

        Raises
        ------
        TypeError
            Invalid type was passed.

        Returns
        -------
        :class:`~github.query.Fragment`
            ``self``, for fluent chaining.
        """

        if not isinstance(fragment, Fragment):
            raise TypeError("fragment should be of type Fragment")

        if fragment is self:
            # prevent recursion
            fragment = fragment.copy()

        self._fragments.append(fragment)
        return self

    def build(self) -> str:
        """
        Builds the fragment.

        Raises
        ------
        RuntimeError
            The fragment is missing collections, fields or fragments.

        Returns
        -------
        :class:`str`
            The built fragment.
        """

        if not self._collections and not self._fields and not self._fragments:
            raise RuntimeError("fragment {0.name} is missing collections, fields or fragments".format(self))

        fragment = "fragment {0.name} on {0.type} ".format(self)
        fragment += "{\n"

        # fragment NAME on TYPE {
        # 

        for (fragment_) in self._fragments:
            fragment_ = fragment_.build_inline()
            fragment_ = textwrap.indent(fragment_, "  ")
            fragment += "{0}\n".format(fragment_)

        # fragment NAME on TYPE {
        #   ... on TYPE {
        #     ALIAS: NAME (NAME: VALUE) {
        #       (continues in collection)
        #     }
        #     ALIAS: NAME
        #   }
        # 

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            fragment += "{0}\n".format(collection)

        # fragment NAME on TYPE {
        #   ... on TYPE {
        #     ALIAS: NAME (NAME: VALUE) {
        #       (continues in collection)
        #     }
        #     ALIAS: NAME
        #   }
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        # 

        for (field) in self._fields:
            field = field.build()
            fragment += "  {0}\n".format(field)

        # fragment NAME on TYPE {
        #   ... on TYPE {
        #     ALIAS: NAME (NAME: VALUE) {
        #       (continues in collection)
        #     }
        #     ALIAS: NAME
        #   }
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # 

        fragment += "}"

        # fragment NAME on TYPE {
        #   ... on TYPE {
        #     ALIAS: NAME (NAME: VALUE) {
        #       (continues in collection)
        #     }
        #     ALIAS: NAME
        #   }
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # }

        return fragment

    def build_inline(self) -> str:
        """
        Builds the fragment as an inline fragment.

        Raises
        ------
        RuntimeError
            The fragment is missing collections or fields or you
            attempted to nest an inline fragment.

        Returns
        -------
        :class:`str`
            The built fragment.
        """

        if self._fragments:
            raise RuntimeError("inline fragments cannot be nested")

        if not self._collections and not self._fields:
            raise RuntimeError("fragment {0.name} is missing collections or fields".format(self))

        fragment = "... on {0.type} ".format(self)
        fragment += "{\n"

        # ... on TYPE {
        # 

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            fragment += "{0}\n".format(collection)

        # ... on TYPE {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        # 

        for (field) in self._fields:
            field = field.build()
            fragment += "  {0}\n".format(field)

        # ... on TYPE {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # 

        fragment += "}"

        # ... on TYPE {
        #   ALIAS: NAME (NAME: VALUE) {
        #     (continues in collection)
        #   }
        #   ALIAS: NAME
        # }

        return fragment

    def copy(self) -> "Fragment":
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~github.query.Fragment`
            The new object.
        """

        return Fragment.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        """
        Creates a dict object from this
        :class:`~github.query.Fragment`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        data["name"] = self.name
        data["type"] = self.type
        data["inline"] = self.inline

        if self._collections:
            data["collections"] = [c.to_dict() for c in self._collections]

        if self._fields:
            data["fields"] = [f.to_dict() for f in self._fields]

        if self._fragments:
            data["fragments"] = [f.to_dict() for f in self._fragments]

        return data

class QueryArgument():
    """
    A helper class for building a query argument.

    Parameters
    ----------
    name: :class:`str`
        The name of the query argument.
    type: :class:`str`
        The type for the query argument.
    default: Optional[:class:`str`]
        The default for the query argument.

    Attributes
    ----------
    name: :class:`str`
        The name of the query argument.
    type: :class:`str`
        The type for the query argument.
    default: Optional[:class:`str`]
        The default for the query argument.
    """

    __slots__ = ("name", "type", "default")

    def __init__(self, *, name: str, type: str, default: str=None):
        self.name = name
        self.type = type
        self.default = default

    @classmethod
    def from_dict(cls, data: dict) -> "QueryArgument":
        """
        Creates a :class:`~github.query.QueryArgument` object from a
        dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to convert to a
            :class:`~github.query.QueryArgument`.

        Returns
        -------
        :class:`~github.query.QueryArgument`
            The query argument object.
        """

        name = data["name"]
        type = data["type"]
        default = data.get("default", None)

        argument = cls(name=name, type=type, default=default)
        return argument

    def build(self) -> str:
        """
        Builds the query argument.

        Returns
        -------
        :class:`str`
            The built query argument.
        """

        if self.default is not None:
            argument = "{0.name}: {0.type}={0.default}".format(self)
        else:
            argument = "{0.name}: {0.type}".format(self)

        return argument

    def copy(self) -> "QueryArgument":
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~github.query.QueryArgument`
            The new object.
        """

        return QueryArgument.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        """
        Creates a dict object from this
        :class:`~github.query.QueryArgument`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        data["name"] = self.name
        data["value"] = self.value

        if self.default is not None:
            data["default"] = self.default

        return data
