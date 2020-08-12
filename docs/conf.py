"""
/docs/conf.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.abspath(".."))

# extensions configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "sphinx_rtd_theme",
]

autodoc_typehints = "none"

extlinks = {
    "issue": ("https://github.com/ShineyDev/github.py/issues/%s", "#")
}

intersphinx_mapping = {
    "aiohttp": ("https://aiohttp.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3", None),
}

# sphinx configuration

highlight_language = "python3"
html_experimental_html5_writer = True
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "includehidden": False,
    "prev_next_buttons_location": "top",
}
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

# project configuration

copyright = "2019-2020, ShineyDev"
project = "github.py"

with open("../github/__init__.py", "r") as file_stream:
    version = re.search(r"^__version__ = [\"]([^\"]*)[\"]", file_stream.read(), re.MULTILINE).group(1)

release = version

# reST configuration

rst_prolog = """

.. |aiter| replace:: This function returns an |aiter_link|_.
.. |aiter_link| replace:: *asynchronous iterator*
.. _aiter_link: https://docs.python.org/3/glossary.html#term-asynchronous-iterator

.. |coro| replace:: This function is a |coro_link|_.
.. |coro_link| replace:: *coroutine*
.. _coro_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""
