from enum import Enum


class RepositoryOrderField(Enum):
    created_at: str
    name: str
    pushed_at: str
    stargazer_count: str
    updated_at: str
