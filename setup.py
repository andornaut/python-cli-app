#!/usr/bin/env python

from distutils.core import setup


from cliapp import __app_name__, __description__, __version__

setup(
    name=__app_name__,
    description=__description__,
    version=__version__,
    author="andornaut",
    url="https://github.com/andornaut/python-cli-app",
    packages=["cliapp"],
    license="MIT",
    entry_points="""\
    [console_scripts]
    cliapp=cliapp.__main__:main
    """,
    install_requires=[
        "typer>=0.9.0",
    ],
)
