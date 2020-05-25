"""
/github/enums/__init__.py

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

import collections
import types


class EnumMeta(type):
    """
    The MIT License (MIT)

    Copyright (c) 2015-2019 Rapptz

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
    """

    def __new__(cls, name, bases, attrs):
        value_map = {}
        member_map = {}
        
        value_cls = collections.namedtuple("_EnumValue_" + name, "name value")
        value_cls.__repr__ = lambda self: "<{0} {2!r}>".format(name, self.name, self.value)
        value_cls.__str__ = lambda self: str(self.value)
        
        def _is_descriptor(obj):
            gsd = ("__get__", "__set__", "__delete__")
            return any([hasattr(obj, m) for m in gsd])

        for (key, value) in attrs.items():
            if isinstance(value, classmethod):
                continue

            is_descriptor = _is_descriptor(value)

            if key[0] == "_" and not is_descriptor:
                continue

            if is_descriptor:
                setattr(value_cls, key, value)
                del attrs[key]
                continue

            try:
                new_value = value_map[value]
            except (KeyError) as e:
                new_value = value_cls(name=key, value=value)
                value_map[value] = new_value

            member_map[key] = new_value
            attrs[key] = new_value

        attrs["_value_map_"] = value_map
        attrs["_member_map_"] = member_map

        actual_cls = super().__new__(cls, name, bases, attrs)
        value_cls._actual_cls_ = actual_cls
        return actual_cls

    def __iter__(cls):
        for (_, value) in cls._member_map_.items():
            yield value

    def __len__(cls):
        return len(cls._member_map_)

    def __repr__(cls):
        return "<enum {0}>".format(cls.__name__)

    def __setattr__(cls, key, value):
        raise TypeError("Enums are immutable.")

    def __delattr__(cls, key):
        raise TypeError("Enums are immutable.")

    def __instancecheck__(self, instance):
        # isinstance(x, y) -> __instancecheck__(y, x)
        
        try:
            return instance._actual_cls_ is self
        except (AttributeError) as e:
            return False

    @property
    def __members__(cls):
        return types.MappingProxyType(cls._member_map_)

class Enum(metaclass=EnumMeta):
    @classmethod
    def try_value(cls, value):
        try:
            return cls._value_map_[value]
        except (KeyError) as e:
            return value


from github.enums.cannotupdatereason import CannotUpdateReason
from github.enums.commentauthorassociation import CommentAuthorAssociation
from github.enums.issuestate import IssueState
from github.enums.lockreason import LockReason
from github.enums.projectcardstate import ProjectCardState
from github.enums.projectcolumnpurpose import ProjectColumnPurpose
from github.enums.projectstate import ProjectState
from github.enums.pullrequeststate import PullRequestState
from github.enums.reaction import Reaction
from github.enums.repositorylockreason import RepositoryLockReason
from github.enums.repositorypermissions import RepositoryPermissions
from github.enums.subscriptionstate import SubscriptionState

__all__ = [
    "CannotUpdateReason", "CommentAuthorAssociation", "IssueState",
    "LockReason", "ProjectCardState", "ProjectColumnPurpose", "ProjectState",
    "PullRequestState", "Reaction", "RepositoryLockReason",
    "RepositoryPermissions", "SubscriptionState",
]
