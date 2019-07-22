import re
import setuptools


with open("README.rst", "r") as file_stream:
    readme = file_stream.read()

with open("requirements.txt", "r") as file_stream:
    install_requires = file_stream.read().splitlines()

with open("github/__init__.py", "r") as file_stream:
    version = re.search(r"^__version__ = [\"]([^\"]*)[\"]$", file_stream.read()).group(1)

if not version:
    raise RuntimeError("version is unset")

if version.endswith(("a", "b", "rc")):
    # append version identifier based on commit count and current commit id

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

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Typing :: Typed",
]

extras_require = {
    "docs": [
        "sphinx",
    ],
}

project_urls = {
    #"Documentation": "...",
    "Issue Tracker": "https://github.com/ShineyDev/github.py/issues/",
    "Source": "https://github.com/ShineyDev/github.py/",
}

setuptools.setup(classifiers=classifiers,
                 description="A python wrapper for the GitHub API",
                 extras_require=extras_require,
                 install_requires=install_requires,
                 long_description=readme,
                 long_description_content_type="text/x-rst",
                 name="github.py",
                 packages=["github"],
                 project_urls=project_urls,
                 python_requires=">=3",
                 url="https://github.com/ShineyDev/github.py",
                 version=version)
