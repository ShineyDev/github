from github.interfaces.actor import *
from github.interfaces.actor import __all__ as _actor__all__
from github.interfaces.announcementowner import *
from github.interfaces.announcementowner import __all__ as _announcementowner__all__
from github.interfaces.discussionauthor import *
from github.interfaces.discussionauthor import __all__ as _discussionauthor__all__
from github.interfaces.node import *
from github.interfaces.node import __all__ as _node__all__
from github.interfaces.packageowner import *
from github.interfaces.packageowner import __all__ as _packageowner__all__
from github.interfaces.profileowner import *
from github.interfaces.profileowner import __all__ as _profileowner__all__
from github.interfaces.repositoryowner import *
from github.interfaces.repositoryowner import __all__ as _repositoryowner__all__
from github.interfaces.resource import *
from github.interfaces.resource import __all__ as _resource__all__
from github.interfaces.sponsorable import *
from github.interfaces.sponsorable import __all__ as _sponsorable__all__
from github.interfaces.starrable import *
from github.interfaces.starrable import __all__ as _starrable__all__
from github.interfaces.subscribable import *
from github.interfaces.subscribable import __all__ as _subscribable__all__
from github.interfaces.type import *
from github.interfaces.type import __all__ as _type__all__


__all__: list[str] = [  # type: ignore[reportUnsupportedDunderAll]
    *_actor__all__,
    *_announcementowner__all__,
    *_discussionauthor__all__,
    *_node__all__,
    *_packageowner__all__,
    *_profileowner__all__,
    *_repositoryowner__all__,
    *_resource__all__,
    *_sponsorable__all__,
    *_starrable__all__,
    *_subscribable__all__,
    *_type__all__,
]
