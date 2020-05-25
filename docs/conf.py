"""
/docs/conf.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.abspath(".."))

# extensions

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
]

autodoc_typehints = "none"

extlinks = {
    "issue": ("https://github.com/ShineyDev/github.py/issues/%s", "#")
}

intersphinx_mapping = {
    "aiohttp": ("https://aiohttp.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3", None),
}

# main config

highlight_language = "python3"
html_experimental_html5_writer = True
html_static_path = ["_static"]
html_theme = "basic"
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

# project information

copyright = "2019-2020, ShineyDev"
project = "github.py"

with open("../github/__init__.py", "r") as file_stream:
    version = re.search(r"^__version__ = [\"]([^\"]*)[\"]", file_stream.read(), re.MULTILINE).group(1)

release = version

# reST config

rst_prolog = """
.. |choosealicense| replace:: |choosealicense_link|_
.. |choosealicense_link| replace:: choosealicense.com
.. _choosealicense_link: https://choosealicense.com/

.. |coro| replace:: This function is a |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine

.. |examples_directory| replace:: |examples_directory_link|_
.. |examples_directory_link| replace:: examples directory
.. _examples_directory_link: https://github.com/ShineyDev/github.py/tree/master/examples

.. |spdx| replace:: |spdx_link|_
.. |spdx_link| replace:: spdx.org
.. _spdx_link: https://spdx.org/licenses/
"""

# dumb setup

def setup(app):
    app.add_stylesheet("css/style.css")
