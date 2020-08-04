# type: ignore

import os
import textwrap

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "pdf_template/__version__.py"), "r") as f:
    exec(f.read(), about)


setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    maintainer=about["__maintainer__"],
    maintainer_email=about["__maintainer_email__"],
    packages=["pdf_template",],
    url=about["__url__"],
    license=about["__license__"],
    description=about["__description__"],
    long_description=textwrap.dedent(open("README.md", "r").read()),
    long_description_content_type="text/markdown",
    install_requires=["dataclasses", "Pillow", "reportlab"],
    tests_require=["pytest"],
    test_suite="nose.collector",
    keywords=about["__keywords__"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Text Editors :: Word Processors",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
