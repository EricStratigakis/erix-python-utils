from os import getenv
from sys import exit

from setuptools import setup
from setuptools.command.install import install

# circleci.py version
VERSION = "1.1.1"

def readme():
    """print long description"""
    with open("README.md", "r") as fh:
        return fh.read()
class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = f"Git tag: {tag} does not match the version of this app: {VERSION}"
            exit(info)

setup(
    name="erix-python-utils",
    version="0.0.10",
    author="Eric Stratigakis",
    author_email="enstrati@uwaterloo.ca",
    description="All of my utilities and tools in one place",
    py_modules=["homebrew"],
    package_dir={"":"src"},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    python_requires='>=3',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)