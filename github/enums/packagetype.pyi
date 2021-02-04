from enum import Enum


class PackageType(Enum):
    debian: str
    docker: str
    maven: str
    npm: str
    nuget: str
    python: str
    rubygems: str
