import collections


_VersionInfo = collections.namedtuple("_VersionInfo", "prime major minor micro release serial")

version = "1.0.0.0a"
version_info = _VersionInfo(1, 0, 0, 0, "alpha", 0)
