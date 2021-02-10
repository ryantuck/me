from setuptools import setup

setup(
    name="me",
    version="0.0.0",
    install_requires=["Click"],
    entry_points={"console_scripts": "me=me.cli:cli"},
)
