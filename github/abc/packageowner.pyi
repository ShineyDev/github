from typing import List

from github.iterator import CollectionIterator
from github.enums import PackageType
from github.objects import Package
from github.objects import Repository


class PackageOwner():
    def fetch_packages(
        self, *, names: List[str]=..., repository: Repository=..., type: PackageType=..., **kwargs
    ) -> CollectionIterator[Package]: ...
