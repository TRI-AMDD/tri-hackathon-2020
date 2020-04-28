# Copyright 2020 Toyota Research Institute

from setuptools import setup, find_packages

setup(
    name="tri_hackathon_2020",
    version="2020.4.28",
    packages=find_packages(),
    install_requires=[
        "camd @ git+https://github.com/TRI-AMDD/camd@dev#egg=camd"
    ],
    # TODO: make dev master
    # Enforce dev version of CAMD
    # dependency_links=[
    #     "git+https://github.com/TRI-AMDD/camd/tarball/dev#egg=camd"
    # ]
)
