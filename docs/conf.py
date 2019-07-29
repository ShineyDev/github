"""
/docs/conf.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.abspath(".."))

# extensions

extensions = ["sphinx.ext.autodoc", "sphinx.ext.extlinks", "sphinx.ext.intersphinx", "sphinx.ext.napoleon"]

autodoc_typehints = "none"
extlinks = {"issue": ("https://github.com/ShineyDev/github.py/issues/%s", "#")}
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "aiohttp": ("https://aiohttp.readthedocs.io/en/stable/", None),
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

copyright = "2019, ShineyDev"
project = "github.py"

with open("../github/__init__.py", "r") as file_stream:
    version = re.search(r"^__version__ = [\"]([^\"]*)[\"]", file_stream.read(), re.MULTILINE).group(1)

release = version

# reST config

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

# dumb setup

def setup(app):
	app.add_stylesheet("css/style.css")
