import os
import re
import sys

sys.path.insert(0, os.path.abspath(".."))


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
    "issue": ("https://github.com/ShineyDev/github/issues/%s", "#"),
}

intersphinx_mapping = {
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "graphql": ("https://docs.shiney.dev/graphql/latest", None),
    "python": ("https://docs.python.org/3", None),
}

highlight_language = "python3"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "includehidden": False,
    "navigation_depth": -1,
    "prev_next_buttons_location": None,
    "titles_only": True,
}
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

copyright = "2019-present, ShineyDev"
project = "github"

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("../github/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass

release = version

rst_prolog = """

.. |aiter| replace:: This function returns an |aiter_link|_.
.. |aiter_link| replace:: asynchronous iterator
.. _aiter_link: https://docs.python.org/3/glossary.html#term-asynchronous-iterator

.. |coro| replace:: This function returns a |coro_link|_.
.. |coro_link| replace:: coroutine
.. _coro_link: https://docs.python.org/3/library/asyncio-task.html#coroutine

.. |PAT_link| replace:: personal access token
.. _PAT_link: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
"""
