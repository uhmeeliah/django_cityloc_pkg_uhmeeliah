from setuptools import setup, find_packages
#install new package, generate distribution files
# put the contents of your README file into the long_description
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()
#that long_description line will hold the full content of the README.rst file

setup(
    long_description=long_description
)