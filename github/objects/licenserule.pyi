from github.abc import Type


class LicenseRule(Type):
    @property
    def description(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def label(self) -> str: ...
