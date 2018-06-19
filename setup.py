import codecs
import os
import re

from setuptools import setup

NAME = "pyramid-is-live"
META_PATH = "pyramid_is_live.py"
CLASSIFIERS = ["Private :: Do Not Upload"]

INSTALL_REQUIRES = ["pyramid"]


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """Extract __*meta*__ from META_FILE."""
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


VERSION = find_meta("version")


setup(
    name=NAME,
    version=VERSION,
    classifiers=CLASSIFIERS,
    py_modules=["pyramid_is_live"],
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
)
