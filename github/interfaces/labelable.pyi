from github.iterator import CollectionIterator
from github.enums import LabelOrderField
from github.objects import Label


class Labelable():
    def fetch_labels(self, *, order_by: LabelOrderField=..., **kwargs) -> CollectionIterator[Label]: ...
