import os
import re
import sys


sys.path.insert(0, os.path.abspath(".."))


author = "ShineyDev"
project = "github"

copyright = f"2019-present, {author}"

_version_regex = r"^version(?:\s*:\s*str)?\s*=\s*('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("../github/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

release = "v" + match.group(2)
version = release

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            release += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            release += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "sphinx_rtd_theme",
]

autodoc_member_order = "groupwise"
autodoc_typehints = "none"

extlinks = {
    "issue": (f"https://github.com/{author}/{project}/issues/%s", "#%s"),
}

intersphinx_mapping = {
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "graphql": ("https://docs.shiney.dev/graphql/latest", None),
    "python": ("https://docs.python.org/3", None),
}


highlight_language = "none"
pygments_style = "friendly"
root_doc = "index"
rst_prolog = """

.. |aiter| replace:: This function returns an |aiter_link|_.
.. |aiter_link| replace:: asynchronous iterator
.. _aiter_link: https://docs.python.org/3/glossary.html#term-asynchronous-iterator

.. |choosealicense| replace:: |choosealicense_link|_
.. |choosealicense_link| replace:: choose a license
.. _choosealicense_link: https://choosealicense.com/

.. |coro| replace:: This function returns a |coro_link|_.
.. |coro_link| replace:: coroutine
.. _coro_link: https://docs.python.org/3/library/asyncio-task.html#coroutine

.. |graphql_explorer| replace:: |graphql_explorer_link|_
.. |graphql_explorer_link| replace:: GitHub's GraphiQL Explorer
.. _graphql_explorer_link: https://graphql.github.com/explorer

.. |graphql_guides| replace:: |graphql_guides_link|_
.. |graphql_guides_link| replace:: GitHub's GraphQL guides
.. _graphql_guides_link: https://docs.github.com/en/graphql/guides

.. |graphql_learn| replace:: |graphql_learn_link|_
.. |graphql_learn_link| replace:: learn GraphQL
.. _graphql_learn_link: https://graphql.org/learn/

.. |graphql_reference| replace:: |graphql_reference_link|_
.. |graphql_reference_link| replace:: GitHub's GraphQL API reference
.. _graphql_reference_link: https://docs.github.com/en/graphql/reference

.. |pat| replace:: |pat_link|_
.. |pat_link| replace:: personal access token
.. _pat_link: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token

.. |spdx| replace:: |spdx_link|_
.. |spdx_link| replace:: SPDX
.. _spdx_link: https://spdx.dev/
"""
source_suffix = ".rst"


html_favicon = "favicon.svg"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "includehidden": False,
    "navigation_depth": -1,
    "prev_next_buttons_location": None,
    "titles_only": True,
}
html_title = f"{project} {version}"
