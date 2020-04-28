# Copyright 2020 Toyota Research Institute

from setuptools import setup, find_packages

setup(
    name="tri_hackathon_2020",
    version="2020.04.28",
    packages=find_packages(),
    install_requires=[
        "camd>=2020.3.24"
    ],
    # TODO: make dev master
    # Enforce dev version of CAMD
    dependency_links=[
        "http://github.com/TRI-AMDD/camd/tarball/dev#egg=qmpy"
    ]
)
