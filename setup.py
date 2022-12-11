from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = "Lightweight NLP preprocessing package for Arabic language"

# Setting up
setup(
    name = "fathah",
    version = VERSION,
    author = "Abdul Fathah KA",
    author_email = "fathah@ziqx.in",
    description = DESCRIPTION,
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/fathah/fathah_python",
    classifiers = ["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
    keywords=['nlp', 'fathah', 'arabic'],
    packages = find_packages()
    )

