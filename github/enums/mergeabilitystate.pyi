from enum import Enum


class MergeabilityState(Enum):
    conflicting: str
    mergeable: str
    unknown: str
