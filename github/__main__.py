"""
/github/__main__.py

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

import argparse
import pkg_resources
import platform
import sys

import aiohttp

import github


def show_version():
    entries = list()

    if sys.version_info.releaselevel != "final":
        entries.append("- python: v{0.major}.{0.minor}.{0.micro}{0.releaselevel[0]}{0.serial}".format(sys.version_info))
    else:
        entries.append("- python: v{0.major}.{0.minor}.{0.micro}".format(sys.version_info))

    if github.version_info.releaselevel != "final":
        entries.append("- github.py: v{0.major}.{0.minor}.{0.micro}{0.releaselevel[0]}{0.serial}".format(github.version_info))

        pkg = pkg_resources.get_distribution("github.py")
        if pkg:
            entries.append("    - package: v{0}".format(pkg.version))
    else:
        entries.append("- github.py: v{0.major}.{0.minor}.{0.micro}".format(github.version_info))

    entries.append("- aiohttp: v{0.__version__}".format(aiohttp))
    entries.append("")
    entries.append("- system: {0.system} {0.version}".format(platform.uname()))

    print("\n".join(entries))

def main():
    parser = argparse.ArgumentParser(prog="github")
    parser.add_argument("-v", "--version", action="store_true", help="display version information")
    args = parser.parse_args()

    if args.version:
        show_version()

main()
