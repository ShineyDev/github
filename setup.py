import re
import setuptools


with open("requirements.txt", "r") as stream:
    install_requires = stream.read().splitlines()

with open("github/__init__.py", "r") as stream:
    version = re.search(r"^version = [\"]([^\"]*)[\"]", stream.read(), re.MULTILINE).group(1)

if version.endswith(("a", "b", "rc")):
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
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Typing :: Typed",
]

extras_require = {
    "docs": [
        "sphinx",
        "sphinxcontrib_trio",
        "sphinx-rtd-theme",
    ],
}

project_urls = {
    "Documentation": "https://githubpy.readthedocs.io/en/latest/",
    "Issue Tracker": "https://github.com/ShineyDev/github.py/issues/",
    "Source": "https://github.com/ShineyDev/github.py/",
}

setuptools.setup(
    author="ShineyDev",
    classifiers=classifiers,
    description="An asynchronous Python wrapper for the GitHub API, v4.",
    extras_require=extras_require,
    install_requires=install_requires,
    license="Apache Software License",
    name="github.py",
    packages=["github", "github.enums", "github.interfaces", "github.objects", "github.gql"],
    project_urls=project_urls,
    python_requires=">=3.6.0",
    url="https://github.com/ShineyDev/github.py",
    version=version,
)
